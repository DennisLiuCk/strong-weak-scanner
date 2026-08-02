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
            {"candidates": 9, "promoted": 9, "highKnowledge": 9},
        )
        self.assertEqual(
            [row["rank"] for row in self.payload["candidates"]],
            list(range(1, 10)),
        )
        self.assertEqual(self.payload["asOf"], "2026-08-02")
        self.assertGreater(self.payload["nextReview"], self.payload["asOf"])

    def test_top_three_are_promoted_to_articles_and_graphs(self):
        top_three = self.payload["candidates"][:3]
        self.assertEqual(
            [row["id"] for row in top_three],
            ["RC-GLASS-SUBSTRATE", "RC-UCIE-3", "RC-800V-WBG"],
        )
        for row in top_three:
            self.assertEqual(row["priority"], "p1")
            self.assertEqual(row["knowledgeValue"], "high")
            self.assertEqual(row["status"], "promoted")
            self.assertTrue(row["articleId"])
            self.assertTrue(row["graphId"])
            self.assertGreaterEqual(len(row["sources"]), 2)

    def test_every_candidate_has_rejection_and_next_evidence(self):
        for row in self.payload["candidates"]:
            self.assertTrue(row["firstRejection"], row["id"])
            self.assertTrue(row["nextEvidence"], row["id"])
            self.assertGreater(row["nextCheck"], self.payload["asOf"])
            self.assertGreaterEqual(len(row["sources"]), 2, row["id"])


if __name__ == "__main__":
    unittest.main()
