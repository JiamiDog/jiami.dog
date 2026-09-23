#!/usr/bin/env python3
"""Mirror every public WordPress post from jiami.dog into this repository.

The script deliberately uses the public posts collection only. It validates the
complete paginated snapshot before touching local files, converts rendered HTML
to GitHub Markdown, and requires two consecutive complete snapshots to omit an
existing post before deleting its mirror.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import date, datetime
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from importlib.metadata import PackageNotFoundError, version as package_version
from pathlib import Path, PurePosixPath
from typing import Any, Callable, Iterable, Mapping, Sequence

from markdownify import markdownify as markdownify_html


WP_POSTS_ENDPOINT = "https://jiami.dog/wp-json/wp/v2/posts"
PER_PAGE = 100
EXPECTED_MARKDOWNIFY_VERSION = "1.2.3"
README_START = "<!-- AUTO:ARTICLES:START -->"
README_END = "<!-- AUTO:ARTICLES:END -->"
MAX_RESPONSE_BYTES = 64 * 1024 * 1024
MAX_ARTICLE_BYTES = 8 * 1024 * 1024
MAX_FETCH_ATTEMPTS = 3


class SyncError(RuntimeError):
    """Raised when a remote snapshot or generated output is incomplete or unsafe."""


@dataclass(frozen=True)
class SourceSnapshot:
    total: int
    total_pages: int
    source_ids: tuple[str, ...]


@dataclass(frozen=True)
class Article:
    source_id: str
    title: str
    slug: str
    canonical_url: str
    published_at: str
    published_at_gmt: str
    modified_at: str
    modified_at_gmt: str
    excerpt: str
    body: str
    tags: tuple[str, ...]
    categories: tuple[str, ...]
    featured_image_url: str
    featured_image_alt: str
    relative_path: PurePosixPath
    body_sha256: str


class _PlainTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        self.parts.append(data)


class _IframeLinkPreprocessor(HTMLParser):
    """Replace iframes with ordinary titled links while preserving other HTML."""

    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=False)
        self.base_url = base_url
        self.parts: list[str] = []
        self.iframe_depth = 0

    def _iframe_link(self, attrs: Sequence[tuple[str, str | None]]) -> str:
        attributes = {key.lower(): value or "" for key, value in attrs}
        source = attributes.get("src", "").strip()
        resolved = urllib.parse.urljoin(self.base_url, source)
        parsed = urllib.parse.urlparse(resolved)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            return ""
        title = (
            attributes.get("title")
            or attributes.get("aria-label")
            or attributes.get("data-title")
            or parsed.hostname
            or "嵌入内容"
        )
        title = re.sub(r"\s+", " ", _plain_text(title)).strip() or "嵌入内容"
        return (
            '<p><a href="'
            + html.escape(resolved, quote=True)
            + '">'
            + html.escape(title)
            + "</a></p>"
        )

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "iframe":
            if self.iframe_depth == 0:
                self.parts.append(self._iframe_link(attrs))
            self.iframe_depth += 1
        elif self.iframe_depth == 0:
            self.parts.append(self.get_starttag_text())

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "iframe":
            if self.iframe_depth == 0:
                self.parts.append(self._iframe_link(attrs))
        elif self.iframe_depth == 0:
            self.parts.append(self.get_starttag_text())

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "iframe":
            if self.iframe_depth:
                self.iframe_depth -= 1
        elif self.iframe_depth == 0:
            self.parts.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if self.iframe_depth == 0:
            self.parts.append(data)

    def handle_entityref(self, name: str) -> None:
        if self.iframe_depth == 0:
            self.parts.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        if self.iframe_depth == 0:
            self.parts.append(f"&#{name};")

    def handle_comment(self, data: str) -> None:
        if self.iframe_depth == 0:
            self.parts.append(f"<!--{data}-->")


def _plain_text(value: Any) -> str:
    if isinstance(value, Mapping):
        value = value.get("rendered", value.get("raw", ""))
    if value is None:
        return ""
    parser = _PlainTextParser()
    parser.feed(str(value))
    parser.close()
    return html.unescape("".join(parser.parts))


def _single_line(value: Any, *, field: str) -> str:
    text = re.sub(r"\s+", " ", _plain_text(value).replace("\r", " ").replace("\n", " ")).strip()
    if not text:
        raise SyncError(f"Published post is missing {field}.")
    return text


def _normalize_datetime(value: Any, *, field: str, append_utc: bool = False) -> tuple[str, date]:
    text = _single_line(value, field=field)
    candidate = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed_date = date.fromisoformat(candidate) if len(candidate) == 10 else datetime.fromisoformat(candidate).date()
    except ValueError as exc:
        raise SyncError(f"Invalid {field}: {text!r}") from exc
    has_explicit_zone = text.endswith("Z") or bool(re.search(r"[+-]\d{2}:\d{2}$", text))
    normalized = text + "Z" if append_utc and "T" in text and not has_explicit_zone else text
    return normalized, parsed_date


def _safe_id(value: Any) -> str:
    text = _single_line(value, field="stable source ID")
    if not re.fullmatch(r"[0-9]+", text):
        raise SyncError(f"WordPress post ID must be numeric: {text!r}")
    return text


def _slugify(value: Any, *, fallback: str) -> str:
    raw = _plain_text(value).strip() or fallback
    ascii_text = raw.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return (slug or fallback)[:100].strip("-")


def _validate_canonical_url(value: Any) -> str:
    url = _single_line(value, field="canonical URL")
    parsed = urllib.parse.urlparse(url)
    hostname = (parsed.hostname or "").rstrip(".").lower()
    if parsed.scheme != "https" or hostname not in {"jiami.dog", "www.jiami.dog"}:
        raise SyncError(f"Canonical URL is outside jiami.dog HTTPS: {url!r}")
    if parsed.username or parsed.password:
        raise SyncError("Canonical URL must not contain credentials.")
    return url


def _safe_media_url(value: Any, *, base_url: str) -> str:
    if not value:
        return ""
    url = urllib.parse.urljoin(base_url, str(value).strip())
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc or parsed.username or parsed.password:
        return ""
    return url


def _drop_active_html(html_text: str) -> str:
    return re.sub(
        r"<(script|style|noscript)\b[^>]*>.*?</\1\s*>",
        "",
        html_text,
        flags=re.IGNORECASE | re.DOTALL,
    )


def preprocess_iframes(rendered_html: str, *, canonical_url: str) -> str:
    parser = _IframeLinkPreprocessor(canonical_url)
    parser.feed(_drop_active_html(rendered_html))
    parser.close()
    return "".join(parser.parts)


def html_to_markdown(rendered_html: str, *, canonical_url: str) -> str:
    if len(rendered_html.encode("utf-8")) > MAX_ARTICLE_BYTES:
        raise SyncError("Rendered WordPress content exceeds the 8 MiB safety limit.")
    prepared = preprocess_iframes(rendered_html, canonical_url=canonical_url)
    markdown = markdownify_html(
        prepared,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "noscript"],
        table_infer_header=True,
    )
    markdown = markdown.replace("\r\n", "\n").replace("\r", "\n")
    markdown = re.sub(r"[ \t]+\n", "\n", markdown)
    markdown = re.sub(r"\n{4,}", "\n\n\n", markdown).strip()
    if not markdown:
        markdown = "_原文没有可转换的正文内容，请查看官网原文。_"
    return markdown + "\n"


def _normalize_terms(value: Iterable[Any]) -> tuple[str, ...]:
    names: set[str] = set()
    for item in value:
        if not isinstance(item, Mapping):
            continue
        name = re.sub(r"\s+", " ", _plain_text(item.get("name", ""))).strip()
        if name:
            names.add(name)
    return tuple(sorted(names, key=str.casefold))


def extract_terms(post: Mapping[str, Any]) -> tuple[tuple[str, ...], tuple[str, ...]]:
    embedded = post.get("_embedded")
    groups = embedded.get("wp:term", []) if isinstance(embedded, Mapping) else []
    categories: list[Mapping[str, Any]] = []
    tags: list[Mapping[str, Any]] = []
    if isinstance(groups, list):
        for group in groups:
            if not isinstance(group, list):
                continue
            for term in group:
                if not isinstance(term, Mapping):
                    continue
                if str(term.get("taxonomy", "")) == "category":
                    categories.append(term)
                elif str(term.get("taxonomy", "")) == "post_tag":
                    tags.append(term)
    return _normalize_terms(categories), _normalize_terms(tags)


def extract_featured_image(post: Mapping[str, Any], *, canonical_url: str) -> tuple[str, str]:
    embedded = post.get("_embedded")
    media_items = embedded.get("wp:featuredmedia", []) if isinstance(embedded, Mapping) else []
    media = media_items[0] if isinstance(media_items, list) and media_items else None
    if not isinstance(media, Mapping):
        fallback = _safe_media_url(post.get("jetpack_featured_media_url"), base_url=canonical_url)
        return fallback, ""
    source_url = _safe_media_url(media.get("source_url"), base_url=canonical_url)
    if not source_url:
        details = media.get("media_details")
        sizes = details.get("sizes") if isinstance(details, Mapping) else None
        full = sizes.get("full") if isinstance(sizes, Mapping) else None
        if isinstance(full, Mapping):
            source_url = _safe_media_url(full.get("source_url"), base_url=canonical_url)
    alt = re.sub(r"\s+", " ", _plain_text(media.get("alt_text", ""))).strip()
    if not alt:
        alt = re.sub(r"\s+", " ", _plain_text(media.get("title", ""))).strip()
    return source_url, alt


def normalize_post(post: Mapping[str, Any]) -> Article:
    if str(post.get("status", "")) != "publish":
        raise SyncError(f"Non-published record reached normalizer: {post.get('id')!r}")
    if str(post.get("type", "")) != "post":
        raise SyncError(f"Non-post record reached normalizer: {post.get('id')!r}")
    content = post.get("content")
    if not isinstance(content, Mapping):
        raise SyncError(f"Post {post.get('id')!r} has no content object.")
    if bool(content.get("protected")):
        raise SyncError(f"Post {post.get('id')!r} is password-protected and cannot be mirrored.")

    source_id = _safe_id(post.get("id"))
    title = _single_line(post.get("title"), field="title")
    canonical_url = _validate_canonical_url(post.get("link"))
    published_at, published_date = _normalize_datetime(post.get("date"), field="published date")
    published_at_gmt = _normalize_datetime(post.get("date_gmt"), field="published GMT date", append_utc=True)[0]
    modified_at = _normalize_datetime(post.get("modified", post.get("date")), field="modified date")[0]
    modified_at_gmt = _normalize_datetime(
        post.get("modified_gmt", post.get("date_gmt")), field="modified GMT date", append_utc=True
    )[0]
    slug = _slugify(post.get("slug"), fallback=f"post-{source_id}")
    rendered_html = content.get("rendered", "")
    if not isinstance(rendered_html, str):
        raise SyncError(f"Post {source_id} content.rendered is not text.")
    body = html_to_markdown(rendered_html, canonical_url=canonical_url)
    excerpt = re.sub(r"\s+", " ", _plain_text(post.get("excerpt", ""))).strip()
    categories, tags = extract_terms(post)
    featured_url, featured_alt = extract_featured_image(post, canonical_url=canonical_url)
    relative_path = PurePosixPath(
        "content", "posts", f"{published_date.year:04d}", f"{published_date.month:02d}", f"{source_id}-{slug}.md"
    )
    return Article(
        source_id=source_id,
        title=title,
        slug=slug,
        canonical_url=canonical_url,
        published_at=published_at,
        published_at_gmt=published_at_gmt,
        modified_at=modified_at,
        modified_at_gmt=modified_at_gmt,
        excerpt=excerpt,
        body=body,
        tags=tags,
        categories=categories,
        featured_image_url=featured_url,
        featured_image_alt=featured_alt,
        relative_path=relative_path,
        body_sha256=hashlib.sha256(body.encode("utf-8")).hexdigest(),
    )


def build_page_url(page: int) -> str:
    if page < 1:
        raise SyncError("WordPress page number must be positive.")
    query = urllib.parse.urlencode(
        [
            ("per_page", str(PER_PAGE)),
            ("page", str(page)),
            ("status", "publish"),
            ("orderby", "id"),
            ("order", "asc"),
            ("_embed", "wp:featuredmedia,wp:term"),
        ],
        safe=":,",
    )
    return f"{WP_POSTS_ENDPOINT}?{query}"


def _validate_response_url(url: str) -> None:
    parsed = urllib.parse.urlparse(url)
    if (
        parsed.scheme != "https"
        or (parsed.hostname or "").rstrip(".").lower() not in {"jiami.dog", "www.jiami.dog"}
        or parsed.path.rstrip("/") != "/wp-json/wp/v2/posts"
        or parsed.username
        or parsed.password
    ):
        raise SyncError(f"Unexpected WordPress REST redirect: {url!r}")


def _retry_delay(error: urllib.error.HTTPError, attempt: int) -> float:
    retry_after = error.headers.get("Retry-After") if error.headers else None
    if retry_after:
        try:
            return max(1.0, min(float(retry_after), 60.0))
        except ValueError:
            try:
                parsed = parsedate_to_datetime(retry_after)
                return max(1.0, min(parsed.timestamp() - time.time(), 60.0))
            except (TypeError, ValueError, OverflowError):
                pass
    return float(2 ** (attempt - 1))


def _fetch_page(
    page: int,
    *,
    timeout_seconds: int,
    opener: Callable[..., Any],
) -> tuple[list[Mapping[str, Any]], int, int]:
    url = build_page_url(page)
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "JiamiDog-GitHub-Sync/1.0 (+https://github.com/JiamiDog/jiami.dog)",
        },
        method="GET",
    )
    last_error: Exception | None = None
    for attempt in range(1, MAX_FETCH_ATTEMPTS + 1):
        try:
            with opener(request, timeout=timeout_seconds) as response:
                _validate_response_url(response.geturl())
                total_header = response.headers.get("X-WP-Total")
                pages_header = response.headers.get("X-WP-TotalPages")
                if total_header is None or pages_header is None:
                    raise SyncError("WordPress response is missing X-WP-Total or X-WP-TotalPages.")
                try:
                    total = int(total_header)
                    total_pages = int(pages_header)
                except ValueError as exc:
                    raise SyncError("WordPress pagination headers are not integers.") from exc
                content_length = response.headers.get("Content-Length")
                if content_length and int(content_length) > MAX_RESPONSE_BYTES:
                    raise SyncError("WordPress page exceeds the 64 MiB safety limit.")
                raw = response.read(MAX_RESPONSE_BYTES + 1)
            break
        except urllib.error.HTTPError as exc:
            last_error = exc
            if exc.code not in {429, 500, 502, 503, 504} or attempt == MAX_FETCH_ATTEMPTS:
                raise SyncError(f"Unable to fetch WordPress page {page}: HTTP {exc.code}") from exc
            time.sleep(_retry_delay(exc, attempt))
        except SyncError:
            raise
        except (urllib.error.URLError, TimeoutError, ValueError) as exc:
            last_error = exc
            if attempt == MAX_FETCH_ATTEMPTS:
                raise SyncError(f"Unable to fetch WordPress page {page}: {exc}") from exc
            time.sleep(float(2 ** (attempt - 1)))
    else:  # pragma: no cover - loop always breaks or raises
        raise SyncError(f"Unable to fetch WordPress page {page}: {last_error}")

    if len(raw) > MAX_RESPONSE_BYTES:
        raise SyncError("WordPress page exceeds the 64 MiB safety limit.")
    try:
        payload = json.loads(raw.decode("utf-8-sig"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SyncError(f"WordPress page {page} is not valid UTF-8 JSON: {exc}") from exc
    if not isinstance(payload, list) or not all(isinstance(item, Mapping) for item in payload):
        raise SyncError(f"WordPress page {page} did not return a post array.")
    return list(payload), total, total_pages


def fetch_wordpress_posts(
    *,
    timeout_seconds: int = 30,
    opener: Callable[..., Any] = urllib.request.urlopen,
) -> tuple[list[Mapping[str, Any]], SourceSnapshot]:
    """Fetch and verify one complete, ordered WordPress posts snapshot."""
    posts: list[Mapping[str, Any]] = []
    expected_total: int | None = None
    expected_pages: int | None = None
    page = 1
    while True:
        page_posts, total, total_pages = _fetch_page(page, timeout_seconds=timeout_seconds, opener=opener)
        if total < 0 or total_pages < 0:
            raise SyncError("WordPress pagination headers cannot be negative.")
        calculated_pages = (total + PER_PAGE - 1) // PER_PAGE
        if total_pages != calculated_pages:
            raise SyncError(f"X-WP-TotalPages mismatch: header={total_pages}, calculated={calculated_pages}.")
        if expected_total is None:
            expected_total, expected_pages = total, total_pages
        elif total != expected_total or total_pages != expected_pages:
            raise SyncError("WordPress pagination headers changed during the snapshot.")
        expected_count = max(0, min(PER_PAGE, total - (page - 1) * PER_PAGE))
        if len(page_posts) != expected_count:
            raise SyncError(f"Incomplete WordPress page {page}: got {len(page_posts)}, expected {expected_count}.")
        posts.extend(page_posts)
        if page >= max(total_pages, 1):
            break
        page += 1

    assert expected_total is not None and expected_pages is not None
    if len(posts) != expected_total:
        raise SyncError(f"Fetched {len(posts)} posts but X-WP-Total is {expected_total}.")
    ids: list[int] = []
    for post in posts:
        if str(post.get("status", "")) != "publish" or str(post.get("type", "")) != "post":
            raise SyncError(f"Unexpected non-published/non-post record: {post.get('id')!r}")
        raw_id = post.get("id")
        if isinstance(raw_id, bool) or not isinstance(raw_id, int):
            raise SyncError(f"WordPress returned a non-integer ID: {raw_id!r}")
        ids.append(raw_id)
    if len(ids) != len(set(ids)):
        raise SyncError("WordPress snapshot contains duplicate post IDs.")
    if ids != sorted(ids):
        raise SyncError("WordPress snapshot is not ordered by ID ascending.")
    return posts, SourceSnapshot(expected_total, expected_pages, tuple(str(item) for item in ids))


def _yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _yaml_list(name: str, values: Sequence[str]) -> list[str]:
    if not values:
        return [f"{name}: []"]
    return [f"{name}:", *[f"  - {_yaml_string(value)}" for value in values]]


def _escape_markdown_text(value: str) -> str:
    return re.sub(r"([\\`*_[\]{}()#+.!|>~-])", r"\\\1", value)


def _media_key(url: str) -> str:
    name = Path(urllib.parse.unquote(urllib.parse.urlparse(url).path)).name.lower()
    stem, suffix = os.path.splitext(name)
    return re.sub(r"-\d+x\d+$", "", stem) + suffix


def render_article(article: Article) -> str:
    lines = [
        "---",
        f"title: {_yaml_string(article.title)}",
        f"slug: {_yaml_string(article.slug)}",
        f"source_id: {_yaml_string(article.source_id)}",
        f"canonical_url: {_yaml_string(article.canonical_url)}",
        f"date_local: {_yaml_string(article.published_at)}",
        f"date_published: {_yaml_string(article.published_at_gmt)}",
        f"date_modified_local: {_yaml_string(article.modified_at)}",
        f"date_modified: {_yaml_string(article.modified_at_gmt)}",
        "draft: false",
    ]
    if article.featured_image_url:
        lines.extend(
            [
                f"featured_image_url: {_yaml_string(article.featured_image_url)}",
                f"featured_image_alt: {_yaml_string(article.featured_image_alt)}",
            ]
        )
    lines.extend(_yaml_list("categories", article.categories))
    lines.extend(_yaml_list("tags", article.tags))
    lines.extend(
        [
            "---",
            "",
            f"# {article.title}",
            "",
            f"> 本文同步自 [jiami.dog 官方原文]({article.canonical_url})，以官网版本为准。",
            "",
        ]
    )
    if article.featured_image_url:
        key = _media_key(article.featured_image_url)
        if key and key not in article.body.lower():
            alt = _escape_markdown_text(article.featured_image_alt or article.title)
            lines.extend([f"![{alt}]({article.featured_image_url})", ""])
    return "\n".join(lines) + "\n" + article.body


def article_to_row(article: Article) -> dict[str, Any]:
    return {
        "categories": list(article.categories),
        "content_sha256": article.body_sha256,
        "date_local": article.published_at,
        "date_modified": article.modified_at_gmt,
        "date_published": article.published_at_gmt,
        "excerpt": article.excerpt,
        "featured_image_alt": article.featured_image_alt,
        "featured_image_url": article.featured_image_url,
        "github_path": article.relative_path.as_posix(),
        "source_id": article.source_id,
        "source_url": article.canonical_url,
        "slug": article.slug,
        "sync_status": "current",
        "tags": list(article.tags),
        "title": article.title,
    }


def _sorted_rows(rows: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        (dict(row) for row in rows),
        key=lambda row: (str(row.get("date_published", "")), int(str(row.get("source_id", "0")))),
        reverse=True,
    )


def render_content_index(rows: Sequence[Mapping[str, Any]]) -> str:
    pending_count = sum(row.get("sync_status") == "missing_once" for row in rows)
    lines = [
        "# 加密狗文章目录",
        "",
        "本目录由同步程序从 jiami.dog 的公开 WordPress posts 自动生成；官网是权威版本。",
        "",
        f"当前镜像：**{len(rows)}** 篇。",
        "",
    ]
    if pending_count:
        lines.extend([f"> 有 {pending_count} 篇等待连续第二次完整抓取确认后再决定是否删除。", ""])
    if not rows:
        lines.append("尚无已同步文章。")
    else:
        current_year = None
        for row in rows:
            published = str(row["date_local"] or row["date_published"])
            year = published[:4]
            if year != current_year:
                if current_year is not None:
                    lines.append("")
                lines.extend([f"## {year}", ""])
                current_year = year
            path = PurePosixPath(str(row["github_path"])).relative_to("content").as_posix()
            suffix = " · 待二次确认" if row.get("sync_status") == "missing_once" else ""
            lines.append(
                f"- {published[:10]} [{_escape_markdown_text(str(row['title']))}]({path}) · "
                f"[官网原文]({row['source_url']}){suffix}"
            )
    return "\n".join(lines).rstrip() + "\n"


def render_readme_section(rows: Sequence[Mapping[str, Any]]) -> str:
    pending_count = sum(row.get("sync_status") == "missing_once" for row in rows)
    lines = [f"已自动镜像 **{len(rows)}** 篇公开文章。", ""]
    if pending_count:
        lines.extend([f"> {pending_count} 篇正在等待第二次完整抓取确认。", ""])
    if not rows:
        lines.append("当前公开 posts 接口没有返回文章。")
    else:
        for row in rows[:10]:
            lines.append(
                f"- {str(row.get('date_local') or row['date_published'])[:10]} "
                f"[{_escape_markdown_text(str(row['title']))}]({row['github_path']}) · "
                f"[官网原文]({row['source_url']})"
            )
        lines.extend(["", "[查看全部文章 →](content/INDEX.md)"])
    return "\n".join(lines).rstrip()


def replace_readme_section(readme: str, generated: str) -> str:
    if readme.count(README_START) != 1 or readme.count(README_END) != 1:
        raise SyncError("README.md must contain exactly one generated-section marker pair.")
    before, remainder = readme.split(README_START, 1)
    _, after = remainder.split(README_END, 1)
    return f"{before}{README_START}\n\n{generated}\n\n{README_END}{after}"


def build_index(rows: Sequence[Mapping[str, Any]], *, source_total: int) -> str:
    normalized_rows = [dict(row) for row in rows]
    fingerprint_input = json.dumps(normalized_rows, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    payload = {
        "article_count": len(normalized_rows),
        "articles": normalized_rows,
        "canonical_site": "https://jiami.dog/",
        "feed_sha256": hashlib.sha256(fingerprint_input.encode("utf-8")).hexdigest(),
        "pending_removal_count": sum(row.get("sync_status") == "missing_once" for row in normalized_rows),
        "schema_version": "1.0",
        "source_article_count": source_total,
        "source_endpoint": WP_POSTS_ENDPOINT,
    }
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def build_state(snapshot: SourceSnapshot) -> str:
    ids_json = json.dumps(snapshot.source_ids, ensure_ascii=False, separators=(",", ":"))
    payload = {
        "endpoint": WP_POSTS_ENDPOINT,
        "last_complete_ids_sha256": hashlib.sha256(ids_json.encode("utf-8")).hexdigest(),
        "last_complete_source_ids": list(snapshot.source_ids),
        "last_complete_total": snapshot.total,
        "last_complete_total_pages": snapshot.total_pages,
        "schema_version": "1.0",
    }
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def _load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SyncError(f"Cannot read valid JSON from {path}: {exc}") from exc


def load_previous_rows(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    payload = _load_json(path)
    rows = payload.get("articles") if isinstance(payload, Mapping) else None
    if not isinstance(rows, list):
        raise SyncError("data/articles.json has no articles array.")
    result = []
    for row in rows:
        if not isinstance(row, Mapping):
            raise SyncError("data/articles.json contains a non-object article.")
        source_id = str(row.get("source_id", ""))
        path_value = PurePosixPath(str(row.get("github_path", "")))
        if not source_id.isdigit() or path_value.parts[:2] != ("content", "posts") or ".." in path_value.parts:
            raise SyncError("data/articles.json contains an unsafe previous article row.")
        result.append(dict(row))
    if len({str(row["source_id"]) for row in result}) != len(result):
        raise SyncError("data/articles.json contains duplicate source IDs.")
    return result


def load_previous_snapshot_ids(path: Path) -> set[str] | None:
    if not path.exists():
        return None
    payload = _load_json(path)
    if not isinstance(payload, Mapping) or payload.get("endpoint") != WP_POSTS_ENDPOINT:
        raise SyncError("data/sync-state.json has an unexpected endpoint.")
    value = payload.get("last_complete_source_ids")
    if value is None:
        return None
    if not isinstance(value, list) or not all(isinstance(item, str) and item.isdigit() for item in value):
        raise SyncError("data/sync-state.json has invalid last_complete_source_ids.")
    if len(value) != len(set(value)):
        raise SyncError("data/sync-state.json has duplicate source IDs.")
    return set(value)


def _assert_safe_managed_paths(repository_root: Path) -> None:
    resolved_root = repository_root.resolve()
    for relative in (
        "README.md",
        "content",
        "content/posts",
        "data",
        "data/articles.json",
        "data/sync-state.json",
    ):
        path = repository_root / relative
        if path.exists() and path.is_symlink():
            raise SyncError(f"Managed path must not be a symlink: {relative}")
        if path.exists() and not path.resolve().is_relative_to(resolved_root):
            raise SyncError(f"Managed path escapes repository root: {relative}")


def _write_if_changed(path: Path, content: str) -> bool:
    encoded = content.encode("utf-8")
    if path.exists() and path.read_bytes() == encoded:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)
    return True


def _remove_empty_post_directories(posts_root: Path) -> None:
    directories = sorted(
        (path for path in posts_root.rglob("*") if path.is_dir()),
        key=lambda path: len(path.parts),
        reverse=True,
    )
    for directory in directories:
        try:
            directory.rmdir()
        except OSError:
            pass


def sync_posts(
    posts: Sequence[Mapping[str, Any]],
    snapshot: SourceSnapshot,
    repository_root: Path,
) -> dict[str, int]:
    """Validate/convert everything before atomically updating allowlisted outputs."""
    repository_root = repository_root.resolve()
    _assert_safe_managed_paths(repository_root)
    readme_path = repository_root / "README.md"
    if not readme_path.is_file():
        raise SyncError(f"README.md not found under {repository_root}")
    if len(posts) != snapshot.total:
        raise SyncError("Complete snapshot metadata does not match the provided posts.")
    articles = [normalize_post(post) for post in posts]
    if len({article.source_id for article in articles}) != len(articles):
        raise SyncError("Normalized posts contain duplicate source IDs.")
    if tuple(article.source_id for article in articles) != snapshot.source_ids:
        raise SyncError("Normalized post IDs do not match the complete source snapshot.")

    index_path = repository_root / "data" / "articles.json"
    state_path = repository_root / "data" / "sync-state.json"
    previous_rows = load_previous_rows(index_path)
    previous_by_id = {str(row["source_id"]): row for row in previous_rows}
    previous_snapshot_ids = load_previous_snapshot_ids(state_path)
    current_rows = [article_to_row(article) for article in articles]
    current_ids = {article.source_id for article in articles}
    retained_rows: list[dict[str, Any]] = []
    for source_id in sorted(set(previous_by_id) - current_ids, key=int):
        if previous_snapshot_ids is not None and source_id not in previous_snapshot_ids:
            continue
        retained = dict(previous_by_id[source_id])
        retained["sync_status"] = "missing_once"
        retained_path = repository_root / PurePosixPath(str(retained["github_path"]))
        if not retained_path.is_file():
            raise SyncError(f"Cannot retain missing-once article because its file is absent: {retained_path}")
        retained_rows.append(retained)

    rows = _sorted_rows([*current_rows, *retained_rows])
    desired: dict[Path, str] = {
        repository_root / article.relative_path: render_article(article) for article in articles
    }
    desired[repository_root / "content" / "INDEX.md"] = render_content_index(rows)
    desired[index_path] = build_index(rows, source_total=snapshot.total)
    desired[state_path] = build_state(snapshot)
    desired[readme_path] = replace_readme_section(
        readme_path.read_text(encoding="utf-8"), render_readme_section(rows)
    )
    changed = sum(int(_write_if_changed(path, content)) for path, content in desired.items())
    keep_paths = {(repository_root / PurePosixPath(str(row["github_path"]))).resolve() for row in rows}
    posts_root = repository_root / "content" / "posts"
    existing = list(posts_root.rglob("*.md"))
    deleted = 0
    for path in existing:
        if path.resolve() not in keep_paths:
            path.unlink()
            deleted += 1
    _remove_empty_post_directories(posts_root)
    return {
        "published": snapshot.total,
        "mirrored": len(rows),
        "pending_removal": len(retained_rows),
        "changed": changed,
        "deleted": deleted,
    }


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repository-root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--timeout-seconds", type=int, default=30)
    args = parser.parse_args(argv)
    if not 1 <= args.timeout_seconds <= 120:
        parser.error("--timeout-seconds must be between 1 and 120")
    return args


def _verify_converter_version() -> None:
    try:
        installed = package_version("markdownify")
    except PackageNotFoundError as exc:
        raise SyncError("markdownify is not installed; run pip install -r requirements.txt") from exc
    if installed != EXPECTED_MARKDOWNIFY_VERSION:
        raise SyncError(f"markdownify version must be {EXPECTED_MARKDOWNIFY_VERSION}, found {installed}.")


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        _verify_converter_version()
        posts, snapshot = fetch_wordpress_posts(timeout_seconds=args.timeout_seconds)
        stats = sync_posts(posts, snapshot, args.repository_root)
    except SyncError as exc:
        print(f"sync error: {exc}", file=sys.stderr)
        return 1
    print(
        "sync complete: "
        f"published={stats['published']} mirrored={stats['mirrored']} "
        f"pending_removal={stats['pending_removal']} changed={stats['changed']} deleted={stats['deleted']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
