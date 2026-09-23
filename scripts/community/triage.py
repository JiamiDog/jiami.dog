#!/usr/bin/env python3
"""Deterministic, least-privilege community triage for JiamiDog.

The bot deliberately has no generative model and never follows URLs supplied by
participants.  It only compares article references with the repository's
committed ``data/articles.json`` index and writes labels/comments through the
GitHub API.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


BOT_VERSION = "v1"
BOT_NAME = "JiamiDog community bot"
API_VERSION = "2022-11-28"
VALID_HOSTS = frozenset({"jiami.dog", "www.jiami.dog"})

URL_RE = re.compile(r"https?://[^\s<>()\[\]{}\"']+", re.IGNORECASE)
ARTICLE_PATH_RE = re.compile(r"/(\d{1,12})\.html/?")
MIRROR_PATH_RE = re.compile(
    r"(?:^|/)content/posts/\d{4}/\d{2}/(\d{1,12})-[^\s?#]+\.md(?:[?#][^\s]*)?",
    re.IGNORECASE,
)
ARTICLE_ID_RE = re.compile(
    r"(?:文章|article|source)(?:\s*[_-]?\s*id)?\s*[:：#]?\s*`?(\d{1,12})`?",
    re.IGNORECASE,
)
BARE_ID_RE = re.compile(r"\bID\s*[:：#]\s*`?(\d{1,12})`?", re.IGNORECASE)

ROUTE_LABELS = frozenset(
    {
        "route:question",
        "route:correction",
        "route:sync",
        "route:feedback",
        "route:share",
        "route:poll",
    }
)
ARTICLE_LABELS = frozenset(
    {"article:verified", "article:needs-reference", "article:invalid"}
)

LABEL_SPECS: dict[str, tuple[str, str]] = {
    "route:question": ("0969da", "General question or usage discussion"),
    "route:correction": ("d93f0b", "Article correction or content-quality report"),
    "route:sync": ("8250df", "Repository mirror or synchronization report"),
    "route:feedback": ("5319e7", "Comment or experience tied to a published article"),
    "route:share": ("0e8a16", "Community experience or verified workflow sharing"),
    "route:poll": ("c5def5", "Community poll"),
    "article:verified": ("1a7f37", "Article ID matches the committed public index"),
    "article:needs-reference": ("fbca04", "A canonical article URL or stable article ID is needed"),
    "article:invalid": ("b60205", "Article reference is conflicting or absent from the public index"),
    "sync": ("8250df", "Article synchronization fault submitted through an issue form"),
    "rendering": ("0052cc", "Markdown rendering fault submitted through an issue form"),
    "metadata": ("006b75", "Article metadata fault submitted through an issue form"),
    "needs-triage": ("fbca04", "Waiting for maintainer review"),
}

ROUTE_NAMES = {
    "question": "问答",
    "correction": "纠错与建议",
    "sync": "同步与技术问题",
    "feedback": "文章评论",
    "share": "经验分享",
    "poll": "投票",
}

CATEGORY_ROUTES = {
    "文章评论": "feedback",
    "纠错与建议": "correction",
    "问答": "question",
    "经验分享": "share",
    "投票": "poll",
}

SYNC_KEYWORDS = (
    "github actions",
    "workflow",
    "同步",
    "镜像",
    "仓库",
    "自动抓取",
    "sync",
)
CORRECTION_KEYWORDS = (
    "纠错",
    "更正",
    "错误",
    "错别字",
    "链接失效",
    "图片失效",
    "内容过期",
    "事实错误",
    "broken link",
    "typo",
)


class TriageError(RuntimeError):
    """Raised when configuration, event data, or GitHub API state is invalid."""


@dataclass(frozen=True)
class Article:
    source_id: str
    source_url: str


@dataclass(frozen=True)
class ArticleReference:
    status: str
    had_reference: bool
    article: Article | None = None


@dataclass(frozen=True)
class EventPlan:
    surface: str
    number: int
    node_id: str | None
    desired_labels: tuple[str, ...]
    managed_labels: tuple[str, ...]
    marker: str
    comment_body: str


def load_article_index(path: Path) -> dict[str, Article]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TriageError(f"Cannot read article index: {path}") from exc

    rows = document.get("articles")
    if not isinstance(rows, list):
        raise TriageError("Article index must contain an articles list")

    result: dict[str, Article] = {}
    for row in rows:
        if not isinstance(row, dict):
            raise TriageError("Article index contains a non-object entry")
        source_id = str(row.get("source_id", ""))
        source_url = str(row.get("source_url", ""))
        if not source_id.isdigit() or not source_url:
            raise TriageError("Article index contains an invalid source record")
        if source_id in result:
            raise TriageError(f"Duplicate article ID in index: {source_id}")
        parsed = urllib.parse.urlsplit(source_url)
        if (
            parsed.scheme != "https"
            or (parsed.hostname or "").lower() != "jiami.dog"
            or parsed.path != f"/{source_id}.html"
        ):
            raise TriageError(f"Non-canonical source URL for article {source_id}")
        result[source_id] = Article(source_id=source_id, source_url=source_url)

    if not result:
        raise TriageError("Article index is empty")
    return result


def _clean_url(raw: str) -> str:
    return raw.rstrip(".,;:!?，。；：！？、")


def resolve_article_reference(
    text: str, articles: dict[str, Article]
) -> ArticleReference:
    """Resolve only local, stable article references without fetching user URLs."""

    candidate_ids: set[str] = set()
    saw_reference = False
    malformed = False

    for raw_url in URL_RE.findall(text or ""):
        cleaned = _clean_url(raw_url)
        parsed = urllib.parse.urlsplit(cleaned)
        hostname = (parsed.hostname or "").lower().rstrip(".")
        if hostname not in VALID_HOSTS:
            continue
        saw_reference = True
        match = ARTICLE_PATH_RE.fullmatch(parsed.path)
        if not match:
            malformed = True
            continue
        candidate_ids.add(match.group(1))

    for pattern in (MIRROR_PATH_RE, ARTICLE_ID_RE, BARE_ID_RE):
        matches = pattern.findall(text or "")
        if matches:
            saw_reference = True
            candidate_ids.update(matches)

    if not saw_reference:
        return ArticleReference(status="missing", had_reference=False)
    if malformed or len(candidate_ids) != 1:
        return ArticleReference(status="invalid", had_reference=True)

    source_id = next(iter(candidate_ids))
    article = articles.get(source_id)
    if article is None:
        return ArticleReference(status="invalid", had_reference=True)
    return ArticleReference(status="verified", had_reference=True, article=article)


def classify_route(text: str) -> str:
    normalized = (text or "").casefold()
    if any(keyword in normalized for keyword in SYNC_KEYWORDS):
        return "sync"
    if any(keyword in normalized for keyword in CORRECTION_KEYWORDS):
        return "correction"
    return "question"


def classify_discussion_route(discussion: dict[str, Any]) -> str | None:
    """Use the trusted GitHub category first; fall back to fixed title prefixes."""

    category = discussion.get("category")
    category_values: set[str] = set()
    if isinstance(category, dict):
        category_values = {
            str(category.get("name", "")).strip(),
            str(category.get("slug", "")).strip(),
        }
        category_values.discard("")

    if category_values & {"公告", "announcement", "announcements"}:
        return None
    for value in category_values:
        if value in CATEGORY_ROUTES:
            return CATEGORY_ROUTES[value]

    title = str(discussion.get("title", ""))
    for category_name, route in CATEGORY_ROUTES.items():
        if title.startswith(f"[{category_name}]"):
            return route
    return classify_route(f"{title}\n{discussion.get('body', '')}")


def hidden_marker(kind: str, identifier: object) -> str:
    if not re.fullmatch(r"[a-z-]+", kind):
        raise TriageError("Invalid marker kind")
    digest = hashlib.sha256(str(identifier).encode("utf-8")).hexdigest()[:20]
    return f"<!-- jiamidog-community-bot:{BOT_VERSION}:{kind}:{digest} -->"


def _article_label(reference: ArticleReference) -> str:
    return {
        "verified": "article:verified",
        "missing": "article:needs-reference",
        "invalid": "article:invalid",
    }[reference.status]


def compose_comment(
    marker: str,
    reference: ArticleReference,
    *,
    route: str | None,
    follow_up: bool,
) -> str:
    lines = [marker]
    if follow_up:
        lines.append("已检查这条新回复中的文章引用。")
    else:
        lines.append("感谢参与 JiamiDog 社区。机器人已完成确定性的初步分流。")

    if route is not None:
        lines.append(f"- 建议分流：**{ROUTE_NAMES[route]}**")

    if reference.status == "verified" and reference.article is not None:
        lines.append(
            "- 文章校验：已匹配公开镜像中的稳定文章 ID "
            f"`{reference.article.source_id}`（{reference.article.source_url}）"
        )
    elif reference.status == "missing":
        lines.append(
            "- 文章校验：尚未发现规范链接。若讨论具体文章，请补充 "
            "`https://jiami.dog/数字.html` 或明确写出 `文章 ID: 数字`。"
        )
    else:
        lines.append(
            "- 文章校验：所给链接或 ID 存在冲突，或不在当前公开镜像索引中；"
            "请改用文章页的规范链接或稳定文章 ID。"
        )

    lines.extend(
        [
            "",
            "该机器人不会删除、隐藏、锁定或关闭讨论，也不会修改 WordPress；最终判断由维护者完成。",
        ]
    )
    return "\n".join(lines)


def _positive_int(value: Any, field: str) -> int:
    if isinstance(value, bool):
        raise TriageError(f"Invalid {field}")
    try:
        result = int(value)
    except (TypeError, ValueError) as exc:
        raise TriageError(f"Invalid {field}") from exc
    if result <= 0:
        raise TriageError(f"Invalid {field}")
    return result


def _node_id(value: Any, field: str) -> str:
    result = str(value or "")
    if not result or len(result) > 256 or not re.fullmatch(r"[A-Za-z0-9_=-]+", result):
        raise TriageError(f"Invalid {field}")
    return result


def build_event_plan(
    event_name: str,
    payload: dict[str, Any],
    articles: dict[str, Article],
) -> EventPlan | None:
    action = str(payload.get("action", ""))

    if event_name == "issues" and action == "opened":
        issue = payload.get("issue") or {}
        if issue.get("pull_request"):
            return None
        number = _positive_int(issue.get("number"), "issue number")
        text = f"{issue.get('title', '')}\n{issue.get('body', '')}"
        route = classify_route(text)
        reference = resolve_article_reference(text, articles)
        marker = hidden_marker("issue-welcome", number)
        return EventPlan(
            surface="issue",
            number=number,
            node_id=None,
            desired_labels=(f"route:{route}", _article_label(reference)),
            managed_labels=tuple(sorted(ROUTE_LABELS | ARTICLE_LABELS)),
            marker=marker,
            comment_body=compose_comment(
                marker, reference, route=route, follow_up=False
            ),
        )

    if event_name == "discussion" and action == "created":
        discussion = payload.get("discussion") or {}
        number = _positive_int(discussion.get("number"), "discussion number")
        node_id = _node_id(discussion.get("node_id"), "discussion node ID")
        text = f"{discussion.get('title', '')}\n{discussion.get('body', '')}"
        route = classify_discussion_route(discussion)
        if route is None:
            return None
        reference = resolve_article_reference(text, articles)
        marker = hidden_marker("discussion-welcome", number)
        return EventPlan(
            surface="discussion",
            number=number,
            node_id=node_id,
            desired_labels=(f"route:{route}", _article_label(reference)),
            managed_labels=tuple(sorted(ROUTE_LABELS | ARTICLE_LABELS)),
            marker=marker,
            comment_body=compose_comment(
                marker, reference, route=route, follow_up=False
            ),
        )

    return None


class GitHubApi:
    def __init__(self, token: str, repository: str, api_url: str) -> None:
        parts = repository.split("/", 1)
        if len(parts) != 2 or not all(
            re.fullmatch(r"[A-Za-z0-9_.-]+", part) for part in parts
        ):
            raise TriageError("GITHUB_REPOSITORY must be owner/name")
        self.owner, self.repository_name = parts
        self.repository = repository
        self.api_url = api_url.rstrip("/")
        self.headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "jiamidog-community-triage/1.0",
            "X-GitHub-Api-Version": API_VERSION,
        }

    def request(
        self,
        method: str,
        path: str,
        data: dict[str, Any] | None = None,
        *,
        expected: Iterable[int] = (200,),
        allow_not_found: bool = False,
    ) -> Any:
        body = None
        headers = dict(self.headers)
        if data is not None:
            body = json.dumps(data, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"
        request = urllib.request.Request(
            f"{self.api_url}{path}", data=body, headers=headers, method=method
        )
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                raw = response.read()
                if response.status not in set(expected):
                    raise TriageError(
                        f"Unexpected GitHub response {response.status} for {method} {path}"
                    )
        except urllib.error.HTTPError as exc:
            if allow_not_found and exc.code == 404:
                return None
            detail = exc.read(2048).decode("utf-8", "replace")
            raise TriageError(
                f"GitHub API {method} {path} failed with {exc.code}: {detail}"
            ) from exc
        except urllib.error.URLError as exc:
            raise TriageError(f"GitHub API {method} {path} failed: {exc.reason}") from exc
        if not raw:
            return None
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise TriageError("GitHub API returned invalid JSON") from exc

    @property
    def repo_path(self) -> str:
        return "/repos/{}/{}".format(
            urllib.parse.quote(self.owner, safe=""),
            urllib.parse.quote(self.repository_name, safe=""),
        )

    def graphql(self, query: str, variables: dict[str, Any]) -> dict[str, Any]:
        response = self.request(
            "POST", "/graphql", {"query": query, "variables": variables}
        )
        if not isinstance(response, dict) or response.get("errors"):
            raise TriageError(f"GitHub GraphQL error: {response.get('errors') if isinstance(response, dict) else response}")
        data = response.get("data")
        if not isinstance(data, dict):
            raise TriageError("GitHub GraphQL response has no data")
        return data

    def ensure_label(self, name: str) -> dict[str, Any]:
        color, description = LABEL_SPECS[name]
        encoded = urllib.parse.quote(name, safe="")
        existing = self.request(
            "GET",
            f"{self.repo_path}/labels/{encoded}",
            allow_not_found=True,
        )
        if existing is not None:
            return existing
        return self.request(
            "POST",
            f"{self.repo_path}/labels",
            {"name": name, "color": color, "description": description},
            expected=(201,),
        )

    def issue_marker_exists(self, number: int, marker: str) -> bool:
        page = 1
        while True:
            comments = self.request(
                "GET",
                f"{self.repo_path}/issues/{number}/comments?per_page=100&page={page}",
            )
            if not isinstance(comments, list):
                raise TriageError("Issue comments response is not a list")
            if any(marker in str(comment.get("body", "")) for comment in comments):
                return True
            if len(comments) < 100:
                return False
            page += 1

    def post_issue_comment(self, number: int, body: str) -> None:
        self.request(
            "POST",
            f"{self.repo_path}/issues/{number}/comments",
            {"body": body},
            expected=(201,),
        )

    def set_issue_labels(
        self, number: int, desired: Iterable[str], managed: Iterable[str]
    ) -> None:
        desired_set = set(desired)
        # ``managed`` documents the labels this bot owns.  Labels are only
        # added, never removed: moderation history remains visible and the bot
        # cannot erase a maintainer's label decision.
        managed_set = set(managed)
        if not desired_set <= managed_set:
            raise TriageError("Issue plan requested a label outside its managed scope")
        for name in sorted(desired_set):
            self.ensure_label(name)

        current_rows = self.request(
            "GET", f"{self.repo_path}/issues/{number}/labels?per_page=100"
        )
        current = {
            str(row.get("name")) for row in current_rows if isinstance(row, dict)
        }
        missing = sorted(desired_set - current)
        if missing:
            self.request(
                "POST",
                f"{self.repo_path}/issues/{number}/labels",
                {"labels": missing},
            )

    def discussion_state(
        self, number: int
    ) -> tuple[str, dict[str, str], list[str]]:
        query = """
        query DiscussionState($owner: String!, $name: String!, $number: Int!, $cursor: String) {
          repository(owner: $owner, name: $name) {
            discussion(number: $number) {
              id
              labels(first: 100) { nodes { id name } }
              comments(first: 100, after: $cursor) {
                nodes { body }
                pageInfo { hasNextPage endCursor }
              }
            }
          }
        }
        """
        cursor: str | None = None
        node_id = ""
        labels: dict[str, str] = {}
        bodies: list[str] = []
        while True:
            data = self.graphql(
                query,
                {
                    "owner": self.owner,
                    "name": self.repository_name,
                    "number": number,
                    "cursor": cursor,
                },
            )
            repository = data.get("repository") or {}
            discussion = repository.get("discussion")
            if not isinstance(discussion, dict):
                raise TriageError(f"Discussion #{number} was not found")
            node_id = str(discussion.get("id", ""))
            label_nodes = ((discussion.get("labels") or {}).get("nodes") or [])
            labels.update(
                {
                    str(row.get("name")): str(row.get("id"))
                    for row in label_nodes
                    if isinstance(row, dict)
                }
            )
            comments = discussion.get("comments") or {}
            bodies.extend(
                str(row.get("body", ""))
                for row in (comments.get("nodes") or [])
                if isinstance(row, dict)
            )
            page_info = comments.get("pageInfo") or {}
            if not page_info.get("hasNextPage"):
                return node_id, labels, bodies
            cursor = str(page_info.get("endCursor", ""))
            if not cursor:
                raise TriageError("Discussion comments pagination has no cursor")

    def set_discussion_labels(
        self,
        discussion_id: str,
        current: dict[str, str],
        desired: Iterable[str],
        managed: Iterable[str],
    ) -> None:
        desired_set = set(desired)
        # See set_issue_labels: this bot intentionally has no removal path.
        managed_set = set(managed)
        if not desired_set <= managed_set:
            raise TriageError(
                "Discussion plan requested a label outside its managed scope"
            )
        # Discussion runs intentionally have no Issues permission.  Labels must
        # already exist from the manual initialization job; missing state stops
        # safely instead of broadening permissions at runtime.
        ensured = {
            name: self.require_existing_label(name) for name in sorted(desired_set)
        }

        add_ids = [
            str(ensured[name].get("node_id", ""))
            for name in sorted(desired_set - set(current))
        ]
        if any(not value for value in add_ids):
            raise TriageError("A label response has no node_id")

        if add_ids:
            self.graphql(
                """
                mutation AddLabels($labelableId: ID!, $labelIds: [ID!]!) {
                  addLabelsToLabelable(input: {labelableId: $labelableId, labelIds: $labelIds}) {
                    clientMutationId
                  }
                }
                """,
                {"labelableId": discussion_id, "labelIds": add_ids},
            )

    def require_existing_label(self, name: str) -> dict[str, Any]:
        data = self.graphql(
            """
            query ExistingLabel($owner: String!, $name: String!, $label: String!) {
              repository(owner: $owner, name: $name) {
                label(name: $label) { id name }
              }
            }
            """,
            {"owner": self.owner, "name": self.repository_name, "label": name},
        )
        repository = data.get("repository") or {}
        label = repository.get("label")
        if not isinstance(label, dict) or not label.get("id"):
            raise TriageError(
                f"Required label {name!r} is missing; run workflow_dispatch first"
            )
        return {"node_id": str(label["id"]), "name": str(label.get("name", ""))}

    def post_discussion_comment(self, discussion_id: str, body: str) -> None:
        self.graphql(
            """
            mutation AddDiscussionComment($discussionId: ID!, $body: String!) {
              addDiscussionComment(input: {discussionId: $discussionId, body: $body}) {
                comment { id }
              }
            }
            """,
            {"discussionId": discussion_id, "body": body},
        )


def execute_plan(api: GitHubApi, plan: EventPlan) -> None:
    if plan.surface == "issue":
        api.set_issue_labels(plan.number, plan.desired_labels, plan.managed_labels)
        if not api.issue_marker_exists(plan.number, plan.marker):
            api.post_issue_comment(plan.number, plan.comment_body)
        return

    if plan.surface == "discussion":
        discussion_id, current_labels, comment_bodies = api.discussion_state(
            plan.number
        )
        if plan.node_id is not None and discussion_id != plan.node_id:
            raise TriageError("Discussion node ID does not match the event payload")
        api.set_discussion_labels(
            discussion_id,
            current_labels,
            plan.desired_labels,
            plan.managed_labels,
        )
        if not any(plan.marker in body for body in comment_bodies):
            api.post_discussion_comment(discussion_id, plan.comment_body)
        return

    raise TriageError(f"Unsupported plan surface: {plan.surface}")


def initialize_labels(api: GitHubApi) -> None:
    """Create the bot's fixed label vocabulary without touching user content."""

    for name in sorted(LABEL_SPECS):
        api.ensure_label(name)


