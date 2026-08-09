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
                "h": "主張與證據帳本",
                "blocks": [{"t": "p", "runs": [{"s": "原文的帳本邊界必須保留。"}]}],
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
            ["研究摘要：已知、未知與下一步", "新手先讀：這篇在講什麼",
             "30 秒摘要", "主張—證據帳本", "影響路由與證據邊界"],
        )
        self.assertIn("不可比", str(topic["sections"]))
        self.assertIn("供應商首次確認訂單", str(topic["sections"]))
        self.assertIn("M1｜C1", str(topic["sections"]))
        self.assertIn("S1 甲公司正式公告", str(topic["sections"]))
        self.assertIn("不可由市場事件直接建立公司訂單", str(topic["sections"]))

        headings = [section["h"] for section in topic["sections"]]
        self.assertNotIn("只含 metadata 的空段落", headings)
        self.assertNotIn("主張與證據帳本", headings)
        self.assertEqual(headings.count("主張—證據帳本"), 1)
        self.assertTrue(all(section["blocks"] for section in topic["sections"]))
        analyst = topic["sections"][0]
        self.assertIn("一句話結論", str(analyst))
        self.assertIn("公司已正式公告擴產", str(analyst))
        self.assertIn("功率元件（方向未定／持續觀察）", str(analyst))
        self.assertIn("2026-08-05", str(analyst))
        self.assertIn("原文的帳本邊界必須保留", str(topic["sections"]))

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

    def test_learning_paths_only_route_to_existing_articles_graphs_and_groups(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        graph = {"graphs": [{
            "id": "test-graph", "label": "測試產業關聯",
            "articleIds": ["topic-MI-2026-07-29-TEST"],
            "nodes": [{"id": "company:1111", "ticker": "1111"},
                      {"id": "concept:test"}],
            "edges": [{"id": "E1", "from": "company:1111", "to": "concept:test"}],
        }]}

        returned = bd.attach_research_learning_paths(library, graph)

        self.assertIs(returned, library)
        self.assertEqual(library["learningPathVersion"], 3)
        article_ids = {article["id"] for article in library["articles"]}
        graph_ids = {item["id"] for item in graph["graphs"]}
        group_ids = {item["id"] for item in library["groups"]}
        for article in library["articles"]:
            path = article["learningPath"]
            self.assertEqual(path["title"], "從這篇接著學")
            self.assertLessEqual(len(path["cards"]), 3)
            self.assertIn("不會把相似題材當成已證實的供應鏈", path["description"])
            for card in path["cards"]:
                if card["kind"] == "article":
                    self.assertIn(card["articleId"], article_ids)
                    self.assertNotEqual(card["articleId"], article["id"])
                elif card["kind"] == "graph":
                    self.assertIn(card["graphId"], graph_ids)
                elif card["kind"] == "route":
                    self.assertIn(card["graphId"], graph_ids)
                elif card["kind"] == "group":
                    self.assertTrue(set(card["groupIds"]).issubset(group_ids))
                else:
                    self.assertEqual(card["kind"], "collection")
                    self.assertIn(card["articleType"], {"formal_note", "narrative", "topic"})

        topic = next(
            article for article in library["articles"]
            if article["id"] == "topic-MI-2026-07-29-TEST"
        )
        self.assertIn("formal-1111", {
            card.get("articleId") for card in topic["learningPath"]["cards"]
        })
        self.assertIn("test-graph", {
            card.get("graphId") for card in topic["learningPath"]["cards"]
        })
        event = next(
            article for article in library["articles"] if article["id"] == "event-tsmc-2026q2"
        )
        self.assertIn("group", {card["kind"] for card in event["learningPath"]["cards"]})

    def test_learning_path_prioritizes_next_registered_route_article(self):
        library = {"counts": {"topic": 3}, "groups": [], "articles": [
            {"id": "topic-a", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第一站", "typeLabel": "市場議題", "readingMinutes": 3},
            {"id": "topic-b", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站", "typeLabel": "市場議題", "readingMinutes": 5},
            {"id": "topic-b-detail", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站補充", "typeLabel": "市場議題", "readingMinutes": 4},
            {"id": "topic-c", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第三站", "typeLabel": "市場議題", "readingMinutes": 7},
        ]}
        graph = {
            "learningRoutes": [{
                "id": "route", "label": "測試路線",
                "description": "依序閱讀", "graphIds": ["graph-a", "graph-b", "graph-c"],
            }],
            "graphs": [
                {"id": "graph-a", "label": "第一圖", "articleIds": ["topic-a"],
                 "nodes": [], "edges": []},
                {"id": "graph-b", "label": "第二圖",
                 "articleIds": ["topic-b", "topic-b-detail", "topic-missing"],
                 "nodes": [], "edges": []},
                {"id": "graph-c", "label": "第三圖", "articleIds": ["topic-c"],
                 "nodes": [], "edges": []},
            ],
        }

        bd.attach_research_learning_paths(library, graph)

        first = library["articles"][0]["learningPath"]["cards"][0]
        second = library["articles"][1]["learningPath"]["cards"][0]
        self.assertEqual(first["label"], "沿學習路線往下讀")
        self.assertEqual(first["articleId"], "topic-b")
        self.assertIn("第 2/3 站", first["meta"])
        self.assertIn("不新增供應鏈或受惠關係", first["description"])
        self.assertEqual(second["articleId"], "topic-c")
        self.assertIn("第 3/3 站", second["meta"])
        self.assertEqual(library["articles"][0]["learningRoute"], {
            "id": "route", "label": "測試路線", "description": "依序閱讀",
            "step": 1, "total": 3, "graphId": "graph-a", "graphLabel": "第一圖",
        })
        self.assertNotIn("learningRoute", library["articles"][2])
        completed = library["articles"][3]["learningPath"]["cards"][0]
        self.assertEqual(completed["kind"], "route")
        self.assertEqual(completed["label"], "已完成這條學習路線")
        self.assertEqual(completed["graphId"], "graph-c")
        self.assertIn("第 3/3 站", completed["meta"])
        self.assertIn("不代表研究結論已完成", completed["description"])

        orphan = {"counts": {"topic": 1}, "groups": [], "articles": [{
            "id": "topic-policy", "type": "topic", "groups": [], "stockIds": [],
        }]}
        bd.attach_research_learning_paths(orphan, {"graphs": []})
        self.assertEqual(orphan["articles"][0]["learningPath"]["cards"], [{
            "kind": "collection", "label": "先比較其他議題",
            "title": "市場議題資料庫",
            "description": "這篇尚未建立可驗證的公司或族群連結；先比較其他議題的已知、未知與追蹤方式。",
            "meta": "1 篇市場議題", "articleType": "topic",
        }])

        wide = {"counts": {"topic": 1}, "groups": [
            {"id": group_id} for group_id in ("g1", "g2", "g3", "g4")
        ], "articles": [{
            "id": "topic-wide", "type": "topic",
            "groups": ["g1", "g2", "g3", "g4"], "stockIds": [],
        }]}
        bd.attach_research_learning_paths(wide, {"graphs": []})
        self.assertEqual(
            wide["articles"][0]["learningPath"]["cards"][0]["kind"], "collection")

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

    def test_group_maturity_keeps_coverage_materiality_and_maintenance_separate(self):
        topics = copy.deepcopy(self.topics)
        topics[0]["monitoring"][0]["status"] = "active"
        topics[0]["confidence"]["stale"] = True
        topics[0]["confidence"]["days_overdue"] = 1
        graph = {"graphs": [{
            "id": "test-graph",
            "nodes": [
                {"id": "company:1111", "type": "company", "universe": True,
                 "ticker": "1111", "groupId": "power"},
                {"id": "concept:test", "type": "concept", "universe": False},
            ],
            "edges": [{
                "id": "E1", "status": "active", "view": "company",
                "from": "company:1111", "to": "concept:test",
                "materiality": "named_product", "evidenceState": "verified",
            }],
        }]}
        reviews = [{
            "topic_id": "MI-2026-07-29-TEST", "monitor_id": "T1",
            "checked_at": "2026-08-05", "next_check": "2026-08-12",
        }]
        method = {"sources": {"thesesNeedingSecondIndependentGroup": [
            "MI-2026-07-29-TEST",
        ]}}
        maturity = bd.build_group_maturity(
            self.notes, topics, self.stock_meta, {"power": "功率元件"},
            graph, reviews, method, "2026-08-06",
        )
        row = maturity["rows"][0]
        self.assertEqual(maturity["summary"]["verifiedNotes"], 1)
        self.assertEqual(maturity["summary"]["dueMonitors"], 0)
        self.assertEqual(row["verifiedNotes"], 1)
        self.assertEqual(row["topics"], 1)
        self.assertEqual(row["companyBridges"], 1)
        self.assertEqual(row["materiality"]["named_product"], 1)
        self.assertEqual(row["materiality"]["financial"], 0)
        self.assertEqual(row["reviewedStaleTopics"], 1)
        self.assertEqual(row["sourceGaps"], 1)
        self.assertEqual(row["action"], "補第二條來源鏈")
        source_actions = [
            item for item in maturity["actionQueue"]
            if item["category"] == "source_gap"
        ]
        self.assertEqual(len(source_actions), 1)
        self.assertEqual(source_actions[0]["articleId"], "topic-MI-2026-07-29-TEST")
        self.assertEqual(row["actionIds"][0], "source-gap:MI-2026-07-29-TEST")
        self.assertNotIn("score", maturity)

    def test_group_maturity_deduplicates_one_source_gap_across_multiple_groups(self):
        topics = copy.deepcopy(self.topics)
        topics[0]["group_ids"] = ["power", "material"]
        topics[0]["monitoring"] = []
        method = {"sources": {"thesesNeedingSecondIndependentGroup": [
            "MI-2026-07-29-TEST",
        ]}}
        maturity = bd.build_group_maturity(
            self.notes, topics, self.stock_meta,
            {"power": "功率元件", "material": "半導體材料"},
            {"graphs": []}, [], method, "2026-08-06",
        )
        source_actions = [
            item for item in maturity["actionQueue"]
            if item["category"] == "source_gap"
        ]
        self.assertEqual(len(source_actions), 1)
        self.assertEqual(
            [group["id"] for group in source_actions[0]["affectedGroups"]],
            ["power", "material"],
        )
        self.assertIn("缺口只有一個", source_actions[0]["boundary"])
        rows = {row["id"]: row for row in maturity["rows"]}
        self.assertIn(source_actions[0]["id"], rows["power"]["actionIds"])
        self.assertIn(source_actions[0]["id"], rows["material"]["actionIds"])

    def test_group_maturity_v2_turns_bounded_proxy_into_watch_not_direct_attribution(self):
        topics = copy.deepcopy(self.topics)
        topics[0]["monitoring"] = []
        graph = {"graphs": [{
            "id": "test-graph",
            "nodes": [
                {"id": "company:1111", "type": "company", "universe": True,
                 "ticker": "1111", "groupId": "power"},
                {"id": "concept:test", "type": "concept", "universe": False},
            ],
            "edges": [{
                "id": "E1", "status": "active", "view": "company",
                "from": "company:1111", "to": "concept:test",
                "materiality": "named_product", "evidenceState": "verified",
                "articleIds": ["topic-MI-2026-07-29-TEST"], "reviewDue": "2026-08-31",
            }],
            "financialAssessments": [{
                "id": "FM1", "edgeId": "E1", "status": "active",
                "financialScope": "segment", "attributionStatus": "bounded_proxy",
                "reviewDue": "2026-08-31", "boundary": "部門大於題材",
                "nextTrigger": "等待題材收入分母",
            }],
        }]}
        maturity = bd.build_group_maturity(
            self.notes, topics, self.stock_meta, {"power": "功率元件"},
            graph, [], {"sources": {"thesesNeedingSecondIndependentGroup": []}},
            "2026-08-06",
        )
        row = maturity["rows"][0]
        self.assertEqual(row["financialMateriality"]["assessments"], 1)
        self.assertEqual(row["financialMateriality"]["attribution"]["bounded_proxy"], 1)
        self.assertEqual(row["financialMateriality"]["attribution"]["direct"], 0)
        self.assertEqual(row["action"], "等待可拆分的題材財務資料")
        self.assertEqual(maturity["summary"]["groupsWithFinancialAssessment"], 1)
        self.assertEqual(maturity["summary"]["groupsWithDirectFinancialAttribution"], 0)
        self.assertEqual(maturity["summary"]["openActions"], 0)
        self.assertEqual(maturity["summary"]["watchActions"], 1)
        action = maturity["actionQueue"][0]
        self.assertEqual(action["id"], "financial-watch:power")
        self.assertEqual(action["status"], "watch")
        self.assertIn("參考值不能改寫為題材收入", action["boundary"])

        graph["graphs"][0]["financialAssessments"] = []
        maturity = bd.build_group_maturity(
            self.notes, topics, self.stock_meta, {"power": "功率元件"},
            graph, [], {"sources": {"thesesNeedingSecondIndependentGroup": []}},
            "2026-08-06",
        )
        self.assertEqual(maturity["rows"][0]["action"], "補上題材財務影響")
        self.assertEqual(maturity["summary"]["openActions"], 1)
        self.assertEqual(maturity["actionQueue"][0]["id"], "financial:power")

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
            "研究摘要：已知、未知與下一步", "function resetReaderScroll()",
            "ARTICLE_AUDIT_HEADINGS", "function renderResearchAppendix(",
            "研究查核附錄：來源、主張與追蹤", "function renderLearningPath(",
            "從這篇接著學", "function openLearningGroups(",
            "function openLearningCollection(", "learning-path-grid",
            "maturity-reading-key", "先從左到右讀三層",
            "entry-guide", "第一次來？照三步開始",
            'id="entryMatrix"', 'id="entryTopics"', 'id="entryGraph"',
            "function showEntryGuide()", "function resetEntryScroll()",
            "function openEntrySurface(", "function openEntryTopics()",
            "text:'延伸學習'",
            "document.body.classList.remove('article-open');selectSurface('library',true)",
        ):
            self.assertIn(marker, template)
        self.assertIn("RESEARCH_TEMPLATE", builder)
        self.assertIn("RESEARCH_OUT", builder)
        self.assertIn('beginner-section', template)
        self.assertIn('新手先讀：這篇在講什麼', template)
        self.assertIn('beginner-toc', template)
        self.assertIn('_article_excerpt(topic.get("summary"))', builder)
        self.assertIn('_topic_structured_sections(topic, sections or [], group_names)', builder)
        self.assertIn('"asOf": library_as_of.isoformat()', builder)
        self.assertIn('as_of=research_as_of', builder)
        self.assertIn('taipei_today as research_today', builder)
        self.assertIn('research_html.replace(', builder)
        self.assertIn('research_library["knowledgeGraph"] = build_knowledge_graph(', builder)
        self.assertIn('attach_research_learning_paths(', builder)
        self.assertIn('research_library["candidateRadar"] = load_research_radar(', builder)
        self.assertIn("body.append(mobileBack,h('h1'", template)
        # meta 之後先標示學習路線，再由行動版大綱接手隱藏的桌機側欄。
        self.assertIn("body.append(meta);const routeContext=renderLearningRouteContext(article);"
                      "if(routeContext)body.appendChild(routeContext);"
                      "const mobileToc=renderMobileToc(article);"
                      "if(mobileToc)body.appendChild(mobileToc);"
                      "body.appendChild(articleSections(article,'beginner'));"
                      "body.appendChild(articleSections(article,'analyst'))", template)
        self.assertIn("body.appendChild(articleSections(article,'reader'))", template)
        self.assertIn("body.appendChild(appendix)", template)
        self.assertIn("schedule();requestAnimationFrame(()=>requestAnimationFrame(schedule))", template)
        self.assertLess(template.index('id="entryGuide"'), template.index('id="results"'))
        self.assertIn("!document.body.classList.contains('article-open')", template)
        self.assertIn("document.getElementById('entryMatrix').addEventListener", template)
        self.assertIn("document.getElementById('entryTopics').addEventListener", template)
        self.assertIn("document.getElementById('entryGraph').addEventListener", template)
        self.assertIn("window.scrollTo({top:0,left:0,behavior:'instant'})", template)
        self.assertIn("body.append(mobileEvidence,h('p'", template)
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
            "function graphHashRoute(value)",
            "selectSurface('graph',false)",
            "else{state.surface='library';syncSurface();document.body.classList.remove('article-open');applyFocusMode();renderAll()}",
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

    def test_template_focus_mode_reclaims_left_and_top_navigation_space(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="focusToggle"', 'aria-pressed="false"',
            "body.focus-mode .filters,body.focus-mode .tools{display:none}",
            "body.focus-mode .catalog{display:none}",
            "body.focus-mode .reader-inner{max-width:1180px",
            "localStorage.getItem('researchFocusMode')",
            "localStorage.setItem('researchFocusMode'",
            "focusToggleButton.setAttribute('aria-pressed'",
            "localStorage.getItem('researchFocusMode')!=='0'",
            "articleOpen&&focusModeRequested&&focusMedia.matches",
            "focusToggleButton.textContent=active?'文章清單':'專注閱讀'",
            "focusMedia.addEventListener('change',applyFocusMode)",
        ):
            self.assertIn(contract, template)
        self.assertIn("@media(min-width:781px){", template)
        self.assertIn(".focusbtn{display:none}", template)

    def test_template_outline_scroll_spy_tracks_reader_and_window_scroll(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function setupOutlineScrollSpy(root)",
            "function setActiveOutlineSection(root,index)",
            "scroll.addEventListener('scroll',schedule",
            "window.addEventListener('scroll',schedule",
            "window.addEventListener('resize',schedule",
            "scroll.getBoundingClientRect().top+70",
            "mobile?112:",
            "button.setAttribute('aria-current','location')",
            "button.classList.toggle('is-active',active)",
            "'data-section-index':index",
            "setupOutlineScrollSpy(root)",
            ".toc button.is-active",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            ".toc button.beginner-toc{border-left-color:var(--teal);"
            "color:var(--teal)",
            template,
        )

    def test_template_has_evidence_backed_dual_view_knowledge_graph(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="surfaceGraph"', 'id="graphHubTabs"', 'id="graphViewTabs"',
            'id="knowledgeGraph"', 'id="graphDetail"', 'id="graphRelationList"',
            'name="graphEvidence"', 'id="graphUniverseOnly"',
            "const KG=LIB.knowledgeGraph", "function renderGraph()",
            "function renderGraphSvg(", "function renderGraphDetail(",
            "function renderGraphExposureRings(",
            "function graphPositions(nodes,rootId,edges)",
            "['company','公司曝險']", "['industry','產業依賴']",
            "GRAPH_EXPOSURE_RINGS", "GRAPH_RELATION_GROUPS",
            "graph-exposure-ring", "graph-node-materiality",
            "graph-relation-group", "graph-relation-items",
            'viewBox="0 0 1100 700"',
            "if(!isRoot)group.append(svgEl('rect',{class:'graph-node-materiality-bg",
            "graphMaterialityWidth", "stroke-dasharray",
            "證據邊界", "下一個升降級節點", "供應集中度範圍",
            "同心環距離＋節點標籤＝商業曝險層級",
            "節點越靠近中心", "只有公司直接揭露且能用同期間分母重算的數字",
            "function graphFinancialPanel(", "題材占比未揭露", "分子／揭露值定義",
            "role:'button',tabindex:'0'", "graphKeyboard(",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("線寬表示商業曝險", template)
        self.assertNotIn("點線與細線表示仍需更多商業證據", template)
        self.assertIn("state.graphUniverseOnly=event.target.checked", template)
        self.assertIn("state.graphEvidence.add(input.value)", template)

    def test_template_graph_uses_progressive_learning_routes_without_changing_evidence(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for contract in (
            'id="graphLearningTitle"', 'id="graphRouteTabs"',
            'id="graphHubSelect"', 'id="graphIntroActions"',
            'aria-label="知識圖譜學習路線"',
            "const GRAPH_LEARNING_ROUTES=KG.learningRoutes||[]",
            "function availableGraphRoutes()",
            "function graphRouteId(graphId)", "function activateGraphRoute(routeId)",
            "function activateGraphTopic(graphId)",
            "graphRoute:graphRouteId((KG.graphs||[])[0]?.id||'')",
            "state.graphRoute=graphRouteId(graphId)",
            "學習路線只整理導覽",
            ".graph-hub-tabs{display:none}", ".graph-hub-select{display:block}",
            "const startArticle=(graph.articleIds||[])",
            "'data-testid':'graph-primary-article'",
            "先讀主題文章 · ",
            "openGraphArticle(startArticle.id)",
            "function renderLearningRouteContext(article)",
            "'aria-label':'學習路線定位'",
            "站次只代表閱讀順序，不是研究完成度或投資排名",
            "查看完整路線",
            "function resetGraphSurfaceScroll()",
            "graphPage.scrollTo(0,0)",
            "window.scrollTo(0,0)",
            "requestAnimationFrame(()=>requestAnimationFrame(reset))",
            "selectSurface('graph',true);resetGraphSurfaceScroll()",
            "card.kind==='route'?'回到學習路線'",
            ".graph-intro-action{width:100%;min-height:44px}",
        ):
            self.assertIn(contract, template)
        self.assertIn(
            "document.getElementById('graphHubSelect').addEventListener('change'",
            template,
        )
        self.assertIn(
            "other=(KG.graphs||[]).filter(graph=>!known.has(graph.id))", template)
        self.assertNotIn("v2 direct assessment 能進入", template)
        for contract in (
            "RESEARCH_LEARNING_ROUTES", "供電與散熱", "記憶體與封裝",
            "運算與互連", "公司財務案例", "先辨識液冷產品資格",
            'research_library["knowledgeGraph"]["learningRoutes"]',
            "沿學習路線往下讀", "不新增供應鏈或受惠關係",
            "已完成這條學習路線", "first existing articleId",
        ):
            self.assertIn(contract, builder)

    def test_template_publishes_ranked_candidate_research_radar(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="surfaceRadar"', 'id="radarPage"', 'id="radarStats"',
            'id="radarMethod"', 'id="radarList"',
            "const RADAR=LIB.candidateRadar", "function renderRadar()",
            "function renderRadarCandidate(", "function openRadarGraph(",
            "'data-testid':'radar-'+candidate.id", "candidate.firstRejection",
            "candidate.nextEvidence", "candidate.nextCheck",
            "排序只用來安排研究先後，不代表預期報酬、股價方向或投資建議",
            "候選排名不是投資評分", "deepLink==='radar'",
            "研究判定與來源", "研究方法與稽核資料（供查核）",
            "document.getElementById('surfaceRadar').addEventListener",
        ):
            self.assertIn(contract, template)
        self.assertIn("grid-template-columns:repeat(4,1fr)", template)

    def test_template_publishes_group_maturity_matrix_without_a_composite_score(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for contract in (
            'id="surfaceMaturity"', 'id="maturityPage"', 'id="maturitySummary"',
            'id="maturityActionQueue"', 'id="maturityMatrix"',
            "const MATURITY=LIB.groupMaturity", "function renderMaturity()",
            "function renderMaturityAction(", "function focusMaturityAction(",
            "function openGroupResearch(", "deepLink==='maturity'",
            "各族群研究完整度", "最大缺口", "不做總分或名次",
            "可水平捲動的族群研究成熟度矩陣",
            "完整查核矩陣與方法說明", "題材財務影響", "maturitySummarySentence",
        ):
            self.assertIn(contract, template)
        self.assertIn("body.article-open .tools{display:none}", template)
        self.assertIn('research_library["groupMaturity"] = build_group_maturity(', builder)
        self.assertIn('candidate_radar=research_library["candidateRadar"]', builder)
        self.assertIn("def build_group_maturity(", builder)


if __name__ == "__main__":
    unittest.main()
