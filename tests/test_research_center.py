# -*- coding: utf-8 -*-
"""獨立研究中心：完整文章 payload、站內閱讀與首頁分流契約。"""
import copy
import inspect
import json
import re
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
            "meta": {
                "last_reviewed_at": "2026-07-29", "publisher_domain": "example.com",
                "status": "triaged", "review_due": "2026-08-05",
                "base_confidence": "medium", "confidence_basis": "兩份一手來源交叉支持",
            },
            "stock_ids": ["1111"], "group_ids": ["power"], "title": "跨公司市場議題",
            "impacts": [{
                "group_id": "power", "stock_ids": ["1111"], "direction": "uncertain",
                "hypothesis_refs": ["1111:H1"], "note_action": "watch",
                "action_due": "2026-08-05", "rationale": "等待公司文件",
                "evidence_boundary": "不可由市場事件直接建立公司訂單",
            }],
            "relpath": "notes/research_topics/test.md",
            "sections": [{
                "h": "新手先讀：這篇在講什麼",
                "blocks": [{"t": "p", "runs": [{"s": "先釐清已知、未知與追蹤方式。"}]}],
            }, {
                "h": "只含 metadata 的空段落", "blocks": [],
            }] + SECTIONS,
            "sources": [
                {"source_id": "S1", "id": "S1", "title": "甲公司正式公告",
                 "document": "甲公司正式公告", "url": "https://example.com/s1"},
                {"source_id": "S2", "id": "S2", "title": "主管機關資料",
                 "document": "主管機關資料", "url": "https://example.org/s2"},
            ],
            "claims": [
                {"claim_id": "C1", "label": "verified", "label_text": "證實",
                 "claim": "公司已正式公告擴產。", "supporting_source_ids": ["S1"],
                 "contrary_source_ids": [], "boundary": "未證明台灣供應商訂單",
                 "basis": "公司公告"},
                {"claim_id": "C2", "label": "unverified", "label_text": "待驗證",
                 "claim": "擴產將帶動特定供應商營收。", "supporting_source_ids": [],
                 "contrary_source_ids": [], "boundary": "尚無公司層級文件",
                 "verification_needed": "等待供應商法說揭露"},
            ],
            "comparisons": [
                {"comparison_id": "M1", "claim_id": "C1", "entity": "甲公司",
                 "evidence_ids": ["S1"], "metric": "CapEx",
                 "reported_value": "100", "period_start": "2026-01-01",
                 "period_end": "2026-06-30", "period_basis": "H1", "unit": "億元",
                 "definition": "現金購置 PP&E", "comparability": "not_comparable",
                 "comparability_text": "不可比", "comparability_reason": "另一家公司含租賃"},
                {"comparison_id": "M1", "claim_id": "C1", "entity": "乙公司",
                 "evidence_ids": ["S1"], "metric": "CapEx",
                 "reported_value": "120", "period_start": "2026-01-01",
                 "period_end": "2026-06-30", "period_basis": "H1", "unit": "億元",
                 "definition": "含融資租賃", "comparability": "not_comparable",
                 "comparability_text": "不可比", "comparability_reason": "定義不同"},
            ],
            "monitoring": [
                {"monitor_id": "T1", "claim_ids": ["C1", "C2"], "metric": "正式訂單揭露",
                 "source_ids": ["S1"], "watch_source_ids": ["S2"],
                 "frequency": "每季", "next_check": "2026-08-05",
                 "trigger": "供應商首次確認訂單", "invalidation": "公司取消擴產"},
            ],
            "last_evidence_at": "2026-07-29",
            "confidence": {
                "declared": "medium", "declared_label": "中", "effective": "medium",
                "effective_label": "中", "stale": False, "days_overdue": 0,
                "reason": "current", "as_of": "2026-07-29",
                "last_evidence_at": "2026-07-29", "review_due": "2026-08-05",
                "basis": "兩份一手來源交叉支持",
            },
            "quality_invalid": False, "quality_errors": [],
        }]
        self.events = {"all": [{
            "subject": "tsmc", "event_date": "2026-07-16", "fiscal_quarter": "2026Q2",
            "content_as_of": "2026-07-16", "next_review": "2026-10-15",
            "verification": "partially_verified", "title": "台積電 2026 Q2 法說會",
            "relpath": "notes/events/2026-07-16_台積電Q2法說會.md", "sections": SECTIONS,
            "guidance": {"power": {"dir": "up", "text": "資本支出上修"}},
            "kpi": {
                "kpi_capex": "US$60–64B", "kpi_fy_growth": "略高於 +40%",
                "kpi_gm": "65–67%", "kpi_hpc_share": "66%",
            },
            "quality_invalid": False, "quality_errors": [],
        }]}
        self.stock_meta = {"1111": {"name": "甲公司", "group": "power", "biz": "功率元件"}}

    def test_library_has_all_three_types_and_excludes_invalid_articles(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        self.assertEqual(library["total"], 4)
        self.assertEqual(library["counts"], {"formal_note": 1, "narrative": 1, "topic": 2})
        self.assertEqual([row["type"] for row in library["articles"]],
                         ["formal_note", "narrative", "topic", "topic"])
        self.assertEqual(library["anchor"], "2026-07-31")
        self.assertEqual(library["asOf"], "2026-07-31")
        self.assertNotIn("9999", " ".join(row["id"] for row in library["articles"]))

    def test_article_payload_preserves_sections_evidence_and_deep_links(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
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

        topic = next(row for row in library["articles"] if row["id"].startswith("topic-MI-"))
        self.assertEqual(topic["sources"][0]["source_id"], "S1")
        self.assertEqual(topic["confidence"]["effective"], "medium")
        self.assertEqual(
            [section["h"] for section in topic["sections"][:5]],
            ["新手先讀：這篇在講什麼", "主張—證據帳本", "影響路由與證據邊界",
             "跨公司數字可比性", "追蹤節點與失效條件"],
        )
        self.assertIn("不可比", str(topic["sections"]))
        self.assertIn("供應商首次確認訂單", str(topic["sections"]))
        self.assertIn("M1｜C1", str(topic["sections"]))
        self.assertIn("S1 甲公司正式公告", str(topic["sections"]))
        self.assertIn("不可由市場事件直接建立公司訂單", str(topic["sections"]))

        headings = [section["h"] for section in topic["sections"]]
        self.assertNotIn("只含 metadata 的空段落", headings)
        self.assertTrue(all(section["blocks"] for section in topic["sections"]))

        impact = next(
            section for section in topic["sections"]
            if section["h"] == "影響路由與證據邊界"
        )["blocks"][0]
        self.assertEqual(impact["t"], "table")
        self.assertEqual(
            [cell[0]["s"] for cell in impact["head"]],
            ["族群／個股", "方向", "筆記動作／期限", "關聯假說", "路由理由", "證據邊界"],
        )
        self.assertEqual(impact["rows"][0][0][0]["s"], "power｜1111")
        self.assertEqual(impact["rows"][0][1][0]["s"], "uncertain")
        self.assertEqual(impact["rows"][0][2][0]["s"], "watch；期限 2026-08-05")
        self.assertEqual(impact["rows"][0][3][0]["s"], "1111:H1")

        monitoring = next(
            section for section in topic["sections"]
            if section["h"] == "追蹤節點與失效條件"
        )["blocks"][0]
        self.assertEqual(
            [cell[0]["s"] for cell in monitoring["head"]],
            ["節點", "關聯主張", "指標／基準來源", "回查入口", "頻率／下次檢查",
             "觸發條件", "失效條件"],
        )
        self.assertIn("S1 甲公司正式公告", monitoring["rows"][0][2][0]["s"])
        self.assertEqual(monitoring["rows"][0][3][0]["s"], "S2 主管機關資料")

    def test_topic_confidence_uses_explicit_as_of_without_changing_article_anchor(self):
        due_day = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events, as_of="2026-08-05",
        )
        due_topic = next(
            row for row in due_day["articles"] if row["id"] == "topic-MI-2026-07-29-TEST")
        self.assertEqual(due_day["anchor"], "2026-07-31")
        self.assertEqual(due_day["asOf"], "2026-08-05")
        self.assertFalse(due_topic["confidence"]["stale"])
        self.assertEqual(due_topic["confidence"]["effective"], "medium")

        overdue = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events, as_of="2026-08-06",
        )
        overdue_topic = next(
            row for row in overdue["articles"] if row["id"] == "topic-MI-2026-07-29-TEST")
        self.assertEqual(overdue["anchor"], "2026-07-31")
        self.assertEqual(overdue["asOf"], "2026-08-06")
        self.assertTrue(overdue_topic["confidence"]["stale"])
        self.assertEqual(overdue_topic["confidence"]["effective"], "low")
        self.assertEqual(overdue_topic["confidence"]["days_overdue"], 1)

    def test_closed_topic_does_not_decay_and_low_becomes_needs_revalidation(self):
        closed = copy.deepcopy(self.topics)
        closed[0]["status"] = "resolved"
        closed[0]["meta"]["status"] = "resolved"
        library = bd.build_research_library(
            self.notes, self.reports, closed, self.stock_meta, {"power": "功率元件"},
            self.events, as_of="2026-09-01",
        )
        topic = next(row for row in library["articles"] if row["id"].startswith("topic-MI-"))
        self.assertFalse(topic["confidence"]["stale"])
        self.assertEqual(topic["confidence"]["effective"], "medium")

        low = copy.deepcopy(self.topics)
        low[0]["confidence"]["declared"] = "low"
        low[0]["confidence"]["declared_label"] = "低"
        low[0]["meta"]["base_confidence"] = "low"
        library = bd.build_research_library(
            self.notes, self.reports, low, self.stock_meta, {"power": "功率元件"},
            self.events, as_of="2026-08-06",
        )
        topic = next(row for row in library["articles"] if row["id"].startswith("topic-MI-"))
        self.assertTrue(topic["confidence"]["stale"])
        self.assertEqual(topic["confidence"]["effective"], "needs_revalidation")
        self.assertEqual(topic["confidence"]["effective_label"], "待重新驗證")

    def test_research_library_confidence_has_no_wall_clock_dependency(self):
        source = inspect.getsource(bd.build_research_library)
        self.assertNotIn("today", source)
        self.assertNotIn("datetime.now", source)
        self.assertNotIn("mtime", source)

    def test_inline_research_json_cannot_close_script(self):
        value = {"claim": "</script><script>alert(1)</script>", "amp": "A&B"}
        encoded = bd._inline_script_json(value)
        self.assertNotIn("</script>", encoded.lower())
        self.assertEqual(json.loads(encoded), value)

    def test_tsmc_event_is_published_as_a_market_topic_with_full_reader_content(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        event = next(row for row in library["articles"] if row["id"] == "event-tsmc-2026q2")
        self.assertEqual(event["type"], "topic")
        self.assertEqual(event["subject"], "2330 台積電")
        self.assertEqual(event["sections"], SECTIONS)
        self.assertEqual(event["groupLabels"], ["功率元件"])
        self.assertEqual(event["status"], "部分核驗")
        self.assertEqual(event["meta"]["eventKind"], "tsmc_earnings")
        self.assertEqual(event["meta"]["kpis"][0]["value"], "US$60–64B")
        self.assertTrue(event["sourceUrl"].endswith("notes/events/2026-07-16_台積電Q2法說會.md"))

    def test_template_has_functional_master_detail_and_accessibility_markers(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for marker in (
            "const LIB=__RESEARCH_JSON__", "研究中心", "搜尋公司、產業、主題",
            "function filteredArticles()", "function selectArticle(", "function renderReader(",
            "正式筆記", "多空小作文", "市場議題", "返回研究清單",
            "事件錨點整理法說脈絡與族群方向",
            "function confidenceBadge(", "function confidencePanel(",
            "function liveConfidence(", "Asia/Taipei", "confidenceAsOf()",
            "證據可信度", "主命題最後有效證據", "可信度判定",
            "來源帳本", "mobile-evidence", "可水平捲動的研究資料表",
            "aria-label=\"搜尋研究文章\"", "filtersPanel.inert", "clearArticleRoute",
            "aria-label=\"研究文章清單\"", ":focus-visible", "@media(max-width:780px)",
        ):
            self.assertIn(marker, template)
        self.assertIn("RESEARCH_TEMPLATE", builder)
        self.assertIn("RESEARCH_OUT", builder)
        self.assertIn('beginner-section', template)
        self.assertIn('新手先讀：這篇在講什麼', template)
        self.assertIn('beginner-toc', template)
        self.assertIn('_article_excerpt(topic.get("summary"))', builder)
        self.assertIn('_topic_structured_sections(topic, sections or [])', builder)
        self.assertIn('"asOf": library_as_of.isoformat()', builder)
        self.assertIn('as_of=research_as_of', builder)
        self.assertIn('taipei_today as research_today', builder)
        self.assertIn('research_html.replace(', builder)
        self.assertIn("body.append(mobileBack,h('h1'", template)
        self.assertIn("body.append(meta,articleSections(article)", template)
        self.assertIn("'aria-selected':state.type===type?'true':'false'", template)
        self.assertIn("'data-testid':'article-'+article.id", template)
        self.assertIn("@media(max-width:1180px){\n  .shell{display:block}", template)
        self.assertIn('id="filterClose"', template)
        self.assertIn("if(byId.has(deepLink))document.body.classList.add('article-open')", template)
        self.assertIn("state.selected=byId.has(deepLink)?deepLink:null", template)
        self.assertIn("function hashArticleId()", template)
        self.assertIn("url.hash=article.id", template)
        self.assertNotIn("github.com/DennisLiuCk/strong-weak-scanner/blob/main/notes/qualitative/8261", template)

    def test_template_recomputes_confidence_from_taipei_calendar_at_runtime(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "timeZone:'Asia/Taipei'",
            "let RESEARCH_TODAY=taipeiDate()",
            "function confidenceAsOf()",
            "RESEARCH_TODAY>(LIB.asOf||'')",
            "const confidence=liveConfidence(article)",
            "RESEARCH_TODAY=current;renderAll()",
        ):
            self.assertIn(contract, template)
        self.assertRegex(
            template,
            r"setInterval\(\(\)=>\{const current=taipeiDate\(\);"
            r"if\(current!==RESEARCH_TODAY\)\{RESEARCH_TODAY=current;renderAll\(\)\}\},60000\)",
        )

    def test_template_mobile_route_keeps_list_and_hash_state_consistent(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function setArticleHash(id)",
            "function clearArticleRoute()",
            "setArticleHash('')",
            "mobileBack.addEventListener('click',clearArticleRoute)",
            "if(document.body.classList.contains('article-open'))setArticleHash(state.selected)",
            "if(document.body.classList.contains('article-open'))clearArticleRoute()",
            "else if(!id)document.body.classList.remove('article-open')",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            "history.replaceState(null,'','#'+encodeURIComponent(state.selected))", template)

    def test_template_offcanvas_filters_manage_inert_focus_and_escape(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        self.assertIn("visibility:hidden", template)
        self.assertIn(".filters.open{transform:translateX(0);visibility:visible", template)
        self.assertIn("filtersPanel.inert=overlay&&!open", template)
        self.assertIn("filtersPanel.setAttribute('aria-hidden',open?'false':'true')", template)
        self.assertIn("filterCloseButton.focus()", template)
        self.assertIn("filterToggleButton.focus()", template)
        self.assertRegex(
            template,
            r"filterCloseButton\s*=\s*document\.getElementById\(['\"]filterClose['\"]\)",
        )
        self.assertRegex(
            template,
            r"filterCloseButton\.addEventListener\(\s*['\"]click['\"]\s*,"
            r"\s*\(\)\s*=>\s*closeFilters\(\)\s*\)",
        )
        self.assertIn(
            "if(event.key==='Escape'&&filtersPanel.classList.contains('open'))closeFilters()",
            template,
        )


if __name__ == "__main__":
    unittest.main()