def _is_bot_sender(payload: dict[str, Any]) -> bool:
    sender = payload.get("sender") or {}
    login = str(sender.get("login", ""))
    return str(sender.get("type", "")).casefold() == "bot" or login.endswith("[bot]")


def main() -> int:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    event_path = Path(os.environ.get("GITHUB_EVENT_PATH", ""))
    token = os.environ.get("GITHUB_TOKEN", "")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    article_path = Path(
        os.environ.get("JIAMIDOG_ARTICLES_PATH", "data/articles.json")
    )

    if not event_name or not event_path.is_file() or not token or not repository:
        raise TriageError("Required GitHub Actions environment is incomplete")
    try:
        payload = json.loads(event_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise TriageError("Cannot read GitHub event payload") from exc
    if not isinstance(payload, dict):
        raise TriageError("GitHub event payload must be an object")
    if _is_bot_sender(payload):
        print("Ignoring bot-authored event.")
        return 0

    api = GitHubApi(token, repository, api_url)
    if event_name == "workflow_dispatch":
        initialize_labels(api)
        print(f"Initialized {len(LABEL_SPECS)} deterministic community labels.")
        return 0

    articles = load_article_index(article_path)
    plan = build_event_plan(event_name, payload, articles)
    if plan is None:
        print("No deterministic triage action is required for this event.")
        return 0

    execute_plan(api, plan)
    print(
        f"Applied {BOT_NAME} {BOT_VERSION} plan to {plan.surface} #{plan.number}."
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except TriageError as exc:
        print(f"community-triage error: {exc}", file=sys.stderr)
        raise SystemExit(1)
