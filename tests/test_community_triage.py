import json
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT / "scripts" / "community"))

from triage import (  # noqa: E402
    Article,
    GitHubApi,
    TriageError,
    build_event_plan,
    classify_discussion_route,
    classify_route,
    execute_plan,
    hidden_marker,
    initialize_labels,
    load_article_index,
    resolve_article_reference,
)


ARTICLES = {
    "5157": Article(
        source_id="5157", source_url="https://jiami.dog/5157.html"
    ),
    "42": Article(source_id="42", source_url="https://jiami.dog/42.html"),
}


class ArticleIndexTests(unittest.TestCase):
    def test_loads_only_canonical_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "articles.json"
            path.write_text(
                json.dumps(
                    {
                        "articles": [
                            {
                                "source_id": "5157",
                                "source_url": "https://jiami.dog/5157.html",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            result = load_article_index(path)
        self.assertEqual(result["5157"].source_url, "https://jiami.dog/5157.html")

    def test_rejects_noncanonical_index_url(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "articles.json"
            path.write_text(
                json.dumps(
                    {
                        "articles": [
                            {
                                "source_id": "5157",
                                "source_url": "https://example.com/5157.html",
                            }
                        ]
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(TriageError):
                load_article_index(path)


class ReferenceTests(unittest.TestCase):
    def test_validates_canonical_article_url_without_fetching_it(self):
        result = resolve_article_reference(
            "请看 https://jiami.dog/5157.html?from=github。", ARTICLES
        )
        self.assertEqual(result.status, "verified")
        self.assertEqual(result.article.source_id, "5157")

    def test_validates_explicit_stable_id(self):
        result = resolve_article_reference("文章 ID: 42", ARTICLES)
        self.assertEqual(result.status, "verified")
        self.assertEqual(result.article.source_url, "https://jiami.dog/42.html")

    def test_validates_mirror_markdown_path(self):
        result = resolve_article_reference(
            "content/posts/2026/09/5157-long-term-us-phone-number-guide-2026.md",
            ARTICLES,
        )
        self.assertEqual(result.status, "verified")

    def test_rejects_conflicting_url_and_id(self):
        result = resolve_article_reference(
            "https://jiami.dog/5157.html，文章 ID: 42", ARTICLES
        )
        self.assertEqual(result.status, "invalid")
        self.assertTrue(result.had_reference)

    def test_rejects_non_article_path_on_real_host(self):
        result = resolve_article_reference("https://jiami.dog/about", ARTICLES)
        self.assertEqual(result.status, "invalid")

    def test_does_not_trust_lookalike_host(self):
        result = resolve_article_reference(
            "https://jiami.dog.evil.example/5157.html", ARTICLES
        )
        self.assertEqual(result.status, "missing")
        self.assertFalse(result.had_reference)


class PlanningTests(unittest.TestCase):
    def test_sync_route_has_deterministic_precedence(self):
        self.assertEqual(classify_route("GitHub 镜像同步错误，请纠错"), "sync")
        self.assertEqual(classify_route("文章有错别字"), "correction")
        self.assertEqual(classify_route("这个怎么使用？"), "question")

    def test_issue_open_plan_welcomes_labels_and_never_echoes_input(self):
        hostile = "<script>alert(1)</script> 文章 ID: 5157"
        plan = build_event_plan(
            "issues",
            {
                "action": "opened",
                "issue": {"number": 7, "title": "纠错", "body": hostile},
            },
            ARTICLES,
        )
        self.assertEqual(plan.surface, "issue")
        self.assertEqual(
            set(plan.desired_labels), {"route:correction", "article:verified"}
        )
        self.assertIn("https://jiami.dog/5157.html", plan.comment_body)
        self.assertNotIn("<script>", plan.comment_body)
        self.assertIn(plan.marker, plan.comment_body)

    def test_discussion_plan_uses_node_id_and_stable_marker(self):
        payload = {
            "action": "created",
            "discussion": {
                "number": 3,
                "node_id": "D_kwDOExample",
                "title": "请问",
                "body": "https://jiami.dog/42.html",
            },
        }
        first = build_event_plan("discussion", payload, ARTICLES)
        second = build_event_plan("discussion", payload, ARTICLES)
        self.assertEqual(first.node_id, "D_kwDOExample")
        self.assertEqual(first.marker, second.marker)

    def test_discussion_category_controls_route_and_announcements_are_quiet(self):
        self.assertEqual(
            classify_discussion_route(
                {"category": {"name": "文章评论", "slug": "文章评论"}}
            ),
            "feedback",
        )
        self.assertEqual(
            classify_discussion_route(
                {"category": {"name": "Article Comments", "slug": "article-comments"}}
            ),
            "feedback",
        )
        self.assertIsNone(
            classify_discussion_route(
                {"category": {"name": "公告", "slug": "公告"}}
            )
        )

    def test_hidden_marker_rejects_dynamic_kind(self):
        with self.assertRaises(TriageError):
            hidden_marker("bad --> marker", 1)

    def test_existing_hidden_marker_prevents_duplicate_comment(self):
        plan = build_event_plan(
            "issues",
            {
                "action": "opened",
                "issue": {"number": 7, "title": "请问", "body": "文章 ID: 42"},
            },
            ARTICLES,
        )

        class FakeApi:
            def __init__(self):
                self.posts = []

            def set_issue_labels(self, number, desired, managed):
                self.labels = (number, tuple(desired), tuple(managed))

            def issue_marker_exists(self, number, marker):
                return marker == plan.marker

            def post_issue_comment(self, number, body):
                self.posts.append((number, body))

        api = FakeApi()
        execute_plan(api, plan)
        self.assertEqual(api.posts, [])

    def test_manual_initialization_uses_only_fixed_label_vocabulary(self):
        class FakeApi:
            def __init__(self):
                self.names = []

            def ensure_label(self, name):
                self.names.append(name)

        api = FakeApi()
        initialize_labels(api)
        self.assertEqual(
            api.names,
            [
                "article:invalid",
                "article:needs-reference",
                "article:verified",
                "metadata",
                "needs-triage",
                "rendering",
                "route:correction",
                "route:feedback",
                "route:poll",
                "route:question",
                "route:share",
                "route:sync",
                "sync",
            ],
        )

    def test_discussion_label_lookup_fails_safe_when_not_initialized(self):
        class MissingLabelApi(GitHubApi):
            def __init__(self):
                self.owner = "JiamiDog"
                self.repository_name = "jiami.dog"

            def graphql(self, query, variables):
                return {"repository": {"label": None}}

        with self.assertRaisesRegex(TriageError, "workflow_dispatch"):
            MissingLabelApi().require_existing_label("route:question")


if __name__ == "__main__":
    unittest.main()
