# -*- coding: utf-8 -*-
"""獨立研究中心：完整文章 payload、站內閱讀與首頁分流契約。"""
import copy
import csv
import inspect
import json
import re
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_dashboard as bd


SECTIONS = [{
    "h": "30 秒摘要",
    "blocks": [{"t": "p", "runs": [{"s": "這是一段可搜尋、可站內閱讀的研究內容。"}]}],
}]

FORMAL_SECTIONS = [{
    "h": "30 秒摘要",
    "blocks": [{"t": "ul", "items": [
        [{"s": "甲公司以功率元件銷售為主要收入來源。"}],
        [{"s": "題材連結仍須回到公司文件逐項核對。"}],
        [{"s": "元件出現在系統裡，不等於已取得平台訂單。"}],
    ]}],
}]

NARRATIVE_SECTIONS = [{
    "h": "多空觀點（小作文）",
    "blocks": [
        {"t": "h3", "runs": [{"s": "看多小作文"}]},
        {"t": "p", "runs": [{"s": "多方需要營收與毛利同步改善。"}]},
        {"t": "h3", "runs": [{"s": "看空小作文"}]},
        {"t": "p", "runs": [{"s": "空方需要庫存與價格壓力延續。"}]},
        {"t": "h3", "runs": [{"s": "勝負手"}]},
        {"t": "ul", "items": [
            [{"s": "營收是否連續兩季成長。"}],
            [{"s": "毛利率是否同步改善。"}],
            [{"s": "庫存天數是否下降。"}],
        ]},
    ],
}]


