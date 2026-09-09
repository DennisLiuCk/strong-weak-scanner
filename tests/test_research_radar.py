# -*- coding: utf-8 -*-
"""候選研究雷達的排序、升格路由與證據契約。"""
import csv
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import research_radar


class ResearchRadarTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        topic_ids, graph_ids = research_radar._default_refs()
        cls.payload = research_radar.load_research_radar(
            topic_ids=topic_ids,
            graph_ids=graph_ids,
            strict=True,
        )

    def test_active_radar_is_complete_and_ranked_without_gaps(self):
        candidates = self.payload["candidates"]
        selection_log = self.payload["selectionLog"]
        expected_stats = {
            "candidates": len(candidates),
            "promoted": sum(row["status"] == "promoted" for row in candidates),
            "expanded": sum(row["status"] == "expand_existing" for row in candidates),
            "highKnowledge": sum(
                row["knowledgeValue"] == "high" for row in candidates
            ),
            "selectionFrozen": len(selection_log),
            "selectedAdvance": sum(
                row["selection_decision"] == "advance" for row in selection_log
            ),
            "selectedWatch": sum(
                row["selection_decision"] == "watch" for row in selection_log
            ),
            "selectedDefer": sum(
                row["selection_decision"] == "defer" for row in selection_log
            ),
        }
        self.assertEqual(self.payload["stats"], expected_stats)
        # 每輪候選數本來就會變；要驗的是雷達與凍結帳本逐一對應且排名連續，
        # 不是某一輪的固定張數。寫死張數只會讓每次發佈都得改測試。
        self.assertGreaterEqual(len(candidates), 1)
        self.assertEqual(len(candidates), len(selection_log))
        self.assertEqual(
            [row["rank"] for row in candidates],
            list(range(1, len(candidates) + 1)),
        )
        self.assertEqual(self.payload["schemaVersion"], 2)
        self.assertTrue(self.payload["selectionCycleId"].startswith("RS-"))
        self.assertEqual(
            {row["cycle_id"] for row in selection_log},
            {self.payload["selectionCycleId"]},
        )
        self.assertGreater(self.payload["nextReview"], self.payload["asOf"])

    def test_promotion_is_evidence_gated_not_a_fixed_top_n_quota(self):
        promoted = [
            row for row in self.payload["candidates"] if row["status"] == "promoted"
        ]
        for row in promoted:
            self.assertEqual(row["route"], "article_and_graph")
            self.assertTrue(row["articleId"])
            self.assertTrue(row["graphId"])
            self.assertEqual(row["evidencePosture"], "research_grade")
            self.assertGreaterEqual(len(row["sources"]), 2)
        advance = [
            row for row in self.payload["candidates"]
            if row["selectionDecision"] == "advance"
        ]
        for row in advance:
            self.assertIn(
                row["selectionOutcome"],
                {"promoted_after_research", "expanded_after_research",
                 "rejected_after_research"},
            )

    def test_watch_and_deferred_candidates_are_not_forced_into_articles_or_graphs(self):
        for row in self.payload["candidates"]:
            if row["status"] == "promoted":
                continue
            self.assertIn(row["status"], {"expand_existing", "watch", "deferred"})
            if row["status"] == "expand_existing":
                self.assertEqual(row["route"], "expand_existing_article")
                self.assertTrue(row["articleId"])
            else:
                self.assertIn(row["route"], {"watch_only", "fold_into_graph"})
                self.assertFalse(row["articleId"])
                self.assertEqual(bool(row["graphId"]), row["route"] == "fold_into_graph")

    def test_frozen_selection_fields_are_exposed_without_rewriting(self):
        frozen = {row["candidate_id"]: row for row in self.payload["selectionLog"]}
        self.assertEqual(len(frozen), len(self.payload["candidates"]))
        for row in self.payload["candidates"]:
            original = frozen[row["id"]]
            self.assertEqual(row["rank"], original["rank"])
            self.assertEqual(row["priority"], original["priority"])
            self.assertEqual(row["knowledgeValue"], original["knowledge_value"])
            self.assertEqual(row["firstRejection"], original["first_rejection"])
            self.assertEqual(row["nextEvidence"], original["next_evidence"])
            self.assertEqual(row["selectedAt"], original["selected_at"])

    def test_selection_parser_rejects_non_taipei_or_gapped_cycle(self):
        text = (
            ",".join(research_radar.SELECTION_HEADER) + "\n"
            "RS-2026-08-03-99-A,RS-2026-08-03-99,2026-08-03T00:00:00Z,"
            "RC-A,2,p1,high,preliminary,advance,reason,reject,next\n"
        )
        _, errors = research_radar._read_selection_text(text)
        self.assertTrue(any("+08:00" in error for error in errors))
        self.assertTrue(any("rank 必須由 1 連續排列" in error for error in errors))

    def test_every_candidate_has_rejection_and_next_evidence(self):
        for row in self.payload["candidates"]:
            self.assertTrue(row["firstRejection"], row["id"])
            self.assertTrue(row["nextEvidence"], row["id"])
            self.assertGreater(row["nextCheck"], self.payload["asOf"])
            self.assertGreaterEqual(len(row["sources"]), 2, row["id"])

    def test_active_candidates_have_a_plain_language_reader_layer(self):
        for row in self.payload["candidates"]:
            self.assertTrue(row["readerQuestion"].endswith(("？", "?")), row["id"])
            self.assertTrue(row["readerStartingPoint"], row["id"])
            self.assertEqual(row["readerStartingPoint"].count("。"), 2, row["id"])
            self.assertIn("目前還", row["readerStartingPoint"], row["id"])
            self.assertTrue(row["readerNextStep"], row["id"])
            self.assertGreaterEqual(len(row["readerTerms"]), 2, row["id"])
            self.assertLessEqual(len(row["readerTerms"]), 4, row["id"])
            terms = [item["term"] for item in row["readerTerms"]]
            self.assertEqual(len(terms), len(set(terms)), row["id"])
            self.assertTrue(all(item["explanation"] for item in row["readerTerms"]))
            self.assertGreaterEqual(len(row["groupIds"]), 1, row["id"])
            self.assertLessEqual(len(row["groupIds"]), 4, row["id"])
            self.assertEqual(len(row["groupIds"]), len(set(row["groupIds"])), row["id"])
            group_questions = row["readerGroupQuestions"]
            self.assertEqual(
                [item["groupId"] for item in group_questions],
                row["groupIds"],
                row["id"],
            )
            self.assertTrue(
                all(item["question"].endswith(("？", "?")) for item in group_questions),
                row["id"],
            )

        errors = []
        self.assertEqual(
            research_radar._reader_terms(
                "EMC => 電磁相容 | chamber => 專用測試室",
                "candidate",
                errors,
            ),
            [
                {"term": "EMC", "explanation": "電磁相容"},
                {"term": "chamber", "explanation": "專用測試室"},
            ],
        )
        self.assertEqual(errors, [])

        starting_point_errors = []
        research_radar._reader_starting_point(
            "零件通過單體測試，不代表整個系統一定合格。目前還缺整機驗收條件與可重複測試結果。",
            "candidate",
            starting_point_errors,
        )
        self.assertEqual(starting_point_errors, [])
        invalid_starting_point_errors = []
        research_radar._reader_starting_point(
            "這題已經可以直接下結論。",
            "candidate",
            invalid_starting_point_errors,
        )
        self.assertTrue(
            any("已知線索＋目前缺口" in error for error in invalid_starting_point_errors)
        )
        self.assertTrue(
            any("目前還" in error for error in invalid_starting_point_errors)
        )

        errors = []
        self.assertEqual(
            research_radar._candidate_group_ids(
                "passive,powersupply,serverodm", "candidate", errors,
            ),
            ["passive", "powersupply", "serverodm"],
        )
        self.assertEqual(errors, [])
        invalid_errors = []
        research_radar._candidate_group_ids(
            "passive,not-a-formal-group", "candidate", invalid_errors,
        )
        self.assertTrue(any("不在正式族群" in error for error in invalid_errors))

        question_errors = []
        self.assertEqual(
            research_radar._candidate_group_questions(
                "passive => 零件要回答什麼？ | powersupply => 系統要回答什麼？",
                ["passive", "powersupply"],
                "candidate",
                question_errors,
            ),
            [
                {"groupId": "passive", "question": "零件要回答什麼？"},
                {"groupId": "powersupply", "question": "系統要回答什麼？"},
            ],
        )
        self.assertEqual(question_errors, [])
        mismatched_errors = []
        research_radar._candidate_group_questions(
            "powersupply => 系統要回答什麼？ | passive => 零件要回答什麼？",
            ["passive", "powersupply"],
            "candidate",
            mismatched_errors,
        )
        self.assertTrue(any("依 group_ids 順序" in error for error in mismatched_errors))

    def test_retired_schema2_radars_remain_accountable(self):
        stats = self.payload["historyStats"]
        self.assertGreater(stats["schema2Cycles"], 1)
        self.assertEqual(
            stats["accountableSchema2Cycles"], stats["schema2Cycles"],
        )
        self.assertGreater(
            stats["candidates"], self.payload["stats"]["candidates"],
        )
        for item in self.payload["history"]:
            if item["schemaVersion"] == 2:
                self.assertTrue(item["accountable"], item["id"])

    def test_historical_watch_expansion_is_not_reported_as_unchanged(self):
        cycle = next(item for item in self.payload["history"]
                     if item["cycleId"] == "RS-2026-08-03-03")
        candidate = next(row for row in cycle["candidates"]
                         if row["id"] == "RC-AI-POWER-TELEMETRY")
        self.assertEqual(candidate["selectionDecision"], "watch")
        self.assertEqual(candidate["selectionOutcome"], "expanded_from_watch")
        self.assertEqual(candidate["evidencePosture"], "preliminary")
        frozen = next(row for row in cycle["selectionLog"]
                      if row["candidate_id"] == candidate["id"])
        self.assertEqual(frozen["selection_decision"], "watch")

    def test_early_reselection_requires_a_new_frozen_source_after_cutover(self):
        required = [
            row for row in self.payload["earlyReselections"] if row["required"]
        ]
        self.assertGreaterEqual(len(required), 1)
        self.assertTrue(all(row["valid"] for row in required))
        self.assertEqual(
            self.payload["historyStats"]["documentedEarlyTriggers"],
            len(required),
        )
        self.assertGreaterEqual(
            self.payload["historyStats"]["grandfatheredEarlyReselections"], 1,
        )
        valid = research_radar._early_trigger(
            "early_trigger:New spec@2026-08-01=>https://example.com/new；reason",
            "2026-08-07",
            {"https://example.com/old"},
        )
        repeated = research_radar._early_trigger(
            "early_trigger:Old spec@2026-08-01=>https://example.com/old；reason",
            "2026-08-07",
            {"https://example.com/old"},
        )
        self.assertTrue(valid["valid"])
        self.assertFalse(repeated["valid"])


