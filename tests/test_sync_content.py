import io
import json
import sys
import tempfile
import unittest
import urllib.parse
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts"))

from sync_content import (  # noqa: E402
    SourceSnapshot,
    SyncError,
    WP_POSTS_ENDPOINT,
    build_page_url,
    fetch_wordpress_posts,
    html_to_markdown,
    normalize_post,
    sync_posts,
)


README = """# Test

<!-- AUTO:ARTICLES:START -->

old

<!-- AUTO:ARTICLES:END -->
"""


def wordpress_post(post_id=42, slug="hello-world", *, featured=True):
    embedded = {
        "wp:term": [
            [{"id": 2, "name": "教程", "taxonomy": "category"}],
            [{"id": 3, "name": "Affiliate", "taxonomy": "post_tag"}],
        ]
    }
    if featured:
        embedded["wp:featuredmedia"] = [
            {
                "source_url": f"https://jiami.dog/wp-content/uploads/{post_id}.jpg",
                "alt_text": "题图",
                "title": {"rendered": "题图标题"},
            }
        ]
    return {
        "id": post_id,
        "date": "2026-09-22T09:00:00",
        "date_gmt": "2026-09-22T01:00:00",
        "modified": "2026-09-23T10:00:00",
        "modified_gmt": "2026-09-23T02:00:00",
        "slug": slug,
        "status": "publish",
        "type": "post",
        "link": f"https://jiami.dog/{post_id}.html",
        "title": {"rendered": "Hello &amp; World"},
        "content": {
            "rendered": (
                '<p><a href="https://example.com">Useful link</a></p>'
                f'<p><img src="https://jiami.dog/wp-content/uploads/{post_id}.jpg" alt="Body image"></p>'
            ),
            "protected": False,
        },
        "excerpt": {"rendered": "<p>Short summary</p>", "protected": False},
        "featured_media": post_id if featured else 0,
        "categories": [2],
        "tags": [3],
        "_embedded": embedded,
    }


class FakeResponse:
    def __init__(self, url, payload, total, total_pages):
        self.url = url
        self.payload = json.dumps(payload).encode("utf-8")
        self.headers = {
            "X-WP-Total": str(total),
            "X-WP-TotalPages": str(total_pages),
            "Content-Length": str(len(self.payload)),
        }

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def geturl(self):
        return self.url

    def read(self, amount=-1):
        return io.BytesIO(self.payload).read(amount)


class SyncContentTests(unittest.TestCase):
    def make_repository(self):
        temporary = tempfile.TemporaryDirectory()
        root = Path(temporary.name)
        (root / "content" / "posts").mkdir(parents=True)
        (root / "data").mkdir()
        (root / "README.md").write_text(README, encoding="utf-8")
        (root / "data" / "articles.json").write_text(
            json.dumps({"articles": []}), encoding="utf-8"
        )
        (root / "data" / "sync-state.json").write_text(
            json.dumps(
                {
                    "endpoint": WP_POSTS_ENDPOINT,
                    "last_complete_source_ids": None,
                }
            ),
            encoding="utf-8",
        )
        return temporary, root

    def test_page_url_has_fixed_complete_contract(self):
        parsed = urllib.parse.urlparse(build_page_url(2))
        query = urllib.parse.parse_qs(parsed.query)
        self.assertEqual(f"{parsed.scheme}://{parsed.netloc}{parsed.path}", WP_POSTS_ENDPOINT)
        self.assertEqual(
            query,
            {
                "per_page": ["100"],
                "page": ["2"],
                "status": ["publish"],
                "orderby": ["id"],
                "order": ["asc"],
                "_embed": ["wp:featuredmedia,wp:term"],
            },
        )

    def test_fetches_all_pages_and_validates_headers_and_ids(self):
        records = [
            {"id": item, "status": "publish", "type": "post"}
            for item in range(1, 102)
        ]

        def opener(request, timeout):
            del timeout
            page = int(urllib.parse.parse_qs(urllib.parse.urlparse(request.full_url).query)["page"][0])
            payload = records[:100] if page == 1 else records[100:]
            return FakeResponse(request.full_url, payload, 101, 2)

        posts, snapshot = fetch_wordpress_posts(opener=opener)
        self.assertEqual(len(posts), 101)
        self.assertEqual(snapshot.total_pages, 2)
        self.assertEqual(snapshot.source_ids[0], "1")
        self.assertEqual(snapshot.source_ids[-1], "101")

    def test_rejects_incomplete_page(self):
        records = [
            {"id": item, "status": "publish", "type": "post"}
            for item in range(1, 100)
        ]

        def opener(request, timeout):
            del timeout
            return FakeResponse(request.full_url, records, 101, 2)

        with self.assertRaisesRegex(SyncError, "Incomplete WordPress page 1"):
            fetch_wordpress_posts(opener=opener)

    def test_html_conversion_preserves_link_image_table_and_replaces_iframe(self):
        rendered = """
        <p><a href="https://example.com">Example</a></p>
        <p><img src="https://example.com/a.jpg" alt="A"></p>
        <table><tr><th>Name</th><th>Value</th></tr><tr><td>A</td><td>1</td></tr></table>
        <iframe src="https://www.youtube-nocookie.com/embed/abc" title="Official video"></iframe>
        """
        result = html_to_markdown(rendered, canonical_url="https://jiami.dog/42.html")
        self.assertIn("[Example](https://example.com)", result)
        self.assertIn("![A](https://example.com/a.jpg)", result)
        self.assertIn("| Name | Value |", result)
        self.assertIn("[Official video](https://www.youtube-nocookie.com/embed/abc)", result)
        self.assertNotIn("iframe", result.lower())

    def test_normalizer_reads_embedded_terms_and_optional_featured_image(self):
        article = normalize_post(wordpress_post())
        self.assertEqual(article.title, "Hello & World")
        self.assertEqual(article.categories, ("教程",))
        self.assertEqual(article.tags, ("Affiliate",))
        self.assertTrue(article.featured_image_url.endswith("/42.jpg"))
        self.assertEqual(article.published_at_gmt, "2026-09-22T01:00:00Z")

        no_featured = normalize_post(wordpress_post(43, "no-featured", featured=False))
        self.assertEqual(no_featured.featured_image_url, "")

    def test_missing_post_is_deleted_only_after_two_complete_snapshots(self):
        temporary, root = self.make_repository()
        self.addCleanup(temporary.cleanup)
        first_posts = [wordpress_post(1, "one"), wordpress_post(2, "two")]
        first = sync_posts(first_posts, SourceSnapshot(2, 1, ("1", "2")), root)
        self.assertEqual(first["mirrored"], 2)

        one_post = [wordpress_post(1, "one")]
        second = sync_posts(one_post, SourceSnapshot(1, 1, ("1",)), root)
        self.assertEqual(second["pending_removal"], 1)
        self.assertTrue((root / "content" / "posts" / "2026" / "09" / "2-two.md").exists())

        third = sync_posts(one_post, SourceSnapshot(1, 1, ("1",)), root)
        self.assertEqual(third["pending_removal"], 0)
        self.assertEqual(third["deleted"], 1)
        self.assertFalse((root / "content" / "posts" / "2026" / "09" / "2-two.md").exists())

        fourth = sync_posts(one_post, SourceSnapshot(1, 1, ("1",)), root)
        self.assertEqual(fourth, {"published": 1, "mirrored": 1, "pending_removal": 0, "changed": 0, "deleted": 0})


if __name__ == "__main__":
    unittest.main()
