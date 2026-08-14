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
                    {"t": "ul", "items": [
                        [{"s": "公司公告與供應商受惠是兩件事。"}],
                        [{"s": "公司公告擴產，只能證明公司自己的規劃。"}],
                        [{"s": "沒有供應商文件，還不能把擴產寫成特定供應商訂單。"}],
                    ]},
                    {"t": "h3", "runs": [{"s": "為什麼重要"}]},
                    {"t": "p", "runs": [{
                        "s": "把公司擴產直接寫成特定供應商訂單，是本文要避免的誤解。"
                             "後續仍要等供應商文件。",
                    }]},
                    {"t": "h3", "runs": [{"s": "想一想"}]},
                    {"t": "ul", "items": [[{
                        "s": "還缺哪一份公司文件，才能把擴產連到供應商？",
                    }]]},
                    {"t": "h3", "runs": [{"s": "接下來怎麼追"}]},
                    {"t": "ul", "items": [[{
                        "s": "先找供應商正式文件，確認是否揭露具名訂單與可辨識收入。",
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
            "keyPoints": [
                "公司公告與供應商受惠是兩件事。",
                "公司公告擴產，只能證明公司自己的規劃。",
                "沒有供應商文件，還不能把擴產寫成特定供應商訂單。",
            ],
            "source": "本文既有的「三句話抓重點」、「為什麼重要」與「想一想」",
        })
        self.assertEqual(topic["readerBoundaryBrief"], {
            "known": "公司公告與供應商受惠是兩件事。",
            "unknown": "沒有供應商文件，還不能把擴產寫成特定供應商訂單。",
            "next": "先找供應商正式文件，確認是否揭露具名訂單與可辨識收入。",
            "source": "同篇既有的「三句話抓重點」與「接下來怎麼追」",
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
        self.assertEqual(library["learningPathVersion"], 109)
        article_ids = {article["id"] for article in library["articles"]}
        article_by_id = {article["id"]: article for article in library["articles"]}
        graph_ids = {item["id"] for item in graph["graphs"]}
        graph_by_id = {item["id"]: item for item in graph["graphs"]}
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
                    target_graph = graph_by_id[card["graphId"]]
                    direct = article["id"] in (target_graph.get("articleIds") or [])
                    if direct:
                        self.assertNotIn("relationBasis", card)
                    else:
                        basis = card["relationBasis"]
                        self.assertEqual(basis["kind"], "stock")
                        self.assertTrue(basis["ids"])
                        self.assertTrue(set(basis["ids"]).issubset(article["stockIds"]))
                        node_by_id = {
                            node["id"]: node for node in target_graph["nodes"]
                        }
                        edge = next(
                            edge for edge in target_graph["edges"]
                            if edge["id"] == card["guidedRelation"]["edgeId"]
                        )
                        guided_tickers = {
                            node_by_id.get(edge.get(endpoint), {}).get("ticker")
                            for endpoint in ("from", "to")
                        }
                        self.assertTrue(set(basis["ids"]).intersection(guided_tickers))
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

    def test_shared_company_graph_card_explains_and_previews_the_same_company(self):
        library = {
            "counts": {"formal_note": 1},
            "groups": [{"id": "power", "label": "功率元件", "count": 1}],
            "articles": [{
                "id": "formal-1111", "type": "formal_note",
                "readerTitle": "1111 甲公司 — 質化研究筆記",
                "subject": "1111 甲公司", "stockIds": ["1111"],
                "groups": ["power"], "groupLabels": ["功率元件"],
            }],
        }
        graph = {"graphs": [{
            "id": "shared-company", "label": "相鄰產業圖",
            "rootNodeId": "concept:test", "articleIds": [],
            "nodes": [
                {"id": "company:2222", "ticker": "2222", "label": "乙公司"},
                {"id": "company:1111", "ticker": "1111", "label": "甲公司"},
                {"id": "concept:test", "label": "測試主題"},
            ],
            "edges": [
                {
                    "id": "E-OTHER", "view": "company",
                    "from": "company:2222", "to": "concept:test",
                    "relationLabel": "其他公司關係", "evidenceState": "verified",
                    "evidenceLabel": "證實", "commercialStageLabel": "量產",
                },
                {
                    "id": "E-SHARED", "view": "company",
                    "from": "company:1111", "to": "concept:test",
                    "relationLabel": "甲公司既有關係", "evidenceState": "inference",
                    "evidenceLabel": "推論", "commercialStageLabel": "研究路由",
                    "boundary": "共同公司不等於兩個題材具有因果關係。",
                },
            ],
        }]}

        bd.attach_research_learning_paths(library, graph)

        card = next(
            card for card in library["articles"][0]["learningPath"]["cards"]
            if card["kind"] == "graph"
        )
        self.assertEqual(card["relationBasis"], {
            "kind": "stock", "ids": ["1111"], "labels": ["1111 甲公司"],
        })
        self.assertEqual(card["guidedRelation"]["edgeId"], "E-SHARED")
        self.assertEqual(card["guidedRelation"]["fromLabel"], "甲公司")
        self.assertNotEqual(card["guidedRelation"]["edgeId"], "E-OTHER")

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
             "groupLabels": ["功率元件", "電源供應"],
             "readingMission": reading_mission},
            {"id": "topic-b", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站", "typeLabel": "市場議題", "readingMinutes": 5,
             "groupLabels": ["電源供應"], "readingMission": reading_mission},
            {"id": "topic-b-detail", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第二站補充", "typeLabel": "市場議題", "readingMinutes": 4},
            {"id": "topic-c", "type": "topic", "groups": [], "stockIds": [],
             "readerTitle": "第三站", "typeLabel": "市場議題", "readingMinutes": 7,
             "groupLabels": ["散熱"], "readingMission": reading_mission},
        ]}
        graph = {
            "learningRoutes": [{
                "id": "route", "label": "測試路線",
                "description": "依序閱讀", "graphIds": ["graph-a", "graph-b", "graph-c"],
                "phases": [
                    {
                        "id": "foundation", "label": "基礎概念",
                        "purpose": "先建立測試用的基礎概念。",
                        "graphIds": ["graph-a"],
                    },
                    {
                        "id": "application", "label": "系統應用",
                        "purpose": "再把基礎概念放進系統應用。",
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
            "phasePurpose": "先建立測試用的基礎概念。",
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
            [station["phasePurpose"] for station in stations],
            ["先建立測試用的基礎概念。", "再把基礎概念放進系統應用。",
             "再把基礎概念放進系統應用。"],
        )
        self.assertEqual(
            [station["phaseStationStep"] for station in stations], [1, 1, 2])
        self.assertEqual(stations[0]["question"], "讀完後能回答哪個問題？")
        self.assertEqual(stations[1]["articleTitle"], "第二站")
        self.assertEqual(stations[2]["readingMinutes"], 7)
        self.assertEqual(stations[0]["groupLabels"], ["功率元件", "電源供應"])
        self.assertEqual(stations[1]["groupLabels"], ["電源供應"])
        self.assertEqual(stations[2]["groupLabels"], ["散熱"])
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
                    "purpose": "只用來測試缺站的階段。",
                    "graphIds": ["graph-a"],
                }],
            }],
            "graphs": graph["graphs"][:2],
        }
        with self.assertRaisesRegex(ValueError, "逐站、依原順序完整覆蓋"):
            bd.attach_research_learning_paths({"articles": []}, invalid_graph)

        missing_purpose_graph = {
            "learningRoutes": [{
                "id": "missing-purpose", "label": "缺課綱路線",
                "graphIds": ["graph-a"],
                "phases": [{
                    "id": "only", "label": "缺課綱階段",
                    "graphIds": ["graph-a"],
                }],
            }],
            "graphs": graph["graphs"][:1],
        }
        with self.assertRaisesRegex(ValueError, "purpose"):
            bd.attach_research_learning_paths(
                {"articles": []}, missing_purpose_graph)

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
                self.assertTrue(phase["purpose"].strip(), route["id"])
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
                 "ticker": "1111", "groupId": "power", "label": "甲公司"},
                {"id": "concept:test", "type": "concept", "universe": False},
            ],
            "edges": [{
                "id": "E1", "status": "active", "view": "company",
                "from": "company:1111", "to": "concept:test",
                "materiality": "named_product", "evidenceState": "verified",
                "relationLabel": "揭露技術能力",
                "materialityLabel": "具名產品／角色",
                "evidenceLabel": "證實",
                "commercialStage": "capability",
                "commercialStageLabel": "能力／研發",
                "reviewDue": "2026-08-20",
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
        self.assertEqual(row["companyEvidence"], [{
            "stockId": "1111",
            "companyName": "甲公司",
            "companyLabel": "1111 甲公司",
            "formalArticleId": "formal-1111",
            "formalVerified": True,
            "graphId": "test-graph",
            "graphLabel": "",
            "edgeId": "E1",
            "articleIds": [],
            "relationLabel": "揭露技術能力",
            "materiality": "named_product",
            "materialityLabel": "具名產品／角色",
            "evidenceState": "verified",
            "evidenceLabel": "證實",
            "commercialStage": "capability",
            "commercialStageLabel": "能力／研發",
            "reviewDue": "2026-08-20",
            "routeCount": 1,
        }])
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

    def test_group_maturity_company_evidence_uses_one_current_deterministic_route(self):
        graph = {"graphs": [{
            "id": "test-graph", "label": "測試題材",
            "nodes": [
                {"id": "company:1111", "type": "company", "universe": True,
                 "ticker": "1111", "groupId": "power", "label": "甲公司"},
                {"id": "concept:a", "type": "concept"},
                {"id": "concept:b", "type": "concept"},
                {"id": "concept:c", "type": "concept"},
            ],
            "edges": [
                {"id": "E-stale", "status": "active", "view": "company",
                 "from": "company:1111", "to": "concept:a",
                 "relationLabel": "過期待複核", "materiality": "financial",
                 "evidenceState": "verified", "reviewDue": "2026-08-01"},
                {"id": "E-current", "status": "active", "view": "company",
                 "from": "company:1111", "to": "concept:b",
                 "relationLabel": "目前起點", "materiality": "named_product",
                 "evidenceState": "inference", "reviewDue": "2026-08-20"},
                {"id": "E-adjacent", "status": "active", "view": "company",
                 "from": "company:1111", "to": "concept:c",
                 "relationLabel": "相鄰證實", "materiality": "adjacent",
                 "evidenceState": "verified", "reviewDue": "2026-08-20"},
            ],
        }]}

        maturity = bd.build_group_maturity(
            self.notes, [], self.stock_meta, {"power": "功率元件"},
            graph, [], {}, "2026-08-06",
        )

        row = maturity["rows"][0]
        self.assertEqual(row["companyBridges"], 1)
        self.assertEqual(len(row["companyEvidence"]), 1)
        self.assertEqual(row["companyEvidence"][0]["edgeId"], "E-current")
        self.assertEqual(row["companyEvidence"][0]["routeCount"], 3)
        self.assertEqual(row["companyEvidence"][0]["formalArticleId"], "formal-1111")
        self.assertTrue(row["companyEvidence"][0]["formalVerified"])

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
        self.assertEqual(len(guide), 40)
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
        topic_reader_boundaries = [
            article["readerBoundaryBrief"]
            for article in published.values()
            if article.get("readingMission")
        ]
        self.assertEqual(len(topic_reader_boundaries), 39)
        self.assertTrue(all(
            boundary.get("known") and boundary.get("unknown") and boundary.get("next")
            for boundary in topic_reader_boundaries
        ))
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
            "文章查核資料", "研究欄位與來源", "mobile-evidence", "可水平捲動的研究資料表",
            "function articleReaderHeading(", "article.readerQuestion",
            "先知道一件事", "讀完能回答", "目前怎麼看：", "這篇先弄懂",
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
            "function focusReadingMissionStart(", "function focusTopicMainStart(",
            "reading-mission-grid", "'data-testid':'reading-mission-start'",
            "'data-reading-start':roleFirst?'role':'source'", "先看產業角色",
            "開始讀三句重點", "先抓住一個重點，再帶著問題讀",
            "'data-testid':'reading-mission-main-start'",
            "'data-reading-main-section':firstMain.index", "直接讀第一節",
            "first=topicReaderSectionItems(article)[0]",
            "section?.querySelector('[data-main-question-anchor]')",
            "section?.querySelector(':scope > h2')||section",
            "if(target)focusReadingTarget(target)",
            ".reading-mission-start.secondary{background:var(--card);color:var(--teal)}",
            "先抓住這個重點", "讀完能回答", "為什麼值得讀",
            "rawLead=(mission.keyPoints||[]).find(Boolean)||mission.orientation",
            "lead=readerLeadParts(article,rawLead)",
            "function readerMissionLeadNodes(", "reading-mission-clause-break",
            "function readingMissionNotationGuide(article,mission)",
            "mission?.readerNotations||[]",
            "data-reading-mission-notation-count", "先解碼這段的 ",
            "const notationGuide=readingMissionNotationGuide(article,mission)",
            "class:'reading-mission-citations'", "原文來源標記：",
            "正文與來源區完整保留",
            ".reading-mission-notation>summary{min-height:44px;",
            "event.preventDefault();fold.open=!fold.open});return fold",
            "reading-mission-why", "需要更多脈絡時再展開",
            "三句重點之後，再比較本文族群角色與所在學習階段。",
            ".reading-mission-start{width:100%;min-height:44px}",
            ".article-learning-origin{display:none}",
            "body.article-open .reader-tabs{display:none}",
            ".mobile-origin-context{display:block",
            ".mobile-origin-context:not([open]) strong{white-space:nowrap",
            "@media(max-width:340px){.mobile-origin-context{margin-bottom:8px}",
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
            "const termGuide=readingMissionTermGuide(lead.text,mission.question,glossaryTerms)",
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
            "beginner-followup", "再看為什麼重要、名詞與後續問題",
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
            "learning-route-bridge-takeaway", "本篇替整條問題先補上",
            "takeaway=String((mission.keyPoints||[])[0]||'').trim()",
            "'data-source-key-point-index':'0'",
            "這一站 → 下一站", "data-route-context-collapsed",
            "只表示學習次序，不代表供應鏈、受惠或因果關係。",
            "function learningRelationPreview(", "一條既有關係示範",
            "先看一條既有關係", "先別外推到哪裡",
            "data-graph-view", "data-guided-edge",
            "card.graphView,card.guidedRelation?.edgeId",
            "查看'+(card.graphViewLabel||'產業關聯')+'圖",
            "function articleRouteGraphView(article)",
            ".learning-route-action{min-height:44px",
            "roleCount>1&&hasIndustry", "!hasCompany&&hasIndustry",
            "'data-graph-view':view", "'data-role-count':roleCount",
            "text:'看這站證據關係 · '+viewLabel",
            "openRadarGraph(route.graphId,view,'',graphLearningOrigin('route-context'))",
            "本入口先開「產業依賴」", "要查具名公司時可在圖內切換「公司曝險」",
            ".graph-origin-roles{grid-column:1/-1",
            ".graph-origin button.graph-origin-role{display:grid",
            "function graphArticleRoleMatches(graph,nodeMap,groupId)",
            "function graphArticleRoleEntries(graph,nodeMap,article)",
            "function graphArticleRoleNavigator(currentEdge)",
            "function revealGraphArticleRole(edge)",
            "function renderGraphArticleRoles(graph,nodeMap)",
            "state.graphView!=='industry'",
            "(graph.articleIds||[]).includes(article.id)",
            "'data-testid':'graph-origin-role-'+group.id",
            "'data-edge-count':matches.length",
            "把剛才文章的 '+entries.length+' 個角色放回圖上",
            "先選一個剛讀過的角色",
            "state.graphEvidence.add(edge.evidenceState)",
            "renderGraphArticleRoles(graph,nodeMap)",
            ".graph-reader-role-nav{padding:10px 11px",
            ".graph-reader-role-switch{display:grid",
            "'data-testid':'graph-reader-role-nav'",
            "'data-testid':'graph-reader-role-'+entry.group.id",
            "'aria-current':current?'step':null",
            "button.addEventListener('keydown',graphKeyboard(activate))",
            "留在圖內比較本文 '+entries.length+' 個角色",
            "切換只比較本文角色",
            "roleNavigator=graphArticleRoleNavigator(edge)",
            "if(roleNavigator)panel.appendChild(roleNavigator)",
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
            "articleOrigin:null", "function graphArticleSelectedRelation(graph,origin)",
            "selection?.type!=='edge'", "(graph?.edges||[]).find(item=>item.id===selection.id)",
            "subject=(from?.label||edge.from)+' → '+(to?.label||edge.to)",
            "title:subject+' · '+edge.relationLabel",
            "function articleOriginContext(", "edgeId:relation?.edge.id||''",
            "mobileMeta:relation?.meta||''", "關係類型「'+relation.edge.relationLabel",
            "routeId:route.id", "originQuestion=question?'整條路線要回答：'+question:''",
            "originQuestion,mobileMeta:originQuestion",
            "function returnArticleOrigin(", "function renderArticleLearningOrigin(",
            "function renderLearningOriginReturn(",
            "'data-testid':'article-origin-top'",
            "'data-testid':'article-origin-back-top'",
            "'data-testid':'article-origin-back-bottom'",
            "originContext?.mobileBackLabel||'返回研究清單'",
            "function renderMobileArticleOrigin(context)",
            "'data-testid':'mobile-origin-context'",
            "'data-origin-edge-id':context.edgeId||null",
            "'data-origin-route-id':context.routeId||null",
            "article-learning-origin-question", "learning-origin-return-question",
            "context.edgeId?'你剛才查這條關係':'你從這個位置進來'",
            "open:!matchMedia('(max-width:340px)').matches",
            "root=h('details',{class:'mobile-origin-context'",
            "h('strong',{text:context.title})",
            "class:'mobile-origin-context-meta',text:context.mobileMeta",
            ".mobile-origin-context-meta{margin:0;padding:8px 9px 9px",
            "const mobileOrigin=renderMobileArticleOrigin(originContext)",
            "if(mobileOrigin)body.appendChild(mobileOrigin)",
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
            "entry-guide", "第一次來？先從問題開始",
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
            template.index("const notationGuide=readingMissionNotationGuide(article,mission)"),
            template.index("const termGuide=readingMissionTermGuide(lead.text,mission.question,glossaryTerms)"),
        )
        self.assertLess(
            template.index("const termGuide=readingMissionTermGuide(lead.text,mission.question,glossaryTerms)"),
            template.index("if(mission.orientation&&mission.orientation!==rawLead)"),
        )
        self.assertLess(
            template.index("section=h('section',{class:'reading-mission','aria-labelledby':'readingMissionTitle'},head,grid,actions)"),
            template.index("const notationGuide=readingMissionNotationGuide(article,mission)"),
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
            "body.appendChild(mobileBack);const mobileOrigin="
            "renderMobileArticleOrigin(originContext);if(mobileOrigin)body.appendChild(mobileOrigin);"
            "const originBar="
            "renderArticleLearningOrigin();if(originBar)body.appendChild(originBar);"
            "const routeTransition=renderRouteTransitionBridge(article);"
            "if(routeTransition)body.appendChild(routeTransition);"
            "const stationTransition=renderStationTransitionBridge(article);"
            "if(stationTransition)body.appendChild(stationTransition);"
            "body.appendChild(articleReaderHeading(article))",
            template,
        )
        self.assertIn(
            "body.appendChild(verification);const topicPosition=renderTopicLearningPosition(article);"
            "if(topicPosition)body.appendChild(topicPosition);const readingMission="
            "renderReadingMission(article,glossaryTerms);if(readingMission)body.appendChild(readingMission);"
            "const boundaryBrief=renderReaderBoundaryBrief(article,glossaryTerms);"
            "if(boundaryBrief)body.appendChild(boundaryBrief);"
            "const roleContext=renderArticleRoleContext(article);",
            template,
        )
        self.assertLess(
            template.index("const readingMission=renderReadingMission(article,glossaryTerms)"),
            template.index("const meta=h('div',{class:'article-meta'}"),
        )
        # 未編固定路線的位置提示先接在查核狀態後；三句重點後再建立族群角色與正式路線位置。
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

    def test_first_visit_guide_opens_with_direct_registered_route_starts(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="entryGuideRoutes"', "可直接開始的六條學習路線",
            "function renderEntryGuideRoutes()", "(MATURITY.learningRoutes||[]).forEach",
            "'data-testid':'entry-route-'+route.id",
            "root.appendChild(h('div',{role:'listitem'},button))",
            "openMaturityRouteArticle(route,route.firstArticleId)",
            "renderEntryGuideRoutes();renderGroupFilters()",
            "researchEntryGuideStateV1", "guide.open=saved!=='closed'",
            "guide.addEventListener('toggle'",
            "localStorage.setItem(key,guide.open?'open':'closed')",
            ".entry-guide-routes{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))",
            "@media(max-width:420px){.entry-guide-routes{grid-template-columns:1fr}}",
            ".entry-guide-route:focus-visible",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("foldCatalogGuideOnNarrow", template)

    def test_mobile_reading_mission_puts_the_start_action_before_the_reflection_question(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "'data-mission-question':'reflection'",
            "desktopFollowup=roleFirst?",
            "mobileFollowup=roleFirst?'先看產業角色；下方問題留作讀後檢查。':"
            "firstMain?'先讀三句重點；熟悉背景時可直接進第一節，下方問題留作讀後檢查。':"
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
            "plain=article.readerBoundaryBrief",
            "['thesis','先知道',plain.known]",
            "['unknown','先別下結論',plain.unknown]",
            "['next','接著怎麼查',plain.next]",
            "'data-boundary-source':hasPlain?'beginner':'summary'",
            "'data-reader-chars':value.length",
            "這篇目前能說到哪裡",
            "先用白話抓住已知、界線與查證方向；需要精確措辭時，再看完整研究摘要。",
            "白話卡逐字重用同篇「三句話抓重點」與「接下來怎麼追」；完整研究摘要保留原始主張與追蹤文字。",
            "body:not(.focus-mode) .reader-boundary-grid{grid-template-columns:1fr}",
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

    def test_topic_reader_handoff_reuses_only_adjacent_authored_headings(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function topicReaderSectionItems(article)",
            "section.h!=='新手先讀：這篇在講什麼'",
            "!ANALYST_HEADINGS.has(section.h)",
            "!isArticleAuditSection(article,section)",
            "function readerSectionHandoff(article,index)",
            "position=items.findIndex(item=>item.index===index)",
            "if(position<=0)return null",
            "'data-reader-section-handoff':current.h||''",
            "'data-reader-section-position':position+1",
            "'data-reader-section-total':total",
            "'data-reader-previous-heading':previous.h||''",
            "'data-reader-current-heading':current.h||''",
            "章節接力 · 第 '+(position+1)+'/'+total+' 節",
            "接著讀下方本節標題",
            "h('span',{text:'上一節'})",
            "標題逐字沿用原文；只表示本文先後，不代表上下游、因果、成熟度或投資排序。",
            "handoff=showReaderAids?readerSectionHandoff(article,index):null",
            "if(handoff)sectionEl.prepend(handoff)",
            ".reader-section-handoff{margin:0 0 12px",
            ".reader-section-handoff+h2{margin-top:0}",
            "@container (max-width:480px){.reader-section-handoff-head{display:block}",
        ):
            self.assertIn(contract, template)
        reader_render = template.index("const showReaderAids=mode==='reader'")
        self.assertLess(
            template.index("if(handoff)sectionEl.prepend(handoff)", reader_render),
            template.index("if(sectionMap)sectionEl.appendChild(sectionMap)", reader_render),
        )
        self.assertNotIn("section.readerSectionHandoff", template)

    def test_topic_main_question_anchor_reuses_catalog_question_only_at_first_main_section(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readerMainQuestionAnchor(article,index)",
            "if(article?.meta?.eventKind)return null",
            "question=catalogReaderQuestion(article)",
            "if(position!==0||!question)return null",
            "'data-main-question-anchor':article.id",
            "'data-main-question-section':current.h||''",
            "'data-main-question-text':question",
            "進入主正文 · 回到這篇要回答的問題",
            "問題逐字沿用文章首屏「讀完能回答」；只作閱讀定位，不改寫正文、研究結論或證據。",
            "mainQuestionAnchor=showReaderAids?readerMainQuestionAnchor(article,index):null",
            "if(mainQuestionAnchor)sectionEl.prepend(mainQuestionAnchor)",
            ".reader-main-question-anchor{margin:0 0 14px",
            ".reader-main-question-anchor+h2{margin-top:0}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("section.readerMainQuestion", template)

    def test_topic_article_frame_map_separates_distinct_authored_table_frameworks(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const READER_ARTICLE_FRAME_CONFIGS=[",
            "kind:'positions',pattern:/^本文[一二三四五六七八九十兩0-9]+個位置$/",
            "kind:'measures',pattern:/^本文[一二三四五六七八九十兩0-9]+把尺$/",
            "kind:'clocks',pattern:/^本文[一二三四五六七八九十兩0-9]+個時鐘$/",
            "kind:'roles',pattern:/^本文[一二三四五六七八九十兩0-9]+類角色$/",
            "kind:'gates',pattern:/^本文[一二三四五六七八九十兩0-9]+關$/",
            "function readerArticleFrameConfig(header)",
            "function readerArticleFrameItems(article)",
            "article?.type!=='topic'||article?.meta?.eventKind",
            "const table=(section.blocks||[]).find(block=>block.t==='table')",
            "firstHeader=runText(table?.head?.[0]||[])",
            "items.length<3||new Set(items.map(item=>item.kind)).size!==items.length",
            "function readerArticleFrameMap(article)",
            "'data-reader-article-frame-map':article.id",
            "'data-reader-frame-count':items.length",
            "'data-reader-frame-kind':item.kind",
            "'data-reader-frame-heading':item.section.h||''",
            "'data-reader-frame-header':item.firstHeader",
            "這篇正文會換 '+items.length+' 種讀法",
            "labels=items.map(item=>item.label).join('、')",
            "text:labels+'各自回答不同問題。先分清每一種讀法，再逐段深入。'",
            "focusReadingTarget(document.getElementById(sectionId(item.index)))",
            "按鈕只沿用本文既有表頭與章節順序；用途文案只說怎麼讀，不改寫研究內容。順序不代表上下游、因果、成熟度或投資排序。",
            "const frameMap=readerArticleFrameMap(article);if(frameMap)body.appendChild(frameMap)",
            ".reader-article-frame-map{margin:18px 0 20px",
            ".reader-article-frame-button{width:100%;min-height:112px",
            ".reader-article-frame-button:focus-visible{outline:3px solid",
            ".reader-article-frame-list{grid-template-columns:1fr}",
            ".reader-article-frame-button{min-height:68px",
        ):
            self.assertIn(contract, template)
        render_reader = template[
            template.index("function renderReader(article,hasRows=true)"):
            template.index("function renderAll()")
        ]
        self.assertLess(
            render_reader.index("const frameMap=readerArticleFrameMap(article)"),
            render_reader.index("body.appendChild(articleSections(article,'reader',glossaryTerms))"),
        )
        self.assertNotIn("article.readerArticleFrames", template)

        pcie = (ROOT / "notes" / "research_topics" /
                "2026-08-03_pcie6_compliance_ladder.md").read_text(encoding="utf-8")
        for authored_header in (
            "本文五個位置", "本文五把尺", "本文六個時鐘",
            "本文六類角色", "本文六關",
        ):
            self.assertIn(authored_header, pcie)

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
            "2026-08-12_chiplet_design_handoff_contracts.md": (
                "**這像蓋房子時的四份契約。**",
                "**機器可讀也有成熟度。**",
                "**這會改變研究順序。**",
            ),
            "2026-08-12_ai_hardware_sdc_lifecycle.md": (
                "**這像一個沒有冒煙的火災。**",
                "**每一站都要交接同一張病歷。**",
                "**通過一項測試，只代表那一項沒有抓到錯。**",
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

    def test_ai_rack_emc_guard_band_contract_separates_physics_metrology_and_rule(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-09_ai_rack_emc_certification.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 裕量不是保證：量測不確定度與判定規則要一起看",
            "## 同一個 38.5，為什麼可以是 pass、conditional pass 或 fail",
            "### 三條路都能變成 pass，發票卻可能落在不同地方",
            "### 多空小作文要共用七欄 EMC 邊界判定護照",
            "## 實驗室有認可標誌，為什麼仍不能替產品背書",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "reason: added_guard_band_decision_rule_and_two_lever_emc_boundary_example_without_thesis_or_clock_refresh",
            "source_id: S12", "source_id: S13",
            "claim_id: C15", "claim_id: C16", "claim_id: C17",
            "**容許限制／規格限制（TL）**",
            "**接受限制（AL）**", "**Guard band（w）**",
            "**符合性聲明（statement of conformity）**",
            "**偽接受／偽拒絕（false accept／false reject）**",
            "AL=40.0－3.0=37.0 dBµV/m",
            "| 38.5 dBµV/m | +1.5 dB | pass | fail | conditional pass |",
            "| 40.5 dBµV/m | −0.5 dB | fail | fail | conditional fail |",
            "| 排放路徑改善 2.0 dB | 36.5 | 3.0 | 3.0 | 37.0 | pass |",
            "| 量測不確定度縮小 2.0 dB | 38.5 | 1.0 | 1.0 | 39.0 | pass |",
            "| 只改成 simple acceptance | 38.5 | 3.0 | 0.0 | 40.0 | pass |",
            "| 1. 被測物 |", "| 5. 不確定度 |", "| 7. 處置與經濟結果 |",
            "N=4` 個量測值與 `N=4` 個決策設定",
            "11e90a6be33eea150b000984320d9f673a327bc8879a2b46615d26734cfa450a",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "process:emc-boundary-decision-passport,process,EMC 邊界判定七欄護照",
            "metric:emc-guard-band-acceptance-limit,metric,EMC guard band 與接受限制",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "ai_rack_emc_certification.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 17)
        for node in (
            "to_id: process:emc-boundary-decision-passport",
            "to_id: metric:emc-guard-band-acceptance-limit",
        ):
            self.assertIn(node, graph)

    def test_ai_rack_action_deadline_contract_separates_api_acceptance_from_safe_state(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-07_ai_rack_action_contract.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 同一個「成功」其實有五層：API 接受後還有四次核對",
            "## 202 Accepted 很快，為什麼安全隔離仍可能逾時",
            "### 同樣在 2.7 秒收到 202，兩個結局卻不同",
            "### 多空小作文要共用八欄安全狀態期限護照",
            "## 四種錯誤要用四種機制：版本、重送、仲裁與結果不能混用",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "reason: added_end_to_end_safe_state_deadline_budget_without_thesis_or_clock_refresh",
            "source_id: S13", "claim_id: C16", "claim_id: C17",
            "**安全狀態期限（safe-state deadline）**",
            "**端到端時間預算（end-to-end time budget）**",
            "**期限裕量（deadline margin）**",
            "`D_safe=8.0 秒`", "`3.5 秒`", "`4.8 秒`",
            "| 4. API 接受／Task 建立 | 0.4 秒 | 2.7 秒 | 2.7 秒 |",
            "| 5. 實體致動 | A 3.5 秒／B 4.8 秒 | 6.2 秒 | 7.5 秒 |",
            "| 6. 獨立物理確認 | 1.0 秒 | 7.2 秒 | 8.5 秒 |",
            "`33.75%`", "`5.3 秒`", "`90.0%`", "`106.25%`",
            "`+0.8 秒`", "`−0.5 秒`", "N=2` 個固定",
            "| 1. 事件與受控版本 |", "| 6. API 與 Task 時間 |",
            "| 8. 裕量、失敗與復原 |", "沒有 sampling SE／t",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "process:safe-state-deadline-passport,process,安全狀態期限八欄護照",
            "metric:end-to-end-safe-state-deadline-margin,metric,端到端安全狀態期限裕量",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph" / "ai_rack_action_contract.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 19)
        for contract in (
            "edge_id: KG-RAC-I17",
            "to_id: process:safe-state-deadline-passport",
            "edge_id: KG-RAC-I18",
            "to_id: metric:end-to-end-safe-state-deadline-margin",
        ):
            self.assertIn(contract, graph)

    def test_ai_rack_attestation_freshness_contract_separates_expiry_replay_and_authorization(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-08_ai_rack_trust_root.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 有簽章的量測報告，為什麼仍不是「可以執行指令」",
            "## 簽章有效、token 沒過期，為什麼仍可能被拒絕",
            "### 同一組時間與簽章狀態下的五個命運",
            "### 多空小作文要共享七欄新鮮度與重播帳",
            "## 用八欄遠端證明決策護照查一份平台資料",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "reason: added_attestation_token_age_nonce_consumption_and_authorization_boundary_without_thesis_or_clock_refresh",
            "source_id: S12", "claim_id: C17", "claim_id: C18",
            "**`iat`（Issued At）**", "**`exp`（Expiration Time）**",
            "**Nonce 消耗帳／重播快取**",
            "`max-age=60 秒`", "clock-skew leeway",
            "`5 秒`", "`N-42`", "至少 64 bits",
            "| fresh first use | 12:00:40／40 秒 | +80 秒 |",
            "| stale but unexpired | 12:01:10／70 秒 | +50 秒 |",
            "| wrong nonce | 12:00:40／40 秒 | +80 秒 |",
            "| replayed nonce | 12:00:41／41 秒 | +79 秒 |",
            "| expired beyond skew | 12:02:10／130 秒 | −10 秒",
            "N=5` 個固定案例", "沒有 sampling SE／t",
            "| 1. Claim 產生時間與範圍 |",
            "| 6. Nonce 消耗與重播紀錄 |",
            "| 7. Gate 輸出與下游決策 |",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 12),
            ("research_claim", 18), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "process:attestation-freshness-replay-ledger,process,遠端證明新鮮度與重播七欄帳",
            "metric:attestation-token-age-validity-window,metric,遠端證明token年齡與處理窗口",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph" / "ai_rack_trust_root.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 19)
        for contract in (
            "edge_id: KG-TRT-I16",
            "to_id: process:attestation-freshness-replay-ledger",
            "edge_id: KG-TRT-I17",
            "to_id: metric:attestation-token-age-validity-window",
        ):
            self.assertIn(contract, graph)

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
            ":labels[index]||'欄 '+(index+1)",
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
            "function readerTableSystemPositions(table,headers)",
            "if(!/(位置|環節|節點|路徑)/.test(firstHeader))return[]",
            "(table?.rows||[]).map(row=>runText(row?.[0]||[]).trim())",
            "positions.length<3||positions.length>8",
            "new Set(positions).size!==positions.length",
            "function readerTableGuide(table)",
            "const headers=(table?.head||[]).map(runText)",
            "const positions=readerTableSystemPositions(table,headers)",
            "readerTablePositions=[]",
            "readerTablePositions.length>0&&readerTablePositions.length===(node.rows||[]).length",
            "positionLabel='位置 '+(rowIndex+1)+'／'+readerTablePositions.length",
            "function readerTableStepCue(index,total)",
            "index===0?'先定位':index===total-1?'最後核對':'接著看'",
            "'data-label':systemFirst?positionLabel",
            "'data-reader-original-label':systemFirst?labels[index]:null",
            "'data-reader-system-row':systemFirst?rowIndex+1:null",
            "class:'reader-table-cell-guide'",
            "'data-reader-table-cell-step':index+1",
            "'aria-hidden':systemFirst?null:'true'",
            "h('b',{'aria-hidden':'true'",
            "h('small',{'aria-hidden':'true'",
            "String(index+1).padStart(2,'0')+' · '+readerTableStepCue(index,row.length)",
            "text:labels[index]||'欄 '+(index+1)",
            "class:'reader-table-system-row-label',text:positionLabel",
            "class:'table-wrap'+(systemRows?' reader-system-table':'')",
            "readerTablePositions=readerTableSystemPositions(item,tableHeaders)",
            "block(item,{readableProse:mode==='reader',readerProseProfile:showReaderAids?'topic':'default',textTransform,readerTablePositions})",
            "'data-reader-table-system-map':positions.length",
            "系統位置索引",
            "先把第一欄放在一起，知道本文正在比較哪些位置，再逐列核對其餘欄位。",
            "位置名稱逐字取自原表第一欄；編號只表示表內出現順序，不代表上下游、流程一定相連、重要性或受惠排序。",
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
            ".reader-table-system-steps{display:grid",
            ".reader-table-system-steps{grid-template-columns:1fr}",
            ".reader-table-system-label{min-width:0",
            ".reader-table-cell-guide,.reader-table-system-row-label{display:none}",
            ".article-section .reader-system-table td{display:block;padding:8px 11px}",
            ".article-section .reader-system-table td::before{content:none}",
            ".article-section .reader-system-table .reader-table-cell-guide{display:grid",
            "gap:4px 8px;margin:0 0 4px",
            ".article-section .reader-table-cell-guide b{font:700 9.5px/1.45",
            ".article-section .reader-table-cell-guide small{min-width:0",
            ".article-section .reader-system-table .reader-table-system-row-label{display:block",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("row.slice(1)", template)

    def test_template_turns_an_explicit_post_system_table_boundary_into_a_takeaway(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readerSystemTableTakeawayParts(node)",
            "node?.t!=='p'||(node.runs||[]).some(run=>run?.a||run?.b)",
            "canToken='這張表只',limitToken='它不能'",
            "text.indexOf(limitToken,canStart+canToken.length)",
            "text.indexOf(canToken,canStart+canToken.length)>=0",
            "text.indexOf(limitToken,limitStart+limitToken.length)>=0",
            "limitStart<=canStart||repeated",
            "!text.slice(0,canStart).endsWith('。')",
            "text.slice(0,canStart),text.slice(canStart,limitStart),text.slice(limitStart)",
            "kind:'principle',label:'01 · 先記住'",
            "kind:'scope',label:'02 · 能說到這裡'",
            "kind:'limit',label:'03 · 先不能說'",
            "function readerSystemTableTakeaway(node)",
            "'aria-label':'表格結論三句話'",
            "'data-reader-table-takeaway-part':index+1",
            "'aria-label':'表格讀完先收束'",
            "'data-reader-table-takeaway':parts.length",
            "'data-reader-table-takeaway-source-chars':parts.reduce",
            "三句文字逐字沿用表後原文；標籤只安排閱讀順序，不新增研究結論。",
            "let previousSystemTable=false",
            "takeaway=showReaderAids&&previousSystemTable?readerSystemTableTakeaway(item):null",
            "rendered=takeaway||block(item",
            "previousSystemTable=readerTablePositions.length>0",
            ".reader-table-takeaway{margin:4px 0 18px",
            ".reader-table-takeaway-steps{display:grid",
            ".reader-table-takeaway-item.limit{border-top-color:var(--amber)",
            "@container (max-width:620px){.reader-table-takeaway-steps{grid-template-columns:1fr}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("readerSystemTableTakeaway(item.rows", template)

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
            "function formalReaderDisplayText(article,value)",
            "function runs(nodes,{sentenceBreaks=false,textTransform=null}={})",
            "function readerProseNeedsBreak(text,sentenceCount,profile='default')",
            "if(sentenceCount<2)return false",
            "if(text.length>=120)return true",
            "profile==='topic'&&((text.length>=100)||(text.length>=80&&sentenceCount>=3))",
            "reader-prose-dense",
            "'data-reader-chars':text.length",
            "'data-reader-sentences':sentenceCount",
            "readerProseNeedsBreak(text,sentenceCount,readerProseProfile)",
            "readerProseProfile:showReaderAids?'topic':'default'",
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

    def test_template_turns_authored_fenced_text_flow_into_a_semantic_list(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function readerTextFlowItems(node,profile='default')",
            "profile!=='topic'||node?.t!=='p'",
            "text.match(/^```text\\s+([\\s\\S]*?)\\s+```$/i)",
            "split(/\\s*→\\s*/)",
            "items.length>=3&&items.length<=8",
            "function readerTextFlow(node,profile='default')",
            "class:'reader-flow-sequence'",
            "'data-reader-flow-steps':items.length",
            "'data-reader-flow-position':index+1",
            "'aria-label':'原文推論鏈，共 '+items.length+' 步'",
            "const flow=readableProse?readerTextFlow(node,readerProseProfile):null",
            ".reader-flow-sequence{margin:0 0 16px!important",
        ):
            self.assertIn(contract, template)
        # 顯示層只重排作者明寫的 fence／箭頭語法，不回寫研究 payload。
        self.assertNotIn("node.runs=readerTextFlowItems", template)

    def test_template_turns_exact_kpi_compass_bullets_into_a_definition_list(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const READER_KPI_COMPASS_ITEMS=[",
            "{label:'主要驅動 KPI',kind:'primary',hint:'先看 · 核心條件是否落地'}",
            "{label:'次要 KPI',kind:'secondary',hint:'再看 · 營運結果是否跟上'}",
            "{label:'常見假訊號',kind:'false-signal',hint:'避開 · 不能直接當成證據'}",
            "{label:'最關鍵分歧',kind:'key-fork',hint:'分辨 · 哪一條路徑正在發生'}",
            "function readerKpiCompass(node,profile='default')",
            "profile!=='topic'||node?.t!=='ul'",
            "String(item[0].s||'').trim()===READER_KPI_COMPASS_ITEMS[index].label",
            "runText(item.slice(1)).startsWith('：')",
            "class:'reader-kpi-compass'",
            "'data-reader-kpi-position':index+1",
            "'aria-label':'投資判讀四個位置'",
            "const compass=readableProse?readerKpiCompass(node,readerProseProfile):null",
            ".reader-kpi-compass-wrap{margin:0 0 16px",
            "@container (min-width:600px){.reader-kpi-compass{grid-template-columns:repeat(2,minmax(0,1fr))}}",
        ):
            self.assertIn(contract, template)
        # 只讀並複製原 runs 的顯示值，不回寫文章或把一般清單推成投資框架。
        self.assertNotIn("node.items=READER_KPI_COMPASS_ITEMS", template)

    def test_formal_reader_hides_internal_taxonomy_and_maintenance_terms_in_view_only(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const FORMAL_READER_OPAQUE_GROUP_IDS=new Set([",
            "'passive','powersupply','serverodm','semiequip','packtest','ipdesign'",
            "function formalReaderDisplayText(article,value)",
            "if(article?.type!=='formal_note')return source",
            "FORMAL_READER_OPAQUE_GROUP_IDS.has(groupId)",
            "groupById.get(groupId)?.label",
            "prefix+label",
            "'本文族群：'+label",
            "replace(/Universe 質化參考/g,'研究中心的公司質化參考')",
            "replace(/\\s+研究中心的公司質化參考/g,'研究中心的公司質化參考')",
            "replace(/查核狀態以 meta 與 `qual_notes\\.py --lint` 為準/g,'查核狀態請以文章上方標示為準')",
            "replace(/`last_updated`/g,'「更新日期」')",
            "replace(/「更新日期」\\s+/g,'「更新日期」')",
            "textTransform=mode==='reader'&&article.type==='formal_note'?value=>formalReaderDisplayText(article,value):null",
            "function readerLeadParts(article,value)",
            "source.replace(/\\[(S\\d+)\\]/gi",
            "article.type!=='formal_note'||item.kind!=='internal_taxonomy'",
            "rendered=takeaway||block(item,{readableProse:mode==='reader',readerProseProfile:showReaderAids?'topic':'default',textTransform,readerTablePositions})",
            "normalizedReaderRunTexts(source).map(text=>textTransform?textTransform(text):text)",
            "查核狀態沿用原始正式筆記；本頁只改善導覽，不改動原始證據邊界。",
            "研究內容以原始 Markdown 與查核資料為準",
        ):
            self.assertIn(contract, template)
        # 只轉換實際建立 DOM 的文字；原始 run、文章 sections 與 payload 都不回寫。
        self.assertNotIn("run.s=formalReaderDisplayText", template)
        self.assertNotIn("article.sections=formalReaderDisplayText", template)

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
            "article.type==='formal_note'?'先認識公司'",
            "article.type==='narrative'?'先看要驗證的說法':'先知道一件事'",
            "function catalogLearningPreview(article,readerQuestion)",
            "function catalogComparableText(value)",
            "function catalogTechnicalTitle(article,lead)",
            "titleKey.includes(leadKey)||leadKey.includes(titleKey)",
            "lead=readerLeadParts(article,rawLead)",
            "class:'result-learning-source'",
            "原文來源標記：",
            "if(technicalTitle)button.appendChild",
            "'data-catalog-learning-id':article.id",
            "text:catalogLearningLabel(article)",
            "text:'讀完能回答'",
            "'data-reader-question-type':article.type",
            "'data-reader-question-id':article.id",
        ):
            self.assertIn(contract, template)
        preview_source = template[
            template.index("function catalogLearningPreview(article,readerQuestion)"):
            template.index("function resultItem(article)")
        ]
        self.assertLess(
            preview_source.index("'data-catalog-learning':'question'"),
            preview_source.index("'data-catalog-learning':'lead'"),
        )
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
            "text:'目前怎麼看：'",
            ".result-learning-preview{display:grid",
            ".result-evidence{display:grid",
            "function restoreCatalogGuidePreference()",
            "const guide=document.getElementById('entryGuide')",
            "guide.open=saved!=='closed'",
            "guide.addEventListener('toggle'",
            "if(guide.hidden)return",
            "也不由 resize 覆寫",
        ):
            self.assertIn(contract, template)
        # 卡片只重排已發布的導讀、狀態與 readerEvidenceGuide，不回寫研究 payload。
        self.assertNotIn("article.readingMission=", template)
        self.assertNotIn("section.readerEvidenceGuide=", template)
        self.assertNotIn("article.status=", template)

    def test_article_check_data_is_collapsed_and_translates_research_operations(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function topicStatusReaderLabel(status)",
            "triaged:'已整理，持續查證'",
            "wrap=h('details',{class:'evidence'}",
            "h('summary',{class:'evidence-summary'}",
            "text:'文章查核資料'",
            "activeSourceCount+' 份可回查來源'",
            "text:'研究欄位與來源'",
            "['研究排程',priority?priority+'（只排研究工作）':'—']",
            "研究狀態與 P1 等排程代號只用來安排查核工作，不代表文章重要性、預期報酬或投資順位。",
            "text:'可回查來源'",
            "text:'開啟 GitHub 原始文件'",
            ".evidence>summary{min-height:52px;",
            ".evidence-summary-state::before{content:'展開'}",
            ".evidence[open] .evidence-summary-state::before{content:'收合'}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("h('h2',{text:'來源與證據摘要'})", template)

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

    def test_learning_route_handoffs_keep_the_system_question_and_completion_review(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function registeredLearningRoute(article)",
            "routeId?learningRouteById(routeId):null",
            "function learningRouteQuestionContext(article)",
            "整條路線要回答",
            "'data-route-question-id':route.id",
            "function learningRouteCompletionReview(article)",
            "回頭回答整條路線",
            "(route.phases||[]).filter(phase=>phase?.label)",
            "return review",
            "'data-route-review-id':route.id",
            "'data-route-phase-count':phases.length",
            "'data-route-review-collapsed':'true'",
            "text:(phase.graphIds||[]).length+' 站'",
            "問題、階段與站數逐字沿用既有學習路線",
            "function learningRouteBridge(card,sourceArticle)",
            "question=learningRouteQuestionContext(sourceArticle)",
            "function learningCard(card,primary=false,sourceArticle=null)",
            "card.kind==='route'?learningRouteCompletionReview(sourceArticle):null",
            "learningCard(cards[0],true,article)",
            "learningCard(card,false,article)",
            ".learning-route-bridge-question{",
            ".learning-route-bridge-takeaway{",
            "align-items:start;gap:9px;margin-bottom:9px",
            ".learning-route-completion-review{",
            ".learning-route-completion-phases{display:grid",
        ):
            self.assertIn(contract, template)
        self.assertTrue(bd.RESEARCH_LEARNING_ROUTES)
        for route in bd.RESEARCH_LEARNING_ROUTES:
            self.assertTrue(route.get("question"), route.get("id"))
            self.assertTrue(route.get("phases"), route.get("id"))

    def test_completed_route_review_is_compact_until_the_reader_opens_it(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "position=article?.learningRoute?'完成第 '",
            "summary=h('summary',{}",
            "class:'learning-route-completion-summary'",
            "text:phases.length+' 個階段 · 需要時再看總複習'",
            "class:'learning-route-completion-state','aria-hidden':'true'",
            "body=h('div',{class:'learning-route-completion-body'}",
            "review=h('details',{class:'learning-route-completion-review'",
            "body.appendChild(h('p',{class:'learning-route-completion-plan'",
            "review.appendChild(body)",
            "if(routeBridge||completion)item.appendChild(h('div',{class:'learning-route-card-footer'},meta,action))",
            "if(card.kind==='route')return'選下一條學習路線'",
            ".learning-route-completion-review>summary{min-height:84px",
            ".learning-route-completion-state::before{content:'展開總複習'",
            ".learning-route-completion-review[open] .learning-route-completion-state::before{content:'收合'",
            ".learning-route-completion-body{padding:9px 10px",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("review=h('section',{class:'learning-route-completion-review'", template)

    def test_next_station_route_context_is_compact_until_the_reader_opens_it(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "phaseSummary=bridge.fromPhaseLabel&&bridge.toPhaseLabel",
            "summary=h('summary',{}",
            "class:'learning-route-bridge-summary-copy'",
            "text:bridge.fromGraphLabel+' → '+bridge.toGraphLabel",
            "return h('details',{class:'learning-route-bridge'",
            "'data-route-context-collapsed':'true'",
            "class:'learning-route-bridge-body'",
            "card.description?h('p',{class:'learning-route-bridge-description'",
            "if(routeBridge)item.appendChild(routeBridge);else item.appendChild",
            "const meta=h('span',{class:'learning-card-meta'",
            "if(routeBridge||completion)item.appendChild(h('div',{class:'learning-route-card-footer'},meta,action))",
            ".learning-route-bridge>summary{min-height:72px",
            ".learning-route-bridge>summary::after{content:'展開脈絡'",
            ".learning-route-bridge[open]>summary::after{content:'收合'",
            ".learning-route-bridge-body{padding:9px 10px",
            ".learning-route-card-footer{display:grid",
            ".learning-route-card-footer .learning-card-action{margin:0}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("return h('aside',{class:'learning-route-bridge'", template)

    def test_completed_learning_route_returns_to_an_explicit_next_route_choice(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="graphRouteComplete"',
            'aria-labelledby="graphRouteCompleteTitle"',
            "function routeCompletionGraphOrigin(article)",
            "kind:'route-complete',source:'route-complete'",
            "articleScrollTop:reader?.scrollTop||0",
            "function routeCompletionChoices(origin)",
            "route.id!==origin.routeId",
            "function renderRouteCompletionOrigin(root,origin,article)",
            "你已完成「'+route.label+'」",
            "你剛完成的系統問題：'+route.question",
            "下一個想弄懂的系統問題",
            "'data-testid':'graph-route-next-'+candidate.id",
            "'aria-pressed':selected?'true':'false'",
            "問題與順序逐字沿用既有學習路線",
            "function chooseNextLearningRoute(routeId)",
            "activateGraphRoute(route.id)",
            "function syncRouteCompletionSelection(routeId)",
            "function routeStartArticle(route)",
            "'data-testid':'graph-route-next-start-action'",
            "openGraphArticle(start.article.id,routeTransitionArticleOrigin(selected,start.article.id))",
            "function bindLearningAction(action,card,sourceArticle=null)",
            "routeCompletionGraphOrigin(sourceArticle)",
            "bindLearningAction(action,card,sourceArticle)",
            "origin.kind==='route-complete'?'#learningPath .learning-card.kind-route .learning-card-action'",
            ".graph-route-next-grid{display:grid;grid-template-columns:repeat(3",
            ".graph-route-next-grid{grid-template-columns:1fr}",
        ):
            self.assertIn(contract, template)
        self.assertLess(
            template.index('id="graphRouteComplete"'),
            template.index('id="graphLearningKey"'),
        )

    def test_next_route_first_station_keeps_an_explicit_cross_route_bridge(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function routeTransitionArticleOrigin(route,articleId)",
            "kind:'route-transition'",
            "fromRouteId:completion.routeId",
            "toRouteId:route.id",
            "firstArticleId:articleId",
            "graphOrigin:{...completion,nextRouteId:route.id}",
            "openGraphArticle(start.article.id,routeTransitionArticleOrigin(selected,start.article.id))",
            "function routeTransitionContext(article)",
            "origin.firstArticleId!==article?.id",
            "article.readingMission?.keyPoints?.[0]",
            "article.readingMission?.question",
            "!station?.graphLabel",
            "function renderRouteTransitionBridge(article)",
            "'data-testid':'route-transition-bridge'",
            "'data-from-route-id':from.id",
            "'data-to-route-id':to.id",
            "跨路線接力",
            "剛完成的系統問題",
            "現在要回答的系統問題",
            "第一站先抓住",
            "讀完這站試著回答",
            "問題、重點與讀後追問都沿用已發布內容",
            "不代表兩條路線存在上下游、受惠、因果或投資排序",
            "context.kind==='route-transition'",
            "state.articleOrigin?.kind==='route-transition'",
            "origin.kind==='graph'||origin.kind==='route-transition'",
            "state.graphOrigin=origin.graphOrigin||state.graphOrigin",
            "[data-testid=\"graph-route-next-start-action\"]",
            ".route-transition-bridge{",
            ".route-transition-steps{display:grid;grid-template-columns:repeat(2",
            ".route-transition-back,.station-transition-back{display:none}",
        ):
            self.assertIn(contract, template)

    def test_route_next_article_carries_the_previous_station_framework(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function stationTransitionArticleOrigin(sourceArticle,card)",
            "kind:'station-transition'",
            "fromArticleId:sourceArticle.id",
            "toArticleId:target.id",
            "Number(to.step)!==Number(from.step)+1",
            "sourceArticle?.readingMission?.keyPoints?.[0]",
            "target?.readingMission?.question",
            "stationTransitionArticleOrigin(sourceArticle,card)||undefined",
            "'data-testid':card.kind==='article'&&card.routeStep?'learning-route-next-action':null",
            "function stationTransitionContext(article)",
            "origin.toArticleId!==article?.id",
            "const phaseChange=Boolean(fromStation.phaseId&&toStation.phaseId",
            "fromPhasePurpose=String(fromStation.phasePurpose||'').trim()",
            "Number(toStation.phaseStep)!==Number(fromStation.phaseStep)+1",
            "function renderStationTransitionBridge(article)",
            "'data-testid':'station-transition-bridge'",
            "'data-phase-change':phaseChange?'true':'false'",
            "同路線接力 · ",
            "把第 '+origin.fromStep+' 站的框架，帶進第 '+origin.toStep+' 站",
            "上一站先建立",
            "這站接著回答",
            "重點與問題逐字沿用前後兩篇既有文章",
            "跨階段接力 · ",
            "從「'+fromStation.phaseLabel+'」進入「'+toStation.phaseLabel+'」",
            "上一階段學到什麼",
            "下一階段要新增什麼",
            "從這一站開始練習",
            "階段目的來自正式學習路線",
            "不代表已掌握",
            "context.kind==='station-transition'",
            "state.articleOrigin?.kind==='station-transition'",
            "origin.kind==='station-transition'",
            "[data-testid=\"learning-route-next-action\"]",
            ".station-transition-bridge{",
            ".station-transition-track{display:grid;grid-template-columns:repeat(2",
            ".station-transition-bridge.phase-change{",
            ".station-transition-phase-track{display:grid;grid-template-columns:repeat(2",
            ".station-transition-phase-question{display:grid",
            ".route-transition-back,.station-transition-back{display:none}",
        ):
            self.assertIn(contract, template)

    def test_template_explains_why_a_shared_company_graph_connects(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function learningGraphBasis(card)",
            "card.kind!=='graph'||basis?.kind!=='stock'||!labels.length",
            "這篇為什麼連到這張圖",
            "共同公司 · ",
            "本文與圖譜都有相同公司節點",
            "下方只示範其中一家公司在圖譜中的既有關係",
            "'data-graph-basis-kind':'stock'",
            "'data-graph-basis-count':labels.length",
            "'data-graph-basis-ids':(basis.ids||[]).join('|')",
            "const graphBasis=learningGraphBasis(card)",
            ".learning-graph-basis{",
            ".learning-graph-basis-more>summary{min-height:44px}",
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
            "function openGraphArticle(articleId,origin=null)",
            "selectArticle(articleId,true,origin||graphArticleOrigin())",
            "graphOrigin:null", "function graphLearningOrigin(source='learning-card')",
            "return{kind:'article-learning',source,articleId:article.id",
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
            "openRadarGraph(route.graphId,view,'',graphLearningOrigin('route-context'))",
            "origin.source==='route-context'?'.learning-route-action'",
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
            "看這站證據關係 · ",
            "function learningRouteById(routeId)",
            "function learningRoutePhaseGroups(stations)",
            "purpose=String(station.phasePurpose||'').trim()",
            "function learningRouteStationReaderQuestion(station)",
            "function learningRouteStation(route,station,total,currentArticleId,mode)",
            "function learningRouteMap(route,currentArticleId='',mode='article')",
            "'data-testid':'learning-route-map-'+route.id",
            "'data-testid':'learning-route-station-'+route.id+'-'+station.step",
            "byId.get(station.articleId)?.readerQuestion||station.question",
            "sourceQuestion=String(station.question||'').trim()",
            "hasPlainQuestion?'這站先弄懂':'這站先回答'",
            "'data-reader-question':hasPlainQuestion?'article':'route'",
            "groupLabels=[...new Set((station.groupLabels||[]).map",
            "'data-station-group-count':groupLabels.length",
            "'aria-label':'這站研究範圍：'+groupLabels.join('、')",
            "class:'learning-route-station-groups-label',text:'這站會用到'",
            "h('strong',{text:primary}),h('small',{text:context})",
            "class:'learning-route-station-precise'",
            "'data-testid':'learning-route-precise-'+route.id+'-'+station.step",
            "讀完再試著回答精確追問",
            "h('p',{text:sourceQuestion})",
            "白話問題與精確追問都沿用同篇既有內容",
            "'aria-label':route.label+' 學習階段與站點'",
            "'data-phase-id':phase.id,'data-phase-purpose':phase.purpose||null,"
            "'data-current':isCurrent?'true':'false'",
            "summaryHint=current?'目前第 '+current.step+' 站'+phaseHint+'；可直接跳到任一站':'先比較每個階段任務，再決定從哪裡開始'",
            "shouldOpen=isCurrent",
            "class:'learning-route-phase-fold',open:shouldOpen",
            "'data-testid':'learning-route-phase-'+route.id+'-'+phase.step",
            "class:'learning-route-phase-summary'",
            "class:'learning-route-phase-purpose',text:phase.purpose",
            "class:'learning-route-phase-meta '+(isCurrent?'learning-route-phase-current':'')",
            "text:(isCurrent?'目前階段 · ':phase.stations.length+' 站 · ')+range",
            "summary.addEventListener('keydown',event=>{if(event.key!=='Enter'&&event.key!==' ')",
            "event.preventDefault();phaseFold.open=!phaseFold.open",
            "目前第 '+current.step+' 站'+phaseHint",
            "learningRouteMap(learningRouteById(route.id),article.id,'article')",
            "learningRouteMap(fullRoute,'','matrix')",
            "每站先沿用同篇既有讀者問句",
            "階段任務逐字沿用正式閱讀課綱",
            "「這站會用到」只列同篇正式研究範圍",
            "精確追問仍逐字保留在可展開內容與文章「想一想」",
            ".learning-route-map>summary:focus-visible",
            ".learning-route-phases{display:grid;gap:7px",
            ".learning-route-phase[data-current=\"true\"]",
            ".learning-route-phase-summary{min-height:44px",
            ".learning-route-phase-summary{min-height:66px",
            ".learning-route-phase-purpose{display:block",
            ".learning-route-phase-summary:focus-visible",
            ".learning-route-phase-fold[open] .learning-route-phase-state::before{content:'收合'}",
            ".learning-route-phase:has(>.learning-route-phase-fold[open]){grid-column:1/-1}",
            ".learning-route-phase-fold[open]>.learning-route-stations",
            ".learning-route-station-button{width:100%;min-height:72px",
            ".learning-route-station-groups{display:flex;flex-wrap:wrap",
            ".learning-route-station-precise>summary{min-height:44px",
            ".learning-route-station-precise>summary:focus-visible",
            "function resetGraphSurfaceScroll()",
            "graphPage.scrollTo(0,0)",
            "window.scrollTo(0,0)",
            "requestAnimationFrame(()=>requestAnimationFrame(reset))",
            "selectSurface('graph',true);resetGraphSurfaceScroll()",
            "if(card.kind==='route')return'選下一條學習路線'",
            ".graph-intro-action{width:100%;min-height:44px}",
            "phaseCue=phasePurpose?' 本階段任務：'+phasePurpose:''",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            "openRadarGraph(route.graphId,'company','',graphLearningOrigin('route-context'))",
            template,
        )
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
            "運算與互連", "設計、製程控制、測試與良率", "政策與合規", "資本投入與公司財務",
            "供電、保護與元件",
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

    def test_unrouted_market_topic_exposes_registered_learning_position(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "function renderTopicLearningPosition(article)",
            "article?.type!=='topic'||article.learningRoute",
            "const cards=article.learningPath?.cards||[]",
            "graphCards=cards.filter(card=>card.kind==='graph')",
            "articleCards=cards.filter(card=>card.kind==='article')",
            "collectionCards=cards.filter(card=>card.kind==='collection')",
            "文章位置 · 目前沒有固定站次",
            "讀完可從「'+graph.title+'」查看既有關係",
            "讀完可接著比較「'+nextArticle.title+'」",
            "研究中心尚未建立可回查圖譜或固定站次",
            "這是明示缺口，不會用相似題材補關係",
            "'data-testid':'topic-learning-position'",
            "'data-learning-position':'unrouted-topic'",
            "'data-graph-card-count':graphCards.length",
            "'data-article-card-count':articleCards.length",
            "'data-collection-card-count':collectionCards.length",
            "'data-testid':'topic-learning-position-jump'",
            "focusReadingTarget(document.getElementById('learningPathTitle'))",
            "const topicPosition=renderTopicLearningPosition(article)",
            "if(topicPosition)body.appendChild(topicPosition)",
            ".learning-position-context{",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("renderTopicLearningPosition(article.readerTitle", template)

    def test_dense_section_glossary_stays_folded_until_the_reader_needs_terms(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "const SECTION_GLOSSARY_FOLD_AT=4",
            "function sectionGlossaryTermButton(entry)",
            "folded=matches.length>=SECTION_GLOSSARY_FOLD_AT",
            "'data-section-term-count':matches.length",
            "'data-section-term-visible-count':folded?0:matches.length",
            "'data-section-term-folded-count':folded?matches.length:0",
            "matches.forEach(entry=>list.appendChild(sectionGlossaryTermButton(entry)))",
            "return h('details',attrs,summary",
            "名詞先不用背：本節 '+matches.length+' 個",
            "先讀內容；看到陌生詞再回來查",
            "全部詞名與解釋只取自同篇「名詞小字典」",
            ".section-glossary-fold>summary{min-height:52px",
            ".section-glossary-fold>summary:focus-visible",
            ".section-glossary-fold-state::before{content:'展開'}",
            ".section-glossary-fold[open] .section-glossary-fold-state::before{content:'收合'}",
            ".section-glossary-body{padding:10px 11px 11px",
            ".section-glossary-fold>summary{min-height:56px",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("SECTION_GLOSSARY_PREVIEW_LIMIT", template)
        self.assertNotIn("section-glossary-more", template)

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
            'id="graphReadingMission" aria-labelledby="graphReadingMissionTitle" aria-live="polite" aria-atomic="true"',
            'id="graphReadingMissionTitle"',
            'id="graphReadingMissionPosition"',
            'id="graphReadingPhasePurpose"',
            'id="graphReadingGraphFocus"',
            "function renderGraphReadingMission(graph,route)",
            "question=String(route?.question||'').trim()",
            "purpose=String(phase?.purpose||route?.description||'').trim()",
            "focus=String(graph.summary||'').trim()",
            "root.dataset.phaseId=phase?.id||''",
            "'本階段先練習 · '+phase.label",
            "'這張圖先看 · '+graph.label",
            "mission?.dataset.graphId!==graph.id",
            "整體問題與階段任務逐字沿用正式學習路線",
            "圖譜焦點逐字沿用目前圖譜摘要",
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
            ".graph-reading-mission-grid{grid-template-columns:1fr}",
        ):
            self.assertIn(contract, template)
        self.assertNotIn(
            ".graph-control-fold[open]>.graph-control-summary{display:none}",
            template,
        )
        self.assertNotIn(
            "document.getElementById('graphSummary').textContent=graph.summary+",
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

    def test_template_skips_already_visited_article_and_graph_handoffs(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            "sourceArticleId=state.graphOrigin?.kind==='article-learning'?state.graphOrigin.articleId:''",
            "article.id===sourceArticleId",
            "'data-testid':'graph-reader-article-already-read'",
            "完整研究脈絡就是剛才文章",
            "不另開同一篇",
            "function originAdjustedLearningCards(article)",
            "card.kind==='article'&&card.articleId===sourceArticleId",
            "card.kind==='graph'&&card.graphId===origin.graphId",
            "function learningOriginProgress(article,adjustment)",
            "'data-skipped-source-article':adjustment.skippedSource?'true':'false'",
            "'data-skipped-graph':adjustment.skippedGraph?'true':'false'",
            "本次已走到這裡",
            "下方先顯示尚未走過的下一站",
            "originProgress=learningOriginProgress(article,adjustment)",
            "if(originProgress)section.appendChild(originProgress)",
            ".learning-origin-progress{",
            ".graph-reader-foot.already-read strong",
        ):
            self.assertIn(contract, template)

    def test_template_publishes_ranked_candidate_research_radar(self):
        template = (SCRIPTS / "research_template.html").read_text(encoding="utf-8")
        for contract in (
            'id="surfaceRadar"', 'id="radarPage"', 'id="radarStats"',
            'id="radarMethod"', 'id="radarList"',
            "const RADAR=LIB.candidateRadar", "function renderRadar()",
            "function renderRadarCandidate(", "function openRadarGraph(",
            "'data-testid':'radar-'+candidate.id", "candidate.firstRejection",
            "candidate.nextEvidence", "candidate.nextCheck",
            "研究中心還在追哪些問題",
            "每張卡都是一個還沒有完整答案的產業問題", "已有文章與關係圖",
            "順序只安排研究先後，不代表預期報酬、股價方向或投資建議",
            "候選排名不是投資評分", "deepLink==='radar'",
            "candidate.readerQuestion", "candidate.readerStartingPoint",
            "candidate.readerNextStep",
            "candidate.readerTerms", "questionText=candidate.readerQuestion||candidate.title",
            "還沒回答完整的問題", "研究題名：", "目前先知道", "接著查什麼",
            "關鍵詞白話解釋", ".radar-reader-steps", ".radar-reader-start",
            "'data-reader-starting-point':candidate.id",
            "function radarArticleOrigin(", "function openRadarArticle(",
            "radarScrollTop:page?.scrollTop||0", "openRadarArticle(candidate)",
            "function radarReaderStatusLabel(candidate)",
            "promoted:'已有文章與關係圖'", "watch:'等待更多證據'",
            "function radarReaderActionGuide(", "function radarReaderActions(",
            "這題現在怎麼讀", "'data-radar-reader-status':candidate.status",
            "'data-radar-reader-article':hasArticle?'true':'false'",
            "'data-radar-reader-graph':hasGraph?'true':'false'",
            "已有文章可讀：先讀文章建立共同語言",
            "再展開下方 '+groupCount+' 個族群問句分清責任",
            "目前沒有文章可讀：先把它當成待驗證問題",
            "目前不投入完整研究：先保留問題",
            ".radar-reader-status{", ".radar-reader-status .radar-actions{margin:0}",
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
            "radarContextStates:new Map()", "function renderRadarContext(",
            "'data-radar-reader-context':candidate.id",
            "open:state.radarContextStates.get(candidate.id)===true",
            "看目前線索與產業角色", "termCount+' 個名詞'",
            "groupCount+' 個族群問句'",
            "context.addEventListener('toggle'",
            ".radar-reader-context>summary{min-height:50px",
            ".radar-reader-context-state::before{content:'展開'}",
            ".radar-reader-context[open] .radar-reader-context-state::before{content:'收合'}",
            ".radar-reader-status .radar-actions{width:100%;display:grid",
            "查看研究判定、原始文字與來源",
            "selectionLabel?radarBadge(selectionLabel,'selection'):null",
            "radarBadge(candidate.priorityLabel,candidate.priority)",
            "auditBadges,copy,track,foot", "研究方法與稽核資料（供查核）",
            "個待查問題", "題已有文章", "下次總檢查",
            'id="radarOverviewFold"', 'id="radarOverviewSummary"',
            'id="radarOverviewReady"', 'id="radarOverviewReadyList"',
            'id="radarOverviewAllFold"', 'id="radarOverviewAllSummary"',
            'id="radarOverviewList"', "function renderRadarOverview(candidates)",
            "function radarOverviewButton(candidate,mode='all')",
            "candidate.articleId&&byId.has(candidate.articleId)",
            "readySection.hidden=!ready.length",
            "ready.forEach(candidate=>readyList.appendChild(radarOverviewButton(candidate,'ready')))",
            "candidates.forEach(candidate=>list.appendChild(radarOverviewButton(candidate)))",
            "題可直接讀", "題先看問題", "現在可以讀",
            "先從已有文章的問題開始；完整研究順序仍保留在下方。",
            "查看全部候選問題", "全部 '+candidates.length+' 題 · 保留原研究順序",
            "已有文章可讀 · 閱讀約 '+article.readingMinutes+' 分鐘",
            "function focusRadarCandidate(candidateId)",
            "function focusRadarOverview()",
            "'data-radar-jump':candidate.id", "'aria-controls':targetId",
            "id:'radar-candidate-'+candidate.id", "tabindex:'-1'",
            "fold.open=!matchMedia('(max-width:780px)').matches",
            "card.scrollIntoView({block:'start'",
            "card.focus({preventScroll:true})",
            "fold.open=true", "summary.focus({preventScroll:true})",
            "class:'radar-map-return'", "text:'回候選題地圖'",
            "mapReturn.addEventListener('click',focusRadarOverview)",
            "研究順序只安排研究資源；不是重要性、報酬、族群受惠或投資排名",
            ".radar-overview-list{display:grid;grid-template-columns:repeat(4,minmax(0,1fr))",
            ".radar-overview-ready-list{display:grid;grid-template-columns:repeat(2,minmax(0,1fr))",
            ".radar-overview-item.ready{min-height:94px",
            ".radar-overview-all>summary{min-height:52px",
            "@media(max-width:1000px){.radar-overview-list{grid-template-columns:repeat(2,minmax(0,1fr))}}",
            "@media(max-width:780px){.radar-overview{scroll-margin-top:74px}.radar-overview>summary{min-height:64px",
            ".radar-overview-list{grid-template-columns:1fr}",
            ".radar-overview-ready-list{grid-template-columns:1fr}",
            ".radar-map-return{width:100%;min-height:44px}",
            "document.getElementById('surfaceRadar').addEventListener",
        ):
            self.assertIn(contract, template)
        self.assertNotIn("先用一句話理解", template)
        self.assertNotIn("class:'radar-question'", template)
        self.assertIn(".radar-card{display:block", template)
        self.assertIn(".radar-rank{min-height:42px;display:flex;flex-direction:row", template)
        self.assertIn("grid-template-columns:repeat(4,1fr)", template)
        self.assertNotIn("candidate.readerQuestion=", template)
        radar_card = template[
            template.index("function renderRadarCandidate(candidate)"):
            template.index("function renderMethodAudit()")
        ]
        radar_first_layer = radar_card.split("const copy=", 1)[0]
        self.assertNotIn("candidate.priorityLabel", radar_first_layer)
        self.assertNotIn("selectionLabel?radarBadge", radar_first_layer)
        self.assertEqual(radar_card.count("radarReaderActions(candidate)"), 1)
        self.assertIn("body.append(head,readerStatus,context)", radar_card)
        self.assertIn("renderRadarContext(candidate,reader,groupRoute,groupCount)", radar_card)
        self.assertIn("body.append(audit,mapReturn)", radar_card)
        self.assertNotIn("body.append(head,readerStatus,reader)", radar_card)
        self.assertNotIn("body.append(head,reader,groups,actions,audit", radar_card)

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
            "把一個產業問題拆成角色與文章", "族群起點", "開始學這個族群",
            "第一次來只看上半部", "下半部的完成度是研究資料是否齊全",
            "先選問題，再讀主題，最後追關係", "先選一個系統問題",
            "從 6 條既有學習路線，看每個問題會用到哪些族群",
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
            "function renderMaturityGroupStartPreview(row)",
            "start?.articleId&&byId.has(start.articleId)?byId.get(start.articleId):null",
            "'data-testid':'maturity-guide-start-card-'+row.id",
            "建議先讀", "帶著這題讀", "article.readerQuestion",
            "族群主題起點", "跨族群基礎起點",
            "第 '+start.step+'/'+start.total+' 站",
            "站次只說明它在完整路線的位置",
            "text:minutes?'讀這篇 · '+minutes+' 分鐘':'讀這篇'",
            "function maturityRoutesForGroup(", "function focusMaturityRoute(",
            "function openMaturityRouteGroup(groupId)",
            "selectMaturityEntry('groups');selectMaturityGuideGroup(groupId)",
            "routeGroups=(route.groupIds||[]).map(groupId=>groupById.get(groupId)).filter(Boolean)",
            "想先認識角色？這題會用到",
            "'data-testid':'maturity-route-group-'+route.id+'-'+group.id",
            "最容易和哪一層混淆",
            "function maturityGroupArticleOrigin(",
            "function maturityRouteArticleOrigin(",
            "function openMaturityGroupArticle(",
            "function openMaturityRouteArticle(",
            "openMaturityGroupArticle(row,start.articleId)",
            "openMaturityRouteArticle(route,route.firstArticleId)",
            "mode==='matrix'?openMaturityRouteArticle(route,station.articleId)",
            "state.maturityGuideGroupId", "data-maturity-guide-group",
            "'aria-pressed':'false'", "會出現在：",
            "看完整族群進度", "只表示既有閱讀路線收錄",
            "function renderMaturityCompanyEvidence(",
            "function renderMaturityCompleted(",
            "function openMaturityCompanyNote(",
            "function openMaturityCompanyGraph(",
            "function returnMaturityCompanyOrigin(",
            "從公司證據接下去", "1 先認識本業", "2 再看題材關係",
            "每家公司只選一條既有關係當起點",
            "不是代表公司、受惠名單或投資排名",
            "族群矩陣 → 公司證據", "maturity-company-note",
            ".maturity-company-evidence", ".maturity-completed-facts",
            ".maturity-group-explorer", ".maturity-group-choice",
            'id="maturityRouteCards"', "function renderMaturityLearningRoute(",
            "MATURITY.learningRoutes", "maturity-route-question",
            "fullRoute=learningRouteById(route.id)||route",
            "firstStation=stations.find(station=>station.articleId===route.firstArticleId)||stations[0]",
            "maturity-route-first", "第一站先建立", "phasePurpose",
            "'data-route-first-step':firstStep", "開始第 '+firstStep+'/'+routeTotal+' 站",
            "graphLabel+(firstMinutes?' · '+firstMinutes+' 分鐘':'')",
            "這條路線還會用到的族群；如需先認識角色可選擇",
            ".maturity-route-start{width:100%;min-height:48px",
            "族群重複出現，表示同一族群會在多個問題中出現",
            "function resetLibrarySurfaceScroll(", "resetLibrarySurfaceScroll()",
            "MATURITY.learningBoundary", 'id="catalogTitle"', "groupScope",
            "selectedGroups.length===1", "最大缺口", "不是產業成熟度、股票排名或受惠程度",
            "可水平捲動的族群研究成熟度矩陣",
            "完整查核矩陣與方法說明", "題材財務影響", "maturitySummarySentence",
        ):
            self.assertIn(contract, template)
        preview_start = template.index("renderMaturityGroupStartPreview(row),routeLinks")
        preview_companies = template.index(
            "renderMaturityCompanyEvidence(row,'preview')", preview_start
        )
        self.assertLess(preview_start, preview_companies)
        self.assertNotIn(
            '不熟族群名稱，從「先認識一個族群」開始', template
        )
        self.assertIn("已知道族群名稱？直接查找", template)
        self.assertLess(
            template.index('id="maturityRouteGuideTitle"'),
            template.index('id="maturityGroupExplorerTitle"'),
        )
        route_card = template.split(
            "function renderMaturityLearningRoute(route,index)", 1
        )[1].split("function maturityRoutesForGroup", 1)[0]
        self.assertLess(
            route_card.index("firstGuide,start,groups"),
            route_card.index("learningRouteMap(fullRoute"),
        )
        for contract in (
            "@media(min-width:781px){.maturity-route-card:has(.learning-route-map[open]){grid-column:1/-1}",
            ".learning-route-phases{grid-template-columns:repeat(auto-fit,minmax(240px,1fr));align-items:start}",
            ".learning-route-map-body>.learning-route-stations{grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}",
            ".maturity-route-group{min-height:32px",
            ".maturity-route-group:not(.static):focus-visible",
            ".maturity-route-group{min-height:44px;padding:6px 9px}",
            ".maturity-group-start-preview{margin-top:10px",
            ".maturity-group-start-preview-question{margin:7px 0 0",
            ".maturity-group-preview-actions{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));width:100%}",
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
        self.assertIn('"companyEvidence": company_evidence', builder)
        self.assertIn('"formalArticleId": (', builder)

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
            "台達管理層已把「液冷產品」連到 2025 年約占合併營收 10%",
            "## 容量可以換算，商業成熟度不能跟著換算",
            "| 2026-08-02 清單中的供應商 | 產品型號 | 來源原始容量 | 換算成 kW | 平台原始供應標籤 | 這一列只能證明 |",
            "## 額定容量只是操作包絡線的一個截面",
            "| 證據包要固定什麼 | 新手可以問的白話問題 | OCP 方法能支持到哪裡 | 還不能因此判定 |",
            "這張表是**判讀框架，不是認證名單**",
            "## 從規格到收入要過五關",
            "| 先問哪一關 | 這一關能回答什麼 | 本輪已有的公開證據 | 仍然缺什麼 |",
            "| 1. 容量規格 |", "| 2. 元件、整機與平台測試 |",
            "| 3. 供應準備 |", "| 4. 場域整合與客戶部署 |",
            "| 5. 公司收入 |",
            "## 財務分母階梯：10% 已經比部門代理更近，但還不是那台 CDU",
            "| 1. 公司液冷產品族 |", "| 2. 廣泛部門代理 |",
            "| 3. 具名型號橋接 |",
            "### DDP 改變報表呈現，不等於產品毛利變好",
            "## 一個 kW 要同時讀三張性能圖與一張量測身分證",
            "## 500 GPM 不是 2MW：先把流量、迴路溫升與 3°C ATD 拆開",
            "15.1894888737 K",
            "多空小作文先共用同一張熱工護照",
            "## 8 月 12 日方法補強：三張性能圖與量測身分證補上 kW 背後的問題",
            "## 同樣寫 kW，水基、PG25 與 PG55 仍是三條證據分支",
            "| 查核位置 | 水基路徑要保留什麼 | PG25／PG55 路徑要保留什麼 | 最容易出現的錯讀 |",
            "## 8 月 14 日方法補強：先固定流體分支，再談容量可比",
            "older_ocp_document_added_as_operating_envelope_and_reliability_decoder_no_thesis_clock_refresh",
            "added_three_performance_scorecards_and_typed_telemetry_context_no_thesis_change",
            "added_fluid_specific_capacity_and_qualification_branch_without_thesis_clock_refresh",
            "added_flow_temperature_heat_balance_bridge_without_thesis_clock_refresh",
            "q2_financial_denominator_evidence_reframed_thesis_from_platform_listing_to_named_model_bridge",
            "## 8 月 14 日方法補強：把 2MW、500 GPM 與 3°C ATD 放回正確位置",
            "## 8 月 14 日監測複核：先有公司液冷分子，仍沒有具名 CDU 橋接",
            "## 接下來看到什麼，判定才會改變",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 68
        )
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 主張與證據帳本", 1
        )[0]
        self.assertNotIn("Sample Ready", reflection)
        self.assertNotIn("MP Ready", reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 20),
            ("research_claim", 25), ("metric_comparison", 7),
            ("impact", 2), ("monitoring_item", 8),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        graph = (
            ROOT / "notes" / "knowledge_graph" / "liquid_cooling.md"
        ).read_text(encoding="utf-8")
        for edge_id in (
            "KG-LC-I10", "KG-LC-I11", "KG-LC-I12", "KG-LC-I13",
            "KG-LC-I14", "KG-LC-I15", "KG-LC-I16", "KG-LC-I17",
            "KG-LC-I18", "KG-LC-I19", "KG-LC-I20",
        ):
            self.assertIn(f"edge_id: {edge_id}", graph)
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for node_id in (
            "metric:cdu-operating-envelope",
            "metric:cdu-thermal-performance-curve",
            "metric:cdu-tcs-pressure-head-curve",
            "metric:cdu-fws-impedance-curve",
            "stage:cdu-assembly-qualification",
            "capability:cdu-reliability-validation",
            "concept:coolant-formulation-branch",
            "metric:propylene-glycol-concentration-freeze-envelope",
            "process:fluid-specific-cdu-rerating",
            "metric:cdu-flow-heat-balance-bridge",
        ):
            self.assertIn(f"{node_id},", concepts)
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
            "added_liquid_heat_flow_atd_pressure_and_pump_power_passport_without_thesis_clock_refresh",
            "added_dew_point_local_surface_and_economizer_passport_without_thesis_clock_refresh",
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
            "## 水質不是一個數字：先寫六欄流體生命週期合約",
            "| 合約欄位 | 必須固定什麼 | 怎麼驗 | 失敗訊號 | 不能被什麼替代 |",
            "| 1. 操作包絡 |", "| 2. 化學基準 |",
            "| 3. 浸液材料與變更控制 |", "| 4. 潔淨度與污染預算 |",
            "| 5. 試運轉基準 |", "| 6. 監測與行動責任 |",
            "## 四種品質失效不是同一種髒",
            "| 結垢（scaling） |", "| 污堵（fouling） |",
            "| 腐蝕（corrosion） |", "| 微生物生長 |",
            "## 同樣 1MW，為什麼還要分熱量、流量、ATD、壓差與泵功",
            "800kW×1.5LPM/kW＝1,200LPM，比 W2 的標準水換算高 4.5%",
            "| W1 | 800kW | 5K | 2,296.651 LPM |",
            "| W2 | 800kW | 10K | 1,148.325 LPM |",
            "| W3 | 800kW | 15K | 765.550 LPM |",
            "| T1 | 25°C | 30°C | 40°C | 5K | 10K |",
            "| T2 | 27°C | 30°C | 40°C | 3K | 10K |",
            "| P1 | 1,200LPM | 200kPa | 70% | 5.714kW | 50.057MWh |",
            "| P2 | 1,200LPM | 400kPa | 70% | 11.429kW | 100.114MWh |",
            "| P3 | 1,200LPM | 200kPa | 50% | 8.000kW | 70.080MWh |",
            "### 多空小作文共用的液冷熱工—水力十欄護照",
            "Python Fraction 與獨立 awk 在顯示精度內完全",
            "沒有 sampling\nSE／t",
            "## 同樣 60% RH，露點可差 7.5°C：防結露要看最冷表面",
            "**局部露點裕度＝最冷局部表面溫度－同位置露點。**",
            "| D1 | 27°C | 60% | 18.579°C | 20°C | ＋1.421K |",
            "| D2 | 35°C | 60% | 26.066°C | 20°C | −6.066K |",
            "| D3 | 27°C | 40% | 12.271°C | 20°C | ＋7.729K |",
            "D1 與 D2 都是 60% RH，露點卻相差 7.4867°C",
            "CAP1 表面約第 6 分鐘落到露點以下",
            "### 多空小作文共用的防結露—economizer 十欄護照",
            "Python\nDecimal 與獨立 awk 重算",
            "production site 的同步表面圖、事件率",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 59
        )
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 主張與證據帳本", 1
        )[0]
        for jargon in ("FWS", "TCS", "rackLocationId"):
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 16),
            ("research_claim", 21), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        for source_id in (
            "S9", "S10", "S11", "S12", "S13", "S14", "S15", "S16"
        ):
            self.assertIn(f"source_id: {source_id}", topic)
        for claim_id in (
            "C13", "C14", "C15", "C16", "C17", "C18", "C19", "C20", "C21"
        ):
            self.assertIn(f"claim_id: {claim_id}", topic)
        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "liquid_cooling_loop_boundaries.md"
        ).read_text(encoding="utf-8")
        for edge_id in (
            "KG-LCB-I21", "KG-LCB-I22", "KG-LCB-I23", "KG-LCB-I24"
        ):
            self.assertIn(f"edge_id: {edge_id}", graph)
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for node_id in (
            "process:liquid-loop-thermal-hydraulic-passport",
            "metric:liquid-heat-flow-pressure-pump-boundary",
            "process:liquid-cooling-dew-point-passport",
            "metric:local-dew-point-surface-margin",
        ):
            self.assertIn(f"{node_id},", concepts)
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
            "added_kv_tiering_measurement_passport_and_refreshed_exact_host_storage_edges",
            "added_roofline_workload_boundary_and_memory_performance_passport_without_thesis_clock_refresh",
            "人工智慧系統不會把所有資料都塞在同一個地方",
            "架構、容量型號、樣品、量產與收入必須分開判讀",
            "## 先按資料的急迫程度分四層",
            "| 資料任務 | 本文怎麼分位置 | 為什麼放這裡 | 本輪產品名稱 | 目前不能因此判定 |",
            "| 正在計算、最怕等待的工作資料 |",
            "| 容量較大、仍需快速取用的系統資料 |",
            "| 可以重新建立、也可能需要共享的上下文資料 |",
            "| 容量最大、可接受較慢存取或需長期保存的資料 |",
            "## 分層不是靜態樓層：還要分清介質、處理、連接、搬運與決策",
            "| 存放介質 | HBM、system RAM／SOCAMM、CMX、local SSD、shared storage |",
            "| 資料處理 | Vera／BlueField-4 STX 文件所述的壓縮、加密、完整性與復原 |",
            "| 連接路徑 | CXL，以及平台既有的記憶體、儲存與網路路徑 |",
            "| 搬運工具 | NIXL 等資料移動介面 |",
            "| 控制決策 | Dynamo、KV block manager 與資料放置規則 |",
            "## 一個可驗證的資料放置迴路",
            "## 再用八格量測護照判斷「多一層」有沒有真的更好",
            "| 八格量測護照 | 要固定什麼 | 要保存什麼 | 少了最容易誤讀成 |",
            "| 1. 受測系統與版本 |",
            "| 4. 重用機會與冷熱起點 |",
            "| 7. 機制是否真的發生 |",
            "| 8. 使用者結果與代價 |",
            "## 一個 TTFT 數字不能替整條資料路徑背書",
            "| TTFT | 使用者送出請求後多久看到第一個 token |",
            "| Good-request／errors／quality |",
            "## HBM 寫著 TB/s，為什麼應用仍可能沒有同幅加速",
            "Roofline 效能上限 P = min（運算上限，記憶體可持續頻寬 × I）",
            "| A：大量搬運 | 120 TFLOP | 12 TB | 10 FLOP/byte | 30 TFLOP/s | 4.0000 秒；memory-bound |",
            "| B：剛好轉折 | 120 TFLOP | 3 TB | 40 FLOP/byte | 120 TFLOP/s | 1.0000 秒；落在 ridge point |",
            "| C：高度重用 | 120 TFLOP | 1.5 TB | 80 FLOP/byte | 120 TFLOP/s | 1.0000 秒；compute-bound |",
            "### 多空小作文共用一份十欄記憶體效能護照",
            "| 4. bytes 分母與參考層 |",
            "| 8. achieved 與 Roofline efficiency |",
            "| 10. 能源、成本、部署與財務 |",
            "## 先問工作負載，再問該買哪一種記憶體",
            "## 用一份 KV cache 看懂資料如何旅行",
            "## 新手最常混在一起的八件事",
            "## 在研究中心裡接著怎麼學",
            "## 四層互補，不是誰取代誰",
            "## 同一家族也要拆到容量型號：192GB 與 256GB 不是同一個時鐘",
            "| 具名容量：192GB | Micron 3 月 16 日明列 high-volume production |",
            "| 具名容量：256GB | Micron 3 月 5 日明列 customer sampling |",
            "| 產品家族 | Micron 6 月 24 日表示 LP5X SOCAMM2 products 已量產",
            "## 每一層的商業進度要各自驗證",
            "| 資料層或連接路徑 | 已看到的一手證據 | 目前走到哪一步 | 還缺哪些商業證據 |",
            "| 圖形運算晶片旁的高速層（HBM4） |",
            "| 中央處理器旁的系統記憶體（SOCAMM） |",
            "| 共享上下文層（CMX） |",
            "| 記憶體擴充連接（CXL 4.0） |",
        ):
            self.assertIn(contract, topic)
        section_order = (
            "## 先按資料的急迫程度分四層",
            "## 分層不是靜態樓層：還要分清介質、處理、連接、搬運與決策",
            "## 一個可驗證的資料放置迴路",
            "## 再用八格量測護照判斷「多一層」有沒有真的更好",
            "## 一個 TTFT 數字不能替整條資料路徑背書",
            "## HBM 寫著 TB/s，為什麼應用仍可能沒有同幅加速",
            "## 先問工作負載，再問該買哪一種記憶體",
            "## 用一份 KV cache 看懂資料如何旅行",
            "## 新手最常混在一起的八件事",
            "## 在研究中心裡接著怎麼學",
            "## 四層互補，不是誰取代誰",
            "## 同一家族也要拆到容量型號：192GB 與 256GB 不是同一個時鐘",
            "## 每一層的商業進度要各自驗證",
        )
        self.assertEqual(
            [topic.index(section) for section in section_order],
            sorted(topic.index(section) for section in section_order),
        )
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 61
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
            ("research_topic", 1), ("research_source", 19),
            ("research_claim", 23), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 6),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        for evidence_contract in (
            "claim_id: C9\nlabel: verified",
            "claim_id: C10\nlabel: verified",
            "claim_id: C11\nlabel: inference",
            "claim_id: C12\nlabel: verified",
            "S9 只對 192GB 明列 high-volume production",
            "不能用同一個家族名稱把所有容量自動升到最高成熟度",
            "KV I/O、metadata、data placement、security 與 control operations",
            "claim_id: C13\nlabel: verified",
            "claim_id: C18\nlabel: verified",
            "claim_id: C19\nlabel: inference",
            "claim_id: C20\nlabel: unverified",
            "claim_id: C21\nlabel: verified",
            "claim_id: C22\nlabel: verified",
            "claim_id: C23\nlabel: inference",
            "只有在 cache reuse 的收益高於資料搬移 overhead 時",
            "同一份 baseline-versus-treatment 量測護照",
            "可達浮點效能上限寫成 peak compute",
            "這只是需要 profiler 補強的第一階近似",
            "同一份十欄效能護照",
        ):
            self.assertIn(evidence_contract, topic)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "product:micron-socamm2-192gb,product,Micron 192GB SOCAMM2",
            "product:micron-socamm2-256gb,product,Micron 256GB SOCAMM2",
            "product:nvidia-bluefield4-stx,product,NVIDIA Vera BlueField-4 STX",
            "capability:ai-context-placement,capability,AI 上下文資料放置",
            "capability:heterogeneous-data-movement,capability,異質記憶體資料搬移",
            "capability:ai-storage-data-processing,capability,AI 儲存資料處理",
            "metric:ai-data-path-end-to-end-slo,metric,AI 資料路徑端到端服務目標",
            "metric:kv-cache-reuse-transfer-observability,metric,KV 快取重用與搬移可觀測欄位",
            "metric:ai-inference-service-slo,metric,人工智慧推論服務等待與合格吞吐",
            "process:ai-memory-tier-measurement-passport,process,人工智慧記憶體分層八格量測護照",
            "process:memory-roofline-performance-passport,process,記憶體Roofline效能十欄護照",
            "metric:operational-intensity-ridge-point-boundary,metric,操作強度與轉折點瓶頸邊界",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph" / "ai_memory_hierarchy.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 25)
        for graph_contract in (
            "edge_id: KG-MEM-C03",
            "to_id: product:micron-socamm2-192gb",
            "to_id: product:micron-socamm2-256gb",
            "to_id: product:nvidia-bluefield4-stx",
            "to_id: capability:ai-context-placement",
            "to_id: capability:heterogeneous-data-movement",
            "to_id: capability:ai-storage-data-processing",
            "to_id: metric:ai-data-path-end-to-end-slo",
            "to_id: metric:kv-cache-reuse-transfer-observability",
            "to_id: metric:ai-inference-service-slo",
            "to_id: process:ai-memory-tier-measurement-passport",
            "to_id: process:memory-roofline-performance-passport",
            "to_id: metric:operational-intensity-ridge-point-boundary",
        ):
            self.assertIn(graph_contract, graph)
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
            "added_workload_interface_base_die_firmware_manufacturing_and_qualification_handoff_contract_without_refreshing_thesis_clock",
            "## 客製不是一顆晶片：六份交接合約要一起凍結",
            "| 本文六份交接合約 | 要固定哪些欄位 | 現有一手資料提供的入口 | 沒有這份合約會發生什麼誤讀 |",
            "| 1. 工作負載與功能 |", "| 2. 容量、速度、功耗與介面 |",
            "| 3. 底部邏輯與智財 |", "| 4. 韌體與系統軟體 |",
            "| 5. 製造、封裝與熱 |", "| 6. 樣品、資格與商業 |",
            "### 一個功能變更，為什麼會沿六份合約傳下去",
            "source_id: S9", "source_id: S10", "source_id: S11",
            "source_id: S12", "claim_id: C8", "claim_id: C9",
            "claim_id: C10", "claim_id: C11", "claim_id: C12",
            "added_affected_fraction_data_movement_and_workload_performance_passport_without_thesis_clock_refresh",
            "## 七倍不是 base die 快七倍：先拆時間占比與資料搬移",
            "maximum inference throughput 約七倍",
            "### 先拆受影響時間：局部變快不會等幅變成整體變快",
            "整體加速比＝1 ÷〔(1−f)＋f ÷ r〕",
            "| 甲：一半時間真的命中 | 50% | 4.000000 倍 | 0.625000 | 1.600000 倍 | 2.000000 倍 |",
            "| 乙：大部分時間真的命中 | 80% | 4.000000 倍 | 0.400000 | 2.500000 倍 | 5.000000 倍 |",
            "### 再拆資料搬移：少搬 75% bytes 也不等於整體快四倍",
            "| 搬移前 | 2,000 | 1,000 | 2.000000 FLOP／byte | 200.000000 GFLOP/s | 200.000000 GFLOP/s |",
            "| 假想搬移後 | 2,000 | 250 | 8.000000 FLOP／byte | 800.000000 GFLOP/s | 600.000000 GFLOP/s |",
            "### 多空小作文共用的 Custom HBM 工作搬移十欄護照",
            "| 1. 產品與工作身分 |", "| 4. 資料搬移邊界 |",
            "| 7. 功耗、能量與熱 |", "| 10. 量產與財務 |",
            "第一個教材是 N＝2 個匿名時間分解情境",
            "第二個教材是同一匿名 Roofline 情境的 N＝2 個固定狀態",
            "Python Fraction 與獨立 awk",
            "sampling SE／t",
            "source_id: S13", "source_id: S14", "claim_id: C13",
            "claim_id: C14", "claim_id: C15", "claim_id: C16",
            "monitor_id: T3",
            "last_reviewed_at: 2026-08-03",
            "review_due: 2026-09-15",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 57
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
            ("research_topic", 1), ("research_source", 14),
            ("research_claim", 16), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
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
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "custom_hbm_scope_ladder.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 21)
        for concept_id, edge_id in (
            ("concept:custom-hbm-workload-contract", "KG-CHBM-I11"),
            ("concept:custom-hbm-interface-contract", "KG-CHBM-I12"),
            ("concept:custom-hbm-base-die-contract", "KG-CHBM-I13"),
            ("concept:custom-hbm-firmware-contract", "KG-CHBM-I14"),
            ("concept:custom-hbm-manufacturing-thermal-contract", "KG-CHBM-I15"),
            ("stage:custom-hbm-handoff-qualification", "KG-CHBM-I16"),
            ("process:custom-hbm-work-movement-performance-passport", "KG-CHBM-I17"),
            ("metric:affected-fraction-operational-intensity-boundary", "KG-CHBM-I18"),
        ):
            with self.subTest(concept_id=concept_id, edge_id=edge_id):
                self.assertIn(concept_id, concepts)
                self.assertIn(f"to_id: {concept_id}", graph)
                self.assertIn(f"edge_id: {edge_id}", graph)

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
            "先分清玻璃是製造後會被剝離的暫時載板",
            "商業化還要依序看完整產品是否完成客戶可靠度測試",
            "## 先問：這片玻璃最後會不會留在封裝裡",
            "| 本文四類角色 | 玻璃在製程或產品裡做什麼 | 最後是否留在封裝 |",
            "| 1. 暫時玻璃載板 |", "| 2. 穿孔玻璃／玻璃中介層 |",
            "| 3. 玻璃核心封裝基板 |", "| 4. 晶圓／面板加工形式 |",
            "## 先把玻璃基板商業化拆成五關",
            "| 本文五關 | 這一關要回答 | 主要接力角色 | 看到這些仍不能直接跳到下一關 |",
            "| 1. 能力與設備就位 |", "| 2. 交出可測樣品 |",
            "| 3. 完成客戶驗證 |", "| 4. 穩定製造 |",
            "| 5. 重複出貨與收入 |",
            "## 同一句「可靠度通過」，可能在測三個不同東西",
            "| 本文三把尺 | 實際測什麼 | 通過後能說什麼 | 還不能說什麼 |",
            "| 1. 材料／局部結構可靠度 |",
            "| 2. 供應商產品與製程可靠度 |",
            "| 3. 客戶產品資格與壽命 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 49
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
            ("research_topic", 1), ("research_source", 16),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
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
            "split_specification_and_product_clocks_after_first_hbf_technical_specification",
            "added_hbf_nominal_usable_working_set_and_simulation_to_service_evidence_bridge_without_thesis_or_clock_refresh",
            "新的記憶體層不能只提供更大容量",
            "規則前進不等於產品同步前進",
            "## 先判斷它能不能成為新的記憶體層",
            "| 本文五項系統條件 | 讀者先問 | 沒通過會怎樣 | 主要接力角色 | 本輪可確認到哪裡 |",
            "| 1. 容量與資料保留 |", "| 2. 讀取與等待時間 |",
            "| 3. 寫入、更新與耐久 |", "| 4. 功耗、熱與封裝 |",
            "| 5. 系統整合與軟體調度 |",
            "## 第一版技術規格先對齊哪四份合約",
            "| 四份共同合約 | 公告摘要對齊什麼 | 初學者要避免的誤讀 | 下一份可升級證據 |",
            "| 1. 產品包絡 |", "| 2. 主機與電氣介面 |",
            "| 3. 堆疊、封裝與可靠度 |", "| 4. 軟體讀寫 |",
            "## 512GB、1.6TB/s 與「只差 2.2%」是三種不同證據",
            "| 看到的數字 | 證據層 | 分子與分母至少還要綁定 | 目前不能說 |",
            "`within 2.2% of unlimited-capacity HBM`",
            "### 405B×8-bit 只得到純權重 payload，不是整個工作集",
            "`405GB`", "`79.1015625%`", "`107GB`",
            "N=1 個假想 weights-only payload",
            "### 同一顆記憶體要過三張成績單",
            "| 1. 裝置與規格 |", "| 2. 模型與資料路徑 |",
            "| 3. 服務與商業結果 |",
            "### 多空小作文必須共用同一個推論情境",
            "| 偏多：更大近端非揮發容量減少資料搬移 |",
            "| 偏空：較高延遲、較大 page 與寫入邊界抵銷容量 |",
            "## 用兩個時鐘避免把規格當產品",
            "| 證據時鐘 | 依序要經過 | 截至本輪的位置 | 還不能說 |",
            "| 規格時鐘 |", "| 產品時鐘 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 56
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
            ("research_topic", 1), ("research_source", 12),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "hbf_commercialization.md"
        ).read_text(encoding="utf-8")
        for concept in (
            "process:hbf-simulation-to-service-evidence-bridge,process,HBF 模擬到服務三層證據橋",
            "metric:hbf-nominal-usable-working-set-capacity-contract,metric,HBF 名目可用與工作集容量契約",
        ):
            self.assertIn(concept, concepts)
        for edge_id in range(17, 19):
            self.assertIn(f"edge_id: KG-HBF-I{edge_id}", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 22)
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
            "用四層契約讀懂 SPHBM4\n"
        ))
        for contract in (
            "editorial_plain_language_wave93_sphbm4_signal_tradeoffs_roles_and_six_gate_ladder",
            "corrected_pin_count_frame_with_four_layer_interface_package_and_qualification_contract",
            "記憶體可以用很多條較慢的資料線，也可以用較少但更快的資料線",
            "主標準與一家供應商的對應介面路徑已出現",
            "## 先把一顆 SPHBM4 拆成四層",
            "| 四層契約 | 這一層在做什麼 | JEDEC 公開資料已確認 | 尚未被公開資料證明 |",
            "| 1. 記憶體裸晶與堆疊 |", "| 2. 介面基礎晶片 |",
            "| 3. 分散式主機通道 |", "| 4. 接點圖與有機封裝 |",
            "### 512 是資料訊號，不是「整顆只有 512 個接點」",
            "## 相同總傳輸量，不等於每一次存取體驗相同",
            "| 閱讀問題 | 已知的架構變化 | 必須另外驗證 |",
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
            "## 最後用七關判斷標準能不能變成收入",
            "| 本文七關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |",
            "| 1. 主標準發布 |", "| 2. 封裝接點契約公開 |",
            "| 3. 介面晶片與主機 PHY 完成 |", "| 4. 記憶體與封裝樣品完成 |",
            "| 5. 運算晶片與系統整合 |", "| 6. 客戶資格與可靠度通過 |",
            "| 7. 穩定量產與形成收入 |",
            "## 把「標準存在」拆成四條時鐘",
            "lane_raw_payload_energy_and_phy_measurement_passport_added_without_thesis_clock_refresh",
            "## 2,048 變 512，只守住 raw throughput 的等式",
            "2,048×1 與 512×4",
            "資料訊號數機械上減少 75%",
            "### 同一個 raw，payload 與每位元能耗仍可分岔",
            "1,945.6 Gbps",
            "1,638.4 Gbps",
            "6.315789",
            "15.789474%",
            "58.333333%",
            "### 延遲與 BER 要先固定量測點",
            "Serializer → Deserializer",
            "Packet／FEC／CRC → Packet／FEC／CRC",
            "### 512 條資料訊號也不能直接算 shoreline density",
            "### 多空小作文共用的 SPHBM4 PHY 十欄護照",
            "| 1. 標準與產品身分 |",
            "| 5. payload 與工作負載 |",
            "| 7. BER 與恢復 |",
            "| 10. silicon 到財務 |",
            "第一個教材是 N＝2 種公開架構映射",
            "第二個教材是 N＝2 個匿名假想 PHY 實作",
            "Python Fraction 與獨立 awk",
            "沒有 sampling SE／t",
            "OCP 官方 PDF 共 44 頁",
            "pp.32–42 已由官方瀏覽器 PDF viewer 逐頁渲染目視核對",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "claim_id: C13",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 41
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先把一顆 SPHBM4 拆成四層", 1
        )[0]
        for jargon in (
            "JEDEC", "JESD330-4", "SPHBM4", "HBM4", "DRAM", "SerDes",
            "base die", "data signals", "throughput", "Micron", "SK hynix",
            "CoWoS", "ABF", "BT",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 8),
            ("research_claim", 13), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "process:sphbm4-phy-performance-passport,process,SPHBM4 PHY 效能十欄護照",
            "metric:sphbm4-lane-raw-payload-energy-boundary,metric,SPHBM4 通道、raw、payload 與能耗邊界",
        ):
            self.assertIn(concept, concepts)
        graph = (ROOT / "notes" / "knowledge_graph" / "hbm.md").read_text(
            encoding="utf-8"
        )
        self.assertEqual(graph.count("<!-- knowledge_edge"), 40)
        for node in (
            "edge_id: KG-HBM-I28",
            "to_id: process:sphbm4-phy-performance-passport",
            "edge_id: KG-HBM-I29",
            "to_id: metric:sphbm4-lane-raw-payload-energy-boundary",
        ):
            self.assertIn(node, graph)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE,"
            "記憶體接點變少，為什麼不代表成本一定下降或產品已經可用？",
            guide,
        )

    def test_ai_memory_station_six_separates_application_generation_paths_and_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_hybrid_bonding_readiness.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 同樣叫混合接合，成熟度可以差很多："
            "先分應用世代，再看五個製程窗口\n"
        ))
        for contract in (
            "editorial_plain_language_wave94_hybrid_bonding_paths_process_windows_and_six_gate_ladder",
            "split_hybrid_bonding_maturity_by_application_process_generation_and_product_stage",
            "成熟的是其中幾個明確格子",
            "200 奈米整片試驗",
            "## 先畫四維地圖：成熟的是哪一格",
            "| 應用或產品格 | 接法與介面範圍 | 公開證據到哪裡 | 可以說什麼 | 不能把什麼一起升級 |",
            "| Sony 堆疊式影像感測器 |",
            "| AMD EPYC 7003 3D V-Cache／TSMC N7 SoIC CoW |",
            "| TSMC N7 SoIC WoW 的 logic＋DTC IPU |",
            "應用 × 接法 × 介面世代／pitch × 具名產品階段",
            "## 先分清兩種「貼法」的良率分母",
            "| 本文兩條接合路徑 | 怎麼接 | 主要優點 | 主要風險 | 為什麼不能直接比較 |",
            "| 單顆晶粒接晶圓（D2W） |", "| 晶圓接晶圓（W2W） |",
            "separated_hybrid_bonding_percent_denominators_and_added_quality_passport_without_thesis_clock_refresh",
            "## 同樣寫 100%，先問分母：量測覆蓋不等於合格產品良率",
            "| 公開寫法 | 分子與分母要怎麼讀 | 這一層能證明什麼 | 還不能證明什麼 |",
            "EVG40 D2W 的 100% die overlay measurement",
            "imec／EVG 200 奈米試驗的所有 die 都低於 40 奈米 overlay",
            "EVG 開發中心示範的 100% void-free bonding yield",
            "imec 2 微米試驗的 Kelvin 大於 85%、菊鏈大於 70%",
            "### 六欄混合接合品質護照",
            "| 品質護照欄位 | 最少要記什麼 | 缺少時最容易誤判什麼 |",
            "| 1. 受測物與分母 |", "| 2. 製程身分 |",
            "| 3. 對準量測 |", "| 4. 介面完整性 |",
            "| 5. 電性與可靠度 |", "| 6. 產品與量產經濟 |",
            "added_pitch_squared_density_overlay_ratio_and_scaling_tradeoff_passport_without_thesis_clock_refresh",
            "## Pitch 砍半，不等於密度、overlay 裕量與良率一起變好",
            "| 公開試驗語境 | 接法 | Pitch | 假想方形網格站點密度指數 | 這一欄不能代表什麼 |",
            "| imec 2µm 試驗載具 | D2W | 2,000nm | 1.000 |",
            "| TEL 140nm 試驗載具 | W2W | 140nm | 204.082 |",
            "204.082 只來自（2,000÷140）²",
            "### Overlay 除以 pitch，先看分子的角色",
            "| 公開語境 | 分子是什麼 | Pitch | 算術 bound÷pitch | 為什麼不能直接排名 |",
            "| TEL 140nm W2W | 含 bond-pad layout 的 hybrid-bond residual <50nm | 140nm | <35.714% |",
            "| TEL fusion diagnostic | 三片 wafer 中 99.5% points residual <40nm | 140nm test context | <28.571% |",
            "初始電阻與 spread 上升、bonding yield 下降",
            "N＝4 個跨來源 pitch 幾何案例與 N＝5 個公開 bound",
            "物理樣本是 N＝3 片 wafer",
            "Python Fraction 與獨立 awk 在顯示精度內完全一致",
            "不計\nsampling SE／t",
            "### 多空小作文共用的互連縮放十欄護照",
            "| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |",
            "| 1. 應用與產品 |", "| 2. 接法與網格 |",
            "| 3. Pitch 與 pad |", "| 4. Overlay 定義 |",
            "| 5. 誤差來源 |", "| 6. 表面與介面 |",
            "| 7. 電性分布 |", "| 8. 可靠度 |",
            "| 9. 樣本與製造 |", "| 10. 產品與商業 |",
            "**較強的多方版本**", "**較強的空方版本**",
            "## 再看五個量產窗口如何接力",
            "| 本文五個量產窗口 | 先回答什麼 | 主要接力角色 | 失敗會怎樣 | 本輪可確認到哪裡 |",
            "| 1. 設計規則與試驗結構 |", "| 2. 表面平坦與銅高度 |",
            "| 3. 潔淨與顆粒控制 |", "| 4. 對準、接合與量測 |",
            "| 5. 良率、產能與可靠度 |",
            "## 最後用六關分開「已有產品」與「量產經濟可稽核」",
            "| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |",
            "| 1. 開放設計入口 |", "| 2. 試驗結構成功 |",
            "| 3. 整合設備與流程使用 |", "| 4. 具名商用產品 |",
            "| 5. Production 聲明 |", "| 6. 量產經濟與財務歸因 |",
            "source_id: S14", "source_id: S15",
            "claim_id: C8", "correction_kind: supersedes",
            "corrects_claim_id: C4", "claim_id: C14",
            "claim_id: C15", "claim_id: C16", "claim_id: C17",
            "monitor_id: T3", "monitor_id: T4",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 53
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先畫四維地圖：成熟的是哪一格", 1
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
            ("research_topic", 1), ("research_source", 15),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-HYBRID-BONDING-READINESS,"
            "同樣叫混合接合，為什麼舊產品已商用，200 奈米試驗仍不能算量產？",
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
            "product:stacked-cmos-image-sensor,product,堆疊式 CMOS 影像感測器",
            "product:tsmc-soic,product,TSMC-SoIC 三維堆疊平台",
            "product:amd-3d-v-cache,product,AMD 3D V-Cache 處理器",
            "metric:hybrid-bond-overlay-measurement-coverage,metric,混合接合對準量測覆蓋率",
            "metric:hybrid-bond-interface-integrity-yield,metric,混合接合介面完整率",
            "metric:hybrid-bond-test-structure-electrical-yield,metric,混合接合測試結構電性良率",
            "metric:hybrid-bond-final-product-yield,metric,混合接合最終產品合格良率",
            "process:hybrid-bond-interconnect-scaling-passport,process,混合接合互連縮放十欄護照",
            "metric:hybrid-bond-pitch-overlay-density-boundary,metric,混合接合 pitch、overlay 與密度邊界",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 混合接合（Hybrid bonding）", graph)
        for edge_id in (
            "KG-HYB-C03", "KG-HYB-C04", "KG-HYB-C05",
            "KG-HYB-I10", "KG-HYB-I11", "KG-HYB-I12",
            "KG-HYB-I13", "KG-HYB-I14", "KG-HYB-I15", "KG-HYB-I16",
            "KG-HYB-I17", "KG-HYB-I18",
        ):
            self.assertIn(f"edge_id: {edge_id}", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 23)

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
            "separated_fanout_architecture_panel_carrier_and_ase_310x310_planned_production_evidence",
            "三個詞不能混成同一個成熟度",
            "公司同一頁仍寫成預計 2027 年投產",
            "## 先把兩條軸拆開：封裝做法不等於面板載體",
            "| 本文兩軸地圖 | 它回答什麼 | 例子 | 本輪可確認 | 不能直接推成 |",
            "| 1. 封裝架構 |", "| 2. 製程先後 |",
            "| 3. 批次載體 |", "| 4. 商用階段 |",
            "### 再用兩條簡化流程看先後順序",
            "**晶片先放**：", "**線路先做**：", "**改用面板**：",
            "separated_310mm_panel_foup_loadport_and_line_release_interfaces_without_thesis_clock_refresh",
            "## 310×310 不是只改一個尺寸：面板、載具、裝卸口與整線是四層",
            "| 本文四層介面 | 它固定什麼 | 本輪一手證據到哪裡 | 尚不能證明什麼 |",
            "| 1. 面板本體 |", "| 2. Panel FOUP 載具 |",
            "| 3. Load Port 與搬運 |", "| 4. 整線與產品放行 |",
            "### 「正在制定」離「整線量產」還有五個動詞",
            "| 五個動詞 | 真正完成什麼 | 本輪狀態 | 不能跳到哪裡 |",
            "| 1. 啟動活動 |", "| 2. 核准草案 |", "| 3. 發布標準 |",
            "| 4. 採用與互通 |", "| 5. 整線產品放行 |",
            "claim_id: C13", "monitor_id: T4",
            "added_nominal_carrier_geometry_and_good_output_cost_bridge_without_thesis_or_clock_refresh",
            "## 96,100 mm² 不等於多 35.9536891656% 合格品",
            "| 名目幾何步驟 | 重算式 | 結果 | 還沒扣掉什麼 |",
            "| 310×310 mm 方形 |", "| 直徑 300 mm 圓形 |",
            "| 名目面積差 |", "| 名目面積比 |", "| 名目增幅 |",
            "N=1 組名目幾何", "sampling\nSE／t",
            "### 從名目面積走到每顆合格成本，要過五本帳",
            "| 本文五本帳 | 同一比較要固定什麼 | 可重算的分子／分母 | 只看上一帳會錯在哪裡 |",
            "| 1. 載體身分帳 |", "| 2. 可用版圖帳 |",
            "| 3. 最終合格品帳 |", "| 4. 合格產出帳 |",
            "| 5. 合格成本帳 |",
            "### 多空小作文也要共用同一份合格產出護照",
            "| 同一查核層 | 多頭小作文要成立 | 空頭小作文要成立 | 雙方都要交的共同資料 |",
            "| 幾何與版圖 |", "| 製造與品質 |", "| 經濟與商用 |",
            "claim_id: C16",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 52
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先把兩條軸拆開", 1
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
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 16), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS,"
            "面板、扇出與晶片先放是同一件事嗎，為什麼預計投產仍不能當成穩定量產？",
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
            "concept:fan-out-packaging,concept,扇出封裝（Fan-out）",
            "process:chip-first-fan-out,process,晶片先放扇出流程（Chip-first）",
            "process:chip-last-fan-out,process,線路先做扇出流程（Chip-last）",
            "component:reconstituted-panel,component,重構面板（Reconstituted panel）",
            "standard:semi-3d20-panel-characteristics,standard,SEMI 3D20 面板物理特性",
            "component:panel-foup,component,面板 FOUP 載具",
            "component:panel-foup-load-port,component,面板 FOUP 裝卸埠",
            "stage:310mm-panel-interface-standardization,stage,310mm 面板介面標準制定",
            "process:panel-good-output-cost-passport,process,面板合格產出與成本護照",
            "metric:gross-carrier-area-to-good-package-contract,metric,名目載體面積到合格品契約",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 面板級封裝（PLP）", graph)
        self.assertIn("edge_id: KG-PLP-C04", graph)
        self.assertIn("from_id: company:3711", graph)
        for edge_id in (
            "KG-PLP-I11", "KG-PLP-I12", "KG-PLP-I13",
            "KG-PLP-I14", "KG-PLP-I15", "KG-PLP-I16",
            "KG-PLP-I17", "KG-PLP-I18", "KG-PLP-I19",
            "KG-PLP-I20", "KG-PLP-I21",
        ):
            self.assertIn(f"edge_id: {edge_id}", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 25)

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
            "added_workload_concurrency_tail_latency_and_unit_performance_passport_without_thesis_or_clock_refresh",
            "## 1M IOPS 不等於固定 GB/s：先建立效能護照",
            "| Headline 指標 | 分子／分母 | 最少要綁定的條件 | 它不能單獨證明 |",
            "| IOPS |", "| Throughput |", "| Latency／tail |",
            "### 同一個 IOPS 數字換 block size，排名就可能反轉",
            "3.814697265625 GiB/s", "12.20703125 GiB/s", "B／A=`3.2`",
            "N=2 個假想 workload",
            "### Queue depth 能推高併行，也會換掉延遲問題",
            "| TC1／QD1 baseline latency |", "| QD／TC sweep |",
            "| AI end-to-end tail |",
            "### 十欄 AI 儲存效能護照",
            "| 1. 工作與量測範圍 |", "| 5. 併行與 demand |",
            "| 8. 延遲分布與事件數 |", "| 10. 使用者結果與分母 |",
            "### 多空小作文要共享同一份 workload",
            "| 偏多：AI 讓高階儲存內容與驗證增加 |",
            "| 偏空：軟體與資料位置吸收硬體增量 |",
            "expanded_checkpoint_completion_recovery_and_training_goodput_measurement_contract",
            "## 「存檔完成」其實有六層，不是按下 save 就結束",
            "| 完成階梯 | 真正完成了什麼 | 最小證據 | 仍不能證明 |",
            "| 1. I/O 模擬跑完 |", "| 2. 暫存完成 |",
            "| 3. 上傳完成 |", "| 4. 耐久副本完成 |",
            "| 5. 正確回載完成 |", "| 6. 訓練結果改善 |",
            "## 用八格復原護照檢查 checkpoint 是否真的讓訓練更有效",
            "| 八格復原護照 | 要先固定什麼 | 要保存什麼 | 少了最容易誤讀成 |",
            "| 1. 受測系統與版本 |", "| 2. Checkpoint 內容與節奏 |",
            "| 3. 比較組與訓練負載 |", "| 4. 完成語意與 barrier |",
            "| 5. 資料路徑與故障範圍 |", "| 6. 故障與正確回載 |",
            "| 7. 訓練使用者結果 |", "| 8. 資源、可靠度與經濟 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 67
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
            ("research_topic", 1), ("research_source", 23),
            ("research_claim", 22), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 4),
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
            "process:checkpoint-recovery-measurement-passport,process,Checkpoint 八格復原護照",
            "metric:checkpoint-completion-semantics,metric,Checkpoint 完成語意",
            "metric:training-runtime-goodput,metric,訓練有效時間",
            "process:ai-storage-performance-passport,process,AI 儲存十欄效能護照",
            "metric:workload-conditioned-tail-latency,metric,工作負載條件化尾端延遲",
            "process:ai-storage-endurance-passport,process,AI 儲存十二欄耐久護照",
            "metric:application-host-nand-write-ledgers,metric,應用、主機與 NAND 三層寫入帳",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AI 資料讀取與儲存路徑", graph)
        for edge_id in (
            "KG-ASD-C04", "KG-ASD-I11", "KG-ASD-I12", "KG-ASD-I13",
            "KG-ASD-I14", "KG-ASD-I15", "KG-ASD-I16", "KG-ASD-I17",
        ):
            self.assertIn(f"edge_id: {edge_id}", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 21)

    def test_ai_storage_endurance_separates_application_host_nand_and_rated_life(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-09_ai_storage_data_plane.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "separated_application_host_nand_and_rated_endurance_ledgers_without_thesis_or_clock_refresh",
            "## GB/s 跑得快，不等於耐久夠：先拆四本寫入帳",
            "| A：應用邏輯資料 |",
            "| H：主機寫入 |",
            "| N：NAND 寫入 |",
            "| L：額定壽命 |",
            "N／A＝H／A×N／H",
            "### DWPD 是壽命分母，不是速度分母",
            "| D7-PS1010 Standard Endurance | 15.36 TB | 1.0 | 15.36 TB／日 | 28.032 PBW | 28 PBW |",
            "| D7-PS1030 Mid-Endurance | 12.8 TB | 3.0 | 38.4 TB／日 | 70.080 PBW | 70 PBW |",
            "可用容量比 PS1010 少 16.6667%",
            "額定每日寫入與\n五年累計寫入都是 2.5 倍",
            "Python Decimal 與獨立 awk",
            "N＝1 個發行人、N＝1 個產品家族、N＝2 個規格組態",
            "沒有 sampling SE／t",
            "### Percentage Used 到 100%，也不是「現在立刻壞掉」",
            "50／50 read／write、4 KiB read、128 KiB write",
            "100% active range、\n80% full、不可壓縮資料與 35°C 環境",
            "### 十二欄耐久度護照：先能對帳，再談買多少",
            "| 1. AI 工作與完成語意 |",
            "| 4. Host writes H |",
            "| 5. NAND writes N 與 WAF |",
            "| 10. 健康與事件 |",
            "| 12. 商業與財務 |",
            "### 多空小作文共用同一張耐久帳",
            "| 偏多：AI 把儲存價值推向高耐久與管理能力 |",
            "| 偏空：軟體把寫入與磨耗增量吸收 |",
            "本輪新增 N＝4 份一手文件／頁面",
            "claim_id: C18\nlabel: verified",
            "claim_id: C19\nlabel: verified",
            "claim_id: C20\nlabel: inference",
            "claim_id: C21\nlabel: verified",
            "claim_id: C22\nlabel: inference",
            "source_id: S20",
            "a06ca25dfb59c59221682937090fb709563622455ebc76640e3aa69e498419ed",
            "source_id: S21",
            "ebda7161ea19a616c1386d6bca94fcf0c153d1b563e5f32d7b97ba62392e2a4b",
            "source_id: S22",
            "直接 curl 回 HTTP 403",
            "source_id: S23",
            "monitor_id: T4\nstatus: active",
        ):
            self.assertIn(contract, topic)
        scans = (
            ROOT / "notes" / "research_topics" / "scan_log.csv"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "scan-2026-08-14-ai-storage-endurance-ledgers", scans
        )
        snapshot = json.loads((
            ROOT / "notes" / "research_method_reviews"
            / "2026-08-14_61.json"
        ).read_text(encoding="utf-8"))
        self.assertEqual(snapshot["snapshotId"], "RMA-2026-08-14-61")
        self.assertEqual(snapshot["claims"]["active"], 682)
        self.assertEqual(snapshot["sources"]["active"], 618)
        self.assertEqual(snapshot["monitors"]["active"], 127)
        self.assertEqual(snapshot["graphs"]["activeEdges"], 812)

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
            "corrected_production_reading_with_reference_design_and_integrated_rack_contract",
            "added_configuration_passport_change_triggered_regression_and_company_stage_refinement_no_thesis_change",
            "added_orw_base_versus_meta_mechanical_qualification_passport_no_thesis_change",
            "一整櫃還要讓運算、兩類網路、供電、液冷、控制軟體與維修共同通過",
            "定義不同，不能相加或互相比較",
            "## 先看一整櫃有哪些共同責任",
            "| 本文八條責任線 | 它負責什麼 | 本輪可確認的 Helios 設計 | 整櫃要驗收什麼 | 不能直接推成 |",
            "| 1. 機架與共同介面 |", "| 2. 運算托盤 |",
            "| 3. 機架內交換 |", "| 4. 跨機架與前端網路 |",
            "| 5. 集中供電 |", "| 6. 液冷迴路 |",
            "| 7. 控制與軟體 |", "| 8. 可維修與營運 |",
            "## 相容不等於可搬、可落地：六張機械資格護照",
            "| 六張機械資格護照 | 受測物／狀態 | 本輪規範能確認 | 品牌系統仍要交付 | 不能跨帳推成 |",
            "| 1. 共同介面 |", "| 2. 結構載重 |",
            "| 3. 移動穩定 |", "| 4. 靜態穩定 |",
            "| 5. 裝箱運輸 |", "| 6. 場站交接 |",
            "4,700 × 9.80665 = 46,091.255 N ≈ 46.1 kN",
            "250 ÷ 9.80665 = 25.4929 kgf ≈ 25.5 kgf",
            "Python `Decimal` 與 `awk` 兩條獨立路徑",
            "這是 `N=1` 份 Meta 實作規範的確定性單位換算",
            "### 多空小作文要共用同一份機械資料包",
            "官方站點本輪拒絕直接 PDF 下載與視覺截圖",
            "## 再分清參考設計、品牌系統與客戶機群",
            "不是 AMD 直接出售的產品",
            "| 本文五種交付物 | 誰要交付 | 必須固定什麼 | 本輪證據 | 不能直接推成 |",
            "| 1. 開放標準與參考設計 |", "| 2. 整機廠品牌系統 |",
            "| 3. 整櫃資格與驗收資料包 |", "| 4. 出貨與現場接收 |",
            "| 5. 生產機群與財務 |",
            "## 同一型號還要有一張配置身分證",
            "| 本文六個配置欄位 | 要留下什麼 | 它防止哪種誤讀 | 變更後先問什麼 |",
            "| 1. 工廠硬體與盤點 |", "| 2. 韌體、軟體與 SBOM |",
            "| 3. 網路、拓撲與設定 |", "| 4. 電力、冷卻與場站輸入 |",
            "| 5. 工作負載、條件與基準 |", "| 6. 簽核、交接與變更紀錄 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 68
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先看一整櫃有哪些共同責任", 1
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
            ("research_topic", 1), ("research_source", 24),
            ("research_claim", 26), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 12),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        for ledger_contract in (
            "source_id: S12", "source_id: S21", "source_id: S24",
            "claim_id: C10", "claim_id: C21", "claim_id: C26",
            "claim_id: C1\nlabel: inference\nstatus: superseded",
            "corrected_by_claim_id: C11", "correction_kind: supersedes",
            "corrects_claim_id: C1", "monitor_id: T6", "monitor_id: T12",
        ):
            self.assertIn(ledger_contract, topic)
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
            "standard:open-rack-wide,standard,開放式寬機架（Open Rack Wide）",
            "component:ai-compute-tray,component,人工智慧運算托盤",
            "component:ai-scale-up-switch-tray,component,人工智慧機架內交換托盤",
            "component:rack-power-shelf,component,機架電力架與匯流排",
            "capability:rack-serviceability,capability,機架可維修性",
            "capability:rack-lifecycle-control,capability,機架生命週期控制",
            "capability:rack-configuration-baseline,capability,機櫃配置基準",
            "process:rack-change-triggered-regression,process,機櫃變更觸發回歸測試",
            "concept:rack-mechanical-qualification-passport,concept,機架機械資格護照",
            "metric:rack-mass-force-support-reaction,metric,機架質量—重力—支承反力邊界",
            "stage:oem-systemization,stage,整機廠品牌系統化",
            "stage:integrated-rack-qualification,stage,整櫃整合資格驗證",
            "component:efb,component,高架扇出橋接（EFB）",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AMD Helios 部署階梯", graph)
        for edge in (
            "edge_id: KG-HEL-I13", "edge_id: KG-HEL-I14",
            "edge_id: KG-HEL-I15", "edge_id: KG-HEL-I16",
            "edge_id: KG-HEL-I17", "edge_id: KG-HEL-I18",
            "edge_id: KG-HEL-I19", "edge_id: KG-HEL-I20",
            "edge_id: KG-HEL-I21", "edge_id: KG-HEL-I22",
            "edge_id: KG-HEL-I23", "edge_id: KG-HEL-I24",
            "edge_id: KG-HEL-I25", "edge_id: KG-HEL-I26",
            "edge_id: KG-HEL-I27",
        ):
            self.assertIn(edge, graph)
        self.assertIn(
            "edge_id: KG-HEL-I01\nview: industry\nfrom_id: product:amd-helios\n"
            "to_id: concept:rack-scale",
            graph,
        )
        self.assertEqual(graph.count("<!-- knowledge_edge"), 41)

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
            "superseded_single_manufacturing_clock_after_design_process_control_reliability_and_roadmap_evidence",
            "added_conditioned_measurement_passport_for_static_dynamic_and_ppa_claims",
            "這種做法把供電網路移到晶圓背面",
            "看到某道製程變重要只代表值得研究",
            "## 先用五個時鐘判斷成熟度",
            "| 本文五個時鐘 | 核心問題 | 可以升級的證據 | 本輪位置 | 仍然缺什麼 |",
            "| 1. 設計與電力完整性 |", "| 2. 背面製程成形 |",
            "| 3. 製程控制與可靠度 |", "| 4. 晶圓節點與客戶產品 |",
            "| 5. 供應商資格與財務轉換 |",
            "## 看到百分比，先填八格比較護照",
            "| 八格比較護照 | 要記下什麼 | 少了會讀錯什麼 |",
            "| 1. 受測物與成熟度 |", "| 3. 固定條件 |",
            "| 5. 工作負載與活動 |", "| 7. PDN 與環境邊界 |",
            "### 四組官方數字，應該怎麼讀",
            "### 靜態 IR drop 和動態下陷，差在時間",
            "added_voltage_current_resistance_loss_and_hotspot_passport_without_thesis_clock_refresh",
            "## 同樣少掉 30mV，不同 Vdd 不是同一個風險",
            "| 假想負載端工作電壓 | 相同絕對壓降 | 壓降÷工作電壓 | 這一列還沒回答什麼 |",
            "| 0.75V | 30mV | 4.000% |",
            "| 0.50V | 30mV | 6.000% |",
            "### 再固定負載功率與路徑，電流才會浮出來",
            "| 假想負載端電壓 | 負載端功率 | 等效總電流 | 路徑壓降 | 壓降占負載端電壓 | 路徑焦耳損耗 | 假想來源端電壓 |",
            "| 0.75V | 100W | 133.333A | 26.667mV | 3.556% | 3.556W | 0.776667V |",
            "| 0.50V | 100W | 200.000A | 40.000mV | 8.000% | 8.000W | 0.540000V |",
            "總電流與絕對壓降都變成 1.5 倍",
            "I²R 損耗則\n變成 2.25 倍",
            "N＝2 個固定 30mV 的電壓分母案例，另有 N＝2 個固定負載功率／等效電阻案例",
            "Python Fraction 與獨立 awk 在顯示精度內完全一致",
            "沒有 sampling SE／t",
            "### 平均電流過關，局部熱點仍可能失敗",
            "單一電阻，可能漏掉接點附近的 hotspot",
            "預測的 maximum hotspot temperature 會實質不同",
            "| 要分開的帳 | 最少要保存什麼 | 只看平均值會漏掉什麼 |",
            "| 負載與總電流 |", "| 分流與導體 |",
            "| 局部電流密度 |", "| 電損地圖 |", "| 熱路徑與熱點 |",
            "### 多空小作文共用的電力—熱十欄護照",
            "| 護照欄位 | 必須固定什麼 | 少了最容易誤讀成什麼 |",
            "| 1. 產品與 rail |", "| 2. 工作點 |", "| 3. 功率分子 |",
            "| 4. 電流分母 |", "| 5. 路徑模型 |", "| 6. 導體身分 |",
            "| 7. 電流密度 |", "| 8. 壓降與電損 |", "| 9. 熱與可靠度 |",
            "| 10. 量產與商業 |", "**較強的多方版本**", "**較強的空方版本**",
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
            "## 看懂一個失敗怎麼沿鏈條放大",
            "布局與幾何 → 微影／蝕刻形貌 → 對準與接觸面積 → 接點電阻 → "
            "供電穩定性 → 電路速度、良率與可靠度",
            "## 把晶圓廠、製程控制與供應商時鐘分開",
            "## 最後用七關把製程需要接回公司",
            "| 本文七關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 架構問題成立 |", "| 2. 設計與試驗晶片可行 |",
            "| 3. 完整流程與接點導通成立 |", "| 4. 製程窗口與可靠度通過 |",
            "| 5. 具名節點與客戶產品量產 |", "| 6. 供應商資格與重複出貨 |",
            "| 7. 財務結果可以歸因 |",
            "claim_id: C6", "claim_id: C17", "source_id: S6",
            "source_id: S10", "source_id: S13", "source_id: S17",
            "source_id: S18", "source_id: S19", "source_id: S20",
            "claim_id: C18", "claim_id: C19", "claim_id: C20", "claim_id: C21",
            "monitor_id: T4", "monitor_id: T5", "PROVision 10",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 68
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個時鐘判斷成熟度", 1
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
            ("research_topic", 1), ("research_source", 20),
            ("research_claim", 21), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 5),
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
            "capability:backside-dtco,capability,背面供電設計技術共同最佳化",
            "metric:ntsv-bpr-contact-resistance,metric,nTSV 至 BPR 接點電阻",
            "capability:backside-overlay-metrology,capability,背面疊對與形貌量測",
            "capability:backside-stress-control,capability,背面機械應力控制",
            "stage:backside-design-validation,stage,背面供電設計驗證",
            "stage:backside-process-control,stage,背面製程控制與可靠度",
            "stage:backside-node-production,stage,背面供電節點與產品量產",
            "stage:backside-supplier-qualification,stage,背面供電供應商資格與出貨",
            "stage:backside-financial-attribution,stage,背面供電財務歸因",
            "concept:backside-performance-comparison-passport,concept,背面供電效能八格比較護照",
            "metric:static-ir-drop,metric,靜態電壓降",
            "metric:dynamic-voltage-droop,metric,動態電壓下陷",
            "metric:conditional-ppa-comparison,metric,條件式效能功耗面積比較",
            "process:backside-electrothermal-passport,process,背面供電電力—熱十欄護照",
            "metric:rail-current-drop-loss-hotspot-boundary,metric,電壓、電流、壓降、損耗與熱點邊界",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 背面供電路徑與製程接力", graph)
        for edge in (
            "edge_id: KG-BSP-C03", "from_id: company:lam-research",
            "edge_id: KG-BSP-C04", "from_id: company:applied-materials",
            "edge_id: KG-BSP-I11", "to_id: metric:ntsv-bpr-contact-resistance",
            "edge_id: KG-BSP-I14", "to_id: stage:backside-design-validation",
            "edge_id: KG-BSP-I15", "to_id: stage:backside-process-control",
            "edge_id: KG-BSP-I16", "to_id: stage:backside-node-production",
            "edge_id: KG-BSP-I17", "to_id: stage:backside-supplier-qualification",
            "edge_id: KG-BSP-I18", "to_id: stage:backside-financial-attribution",
            "edge_id: KG-BSP-I19", "to_id: concept:backside-performance-comparison-passport",
            "edge_id: KG-BSP-I20", "to_id: metric:static-ir-drop",
            "edge_id: KG-BSP-I21", "to_id: metric:dynamic-voltage-droop",
            "edge_id: KG-BSP-I22", "to_id: metric:conditional-ppa-comparison",
            "edge_id: KG-BSP-I23", "to_id: process:backside-electrothermal-passport",
            "edge_id: KG-BSP-I24", "to_id: metric:rail-current-drop-loss-hotspot-boundary",
        ):
            self.assertIn(edge, graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 28)

    def test_compute_connect_station_four_separates_three_axis_optics_and_evidence_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_cpo_pluggable_coexistence.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 資料先是電、再變成光："
            "別只問 CPO 或可插拔，要拆光引擎、訊號處理與雷射位置\n"
        ))
        for contract in (
            "editorial_plain_language_wave99_cpo_five_positions_five_tradeoffs_roles_and_six_gate_ladder",
            "corrected_binary_optics_frame_with_engine_signal_and_laser_axes",
            "資料先以電訊號進入交換晶片，再轉成光訊號",
            "三個答案可以重新組合，不能濃縮成「CPO 對可插拔」",
            "## 先用五個位置看資料怎麼從電變成光",
            "| 本文五個位置 | 資料現在是什麼 | 這裡負責什麼 | 主要接力角色 | 不能直接推成 |",
            "| 1. 交換晶片內部 |", "| 2. 晶片到轉換器的高速電路 |",
            "| 3. 電光轉換位置 |", "| 4. 雷射與光纖耦合 |",
            "| 5. 光纖與下一台設備 |",
            "## 不要把架構畫成一條線：先拆三個獨立決策軸",
            "| 1. 光引擎位置 |", "| 2. 電介面訊號處理 |",
            "| 3. 雷射位置 |", "CPO 光引擎 + 外部 ELSFP 雷射",
            "## 雷射移到外部後，維修邊界與損耗一起改變",
            "| 故障替換 |", "| 光學損耗 |", "| 控制與安全 |",
            "## 再用五把尺比較三種光引擎位置",
            "| 本文五把尺 | 前面板可插拔 | 板上／NPO | CPO | 共同要量的結果 |",
            "| 1. 高速電路與功耗 |", "| 2. 空間與頻寬密度 |",
            "| 3. 維修與故障範圍 |", "| 4. 升級與第二來源 |",
            "| 5. 製造與生命週期成本 |",
            "## 四份 OIF 資料各回答不同問題",
            "Co-Packaging Framework（2022）", "ELSFP IA 02.0（2025）",
            "framework 建語彙 → IA 固定介面",
            "## 把五類角色放回同一條光電接力",
            "| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |",
            "| 1. 平台與交換器產品 |", "| 2. 訊號處理與光引擎 |",
            "| 3. 雷射與光源 |", "| 4. 封裝、組裝與測試 |",
            "| 5. 客戶部署與營運 |",
            "## 產品時鐘不是一條「誰取代誰」的時鐘",
            "## 最後用七關分開標準、產品、部署與公司受惠",
            "| 本文七關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 三軸組態可辨識 |", "| 2. 標準與應用契約閉合 |",
            "| 3. 產品進入持續生產 |", "| 4. 供應商角色能雙向核對 |",
            "| 5. 互通、客戶驗收與部署分母出現 |",
            "| 6. 供應商出貨、份額與價格可辨識 |",
            "| 7. 收入、毛利與現金流留下來 |",
            "## 「100 萬小時零 flap」不是零失效率：先拆暴露、事件與模型",
            "### 第一步：先問 100 萬究竟由什麼組成",
            "| 可靠度護照欄位 | 新聞稿直接給什麼 | 還缺什麼 | 少了會怎麼誤讀 |",
            "### 第二步：零次事件只能做有條件的單側界線",
            "MTBF_lower = T / (-ln α)",
            "MTBF_lower ≈ 333,808 port-device-hours",
            "等價失效率上限 ≈ 2.996 × 10^-6 / port-device-hour",
            "### 第三步：把工程結果接回多空共同裁決",
            "**多方小作文可以寫到哪裡：**",
            "**空方小作文可以寫到哪裡：**",
            "本節有 `N=2` 條消息鏈",
            "added_two_sided_worst_case_optical_power_budget_without_thesis_or_clock_refresh",
            "## 同樣速率與元件，為什麼一條光路通過、另一條失敗",
            "### 先畫兩道門：不能太暗，也不能太亮",
            "| 共同假設 | 教材固定值 | 這一欄回答什麼 |",
            "P_rx,low  = P_tx,min − L_max",
            "pass      = M_low ≥ 0 且 M_high ≥ 0",
            "| A | `2.5／4.5 dB` |", "+1.5 dB", "+0.5 dB",
            "| B | `4.5／6.5 dB` |", "−0.5 dB", "+2.5 dB",
            "### 多空小作文要共用十欄光功率護照",
            "| 十欄光功率護照 | 至少保存什麼 | 少了最容易被誤寫成 |",
            "Python `Decimal` 與獨立 `awk` 浮點路徑",
            "source_id: S14", "claim_id: C14", "claim_id: C15",
            "source_id: S12", "source_id: S13",
            "claim_id: C11", "claim_id: C12", "claim_id: C13",
            "claim_id: C9", "correction_kind: supersedes",
            "corrects_claim_id: C2", "monitor_id: T3",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 64
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先用五個位置看", 1
        )[0]
        for jargon in (
            "Spectrum-X", "Photonics", "Spectrum-6", "Ara", "SPIL",
            "Lumentum", "Marvell", "NVIDIA", "TSMC", "TFC", "Foxconn",
        ):
            self.assertNotIn(jargon, lead)
            self.assertNotIn(jargon, reflection)
        for block, expected in (
            ("research_topic", 1), ("research_source", 14),
            ("research_claim", 15), ("metric_comparison", 0),
            ("impact", 1), ("monitoring_item", 3),
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
            "concept:cpo-three-axis-architecture,concept,CPO 三軸組態框架",
            "component:npo-optical-engine,component,近封裝光引擎（NPO）",
            "concept:optical-interface-processing-mode,concept,光學電介面訊號處理模式",
            "component:external-laser-source,component,外部雷射光源（ELS）",
            "metric:optical-loss-budget,metric,光學損耗預算",
            "stage:optics-multivendor-field-validation,stage,光學多供應商與現場驗證",
            "process:cpo-reliability-exposure-passport,process,CPO 可靠度暴露護照",
            "metric:zero-event-reliability-bound,metric,零事件可靠度單側界線",
            "process:cpo-optical-power-budget-passport,process,CPO 光功率預算十欄護照",
            "metric:worst-case-optical-power-margin,metric,最差條件光功率兩端裕量",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AI 光學三軸組態與產品證據", graph)
        for edge in (
            "edge_id: KG-CPO-I06", "to_id: concept:cpo-three-axis-architecture",
            "edge_id: KG-CPO-I07", "to_id: component:npo-optical-engine",
            "edge_id: KG-CPO-I08", "to_id: concept:optical-interface-processing-mode",
            "edge_id: KG-CPO-I09", "to_id: component:external-laser-source",
            "edge_id: KG-CPO-I10", "to_id: metric:optical-loss-budget",
            "edge_id: KG-CPO-I11", "to_id: stage:optics-multivendor-field-validation",
            "edge_id: KG-CPO-I12", "to_id: process:cpo-reliability-exposure-passport",
            "edge_id: KG-CPO-I13", "to_id: metric:zero-event-reliability-bound",
            "edge_id: KG-CPO-I14", "to_id: process:cpo-optical-power-budget-passport",
            "edge_id: KG-CPO-I15", "to_id: metric:worst-case-optical-power-margin",
        ):
            self.assertIn(edge, graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 18)

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
            "added_anamorphic_field_stitching_dose_yield_and_electrical_evidence_ladder_without_hvm_upgrade",
            "added_na_resolution_depth_of_focus_and_half_field_passport_without_thesis_clock_refresh",
            "## 解析度變好，為什麼反而多出五個新難題",
            "| 本文五個新難題 | 變化從哪裡來 | 本輪一手證據走到哪裡 | 下一個要驗收 | 不能直接推成 |",
            "| 1. 半視場與接縫 |", "| 2. 焦深、薄膜與表面起伏 |",
            "| 3. 劑量、速度與隨機缺陷 |",
            "| 4. 光罩、修正、光阻與烘烤 |",
            "| 5. 圖形轉移與電性 |",
            "## 0.55 比 0.33 大，為什麼景深反而只剩約三分之一",
            "CD ＝ k1 × 波長 ÷ NA",
            "| A：較低 NA | 13.5nm | 0.32 | 0.33 | 13.0909nm |",
            "| B：較高 NA | 13.5nm | 0.32 | 0.55 | 7.8545nm |",
            "| 焦深帳 | 受邀摘要報告 0.55 NA 計算值 45nm、約為 0.33 NA 的三分之一 |",
            "### 多空小作文共用一份十欄光學—製程護照",
            "| 5. 焦距預算 |", "| 8. 設備生產 |",
            "| 10. 商業與變更沿革 |",
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
            "## 再用六級證據分清印得出來與產品能量產",
            "| 本文六級圖形證據 | 這一級回答什麼 | 本輪可確認 | 還缺什麼 | 不能替代 |",
            "| 1. 光學或材料單項結果 |", "| 2. 顯影後光阻圖形 |",
            "| 3. 蝕刻或金屬化測試結構 |", "| 4. 電性測試載具 |",
            "| 5. 功能性整合元件 |", "| 6. 客戶產品層與高量產 |",
            "## 一份可重驗的製程視窗紀錄至少有十欄",
            "| 本文十欄製程視窗紀錄 | 至少要記什麼 | 為什麼不能省略 |",
            "| 1. 受測物與版本 |", "| 2. 光罩、視場與拼接 |",
            "| 3. 光阻與底層 |", "| 4. 曝光設定 |",
            "| 5. 烘烤、顯影與環境 |", "| 6. 膜堆與表面地形 |",
            "| 7. 圖形轉移與金屬化 |", "| 8. 量測與電性判定 |",
            "| 9. 樣本、失效與良率分母 |", "| 10. 生產與變更沿革 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 48
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
            ("research_topic", 1), ("research_source", 15),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 3),
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
            "concept:high-na-anamorphic-half-field,concept,High-NA 非等向光學與半視場",
            "process:high-na-field-stitching,process,High-NA 半視場接縫拼接",
            "metric:high-na-dose-yield-throughput-window,metric,High-NA 劑量缺陷良率產出視窗",
            "process:high-na-electrical-evidence-ladder,process,High-NA 圖形到電性量產證據階梯",
            "process:high-na-optical-process-window-passport,process,High-NA 光學與製程視窗十欄護照",
            "metric:resolution-depth-of-focus-field-boundary,metric,解析度焦深與曝光視場邊界",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: 晶圓圖形曝光與 High-NA 導入階梯", graph)
        for edge in (
            "edge_id: KG-HNA-I12", "to_id: concept:high-na-anamorphic-half-field",
            "edge_id: KG-HNA-I13", "to_id: process:high-na-field-stitching",
            "edge_id: KG-HNA-I14", "to_id: metric:high-na-dose-yield-throughput-window",
            "edge_id: KG-HNA-I15", "to_id: process:high-na-electrical-evidence-ladder",
            "edge_id: KG-HNA-I16", "to_id: process:high-na-optical-process-window-passport",
            "edge_id: KG-HNA-I17", "to_id: metric:resolution-depth-of-focus-field-boundary",
        ):
            self.assertIn(edge, graph)

    def test_compute_connect_station_six_separates_data_path_scopes_roles_and_interoperability_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_open_ai_fabrics.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 資料從一顆運算晶片走到另一顆："
            "先分清六張網，再判斷跨廠互通\n"
        ))
        for contract in (
            "editorial_plain_language_wave101_data_path_two_network_scopes_roles_and_six_gate_interoperability",
            "corrected_single_fabric_path_frame_with_network_plane_and_stack_contract",
            "added_collective_algorithm_bus_bandwidth_and_training_outcome_performance_passport_without_thesis_or_clock_refresh",
            "一座人工智慧叢集同時有運算同步、跨機架傳送、一般服務、"
            "儲存與維修管理等不同工作",
            "## 先把一座人工智慧叢集拆成六張網",
            "| 本文六張網 | 它搬什麼／做什麼 | OCP 參考架構如何分 | 失效時先看到什麼 | 不能直接推成 |",
            "| 1. 加速器機架內擴充 |", "| 2. 跨機架／後端擴充 |",
            "| 3. 一般服務／處理器網路 |", "| 4. 儲存網路 |",
            "| 5. 帶內管理網路 |", "| 6. 帶外管理網路 |",
            "## 再把每張網拆成八層驗收契約",
            "| 本文八層契約 | 要回答的問題 | 本輪一手文件走到哪裡 | 升級所需證據 | 不能直接推成 |",
            "| 1. 實體與連結 |", "| 2. 端點、記憶體與傳輸 |",
            "| 3. 交換、路由與壅塞 |", "| 4. 軟體與控制 |",
            "| 5. 管理、遙測與除錯 |", "| 6. 單件合規與自我聲明 |",
            "| 7. 多供應商互通 |", "| 8. 系統、部署與財務 |",
            "## 400G、algbw、busbw 與訓練時間不是同一個數字",
            "| 效能數字 | 它真正量什麼 | 最少要綁定 | 它不能單獨證明 |",
            "| Port／lane line rate |", "| Payload goodput |",
            "| Algorithm bandwidth（algbw） |", "| Bus bandwidth（busbw） |",
            "### Collective 名稱先固定，頻寬係數才有意義",
            "| Collective | 每個 rank 最後拿到什麼 | NCCL tests 的 busbw／algbw 係數 | 不能誤讀成 |",
            "| AllReduce |", "| ReduceScatter |", "| AllGather |", "| AlltoAll |",
            "### 同一個 20 ms，可以同時產生兩個不同頻寬欄位",
            "`50 GB/s`", "`1.75`", "`87.5 GB/s`",
            "N=1 個假想", "### 十欄 AI collective 效能護照",
            "| 1. 網路工作與量測範圍 |", "| 8. 指標、時間與正確性 |",
            "| 10. 使用者與商業結果 |",
            "### 多空小作文要共享同一個 step",
            "| 偏多：更大 AI 叢集提高網路內容與驗證 |",
            "| 偏空：軟體與拓撲吸收部分硬體增量 |",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 59
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先把一座人工智慧叢集拆成六張網", 1
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
            ("research_topic", 1), ("research_source", 24),
            ("research_claim", 23), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        for ledger_contract in (
            "source_id: S15", "source_id: S20", "source_id: S24",
            "claim_id: C14", "claim_id: C19", "claim_id: C23",
            "monitor_id: T4", "monitor_id: T5",
            "claim_id: C9\nlabel: inference\nstatus: superseded",
            "claim_id: C18\nlabel: inference\nstatus: active",
            "correction_kind: supersedes\ncorrects_claim_id: C9",
        ):
            self.assertIn(ledger_contract, topic)
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
            "concept:ai-network-plane-map,concept,AI 叢集網路平面圖",
            "concept:ai-front-end-network,concept,AI 前端與服務網路",
            "concept:ai-storage-network,concept,AI 儲存網路",
            "concept:ai-in-band-management-network,concept,AI 帶內管理網路",
            "concept:ai-out-of-band-management-network,concept,AI 帶外管理網路",
            "concept:ai-fabric-stack-contract,concept,AI 網路分層驗收契約",
            "stage:compliance-self-attestation,stage,合規自我聲明",
            "stage:system-stress-validation,stage,系統壓力與規模驗收",
            "capability:fabric-lifecycle-management,capability,網路生命週期管理",
            "process:ai-collective-performance-passport,process,AI 集體通訊十欄效能護照",
            "metric:collective-algorithm-bus-bandwidth-contract,metric,集體通訊演算法與匯流排頻寬契約",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: AI 資料路徑與跨廠互通", graph)
        for edge_id in range(15, 28):
            self.assertIn(f"edge_id: KG-FAB-I{edge_id}", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 32)

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
            "expanded_single_compliance_ladder_into_link_correctness_and_commercialization_axes",
            "added_test_object_boundary_post_workshop_listing_snapshot_and_listing_lag_contract",
            "zero_observed_error_exposure_counter_layers_and_conditional_upper_bound_added_without_thesis_or_clock_refresh",
            "一條完整高速連線，要讓主機、板路與線材、必要的訊號或交換元件、"
            "終端裝置，以及低階控制軟體一起工作",
            "## 先看 64 GT/s 為什麼牽動整條連線",
            "| 本文五個連動步驟 | 為什麼需要它 | 它把問題交給誰 | 要驗收什麼 | 不能直接推成 |",
            "| 1. 以 PAM4 承載更多資料 |", "| 2. 接受更敏感的原始錯誤環境 |",
            "| 3. 把資料整理成固定 Flit |", "| 4. 依序修正、偵測與重送 |",
            "| 5. 再驗設定、協定與工作負載 |",
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
            "## 先認清「誰真的被測到」",
            "| 測試物件合約的五個欄位 | 要回答的問題 | 第 140 次工作坊政策給的線索 | 常見誤讀 | 下一份證據 |",
            "| 1. 註冊產品身分 |", "| 2. 測試角色 |",
            "| 3. 暴露介面與邊界 |", "| 4. 必要測項與互通門檻 |",
            "| 5. 申請、列名與日期 |",
            "## 跑了很久沒錯，不等於 BER=0：先固定暴露量與錯誤層級",
            "### 先把六層 counter 分開",
            "| 1. 接收端原始層 |", "| 2. FEC 修正層 |",
            "| 3. CRC 殘留層 |", "| 4. 鏈路恢復層 |",
            "| 5. 連線狀態層 |", "| 6. 交易與應用層 |",
            "### 再寫一張八欄暴露護照",
            "| 1. 受測物件與版本 |", "| 5. 有效暴露分母 |",
            "| 6. Counter 契約 |", "| 8. 退出與缺口 |",
            "### 零事件仍有上界，而且上界有前提",
            "lambda_upper = -ln(alpha) / E",
            "2.995732273553991 × 10^-12 errors/bit",
            "N=1 個假想暴露量",
            "### 多空小作文先共用同一張成績單",
            "| 偏多：測試與訊號內容增加 |",
            "| 偏空：錯誤控制吸收工程複雜度 |",
            "## 把「連得對」和「賣得出去」分成兩條軸",
            "| 兩條證據軸 | 第一步 | 中間要跨過 | 靠近完成時要看到 | 本輪位置 | 不能互相替代 |",
            "| A. 連線正確性 |", "| B. 商業落地 |",
            "## 把六個動作分成不同時鐘",
            "| 本文六個時鐘 | 誰來確認 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |",
            "| 1. 規格與測試入口存在 |", "| 2. 具名產品宣稱支援 |",
            "| 3. 供應商或客戶完成互通 |", "| 4. 具名產品正式通過並列名 |",
            "| 5. 單一元件進入量產 |", "| 6. 完整平台進入客戶部署 |",
            "## 8 月 12 日複核：考場已開，最高速度公開列名仍未見",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 60
        )
        lead = topic.split("### 三句話抓重點", 1)[1].split(
            "### 為什麼重要", 1
        )[0]
        reflection = topic.split("### 想一想", 1)[1].split(
            "## 先看 64 GT/s 為什麼牽動整條連線", 1
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
            ("research_topic", 1), ("research_source", 15),
            ("research_claim", 19), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        for ledger_contract in (
            "source_id: S8", "source_id: S12", "claim_id: C10",
            "claim_id: C12", "source_id: S13", "claim_id: C13",
            "source_id: S14", "claim_id: C16", "monitor_id: T3",
            "monitor_id: T4", "monitor_id: T5",
            "source_id: S15", "claim_id: C17", "claim_id: C18",
            "claim_id: C19",
        ):
            self.assertIn(ledger_contract, topic)
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
            "process:pcie-pam4-signaling,process,PCIe 6 四電位訊號（PAM4）",
            "concept:pcie-flit-mode,concept,PCIe 6 固定資料單元（Flit Mode）",
            "capability:pcie-error-control,capability,PCIe 6 錯誤修正偵測與重送",
            "metric:pcie-first-bit-error-rate,metric,PCIe 首個位元錯誤率（FBER）",
            "stage:pcie-electrical-testing,stage,PCIe 電氣測試",
            "stage:pcie-configuration-testing,stage,PCIe 設定空間測試",
            "stage:pcie-link-protocol-testing,stage,PCIe 鏈路協定測試",
            "stage:pcie-transaction-protocol-testing,stage,PCIe 交易協定測試",
            "stage:pcie6-financial-attribution,stage,PCIe 6 財務歸因",
            "concept:pcie-test-object-contract,concept,PCIe 測試物件與邊界合約",
            "stage:pcie-component-specific-testing,stage,PCIe 關鍵元件獨立測試",
            "stage:pcie-lane-margining,stage,PCIe 通道餘裕量測",
            "stage:pcie-integrators-eligibility,stage,PCIe 公開列名資格鏈",
            "process:pcie-zero-error-exposure-passport,process,PCIe 零錯誤暴露護照",
            "metric:pcie-zero-event-upper-error-rate,metric,PCIe 零事件錯誤率單側上界",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: PCIe 6 高速連線的測試與部署階梯", graph)
        for graph_contract in (
            "edge_id: KG-PCIE6-I13", "to_id: process:pcie-pam4-signaling",
            "edge_id: KG-PCIE6-I16", "to_id: metric:pcie-first-bit-error-rate",
            "edge_id: KG-PCIE6-I20", "to_id: stage:pcie-transaction-protocol-testing",
            "edge_id: KG-PCIE6-I21", "to_id: stage:pcie6-financial-attribution",
            "edge_id: KG-PCIE6-I22", "to_id: concept:pcie-test-object-contract",
            "edge_id: KG-PCIE6-I23", "to_id: stage:pcie-component-specific-testing",
            "edge_id: KG-PCIE6-I24", "to_id: stage:pcie-lane-margining",
            "edge_id: KG-PCIE6-I25", "to_id: stage:pcie-integrators-eligibility",
            "edge_id: KG-PCIE6-I26", "to_id: process:pcie-zero-error-exposure-passport",
            "edge_id: KG-PCIE6-I27", "to_id: metric:pcie-zero-event-upper-error-rate",
        ):
            self.assertIn(graph_contract, graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 29)

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
            "added_ucie_transfer_raw_direction_payload_and_interoperability_performance_contract_without_thesis_or_clock_refresh",
            "## 先把 64 GT/s、128 GB/s、256 GB/s 與 payload 分開",
            "| 每 lane 傳輸率 |", "| 單向資料通道算術 |",
            "| 雙向 aggregate |", "| payload goodput |",
            "64×16÷8＝128 GB/s／direction",
            "128×2＝256 GB/s aggregate",
            "N=1 個假想",
            "### Raw 之後還有五層，不能只套一個固定效率",
            "| 1. 實體 module |", "| 2. Link framing 與可靠度 |",
            "| 3. Protocol 與 payload |", "| 4. 運作狀態 |",
            "| 5. 應用服務 |",
            "### 十欄 link-performance passport",
            "| 1. 物件與版本 |", "| 3. Lane 與方向 |",
            "| 4. Raw 參考平面 |", "| 5. Protocol 與 payload |",
            "| 6. 錯誤與恢復 |", "| 9. 互通與判定 |",
            "| 10. 客戶與財務 |",
            "### 多空小作文：兩邊都必須交同一份成績單",
            "| 偏多 |", "| 偏空 |", "| 共同裁決 |",
            "added_taiwan_32g_silicon_and_64g_tapeout_schedule_without_promoting_64g_interoperability",
            "## 先不要只畫一條階梯：三條軸要同時對齊",
            "| 1. 證據物件階段 |", "| 2. 測試包絡 |", "| 3. 供應商獨立性 |",
            "## 把 16、32、64 放進同一張證據矩陣",
            "| Intel／Cadence Cameron Creek 16G |",
            "| 創意 N3P／CoWoS 32G |", "| 創意 N3P／CoWoS 64G |",
            "## 創意（3443）應該怎麼讀",
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
            sum(line.startswith("- **") for line in glossary.splitlines()), 39
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
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 14), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
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
            "stage:silicon-validation,stage,實體晶片回片驗證",
            "stage:cross-vendor-demo,stage,跨廠測試晶片互通",
            "stage:compliance,stage,正式符合規格測試",
            "stage:customer-qualification,stage,客戶產品資格驗證",
            "metric:ucie-evidence-matrix,metric,UCIe 互通證據矩陣",
            "process:ucie-link-performance-passport,process,UCIe 連線效能與互通護照",
            "metric:ucie-transfer-raw-payload-direction-contract,metric,UCIe 傳輸率、raw、payload 與方向契約",
        ):
            self.assertIn(concept, concepts)
        self.assertIn("label: UCIe 小晶片互通與量產階梯", graph)
        for graph_contract in (
            "edge_id: KG-UCI-C04", "from_id: company:3443",
            "edge_id: KG-UCI-I11", "to_id: stage:silicon-validation",
            "edge_id: KG-UCI-I12", "to_id: metric:ucie-evidence-matrix",
            "edge_id: KG-UCI-I13", "to_id: process:ucie-link-performance-passport",
            "edge_id: KG-UCI-I14", "to_id: metric:ucie-transfer-raw-payload-direction-contract",
        ):
            self.assertIn(graph_contract, graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 18)

    def test_design_test_quality_station_one_separates_chiplet_handoff_contracts_and_conformance_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-12_chiplet_design_handoff_contracts.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 小晶片會連線，還不等於能交付：從 FCSA、CDXML 到 3DK 合規鏈\n"
        ))
        for contract in (
            "小晶片能用共同介面傳資料，只證明連線契約的一部分",
            "## 先分四層契約，才知道問題卡在哪裡",
            "| 1. 連線介面 |", "| 2. 系統角色 |",
            "| 3. 設計資料 |", "| 4. 符合性流程 |",
            "## 3DK 不是一個檔案，而是六種交接責任",
            "| CDK |", "| ADK |", "| MDK |", "| TDK |",
            "## 公開 schema 的可重現檢查",
            "完整母體四份檔案，`n=4`，不是抽樣，所以沒有抽樣標準誤",
            "## Schema 通過不是幾何正確：先鎖單位、座標與跨檔身分",
            "### 單位不正規化，線性差 1,000 倍、面積差 1,000,000 倍",
            "| 正規化後的線性比值 | 20,000 µm ÷ 400 µm | 50 | 基準 |",
            "| 把 20 × 15 誤當 µm² | 20 µm × 15 µm | 300 µm² | 少 1,000,000 倍 |",
            "### 同一座標數字，旋轉原點不同會落在另一處",
            "兩個答案相距 √26 = 5.099019514 mm",
            "### XSD pass 檢查已宣告文法，不檢查所有工程語意",
            "### 組裝後仍要重驗，KGD 不是永久證書",
            "### 一份語意交接護照至少要有十欄",
            "| 1. Bundle 身分 |", "| 6. Schema 與語意檢查 |",
            "| 9. 組裝後實體資格 |", "| 10. 商業與財務 |",
            "### 多空小作文：同一張護照，正反敘事才可比較",
            "### 樣本、誤差與可外推範圍",
            "本輪具名產品、工具往返、foundry／OSAT sign-off、組裝批次、客戶資格與財務觀測均為 N=0",
            "## 用六關判斷是否真的能跨公司交接",
            "| 1. 名詞與規格發布 |", "| 2. schema 可執行 |",
            "| 3. 單工具匯入 |", "| 4. 跨工具重現 |",
            "| 5. 製造與封測簽核 |", "| 6. 客戶與財務 |",
            "## 誰負責交接，誰不能替別人背書",
            "## 這篇對個股判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 12),
            ("research_claim", 14), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS,"
            "小晶片已能互相連線後，為什麼設計資料還要經過工具、"
            "晶圓廠與封測廠的共同驗證？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:chiplet-design-handoff,concept,小晶片設計資料交接與合規鏈",
            "standard:fcsa,standard,基礎小晶片系統架構（FCSA）",
            "standard:cdxml,standard,小晶片資料交換格式（CDXML）",
            "concept:3d-ic-design-kits,concept,3D-IC 設計套件（3DK）",
            "stage:executable-schema,stage,Schema 可執行驗證",
            "stage:cross-tool-conformance,stage,跨工具符合性重現",
            "stage:foundry-osat-conformance,stage,製造與封測共同簽核",
            "process:chiplet-semantic-handoff-passport,process,小晶片語意交接十欄護照",
            "metric:chiplet-unit-coordinate-cross-artifact-boundary,metric,小晶片單位座標與跨檔身分邊界",
        ):
            self.assertIn(concept, concepts)
        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "chiplet_design_handoff_contracts.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 小晶片設計資料交接與合規鏈", graph)
        for graph_contract in (
            "edge_id: KG-CDH-I12",
            "to_id: process:chiplet-semantic-handoff-passport",
            "edge_id: KG-CDH-I13",
            "to_id: metric:chiplet-unit-coordinate-cross-artifact-boundary",
        ):
            self.assertIn(graph_contract, graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 14)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "design-test-quality"
        )
        self.assertEqual(
            route["graphIds"][:2],
            ["chiplet-design-handoff-contracts", "high-na-euv-readiness"],
        )
        phase = next(
            row for row in route["phases"]
            if row["id"] == "design-manufacturing-contracts"
        )
        self.assertEqual(
            phase["graphIds"],
            ["chiplet-design-handoff-contracts", "high-na-euv-readiness"],
        )

    def test_process_control_route_requires_measurement_contract_before_control_plan(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_ai_process_control_intensity.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "## 量得出數字，不代表能拿去控製程：先過量測系統六關",
            "### 先分清「準」與「穩」",
            "| 偏差／準確度 |", "| 重複性 |", "| 再現性 |",
            "| 穩定性／漂移 |", "| 不確定度 |",
            "### 一份可用的 measurement-system contract 至少有六欄",
            "| 1. 被測量、單位與決策 |",
            "| 2. 方法、組態與環境 |",
            "| 3. 參考、校正與可追溯鏈 |",
            "| 4. 偏差、解析度與線性 |",
            "| 5. 重複性、再現性與穩定性 |",
            "| 6. 不確定度與決策規則 |",
            "可追溯的是**特定量測結果**，不是設備、",
            "**量測系統契約**先證明數字",
            "**Control plan 契約**再決定在哪一站",
            "不能把方法完整\n直接當成財務材料性",
            "## 兩個「超過」仍拼不出製程控制收入",
            "`F > 20 億美元` 與 `g > 50%`",
            "這兩組只是\n驗證不可識別性的假設情境",
            "整體 AP 不等於 process-control 分子",
            "## 8 月 13 日 FY26Q3：兩條成長線仍不是交集",
            "公司實際營收\n91.15 億美元",
            "Semiconductor Systems（半導體系統）部門實際營收 70.40 億美元",
            "AP 成長逾 70%、PDC 成長逾 50%，仍解不出 `A ∩ P`",
            "`A₀=100`、`P₀=100`",
            "分別代表 −60%、0% 或 +100%",
            "不能把 70% 與 50% 平均成 60%、相乘成一個題材放大率",
            "CY26` 明定為 FQ2'26～FQ1'27",
            "不是 2026 年 1 月 1 日到 12 月 31 日",
            "只有公司／部門總額與兩個廣義集合成長率仍不算",
            "## 缺陷數不是良率：從「被看到」走到「會殺死產品」的五道閘門",
            "### 先用四格表停止把「工具標記」當成「參考真值」",
            "| **系統有標記** | TP：成功攔截",
            "| **系統未標記** | FN／escape",
            "### 99.8801% accuracy，仍可能讓總錯判成本更高",
            "reason: added_defect_threshold_base_rate_review_load_and_miss_cost_crossover_without_thesis_or_clock_refresh",
            "source_id: S34",
            "claim_id: C39",
            "claim_id: C40",
            "Precision＝TP／(TP＋FP)",
            "8.264462809917%",
            "44.469149527515%",
            "83.480257116621%",
            "C = (10,890 − 1,799) ÷ (200 − 100) = 90.91",
            "defect-threshold cost passport",
            "| 1. 訊號／候選 |",
            "| 5. 製造與經濟結果 |",
            "使用 die-level MES 提供即時資訊、派工、缺陷攔截與分類",
            "### 為什麼缺陷數上升至少有四種解釋",
            "### 多方小作文：可以寫到哪裡",
            "### 空方小作文：可以寫到哪裡",
            "本節定向使用 `N=2` 條消息鏈",
            "source_id: S28", "source_id: S29", "source_id: S30",
            "claim_id: C31", "claim_id: C32", "claim_id: C33",
            "claim_id: C34",
            "## 警報不是處置：用九個事件讀懂異常圍堵",
            "### 三個時鐘不能合成一個「反應很快」",
            "| `t0` 最後已證實在控 |",
            "| `t6` 圍堵生效 |",
            "`signal-to-hold` 只等於 `t6−t3`",
            "### 受影響量要從物件集合重建，不能只拿流率乘時間",
            "### 多空小作文要用同一張事件護照裁決",
            "本節定向使用 `N=3` 條消息鏈",
            "source_id: S31", "source_id: S32", "source_id: S33",
            "claim_id: C35", "claim_id: C36", "claim_id: C37",
            "claim_id: C38",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 34),
            ("research_claim", 40), ("metric_comparison", 5),
            ("impact", 4), ("monitoring_item", 10),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:measurement-system-contract,concept,製程控制量測系統契約",
            "metric:measurement-measurand-decision,metric,被測量單位與決策",
            "capability:measurement-method-context,capability,量測方法組態與環境",
            "capability:measurement-reference-traceability,capability,量測參考校正與可追溯鏈",
            "metric:measurement-bias-resolution-linearity,metric,量測偏差解析度與線性",
            "metric:measurement-repeatability-reproducibility-stability,metric,量測重複性再現性與穩定性",
            "metric:measurement-uncertainty-decision-rule,metric,量測不確定度與決策規則",
            "process:out-of-control-action-plan,process,失控處置計畫",
            "process:excursion-containment-event-passport,process,異常圍堵九事件護照",
            "metric:signal-validation-actuation-latency,metric,訊號—確認—控制動作延遲",
            "capability:manufacturing-genealogy,capability,製造履歷與物件追溯",
            "process:defect-threshold-cost-passport,process,缺陷門檻成本護照",
            "metric:defect-miss-review-cost-crossover,metric,漏失與複判成本交叉點",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "process_control_measurement_contract.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 製程控制量測系統契約", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 24)
        for node in (
            "from_id: company:kla",
            "from_id: company:nova",
            "to_id: metric:measurement-measurand-decision",
            "to_id: capability:measurement-method-context",
            "to_id: capability:measurement-reference-traceability",
            "to_id: metric:measurement-bias-resolution-linearity",
            "to_id: metric:measurement-repeatability-reproducibility-stability",
            "to_id: metric:measurement-uncertainty-decision-rule",
            "to_id: concept:inspection-control-plan",
            "to_id: metric:inspection-sampling-coverage",
            "to_id: metric:defect-sensitivity-escape",
            "to_id: metric:nuisance-false-alarm",
            "to_id: metric:inspection-cycle-time",
            "to_id: capability:excursion-containment",
            "to_id: process:out-of-control-action-plan",
            "to_id: process:excursion-containment-event-passport",
            "to_id: metric:signal-validation-actuation-latency",
            "to_id: capability:manufacturing-genealogy",
            "to_id: process:defect-threshold-cost-passport",
            "to_id: metric:defect-miss-review-cost-crossover",
            "to_id: group:semiequip", "to_id: group:packtest",
        ):
            self.assertIn(node, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "design-test-quality"
        )
        phase = next(
            row for row in route["phases"]
            if row["id"] == "measurement-process-control"
        )
        self.assertEqual(
            phase["graphIds"],
            ["process-control-measurement-contract"],
        )
        self.assertEqual(route["graphIds"][2], phase["graphIds"][0])

    def test_design_test_quality_sdc_lifecycle_separates_detection_isolation_and_commercial_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-12_ai_hardware_sdc_lifecycle.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# AI 硬體沒有報錯，答案仍可能算錯：從出廠測試到機群隔離的 SDC 責任鏈\n"
        ))
        for contract in (
            "SDC 最危險的地方不是設備停機",
            "## 先分清四種結果：沒有錯、已修正、停下來與悄悄算錯",
            "| 良性錯誤 |", "| 已修正錯誤 |", "| DUE |", "| SDC |",
            "## 一次通過不等於一生可靠：六個生命週期站點",
            "| 1. 晶片與封裝製造測試 |", "| 2. 燒機與壓力測試 |",
            "| 3. 整機整合與客戶驗收 |", "| 4. 工作前與維修後主動診斷 |",
            "| 5. 運行中偵測 |", "| 6. 隔離、重測與供應商回饋 |",
            "## 每一站要交接的不是「好／壞」，而是六欄測試契約",
            "| 1. 測試身分 |", "| 2. 題目與答案 |", "| 3. 執行環境 |",
            "| 4. 結果品質 |", "| 5. 定位與處置 |", "| 6. 零件病歷 |",
            "## 三套公開做法，各自只看到責任鏈的一個切面",
            "## 為什麼「多跑測試」仍可能抓不到",
            "added_zero_event_exposure_confidence_and_isolation_evidence_passport_without_thesis_clock_refresh",
            "## 零次命中不是零風險：先鎖試驗機會、裝置時數與錯判矩陣",
            "事件率上限＝1−0.05 的 1／N 次方",
            "| 小型驗證 | 100 | 0 | 2.951304961% | 29,513.049607 ppm |",
            "| 擴大驗證 | 1,000 | 0 | 0.299124955% | 2,991.249545 ppm |",
            "| 大型匿名母體 | 1,000,000 | 0 | 0.000299573% | 2.995728 ppm |",
            "| 百萬裝置時數 | 1,000,000 | 0 | 333,808.200695 小時 | 2,995.732274 FIT |",
            "| 十億裝置時數 | 1,000,000,000 | 0 | 333,808,200.695334 小時 | 2.995732 FIT |",
            "| 已知壞 | 90 | 10 | 100 |",
            "| 已知好 | 50 | 9,950 | 10,000 |",
            "| 陽性預測值 | 90 ÷ 140 | 64.285714% |",
            "### 多空小作文共用的 SDC 零事件—隔離十欄護照",
            "| 1. 事件定義 |", "| 6. 混淆矩陣 |", "| 10. 成本與財務 |",
            "第一張表是 N＝3 個匿名零事件情境",
            "第二張表是 N＝2 個匿名總暴露情境",
            "第三組混淆矩陣是 N＝10,100 筆刻意組成的匿名",
            "Python math／Fraction 與獨立 awk",
            "物理樣本 N＝0",
            "source_id: S11", "source_id: S12", "claim_id: C11",
            "claim_id: C12", "claim_id: C13", "claim_id: C14",
            "last_reviewed_at: 2026-08-12",
            "review_due: 2026-08-31",
            "## 用七關判斷 SDC 需求是否真的形成",
            "| 1. 分類對齊 |", "| 2. 可執行測試 |", "| 3. 品質可量化 |",
            "| 4. 裝置可隔離 |", "| 5. 病歷可回傳 |", "| 6. 跨平台重現 |",
            "| 7. 客戶與財務 |",
            "## 誰負責，誰不能替別人背書",
            "## 這篇對個股判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 39
        )
        for block, expected in (
            ("research_topic", 1), ("research_source", 12),
            ("research_claim", 14), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE,"
            "人工智慧硬體沒有報錯卻算錯時，從工廠到資料中心要如何發現、隔離與追查？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:ai-hardware-sdc-lifecycle,concept,AI 硬體 SDC 生命週期責任鏈",
            "concept:sdc-outcome-taxonomy,concept,SDC 錯誤結果分類",
            "capability:factory-sdc-screening,capability,工廠 SDC 缺陷篩檢",
            "capability:system-level-sdc-diagnostics,capability,系統層 SDC 主動診斷",
            "capability:in-fleet-sdc-detection,capability,機群運行中 SDC 偵測",
            "capability:workload-correctness-check,capability,工作負載正確性檢查",
            "capability:sdc-device-quarantine,capability,SDC 可疑設備隔離",
            "process:sdc-part-history-feedback,process,SDC 零件病歷回饋",
            "stage:sdc-common-test-format,stage,SDC 共同測試格式跨框架實作",
            "stage:sdc-commercial-attribution,stage,SDC 商業與財務歸因",
            "process:sdc-zero-event-isolation-evidence-passport,process,SDC 零事件—隔離證據十欄護照",
            "metric:sdc-exposure-confidence-confusion-boundary,metric,SDC 暴露量、信賴上限與錯判邊界",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("company:google,company,Google,GOOGL", entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "ai_hardware_sdc_lifecycle.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: AI 硬體 SDC 生命週期責任鏈", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 18)
        for graph_contract in (
            "edge_id: KG-SDC-I13",
            "to_id: process:sdc-zero-event-isolation-evidence-passport",
            "edge_id: KG-SDC-I14",
            "to_id: metric:sdc-exposure-confidence-confusion-boundary",
        ):
            self.assertIn(graph_contract, graph)

        radar = (
            ROOT / "notes" / "research_candidates"
            / "2026-08-09_industry_coverage_radar.md"
        ).read_text(encoding="utf-8")
        candidate = radar.split(
            "candidate_id: RC-AI-SILENT-DATA-CORRUPTION", 1
        )[1].split("-->", 1)[0]
        for field in (
            "status: promoted",
            "evidence_posture: research_grade",
            "route: article_and_graph",
            "article_topic_id: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE",
            "graph_id: ai-hardware-sdc-lifecycle",
        ):
            self.assertIn(field, candidate)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "design-test-quality"
        )
        self.assertIn("ai-hardware-sdc-lifecycle", route["graphIds"])
        phase = next(
            row for row in route["phases"]
            if row["id"] == "field-feedback"
        )
        self.assertEqual(
            phase["graphIds"],
            ["ai-hardware-sdc-lifecycle"],
        )

    def test_compute_connect_224g_pcb_chain_separates_material_channel_ber_and_attribution(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-12_224g_pcb_qualification_chain.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 材料表寫著低損耗，整板仍可能出錯：224G PCB 從 Dk／Df 到 BER 的七關資格鏈\n"
        ))
        for contract in (
            "材料規格表的 Dk／Df，只是高速連線的第一組輸入",
            "## 先用七關看懂：一個「低損耗」標籤還缺什麼",
            "| 1. 材料身分 |", "| 2. 測法對齊 |", "| 3. reference stackup |",
            "| 4. coupon 與板級不連續點 |", "| 5. 完整通道 loss budget |",
            "| 6. BER 與 FEC |", "| 7. 跨廠量產與公司歸因 |",
            "## 為什麼同一材料會出現不同 Dk／Df",
            "## 三組公開證據，為何還拼不成「同一塊板」",
            "| IEEE 2022 PCB contribution |", "| OIF OFC 2024 VSR demo |",
            "| IPC-4103 QPL |",
            "## loss budget 不是把幾個 dB 隨手相加",
            "db_reference_plane_fixture_removal_and_log_ratio_passport_added_without_thesis_or_clock_refresh",
            "## 32 dB 不是 32%：先建立 dB 與參考面護照",
            "### 八欄 dB 護照",
            "| 1. Quantity 與正負號 |", "| 2. Port、mode 與方向 |",
            "| 5. Measurement／device planes |", "| 6. Fixture-removal chain |",
            "| 8. Raw data 與量測品質 |",
            "### 校正、時間閘門、port extension 與去嵌入不是同一個按鈕",
            "| Calibration |", "| Gating |", "| Port extension |", "| De-embedding |",
            "### 把 OIF 的 32 dB 展開一次，但不把它改寫成效率",
            "0.0251188643150958", "0.0630957344480193%",
            "N=1 個既有 demo dB 值",
            "### 多空小作文必須先固定同一個 plane",
            "| 偏多：高頻量測與低損耗內容增加 |",
            "| 偏空：看似改善只是邊界或架構轉移 |",
            "## 為什麼 Df 不能直接換算 BER",
            "## 標準、展示與量產各有自己的時鐘",
            "## 台燿的 QPL 應該怎麼讀",
            "## 用七個欄位建立可重算的 qualification 記錄",
            "## 誰負責，誰不能替別人背書",
            "## 這篇對公司判斷的用處與界線",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 15),
            ("research_claim", 14), ("metric_comparison", 0),
            ("impact", 1), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN,"
            "材料規格表宣稱能跑高速後，做成含走線、孔洞與連接器的完整電路板，"
            "錯誤率仍能過關嗎？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:224g-pcb-qualification-chain,concept,224G PCB 材料到 BER 七關資格鏈",
            "metric:pcb-dk-df,metric,PCB 材料 Dk／Df",
            "component:pcb-stackup,component,高速 PCB stackup",
            "component:low-dk-glass-weave,component,低 Dk 玻纖與編織結構",
            "component:low-profile-copper-foil,component,低粗糙度銅箔",
            "stage:pcb-loss-coupon,stage,板級損耗 coupon",
            "component:pcb-via-connector,component,PCB via 與連接器不連續點",
            "stage:channel-loss-budget,stage,完整通道損耗預算",
            "metric:pre-post-fec-ber,metric,FEC 前後 BER",
            "stage:multi-vendor-board-qualification,stage,跨廠同板資格重現",
            "stage:224g-pcb-commercial-attribution,stage,224G PCB 商業與財務歸因",
            "process:pcb-db-reference-plane-passport,process,PCB dB 與參考面八欄護照",
            "metric:fixture-deembedded-differential-insertion-loss,metric,去嵌入差分插入損耗",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        for entity in (
            "organization:ipc,organization,IPC",
            "organization:oif,organization,OIF",
            "organization:ieee-8023,organization,IEEE 802.3",
            "organization:ethernet-alliance,organization,Ethernet Alliance",
            "company:panasonic-industry,company,Panasonic Industry",
        ):
            self.assertIn(entity, entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "224g_pcb_qualification_chain.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 224G PCB 材料到 BER 七關資格鏈", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 22)
        self.assertIn("from_id: company:6274", graph)
        self.assertIn("to_id: standard:ipc-4103", graph)
        self.assertIn("edge_id: KG-224GPCB-I19", graph)
        self.assertIn("to_id: process:pcb-db-reference-plane-passport", graph)
        self.assertIn("edge_id: KG-224GPCB-I20", graph)
        self.assertIn("to_id: metric:fixture-deembedded-differential-insertion-loss", graph)

        radar = (
            ROOT / "notes" / "research_candidates"
            / "2026-08-09_industry_coverage_radar.md"
        ).read_text(encoding="utf-8")
        candidate = radar.split(
            "candidate_id: RC-224G-PCB-MATERIAL-QUALIFICATION", 1
        )[1].split("-->", 1)[0]
        for field in (
            "group_ids: pcb",
            "status: promoted",
            "evidence_posture: research_grade",
            "route: article_and_graph",
            "article_topic_id: MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN",
            "graph_id: 224g-pcb-qualification-chain",
        ):
            self.assertIn(field, candidate)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "compute-connect"
        )
        phase = next(
            row for row in route["phases"]
            if row["id"] == "interconnect-standards"
        )
        self.assertEqual(
            phase["graphIds"][0:3],
            ["open-ai-fabrics", "224g-pcb-qualification-chain", "pcie6-compliance-ladder"],
        )

    def test_800v_power_tree_teaches_topology_before_material_selection(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_800v_power_semiconductor_partition.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 800VDC 不是 SiC 或 GaN 二選一：先看拓撲，再用六把尺選元件\n"
        ))
        for contract in (
            "thesis_claim_id: C7",
            "review_due: 2026-08-19",
            "claim_id: C5\nlabel: inference\nstatus: active",
            "claim_id: C7\nlabel: inference\nstatus: active",
            "claim_id: C11\nlabel: unverified\nstatus: active",
            "claim_id: C12\nlabel: verified\nstatus: active",
            "claim_id: C13\nlabel: verified\nstatus: active",
            "claim_id: C14\nlabel: inference\nstatus: active",
            "claim_id: C15\nlabel: inference\nstatus: active",
            "## 先用四個位置看：拓撲會把元件工作移到哪裡",
            "| 本文四個位置 |",
            "## 為什麼 48V 與 800V 會共存一段時間",
            "## 48V 不一定是 48.0V，±400V 也不能只除以 400",
            "`72,000W ÷ 50V = 1,440A`",
            "`72,000W ÷ 800V = 90A`",
            "1／256 = 0.390625%",
            "99.609375% 下降，但這只是 **fixed-R sensitivity**",
            "多空小作文：升壓是價值搬家",
            "reason: added_voltage_current_reference_plane_and_fixed_resistance_sensitivity_without_thesis_clock_refresh",
            "## 再用六把尺：同一個 power stage 也不能只看材料",
            "| 本文六把尺 |",
            "| 1. 工作電壓與電流 |",
            "| 6. Qualification 與供應 |",
            "## 最後用五關：不要用元件資料替整套系統背書",
            "| 本文五關 |",
            "| 1. Topology contract |",
            "| 5. Production BOM／財務 |",
            "reason: expanded_functional_partition_to_topology_first_six_axis_and_five_gate_contract",
            "monitor_id: T1\nstatus: retired",
            "monitor_id: T3\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 15), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 4),
            ("transition", 8),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:800v-topology-device-selection,concept,800V 拓撲與元件選擇雙層框架",
            "metric:power-stage-selection-envelope,metric,功率級六軸選材包絡線",
            "component:direct-hv-bus-converter,component,高壓匯流排直降轉換器",
            "component:48v-power-shelf,component,48V 機架電力架",
            "concept:power-voltage-current-reference-plane,concept,電力電壓電流參考平面",
            "metric:conditional-i2r-loss-sensitivity,metric,條件式 I²R 損耗敏感度",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph" / "800v_power_tree.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 25)
        for target in (
            "to_id: concept:800v-topology-device-selection",
            "to_id: metric:power-stage-selection-envelope",
            "to_id: component:direct-hv-bus-converter",
            "to_id: component:48v-power-shelf",
            "to_id: concept:power-voltage-current-reference-plane",
            "to_id: metric:conditional-i2r-loss-sensitivity",
            "to_id: stage:800v-subsystem-qualification",
            "to_id: stage:800v-site-acceptance",
            "to_id: stage:800v-commercial-attribution",
        ):
            self.assertIn(target, graph)

    def test_800vdc_protection_separates_stored_energy_discharge_pulse_and_safe_access(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-03_800vdc_protection_layers.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 800VDC 保護不是一顆保險絲：人身、故障電流與 Hot-swap 必須分層\n"
        ))
        for contract in (
            "reason: separated_capacitor_stored_energy_time_constant_residual_voltage_and_discharge_pulse_without_refreshing_thesis_clock",
            "claim_id: C12\nlabel: inference\nstatus: active",
            "claim_id: C13\nlabel: inference\nstatus: active",
            "## 關掉不等於沒電：四道維修安全閘門",
            "## 100µF、800V、1.5 秒與 10W 不是四個同義規格",
            "### 先固定電壓究竟跨在哪兩點",
            "½ × 100µF × 800V²＝32J",
            "½ × 100µF × 400V²＝8J",
            "2kΩ × 100µF＝0.2 秒",
            "800V² ÷ 2kΩ＝320W",
            "0.442467496V",
            "0.000030590%",
            "31.999990211J",
            "### 一份儲能—放電護照至少要有九欄",
            "| 1. topology／reference plane |",
            "| 9. 維修與復歸 |",
            "### 多空小作文共用同一份能量底稿",
            "N＝1 組 TI 指定名目條件",
            "真實 rack、capacitor、resistor、switch、temperature run",
            "0fb1a939c277b9efb433764ef8b17ff20d6e40bb3ab2d0a2991157f9f17abcf7",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 9),
            ("research_claim", 13), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
            ("transition", 8),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()), 32
        )

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "metric:dc-stored-energy-discharge-pulse,metric,直流儲能與放電脈衝",
            concepts,
        )
        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "800vdc_protection_layers.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 18)
        self.assertIn("edge_id: KG-8PL-I16", graph)
        self.assertIn(
            "to_id: metric:dc-stored-energy-discharge-pulse", graph
        )

    def test_800vdc_execution_route_separates_seven_facility_and_financial_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_800vdc_execution_readiness.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 800VDC 從路線圖走到量產要跨七關："
            "2026 已到設計與驗證，full-scale 仍待 2027\n"
        ))
        for contract in (
            "## 先用七關看懂：800VDC 何時才算真的走到量產",
            "| 1. 架構與時鐘 |",
            "| 2. 設施轉換邊界 |",
            "| 3. 介面、冗餘與維修 |",
            "| 4. 安全、標準與人員 |",
            "| 5. 子系統資格 |",
            "| 6. 場站 commissioning 與客戶驗收 |",
            "| 7. 量產與財務歸因 |",
            "## OCP 的三階段不是「成熟度排名」，而是改動範圍",
            "## 同樣寫 1MW，為什麼 installed、critical、actual 與 PUE 是四本帳",
            "### 先固定失效情境，再算 installed 與 critical",
            "### PUE 是年度能源比，不是容量折扣",
            "### 多空小作文要共用十欄設施容量—能源護照",
            "5+1 N+1 的 installed／critical 為 1.2／1.0MW",
            "雙完整路徑 2N 為 2.0／1.0MW",
            "0.80÷1.20 = 66.7%",
            "0.80÷2.00 = 40.0%",
            "IT energy          = 0.80MW × 8,760h = 7,008MWh",
            "Facility energy    = 1.00MW × 8,760h = 8,760MWh",
            "PUE                = 8,760 ÷ 7,008   = 1.25",
            "0.96MW",
            "1.60MW",
            "Python Fraction 與獨立 awk",
            "沒有 sampling SE／t",
            "f4db5c015154933482e84f1946dcafc297d8ad526db90d2985df35232d8ab0c2",
            "官方端點對命令列直取回應 403",
            "## 為什麼子系統通過，還不等於場站穩定",
            "## 公司公告要放回正確抽屜",
            "## 新手最常混淆的九件事",
            "## 在研究中心接著怎麼學",
            "claim_id: C4\nlabel: inference\nstatus: superseded",
            "corrected_by_claim_id: C13",
            "claim_id: C14\nlabel: verified\nstatus: active",
            "claim_id: C15\nlabel: verified\nstatus: active",
            "claim_id: C16\nlabel: inference\nstatus: active",
            "thesis_claim_id: C13",
            "review_due: 2026-09-12",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 15),
            ("research_claim", 16), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
            ("transition", 6),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:800vdc-execution-readiness,concept,800VDC 七關執行準備度",
            "stage:800v-architecture-roadmap,stage,架構需求與平台時鐘",
            "stage:800v-facility-transition,stage,設施轉換邊界",
            "stage:800v-interface-redundancy,stage,介面冗餘與維修",
            "stage:800v-standards-readiness,stage,安全標準與人員準備",
            "stage:800v-subsystem-qualification,stage,800V 子系統資格",
            "stage:800v-site-acceptance,stage,場站試運轉與客戶驗收",
            "stage:800v-commercial-attribution,stage,量產部署與財務歸因",
            "process:data-center-capacity-energy-passport,process,資料中心容量與能源十欄護照",
            "metric:installed-critical-load-pue-boundary,metric,裝置、關鍵負載與PUE邊界",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "800vdc_execution_readiness.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 800VDC 七關執行準備度", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 19)
        for edge_target in (
            "from_id: company:2308",
            "from_id: organization:open-compute-project",
            "to_id: stage:800v-architecture-roadmap",
            "to_id: stage:800v-facility-transition",
            "to_id: stage:800v-interface-redundancy",
            "to_id: stage:800v-standards-readiness",
            "to_id: stage:800v-subsystem-qualification",
            "to_id: stage:800v-site-acceptance",
            "to_id: stage:800v-commercial-attribution",
            "edge_id: KG-8ER-I15",
            "to_id: process:data-center-capacity-energy-passport",
            "edge_id: KG-8ER-I16",
            "to_id: metric:installed-critical-load-pue-boundary",
            "to_id: group:powersupply", "to_id: group:power",
            "to_id: group:thermal",
        ):
            self.assertIn(edge_target, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "power-cooling"
        )
        self.assertEqual(route["graphIds"][0], "800vdc-execution-readiness")
        phase = next(
            row for row in route["phases"]
            if row["id"] == "power-components"
        )
        self.assertEqual(
            phase["graphIds"][:2],
            ["800vdc-execution-readiness", "800v-power-tree"],
        )

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        self.assertIn("MR-2026-08-08-800VDC-T1", reviews)
        self.assertIn(
            "MR-2026-08-14-800VDC-T3-CAPACITY-ENERGY-BOUNDARY", reviews
        )

    def test_power_route_sic_chain_separates_device_system_customer_and_financial_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-12_sic_ai_power_qualification.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 元件通過短路測試，電源仍不能直接上機："
            "SiC 從 JEP203／JEP204 到 AI BBU／PSU 的七關資格鏈\n"
        ))
        for contract in (
            "元件測試回答「這顆開關在指定實驗條件下怎麼壞」",
            "## 先用七關看懂：同一顆 SiC 要拿七張不同的證書",
            "| 1. Application stress envelope |",
            "| 2. Standardized device evaluation |",
            "| 3. Supplier qualification data |",
            "| 4. Converter validation |",
            "| 5. System reliability／protection |",
            "| 6. Mixed-source customer qualification |",
            "| 7. Deployment／financial attribution |",
            "## JEP203 解決的是測法一致，不是替平台設定關斷時間",
            "## JEP204 是 stress catalog，不是壽命保證書",
            "## 三份 OCP 規格真正教了什麼",
            "## 「0 次命中」能說什麼，不能說什麼",
            "## Reference design、adoption、platform qualification 是三張不同證書",
            "## 從元件微秒到整機故障：時間線要閉合",
            "## 10–40 kA 不是 MOSFET 的測試電流：先對齊四個故障參考面",
            "### DESAT 不是只把旋鈕轉到「最快」",
            "### 一張可重算的 fault passport 至少要有四個 reference plane",
            "| 1. 故障來源 |",
            "| 2. Converter 路徑 |",
            "| 3. Device stress |",
            "| 4. Protection／clearing |",
            "40 kA 除以 250 A",
            "Edevice = ∫VDS(t) × ID(t)dt",
            "N＝0；本節不計算 kA／A 比率",
            "## 用九個欄位建立可重算的 SiC qualification pack",
            "## 誰負責，誰不能替別人背書",
            "## 台達與 power／powersupply 族群應該怎麼讀",
            "source_id: S13",
            "source_id: S14",
            "claim_id: C14",
            "claim_id: C15",
            "claim_id: C16",
            "monitor_id: T4",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 14),
            ("research_claim", 16), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-12-SIC-AI-POWER-QUALIFICATION,"
            "新的碳化矽可靠度指引，是否真的進入人工智慧備援電源與"
            "電源供應器的驗收並改變設計？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:sic-ai-power-qualification,concept,SiC 到 AI BBU／PSU 七關資格鏈",
            "standard:jep203,standard,JEDEC JEP203",
            "standard:jep204,standard,JEDEC JEP204",
            "stage:sic-application-stress-envelope,stage,SiC 應用壓力範圍",
            "stage:sic-device-evaluation,stage,SiC 元件標準化評估",
            "stage:sic-supplier-qualification-data,stage,SiC 供應商資格資料包",
            "stage:sic-converter-validation,stage,SiC BBU／PSU 轉換器驗證",
            "stage:sic-system-reliability,stage,SiC 電源系統可靠度與保護",
            "stage:sic-mixed-source-qualification,stage,SiC 跨來源客戶資格",
            "stage:sic-commercial-attribution,stage,SiC AI 電源商業與財務歸因",
            "standard:ipc-9592b,standard,IPC-9592B 電源轉換裝置要求",
            "standard:telcordia-sr332,standard,Telcordia SR-332",
            "stage:sic-short-circuit-coordination,stage,SiC 短路故障四參考面協同",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "sic_ai_power_qualification.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: SiC 到 AI BBU／PSU 七關資格鏈", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 21)
        self.assertIn("from_id: company:2308", graph)
        self.assertIn("to_id: standard:jep203", graph)
        self.assertIn("to_id: standard:jep204", graph)
        self.assertIn("to_id: stage:sic-short-circuit-coordination", graph)
        self.assertIn(
            "MI-2026-08-12-SIC-AI-POWER-QUALIFICATION#C16", graph
        )

        radar = (
            ROOT / "notes" / "research_candidates"
            / "2026-08-09_industry_coverage_radar.md"
        ).read_text(encoding="utf-8")
        candidate = radar.split(
            "candidate_id: RC-SIC-AI-POWER-QUALIFICATION", 1
        )[1].split("-->", 1)[0]
        for field in (
            "group_ids: power,powersupply",
            "status: promoted",
            "evidence_posture: research_grade",
            "route: article_and_graph",
            "article_topic_id: MI-2026-08-12-SIC-AI-POWER-QUALIFICATION",
            "graph_id: sic-ai-power-qualification",
            "因此事先第一拒絕已觸發",
        ):
            self.assertIn(field, candidate)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "power-cooling"
        )
        self.assertIn("sic-ai-power-qualification", route["graphIds"])
        phase = next(
            row for row in route["phases"]
            if row["id"] == "power-components"
        )
        self.assertEqual(
            phase["graphIds"],
            [
                "800vdc-execution-readiness", "800v-power-tree",
                "800vdc-protection-layers",
                "ai-capacitor-role-map", "sic-ai-power-qualification",
            ],
        )

    def test_policy_route_pfas_chain_separates_substance_law_qualification_and_finance(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-12_semiconductor_pfas_exposure.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# 不是看到 PFAS 限制就全面換料："
            "半導體從物質、用途、法域到再驗證的七關曝險圖\n"
        ))
        for contract in (
            "**PFAS**：一大類含碳氟鍵的人造物質",
            "## 先用七關看懂：一個 PFAS 題材要補齊哪七張表",
            "| 1. 物質身分 |",
            "| 2. 製程功能 |",
            "| 3. 產品形態 |",
            "| 4. 法域義務 |",
            "| 5. 豁免與過渡 |",
            "| 6. 變更資格驗證 |",
            "| 7. 公司與財務歸因 |",
            "## 先分清三個政策時鐘：意見、法條與申報不是同一件事",
            "## 同一台蝕刻設備，為什麼可能落進六個法規抽屜",
            "## 「找到替代分子」為什麼離量產還很遠",
            "## 建一份可重算的 PFAS qualification pack",
            "## 買進 100 公斤，不代表排放 100 公斤：PFAS 的四本帳",
            "### 先辨認四本帳各自在回答什麼",
            "### 用一個固定場址年看懂分母差異",
            "### Treatment input、destroyed amount 與 off-site fate 是三件事",
            "### 一份 flow-to-financial passport 至少有十欄",
            "### 多空小作文必須共用同一份流量底稿",
            "### 樣本、誤差與可外推範圍",
            "| 現場已驗證破壞 | 45 |",
            "closure 是 98.333333%",
            "2 公斤，占 1.666667%",
            "比例是\n2.5%",
            "N＝1 個匿名固定 site-year",
            "## 本輪第一拒絕如何裁決",
            "## 上品與三福化應該怎麼讀",
            "## 誰負責，誰不能替別人背書",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 16),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 2), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE,"
            "半導體使用的含氟物質，受限後為什麼不能直接換料或整台設備一起判定？",
            guide,
        )
        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:semiconductor-pfas-exposure,concept,半導體 PFAS 七關曝險鏈",
            "process:eu-reach-pfas-restriction,process,歐盟 REACH PFAS 限制程序",
            "process:us-tsca-pfas-reporting,process,美國 TSCA PFAS 歷史申報",
            "stage:pfas-substance-identity,stage,PFAS 物質身分盤點",
            "stage:pfas-process-function,stage,PFAS 製程功能映射",
            "stage:pfas-product-form,stage,PFAS 產品形態判定",
            "stage:pfas-jurisdiction-duty,stage,PFAS 法域與義務判定",
            "stage:pfas-derogation-transition,stage,PFAS 豁免與過渡條件",
            "stage:pfas-change-qualification,stage,PFAS 替代變更資格驗證",
            "stage:pfas-company-financial-attribution,stage,PFAS 公司與財務歸因",
            "process:pfas-site-mass-balance,process,PFAS 場址質量平衡",
            "metric:pfas-use-release-waste-boundary,metric,PFAS 使用、釋放與廢棄物流邊界",
        ):
            self.assertIn(concept, concepts)

        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("organization:echa,organization,European Chemicals Agency", entities)
        self.assertIn(
            "organization:us-epa,organization,United States Environmental Protection Agency",
            entities,
        )

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "semiconductor_pfas_exposure.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 半導體 PFAS 七關曝險鏈", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 23)
        for edge_target in (
            "from_id: company:4755", "from_id: company:4770",
            "from_id: organization:echa", "from_id: organization:us-epa",
            "to_id: group:material", "to_id: group:semiequip",
            "to_id: process:pfas-site-mass-balance",
            "to_id: metric:pfas-use-release-waste-boundary",
        ):
            self.assertIn(edge_target, graph)

        radar = (
            ROOT / "notes" / "research_candidates"
            / "2026-08-09_industry_coverage_radar.md"
        ).read_text(encoding="utf-8")
        candidate = radar.split(
            "candidate_id: RC-SEMICONDUCTOR-PFAS-EXPOSURE", 1
        )[1].split("-->", 1)[0]
        for field in (
            "group_ids: material,semiequip",
            "status: promoted",
            "evidence_posture: research_grade",
            "route: article_and_graph",
            "article_topic_id: MI-2026-08-12-SEMICONDUCTOR-PFAS-EXPOSURE",
            "graph_id: semiconductor-pfas-exposure",
            "因此事先第一拒絕已觸發",
            "next_check: 2026-12-15",
        ):
            self.assertIn(field, candidate)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "policy-compliance"
        )
        self.assertEqual(
            route["graphIds"],
            ["section301-taiwan-exposure", "semiconductor-pfas-exposure"],
        )
        phase = next(
            row for row in route["phases"]
            if row["id"] == "substance-regulation"
        )
        self.assertEqual(
            phase["graphIds"],
            ["semiconductor-pfas-exposure"],
        )

    def test_section301_policy_route_separates_tariff_gates_from_company_finance(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-23_us_section_301_taiwan.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 先分流：四種「受限制」不是同一件事",
            "### HTS 與 ECCN 都是代碼，卻回答不同問題",
            "### 同樣出現在「清單」，BIS 與 OFAC 的後果仍不同",
            "### 技術合格也不等於只有一張第三方證書",
            "### 同一產品要留下四欄，而不是一個「合規」標籤",
            "## 先用七關把國家稅率拆到公司財務",
            "### 同一商品有三個名字",
            "### 關稅由誰先付，和誰最後吸收，是兩個問題",
            "### 新手最常混淆的六件事",
            "### 在研究中心裡接著怎麼學",
            "## 公告稅率不是毛利率：從 entered value 到成本歸宿的三本帳",
            "### 先把稅率公式和金額分開",
            "### 同一筆 10% 關稅，供應商毛利率可能是三個答案",
            "### 歷史 pass-through 只能當先驗，不能當 2026 台灣係數",
            "### 一份 tariff-to-financial passport 至少有十欄",
            "### 多空小作文共用同一張護照",
            "### 樣本、誤差與可外推範圍",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "**原產地（country of origin）**",
            "**Importer of record**",
            "**關稅歸宿／轉嫁（incidence／pass-through）**",
            "**Section 232**",
            "**EAR（Export Administration Regulations）**",
            "**ECCN**",
            "**EAR99**",
            "**Entity List**",
            "**OFAC**",
            "**SDN List**",
            "**合格評定（conformity assessment）**",
            "**第一方／第二方／第三方評定**",
            "| 進口關稅／Section 301 |",
            "| EAR 出口管制 |",
            "| OFAC 制裁 |",
            "| 技術合格評定／客戶資格 |",
            "| 1. 政策行動與範圍 |",
            "| 2. HTS 商品分類 |",
            "| 3. Annex 豁免 |",
            "| 4. 海關原產地 |",
            "| 5. 出貨與交易責任 |",
            "| 6. 需求與成本轉嫁 |",
            "| 7. 公司財務歸因 |",
            "| 4.5% | 5.5% | 10.0% | 4,500 美元 | 5,500 美元 | 10,000 美元 |",
            "| 10,000 美元 | 90,000 美元 | 70,000 美元 | 20,000 美元 | 22.222222% |",
            "| 1. Policy identity |", "| 5. Customs value |",
            "| 9. Company bridge |", "| 10. Uncertainty and update |",
            "真實 company、SKU、entry、HTS、origin、importer、contract、shipment、customer 與財務期間",
            "樣本 N=0",
            "thesis_claim_id: C6",
            "claim_id: C5",
            "claim_id: C6",
            "claim_id: C7",
            "claim_id: C8",
            "claim_id: C9",
            "claim_id: C10",
            "reason: published_notice_confirmed_rate_formula_and_policy_to_company_exposure_framework",
            "reason: distinguished_tariff_export_control_sanctions_and_conformity_without_changing_section301_thesis",
            "monitor_id: T3",
            "monitor_id: T4",
            "status: retired",
            "retirement_reason: 正式政策變動應追 USTR investigation docket",
            "https://media.bis.gov/licensing/classify-your-item",
            "https://ofac.treasury.gov/faqs/56",
            "https://www.nist.gov/standardsgov/conformity-assessment-basics",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 14), ("metric_comparison", 0),
            ("impact", 4), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        glossary = topic[topic.index("### 名詞小字典"):topic.index("### 三句話抓重點")]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()),
            29,
        )

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:section301-taiwan-exposure,concept,Section 301 台灣商品七關曝險鏈",
            "stage:policy-action-scope,stage,政策行動與適用範圍",
            "stage:hts-product-classification,stage,HTS 商品分類",
            "stage:annex-exemption-test,stage,Annex 豁免判定",
            "stage:customs-origin-test,stage,海關原產地判定",
            "stage:shipment-contract-incidence,stage,出貨與交易責任",
            "stage:demand-pass-through-response,stage,需求與成本轉嫁",
            "stage:section301-company-financial-attribution,stage,Section 301 公司財務歸因",
            "process:tariff-to-financial-passport,process,關稅到財務十欄護照",
            "metric:customs-value-duty-incidence-boundary,metric,報關價值、關稅與成本歸宿邊界",
            "concept:trade-regime-separation,concept,關稅、出口管制、制裁與資格四制度分流",
            "stage:tariff-import-entry,stage,進口關稅與報關 entry",
            "stage:ear-export-license-screen,stage,EAR 出口許可判定",
            "stage:ofac-sanctions-transaction-screen,stage,OFAC 制裁交易判定",
            "stage:technical-conformity-assessment,stage,技術合格評定與客戶資格",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "section301_taiwan_exposure.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: Section 301 台灣商品七關與四制度分流", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 19)
        for edge_target in (
            "from_id: company:2308",
            "to_id: stage:policy-action-scope",
            "to_id: stage:hts-product-classification",
            "to_id: stage:annex-exemption-test",
            "to_id: stage:customs-origin-test",
            "to_id: stage:shipment-contract-incidence",
            "to_id: stage:demand-pass-through-response",
            "to_id: stage:section301-company-financial-attribution",
            "to_id: group:passive", "to_id: group:pcb",
            "to_id: group:powersupply", "to_id: group:thermal",
            "to_id: concept:trade-regime-separation",
            "to_id: stage:tariff-import-entry",
            "to_id: stage:ear-export-license-screen",
            "to_id: stage:ofac-sanctions-transaction-screen",
            "to_id: stage:technical-conformity-assessment",
            "to_id: process:tariff-to-financial-passport",
            "to_id: metric:customs-value-duty-incidence-boundary",
        ):
            self.assertIn(edge_target, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "policy-compliance"
        )
        self.assertEqual(
            route["graphIds"],
            ["section301-taiwan-exposure", "semiconductor-pfas-exposure"],
        )
        self.assertEqual(
            [phase["id"] for phase in route["phases"]],
            ["trade-border-policy", "substance-regulation"],
        )
        self.assertEqual(
            [graph_id for phase in route["phases"] for graph_id in phase["graphIds"]],
            route["graphIds"],
        )

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        self.assertIn("MR-2026-08-12-SECTION301-T1-FINAL-NOTICE", reviews)


    def test_vera_rubin_article_separates_seven_delivery_gates_and_financial_attribution(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-21_nvidia_vera_rubin_production.md"
        ).read_text(encoding="utf-8")
        self.assertTrue(topic.startswith(
            "# NVIDIA Vera Rubin 由路線圖進入量產與首波部署\n"
        ))
        headings = (
            "## 先把「量產」拆成七個交接關卡",
            "## 看到「量產／就緒／驗證／上線」，先補齊五個欄位",
            "## 一座 AI 機架不是放大的單機：七條責任鏈要同時接上",
            "## 五份一手文件，為什麼不能合併成一句「已上線」",
            "## 27,500 顆 GPU、140MW 與 10 倍效率，三種分母不能直接變成營收",
            "## 從工廠到工作負載的交付順序",
            "## 同一套系統會被數很多次：九事件出貨與會計護照",
            "## 用雙向證據把平台進度連回台灣公司",
            "## 新手最常混淆的六件事",
            "## 在研究中心裡接著怎麼學",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "| 1. 平台進入生產 |",
            "| 2. 設計／型錄就緒 |",
            "| 3. 工廠實際生產 |",
            "| 4. 整櫃 bring-up／驗證 |",
            "| 5. 站點啟用／客戶驗收 |",
            "| 6. 雲端可用／工作負載運行 |",
            "| 7. 供應商財務歸因 |",
            "| 1. 誰在說 |",
            "| 2. 說哪個物件 |",
            "| 3. 用什麼動詞 |",
            "| 4. 範圍與日期 |",
            "| 5. 下一份裁決證據 |",
            "Noetra 的規劃容量、CoreWeave 的單一工作負載 benchmark",
            "平台／客戶端往回找",
            "台灣公司端往前找",
            "平台 full production ≠ 每家供應商都在量產",
            "thesis_claim_id: C11",
            "reason: superseded_coarse_ramp_frame_after_operator_validation_cloud_offer_and_live_system_catalog_evidence",
            "corrected_by_claim_id: C11",
            "corrects_claim_id: C2",
            "monitor_id: T3",
            "monitor_id: T4",
            "monitor_id: T5",
            "source_id: S13",
            "claim_id: C12",
            "reason: added_current_platform_system_composition_and_graph_projection_without_changing_financial_boundary",
            "27,500 ÷ 72 = 6,875／18 ≈ 381.944",
            "13,750 ÷ 36 = 6,875／18 ≈ 381.944",
            "| 1. 技術可重現 |",
            "| 2. 營運轉換 |",
            "| 3. 商業變現 |",
            "| 4. 財務與供應鏈歸因 |",
            "10 倍產能直接寫成 10 倍營收",
            "source_id: S14",
            "source_id: S15",
            "source_id: S16",
            "claim_id: C13",
            "claim_id: C14",
            "claim_id: C15",
            "claim_id: C16",
            "reason: named_project_capacity_and_benchmark_economics_bridges_added_without_supplier_financial_upgrade",
            "reason: shipment_custody_acceptance_and_revenue_event_ledger_added_without_refreshing_thesis_clock",
            "### 七欄事件護照：先對物件，再對數量與控制",
            "### 存量、事件流量、可用容量與金額要分四本帳",
            "### 多空小作文共用同一張事件對帳表",
            "| 1. 廠內完工／測試 |",
            "| 2. 出廠／shipping |",
            "| 3. 到站／receiving |",
            "| 4. 安裝／commissioning |",
            "| 5. 客戶驗收 |",
            "| 6. 可用容量 |",
            "| 7. 可計費工作量 |",
            "| 8. 收入認列／應收 |",
            "| 9. 現金回收 |",
            "同一批 100 櫃若依序完工、出貨、收貨與驗收",
            "期末在途＝期初在途＋本期出貨－本期收貨±更正",
            "`installed`、`available`、`billable`、`revenue` 與 `cash`",
            "`N=3` 條定向一手消息鏈",
            "沒有新估計值、抽樣\n效果或可報的 sampling SE／t",
            "6c9b2b51b41cd2cf169f6723001cac56a31c574e9c79ec8d4d52d2bf505f8eaa",
            "74f781c2f3863c7fb772908f289504cd1c0039ce760fbca922da424c236a101d",
            "source_id: S17",
            "source_id: S18",
            "source_id: S19",
            "claim_id: C17",
            "claim_id: C18",
            "claim_id: C19",
            "claim_id: C20",
        ):
            self.assertIn(contract, topic)
        glossary = topic.split("### 名詞小字典", 1)[1].split(
            "### 三句話抓重點", 1
        )[0]
        self.assertGreaterEqual(glossary.count("- **"), 26)
        for block, expected in (
            ("research_topic", 1), ("research_source", 19),
            ("research_claim", 20), ("metric_comparison", 0),
            ("impact", 6), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        guide = (ROOT / "config" / "research_topic_guide.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "topic-MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP,"
            "新一代運算平台開始量產後，何時才有台灣供應商的訂單或收入證據？",
            guide,
        )

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "product:nvidia-vera-rubin-nvl72,product,NVIDIA Vera Rubin NVL72",
            "stage:vera-rubin-platform-production,stage,Vera Rubin 平台進入生產",
            "stage:vera-rubin-system-ready,stage,Vera Rubin 系統設計與型錄就緒",
            "stage:vera-rubin-factory-production,stage,Vera Rubin 工廠實際生產",
            "stage:vera-rubin-rack-validation,stage,Vera Rubin 整櫃帶起與系統驗證",
            "stage:vera-rubin-site-acceptance,stage,Vera Rubin 站點啟用與客戶驗收",
            "stage:vera-rubin-cloud-workload,stage,Vera Rubin 雲端可用與工作負載",
            "stage:vera-rubin-financial-attribution,stage,Vera Rubin 供應商財務歸因",
            "process:ai-system-shipment-event-passport,process,AI 系統出貨事件護照",
            "metric:installed-available-billable-revenue-boundary,metric,安裝—可用—計費—營收邊界",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("company:coreweave,company,CoreWeave,CRWV", entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "vera_rubin_delivery_contract.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: Vera Rubin 七關交付與整櫃責任", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 26)
        for node in (
            "from_id: company:nvidia", "from_id: company:coreweave",
            "from_id: company:google", "from_id: company:2376",
            "from_id: company:2382", "from_id: company:3231",
            "from_id: company:6669",
            "to_id: stage:vera-rubin-platform-production",
            "to_id: stage:vera-rubin-system-ready",
            "to_id: stage:vera-rubin-factory-production",
            "to_id: stage:vera-rubin-rack-validation",
            "to_id: stage:vera-rubin-site-acceptance",
            "to_id: stage:vera-rubin-cloud-workload",
            "to_id: stage:vera-rubin-financial-attribution",
            "to_id: concept:ai-memory-hierarchy",
            "to_id: concept:open-ai-fabrics",
            "to_id: concept:liquid-cooling-loop-boundary",
            "to_id: concept:ai-storage-data-plane",
            "to_id: capability:rack-lifecycle-control",
            "to_id: group:memory", "to_id: group:pcb",
            "to_id: group:powersupply", "to_id: group:serverodm",
            "to_id: group:thermal",
            "edge_id: KG-VRD-I18",
            "to_id: process:ai-system-shipment-event-passport",
            "edge_id: KG-VRD-I19",
            "to_id: metric:installed-available-billable-revenue-boundary",
        ):
            self.assertIn(node, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "compute-connect"
        )
        phase = next(
            row for row in route["phases"]
            if row["id"] == "data-platform"
        )
        self.assertEqual(
            phase["graphIds"],
            [
                "ai-storage-data-plane", "amd-helios",
                "vera-rubin-delivery-contract",
            ],
        )
        self.assertEqual(
            [graph_id for row in route["phases"] for graph_id in row["graphIds"]],
            route["graphIds"],
        )

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "MR-2026-08-14-VERA-RUBIN-T4-SHIPMENT-EVENT-PASSPORT", reviews
        )

    def test_company_finance_route_connects_buyer_capex_to_supplier_attribution(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_ai_capex_cash_conversion.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 同一個資料中心有四個時鐘",
            "## 折舊是成本碼表，不是利用率碼表",
            "### 先辨認存量、流量與承諾",
            "### 「按使用分攤」不是「公布利用率」",
            "### 建一張「資產批次護照」再談回收",
            "## 把四道閘門展成七張交接單",
            "### 同一美元會在不同帳本、不同時間出現",
            "### 買方與供應商要做兩端對帳",
            "### 新手最常把哪幾件事畫上等號",
            "### 在研究中心裡接著怎麼學",
            "## 會計口徑本身也會移動",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "**PP&E（不動產、廠房及設備）**",
            "**在建工程（CIP）**",
            "**尚未起租的租賃（lease not yet commenced）**",
            "**試運轉／啟用（commissioning／placed in service）**",
            "**履約義務（performance obligation）**",
            "**非現金資產增加**",
            "**折舊／折舊攤銷**",
            "**使用權資產（ROU asset）**",
            "**租賃負債（lease liability）**",
            "**起租／租賃開始（lease commencement）**",
            "**租賃新增額／本金償還**",
            "**營運資金（working capital）**",
            "## 都寫「含租賃」，仍可能是兩支碼表：新增額不等於本金",
            "| 起租／新增 | 取得使用權",
            "| 付款 | 支付本期租賃款",
            "`principal payments under finance lease obligations` 是 1,500",
            "Microsoft FY2026Q4 | CapEx 410 億美元",
            "Meta 2026Q2 | cash PP&E 301.16 億美元",
            "`301.16 + 9.62 = 310.78` 億",
            "不能硬算 `358 + 56 = 414` 億",
            "前者標成 total finance leases，後者明確是償還本金",
            "| 合約承諾 | 尚未起租的租賃",
            "| 資產可用 | 在建工程",
            "| 客戶使用與收入 | 使用量、履約義務",
            "| 現金支付與回收 | cash PP&E",
            "Microsoft FY2026 10-K | 全年 cash PP&E additions 115.948",
            "Meta 2026 Q2 10-Q | H1 cash PP&E 49.11",
            "Amazon 2026 Q2 10-Q | H1 PP&E 淨新增 118.648",
            "機械相減是 29.824",
            "分部成本按 usage 分攤也不是公開的容量利用率",
            "| 資產批次／站點 |",
            "| 容量與利用分母 |",
            "| 付款、收款與供應商共同鍵 |",
            "| 1. 資本計畫與承諾 |",
            "| 2. 現金 PP&E 與租賃 |",
            "| 3. 資產建置與試運轉 |",
            "| 4. 服務容量可用 |",
            "| 5. 工作負載、利用與收入 |",
            "| 6. 買方現金回收 |",
            "| 7. 供應商財務歸因 |",
            "供應商端還多一道時間差",
            "國巨 Q2 公司財務分母",
            "claim_id: C6",
            "claim_id: C7",
            "claim_id: C8",
            "claim_id: C9",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "claim_id: C13",
            "claim_id: C14",
            "claim_id: C15",
            "reason: capex_to_supplier_financial_bridge_synthesized_from_existing_disclosures",
            "reason: four_accounting_clocks_added_from_meta_and_amazon_filings_without_refreshing_thesis_clock",
            "reason: finance_lease_addition_and_principal_clocks_separated_with_fasb_contract_without_refreshing_thesis_clock",
            "reason: depreciation_cost_clock_separated_from_utilization_and_recovery_with_latest_filings_without_refreshing_thesis_clock",
            "evidence: sources:S1,S2,S3,S4,S5",
            "evidence: sources:S7,S8",
            "evidence: sources:S1,S2,S9,S10",
            "evidence: sources:S11,S12,S13",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 13),
            ("research_claim", 15), ("metric_comparison", 9),
            ("impact", 4), ("monitoring_item", 2),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:ai-capex-cash-conversion,concept,AI CapEx 到供應商財務七關橋接",
            "concept:capital-asset-revenue-cash-clocks,concept,承諾、資產、收入與現金四個時鐘",
            "stage:capital-commitment,stage,資本計畫與承諾",
            "stage:cash-ppe-and-leases,stage,現金 PP&E 與租賃支出",
            "stage:asset-construction-commissioning,stage,資產建置與試運轉",
            "stage:service-capacity-available,stage,服務容量可用",
            "stage:workload-utilization-revenue,stage,工作負載利用與收入",
            "stage:buyer-cash-conversion,stage,買方現金回收",
            "stage:supplier-financial-attribution,stage,供應商財務歸因",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("company:amazon,company,Amazon,AMZN", entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "ai_capex_cash_conversion.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: AI CapEx 到供應商財務七關橋接", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 15)
        for node in (
            "from_id: company:microsoft", "from_id: company:meta",
            "from_id: company:amazon", "to_id: stage:capital-commitment",
            "to_id: stage:supplier-financial-attribution",
            "to_id: group:serverodm", "to_id: group:pcb",
            "to_id: group:powersupply", "to_id: group:thermal",
            "to_id: concept:capital-asset-revenue-cash-clocks",
        ):
            self.assertIn(node, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "company-finance"
        )
        self.assertEqual(
            route["graphIds"],
            [
                "ai-capex-cash-conversion",
                "us-advanced-packaging-regionalization",
                "yageo-q2-financial-materiality",
            ],
        )
        self.assertEqual(
            [phase["id"] for phase in route["phases"]],
            [
                "buyer-capex-conversion",
                "regional-capacity-conversion",
                "supplier-financial-attribution",
            ],
        )
        self.assertEqual(
            [graph_id for phase in route["phases"] for graph_id in phase["graphIds"]],
            route["graphIds"],
        )

    def test_power_buffering_separates_ideal_mission_energy_from_nameplate_and_delivery(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-03_ai_power_buffering_hierarchy.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 三種儲能怎麼接力：先看事件持續多久",
            "## 「能撐多久」不是完整規格：先寫七欄事件合約",
            "## 45–90 秒不是銘牌容量：把功率、任務能量與可交付能量拆成三本帳",
            "## 這篇和 800V 電力轉換文章各回答什麼",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "reason: converted_bbu_power_and_duration_into_conditional_delivered_energy_book_without_refreshing_thesis_clock",
            "source_id: S8",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "800kW（480VAC option 表列範圍下緣）",
            "10.00kWh",
            "20.00kWh",
            "13.75kWh",
            "27.50kWh",
            "E_deliverable ≈ (SOC_start − SOC_min) × E_rated × SOH × η_discharge",
            "Python `Decimal` 與 `awk` 獨立重算一致",
            "### 多方小作文：可以寫到哪裡",
            "### 空方小作文：可以寫到哪裡",
            "### 多空共同裁決：同一張可交付能量護照",
            "### 分母、誤差與限制",
            "`N=2` 條消息鏈",
            "本輪沒有刷新 C4 主命題、`last_reviewed_at`、`review_due` 或 base confidence",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 8),
            ("research_claim", 12), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 3),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)
        glossary = topic[topic.index("### 名詞小字典"):topic.index("### 三句話抓重點")]
        self.assertEqual(
            sum(line.startswith("- **") for line in glossary.splitlines()),
            38,
        )

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn(
            "metric:buffer-nameplate-delivered-energy-bridge,metric,銘牌到可交付能量橋接",
            concepts,
        )
        graph = (
            ROOT / "notes" / "knowledge_graph" / "ai_power_buffering.md"
        ).read_text(encoding="utf-8")
        self.assertIn("edge_id: KG-APB-I16", graph)
        self.assertIn(
            "to_id: metric:buffer-nameplate-delivered-energy-bridge", graph
        )
        self.assertEqual(graph.count("<!-- knowledge_edge"), 18)

    def test_design_test_quality_route_uses_eight_denominators_before_financial_attribution(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_inference_compute_tester_tam.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 先把 tester TAM 拆成八個分母",
            "## 一顆複雜晶片會在哪些地方被測",
            "## 同樣叫「測試」，七種決策不能相加",
            "## 一份測試責任護照至少有十欄",
            "## 哪些變更要觸發回歸重測",
            "## 為什麼測試時間增加，設備台數仍可能不線性增加",
            "## 120 秒變 150 秒，不等於多買 25% 測試單元",
            "## 五組數字不能直接排高低",
            "## 產業角色不要混在一起",
            "## 同一個 test cell，會開出三種不同的發票",
            "## 新手最常混淆的八件事",
            "## 在研究中心接著怎麼學",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "thesis_claim_id: C6",
            "reason: reframed_tester_tam_as_eight_denominator_test_cell_and_financial_conversion",
            "status: superseded",
            "corrected_by_claim_id: C6",
            "correction_kind: supersedes",
            "corrects_claim_id: C2",
            "monitor_id: T3",
            "monitor_id: T4",
            "monitor_id: T5",
            "reason: added_test_responsibility_passport_and_change_triggered_regression_without_thesis_upgrade",
            "reason: separated_test_service_interface_product_and_equipment_revenue_clocks_without_company_beneficiary_upgrade",
            "reason: added_test_cell_seconds_productive_time_and_capacity_ceiling_passport_without_thesis_or_clock_refresh",
            "claim_id: C8",
            "claim_id: C9",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "claim_id: C13",
            "claim_id: C14",
            "| 1. 產品組合與數量 |",
            "| 8. 公司財務歸因 |",
            "| 1. 設計驗證與可測試性設計 |",
            "| 10. 變更與回歸條件 |",
            "需求的測試單元時數",
            "同時站數 × 並行效率 × 可用率",
            "增量實體單元 = ceil[max(0, test-cell 等價數 − 既有未承諾合格單元)]",
            "9.965934623469",
            "10.381181899447",
            "4.166666666667%",
            "N=2 個假想設定",
            "多空小作文必須共用同一份護照",
            "observation_id: M2-O1",
            "value_kind: upper_bound",
            "reported_value: 720",
            "observation_id: M2-O2",
            "reported_value: 15..50",
            "observation_id: M3-O1",
            "observation_id: M3-O2",
            "observation_id: M3-O3",
            "comparability: not_comparable",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 21),
            ("research_claim", 14), ("metric_comparison", 8),
            ("impact", 3), ("monitoring_item", 5),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:inference-compute-test-demand,concept,推論晶片測試需求八分母",
            "stage:test-device-mix-volume,stage,測試產品組合與數量",
            "stage:test-insertion-map,stage,測試插入點地圖",
            "stage:test-content-coverage,stage,測試內容與覆蓋",
            "stage:test-time-power-pin-thermal,stage,單顆測試時間與負載",
            "stage:test-multisite-throughput,stage,多站並行與吞吐",
            "stage:test-yield-retest-escape,stage,良率重測與漏測",
            "stage:test-installed-base-capex,stage,既有設備與增量資本支出",
            "stage:test-company-financial-attribution,stage,測試需求公司財務歸因",
            "concept:test-responsibility-passport,concept,測試責任護照",
            "process:test-change-triggered-regression,process,測試變更觸發回歸重測",
            "process:test-result-lineage-feedback,process,測試結果沿革與現場回饋",
            "process:test-cell-capacity-passport,process,測試單元產能護照",
            "metric:test-seconds-to-qualified-cell-equivalents,metric,測試秒數到合格單元等價數",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("company:advantest,company,Advantest,6857", entities)
        self.assertIn("company:teradyne,company,Teradyne,TER", entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "inference_compute_test_demand.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 推論晶片測試需求八分母", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 21)
        for node in (
            "from_id: company:advantest", "from_id: company:teradyne",
            "from_id: company:amazon", "from_id: company:microsoft",
            "from_id: company:amkor",
            "to_id: stage:test-device-mix-volume",
            "to_id: stage:test-insertion-map",
            "to_id: stage:test-content-coverage",
            "to_id: stage:test-time-power-pin-thermal",
            "to_id: stage:test-multisite-throughput",
            "to_id: stage:test-yield-retest-escape",
            "to_id: stage:test-installed-base-capex",
            "to_id: stage:test-company-financial-attribution",
            "to_id: concept:test-responsibility-passport",
            "to_id: process:test-change-triggered-regression",
            "to_id: process:test-result-lineage-feedback",
            "to_id: process:test-cell-capacity-passport",
            "to_id: metric:test-seconds-to-qualified-cell-equivalents",
            "to_id: group:ipdesign", "to_id: group:packtest",
            "to_id: group:semiequip",
        ):
            self.assertIn(node, graph)

        route = next(
            row for row in bd.RESEARCH_LEARNING_ROUTES
            if row["id"] == "design-test-quality"
        )
        self.assertEqual(
            route["graphIds"],
            [
                "chiplet-design-handoff-contracts", "high-na-euv-readiness",
                "process-control-measurement-contract",
                "hybrid-bonding", "inference-compute-test-demand",
                "ai-hardware-sdc-lifecycle",
            ],
        )
        self.assertEqual(
            [phase["id"] for phase in route["phases"]],
            [
                "design-manufacturing-contracts",
                "measurement-process-control",
                "packaging-production-test",
                "field-feedback",
            ],
        )
        self.assertEqual(
            [graph_id for phase in route["phases"] for graph_id in phase["graphIds"]],
            route["graphIds"],
        )

    def test_us_advanced_packaging_route_preserves_scope_money_and_nine_gates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-01_us_advanced_packaging_regionalization.md"
        ).read_text(encoding="utf-8")
        headings = (
            "## 先把區域化拆成九個交接關卡",
            "## 四種錢不能放進同一個加總",
            "## 15 億美元預付款不是免息營收：用六本帳拆開資金、義務與產能",
            "## 為什麼會看見 17 億、約 20 億與 70 億美元",
            "## 產能數字至少有五個分母",
            "## 產能上線、損平與滿載不是同一天：用雙地區成熟度護照拆零和敘事",
            "## 事件、會計與產能時鐘",
            "## 新手最常混淆的六件事",
            "## 在研究中心裡接著怎麼學",
        )
        positions = [topic.index(heading) for heading in headings]
        self.assertEqual(positions, sorted(positions))
        for contract in (
            "thesis_claim_id: C16",
            "reason: reconciled_chips_award_project_scope_with_expanded_campus_and_nine_gate_conversion",
            "reason: arizona_break_even_full_utilization_and_taiwan_concurrent_build_clocks_reconciled",
            "claim_id: C5",
            "claim_id: C6",
            "claim_id: C7",
            "claim_id: C8",
            "claim_id: C9",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "claim_id: C13",
            "claim_id: C14",
            "claim_id: C15",
            "claim_id: C16",
            "source_id: S10",
            "source_id: S11",
            "source_id: S12",
            "corrected_by_claim_id: C6",
            "corrects_claim_id: C2",
            "monitor_id: T3",
            "monitor_id: T4",
            "| 1. 政策獎勵與專案範圍 |",
            "| 9. 財務與區域替代 |",
            "最高 4.07 億美元直接補助",
            "每月 14,500 片晶圓與 370 萬顆 units",
            "project／phase／facility",
            "合約負債 3.930 億美元",
            "採購義務 14.652 億美元",
            "7 月已收到 1 億美元",
            "公司另行簽訂一份預計 2027 年收到約 15 億美元",
            "文件沒有說後一份也需要信用狀",
            "| 1. 協議權利帳 |",
            "| 6. 履約與經濟帳 |",
            "### 多方小作文：可以寫到哪裡",
            "### 空方小作文：可以寫到哪裡",
            "### 分母、誤差與限制",
            "`N=1` 家發行人的一份 2026Q2 10-Q",
            "Python `Decimal` 與 `awk` 兩條獨立路徑",
            "SHA-256 0fa5f4241d383af7a7ea1ab24b742797c598c7967b133e21e09d9c3d92166848",
            "不能只看到面額就假定等額現金已被凍結",
            "2029 預估損平",
            "2030 預估滿載",
            "Phase 2 尚未納入",
            "約 10 億美元 revenue contribution",
            "超過 30% gross margin",
            "FOCoS／FC BGA",
            "### 跨地區比較要帶十欄成熟度護照",
            "| 10. 需求反事實 |",
            "零和與互補都尚未被證明",
            "N＝2 家 OSAT、N＝2 條公司一手消息鏈",
            "corrected_by_claim_id: C16",
            "corrects_claim_id: C6",
            "monitor_id: T5",
            "monitor_id: T6",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 12),
            ("research_claim", 16), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 6),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:us-advanced-packaging-regionalization,concept,美國先進封裝區域化九關橋接",
            "stage:chips-award-scope,stage,CHIPS 獎勵與專案範圍",
            "stage:milestone-disbursement,stage,里程碑撥付",
            "stage:regional-project-capital-stack,stage,區域專案資本結構",
            "stage:regional-site-construction,stage,區域廠房建設交付",
            "stage:regional-tool-process-enablement,stage,工具進場與製程啟用",
            "stage:regional-process-qualification,stage,區域製程資格",
            "stage:regional-customer-product-qualification,stage,區域客戶產品資格",
            "stage:regional-capacity-ramp-utilization,stage,區域產能爬坡與利用",
            "stage:regional-packaging-financial-attribution,stage,區域封裝財務與替代歸因",
        ):
            self.assertIn(concept, concepts)
        entities = (ROOT / "config" / "external_entities.csv").read_text(
            encoding="utf-8"
        )
        self.assertIn("company:amkor,company,Amkor Technology,AMKR", entities)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "us_advanced_packaging_regionalization.md"
        ).read_text(encoding="utf-8")
        self.assertIn("label: 美國先進封裝區域化九關橋接", graph)
        self.assertEqual(graph.count("<!-- knowledge_edge"), 15)
        for node in (
            "from_id: company:amkor", "from_id: company:nvidia",
            "from_id: company:tsmc", "to_id: stage:chips-award-scope",
            "to_id: stage:milestone-disbursement",
            "to_id: stage:regional-project-capital-stack",
            "to_id: stage:regional-site-construction",
            "to_id: stage:regional-tool-process-enablement",
            "to_id: stage:regional-process-qualification",
            "to_id: stage:regional-customer-product-qualification",
            "to_id: stage:regional-capacity-ramp-utilization",
            "to_id: stage:regional-packaging-financial-attribution",
            "to_id: group:packtest", "to_id: group:semiequip",
            "to_id: group:material",
        ):
            self.assertIn(node, graph)
        for graph_contract in (
            "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C12",
            "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C13",
            "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C14",
            "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C15",
            "MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C16",
            "2028 至 2029 ramp 與 2030 estimated full utilization",
            "兩地同時規劃新增能力",
        ):
            self.assertIn(graph_contract, graph)

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        for review_id in (
            "MR-2026-08-14-US-ADVPKG-T3-MATURITY-CLOCKS",
            "MR-2026-08-14-US-ADVPKG-T4-TAIWAN-CONCURRENT-BUILD",
        ):
            self.assertIn(review_id, reviews)

    def test_priority_q2_faraday_dual_denominator_blocks_false_conversion_rate(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-29_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: faraday_nre_mp_dual_denominator_and_revenue_recognition_bridge_added_without_refreshing_thesis_clock",
            "## 35.4% 與 0.4% 不是轉單率：先做 NRE／MP 雙分母矩陣",
            "NRE AI 的顯示值代理是 159.579306 百萬元",
            "MP AI 的顯示值代理是 9.720068 百萬元",
            "169.299374 百萬元",
            "部分代理占 5.1093296%",
            "167.858971～170.739777",
            "5.0658593%～5.1527999%",
            "### 合約帳與收入時鐘不能替 cohort 補空白",
            "某一時點／隨時間認列 | 2,573.901／739.633 百萬元",
            "提供勞務＋IP 尚未履約交易價格 | 3,470.780 百萬元",
            "委託設計專案履行合約成本 | 555.547 百萬元",
            "### 轉化率需要一張同批專案護照",
            "| 8. 分子／分母公式 |",
            "### 多空小作文必須共用同一個 cohort 裁決",
            "真正同一 AI 專案的 NRE、tape-out、qualification、MP、毛利與收現共同\n觀測 N＝0",
            "Python Decimal\n與獨立 awk 兩條路徑",
            "7ed866b210f9175272ab10e0a106572a69f786d68c16d3dfe3dca009d98e02c9",
            "source_id: S27",
            "claim_id: C16",
            "claim_id: C17",
            "claim_id: C18",
            "claim_id: C19",
            "8 月 15 日依 T10 回查",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 31),
            ("research_claim", 27), ("metric_comparison", 0),
            ("impact", 7), ("monitoring_item", 10),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

    def test_priority_q2_tong_hsing_separates_product_application_and_capex_clocks(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-29_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: tong_hsing_product_application_capex_clock_bridge_added_without_refreshing_thesis_clock",
            "## 同一個 11.8%，其實是五個收入池在拉扯：同欣電產品、應用與擴產時鐘",
            "| 影像產品 | 1,391.322 | 1,615.531 | +224.209 | 67.2% |",
            "| 陶瓷電路板 | 521.287 | 602.603 | +81.316 | 24.4% |",
            "| 高頻無線通訊模組 | 348.336 | 407.159 | +58.823 | 17.6% |",
            "| 混合積體電路模組 | 546.587 | 505.265 | −41.322 | −12.4% |",
            "| 合併營收 | 2,819.237 | 3,152.964 | +333.727 | 100.0% |",
            "### 產品、應用與客戶是三張不同的表",
            "車用 60%、工業 15%、通訊 13%、手機 8%、醫療 3%",
            "45.898%",
            "產品×應用×客戶交叉表",
            "### 毛利可以做數學橋，不能做產品因果橋",
            "| 若新增營收沿用 Q1 毛利率 | +93.344 |",
            "| Q2 合併毛利率變動殘差 | +98.353 |",
            "### 擴產至少有五個不同時鐘",
            "菲律賓廠房工程合約 613.576 百萬元",
            "尚未到期工程款 490.127 百萬元",
            "未完工程及待驗設備增置 256.521 百萬元",
            "購置不動產、廠房及設備付現 396.638 百萬元",
            "存貨半年增加 288.524 百萬元",
            "### 多空小作文要共用同一張裁決表",
            "真正的產品×應用×客戶×毛利共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "a7a8a414f79098a5af8cef8ec8eb23805ed68b57b64eaaec6c8c4135d7e8c81f",
            "b169afa31c1884c21d33b29602b3a09bb5dfc863595d058f192e57a00eb4e638",
            "source_id: S28",
            "source_id: S29",
            "claim_id: C20",
            "claim_id: C21",
            "claim_id: C22",
            "claim_id: C23",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 31),
            ("research_claim", 27), ("metric_comparison", 0),
            ("impact", 7), ("monitoring_item", 10),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

    def test_priority_q2_eris_separates_segment_end_application_and_cash_sources(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-29_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: eris_q2_segment_related_party_and_cash_bridge_added_without_refreshing_thesis_clock",
            "## 營收季增 17%，為什麼不能直接叫作 AI 晶圓放量：德微三道橋",
            "| 德微科技及杰成 | 研發、製造及銷售二極體 | 358.452 | 452.781 | +94.329 | 81.1% |",
            "| 亞昕科技 | 研發、製造及銷售晶圓 | 205.532 | 208.024 | +2.492 | 2.1% |",
            "| 喜可士 | 研發及銷售二極體、IC、散熱片及晶片 | 120.614 | 140.099 | +19.485 | 16.8% |",
            "| 合併營收 | 三部門外部收入加總 | 684.598 | 800.904 | +116.306 | 100.0% |",
            "晶圓部門外部\n收入只較 Q1 增加 1.2125%",
            "公司總營收增量的 70.3369%",
            "### 第二道橋：毛利改善可以重算，產品因果仍要留白",
            "| 新增營收沿用 Q1 毛利率 | +44.503 |",
            "| Q2 合併毛利率變動殘差 | +20.357 |",
            "### 第三道橋：正營業現金流與現金大增不是同一件事",
            "| 營業活動 | +62.542 |",
            "| 籌資活動 | +300.463 |",
            "| 現金增加 | +388.237 |",
            "處分亞昕科技部分股權",
            "96.10% 降至 76.63%",
            "800.000 百萬元",
            "真正的\n部門×料號×AI server／車用×終端客戶×毛利×收現共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "6b3921dd5445261652daab299bbc987a603c5a8ae633945e8e3ee031c9700add",
            "4de043ba2038ec55bc76948fd6f9f42eabf8f3280913f43c9b8c7527febbab04",
            "source_id: S30",
            "source_id: S31",
            "claim_id: C24",
            "claim_id: C25",
            "claim_id: C26",
            "claim_id: C27",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 31),
            ("research_claim", 27), ("metric_comparison", 0),
            ("impact", 7), ("monitoring_item", 10),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

    def test_missed_priority_q2_macronix_four_bridges_preserve_denominators(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-31_missed_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "thesis_claim_id: C19",
            "## 旺宏 Q2 四道橋：64.4% 毛利不是一個乾淨的價格訊號",
            "| 1. 毛利 → 存貨會計 |",
            "| 2. Flash → eMMC／NOR／SLC |",
            "| 3. 獲利 → 現金與收款 |",
            "| 4. 設備 → 三個時間點 |",
            "報表毛利率 64.42%",
            "回升利益相當於營收 5.02 個百分點",
            "機械橋接為 59.40%",
            "Flash 收入 174.71 億元，占合併營收 91.35%",
            "H1 營業現金流 100.34 億元",
            "未認列設備採購承諾 153.98 億元",
            "### 多方小作文：可以寫到哪裡",
            "### 空方小作文：可以寫到哪裡",
            "### 分母、誤差與限制",
            "`N=1` 家發行人、1 份 115Q2 合併財報",
            "SHA-256 5f554e96428e6cd607913ad6a5d78508795c828462294066ef269d65b6213ed2",
            "claim_id: C14\nlabel: inference\nstatus: superseded",
            "claim_id: C19\nlabel: inference\nstatus: active",
            "monitor_id: T9\nstatus: retired",
            "monitor_id: T11\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 30),
            ("research_claim", 35), ("metric_comparison", 12),
            ("impact", 6), ("monitoring_item", 12),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "MR-2026-08-14-MISSED-Q2-T9-MACRONIX-FILING", reviews
        )

    def test_missed_priority_q2_ardentec_separates_production_from_capital_absorption(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-31_missed_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: added_ardentec_q2_capital_absorption_and_commercial_maturity_bridges_without_refreshing_thesis_clock",
            "## 7 月量產，為什麼不能倒填 Q2 收入：欣銓七道資本吸收時鐘",
            "6 月 30 日；隔日才進入第三季",
            "7 月起正式量產",
            "| 4. 未完／待驗 |",
            "Q2＝H1 累計－Q1",
            "| 營業現金流 | 16.71 億元 | 8.70 億元 |",
            "| 取得 PP&E 付現 | 13.30 億元 | 56.77 億元 |",
            "| 自由現金流 | 正 3.41 億元 | 負 48.07 億元 |",
            "| 銀行借款現金淨流入 | 負 7.43 億元 | 正 40.71 億元 |",
            "占 86.92%",
            "期末該欄 64.84 億元",
            "Q2 總折舊 8.62 億元、季增 4.95%",
            "EIC／PIC 測試設備逾 150 台",
            "晶圓測試與成品測試分別季增 16.01% 與 8.45%",
            "真正廠區×產品×客戶×設備×利用率×收入×毛利×收現共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "source_id: S23",
            "source_id: S24",
            "SHA-256 e787cc74a0df031e86a471721e8fe6a0a8b75e2b6fe9f113ba098ef5089fca80",
            "SHA-256 905bcda6204f62f7d7d14c5decd79279fe7ddea9d13c1f37d4dce48ba7646ad5",
            "claim_id: C20\nlabel: verified\nstatus: active",
            "claim_id: C21\nlabel: inference\nstatus: active",
            "claim_id: C22\nlabel: verified\nstatus: active",
            "claim_id: C23\nlabel: inference\nstatus: active",
        ):
            self.assertIn(contract, topic)

    def test_missed_priority_q2_globalwafers_separates_operating_valuation_cash_and_event_clocks(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-31_missed_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: added_globalwafers_q2_operating_valuation_cash_capacity_and_subsequent_event_bridges_without_refreshing_thesis_clock",
            "## 淨利季增 99.3%，為什麼不能叫晶圓漲價：環球晶三個日期、四本帳",
            "| 7 月 21 日事件日 |",
            "| 營業利益 | 14.75 | 14.23 | −0.53 |",
            "營業利益季減 0.53 億元，業外淨額季增 22.91 億元",
            "占 Q2 稅前淨利 66.21%",
            "股份連結選擇權公允價值再衡量損失",
            "加回選擇權損失後的其餘 FVTPL 機械殘差",
            "FVTPL 增量占「其他利益及損失」增量 93.22%",
            "營業現金流為 21.39 億元",
            "負 0.63 億元",
            "未完工程及待驗設備轉出 | 418.47",
            "總折舊 | 24.08",
            "模擬毛利率 32.4%、營益率 22.6%",
            "真正產品×晶圓尺寸×廠區×客戶×數量×ASP×利用率×毛利×收現共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "source_id: S25",
            "source_id: S26",
            "SHA-256 30375d8441d746efdb292d41a9354b102bdbbd96a6495dcecf36f477218793ac",
            "SHA-256 8b23bb27baa389809c0fb27c63fec020cf6af4cb30d302e30a7afae25c3b2819",
            "公司簡報為 85e1889eb3fabdab34c072b838a543fc7c46f02b946db76e1af171ab54fd0380",
            "claim_id: C24\nlabel: verified\nstatus: active",
            "claim_id: C25\nlabel: verified\nstatus: active",
            "claim_id: C26\nlabel: inference\nstatus: active",
            "claim_id: C27\nlabel: inference\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 30),
            ("research_claim", 35), ("metric_comparison", 12),
            ("impact", 6), ("monitoring_item", 12),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

    def test_missed_priority_q2_delta_separates_segment_application_product_and_maturity_coordinates(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-31_missed_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: added_delta_q2_overlapping_denominator_segment_profit_cash_capex_and_maturity_bridges_without_refreshing_thesis_clock",
            "## 1,832.56 億元不能拆成 AI＋液冷＋HVDC：台達電六種重疊座標",
            "| 應報導部門 | Q2 電源及零組件 962.96 億元",
            "| 資料中心應用 | 管理層稱 H1 相關業務占合併營收逾半",
            "| AI 相關產品 | 管理層預期 2026 全年占總營收逾 25%",
            "| 液冷產品族 | 管理層稱 2025 約占營收 10%",
            "| HVDC 商業時鐘 | 管理層預期正負 400V 與 800V 產品 Q3 起量產",
            "全公司營收增量的 **93.19%**",
            "全公司營業利益增量的 **108.95%**",
            "預期信用減損費用為 10.20 億元",
            "這一項約占增量的 **23.32%**",
            "| 合併稅後淨利 | 238.35 | 271.69 | ＋33.35 |",
            "| 歸屬母公司淨利 | 205.56 | 251.36 | ＋45.80 |",
            "歸母淨利季增 **22.28%**",
            "合併淨利季增\n**13.99%**",
            "| 營業現金流 | 431.69 |",
            "| PP&E 付現 | 161.61 |",
            "| 簡單自由現金流 | 270.08 |",
            "期末短期借款則由 Q1 的 12.18 億元升至\n163.02 億元",
            "H2 逾 400 億元與全年約 700 億元",
            "真正產品族×應用×部門×客戶×實際收入共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "source_id: S27",
            "source_id: S28",
            "source_id: S29",
            "79bc77a81d436331c308264767bf72291a21a9a60bfcd8dd88a0612a2a97924f",
            "838b88e3b21639a122a4cdd88d87fe1bb3b185592d603184d65e5a955402ed08",
            "ddc39e8e1387e56d0974ac22a7d2566d91266bd34f178c54c1fae9416dd0d04e",
            "1d3cf7fb34d23713300c694b86e0af732115eb937b24996b649591aad107916b",
            "claim_id: C28\nlabel: verified\nstatus: active",
            "claim_id: C29\nlabel: verified\nstatus: active",
            "claim_id: C30\nlabel: verified\nstatus: active",
            "claim_id: C31\nlabel: inference\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 30),
            ("research_claim", 35), ("metric_comparison", 12),
            ("impact", 6), ("monitoring_item", 12),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        scans = (
            ROOT / "notes" / "research_topics" / "scan_log.csv"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "scan-2026-08-14-delta-overlapping-denominators-and-cash-capex-bridges",
            scans,
        )

    def test_missed_priority_q2_powertech_separates_dual_marginals_hbm_gates_and_capital_clocks(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-31_missed_priority_q2_disclosures.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: added_powertech_q2_dual_marginal_mix_hbm_evidence_gates_and_cash_capex_bridges_without_refreshing_thesis_clock",
            "## 兩張 100% 圓餅不能相乘：力成 231.16 億元與 HBM2 的五道證據門",
            "| 封裝加工 | 153.14 億元／66.25% | Logic | 41% |",
            "| 測試加工 | 53.72 億元／23.24% | NAND | 29% |",
            "231.16 億元×66.25%×19% 算成 29.10 億元",
            "0 到 43.92 億元的最寬代數界線",
            "| 1. 產業需求 |",
            "| 3. 客戶資格 |",
            "| 5. 收入與現金 |",
            "封裝與測試合計創造 94.69% 的營收增量",
            "| 毛利率 | 19.44% | 21.76% | ＋2.32 個百分點 |",
            "| 營業利益率 | 12.95% | 15.27% | ＋2.32 個百分點 |",
            "營業利益增加 7.70 億元，業外淨額卻減少 2.66 億元",
            "| 簡單現金差 | 負 24.45 | 正 13.28 |",
            "分別占當季 PP&E 增添 97.35% 與 91.73%",
            "簡單現金差由負 24.45 億元改善為正 13.28 億元",
            "四項淨效果為負 7.57 億元",
            "真正服務×產品×技術×客戶×訂單×收入×毛利×收現共同觀測 N＝0",
            "Python Decimal 與獨立 awk",
            "source_id: S30",
            "0fdf9f373bde7e7d6659bbd234596fa59ee7ea37b0a1a16a5d24e0665df6d439",
            "ad220e9985ca5b1d21b2b299603f9139b7be1c5164ce94b81ee48de32d3a950e",
            "a3fecadec18d7b3657fbbc1c5b046761e7344fd3f44a1de12617394d1e29e4b7",
            "claim_id: C32\nlabel: verified\nstatus: active",
            "claim_id: C33\nlabel: verified\nstatus: active",
            "claim_id: C34\nlabel: verified\nstatus: active",
            "claim_id: C35\nlabel: inference\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 30),
            ("research_claim", 35), ("metric_comparison", 12),
            ("impact", 6), ("monitoring_item", 12),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        scans = (
            ROOT / "notes" / "research_topics" / "scan_log.csv"
        ).read_text(encoding="utf-8")
        self.assertIn(
            "scan-2026-08-14-powertech-hbm-evidence-gates-and-capital-clocks",
            scans,
        )

    def test_yageo_q2_reconciles_fcf_ifrs_cash_and_management_cash(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-07-30_yageo_q2_earnings_call.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: profit_free_cash_flow_cash_stock_and_working_capital_ledgers_added_from_existing_deck_without_refreshing_thesis_clock",
            "reason: formal_q2_cash_flow_and_cash_definition_boundary_added_without_refreshing_revenue_thesis_clock",
            "## 淨利變好，現金不一定同速進來：四本帳與兩張現金調節橋",
            "### 第一帳：淨利與自由現金流要同期間、同公式對讀",
            "### 第二帳：期末現金大增，不等於營運現金同額流入",
            "### 第三帳：同一句「現金及約當現金」竟有兩個數字",
            "### 同一個現金名詞，必須帶十欄護照",
            "### 第四帳：營運資金要同時看絕對額與相對強度",
            "### 多空小作文必須共用同一組現金裁決欄位",
            "### 分母、誤差與限制",
            "公司簡報所列自由現金流",
            "H1 自由現金流 135.35521 億元",
            "四條流量精確相加的結果",
            "1,474.95485 億元",
            "2,000.78 億元",
            "相差 525.82515 億元",
            "2,007.17783 億元",
            "仍比\n簡報數字多 6.39783 億元",
            "投資淨流出的主要部分",
            "43,744",
            "48,274",
            "絕對額增加 45.30 億元",
            "應收帳款／營收 | 78.4% | 75.6%",
            "存貨／銷貨成本 | 139.9% | 130.2%",
            "應付帳款／銷貨成本 | 82.0% | 76.6%",
            "沒有 sampling SE／t",
            "cf0bc1a51edb3fc3fc0160310c7c903b36e3766ce80fb3eaa8d949bc0c4d9561",
            "4ace6c4735abd1edfe2b015062bf5b125f741217aac3e9142185f34cbddbcc2c",
            "Python Decimal 與獨立 awk 兩條路徑",
            "claim_id: C10",
            "claim_id: C11",
            "claim_id: C12",
            "claim_id: C13",
            "monitor_id: T3\nstatus: retired",
            "monitor_id: T4\nstatus: retired",
            "monitor_id: T5\nstatus: active",
            "monitor_id: T6\nstatus: active",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 5),
            ("research_claim", 13), ("metric_comparison", 0),
            ("impact", 1), ("monitoring_item", 6),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "concept:profit-fcf-cash-stock-ledgers,concept,淨利、自由現金流與現金存量三本帳",
            "metric:working-capital-intensity-proxy,metric,營運資金強度代理比率",
            "process:ifrs-management-cash-reconciliation-passport,process,IFRS 與管理現金口徑護照",
            "process:operating-investing-financing-cash-bridge,process,營業投資籌資現金流量橋",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "yageo_q2_financial_materiality.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 6)
        for node in (
            "edge_id: KG-YQ2-I02",
            "to_id: concept:profit-fcf-cash-stock-ledgers",
            "edge_id: KG-YQ2-I03",
            "to_id: metric:working-capital-intensity-proxy",
            "edge_id: KG-YQ2-I04",
            "to_id: process:ifrs-management-cash-reconciliation-passport",
            "edge_id: KG-YQ2-I05",
            "to_id: process:operating-investing-financing-cash-bridge",
        ):
            self.assertIn(node, graph)

        reviews = (
            ROOT / "notes" / "research_method_reviews" / "monitor_reviews.csv"
        ).read_text(encoding="utf-8")
        self.assertIn("MR-2026-08-14-YAGEO-T3-FORMAL-Q2-FILING", reviews)
        self.assertIn("MR-2026-08-14-YAGEO-T4-FCF-CASH-BRIDGE", reviews)

    def test_glass_substrate_thermomechanical_passport_preserves_measurement_boundary(self):
        topic = (
            ROOT / "notes" / "research_topics"
            / "2026-08-02_glass_substrate_commercialization.md"
        ).read_text(encoding="utf-8")
        for contract in (
            "reason: thermomechanical_passport_and_measurement_boundary_added_without_refreshing_thesis_clock",
            "## 低 CTE 不等於不翹曲：六欄熱機械資格護照",
            "| 1. 材料身分與性質 |",
            "| 2. 疊構與拘束 |",
            "| 3. 幾何與支撐 |",
            "| 4. 製程與環境歷史 |",
            "| 5. 量測契約 |",
            "| 6. 完整產品資格 |",
            "### 一個材料 CTE 範例，為何反而證明條件不能省",
            "### 多空小作文必須共用同一張熱機械表",
            "### 分母、誤差與限制",
            "120 °C 固化 8 小時",
            "三次 40–75 °C 循環",
            "89.9 µstrain/K",
            "99% 信賴區間",
            "strain uncertainty ±0.13% strain",
            "探頭 one-SD noise",
            "`N=2` 條消息鏈",
            "三次循環是同一量測內的重複歷史",
            "沒有可估玻璃產業或產品效果的 sampling SE／t",
            "6ec91c4bfb21958c6798fd935dc3ca61299025677fabdc24684e4ca7aea2349d",
            "9c9b7bf2c3a255c240ba33145f0fe4fce34c8fd8a42fb04ecf5a3250b27b6472",
            "官方 URL 已導向 404",
            "claim_id: C13",
            "claim_id: C14",
            "claim_id: C15",
            "claim_id: C16",
            "claim_id: C17",
        ):
            self.assertIn(contract, topic)
        for block, expected in (
            ("research_topic", 1), ("research_source", 16),
            ("research_claim", 17), ("metric_comparison", 0),
            ("impact", 3), ("monitoring_item", 4),
        ):
            self.assertEqual(topic.count(f"<!-- {block}"), expected)

        concepts = (ROOT / "config" / "knowledge_concepts.csv").read_text(
            encoding="utf-8"
        )
        for concept in (
            "process:glass-substrate-thermomechanical-passport,process,玻璃基板熱機械六欄資格護照",
            "metric:package-warpage-measurement-contract,metric,封裝翹曲量測契約",
        ):
            self.assertIn(concept, concepts)

        graph = (
            ROOT / "notes" / "knowledge_graph"
            / "glass_substrate_commercialization.md"
        ).read_text(encoding="utf-8")
        self.assertEqual(graph.count("<!-- knowledge_edge"), 22)
        for node in (
            "edge_id: KG-GLS-I15",
            "to_id: process:glass-substrate-thermomechanical-passport",
            "edge_id: KG-GLS-I16",
            "to_id: metric:package-warpage-measurement-contract",
        ):
            self.assertIn(node, graph)


if __name__ == "__main__":
    unittest.main()