class ResearchRadarOutcomeTest(unittest.TestCase):
    def load_cases(self, cases, *, overrides=None, strict=True):
        """Exercise outcome classification through the real frozen-ledger loader."""
        cycle = "RS-2026-09-10-99"
        meta = {
            "schema_version": "2", "radar_id": "RADAR-2026-09-10-99",
            "as_of": "2026-09-10", "next_review": "2026-10-01",
            "status": "active", "method": "檢驗凍結選擇與研究結果的對應",
            "selection_cycle_id": cycle,
        }
        blocks = ["<!-- research_radar\n" + "\n".join(
            f"{key}: {value}" for key, value in meta.items()) + "\n-->"]
        selections = []
        for rank, (decision, status) in enumerate(cases, 1):
            fields = {
                "candidate_id": f"RC-OUTCOME-{rank}", "rank": str(rank),
                "title": "同一問題的研究結果", "priority": "p1",
                "knowledge_value": "high", "status": status,
                "evidence_posture": "research_grade" if status == "promoted" else "preliminary",
                "why_now": "已有一手文件可回查，仍需核對採用範圍。",
                "knowledge_gain": "分開公開規格與量產部署",
                "first_rejection": "沒有共同量測分母就不外推",
                "next_evidence": "下一季公司公開資料", "next_check": "2026-10-01",
                "route": {"promoted": "article_and_graph",
                          "expand_existing": "expand_existing_article"}.get(status, "watch_only"),
                "sources": "公司文件 => https://example.com/company | 規格 => https://example.org/spec",
                "reader_question": "公開規格能說明部署嗎？",
                "reader_starting_point": "一手文件已經說明公開規格，可以先確認系統的位置。目前還缺同一場址的部署與量測分母。",
                "reader_terms": "規格 => 公開要求 | 部署 => 實際投入使用",
                "reader_next_step": "比對公司文件與公開規格",
                "group_ids": "passive", "reader_group_questions": "passive => 元件在哪個位置？",
            }
            if status in {"promoted", "expand_existing"}:
                fields["article_topic_id"] = "MI-2026-09-10-OUTCOME"
            if status == "promoted":
                fields["graph_id"] = "outcome"
            fields.update(overrides or {})
            blocks.append("<!-- research_candidate\n" + "\n".join(
                f"{key}: {value}" for key, value in fields.items()) + "\n-->")
            selections.append({
                "selection_id": f"{cycle}-{rank}", "cycle_id": cycle,
                "selected_at": "2026-09-10T09:00:00+08:00",
                "candidate_id": fields["candidate_id"], "rank": rank,
                "priority": fields["priority"], "knowledge_value": fields["knowledge_value"],
                "evidence_posture": "preliminary", "selection_decision": decision,
                "selection_reason": "研究前已凍結的選擇理由",
                "first_rejection": fields["first_rejection"], "next_evidence": fields["next_evidence"],
            })
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)
            (path / "radar.md").write_text("\n".join(blocks) + "\n", encoding="utf-8")
            with (path / "selection_log.csv").open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=research_radar.SELECTION_HEADER,
                                        lineterminator="\n")
                writer.writeheader()
                writer.writerows(selections)
            return research_radar.load_research_radar(
                str(path), topic_ids={"MI-2026-09-10-OUTCOME"}, graph_ids={"outcome"},
                strict=strict,
            )

    def test_completed_and_uncompleted_outcomes_keep_the_frozen_decision(self):
        cases = [
            ("advance", "promoted", "promoted_after_research"),
            ("advance", "expand_existing", "expanded_after_research"),
            ("advance", "watch", "rejected_after_research"),
            ("advance", "deferred", "rejected_after_research"),
            ("watch", "promoted", "promoted_from_watch"),
            ("watch", "expand_existing", "expanded_from_watch"),
            ("watch", "watch", "remained_watch"),
            ("watch", "deferred", "deferred_from_watch"),
            ("defer", "promoted", "promoted_from_defer"),
            ("defer", "expand_existing", "expanded_from_defer"),
            ("defer", "watch", "watched_from_defer"),
            ("defer", "deferred", "remained_deferred"),
        ]
        payload = self.load_cases([(decision, status) for decision, status, _ in cases])
        for row, (decision, status, expected) in zip(payload["candidates"], cases):
            with self.subTest(decision=decision, status=status):
                self.assertEqual(row["selectionOutcome"], expected)
                self.assertEqual(row["selectionDecision"], decision)
                self.assertEqual(row["initialEvidencePosture"], "preliminary")
        self.assertTrue(payload["history"][0]["accountable"])

    def test_a_whole_cycle_can_expand_without_new_articles_or_graphs(self):
        payload = self.load_cases([("advance", "expand_existing")] * 3)
        self.assertEqual(payload["stats"]["expanded"], 3)
        self.assertEqual(payload["stats"]["promoted"], 0)
        for row in payload["candidates"]:
            self.assertEqual(row["selectionOutcome"], "expanded_after_research")
            self.assertTrue(row["articleId"])
            self.assertFalse(row["graphId"])
            self.assertEqual(row["evidencePosture"], "preliminary")

    def test_result_routes_still_require_their_references_and_sources(self):
        for status, overrides, error in (
            ("expand_existing", {"article_topic_id": ""}, "必須提供 article_topic_id"),
            ("promoted", {"graph_id": ""}, "promoted 必須同時連到文章與圖譜"),
            ("watch", {"route": "fold_into_graph"}, "必須提供 graph_id"),
            ("deferred", {"sources": "一份文件 => https://example.com/only"}, "至少需要兩個"),
        ):
            with self.subTest(status=status):
                payload = self.load_cases([("advance", status)], overrides=overrides, strict=False)
                self.assertTrue(any(error in item for item in payload["errors"]))


if __name__ == "__main__":
    unittest.main()
