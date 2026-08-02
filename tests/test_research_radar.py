# -*- coding: utf-8 -*-
"""候選研究雷達的排序、升格路由與證據契約。"""
import sys
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
        self.assertEqual(
            self.payload["stats"],
            {
                "candidates": 5,
                "promoted": 2,
                "highKnowledge": 4,
                "selectionFrozen": 5,
                "selectedAdvance": 2,
                "selectedWatch": 2,
                "selectedDefer": 1,
            },
        )
        self.assertEqual(
            [row["rank"] for row in self.payload["candidates"]],
            list(range(1, 6)),
        )
        self.assertEqual(self.payload["schemaVersion"], 2)
        self.assertEqual(self.payload["selectionCycleId"], "RS-2026-08-03-01")
        self.assertEqual(self.payload["asOf"], "2026-08-03")
        self.assertGreater(self.payload["nextReview"], self.payload["asOf"])

    def test_top_two_are_promoted_to_articles_and_graphs(self):
        top_two = self.payload["candidates"][:2]
        self.assertEqual(
            [row["id"] for row in top_two],
            ["RC-CUSTOM-HBM", "RC-PCIE6-COMPLIANCE"],
        )
        for row in top_two:
            self.assertEqual(row["priority"], "p1")
            self.assertEqual(row["knowledgeValue"], "high")
            self.assertEqual(row["status"], "promoted")
            self.assertEqual(row["selectionDecision"], "advance")
            self.assertEqual(row["selectionOutcome"], "promoted_after_research")
            self.assertTrue(row["articleId"])
            self.assertTrue(row["graphId"])
            self.assertGreaterEqual(len(row["sources"]), 2)

    def test_watch_and_deferred_candidates_are_not_forced_into_articles_or_graphs(self):
        for row in self.payload["candidates"][2:]:
            self.assertIn(row["status"], {"watch", "deferred"})
            self.assertFalse(row["articleId"])
            self.assertFalse(row["graphId"])

    def test_frozen_selection_fields_are_exposed_without_rewriting(self):
        frozen = {row["candidate_id"]: row for row in self.payload["selectionLog"]}
        self.assertEqual(len(frozen), 5)
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


if __name__ == "__main__":
    unittest.main()