class ResearchCenterTest(unittest.TestCase):
    def setUp(self):
        self.notes = {
            "1111": {
                "last_updated": "2026-07-31", "verification": "independently_verified",
                "quality_invalid": False, "quality_errors": [], "summary": "正式筆記摘要",
                "relpath": "notes/qualitative/1111_甲公司.md", "sections": FORMAL_SECTIONS,
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
                "sections": NARRATIVE_SECTIONS,
                "relpath": "notes/leading_hypotheses/1111_甲公司.md",
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
                "blocks": [
                    {"t": "h3", "runs": [{"s": "名詞小字典"}]},
                    {"t": "ul", "items": [[{"s": "擴產：增加既有或新建產能。"}]]},
                    {"t": "h3", "runs": [{"s": "三句話抓重點"}]},
                    {"t": "ul", "items": [[{"s": "公司公告與供應商受惠是兩件事。"}]]},
                    {"t": "h3", "runs": [{"s": "為什麼重要"}]},
                    {"t": "p", "runs": [{
                        "s": "把公司擴產直接寫成特定供應商訂單，是本文要避免的誤解。"
                             "後續仍要等供應商文件。",
                    }]},
                    {"t": "h3", "runs": [{"s": "想一想"}]},
                    {"t": "ul", "items": [[{
                        "s": "還缺哪一份公司文件，才能把擴產連到供應商？",
                    }]]},
                ],
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

    def test_formal_and_narrative_articles_require_traceable_mission_sources(self):
        broken_notes = copy.deepcopy(self.notes)
        broken_notes["1111"]["sections"] = SECTIONS
        with self.assertRaisesRegex(ValueError, "formal-1111"):
            bd.build_research_library(
                broken_notes, {}, [], self.stock_meta, {"power": "功率元件"}, {},
            )

        broken_reports = copy.deepcopy(self.reports)
        broken_reports["1111"]["sections"] = SECTIONS
        with self.assertRaisesRegex(ValueError, "narrative-1111"):
            bd.build_research_library(
                {}, broken_reports, [], self.stock_meta, {"power": "功率元件"}, {},
            )

    def test_reading_mission_notations_decode_periods_sources_and_internal_labels(self):
        formal = bd._research_reading_mission_notations(
            {"type": "formal_note"},
            {
                "keyPoints": [
                    "2026Q2 營收成長，Universe 歸入 serverodm。[S1][S3]"
                ],
                "question": "這些數字如何回查？",
            },
            {"serverodm": "伺服器組裝/機構"},
        )
        self.assertEqual(
            [item["kind"] for item in formal],
            ["quarter", "internal_taxonomy", "source_index"],
        )
        self.assertEqual(formal[0]["tokens"], ["2026Q2"])
        self.assertIn("研究中心追蹤範圍", formal[1]["definition"])
        self.assertIn("伺服器組裝/機構族群", formal[1]["definition"])
        self.assertEqual(formal[2]["tokens"], ["S1", "S3"])
        self.assertIn("不代表證據強弱", formal[2]["boundary"])

        narrative = bd._research_reading_mission_notations(
            {"type": "narrative"},
            {
                "keyPoints": [
                    "MOPS 公告 2026Q4 數字後，依 H1 門檻判定。"
                ],
                "question": "哪個資料會改變判斷？",
            },
        )
        self.assertEqual(
            [item["kind"] for item in narrative],
            ["mops", "quarter", "hypothesis_id"],
        )
        self.assertIn("公開資訊觀測站", narrative[0]["label"])
        self.assertIn("不是上、下半年", narrative[2]["boundary"])

    def test_article_payload_preserves_sections_evidence_and_deep_links(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        formal = library["articles"][0]
        self.assertEqual(formal["id"], "formal-1111")
        self.assertEqual(formal["readerTitle"], "1111 甲公司 — 質化研究筆記")
        self.assertEqual(formal["sections"], FORMAL_SECTIONS)
        self.assertEqual(formal["sources"][0]["id"], "S1")
        self.assertEqual(formal["statusKey"], "verified")
        self.assertEqual(formal["groupLabels"], ["功率元件"])
        self.assertGreaterEqual(formal["readingMinutes"], 2)
        self.assertTrue(formal["sourceUrl"].endswith("notes/qualitative/1111_甲公司.md"))
        self.assertEqual(formal["readingMission"]["keyPoints"], [
            "甲公司以功率元件銷售為主要收入來源。",
            "題材連結仍須回到公司文件逐項核對。",
            "元件出現在系統裡，不等於已取得平台訂單。",
        ])
        self.assertEqual(formal["readingMission"]["sourceLabel"], "30 秒摘要")
        self.assertIn("1111 甲公司", formal["readingMission"]["question"])

        narrative = library["articles"][1]
        self.assertEqual(narrative["sections"], NARRATIVE_SECTIONS)
        self.assertEqual(narrative["readingMission"]["keyPoints"], [
            "營收是否連續兩季成長。",
            "毛利率是否同步改善。",
            "庫存天數是否下降。",
        ])
        self.assertEqual(narrative["readingMission"]["sourceLabel"], "勝負手")
        self.assertEqual(narrative["readingMission"]["sourceSection"], "多空觀點（小作文）")
        self.assertIn("1111 甲公司", narrative["readingMission"]["question"])

        topic = next(row for row in library["articles"] if row["id"].startswith("topic-MI-"))
        self.assertEqual(topic["sources"][0]["source_id"], "S1")
        self.assertEqual(topic["confidence"]["effective"], "medium")
        self.assertEqual(topic["readingMission"], {
            "orientation": "把公司擴產直接寫成特定供應商訂單，是本文要避免的誤解。",
            "question": "還缺哪一份公司文件，才能把擴產連到供應商？",
            "keyPoints": ["公司公告與供應商受惠是兩件事。"],
            "source": "本文既有的「三句話抓重點」、「為什麼重要」與「想一想」",
        })
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
        guide = analyst["readerEvidenceGuide"]
        self.assertEqual(guide["claimKey"], "verified")
        self.assertEqual(guide["claimLabel"], "證實")
        self.assertIn("直接支持這句主張的精確措辭", guide["claimMeaning"])
        self.assertEqual(guide["confidenceKey"], "medium")
        self.assertEqual(guide["confidenceLabel"], "中")
        self.assertIn("不是主張真假，也不是發生機率", guide["confidenceMeaning"])
        self.assertEqual(guide["sourceCount"], 1)
        self.assertEqual(guide["independenceCount"], 1)
        self.assertIn("不能直接換算成公司訂單", guide["boundary"])
        self.assertEqual(
            [item[0]["s"] for item in analyst["blocks"][1]["items"]],
            ["一句話結論：", "目前已知：", "尚未知道：", "對哪些族群有意義：", "下一步看什麼："],
        )
        self.assertTrue(all(
            len(item) == 2 and item[0].get("b") is True and not item[1].get("b", False)
            for item in analyst["blocks"][1]["items"]
        ))
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

    def test_evidence_reader_guide_separates_inference_from_confidence(self):
        topics = copy.deepcopy(self.topics)
        topics[0]["meta"]["thesis_claim_id"] = "C1"
        topics[0]["claims"][0]["label"] = "inference"
        topics[0]["claims"][0]["label_text"] = "推論"
        library = bd.build_research_library(
            self.notes, self.reports, topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        article = next(row for row in library["articles"] if row["id"].startswith("topic-MI-"))
        guide = article["sections"][0]["readerEvidenceGuide"]
        self.assertEqual(guide["claimKey"], "inference")
        self.assertEqual(guide["claimLabel"], "推論")
        self.assertIn("不是任一來源逐字寫出的整句結論", guide["claimMeaning"])
        self.assertEqual(guide["confidenceKey"], "medium")
        self.assertEqual(guide["confidenceLabel"], "中")
        self.assertIn("兩把不同的尺", guide["boundary"])

    def test_learning_paths_only_route_to_existing_articles_graphs_and_groups(self):
        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta, {"power": "功率元件"},
            self.events,
        )
        graph = {"graphs": [{
            "id": "test-graph", "label": "測試產業關聯",
            "articleIds": ["topic-MI-2026-07-29-TEST"],
            "rootNodeId": "concept:test",
            "nodes": [
                {"id": "company:1111", "ticker": "1111", "label": "甲公司"},
                {"id": "concept:test", "label": "測試主題"},
                {"id": "industry:power", "label": "功率元件"},
            ],
            "edges": [
                {
                    "id": "E1", "view": "company",
                    "from": "company:1111", "to": "concept:test",
                    "relationLabel": "供應測試角色", "evidenceState": "verified",
                    "evidenceLabel": "證實", "commercialStageLabel": "量產前驗證",
                    "boundary": "公司角色不等於具名量產訂單。",
                },
                {
                    "id": "E2", "view": "industry",
                    "from": "industry:power", "to": "concept:test",
                    "relationLabel": "參與產業環節", "evidenceState": "inference",
                    "evidenceLabel": "推論", "commercialStageLabel": "研究路由",
                },
            ],
        }]}

        returned = bd.attach_research_learning_paths(library, graph)

        self.assertIs(returned, library)
        self.assertEqual(library["learningPathVersion"], 66)
        article_ids = {article["id"] for article in library["articles"]}
        article_by_id = {article["id"]: article for article in library["articles"]}
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
                    if not card.get("routeBridge"):
                        target = article_by_id[card["articleId"]]
                        basis = card["relationBasis"]
                        self.assertEqual(card["questionLabel"], "讀下一篇時比較")
                        self.assertTrue(card["question"])
                        self.assertIn(basis["labels"][0], card["question"])
                        self.assertIn(basis["kind"], {"stock", "group"})
                        self.assertTrue(basis["ids"])
                        self.assertEqual(len(basis["ids"]), len(basis["labels"]))
                        if basis["kind"] == "stock":
                            self.assertTrue(set(basis["ids"]).issubset(
                                set(article["stockIds"]).intersection(target["stockIds"])
                            ))
                        else:
                            self.assertFalse(
                                set(article["stockIds"]).intersection(target["stockIds"])
                            )
                            self.assertTrue(set(basis["ids"]).issubset(
                                set(article["groups"]).intersection(target["groups"])
                            ))
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
        formal_card = next(
            card for card in topic["learningPath"]["cards"]
            if card.get("articleId") == "formal-1111"
        )
        self.assertEqual(formal_card["relationBasis"], {
            "kind": "stock", "ids": ["1111"], "labels": ["1111 甲公司"],
        })
        self.assertEqual(
            formal_card["question"],
            "回到「1111 甲公司」的公司底稿，哪些是已確認本業，"
            "哪些仍只是本篇的題材情境？",
        )
        graph_card = next(
            card for card in topic["learningPath"]["cards"]
            if card["kind"] == "graph"
        )
        self.assertEqual(graph_card["graphView"], "company")
        self.assertEqual(graph_card["graphViewLabel"], "公司曝險")
        self.assertEqual(graph_card["meta"], "公司曝險 · 2 個節點 · 1 條關係")
        self.assertEqual(graph_card["guidedRelation"], {
            "edgeId": "E1", "fromLabel": "甲公司", "toLabel": "測試主題",
            "relationLabel": "供應測試角色", "evidenceLabel": "證實",
            "commercialStageLabel": "量產前驗證",
            "boundary": "公司角色不等於具名量產訂單。",
        })
        self.assertNotIn("3 個節點", graph_card["meta"])
        self.assertNotIn("2 條關係", graph_card["meta"])
        event = next(
            article for article in library["articles"] if article["id"] == "event-tsmc-2026q2"
        )
        self.assertIn("group", {card["kind"] for card in event["learningPath"]["cards"]})

    def test_graph_learning_card_falls_back_to_an_existing_industry_view(self):
        library = {"counts": {"topic": 1}, "groups": [], "articles": [{
            "id": "topic-industry", "type": "topic", "groups": [], "stockIds": [],
        }]}
        graph = {"graphs": [{
            "id": "industry-only", "label": "產業測試圖",
            "rootNodeId": "concept:test", "articleIds": ["topic-industry"],
            "nodes": [
                {"id": "concept:test", "label": "測試主題"},
                {"id": "industry:power", "label": "功率元件"},
            ],
            "edges": [{
                "id": "I1", "view": "industry",
                "from": "industry:power", "to": "concept:test",
                "relationLabel": "參與產業環節", "evidenceState": "inference",
                "evidenceLabel": "推論", "commercialStageLabel": "研究路由",
                "boundary": "產業關聯不等於公司受惠。",
            }],
        }]}

        bd.attach_research_learning_paths(library, graph)

        card = next(
            card for card in library["articles"][0]["learningPath"]["cards"]
            if card["kind"] == "graph"
        )
        self.assertEqual(card["graphView"], "industry")
        self.assertEqual(card["graphViewLabel"], "產業依賴")
        self.assertEqual(card["meta"], "產業依賴 · 2 個節點 · 1 條關係")
        self.assertEqual(card["guidedRelation"]["edgeId"], "I1")

    def test_learning_article_basis_falls_back_to_shared_group(self):
        library = {
            "counts": {"formal_note": 1, "topic": 1},
            "groups": [{"id": "power", "label": "功率元件", "count": 2}],
            "articles": [
                {
                    "id": "formal-a", "type": "formal_note",
                    "readerTitle": "1111 甲公司 — 質化研究筆記",
                    "subject": "1111 甲公司", "stockIds": ["1111"],
                    "groups": ["power"], "groupLabels": ["功率元件"],
                },
                {
                    "id": "topic-b", "type": "topic",
                    "readerTitle": "另一家公司同族群議題",
                    "stockIds": ["2222"], "groups": ["power"],
                    "groupLabels": ["功率元件"],
                },
            ],
        }

        bd.attach_research_learning_paths(library, {"graphs": []})

        card = next(
            card for card in library["articles"][0]["learningPath"]["cards"]
            if card.get("articleId") == "topic-b"
        )
        self.assertEqual(card["relationBasis"], {
            "kind": "group", "ids": ["power"], "labels": ["功率元件"],
        })
        self.assertEqual(card["questionLabel"], "讀下一篇時比較")
        self.assertEqual(
            card["question"],
            "兩篇都談「功率元件」；下一篇多了什麼市場情境？"
            "哪些內容仍不能套回本篇公司？",
        )

    def test_learning_path_prioritizes_next_registered_route_article(self):
        reading_mission = {
            "orientation": "這是測試文章要先釐清的情境。",
            "question": "讀完後能回答哪個問題？",
            "keyPoints": ["這是測試文章的既有重點。"],
        }
        library = {"counts": {"topic": 3}, "groups": [], "articles": [
            {"id": "topic-a", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第一站", "typeLabel": "市場議題", "readingMinutes": 3,
             "readingMission": reading_mission},
            {"id": "topic-b", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站", "typeLabel": "市場議題", "readingMinutes": 5,
             "readingMission": reading_mission},
            {"id": "topic-b-detail", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站補充", "typeLabel": "市場議題", "readingMinutes": 4},
            {"id": "topic-c", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第三站", "typeLabel": "市場議題", "readingMinutes": 7,
             "readingMission": reading_mission},
        ]}
        graph = {
            "learningRoutes": [{
                "id": "route", "label": "測試路線",
                "description": "依序閱讀", "graphIds": ["graph-a", "graph-b", "graph-c"],
                "phases": [
                    {
                        "id": "foundation", "label": "基礎概念",
                        "graphIds": ["graph-a"],
                    },
                    {
                        "id": "application", "label": "系統應用",
                        "graphIds": ["graph-b", "graph-c"],
                    },
                ],
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
        self.assertEqual(first["routeStep"], 2)
        self.assertEqual(first["routeTotal"], 3)
        self.assertEqual(first["question"], "讀完後能回答哪個問題？")
        self.assertEqual(first["phaseLabel"], "系統應用")
        self.assertEqual(first["phaseStep"], 2)
        self.assertEqual(first["phaseTotal"], 2)
        self.assertEqual(first["routeBridge"], {
            "fromGraphLabel": "第一圖", "fromPhaseLabel": "基礎概念",
            "toGraphLabel": "第二圖", "toPhaseLabel": "系統應用",
        })
        self.assertIn("下一站進入「系統應用」階段", first["description"])
        self.assertIn("測試路線 · 系統應用 · 第 2/3 站", first["meta"])
        self.assertIn("不新增供應鏈或受惠關係", first["description"])
        self.assertEqual(second["articleId"], "topic-c")
        self.assertEqual(second["routeBridge"], {
            "fromGraphLabel": "第二圖", "fromPhaseLabel": "系統應用",
            "toGraphLabel": "第三圖", "toPhaseLabel": "系統應用",
        })
        self.assertIn("下一站仍在「系統應用」階段", second["description"])
        self.assertIn("第 3/3 站", second["meta"])
        self.assertEqual(library["articles"][0]["learningRoute"], {
            "id": "route", "label": "測試路線", "description": "依序閱讀",
            "step": 1, "total": 3, "graphId": "graph-a", "graphLabel": "第一圖",
            "phaseId": "foundation", "phaseLabel": "基礎概念",
            "phaseStep": 1, "phaseTotal": 2,
            "phaseStationStep": 1, "phaseStationTotal": 1,
        })
        stations = graph["learningRoutes"][0]["stations"]
        self.assertEqual(
            [station["articleId"] for station in stations],
            ["topic-a", "topic-b", "topic-c"],
        )
        self.assertEqual(
            [station["graphLabel"] for station in stations],
            ["第一圖", "第二圖", "第三圖"],
        )
        self.assertEqual([station["step"] for station in stations], [1, 2, 3])
        self.assertEqual(
            [station["phaseLabel"] for station in stations],
            ["基礎概念", "系統應用", "系統應用"],
        )
        self.assertEqual([station["phaseStep"] for station in stations], [1, 2, 2])
        self.assertEqual(
            [station["phaseStationStep"] for station in stations], [1, 1, 2])
        self.assertEqual(stations[0]["question"], "讀完後能回答哪個問題？")
        self.assertEqual(stations[1]["articleTitle"], "第二站")
        self.assertEqual(stations[2]["readingMinutes"], 7)
        self.assertEqual(stations[0]["groupLabels"], [])
        self.assertNotIn("learningRoute", library["articles"][2])
        completed = library["articles"][3]["learningPath"]["cards"][0]
        self.assertEqual(completed["kind"], "route")
        self.assertEqual(completed["label"], "已完成這條學習路線")
        self.assertEqual(completed["graphId"], "graph-c")
        self.assertIn("第 3/3 站", completed["meta"])
        self.assertIn("不代表研究結論已完成", completed["description"])

        invalid_graph = {
            "learningRoutes": [{
                "id": "invalid-route", "label": "缺站路線",
                "graphIds": ["graph-a", "graph-b"],
                "phases": [{
                    "id": "only", "label": "只含一站",
                    "graphIds": ["graph-a"],
                }],
            }],
            "graphs": graph["graphs"][:2],
        }
        with self.assertRaisesRegex(ValueError, "逐站、依原順序完整覆蓋"):
            bd.attach_research_learning_paths({"articles": []}, invalid_graph)

        missing_mission = {"counts": {"topic": 1}, "groups": [], "articles": [{
            "id": "topic-a", "type": "topic", "groups": [], "stockIds": [],
        }]}
        with self.assertRaisesRegex(ValueError, "學習路線主文章缺少.*topic-a"):
            bd.attach_research_learning_paths(missing_mission, graph)

        missing_key_points = {"counts": {"topic": 1}, "groups": [], "articles": [{
            "id": "topic-a", "type": "topic", "groups": [], "stockIds": [],
            "readingMission": {
                "orientation": "這篇先釐清的情境。",
                "question": "讀完後能回答哪個問題？",
            },
        }]}
        with self.assertRaisesRegex(ValueError, "缺少可逐字回查的三句重點.*topic-a"):
            bd.attach_research_learning_paths(missing_key_points, graph)

        missing_bridge_labels = {
            "counts": {"topic": 2}, "groups": [], "articles": [
                {"id": "topic-a", "type": "topic", "groups": [], "stockIds": [],
                 "readerTitle": "第一站", "readingMission": reading_mission},
                {"id": "topic-b", "type": "topic", "groups": [], "stockIds": [],
                 "readerTitle": "第二站", "readingMission": reading_mission},
            ],
        }
        missing_bridge_graph = {
            "learningRoutes": [{
                "id": "route", "label": "測試路線",
                "graphIds": ["graph-a", "graph-b"],
            }],
            "graphs": [
                {"id": "graph-a", "label": "第一圖", "articleIds": ["topic-a"]},
                {"id": "graph-b", "label": "", "articleIds": ["topic-b"]},
            ],
        }
        with self.assertRaisesRegex(ValueError, "交接缺少 graph／phase label.*topic-a.*topic-b"):
            bd.attach_research_learning_paths(missing_bridge_labels, missing_bridge_graph)

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

    def test_group_learning_start_prefers_declared_primary_group_then_route_order(self):
        library = {
            "groups": [
                {"id": "passive"}, {"id": "power"}, {"id": "orphan"},
            ],
            "articles": [
                {
                    "id": "topic-power-first", "groups": ["power", "passive"],
                    "readerTitle": "功率優先文章",
                    "learningRoute": {
                        "id": "route-a", "label": "路線 A", "step": 1,
                        "total": 2, "graphId": "graph-a", "graphLabel": "第一站",
                        "phaseLabel": "基礎", "phaseStep": 1, "phaseTotal": 2,
                    },
                },
                {
                    "id": "topic-passive-first", "groups": ["passive", "power"],
                    "readerTitle": "被動元件優先文章",
                    "learningRoute": {
                        "id": "route-a", "label": "路線 A", "step": 2,
                        "total": 2, "graphId": "graph-b", "graphLabel": "第二站",
                        "phaseLabel": "應用", "phaseStep": 2, "phaseTotal": 2,
                    },
                },
                {"id": "topic-unrouted", "groups": ["passive"]},
            ],
            "knowledgeGraph": {
                "learningRoutes": [{
                    "id": "route-a", "label": "路線 A",
                    "question": "這條路線要回答什麼？",
                }],
            },
            "groupMaturity": {
                "summary": {"groups": 3},
                "rows": [
                    {"id": "passive", "label": "被動元件"},
                    {"id": "power", "label": "功率元件"},
                    {"id": "orphan", "label": "尚無路線"},
                ],
            },
        }

        bd.attach_group_learning_starts(library)

        rows = {row["id"]: row for row in library["groupMaturity"]["rows"]}
        self.assertEqual(
            rows["passive"]["learningStart"]["articleId"],
            "topic-passive-first",
        )
        self.assertEqual(rows["passive"]["learningStart"]["scope"], "primary_group")
        self.assertEqual(rows["passive"]["learningStart"]["phaseLabel"], "應用")
        self.assertEqual(rows["passive"]["learningStart"]["phaseStep"], 2)
        self.assertEqual(rows["passive"]["learningStart"]["phaseTotal"], 2)
        self.assertEqual(rows["passive"]["articleCount"], 3)
        self.assertEqual(
            rows["power"]["learningStart"]["articleId"], "topic-power-first")
        self.assertIsNone(rows["orphan"]["learningStart"])
        self.assertEqual(
            library["groupMaturity"]["summary"]["groupsWithLearningStart"], 2)
        self.assertIn("不是熱門度", library["groupMaturity"]["learningBoundary"])
        guide = library["groupMaturity"]["learningRoutes"][0]
        self.assertEqual(guide["question"], "這條路線要回答什麼？")
        self.assertEqual(guide["firstArticleId"], "topic-power-first")
        self.assertEqual(guide["firstGraphLabel"], "第一站")
        self.assertEqual(guide["stationCount"], 2)
        self.assertEqual(guide["groupIds"], ["passive", "power"])
        self.assertEqual(guide["groupLabels"], ["被動元件", "功率元件"])

    def test_registered_learning_route_phases_cover_every_graph_in_order(self):
        for route in bd.RESEARCH_LEARNING_ROUTES:
            phases = route.get("phases") or []
            self.assertTrue(phases, route["id"])
            self.assertEqual(
                [graph_id for phase in phases for graph_id in phase["graphIds"]],
                route["graphIds"],
                route["id"],
            )
            self.assertEqual(
                len({phase["id"] for phase in phases}), len(phases), route["id"])
            for phase in phases:
                self.assertTrue(phase["label"].strip(), route["id"])
                self.assertTrue(phase["graphIds"], route["id"])

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

    def test_research_group_guide_covers_every_formal_group_and_reaches_matrix_rows(self):
        with (ROOT / "config" / "groups.csv").open(encoding="utf-8", newline="") as handle:
            formal_ids = [row["group"] for row in csv.DictReader(handle)]
        guide = bd.load_research_group_guide(strict=True)
        self.assertEqual(list(guide), formal_ids)
        for group_id, item in guide.items():
            self.assertTrue(item["readerRole"].endswith("。"), group_id)
            self.assertTrue(item["readerBoundary"].endswith("。"), group_id)

        maturity = bd.build_group_maturity(
            self.notes, [], self.stock_meta, {"power": "功率元件"},
            {"graphs": []}, [], {}, "2026-08-06",
            group_guide={"power": guide["power"]},
        )
        row = maturity["rows"][0]
        self.assertEqual(row["readerRole"], guide["power"]["readerRole"])
        self.assertEqual(row["readerBoundary"], guide["power"]["readerBoundary"])

    def test_research_reader_terms_are_strict_and_reach_library_payload(self):
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        self.assertIn("load_research_reader_terms(strict=True)", builder)
        self.assertIn("reader_terms=research_reader_terms", builder)
        terms = bd.load_research_reader_terms(strict=True)
        self.assertEqual(
            [term["id"] for term in terms],
            [
                "bom", "reference_design", "sample", "qualification", "pilot",
                "production", "full_scale", "hvm", "tam", "asp",
            ],
        )
        for term in terms:
            self.assertTrue(term["aliases"], term["id"])
            self.assertTrue(term["definition"].endswith("。"), term["id"])
            self.assertTrue(term["boundary"].endswith("。"), term["id"])

        library = bd.build_research_library(
            self.notes, self.reports, self.topics, self.stock_meta,
            {"power": "功率元件"}, reader_terms=terms,
        )
        self.assertEqual(library["readerTerms"], terms)
        library["readerTerms"][0]["aliases"].append("mutated")
        self.assertNotIn("mutated", terms[0]["aliases"])

        with tempfile.TemporaryDirectory() as tmp:
            invalid = Path(tmp) / "research_reader_terms.csv"
            invalid.write_text(
                "term_id,label,aliases,definition,boundary\n"
                "first,第一詞,BOM,第一個解釋。,第一個邊界。\n"
                "second,第二詞,bom,第二個解釋。,第二個邊界。\n",
                encoding="utf-8",
            )
            with mock.patch.object(bd, "RESEARCH_READER_TERMS", str(invalid)):
                with self.assertRaisesRegex(ValueError, "alias 重複"):
                    bd.load_research_reader_terms(strict=True)

    def test_research_topic_guide_is_chinese_first_and_covers_published_topics(self):
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        self.assertIn("load_research_topic_guide(strict=True)", builder)
        self.assertIn("attach_research_topic_guide(", builder)
        guide = bd.load_research_topic_guide(strict=True)
        self.assertEqual(len(guide), 35)
        for article_id, item in guide.items():
            question = item["readerQuestion"]
            self.assertTrue(question.endswith("？"), article_id)
            self.assertGreaterEqual(len(question), 18, article_id)
            self.assertLessEqual(len(question), 56, article_id)
            self.assertNotRegex(question, r"[A-Za-z`]", article_id)

        notes = bd.load_notes(bd.NOTES_DIR)
        reports = bd.load_hypothesis_reports(bd.HYPOTHESES_DIR, notes=notes)
        as_of = bd.research_today()
        topics = bd.load_research_topics(
            bd.TOPICS_DIR, reports=reports, as_of=as_of,
        )
        with (ROOT / "config" / "groups.csv").open(encoding="utf-8", newline="") as handle:
            group_names = {row["group"]: row["name"] for row in csv.DictReader(handle)}
        library = bd.build_research_library(
            notes, reports, topics, {}, group_names, bd.load_events(), as_of=as_of,
        )
        formal_articles = [
            article for article in library["articles"]
            if article["type"] == "formal_note"
        ]
        narrative_articles = [
            article for article in library["articles"]
            if article["type"] == "narrative"
        ]
        self.assertTrue(formal_articles)
        self.assertTrue(narrative_articles)
        self.assertTrue(all(
            article.get("readingMission", {}).get("sourceLabel") == "30 秒摘要"
            and 1 <= len(article["readingMission"].get("keyPoints") or []) <= 3
            for article in formal_articles
        ))
        self.assertTrue(all(
            article.get("readingMission", {}).get("sourceLabel") == "勝負手"
            and len(article["readingMission"].get("keyPoints") or []) == 3
            for article in narrative_articles
        ))
        bd.attach_research_topic_guide(library, guide, strict=True)
        published = {
            article["id"]: article for article in library["articles"]
            if article["type"] == "topic"
        }
        self.assertEqual(set(published), set(guide))
        self.assertTrue(all(article.get("readerQuestion") for article in published.values()))
        memory = published["topic-MI-2026-08-02-AI-MEMORY-HIERARCHY"]
        self.assertEqual(
            memory["readerQuestion"],
            "人工智慧資料為什麼要分層存放，越常用的資料就一定要離運算晶片越近嗎？",
        )
        self.assertIn("人工智慧資料為什麼要分層存放", memory["readerTitle"])
        self.assertIn(memory["readerQuestion"].lower(), memory["searchText"])

        with tempfile.TemporaryDirectory() as tmp:
            invalid = Path(tmp) / "research_topic_guide.csv"
            invalid.write_text(
                "article_id,reader_question\n"
                "topic-test,AI 題目為何難懂？\n",
                encoding="utf-8",
            )
            with mock.patch.object(bd, "RESEARCH_TOPIC_GUIDE", str(invalid)):
                with self.assertRaisesRegex(ValueError, "必須先用中文概念"):
                    bd.load_research_topic_guide(strict=True)

    def test_topic_reader_copy_does_not_expose_opaque_group_ids(self):
        opaque = re.compile(
            r"(?<![a-z0-9])(?:passive|powersupply|serverodm|semiequip|packtest|ipdesign)"
            r"(?![a-z0-9-])",
            re.I,
        )
        source = [{
            "h": "passive 與 powersupply",
            "blocks": [{"t": "p", "runs": [{
                "s": "passive、powersupply、serverodm；passive-component",
                "a": "https://example.com/serverodm",
            }]}],
        }]
        labels = {
            "passive": "被動元件", "powersupply": "電源供應",
            "serverodm": "伺服器組裝/機構",
        }
        rendered = bd._reader_group_labels_in_sections(source, labels)
        self.assertEqual(rendered[0]["h"], "被動元件 與 電源供應")
        self.assertEqual(
            rendered[0]["blocks"][0]["runs"][0]["s"],
            "被動元件、電源供應、伺服器組裝/機構；passive-component",
        )
        self.assertEqual(
            rendered[0]["blocks"][0]["runs"][0]["a"],
            "https://example.com/serverodm",
        )
        self.assertEqual(source[0]["h"], "passive 與 powersupply")

        notes = bd.load_notes(bd.NOTES_DIR)
        reports = bd.load_hypothesis_reports(bd.HYPOTHESES_DIR, notes=notes)
        as_of = bd.research_today()
        topics = bd.load_research_topics(
            bd.TOPICS_DIR, reports=reports, as_of=as_of,
        )
        with (ROOT / "config" / "groups.csv").open(encoding="utf-8", newline="") as handle:
            group_names = {row["group"]: row["name"] for row in csv.DictReader(handle)}
        library = bd.build_research_library(
            notes, reports, topics, {}, group_names, bd.load_events(), as_of=as_of,
        )

        def visible_text(value, key=None):
            if isinstance(value, list):
                return " ".join(visible_text(item) for item in value)
            if isinstance(value, dict):
                return " ".join(
                    visible_text(item, item_key) for item_key, item in value.items()
                )
            return value if isinstance(value, str) and key in {"s", "h"} else ""

        for article in library["articles"]:
            if article["type"] == "topic":
                self.assertNotRegex(
                    visible_text(article["sections"]), opaque, article["id"],
                )

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
            "function articleReaderHeading(", "article.readerQuestion",
            "先學一件事", "讀完能回答", "證據位置：", "這篇先弄懂",
            "研究題名：", "研究範圍：",
            ".result-reader-question", ".article-reader-heading",
            "aria-label=\"搜尋研究文章\"", "filtersPanel.inert", "clearArticleRoute",
            "aria-label=\"研究文章清單\"", ":focus-visible", "@media(max-width:780px)",
            "研究摘要：已知、未知與下一步", "function resetReaderScroll()",
            "ARTICLE_AUDIT_HEADINGS", "function renderResearchAppendix(",
            "研究查核附錄：來源、主張與追蹤", "function renderLearningPath(",
            "function focusReadingTarget(", "function focusBeginnerHighlights(",
            "function focusReadingMissionSource(", "function renderReadingMission(",
            "function readingMissionStartsWithRole(", "function focusArticleRoleContext(",
            "function focusReadingMissionStart(",
            "reading-mission-grid", "'data-testid':'reading-mission-start'",
            "'data-reading-start':roleFirst?'role':'source'", "先看產業角色",
            "開始讀三句重點", "先抓住一個重點，再帶著問題讀",
            "先抓住這個重點", "讀完能回答", "為什麼值得讀",
            "lead=(mission.keyPoints||[]).find(Boolean)||mission.orientation",
            "function readerMissionLeadNodes(", "reading-mission-clause-break",
            "function readingMissionNotationGuide(", "mission?.readerNotations||[]",
            "data-reading-mission-notation-count", "先解碼這段的 ",
            "const notationGuide=readingMissionNotationGuide(mission)",
            ".reading-mission-notation>summary{min-height:44px;",
            "event.preventDefault();fold.open=!fold.open});return fold",
            "reading-mission-why", "需要更多脈絡時再展開",
            "三句重點之後，再比較本文族群角色與所在學習階段。",
            ".reading-mission-start{width:100%;min-height:44px}",
            ".article-learning-origin{display:none}",
            "function articleGroupGuideRows(", "function renderArticleRoleContext(",
            "'data-testid':'article-role-context'", "article-role-context",
            "'data-testid':'article-role-next'", "article-role-next",
            "function articleRoleCard(", "function articleRoleGrid(",
            "'data-testid':'article-role-card-'", "article-role-grid",
            "'aria-labelledby':titleId", "角色說明",
            "if(radarContext)section.append(articleRoleQuestionGrid(rows,radarContext),articleRoleGuideFold(rows))",
            "else if(rows.length<=4)section.appendChild(articleRoleGrid(rows))",
            "再比較其餘 ", "一次展開全部角色說明，不必逐一切換",
            ".article-role-more[open]",
            "並列只表示本文同時討論這些族群，不代表上下游、受惠、訂單或投資排序。",
            "function orderedBeginnerGroups(", "BEGINNER_BLOCK_ORDER",
            "function beginnerGlossary(", "beginner-glossary-state",
            "function beginnerGlossaryTerms(", "function articleGlossaryTerms(",
            "function glossaryTokenPosition(", "function beginnerKeyPointMatches(",
            "const READER_TERMS=LIB.readerTerms||[]", "function sharedReaderTermMatches(",
            "function beginnerKeyPointBoundary(",
            "function readerTermDefinitionList(", "function beginnerKeyPoints(",
            "article=byId.get(state.selected)",
            "第 1 句 · 先看資料", "第 2 句 · 再補脈絡", "第 3 句 · 最後看邊界",
            "topicGuide?topicRoles[index]:null",
            "function readingMissionTermGuide(", "data-reading-mission-term-count",
            "data-reading-mission-article-term-count", "先認得這兩句的 ",
            "const termGuide=readingMissionTermGuide(lead,mission.question,glossaryTerms)",
            ".reading-mission-terms>summary{min-height:44px;",
            "class:'beginner-keypoints'", "data-keypoint-term-count",
            "data-keypoint-shared-term-count", "研究中心共通語",
            "先看懂這句的 ", "解釋逐字取自本篇「名詞小字典」；不另外改寫。",
            "共通語只解釋研究流程與常見指標的字面",
            ".beginner-keypoint-terms>summary{min-height:44px}",
            "articleSections(article,'beginner-highlights',glossaryTerms)",
            "articleSections(article,'beginner-followup',glossaryTerms)",
            "beginnerHighlights&&group.heading!=='三句話抓重點'",
            "beginnerFollowup&&group.heading==='三句話抓重點'",
            "beginner-followup", "再補重要性、名詞與追蹤",
            "function appendBeginnerWhy(parent,items)",
            "beginnerFollowup&&group.heading==='為什麼重要'",
            "rendered.dataset.readerLead='true'",
            ".beginner-why-paragraph.has-reader-lead>strong:first-child",
            ".beginner-highlights+.article-role-context{margin-top:12px}",
            "名詞小字典'+(termCount?'（'+termCount+' 個）':'')",
            "遇到陌生詞再展開，不用一次背完",
            "function renderGlossaryQuickView(", "articleGlossaryDialog",
            "function setupGlossaryQuickAction(", "glossaryQuickReturnFocus",
            "內容逐字取自本篇「新手先讀」名詞小字典；不新增解釋。",
            "id:'glossaryQuickStatus','aria-live':'polite'",
            "'aria-haspopup':'dialog'", "floating-glossary-action",
            "outline-glossary-action", "placeholder:'例如：CXL、HBM'",
            "function researchSummaryEntries(", "function articleResearchSummary(",
            "function researchSummaryGrid(", "RESEARCH_SUMMARY_KINDS",
            "research-summary-grid", "data-summary-kind",
            "role:'list','aria-label':'研究摘要重點'",
            "function evidenceReadingGuide(section,article)",
            "新手證據讀法", "先分清兩把尺",
            "data-claim-key", "data-confidence-key",
            "主張類型與證據可信度", ".evidence-reading-guide",
            ".evidence-reading-scales{grid-template-columns:1fr}",
            "confidence?.effective||guide.confidenceKey",
            "降級只表示證據需要更新，不代表主張已被推翻",
            "從這篇接著學", "function openLearningGroups(",
            "function openLearningCollection(", "learning-path-grid",
            ".learning-path{container-type:inline-size",
            "@container (max-width:620px){.learning-handoff,.learning-path-grid{grid-template-columns:1fr}",
            "function learningCheckpoint(", "function learningCard(",
            "function learningRouteBridge(", "learning-route-bridge",
            "本篇與下一站的閱讀順序", "data-route-from-graph",
            "把兩站串起來 · 閱讀順序",
            "只表示學習次序，不代表供應鏈、受惠或因果關係。",
            "function learningRelationPreview(", "一條既有關係示範",
            "先看一條既有關係", "先別外推到哪裡",
            "data-graph-view", "data-guided-edge",
            "card.graphView,card.guidedRelation?.edgeId",
            "查看'+(card.graphViewLabel||'產業關聯')+'圖",
            ".learning-relation-boundary>summary{min-height:44px}",
            "你能用自己的話回答嗎？", "sourceLabel=mission.sourceLabel||'三句重點'",
            "text:'需要提示？查看本文'+sourceLabel",
            "text:'提示逐字取自本篇「'+sourceHeading+'」；不新增或改寫結論。'",
            "繼續第 '+card.routeStep+'/'+card.routeTotal+' 站",
            "text:'回看本篇'+sourceLabel",
            "review.addEventListener('click',()=>focusReadingMissionSource(article,'review'))",
            "start.addEventListener('click',()=>focusReadingMissionStart(article))",
            "target.focus();requestAnimationFrame",
            "window.scrollTo({top:window.scrollY+target.getBoundingClientRect().top-120",
            ".learning-checkpoint-hints>summary{min-height:44px}",
            "articleOrigin:null", "function articleOriginContext(",
            "function returnArticleOrigin(", "function renderArticleLearningOrigin(",
            "function renderLearningOriginReturn(",
            "'data-testid':'article-origin-top'",
            "'data-testid':'article-origin-back-top'",
            "'data-testid':'article-origin-back-bottom'",
            "originContext?.mobileBackLabel||'返回研究清單'",
            "selectArticle(value,false,null)",
            ".article-learning-origin", ".learning-origin-return",
            "origin.kind==='radar'", "研究雷達第 '+candidate.rank+' 題",
            "只表示研究資源安排",
            "該題已升格為文章",
            "返回會保留同一張候選卡與閱讀位置",
            "radarPage?.scrollTo({top:Math.max(0,origin.radarScrollTop||0)",
            "只表示路線收錄，不代表上下游或受惠排序",
            "maturity-reading-key", "先選一個想弄懂的問題",
            "這頁的「完成度」怎麼看？", "maturityRouteCards",
            "function renderMaturityLearningRoute(",
            "entry-guide", "第一次來？照三步開始",
            'id="entryMatrix"', 'id="entryTopics"', 'id="entryGraph"',
            "function showEntryGuide()", "function resetEntryScroll()",
            "function openEntrySurface(", "function openEntryTopics()",
            "function renderReaderWelcome(", "reader-welcome-maturity",
            "先選一個系統問題，再打開文章",
            'id="maturityIntroTitle" tabindex="-1"',
            "heading?.focus({preventScroll:true})",
            "text:'延伸學習'",
            "document.body.classList.remove('article-open');selectSurface('library',true)",
        ):
            self.assertIn(marker, template)
        self.assertIn("RESEARCH_TEMPLATE", builder)
        self.assertIn("RESEARCH_OUT", builder)
        self.assertIn("def _research_reading_mission_notations(", builder)
        self.assertIn('reading_mission["readerNotations"] = notations', builder)
        self.assertIn('beginner-section', template)
        self.assertIn("h('details',{class:'beginner-glossary','data-term-count':termCount}", template)
        self.assertIn("if(group.heading==='名詞小字典')sectionEl.appendChild(beginnerGlossary(group))", template)
        self.assertIn("terms.forEach(term=>list.appendChild", template)
        self.assertIn("...runs(term)", template)
        self.assertIn("if(glossaryTerms.length)body.append(renderGlossaryQuickView(glossaryTerms)", template)
        self.assertIn("if(glossaryTerms.length)sticky.appendChild(glossaryQuickAction", template)
        self.assertIn("if(target?.isConnected)target.focus({preventScroll:true})", template)
        self.assertIn("search?.focus({preventScroll:true});restorePosition()", template)
        self.assertIn("if(event.target===dialog)dialog.close()", template)
        self.assertIn("readerTermDefinitionList(matches,'beginner-keypoint-term-list')", template)
        self.assertIn("readerTermDefinitionList(matches,'reading-mission-term-list')", template)
        self.assertIn("if(!matches.length)return null;const articleCount=", template)
        self.assertLess(
            template.index("const notationGuide=readingMissionNotationGuide(mission)"),
            template.index("const termGuide=readingMissionTermGuide(lead,mission.question,glossaryTerms)"),
        )
        self.assertLess(
            template.index("const termGuide=readingMissionTermGuide(lead,mission.question,glossaryTerms)"),
            template.index("if(mission.orientation&&mission.orientation!==lead)"),
        )
        self.assertLess(
            template.index("section=h('section',{class:'reading-mission','aria-labelledby':'readingMissionTitle'},head,grid,actions)"),
            template.index("const notationGuide=readingMissionNotationGuide(mission)"),
        )
        self.assertNotIn("orderedBeginnerBlocks", template)
        self.assertIn("else if(analyst){let guideInserted=false;", template)
        self.assertIn("researchSummaryGrid(item)||block(item)", template)
        self.assertIn("entry.label!==expected[index]", template)
        for label in ("一句話結論", "目前已知", "尚未知道", "對哪些族群有意義", "下一步看什麼"):
            self.assertIn(label, template)
        self.assertIn('新手先讀：這篇在講什麼', template)
        self.assertIn('beginner-toc', template)
        self.assertIn('_article_excerpt(topic.get("summary"))', builder)
        self.assertIn('_research_article_reading_mission(article)', builder)
        self.assertIn('_topic_structured_sections(topic, sections or [], group_names)', builder)
        self.assertIn('"asOf": library_as_of.isoformat()', builder)
        self.assertIn('as_of=research_as_of', builder)
        self.assertIn('taipei_today as research_today', builder)
        self.assertIn('research_html.replace(', builder)
        self.assertIn('research_library["knowledgeGraph"] = build_knowledge_graph(', builder)
        self.assertIn('attach_research_learning_paths(', builder)
        self.assertIn('research_library["candidateRadar"] = load_research_radar(', builder)
        self.assertIn(
            "body.appendChild(mobileBack);const originBar="
            "renderArticleLearningOrigin();if(originBar)body.appendChild(originBar);"
            "body.appendChild(articleReaderHeading(article))",
            template,
        )
        self.assertIn(
            "body.appendChild(verification);const readingMission=renderReadingMission(article,glossaryTerms);"
            "if(readingMission)body.appendChild(readingMission);",
            template,
        )
        self.assertIn(
            "if(readingMission)body.appendChild(readingMission);const boundaryBrief="
            "renderReaderBoundaryBrief(article,glossaryTerms);if(boundaryBrief)body.appendChild(boundaryBrief);"
            "const roleContext=renderArticleRoleContext(article);",
            template,
        )
        self.assertLess(
            template.index("const readingMission=renderReadingMission(article,glossaryTerms)"),
            template.index("const meta=h('div',{class:'article-meta'}"),
        )
        # 三句重點後立刻建立族群角色與路線位置，再補 metadata 與其餘新手內容。
        self.assertIn(
            "const routeContext=renderLearningRouteContext(article),mobileProgress="
            "renderMobileReadingProgress(article);body.appendChild(articleSections(article,'beginner-highlights',glossaryTerms));"
            "if(roleContext)body.appendChild(roleContext);if(routeContext)body.appendChild(routeContext);"
            "body.appendChild(meta);body.appendChild(articleSections(article,'beginner-followup',glossaryTerms));"
            "if(mobileProgress)body.appendChild(mobileProgress);"
            "body.appendChild(articleSections(article,'analyst'))",
            template,
        )
        self.assertLess(
            template.index("body.appendChild(articleSections(article,'beginner-highlights',glossaryTerms))"),
            template.index("if(roleContext)body.appendChild(roleContext)"),
        )
        self.assertLess(
            template.index("if(roleContext)body.appendChild(roleContext)"),
            template.index("body.appendChild(articleSections(article,'beginner-followup',glossaryTerms))"),
        )
        self.assertNotIn("先別急著記名詞，先掌握問題", template)
        self.assertNotIn("article-role-choice", template)
        self.assertNotIn("article-role-preview", template)
        self.assertIn(
            "body.appendChild(articleSections(article,'reader',glossaryTerms))", template)
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
        self.assertIn("renderAll();if(byId.has(deepLink))focusArticleHeading(deepLink)", template)
        self.assertIn("if(!open){state.selected=null;return null}", template)
        self.assertNotIn("if(!state.selected||!rows.some(article=>article.id===state.selected)){state.selected=rows[0].id", template)
        self.assertIn("function hashArticleId()", template)
        self.assertIn("url.hash=article.id", template)
        self.assertNotIn("github.com/DennisLiuCk/strong-weak-scanner/blob/main/notes/qualitative/8261", template)

    def test_mobile_reading_mission_puts_the_start_action_before_the_reflection_question(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "'data-mission-question':'reflection'",
            "desktopFollowup=roleFirst?",
            "mobileFollowup=roleFirst?'先看產業角色；下方問題留作讀後檢查。':"
            "'先讀三句重點；下方問題留作讀後檢查。'",
            "reading-mission-followup-desktop",
            "reading-mission-followup-mobile",
            ".reading-mission{display:flex;flex-direction:column;padding:12px 13px 10px}",
            ".reading-mission-grid{display:contents}",
            ".reading-mission-item:first-child{order:1}",
            ".reading-mission-actions{order:2",
            ".reading-mission-item[data-mission-question=\"reflection\"]{order:3;margin-top:8px}",
            ".reading-mission-followup-desktop{display:none}",
            ".reading-mission-followup-mobile{display:inline}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            '.reading-mission-item[data-mission-question="reflection"]{display:none}',
            template,
        )

    def test_reader_surfaces_existing_conclusion_boundary_before_technical_detail(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function researchSummaryEntries(node)",
            "function articleResearchSummary(article)",
            "function focusResearchSummary(sectionIndex)",
            "function renderReaderBoundaryBrief(article,glossaryTerms=[])",
            "'data-testid':'reader-boundary-brief'",
            "'data-testid':'reader-boundary-summary-action'",
            "'data-testid':'reader-boundary-glossary-action'",
            "'aria-controls':'articleGlossaryDialog'",
            "查本文名詞（'+glossaryTerms.length+'）",
            "openGlossaryQuickView(glossaryAction)",
            "['thesis','現在能說']",
            "['unknown','還不能說']",
            "['next','接著查什麼']",
            "這篇目前能說到哪裡",
            "先確認結論、限制與下一份證據，再進入技術細節。",
            "三張卡逐字重用同篇研究摘要；這裡只前移閱讀順序，不改寫主張、證據或判定。",
            ".reader-boundary-grid{grid-template-columns:1fr}",
            ".reader-boundary-buttons{grid-template-columns:1fr}",
            "heading.focus({preventScroll:true})",
        ):
            self.assertIn(contract, template)
        self.assertLess(
            template.index("const boundaryBrief=renderReaderBoundaryBrief(article,glossaryTerms)"),
            template.index("body.appendChild(articleSections(article,'beginner-highlights',glossaryTerms))"),
        )
        self.assertIn("const parsed=researchSummaryEntries(node)", template)
        self.assertNotIn("text:'現在能說到哪裡？'", template)

    def test_topic_reader_maps_authored_section_leads_before_dense_prose(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readerSectionMapItems(section)",
            "if(block.t!=='p')break",
            "if(!lead?.b)break",
            "return items.length>=3?items:[]",
            "function readerSectionMap(section,index)",
            "'data-reader-section-map':section.h||''",
            "'data-reader-section-map-count':items.length",
            "'data-reader-section-map-step':itemIndex+1",
            "本節先看",
            "先把這 '+items.length+' 個重點放在一起",
            "先比較它們負責什麼、哪裡不同，再往下讀完整說明。",
            "重點逐字沿用本節原文；編號只表示出現順序，不代表重要性、上下游或因果關係。",
            "showReaderAids=mode==='reader'&&article.type==='topic'&&!audit",
            "sectionMap=showReaderAids?readerSectionMap(section,index):null",
            "if(sectionMap)sectionEl.appendChild(sectionMap);if(guide)sectionEl.appendChild(guide)",
            ".reader-section-map-steps{display:grid",
            "@container (max-width:480px){.reader-section-map-head{grid-template-columns:1fr}",
        ):
            self.assertIn(contract, template)
        reader_render = template.index("const showReaderAids=mode==='reader'")
        self.assertLess(
            template.index("if(sectionMap)sectionEl.appendChild(sectionMap)", reader_render),
            template.index("if(guide)sectionEl.appendChild(guide)", reader_render),
        )
        self.assertNotIn("section.readerSectionMap", template)

    def test_formal_and_narrative_reading_actions_do_not_skip_industry_role_context(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readingMissionStartsWithRole(article)",
            "article?.type==='formal_note'||article?.type==='narrative'",
            "articleGroupGuideRows(article).length>0",
            "function focusArticleRoleContext()",
            "document.querySelector('.article-role-context h2')",
            "function focusReadingMissionStart(article)",
            "if(readingMissionStartsWithRole(article)){focusArticleRoleContext();return}",
            "focusReadingMissionSource(article,'start')",
            "'data-reading-start':roleFirst?'role':'source'",
            "text:roleFirst?'先看產業角色'",
            "'data-testid':'article-role-next'",
            "String(mission.startLabel||'開始讀正文').replace(/^開始/,'接著')",
            "角色看完後，再回到同篇原文檢查證據。",
            "action.addEventListener('click',()=>focusReadingMissionSource(article,'start'))",
            ".article-role-next .reading-mission-start{width:100%;min-height:44px}",
        ):
            self.assertIn(contract, template)
        # 市場議題仍先去既有三句重點；沒有正式族群指南時也直接退回原來源段落。
        self.assertIn("focusReadingMissionSource(article,'start')", template)
        self.assertNotIn("article.roleFirst=", template)

    def test_promoted_topic_role_questions_follow_the_article_across_entry_paths(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function articleRadarRoleContext(article)",
            "originCandidate?.articleId===article.id?originCandidate:",
            "directCandidates=(RADAR.candidates||[]).filter(item=>item.articleId===article.id",
            "directCandidates.length===1?directCandidates[0]:null",
            "candidate.readerGroupQuestions||[]",
            "function articleRoleQuestionGrid(rows,radarContext)",
            "'data-testid':'article-role-question-'",
            "'data-role-question-source':'radar'",
            "text:'本文先問'",
            "function articleRoleGuideFold(rows)",
            "需要背景？再看平常角色與界線",
            "完整保留 '+rows.length+' 個族群的通用說明",
            "先分清：本文每個族群要回答什麼？",
            "先把本文問題分給各角色；需要背景時，再展開平常職責與最容易混淆的界線。",
            "articleRoleQuestionGrid(rows,radarContext),articleRoleGuideFold(rows)",
            "個問句逐字取自同一篇升格前的研究雷達候選",
            ".article-role-question-grid{display:grid",
            ".article-role-guide-fold>summary{min-height:44px",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            "if(origin?.kind!=='radar'&&origin?.kind!=='maturity-radar')return null",
            template,
        )
        self.assertNotIn("article.radarRoleQuestions", template)

    def test_promoted_topics_use_authored_reader_leads_in_why_it_matters(self):
        expectations = {
            "2026-08-09_ai_rack_emc_certification.md": (
                "**先看問題怎麼從單機變成整櫃。**",
                "**別把元件測試當成整櫃合規。**",
                "**再拆開每一層的責任。**",
                "**最後用三個責任盒查證。**",
            ),
            "2026-08-09_ai_storage_data_plane.md": (
                "**三種工作像三種物流。**",
                "**資料放在哪裡，也會改變硬體需求。**",
                "**最後才把平台需求接回公司。**",
            ),
        }
        for filename, leads in expectations.items():
            source = (ROOT / "notes" / "research_topics" / filename).read_text(
                encoding="utf-8"
            )
            why = source.split("### 為什麼重要", 1)[1].split(
                "### 接下來怎麼追", 1
            )[0]
            for lead in leads:
                self.assertIn(lead, why)

    def test_promoted_topics_keep_first_reader_section_labels_in_plain_chinese(self):
        expectations = {
            "2026-08-09_ai_rack_emc_certification.md": (
                "**第一道是元件與材料。**",
                "**第二道先確認被測設備範圍。**",
                "**第三道是量測程序與責任。**",
                "**第四道才是實驗室可用量能。**",
                "共模扼流圈、濾波器、屏蔽結構、導電墊片、吸波材與 PCB 佈局",
            ),
            "2026-08-09_ai_storage_data_plane.md": (
                "| 1. 訓練時持續餵資料 |",
                "| 2. 故障前保存進度 |",
                "| 3. 上線或擴充時搬模型 |",
            ),
        }
        for filename, phrases in expectations.items():
            source = (ROOT / "notes" / "research_topics" / filename).read_text(
                encoding="utf-8"
            )
            for phrase in phrases:
                self.assertIn(phrase, source)
            self.assertIn(
                "evidence: editorial:reader_section_leads_plain_language", source
            )
        emc = (ROOT / "notes" / "research_topics" /
               "2026-08-09_ai_rack_emc_certification.md").read_text(encoding="utf-8")
        self.assertNotIn("**第二道是 equipment scope。**", emc)
        self.assertNotIn("**第三道是 measurement procedure 與責任。**", emc)
        self.assertNotIn("**第四道才是可用 capacity。**", emc)

    def test_template_brings_existing_glossary_terms_to_each_reader_section(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function glossaryTermLabel(term)",
            "function sectionBlockText(node)",
            "function glossarySearchTokens(label)",
            "function sectionHasGlossaryTerm(text,label)",
            "function sectionGlossaryGuide(section,terms)",
            "'data-section-glossary':section.h||''",
            "'data-glossary-term':entry.fullLabel",
            "'aria-haspopup':'dialog','aria-controls':'articleGlossaryDialog'",
            "'aria-label':'查看本文名詞定義：'+entry.fullLabel",
            "openGlossaryQuickView(button,entry.fullLabel)",
            "詞名與解釋只取自同篇「名詞小字典」；這裡不新增第二套定義。",
            "articleSections(article,'reader',glossaryTerms)",
            ".section-glossary-term{min-height:38px",
            ".section-glossary-term{min-height:44px",
            "search.value=query;search.dispatchEvent",
            "requestAnimationFrame(restorePosition)",
        ):
            self.assertIn(contract, template)
        self.assertIn("const guide=!audit?sectionGlossaryGuide(section,glossaryTerms):null", template)
        self.assertNotIn("本節名詞由模型", template)

    def test_template_stacks_topic_reader_tables_with_original_column_labels_on_mobile(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const labels=(node.head||[]).map(cell=>displayText(cell).trim())",
            "h('th',{scope:'col'}",
            "'data-label':labels[index]||'欄 '+(index+1)",
            "if(article.type==='topic'&&!audit)sectionEl.querySelectorAll('.table-wrap')",
            "wrap.classList.add('reader-table')",
            ".article-section{container-type:inline-size",
            "@container (max-width:620px)",
            ".article-section .reader-table thead{position:absolute",
            ".article-section .reader-table td::before{content:attr(data-label)",
            "wrap.classList.contains('reader-table')",
            "getComputedStyle(wrap.querySelector('table')).display==='block'",
            "wrap.removeAttribute('tabindex')",
            "markScrollableTables(document.getElementById('reader'))",
            "outlineSpyRefresh();markScrollableTables(document.getElementById('reader'))",
        ):
            self.assertIn(contract, template)
        self.assertIn(
            ".table-wrap[data-scrollable]:not(.reader-table)::before", template)
        self.assertNotIn(
            "class:'table-wrap',tabindex:'0',role:'region'", template)

    def test_template_guides_novices_across_topic_table_columns_without_rewriting_data(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readerTableGuide(table)",
            "const headers=(table?.head||[]).map(runText)",
            "headers.slice(1,-1).join('、')",
            "title:headers.at(-1)",
            "'data-reader-table-step':index+1",
            "'aria-label':'表格閱讀順序'",
            "'data-reader-table-guide':headers.length",
            "新手讀表",
            "一次只讀一列，從左往右",
            "欄名逐字取自原表；這裡只安排閱讀順序，不改寫表格內容、數字或證據邊界。",
            "showTableGuide=mode==='reader'&&article.type==='topic'&&!audit",
            "if(showTableGuide&&item.t==='table')",
            ".reader-table-guide-steps{display:grid",
            ".article-section .reader-table-guide-steps{grid-template-columns:1fr}",
            ".reader-table-guide-steps{grid-template-columns:1fr}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("table?.rows", template)

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

    def test_template_mobile_route_keeps_list_hash_and_learning_origin_consistent(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function setArticleHash(id)",
            "function clearArticleRoute()",
            "setArticleHash('')",
            "mobileBack.addEventListener('click',originContext?returnArticleOrigin:clearArticleRoute)",
            "state.selected=rows[0].id;setArticleHash(state.selected)",
            "if(!rows.length){state.selected=null;if(open)clearArticleRoute();return null}",
            "function graphHashRoute(value)",
            "selectSurface('graph',false)",
            "else{state.articleOrigin=null;state.surface='library';syncSurface();document.body.classList.remove('article-open');applyFocusMode();renderAll()}",
            "if(guide)guide.hidden=!showEntryGuide()",
            "button.dataset.testid==='article-'+state.selected",
            "let catalogReturnPosition=null",
            "catalogReturnPosition={windowTop:window.scrollY,catalogTop:",
            "articleId:id",
            "if(position?.articleId&&byId.has(position.articleId))state.selected=position.articleId",
            "const open=document.body.classList.contains('article-open')",
            "if(open&&state.selected&&byId.has(state.selected))return byId.get(state.selected)",
            "renderAll();const target=",
            "catalog-reader-detached",
            "目前閱讀不在左側結果",
            "這篇由延伸學習開啟；原搜尋與篩選仍保留。",
            "target.scrollIntoView({block:'center',behavior:'instant'})",
            "target.focus({preventScroll:true})",
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
            "body.focus-mode .reader-inner{grid-template-columns:minmax(0,1fr);max-width:720px;gap:0}",
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
        self.assertGreater(
            template.index(
                "body.focus-mode .reader-inner{grid-template-columns:minmax(0,1fr);max-width:720px;gap:0}"
            ),
            template.index("body.focus-mode .reader-inner{max-width:1180px"),
        )

    def test_template_outline_scroll_spy_tracks_reader_and_window_scroll(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function setupOutlineScrollSpy(root)",
            "function setActiveOutlineSection(root,index)",
            "scroll.addEventListener('scroll',schedule",
            "window.addEventListener('scroll',schedule",
            "window.addEventListener('resize',schedule",
            "scroll.getBoundingClientRect().top+70",
            "mobile?160:narrow?",
            "button.setAttribute('aria-current','location')",
            "button.classList.toggle('is-active',active)",
            "'data-section-index':index",
            ".article > .research-appendix[data-section-index]",
            "setupOutlineScrollSpy(root)",
            ".toc button.is-active",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            ".toc button.beginner-toc{border-left-color:var(--teal);"
            "color:var(--teal)",
            template,
        )

    def test_template_keeps_narrow_article_reading_position_sticky(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function articleReadingStops(article)",
            "function openReadingStop(index)",
            "function renderMobileReadingProgress(article)",
            "class:'mobile-reading-progress'",
            "'data-reading-stop-total':total",
            "'data-reading-position':index+1",
            "role:'progressbar'",
            "'aria-valuemin':'1'",
            "'aria-valuemax':total",
            "step.setAttribute('aria-valuenow',String(position))",
            "tracker.style.setProperty('--reading-progress'",
            "'data-section-index':'appendix'",
            ".mobile-reading-progress{display:block;position:sticky;top:58px",
            ".mobile-reading-progress{top:102px",
            ".article-section{scroll-margin-top:160px}",
            ".learning-path{scroll-margin-top:160px",
            ".research-appendix{scroll-margin-top:160px}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("function renderMobileToc(article)", template)
        self.assertNotIn("class:'mobile-toc'", template)

    def test_template_normalizes_chinese_wrap_spaces_and_breaks_dense_prose(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function normalizeReaderAsciiPunctuation(value)",
            "function normalizeReaderRunText(value)",
            "function normalizedReaderRunTexts(nodes)",
            "function readerRunNode(run,text)",
            "function escapeReaderPattern(value)",
            "function formalPositioningReaderText(article,value)",
            "function runs(nodes,{sentenceBreaks=false,textTransform=null}={})",
            "reader-prose-dense",
            "'data-reader-chars':text.length",
            "'data-reader-sentences':sentenceCount",
            "text.length>=120&&sentenceCount>=2",
            "{readableProse:mode==='reader',textTransform}",
            "@container (max-width:860px){.reader-prose-dense .reader-sentence-break{display:block;height:.45em}}",
            ".reader-prose-dense .reader-sentence-break{display:block;height:.55em}",
            "class:'reader-sentence-break','aria-hidden':'true'",
            ".evidence-row{min-width:0",
            ".evidence-name{max-width:100%;overflow-wrap:anywhere",
            "if(mark===','&&!latinPair&&!digitPair)return'，'",
            "if(mark===';'&&!latinPair&&!digitPair)return'；'",
            "replace(/([A-Za-z]),(?=[A-Za-z])/g,'$1, ')",
        ):
            self.assertIn(contract, template)
        # 顯示層只讀 run.s；不改寫發布 payload 或原始 Markdown。
        self.assertIn("String(value==null?'':value)", template)
        self.assertNotIn("run.s=normalizeReaderRunText", template)

    def test_formal_positioning_hides_internal_maintenance_terms_in_reader_view_only(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function formalPositioningReaderText(article,value)",
            "if(article?.type!=='formal_note')return source",
            "groupById.get(groupId)?.label",
            "'本文族群：'+label",
            "replace(/Universe 質化參考/g,'研究中心的公司質化參考')",
            "replace(/\\s+研究中心的公司質化參考/g,'研究中心的公司質化參考')",
            "replace(/查核狀態以 meta 與 `qual_notes\\.py --lint` 為準/g,'查核狀態請以文章上方標示為準')",
            "replace(/`last_updated`/g,'「更新日期」')",
            "replace(/「更新日期」\\s+/g,'「更新日期」')",
            "section.h==='研究定位與重要註記'?value=>formalPositioningReaderText(article,value):null",
            "const rendered=block(item,{readableProse:mode==='reader',textTransform})",
            "normalizedReaderRunTexts(source).map(text=>textTransform?textTransform(text):text)",
        ):
            self.assertIn(contract, template)
        # 只轉換實際建立 DOM 的文字；原始 run、文章 sections 與 payload 都不回寫。
        self.assertNotIn("run.s=formalPositioningReaderText", template)
        self.assertNotIn("article.sections=formalPositioningReaderText", template)

    def test_template_explains_the_reading_purpose_of_research_section_headings(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const FORMAL_SECTION_PURPOSES=new Map([",
            "const NARRATIVE_SECTION_PURPOSES=new Map([",
            "function readerSectionPurpose(article,section)",
            "function readerSectionPurposeNote(article,section,purpose)",
            "mode==='reader'?readerSectionPurpose(article,section):''",
            "if(purpose)sectionEl.appendChild(readerSectionPurposeNote(article,section,purpose))",
            "'data-reader-purpose-type':article.type",
            "'data-reader-purpose-heading':section.h||''",
            "'aria-label':'本節閱讀目的'",
            "text:'這節先看'",
            "把可持續的能力、尚未量化的宣稱與結構風險分開。",
            "這些數字只交代假說形成時的市場位置，不負責證明假說。",
            "把這一則假說拆成主張、來源、可證偽條件、驗證期限與目前判讀。",
            ".article-section-purpose{display:grid",
            ".article-section-purpose strong{padding-top:1px",
        ):
            self.assertIn(contract, template)
        self.assertIn(r"if(/^H\d+｜/.test(heading))", template)
        # 白話目的只在 reader 顯示層產生，不寫回 article.sections 或原始 Markdown。
        self.assertNotIn('section["readerPurpose"]', template)
        self.assertNotIn("section.readerPurpose=", template)

    def test_catalog_leads_every_research_article_type_with_a_reader_question(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function catalogReaderQuestion(article)",
            "article.type==='topic'",
            "article.readerQuestion||''",
            "article.type==='formal_note'||article.type==='narrative'",
            "article.readingMission?.question||''",
            "function catalogSourceLabel(article)",
            "article.type==='formal_note'?'原始摘要：'",
            "article.type==='narrative'?'待驗命題：':'研究題名：'",
            "readerQuestion=catalogReaderQuestion(article)",
            "function catalogLearningLead(article)",
            "(mission.keyPoints||[]).find(Boolean)||mission.orientation||''",
            "function catalogLearningLabel(article)",
            "article.type==='formal_note'?'先認識本業'",
            "article.type==='narrative'?'先看勝負手':'先學一件事'",
            "function catalogLearningPreview(article,readerQuestion)",
            "'data-catalog-learning-id':article.id",
            "text:catalogLearningLabel(article)",
            "text:'讀完能回答'",
            "'data-reader-question-type':article.type",
            "'data-reader-question-id':article.id",
        ):
            self.assertIn(contract, template)
        # 清單只讀取既有導讀欄位，沒有從正文或題名生成新的研究問題。
        self.assertNotIn("article.catalogQuestion=", template)
        self.assertNotIn("article.readingMission.question=", template)

    def test_catalog_cards_explain_evidence_position_and_mobile_preserves_first_screen(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function catalogEvidencePosition(article)",
            "(article.sections||[]).map(section=>section.readerEvidenceGuide).find(Boolean)",
            "parts=[String(article.status||'').trim()].filter(Boolean)",
            "guide?.claimLabel",
            "confidenceText(confidence)",
            "Number.isInteger(guide.sourceCount)",
            "guide.sourceCount+' 份有效來源'",
            "'data-catalog-evidence-id':article.id",
            "text:'證據位置：'",
            ".result-learning-preview{display:grid",
            ".result-evidence{display:grid",
            "function foldCatalogGuideOnNarrow()",
            "const guide=document.getElementById('entryGuide')",
            "window.matchMedia('(max-width:780px)').matches",
            "guide.open=false",
            "不在旋轉或 resize 時覆寫使用者之後的手動狀態",
        ):
            self.assertIn(contract, template)
        # 卡片只重排已發布的導讀、狀態與 readerEvidenceGuide，不回寫研究 payload。
        self.assertNotIn("article.readingMission=", template)
        self.assertNotIn("section.readerEvidenceGuide=", template)
        self.assertNotIn("article.status=", template)

    def test_article_heading_continues_the_catalog_reader_question(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function articleReaderTitleLabel(article)",
            "article.type==='topic'?'研究題名：':'原研究頁名：'",
            "function articleReaderHeading(article)",
            "const readerQuestion=catalogReaderQuestion(article)",
            "'data-reader-heading-type':article.type",
            "'data-reader-heading-id':article.id",
            "tabindex:'-1'",
            "'data-reader-heading-focus':article.id",
            "h('h1',{...headingAttrs,text:readerQuestion})",
            "h('strong',{text:articleReaderTitleLabel(article)})",
            "article.readerTitle",
            "function focusArticleHeading(articleId)",
            "heading.focus({preventScroll:true})",
            "resetReaderScroll();focusArticleHeading(id)",
            ".article h1[data-reader-heading-focus]:focus-visible",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("article.type==='topic'&&article.readerQuestion", template)

    def test_template_explains_why_generic_article_recommendations_connect(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function learningArticleBasis(card)",
            "card.kind!=='article'||card.routeBridge||!labels.length",
            "這兩篇為什麼相連",
            "共同公司",
            "共同族群",
            "'data-relation-basis-kind':kind",
            "'data-relation-basis-count':labels.length",
            "'data-relation-basis-ids':(basis.ids||[]).join('|')",
            "labels.slice(0,3).join('、')",
            "查看全部'+kindLabel",
            "不代表上下游、受惠、訂單或因果關係",
            "const articleBasis=learningArticleBasis(card)",
            "'data-question-label':card.questionLabel||'下一站試著回答'",
            "text:card.questionLabel||'下一站試著回答'",
            ".learning-article-basis{",
            ".learning-article-basis-more>summary{min-height:44px}",
        ):
            self.assertIn(contract, template)

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
            "還不能推到哪裡", "看到什麼才升級", "供應集中度範圍",
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
            'id="graphOrigin"', 'aria-labelledby="graphOriginTitle"',
            'aria-label="知識圖譜學習路線"',
            "const GRAPH_LEARNING_ROUTES=KG.learningRoutes||[]",
            "function availableGraphRoutes()",
            "function graphRouteId(graphId)", "function activateGraphRoute(routeId)",
            "function activateGraphTopic(graphId)",
            "function graphRoutePhase(route,graphId)",
            "parts.push('階段 '+phase.step+'/'+phase.total+' · '+phase.label)",
            "const group=h('optgroup',{label:'階段 '+(index+1)+'/'+phases.length+' · '+phase.label})",
            "graphRoute:graphRouteId((KG.graphs||[])[0]?.id||'')",
            "state.graphRoute=graphRouteId(graphId)",
            "學習路線只整理導覽",
            ".graph-hub-tabs{display:none}", ".graph-hub-select{display:block}",
            "const startArticle=(graph.articleIds||[])",
            "'data-testid':'graph-primary-article'",
            "先讀主題文章 · ",
            "function graphArticleOrigin()",
            "kind:'graph',graphId:state.graphId,graphView:state.graphView",
            "graphSelection:state.graphSelection?{...state.graphSelection}:null",
            "graphScrollTop:graphPage?.scrollTop||0",
            "openGraphArticle(startArticle.id)",
            "selectArticle(articleId,true,graphArticleOrigin())",
            "graphOrigin:null", "function graphLearningOrigin()",
            "kind:'article-learning'", "articleScrollTop:reader?.scrollTop||0",
            "articleWindowTop:window.scrollY||0", "articleOrigin}",
            "function graphLearningNextLabel(article)",
            "function renderGraphOrigin()", "'data-testid':'graph-origin-back'",
            "回到剛才文章", "文章 → 關係圖",
            "function focusGraphOrigin()", "function returnGraphLearningOrigin()",
            "#learningPath .learning-card.kind-graph .learning-card-action",
            "openRadarGraph(graphId,graphView='company',edgeId='',origin=null)",
            "state.graphOrigin=origin", "if(origin)focusGraphOrigin()",
            "card.guidedRelation?.edgeId,graphLearningOrigin()",
            "state.graphOrigin=null;selectSurface('graph')",
            ".graph-origin{display:grid;grid-template-columns:minmax(0,1fr) auto",
            ".graph-origin button{min-height:44px",
            "if(origin.kind==='graph')",
            "返回這張知識圖譜",
            "返回會保留原主題、投影視角與已選關係",
            "state.graphSelection=origin.graphSelection||null",
            "graphPage?.scrollTo({top:Math.max(0,origin.graphScrollTop||0)",
            "function renderLearningRouteContext(article)",
            "'aria-label':'學習路線定位'",
            "階段與站次只代表閱讀順序，不是上下游、研究完成度或投資排名",
            "看這站證據關係",
            "function learningRouteById(routeId)",
            "function learningRoutePhaseGroups(stations)",
            "function learningRouteStationReaderQuestion(station)",
            "function learningRouteStation(route,station,total,currentArticleId,mode)",
            "function learningRouteMap(route,currentArticleId='',mode='article')",
            "'data-testid':'learning-route-map-'+route.id",
            "'data-testid':'learning-route-station-'+route.id+'-'+station.step",
            "byId.get(station.articleId)?.readerQuestion||station.question",
            "sourceQuestion=String(station.question||'').trim()",
            "hasPlainQuestion?'這站先弄懂':'這站先回答'",
            "'data-reader-question':hasPlainQuestion?'article':'route'",
            "h('strong',{text:primary}),h('small',{text:context})",
            "class:'learning-route-station-precise'",
            "'data-testid':'learning-route-precise-'+route.id+'-'+station.step",
            "讀完再試著回答精確追問",
            "h('p',{text:sourceQuestion})",
            "白話問題與精確追問都沿用同篇既有內容",
            "'aria-label':route.label+' 學習階段與站點'",
            "'data-phase-id':phase.id,'data-current':isCurrent?'true':'false'",
            "shouldOpen=isCurrent||(!currentArticleId&&index===0)",
            "class:'learning-route-phase-fold',open:shouldOpen",
            "'data-testid':'learning-route-phase-'+route.id+'-'+phase.step",
            "class:'learning-route-phase-summary'",
            "text:(isCurrent?'目前階段 · ':phase.stations.length+' 站 · ')+range",
            "summary.addEventListener('keydown',event=>{if(event.key!=='Enter'&&event.key!==' ')",
            "event.preventDefault();phaseFold.open=!phaseFold.open",
            "目前第 '+current.step+' 站'+phaseHint",
            "learningRouteMap(learningRouteById(route.id),article.id,'article')",
            "learningRouteMap(learningRouteById(route.id)||route,'','matrix')",
            "每站先沿用同篇既有讀者問句",
            "精確追問仍逐字保留在可展開內容與文章「想一想」",
            ".learning-route-map>summary:focus-visible",
            ".learning-route-phases{display:grid;gap:7px",
            ".learning-route-phase[data-current=\"true\"]",
            ".learning-route-phase-summary{min-height:44px",
            ".learning-route-phase-summary:focus-visible",
            ".learning-route-phase-fold[open] .learning-route-phase-state::before{content:'收合'}",
            ".learning-route-station-button{width:100%;min-height:72px",
            ".learning-route-station-precise>summary{min-height:44px",
            ".learning-route-station-precise>summary:focus-visible",
            "function resetGraphSurfaceScroll()",
            "graphPage.scrollTo(0,0)",
            "window.scrollTo(0,0)",
            "requestAnimationFrame(()=>requestAnimationFrame(reset))",
            "selectSurface('graph',true);resetGraphSurfaceScroll()",
            "if(card.kind==='route')return'回到學習路線'",
            ".graph-intro-action{width:100%;min-height:44px}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("learning-route-phase-head", template)
        self.assertNotIn("讀完試著回答：", template)
        self.assertIn(
            "document.getElementById('graphHubSelect').addEventListener('change'",
            template,
        )
        self.assertIn(
            "other=(KG.graphs||[]).filter(graph=>!known.has(graph.id))", template)
        self.assertNotIn("v2 direct assessment 能進入", template)
        for contract in (
            "RESEARCH_LEARNING_ROUTES", "供電與散熱", "記憶體與封裝",
            "運算與互連", "公司財務案例", "供電、保護與元件",
            '"phases": [', "def route_phase_map(route):",
            "學習路線階段必須逐站、依原順序完整覆蓋 graphIds",
            'research_library["knowledgeGraph"]["learningRoutes"]',
            'route["stations"] = []',
            'article.get("readingMission") or {}',
            "沿學習路線往下讀", "不新增供應鏈或受惠關係",
            "已完成這條學習路線", "first existing articleId",
        ):
            self.assertIn(contract, builder)
        self.assertNotIn("查看完整路線", template)

    def test_template_graph_entry_progressively_discloses_controls(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'details class="graph-learning-key" id="graphLearningKey" open',
            'details class="graph-control-fold" id="graphControlFold">',
            '<span class="graph-control-summary-label">目前這張圖</span>',
            'class="graph-learning-body" aria-labelledby="graphLearningTitle"',
            'class="graph-control-current" id="graphControlCurrent"',
            'class="graph-control-meta" id="graphControlMeta"',
            "function renderGraphControlSummary(graph,route)",
            "evidence=['verified','inference','unverified']",
            "state.graphView==='company'&&state.graphUniverseOnly",
            "renderGraphControlSummary(graph,route);introActions.replaceChildren()",
            "(function foldGraphGuidesOnNarrow()",
            "['graphLearningKey','graphControlFold']",
            "if(fold)fold.open=false",
            "只在載入時收起一次，不覆寫使用者之後的手動狀態",
            ".graph-learning-head:focus-visible,.graph-control-summary:focus-visible",
            ".graph-control-summary{min-height:72px",
            ".graph-chip{min-height:44px}.graph-filter{min-height:44px}",
            ".graph-control-fold[open]>.graph-control-summary{border-bottom:1px solid var(--line2)}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            ".graph-control-fold[open]>.graph-control-summary{display:none}",
            template,
        )

    def test_template_graph_guides_novice_through_existing_edge_fields(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="graphDetail" aria-live="polite" tabindex="-1"',
            "function focusGraphDetail()",
            "detail.focus({preventScroll:true})",
            "selectGraphEdge(id,focusDetail=false)",
            "if(focusDetail)focusGraphDetail()",
            "function graphEvidenceReaderCopy(edge)",
            "來源直接支持這項關係",
            "還不是來源直接確認的關係",
            "不能先當成已確認事實",
            "function graphRelationReader(edge,from,to)",
            "function graphRelationOrigin()",
            "'data-testid':'graph-reader-brief'",
            "'data-testid':'graph-reader-origin'",
            "'data-testid':'graph-reader-origin-back'",
            "graphReaderStep(1,'這條線現在怎麼讀',now)",
            "graphReaderStep(2,'還不能推到哪裡',edge.boundary)",
            "graphReaderStep(3,'看到什麼才升級',edge.nextTrigger)",
            "'data-testid':'graph-reader-article'",
            "(edge.articleIds||[]).map(articleId=>byId.get(articleId)).find(Boolean)",
            "'data-testid':'graph-guided-relation'",
            "edges.find(edge=>edge.evidenceState==='verified'&&!edgeIsStale(edge))",
            "edges.find(edge=>edge.evidenceState==='verified')||edges[0]",
            "selectGraphEdge(guidedEdge.id,true)",
            "button.addEventListener('click',()=>selectGraphEdge(edge.id,true))",
            "示範只用一條既有關係教讀法，不代表重要性、受惠或投資排序",
            "關係：'+edge.relationLabel+' · 證據：'+edge.evidenceLabel+' · 階段：",
            "證據：'+edge.evidenceLabel",
            "商業位置：'+edge.materialityLabel",
            "h('span',{text:'關係解讀'})",
            "完成這條線後",
            "graphLearningNextLabel(article)",
            "button.addEventListener('click',returnGraphLearningOrigin)",
            "這張卡只重排原關係資料，不新增關係或結論",
            ".graph-reader-step",
            ".graph-reader-cta",
            ".graph-reader-origin button{width:100%;min-height:44px",
            "@media(max-height:840px) and (min-width:981px){.graph-detail{position:static;max-height:none;overflow:visible}}",
            ".graph-detail:focus-visible",
            "matchMedia('(prefers-reduced-motion: reduce)')",
            "@media(max-width:780px){.graph-detail{scroll-margin-top:74px}}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("原 edge 欄位", template)

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
            "candidate.readerQuestion", "candidate.readerNextStep",
            "candidate.readerTerms", "questionText=candidate.readerQuestion||candidate.title",
            "這題想弄清楚", "研究題名：", "接著查什麼", "關鍵詞白話解釋",
            "function radarArticleOrigin(", "function openRadarArticle(",
            "radarScrollTop:page?.scrollTop||0", "openRadarArticle(candidate)",
            "function radarReaderStatusLabel(candidate)",
            "promoted:'已有文章與關係圖'", "watch:'等待更多證據'",
            "研究順序 '+candidate.rank", "只排研究待辦，不是股票或投資排名",
            "閱讀這題的文章 · '+article.readingMinutes+' 分鐘",
            ".radar-head-copy", ".radar-technical-title",
            "candidate.groupIds", "candidate.readerGroupQuestions",
            "function renderRadarGroups(",
            "function openRadarGroup(", "function focusMaturityGroup(",
            "先分清：每個族群在這題要回答什麼？", "從研究雷達定位",
            "在這題要回答", "不代表上下游順序",
            ".radar-group-copy", ".maturity-origin-question",
            "'data-radar-group-id':group.id", "state.maturityOrigin",
            "查看研究判定、原始文字與來源",
            "auditBadges,copy,track,foot", "研究方法與稽核資料（供查核）",
            "document.getElementById('surfaceRadar').addEventListener",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("先用一句話理解", template)
        self.assertNotIn("class:'radar-question'", template)
        self.assertIn(".radar-card{display:block", template)
        self.assertIn(".radar-rank{min-height:42px;display:flex;flex-direction:row", template)
        self.assertIn("grid-template-columns:repeat(4,1fr)", template)

    def test_radar_group_matrix_keeps_promoted_question_article_and_return_path(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "state.maturityGuideGroupId=groupId",
            "function maturityRadarArticleOrigin(row,candidate,question)",
            "kind:'maturity-radar'",
            "function openMaturityRadarArticle(row,candidate,question)",
            "candidate?.articleId&&byId.has(candidate.articleId)",
            "function maturityRadarContext(row)",
            "function renderMaturityOrigin(row)",
            "'data-maturity-radar-origin':candidate.id",
            "'data-maturity-radar-group':row.id",
            "maturity-origin-pending",
            "row.label+'在這題要回答'",
            "先讀這篇回答本題",
            "'data-testid':'group-radar-start-'+row.id",
            "先讀本題文章 · ",
            "openMaturityRadarArticle(row,candidate,question)",
            "下方四欄是「'+row.label+'」整體研究盤點，不是本題答案。",
            "origin=renderMaturityOrigin(row);if(origin)readerRow.appendChild(origin)",
            "fromRadar?'start':'center'",
            ".maturity-origin-wide{width:auto;grid-column:1/-1",
            "@media(max-width:1000px) and (min-width:781px){.maturity-origin-wide",
            "@media(max-width:780px){.maturity-origin-wide",
            "讀完本題後 · 族群基礎起點",
            "再讀族群基礎",
            "originCandidate?.articleId===article.id?originCandidate:",
            "item.articleId===article.id",
            "state.articleOrigin?.kind==='maturity-radar'",
            "radarById.get(state.articleOrigin.candidateId)?.articleId!==id",
            "if(state.articleOrigin.kind==='maturity-radar')state.maturityOrigin=null",
            "if(origin.kind==='maturity-radar')",
            "state.maturityOrigin={candidateId:origin.candidateId,groupId:origin.groupId}",
            "state.articleOrigin?.kind==='maturity-group'||state.articleOrigin?.kind==='maturity-radar'",
            ".maturity-origin .maturity-origin-start",
        ):
            self.assertIn(contract, template)
        medium_start = template.index(
            "@media(max-width:1000px) and (min-width:781px){.maturity-origin-wide"
        )
        medium_end = template.index(
            "@media(max-width:780px){.maturity-origin-wide", medium_start
        )
        medium_contract = template[medium_start:medium_end]
        for contract in (
            ".maturity-reader{border:0;background:transparent;overflow:visible}",
            ".maturity-reader-head{display:none}",
            ".maturity-reader-row{grid-template-columns:repeat(2,minmax(0,1fr))",
            ".maturity-reader-cell:nth-of-type(2n){border-right:0}",
            ".maturity-reader-cell:nth-last-child(-n+2){border-bottom:0}",
            ".maturity-reader-cell>small{display:block",
        ):
            self.assertIn(contract, medium_contract)
        self.assertNotIn("wrap.prepend(card)", template)
        self.assertLess(
            template.index("'data-testid':'group-radar-start-'+row.id"),
            template.index("'data-testid':'group-start-'+row.id"),
        )

    def test_template_publishes_group_maturity_matrix_without_a_composite_score(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")
        for contract in (
            'id="surfaceMaturity"', 'id="maturityPage"', 'id="maturitySummary"',
            'id="maturityActionQueue"', 'id="maturityMatrix"',
            "const MATURITY=LIB.groupMaturity", "function renderMaturity()",
            "function renderMaturityAction(", "function focusMaturityAction(",
            "function openGroupResearch(", "deepLink==='maturity'",
            "先從一個想弄懂的問題開始", "族群起點", "開始學這個族群",
            "先選問題，再讀主題，最後追關係", "先選一個系統問題",
            "從四條既有學習路線，看每個問題會用到哪些族群",
            "function renderMaturityGroupStart(", "groupsWithLearningStart",
            "row.readerRole", "row.readerBoundary", "研究中心怎麼分",
            "先別混淆：", ".maturity-group-guide",
            'id="maturityEntrySwitch"', 'data-maturity-entry="routes"',
            'data-maturity-entry="groups"', 'data-maturity-entry-panel="routes"',
            'data-maturity-entry-panel="groups"', "不熟族群名稱",
            "從問題開始", "依族群名稱查找",
            "maturityEntry:'routes'", "function syncMaturityEntry(",
            "function selectMaturityEntry(",
            "panel.hidden=mobile&&panel.dataset.maturityEntryPanel!==selected",
            "state.maturityEntry='groups';selectSurface('maturity',true)",
            "state.maturityEntry='routes';syncMaturityEntry();const cards",
            "state.maturityEntry='groups';syncMaturityEntry();const rows",
            "maturityEntryResizeFrame", ".maturity-entry-switch{display:none}",
            ".maturity-entry-button{min-width:0;min-height:56px",
            "@media(max-width:780px){.maturity-entry-switch{display:grid",
            'id="maturityGroupChoices"', 'id="maturityGroupPreview"',
            "function renderMaturityGroupExplorer(",
            "function renderMaturityGroupPreview(",
            "function maturityRoutesForGroup(", "function focusMaturityRoute(",
            "function maturityGroupArticleOrigin(",
            "function maturityRouteArticleOrigin(",
            "function openMaturityGroupArticle(",
            "function openMaturityRouteArticle(",
            "openMaturityGroupArticle(row,start.articleId)",
            "openMaturityRouteArticle(route,route.firstArticleId)",
            "mode==='matrix'?openMaturityRouteArticle(route,station.articleId)",
            "state.maturityGuideGroupId", "data-maturity-guide-group",
            "'aria-pressed':'false'", "會出現在：", "從第一篇開始",
            "看完整族群進度", "只表示既有閱讀路線收錄",
            ".maturity-group-explorer", ".maturity-group-choice",
            'id="maturityRouteCards"', "function renderMaturityLearningRoute(",
            "MATURITY.learningRoutes", "maturity-route-question",
            "從「'+graphLabel+'」開始", "族群重複出現，表示同一族群會在多個問題中出現",
            "function resetLibrarySurfaceScroll(", "resetLibrarySurfaceScroll()",
            "MATURITY.learningBoundary", 'id="catalogTitle"', "groupScope",
            "selectedGroups.length===1", "最大缺口", "不做總分或名次",
            "可水平捲動的族群研究成熟度矩陣",
            "完整查核矩陣與方法說明", "題材財務影響", "maturitySummarySentence",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            '不熟族群名稱，從「先認識一個族群」開始', template
        )
        self.assertIn("已知道族群名稱？直接查找", template)
        self.assertLess(
            template.index('id="maturityRouteGuideTitle"'),
            template.index('id="maturityGroupExplorerTitle"'),
        )
        for contract in (
            "@media(min-width:781px){.maturity-route-card:has(.learning-route-map[open]){grid-column:1/-1}",
            ".learning-route-phases{grid-template-columns:repeat(auto-fit,minmax(240px,1fr));align-items:start}",
            ".learning-route-map-body>.learning-route-stations{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}",
            "document.getElementById('maturityRouteCards').addEventListener('keydown'",
            "event.target.closest?.('.learning-route-map>summary')",
            "summary.parentElement.open=!summary.parentElement.open",
        ):
            self.assertIn(contract, template)
        self.assertIn("body.article-open .tools{display:none}", template)
        self.assertIn('research_library["groupMaturity"] = build_group_maturity(', builder)
        self.assertIn("load_research_group_guide(strict=True)", builder)
        self.assertIn("group_guide=research_group_guide", builder)
        self.assertIn("def attach_group_learning_starts(", builder)
        self.assertIn('maturity["learningRoutes"] = route_guides', builder)
        self.assertIn('"question": "電力如何送進 AI 機櫃', builder)
        self.assertIn("attach_group_learning_starts(research_library)", builder)
        self.assertIn('candidate_radar=research_library["candidateRadar"]', builder)
        self.assertIn("def build_group_maturity(", builder)

    def test_liquid_cooling_station_eight_separates_capacity_progress_and_income(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_liquid_cooling_qualification_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 液冷設備不能只比容量：平台列名、供應準備與收入是三種不同證據\n"
        ))
        for contract in (
            "editorial_plain_language_wave87_capacity_maturity_evidence_ladder",
            "容量只回答設備在指定條件下設計可帶走多少熱",
            "要判斷誰更接近收入，還要看到客戶驗收、量產數量與公司財務揭露",
            "## 容量可以換算，商業成熟度不能跟著換算",
            "| 2026-08-02 清單中的供應商 | 產品型號 | 來源原始容量 | 換算成 kW | 平台原始供應標籤 | 這一列只能證明 |",
            "## 從規格到收入要過五關",
            "| 先問哪一關 | 這一關能回答什麼 | 本輪已有的公開證據 | 仍然缺什麼 |",
            "| 1. 容量規格 |", "| 2. 平台列名與測試 |",
            "| 3. 供應準備 |", "| 4. 場域整合與客戶部署 |",
            "| 5. 公司收入 |", "## 接下來看到什麼，判定才會改變",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 主張與證據帳本", 1
        )[0]
        self.assertNotIn("Sample Ready", reflection)
        self.assertNotIn("MP Ready", reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 8),
            ("research_claim", 9), ("metric_comparison", 7),
            ("impact", 2), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER,"
            "液冷設備容量比較大，為什麼不代表已量產或有訂單？",
            guide,
        )

    def test_liquid_cooling_station_nine_maps_handoffs_and_evidence_gates_in_plain_language(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-03_liquid_cooling_loop_boundaries.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 液冷不是買完設備就能運作：冷源、管路、伺服器與控制必須共同交接\n"
        ))
        for contract in (
            "editorial_plain_language_wave88_cooling_loop_handoffs_and_evidence_gates",
            "液冷可以先分成三段：機房把熱送走的設施水路",
            "完整部署還要讓冷源、管路、接頭、分流器、冷板、控制與維護一起通過驗收",
            "## 冷源到伺服器要交接五次",
            "| 交接點 | 這一段由誰或什麼負責 | 雙方要說清楚什麼 | 沒說清楚會怎樣 | 本輪依據 |",
            "| 1. 機房設施 ↔ 冷卻設備 |",
            "| 2. 冷卻設備 ↔ 循環水路 |",
            "| 3. 循環水路 ↔ 機櫃分流 |",
            "| 4. 機櫃分流 ↔ 伺服器冷板 |",
            "| 5. 建築控制 ↔ IT 控制 |",
            "## 從文件要求到長期營運要過五關",
            "| 先過哪一關 | 看到什麼才算往前 | 還不能因此判定 |",
            "| 1. 責任與範圍寫清楚 |", "| 2. 零件與設備通過測試 |",
            "| 3. 平台列出具名產品 |", "| 4. 具名場域完成驗收 |",
            "| 5. 長期運作與財務出現 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 27
        )
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 主張與證據帳本", 1
        )[0]
        for jargon in ("FWS", "TCS", "rackLocationId"):
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 6),
            ("research_claim", 7), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES,"
            "液冷系統出問題時，如何分清設備、整合與設施的責任？",
            guide,
        )

    def test_ai_memory_station_one_starts_from_data_roles_and_separates_maturity(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_ai_memory_hierarchy.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 人工智慧資料為什麼要分層存放："
            "正在運算、等待取用與長期保存各有位置\n"
        ))
        for contract in (
            "editorial_plain_language_wave89_memory_layers_and_maturity",
            "人工智慧系統不會把所有資料都塞在同一個地方",
            "架構、樣品、量產與收入必須分開判讀",
            "## 先按資料的急迫程度分四層",
            "| 資料任務 | 本文怎麼分位置 | 為什麼放這裡 | 本輪產品名稱 | 目前不能因此判定 |",
            "| 正在計算、最怕等待的工作資料 |",
            "| 容量較大、仍需快速取用的系統資料 |",
            "| 可以重新建立、也可能需要共享的上下文資料 |",
            "| 容量最大、可接受較慢存取或需長期保存的資料 |",
            "## 四層互補，不是誰取代誰",
            "## 每一層的商業進度要各自驗證",
            "| 資料層或連接路徑 | 已看到的一手證據 | 目前走到哪一步 | 還缺哪些商業證據 |",
            "| 圖形運算晶片旁的高速層（HBM4） |",
            "| 中央處理器旁的系統記憶體（SOCAMM） |",
            "| 共享上下文層（CMX） |",
            "| 記憶體擴充連接（CXL 4.0） |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0].splitlines()[2]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先按資料的急迫程度分四層", 1
        )[0]
        for jargon in ("HBM", "SOCAMM", "CMX", "KV cache", "Rubin"):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 7),
            ("research_claim", 6), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-AI-MEMORY-HIERARCHY,"
            "人工智慧資料為什麼要分層存放，越常用的資料就一定要離運算晶片越近嗎？",
            guide,
        )

    def test_ai_memory_station_two_separates_custom_scope_from_business_progress(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-03_custom_hbm_scope_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 高頻寬記憶體可以客製到哪裡："
            "先分規格、底部晶片與工作搬移\n"
        ))
        for contract in (
            "editorial_plain_language_wave90_custom_scope_and_progress",
            "同樣寫「客製」，公開資料可能在談三種不同改法",
            "把「改了哪裡」和「走到哪一步」分成兩把尺",
            "## 先拆「改了哪裡」，再看「走到哪一步」",
            "### 先用三種範圍讀懂「客製」",
            "| 本文讀法 | 改了什麼 | 可能需要哪些角色一起做 | 本輪可能增加的功能 | 還不能因此判定 |",
            "| 調整記憶體規格 |", "| 重做堆疊底部邏輯 |",
            "| 搬移部分資料整理工作 |",
            "### 再把每家公司放回自己的證據位置",
            "| 公開公司 | 本輪談的是哪種改法 | 已看到的公開證據 | 目前走到哪一步 | 還不能說什麼 |",
            "| 三星（Samsung） |", "| SK 海力士（SK hynix） |",
            "| 美光（Micron） |",
            "一般版本的樣品、客製版本的",
            "不能合併成一條供應商進度排名",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0].splitlines()[2]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先拆「改了哪裡」，再看「走到哪一步」", 1
        )[0]
        for jargon in (
            "HBM", "Stream DQ", "NRE", "qualification", "roadmap",
            "Samsung", "Micron",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 8),
            ("research_claim", 7), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER,"
            "客製高頻寬記憶體只改規格或重做底部晶片，為何不能排在一起？",
            guide,
        )

    def test_ai_memory_station_three_uses_five_commercialization_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_glass_substrate_commercialization.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 玻璃基板從工廠走到穩定出貨："
            "樣品、客戶驗證、良率與訂單不能跳級\n"
        ))
        for contract in (
            "editorial_plain_language_wave91_commercialization_ladder_and_role_handoffs",
            "工廠建好、設備就位與樣品完成，只證明已具備開發和試製能力",
            "商業化還要依序看客戶是否完成可靠度測試",
            "## 先把玻璃基板商業化拆成五關",
            "| 本文五關 | 這一關要回答 | 主要接力角色 | 看到這些仍不能直接跳到下一關 |",
            "| 1. 能力與設備就位 |", "| 2. 交出可測樣品 |",
            "| 3. 完成客戶驗證 |", "| 4. 穩定製造 |",
            "| 5. 重複出貨與收入 |",
            "## 再把四組公開證據放回正確關卡",
            "| 公開公司或合作 | 本輪可確認 | 放在五關哪裡 | 接下來缺什麼 | 不能外推 |",
            "| SKC／Absolics |", "| Samsung Electro-Mechanics |",
            "| Intel／Lens Technology |", "| Corning |",
            "同一家公司的證據可能同時出現在不同關",
            "不替公司排快慢",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先把玻璃基板商業化拆成五關", 1
        )[0]
        for jargon in (
            "HVM", "TGV", "reliability", "production", "pilot",
            "proof sample", "mass-production", "Intel", "Samsung",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 9),
            ("research_claim", 7), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION,"
            "玻璃基板已有工廠與樣品，為什麼還不能算穩定量產？",
            guide,
        )

    def test_ai_memory_station_four_separates_system_conditions_roles_and_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_hbf_commercialization_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 新記憶體層不能只靠大容量："
            "HBF 還要通過讀寫、耐久、系統整合與量產\n"
        ))
        for contract in (
            "editorial_plain_language_wave92_hbf_system_conditions_roles_and_six_gate_ladder",
            "新的記憶體層不能只提供更大容量",
            "目前只能說兩家公司和開放運算計畫正討論共同規則",
            "## 先判斷它能不能成為新的記憶體層",
            "| 本文五項系統條件 | 讀者先問 | 沒通過會怎樣 | 主要接力角色 | 本輪可確認到哪裡 |",
            "| 1. 容量與資料保留 |", "| 2. 讀取與等待時間 |",
            "| 3. 寫入、更新與耐久 |", "| 4. 功耗、熱與封裝 |",
            "| 5. 系統整合與軟體調度 |",
            "## 再把商用化拆成六關",
            "| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |",
            "| 1. 技術位置與工作負載說清楚 |", "| 2. 共同規則公開 |",
            "| 3. 交出可測記憶體樣品 |", "| 4. 完成裝置整合 |",
            "| 5. 通過客戶資格認證 |", "| 6. 穩定量產與形成收入 |",
            "## 再把五組角色接力放回正確位置",
            "| 接力角色 | 要交付什麼 | 要和下一角色說清楚 | 本輪證據 | 不能外推 |",
            "| 快閃記憶體與堆疊 |", "| 底部邏輯晶片與控制器 |",
            "| 封裝、測試與熱管理 |", "| 裝置、系統與軟體 |",
            "| 客戶、製造與財務 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先判斷它能不能成為新的記憶體層", 1
        )[0]
        for jargon in (
            "HBF", "HBM", "NAND", "KV cache", "OCP", "logic base die",
            "memory sample", "device sample", "qualification",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 6),
            ("research_claim", 6), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER,"
            "新的記憶體層要滿足哪些讀寫與耐久條件，才不只是特殊儲存裝置？",
            guide,
        )

    def test_ai_memory_station_five_separates_signal_tradeoffs_roles_and_evidence_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_sphbm4_organic_substrate.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 接點變少不等於設計變簡單："
            "SPHBM4 把難題移到高速傳輸、功耗與系統驗證\n"
        ))
        for contract in (
            "editorial_plain_language_wave93_sphbm4_signal_tradeoffs_roles_and_six_gate_ladder",
            "記憶體可以用很多條較慢的資料線，也可以用較少但更快的資料線",
            "本輪只能確認標準文件已發布",
            "## 先看難題從哪裡搬到哪裡",
            "| 本文五項接力問題 | 原路徑較難的地方 | 新路徑把壓力移到 | 主要接力角色 | 本輪可確認到哪裡 |",
            "| 1. 接點與扇出 |", "| 2. 每線速度與訊號品質 |",
            "| 3. 功耗、延遲與熱 |", "| 4. 材料、組裝與良率 |",
            "| 5. 系統容量與配置 |",
            "## 再把五組角色接力放回正確位置",
            "| 接力角色 | 要交付什麼 | 要和下一角色說清楚 | 本輪證據 | 不能外推 |",
            "| 記憶體裸晶與堆疊 |", "| 底部介面晶片與高速介面 |",
            "| 有機基板與材料 |", "| 封裝、測試與熱管理 |",
            "| 運算晶片、系統與客戶 |",
            "## 最後用六關判斷標準能不能變成收入",
            "| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |",
            "| 1. 共同標準發布 |", "| 2. 底部介面晶片完成 |",
            "| 3. 記憶體與封裝樣品完成 |", "| 4. 運算晶片與系統整合 |",
            "| 5. 客戶資格與可靠度通過 |", "| 6. 穩定量產與形成收入 |",
            "## 把既有產品與新標準分成兩條時鐘",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先看難題從哪裡搬到哪裡", 1
        )[0]
        for jargon in (
            "JEDEC", "JESD330-4", "SPHBM4", "HBM4", "DRAM", "SerDes",
            "base die", "data signals", "throughput", "Micron", "SK hynix",
            "CoWoS", "ABF", "BT",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 4),
            ("research_claim", 4), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE,"
            "記憶體接點變少，為什麼不代表成本一定下降或產品已經可用？",
            guide,
        )

    def test_ai_memory_station_six_separates_bonding_paths_process_windows_and_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_hybrid_bonding_readiness.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 晶片貼得更近，量產反而更難："
            "混合接合要同時守住五個製程窗口\n"
        ))
        for contract in (
            "editorial_plain_language_wave94_hybrid_bonding_paths_process_windows_and_six_gate_ladder",
            "兩層晶片讓平坦表面與細小銅接點直接貼合後",
            "不能把試驗成功直接讀成量產成熟",
            "## 先分清兩種「貼法」的良率分母",
            "| 本文兩條接合路徑 | 怎麼接 | 主要優點 | 主要風險 | 為什麼不能直接比較 |",
            "| 單顆晶粒接晶圓（D2W） |", "| 晶圓接晶圓（W2W） |",
            "## 再看五個量產窗口如何接力",
            "| 本文五個量產窗口 | 先回答什麼 | 主要接力角色 | 失敗會怎樣 | 本輪可確認到哪裡 |",
            "| 1. 設計規則與試驗結構 |", "| 2. 表面平坦與銅高度 |",
            "| 3. 潔淨與顆粒控制 |", "| 4. 對準、接合與量測 |",
            "| 5. 良率、產能與可靠度 |",
            "## 最後用六關分開技術進展與收入",
            "| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |",
            "| 1. 開放設計入口 |", "| 2. 試驗結構成功 |",
            "| 3. 整合設備與流程使用 |", "| 4. 具名產品資格認證 |",
            "| 5. 穩定大量生產 |", "| 6. 重複出貨與形成收入 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先分清兩種「貼法」的良率分母", 1
        )[0]
        for jargon in (
            "Hybrid bonding", "D2W", "W2W", "PDK", "Test vehicle",
            "Overlay", "HVM", "CMP", "OSAT", "Kinex", "Applied Materials",
            "imec", "EVG", "200nm", "good-die yield", "throughput",
            "qualification", "tape-out", "pitch", "chiplet",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 5),
            ("research_claim", 5), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-HYBRID-BONDING-READINESS,"
            "兩層晶片貼得更密，為什麼一次試驗成功還不能證明可長期量產？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "hybrid_bonding.md"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "concept:hybrid-bonding,concept,混合接合（Hybrid bonding）",
            concepts,
        )
        for concept in (
            "process:die-to-wafer-hybrid-bonding,process,單顆晶粒接晶圓（D2W）",
            "process:wafer-to-wafer-hybrid-bonding,process,晶圓接晶圓（W2W）",
            "stage:test-vehicle,stage,試驗結構",
            "capability:overlay-control,capability,對準控制（Overlay）",
            "process:cmp-planarization,process,表面平坦化（CMP）",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 混合接合（Hybrid bonding）", graph)

    def test_ai_memory_station_seven_separates_area_yield_output_and_cost(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_panel_level_packaging_readiness.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 面板排得更滿，成品不一定更便宜："
            "要一起看面積、良率、速度與報廢\n"
        ))
        for contract in (
            "editorial_plain_language_wave95_panel_cost_four_measures_production_chain_and_six_gate_ladder",
            "這只回答「排得下多少」，還沒回答最後能做出多少合格品",
            "不能把「排得更多」直接讀成「每顆更便宜」或台灣公司已受惠",
            "## 先用四把尺拆開「更便宜」",
            "| 本文四把尺 | 它先回答什麼 | 最簡單的關係 | 容易忽略什麼 | 不能直接推成 |",
            "| 1. 面積利用率 |", "| 2. 合格封裝良率 |",
            "| 3. 單位時間合格產出 |", "| 4. 每顆合格品總成本 |",
            "## 再看五個生產關卡如何接力",
            "| 本文五個生產關卡 | 先回答什麼 | 主要接力角色 | 過不了會怎樣 | 本輪可確認到哪裡 |",
            "| 1. 載體與共同尺寸 |", "| 2. 圖形、金屬與均勻度 |",
            "| 3. 翹曲、搬運與缺陷 |", "| 4. 封裝整合、測試與認證 |",
            "| 5. 良率、產出與財務 |",
            "## 最後用六關分開研發能力與收入",
            "| 本文六關 | 這一關要證明 | 本輪公開資料 | 下一份證據 | 不能外推 |",
            "| 1. 研發場域與設備能力 |", "| 2. 試產與工程測試 |",
            "| 3. 早期共同開發與認證 |", "| 4. 共同尺寸與具名產品認證 |",
            "| 5. 穩定大量生產 |", "| 6. 重複出貨與形成收入 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用四把尺拆開", 1
        )[0]
        for jargon in (
            "Panel-level packaging", "PLP", "area utilization",
            "Good-package yield", "Uniformity", "Throughput",
            "cycle time", "panel size", "form factor", "ECD", "PVD",
            "CVD", "HVM", "pilot", "qualification", "NEXX", "Lam",
            "Applied Materials",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 5),
            ("research_claim", 5), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS,"
            "面板能排進更多封裝，為什麼還要一起看良率、製程速度與報廢成本？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "panel_level_packaging.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:panel-level-packaging,concept,面板級封裝（PLP）",
            "component:panel-substrate,component,面板載體（Panel substrate）",
            "metric:panel-throughput,metric,面板單位時間產出（Throughput）",
            "standard:panel-size,standard,面板尺寸標準",
            "process:panel-ecd,process,面板電鍍沉積（ECD）",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 面板級封裝（PLP）", graph)

    def test_compute_connect_station_one_separates_ai_storage_jobs_positions_and_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-09_ai_storage_data_plane.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# AI 儲存不是容量越大越好："
            "先分清餵資料、保存進度與搬模型\n"
        ))
        for contract in (
            "editorial_plain_language_wave96_ai_storage_three_jobs_five_positions_and_six_gate_ladder",
            "三種工作卡住的原因不同",
            "不能直接換算成更多硬碟或某家公司營收",
            "## 先把三種「存資料」工作分開",
            "| 本文三種工作 | 何時發生 | 最怕什麼 | 先看哪個結果 | 不能直接推成 |",
            "| 1. 訓練時持續餵資料 |", "| 2. 故障前保存進度 |",
            "| 3. 上線或擴充時搬模型 |",
            "## 再看資料可能經過的五個位置",
            "| 本文五個位置 | 它負責什麼 | 常見資料去向 | 卡住時先查誰 | 不能直接推成 |",
            "| 1. 軟體、索引與排程 |", "| 2. 近端記憶體與快取 |",
            "| 3. 單機本地 SSD |", "| 4. 共享與長期儲存 |",
            "| 5. 網路與系統整合 |",
            "## 最後用六關把平台需求接回公司",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 三種工作已分開 |", "| 2. 同一平台量到瓶頸 |",
            "| 3. 瓶頸落到具名元件 |", "| 4. 客戶資格認證 |",
            "| 5. 正式部署與設備分母 |", "| 6. 可辨識收入與毛利 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 主張與證據帳本", 1
        )[0]
        for jargon in (
            "pMax", "checkpoint", "dataset", "fetch", "object storage",
            "local storage", "peer", "GPUDirect", "RDMA", "NIC", "SLO",
            "NAND", "NVMe", "AI Ecosystem", "qualification", "production",
            "I/O", "BOM", "TAM", "Meta", "AWS", "NVIDIA", "GPU",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 8),
            ("research_claim", 8), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-09-AI-STORAGE-DATA-PLANE,"
            "人工智慧為什麼會一邊餵訓練資料、一邊保存進度，"
            "還要把模型送到新機器？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "ai_storage_data_plane.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:ai-storage-data-plane,concept,AI 資料讀取與儲存路徑",
            "capability:training-dataset-fetch,capability,訓練資料持續餵送",
            "capability:checkpoint-persistence,capability,訓練進度保存",
            "capability:model-artifact-distribution,capability,模型檔案分發",
            "capability:tail-latency-control,capability,最慢讀取時間控制",
            "capability:direct-storage-gpu-transfer,capability,儲存直達運算晶片",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AI 資料讀取與儲存路徑", graph)

    def test_compute_connect_station_two_separates_helios_stages_customers_and_company_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_amd_helios_deployment_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# AI 機櫃做出來，不等於客戶已上線："
            "用六個關卡讀懂 AMD Helios\n"
        ))
        for contract in (
            "editorial_plain_language_wave97_helios_six_stage_five_customer_timeline_and_six_gate_ladder",
            "中間還要經過出貨、測試與產品開放",
            "它們不能相加成已部署",
            "## 先把六個部署關卡排成順序",
            "| 本文六個關卡 | 白話意思 | 可接受的證據 | 本篇目前到哪裡 | 不能直接推成 |",
            "| 1. 方案成形 |", "| 2. 開始生產 |", "| 3. 實際出貨 |",
            "| 4. 客戶測試與產品開放 |", "| 5. 正式上線 |",
            "| 6. 規模部署與財務轉換 |",
            "## 再把五組公開節點放回自己的時間線",
            "| 本文五條時間線 | 已公開到哪一步 | 時間或上限 | 下一個可驗收節點 | 不能混成 |",
            "| 1. AMD 整體平台 |", "| 2. Microsoft／Azure |",
            "| 3. OpenAI |", "| 4. Meta |", "| 5. Anthropic |",
            "## 最後用六關把平台進度接回台灣公司",
            "| 本文六關 | 要回答的問題 | 現有資料能確認 | 下一份公司證據 | 不能外推 |",
            "| 1. 公開列名 |", "| 2. 具體角色 |", "| 3. 平台專屬產品 |",
            "| 4. 驗證與量產出貨 |", "| 5. 可辨識財務結果 |",
            "| 6. 現金流與重複訂單 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先把六個部署關卡排成順序", 1
        )[0]
        for jargon in (
            "Helios", "production", "shipment", "online", "validation",
            "GW", "SKU", "MI455X", "upcoming", "preview", "GA",
            "rack-scale", "purpose-built", "GPU", "ASIC", "EFB", "ODM",
            "compute-tray", "Azure", "OpenAI", "Meta", "Anthropic", "AMD",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 11),
            ("research_claim", 9), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER,"
            "一整櫃人工智慧設備開始生產後，為什麼還不能算客戶已經上線使用？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "amd_helios.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "product:amd-helios,product,AMD Helios 機架級平台",
            "concept:rack-scale,concept,機架級系統（Rack-scale）",
            "stage:production,stage,開始生產（Production）",
            "stage:shipment,stage,實際出貨（Shipment）",
            "stage:cloud-deployment,stage,客戶上線與雲端部署",
            "stage:validation,stage,客戶測試與驗證（Validation）",
            "component:efb,component,高架扇出橋接（EFB）",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AMD Helios 部署階梯", graph)

    def test_compute_connect_station_three_separates_backside_power_path_process_and_company_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_backside_power_delivery.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 晶片把供電線移到背面，不只是換條路："
            "先看電力路徑、製程接力與量產證據\n"
        ))
        for contract in (
            "editorial_plain_language_wave98_backside_power_path_process_roles_and_six_gate_ladder",
            "這種做法把供電網路移到晶圓背面",
            "看到某道製程變重要只代表值得研究",
            "## 先用五個位置分開「送訊號」和「送電」",
            "| 本文五個位置 | 它負責什麼 | 和下一位置怎麼接 | 主要工程問題 | 不能直接推成 |",
            "| 1. 正面訊號佈線 |", "| 2. 背面金屬網路 |",
            "| 3. 奈米級背面導通孔 |", "| 4. 埋置電源軌 |",
            "| 5. 電晶體 |",
            "## 再把背面加工排成六個製程步驟",
            "| 本文六個步驟 | 在做什麼 | 主要接力角色 | 要驗收什麼 | 本輪可確認到哪裡 |",
            "| 1. 完成前側元件與電源軌 |", "| 2. 接到支撐載體 |",
            "| 3. 從背面把晶圓變薄 |", "| 4. 從背面重新找準位置 |",
            "| 5. 形成導通孔與背面金屬 |", "| 6. 驗證完整流程能重複生產 |",
            "## 把晶圓廠時鐘與供應商時鐘分開",
            "## 最後用六關把製程需要接回公司",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 一般機制與流程成立 |",
            "| 2. 晶圓廠具名製程進入製造時鐘 |",
            "| 3. 供應商具名到同一製程步驟 |",
            "| 4. 通過資格並進入量產出貨 |",
            "| 5. 份額、價格與重複需求可辨識 |",
            "| 6. 收入、毛利與現金流出現 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置分開", 1
        )[0]
        for jargon in (
            "BSPDN", "A16", "18A", "Super Power Rail", "PowerVia",
            "BPR", "nano-TSV", "nTSV", "CMP", "PDK", "DTCO",
            "qualification", "production", "risk production", "HVM",
            "TSMC", "Intel", "imec",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 5),
            ("research_claim", 5), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-BACKSIDE-POWER-DELIVERY,"
            "晶片為什麼要把供電線移到背面，這會新增哪些製程，"
            "又怎麼判斷公司真的受惠？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "backside_power.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:backside-power,concept,背面供電路徑（BSPDN）",
            "process:super-power-rail,process,超級電源軌（Super Power Rail）",
            "process:powervia,process,背面供電導通（PowerVia）",
            "component:buried-power-rail,component,埋置電源軌（BPR）",
            "component:nano-tsv,component,奈米級背面導通孔（nano-TSV）",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 背面供電路徑與製程接力", graph)

    def test_compute_connect_station_four_separates_optical_path_tradeoffs_roles_and_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_cpo_pluggable_coexistence.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 資料先是電、再變成光："
            "轉換器放哪裡，決定可插拔與共同封裝的取捨\n"
        ))
        for contract in (
            "editorial_plain_language_wave99_cpo_five_positions_five_tradeoffs_roles_and_six_gate_ladder",
            "資料先以電訊號進入交換晶片，再轉成光訊號",
            "一種方案開始生產，不代表另一種立刻消失",
            "## 先用五個位置看資料怎麼從電變成光",
            "| 本文五個位置 | 資料現在是什麼 | 這裡負責什麼 | 主要接力角色 | 不能直接推成 |",
            "| 1. 交換晶片內部 |", "| 2. 晶片到轉換器的高速電路 |",
            "| 3. 電光轉換位置 |", "| 4. 雷射與光纖耦合 |",
            "| 5. 光纖與下一台設備 |",
            "## 再用五把尺比較兩種轉換位置",
            "| 本文五把尺 | 可插拔光模組 | 共同封裝光學 | 下一個要量的結果 | 不能直接推成 |",
            "| 1. 高速電路長度與功耗 |", "| 2. 前面板空間與頻寬密度 |",
            "| 3. 維修與故障範圍 |", "| 4. 升級與多供應商彈性 |",
            "| 5. 封裝、測試與生命週期成本 |",
            "## 把五類角色放回同一條光電接力",
            "| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 平台與交換器產品 |", "| 2. 可插拔訊號處理 |",
            "| 3. 雷射與光源 |", "| 4. 封裝、組裝與測試 |",
            "| 5. 客戶部署與營運 |",
            "## 把兩條產品時鐘放回同一代共存",
            "## 最後用六關分開產品生產、部署與公司受惠",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 兩種產品路徑已具名 |", "| 2. 產品進入持續生產 |",
            "| 3. 供應商角色能雙向核對 |", "| 4. 客戶驗收與部署分母出現 |",
            "| 5. 供應商出貨、份額與價格可辨識 |",
            "| 6. 收入、毛利與現金流留下來 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "CPO", "Spectrum-X", "Photonics", "Spectrum-6", "1.6T",
            "Ara", "DSP", "SerDes", "SPIL", "Lumentum", "Marvell",
            "NVIDIA", "InP", "production", "full production",
            "pluggable", "TSMC", "TFC", "Foxconn",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 7),
            ("research_claim", 5), ("metric_comparison", 0),
            ("impact", 1), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE,"
            "資料從交換晶片送出去時，為什麼有的光模組能拔換，"
            "有的要和晶片放在一起？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "cpo_networking.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:cpo-networking,concept,共同封裝光學網路（CPO）",
            "product:spectrum-x-ethernet-photonics,product,"
            "Spectrum-X 共同封裝光學交換器",
            "component:co-packaged-optics,component,共同封裝光學（CPO）",
            "component:pluggable-optics,component,可插拔光模組",
            "stage:product-production,stage,進入產品生產",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 光電轉換位置與兩種光學路徑", graph)

    def test_compute_connect_station_five_separates_exposure_cost_roles_and_company_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_high_na_euv_insertion_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 曝光次數少了，晶片不一定更便宜："
            "先看圖形怎麼印、哪些成本又冒出來\n"
        ))
        for contract in (
            "editorial_plain_language_wave100_high_na_five_positions_five_cost_lenses_roles_and_six_gate_ladder",
            "先在晶圓表面塗上光阻，再用光罩控制光線落在哪裡",
            "每顆合格晶片的總成本",
            "## 先用五個位置看圖形怎麼印到晶圓",
            "| 本文五個位置 | 眼前發生什麼 | 主要接力角色 | 下一個要驗收 | 不能直接推成 |",
            "| 1. 設計圖形與光罩 |", "| 2. 晶圓表面與光阻 |",
            "| 3. 曝光機與光學 |", "| 4. 顯影與圖形轉移 |",
            "| 5. 量測、檢查與下一層 |",
            "## 再用五把尺比較少做步驟是否真的省錢",
            "| 本文五把尺 | 較高數值孔徑方案 | 現行多步驟方案 | 下一個要量的結果 | 不能直接推成 |",
            "| 1. 曝光與加工次數 |", "| 2. 機器可用時間與每小時產出 |",
            "| 3. 光罩、光阻與缺陷 |", "| 4. 對準、製程視窗與良率 |",
            "| 5. 每顆合格晶片總成本 |",
            "## 把五類角色放回同一段曝光接力",
            "| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 曝光設備與平台 |", "| 2. 研發與資格整合 |",
            "| 3. 晶圓製造客戶 |", "| 4. 光罩、材料與圖形轉移 |",
            "| 5. 量測、檢查與生產經濟 |",
            "## 把五個里程碑排成同一條導入階梯",
            "| 本文五個里程碑 | 白話意思 | 本輪可確認 | 下一份證據 | 不能合併成 |",
            "| 1. 機器送達 |", "| 2. 開始運轉與校準 |",
            "| 3. 研發資格與共同整合 |", "| 4. 實際產品晶圓測試 |",
            "| 5. 穩定量產導入 |",
            "## 最後用六關分開設備進度、客戶量產與公司受惠",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 目標圖形可以印出 |", "| 2. 多台設備能持續運轉 |",
            "| 3. 共同製程通過資格 |", "| 4. 實際產品達成視窗與良率 |",
            "| 5. 量產層數、產出與成本可重算 |",
            "| 6. 供應商財務足跡出現 |",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "High-NA", "Low-NA", "EUV", "EXE", "HVM", "wafer",
            "product", "availability", "throughput", "qualification",
            "insertion", "scanner", "resist", "mask", "metrology",
            "ASML", "imec", "Intel", "multi-patterning", "calibration",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 7),
            ("research_claim", 8), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER,"
            "晶片圖形能一次印得更細，為什麼少做幾個步驟仍不一定更便宜？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "high_na_euv_readiness.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:high-na-euv-readiness,concept,晶圓圖形曝光與 High-NA 導入階梯",
            "component:high-na-euv-scanner,component,高數值孔徑 EUV 曝光機",
            "product:exe-5200b,product,ASML EXE:5200B 曝光機",
            "stage:high-na-operation,stage,客戶端開始運轉",
            "stage:high-na-process-qualification,stage,製程資格驗證",
            "stage:high-na-product-wafer,stage,實際產品晶圓測試",
            "stage:high-na-hvm-insertion,stage,高量產導入",
            "component:high-na-resist,component,高數值孔徑曝光用光阻",
            "capability:high-na-metrology,capability,高數值孔徑曝光量測與檢查",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 晶圓圖形曝光與 High-NA 導入階梯", graph)

    def test_compute_connect_station_six_separates_data_path_scopes_roles_and_interoperability_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_open_ai_fabrics.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 資料從一顆運算晶片走到另一顆："
            "先分清機架內外，再判斷跨廠互通\n"
        ))
        for contract in (
            "editorial_plain_language_wave101_data_path_two_network_scopes_roles_and_six_gate_interoperability",
            "一條完整資料路徑，要讓運算端點、連接傳輸、交換器、"
            "控制軟體與另一個端點接力",
            "## 先用五個位置看資料怎麼從一顆晶片走到另一顆",
            "| 本文五個位置 | 它做什麼 | 代表元件或軟體 | 下一個要驗收 | 不能直接推成 |",
            "| 1. 資料出發的運算端點 |", "| 2. 連接與傳輸 |",
            "| 3. 交換與網路 |", "| 4. 協調與控制軟體 |",
            "| 5. 目的端點與工作負載 |",
            "## 再用五把尺分開機架內與跨機架網路",
            "| 本文五把尺 | 機架內擴充 | 跨機架擴充 | 下一個要量的結果 | 不能直接推成 |",
            "| 1. 距離與連線形狀 |", "| 2. 延遲與記憶體 |",
            "| 3. 交換、路由與壅塞 |", "| 4. 可靠性與恢復 |",
            "| 5. 實際工作與客戶驗收 |",
            "## 把五條規格與傳輸路徑放回機架內外",
            "| 本文五條路徑 | 主要範圍 | 它定義或承載什麼 | 本輪可確認 | 還不能說 |",
            "| 1. UALink |", "| 2. ESUN |", "| 3. SUE-T |",
            "| 4. UEC |", "| 5. UALoE |",
            "## 把六類角色放回同一條資料路徑",
            "| 本文六類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 規格與開放工作組 |", "| 2. 加速器、端點與晶片智財 |",
            "| 3. 交換器專用晶片與平台 |", "| 4. 機架與系統整合 |",
            "| 5. 雲端客戶與實際部署 |", "| 6. 台灣供應鏈查證 |",
            "## 最後用六關判斷「能連」到「真正互通」",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 共同規則可查核 |", "| 2. 路徑各位置有具名實物 |",
            "| 3. 單件產品符合指定規格 |", "| 4. 不同廠商完成交叉互通 |",
            "| 5. 整個系統與工作可重現 |",
            "| 6. 客戶部署與公司財務對上 |",
            "## 這篇對公司判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "UALink", "UEC", "ESUN", "SUE-T", "UALoE", "scale-up",
            "scale-out", "endpoint", "switch", "ASIC", "compliance",
            "interoperability", "plugfest", "Helios", "MI450", "AMD",
            "Arista", "Broadcom", "Marvell", "Oracle", "OCP",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 14),
            ("research_claim", 13), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-OPEN-AI-FABRICS,"
            "資料要從一顆運算晶片送到另一顆，"
            "端點、交換器和軟體要一起通過哪些測試？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "open_ai_fabrics.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:open-ai-fabrics,concept,AI 資料路徑與跨廠互通",
            "standard:ualink,standard,UALink 加速器互連",
            "standard:uec,standard,超乙太網路（UEC）",
            "concept:scale-up,concept,機架內擴充（scale-up）",
            "concept:scale-out,concept,跨機架擴充（scale-out）",
            "standard:ualoe,standard,以乙太網路承載 UALink（UALoE）",
            "stage:interoperability,stage,跨廠互通",
            "standard:esun,standard,機架內乙太網路交換（ESUN）",
            "standard:sue-t,standard,機架內乙太傳輸（SUE-T）",
            "product:arista-7060xe7,product,Arista 7060XE7 網路平台",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AI 資料路徑與跨廠互通", graph)

    def test_compute_connect_station_seven_separates_link_test_clocks_roles_and_deployment_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-03_pcie6_compliance_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# PCIe 6 元件寫著第六代，不代表整套系統已通過："
            "先分清裝置、連線、正式測試與部署\n"
        ))
        for contract in (
            "editorial_plain_language_wave102_complete_link_test_dimensions_roles_and_six_gate_deployment",
            "一條完整高速連線，要讓主機、板路與線材、必要的訊號或交換元件、"
            "終端裝置，以及低階控制軟體一起工作",
            "## 先用五個位置看一條高速連線怎麼接起來",
            "| 本文五個位置 | 它做什麼 | 代表裝置或軟體 | 下一個要驗收 | 不能直接推成 |",
            "| 1. 主機與連線控制 |", "| 2. 板路、連接器與線材 |",
            "| 3. 訊號修復或速率轉換 |", "| 4. 連線交換與分支 |",
            "| 5. 終端與實際工作 |",
            "## 再用五把尺讀懂一筆測試到底證明什麼",
            "| 本文五把尺 | 每筆結果要記錄 | 本輪可看到的例子 | 下一份證據 | 不能直接推成 |",
            "| 1. 規格版本與連線世代 |", "| 2. 每條通道的傳輸率 |",
            "| 3. 通道數與連線拓撲 |", "| 4. 產品、韌體與軟體組合 |",
            "| 5. 測試主體與結果狀態 |",
            "## 把六個動作分成不同時鐘",
            "| 本文六個時鐘 | 誰來確認 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 規格與測試入口存在 |", "| 2. 具名產品宣稱支援 |",
            "| 3. 供應商或客戶完成互通 |", "| 4. 具名產品正式通過並列名 |",
            "| 5. 單一元件進入量產 |", "| 6. 完整平台進入客戶部署 |",
            "## 把六類角色放回同一套平台",
            "| 本文六類角色 | 它負責什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 規格與正式測試組織 |", "| 2. 主機、控制器與平台 |",
            "| 3. 連接與訊號元件 |", "| 4. 終端與儲存裝置 |",
            "| 5. 系統整合、雲端客戶與營運者 |", "| 6. 台灣供應鏈查證 |",
            "## 最後用六關分開「元件已量產」與「整套系統已通過」",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 完整連線的位置與責任可辨認 |", "| 2. 測試合約寫完整 |",
            "| 3. 具名產品在目標速度正式通過 |", "| 4. 不同廠商的完整路徑互通 |",
            "| 5. 具名客戶的完整平台穩定部署 |",
            "| 6. 台灣公司財務足跡可雙向核對 |",
            "## 這篇對公司判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "PCIe", "Gen6", "GT/s", "retimer", "switch", "endpoint",
            "host", "firmware", "Official", "Integrators", "Workshop",
            "Astera", "Micron", "PCI-SIG", "qualification",
            "production", "deployment",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 7),
            ("research_claim", 7), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-03-PCIE6-COMPLIANCE-LADDER,"
            "一個高速元件已經量產，為什麼還不能說整台伺服器已通過第六代連線？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "pcie6_compliance_ladder.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:pcie6-deployment-readiness,concept,PCIe 6 高速連線的測試與部署階梯",
            "standard:pcie6,standard,第六代高速周邊連接（PCIe 6）",
            "component:pcie-retimer,component,高速訊號重整器（retimer）",
            "component:pcie-fabric-switch,component,高速連線交換器（switch）",
            "product:micron-9650,product,Micron 9650 固態硬碟",
            "stage:vendor-interoperability,stage,跨廠元件互通",
            "stage:official-compliance,stage,PCI-SIG 官方相容性測試",
            "stage:integrators-listing,stage,PCI-SIG 合格清單列名",
            "stage:pcie6-platform-deployment,stage,客戶完整平台部署",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: PCIe 6 高速連線的測試與部署階梯", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 14)

    def test_compute_connect_station_eight_separates_package_positions_test_dimensions_and_ecosystem_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_ucie_interoperability_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# UCIe 讓小晶片共用語言，但一次互通不代表生態系成熟："
            "先分清設計、實體測試與客戶產品\n"
        ))
        for contract in (
            "editorial_plain_language_wave103_ucie_package_positions_test_dimensions_evidence_objects_roles_and_six_gate_ecosystem_ladder",
            "把一顆大晶片拆成多顆小晶片後，它們仍要在同一封裝裡交換資料、"
            "時鐘、管理訊息與錯誤狀態",
            "## 先用五個位置看小晶片如何在同一封裝裡接力",
            "| 本文五個位置 | 它做什麼 | 代表元件或工作 | 下一個要驗收 | 不能直接推成 |",
            "| 1. 執行功能的小晶片 |", "| 2. 介面控制與傳輸協定 |",
            "| 3. 實體傳輸電路與通道 |", "| 4. 接點與封裝內布線 |",
            "| 5. 封裝整體協調與測試 |",
            "## 再用五把尺讀懂一次互通展示證明什麼",
            "| 本文五把尺 | 每筆展示要記錄 | 本輪可看到的例子 | 下一份證據 | 不能直接推成 |",
            "| 1. 傳輸率 |", "| 2. 實體路徑 |",
            "| 3. 協定與管理功能 |", "| 4. 廠商獨立性與晶片狀態 |",
            "| 5. 封裝、時間與故障條件 |",
            "## 把五種證據物件分開，不讓它們斜著畢業",
            "| 本文五種證據物件 | 白話意思 | 本輪可確認 | 下一份證據 | 不能借用 |",
            "| 1. 共同規格 |", "| 2. 介面智財與設計工具 |",
            "| 3. 送廠設計與回片 |", "| 4. 測試晶片互通展示 |",
            "| 5. 客戶量產產品 |",
            "## 把六類角色放回同一個小晶片產品",
            "| 本文六類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 規格聯盟與測試規則 |", "| 2. 介面智財與設計工具 |",
            "| 3. 小晶片設計者 |", "| 4. 晶圓製造 |",
            "| 5. 封裝、載板與測試服務 |", "| 6. 客戶產品與台灣財務查證 |",
            "## 最後用六關判斷「能互通」到「生態系成熟」",
            "| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 共同規格與測試合約可查 |", "| 2. 介面實作完成並送廠 |",
            "| 3. 實體晶片在目標速度運作 |", "| 4. 跨廠互通與正式測試對齊 |",
            "| 5. 客戶產品通過資格並量產 |",
            "| 6. 台灣公司財務足跡可雙向核對 |",
            "## 這篇對公司判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "UCIe", "GT/s", "chiplet", "die-to-die", "controller",
            "PHY", "lane", "sideband", "manageability", "protocol",
            "tape-out", "silicon", "test chip", "simulation", "loopback",
            "interoperability", "compliance", "qualification", "OSAT",
            "substrate", "Intel", "Cadence", "Synopsys", "Consortium",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 6),
            ("research_claim", 5), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER,"
            "把一顆大晶片拆成多顆小晶片後，還要通過哪些關卡，"
            "才能讓不同公司的零件一起量產？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "ucie_interoperability.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "concept:ucie-interoperability,concept,UCIe 小晶片互通與量產階梯",
            "standard:ucie3,standard,第三代通用小晶片互連（UCIe 3.0）",
            "stage:specification,stage,共同規格發布",
            "stage:ip-tapeout,stage,介面設計送廠（IP tape-out）",
            "stage:cross-vendor-demo,stage,跨廠測試晶片互通",
            "stage:compliance,stage,正式符合規格測試",
            "stage:customer-qualification,stage,客戶產品資格驗證",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: UCIe 小晶片互通與量產階梯", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 13)


if __name__ == "__main__":
    unittest.main()
