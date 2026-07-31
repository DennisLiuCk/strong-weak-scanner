# -*- coding: utf-8 -*-
"""獨立研究中心：完整文章 payload、站內閱讀與首頁分流契約。"""
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_dashboard as bd


SECTIONS = [{
    "h": "30 秒摘要",
    "blocks": [{"t": "p", "runs": [{"s": "這是一段可搜尋、可站內閱讀的研究內容。"}]}],
}]


class ResearchCenterTest(unittest.TestCase):
    def setUp(self):
        self.notes = {
            "1111": {
                "last_updated": "2026-07-31", "verification": "independently_verified",
                "quality_invalid": False, "quality_errors": [], "summary": "正式筆記摘要",
                "relpath": "notes/qualitative/1111_甲公司.md", "sections": SECTIONS,
                "sources": [{"id": "S1", "type": "一手", "document": "2026Q2 法說簡報",
                             "url": "https://example.com/source.pdf"}],
                "content_as_of": "2026-07-30", "latest_financial_period": "2026Q2",
                "next_review": "2026-08-31", "reviewed_at": "2026-07-31",
                "reviewed_by": "reviewer", "primary_source_count": 1,
                "claim_count": 4, "cited_claim_count": 4,
            },
            "9999": {
                "last_updated": "2099-01-01", "verification": "ai_draft",
                "quality_invalid": True, "quality_errors": ["壞資料"],
                "summary": "不可發布", "relpath": "notes/qualitative/9999_壞資料.md",
            },
        }
        self.reports = {
            "1111": {
                "quality_invalid": False, "quality_errors": [],
                "narrative": {"updated": "2026-07-30"},
                "hypotheses": [{"title": "營收將季增"}], "hypothesis_count": 1,
                "sections": SECTIONS, "relpath": "notes/leading_hypotheses/1111_甲公司.md",
                "content_as_of": "2026-07-30", "next_review": "2026-08-15",
                "status": "active_monitoring",
            }
        }
        self.topics = [{
            "topic_id": "MI-2026-07-29-TEST", "captured_at": "2026-07-29",
            "review_due": "2026-08-05", "priority": "p1", "status": "triaged",
            "meta": {"last_reviewed_at": "2026-07-29", "publisher_domain": "example.com"},
            "stock_ids": ["1111"], "group_ids": ["power"], "title": "跨公司市場議題",
            "relpath": "notes/research_topics/test.md", "sections": SECTIONS,
            "quality_invalid": False, "quality_errors": [],
        }]
        self.stock_meta = {"1111": {"name": "甲公司", "group": "power", "biz": "功率元件"}}

    def test_library_has_all_three_types_and_excludes_invalid_articles(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"}
        )
        self.assertEqual(library["total"], 3)
        self.assertEqual(library["counts"], {"formal_note": 1, "narrative": 1, "topic": 1})
        self.assertEqual([row["type"] for row in library["articles"]],
                         ["formal_note", "narrative", "topic"])
        self.assertEqual(library["anchor"], "2026-07-31")
        self.assertNotIn("9999", " ".join(row["id"] for row in library["articles"]))

    def test_article_payload_preserves_sections_evidence_and_deep_links(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"}
        )
        formal = library["articles"][0]
        self.assertEqual(formal["id"], "formal-1111")
        self.assertEqual(formal["readerTitle"], "1111 甲公司 — 質化研究筆記")
        self.assertEqual(formal["sections"], SECTIONS)
        self.assertEqual(formal["sources"][0]["id"], "S1")
        self.assertEqual(formal["statusKey"], "verified")
        self.assertEqual(formal["groupLabels"], ["功率元件"])
        self.assertGreaterEqual(formal["readingMinutes"], 2)
        self.assertTrue(formal["sourceUrl"].endswith("notes/qualitative/1111_甲公司.md"))

    def test_template_has_functional_master_detail_and_accessibility_markers(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for marker in (
            "const LIB=__RESEARCH_JSON__", "研究中心", "搜尋公司、產業、主題",
            "function filteredArticles()", "function selectArticle(", "function renderReader(",
            "正式筆記", "多空小作文", "市場議題", "返回研究清單",
            "aria-label=\"研究文章清單\"", ":focus-visible", "@media(max-width:780px)",
        ):
            self.assertIn(marker, template)
        self.assertIn("RESEARCH_TEMPLATE", builder)
        self.assertIn("RESEARCH_OUT", builder)
        self.assertIn('research_html.replace(', builder)
        self.assertIn("body.append(mobileBack,h('h1'", template)
        self.assertIn("body.append(meta,articleSections(article)", template)
        self.assertIn("'aria-selected':state.type===type?'true':'false'", template)
        self.assertIn("'data-testid':'article-'+article.id", template)
        self.assertIn("@media(max-width:1180px){\n  .shell{display:block}", template)
        self.assertIn('id="filterClose"', template)
        self.assertIn("getElementById('filterClose').addEventListener", template)
        self.assertNotIn("github.com/DennisLiuCk/strong-weak-scanner/blob/main/notes/qualitative/8261", template)


if __name__ == "__main__":
    unittest.main()
