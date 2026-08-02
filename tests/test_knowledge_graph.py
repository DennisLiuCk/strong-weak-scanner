# -*- coding: utf-8 -*-
"""研究中心知識圖譜的 evidence contract 與 MVP 發布資料。"""
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import knowledge_graph as kg


class KnowledgeGraphTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.topics, cls.notes = kg._load_default_context()
        cls.payload = kg.build_knowledge_graph(cls.topics, cls.notes, strict=True)

    def test_publishes_nine_valid_hubs_and_two_separate_views(self):
        self.assertEqual(self.payload["stats"], {"graphs": 9, "nodes": 117, "edges": 133})
        self.assertEqual(
            {graph["id"] for graph in self.payload["graphs"]},
            {
                "hbm", "liquid-cooling", "amd-helios", "backside-power",
                "ai-memory-hierarchy", "open-ai-fabrics",
                "cpo-networking", "hybrid-bonding", "panel-level-packaging",
            },
        )
        for graph in self.payload["graphs"]:
            self.assertEqual({edge["view"] for edge in graph["edges"]},
                             {"company", "industry"})
            for edge in graph["edges"]:
                self.assertIn(graph["rootNodeId"], {edge["from"], edge["to"]})

    def test_every_edge_preserves_evidence_boundary_clock_and_monitoring_trigger(self):
        for graph in self.payload["graphs"]:
            for edge in graph["edges"]:
                self.assertTrue(edge["claimRefs"] or edge["noteRefs"], edge["id"])
                if edge["evidenceState"] != "unverified":
                    self.assertTrue(edge["sources"], edge["id"])
                self.assertTrue(edge["boundary"], edge["id"])
                self.assertTrue(edge["nextTrigger"], edge["id"])
                self.assertRegex(edge["asOf"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertRegex(edge["reviewDue"], r"^\d{4}-\d{2}-\d{2}$")
                self.assertLessEqual(edge["asOf"], edge["reviewDue"])
                self.assertIn(edge["evidenceState"], kg.EVIDENCE_STATES)

    def test_company_nodes_distinguish_universe_from_external_entities(self):
        hbm = next(graph for graph in self.payload["graphs"] if graph["id"] == "hbm")
        nodes = {node["id"]: node for node in hbm["nodes"]}
        self.assertTrue(nodes["company:3443"]["universe"])
        self.assertEqual(nodes["company:3443"]["ticker"], "3443")
        self.assertFalse(nodes["company:micron"]["universe"])
        self.assertEqual(nodes["company:micron"]["ticker"], "MU")

    def test_strength_never_silently_promotes_financial_or_exclusive_exposure(self):
        edges = [edge for graph in self.payload["graphs"] for edge in graph["edges"]]
        for edge in edges:
            if edge["materiality"] == "financial":
                self.assertEqual(edge["evidenceState"], "verified")
                self.assertEqual(edge["commercialStage"], "financial")
            if edge["exclusivity"] != "unknown":
                self.assertTrue(edge["exclusivityScope"], edge["id"])
                self.assertNotEqual(edge["evidenceState"], "unverified")
        microsoft = next(edge for edge in edges if edge["id"] == "KG-HEL-C02")
        self.assertEqual(microsoft["exclusivity"], "multi_source")

    def test_lint_rejects_unverified_exclusivity_claim(self):
        errors = []
        nodes = kg.load_nodes(errors)
        topic_by_id, claim_by_ref = kg._topic_maps(self.topics)
        fields = {
            "edge_id": "INVALID-COMPANY", "view": "company",
            "from_id": "company:micron", "to_id": "concept:hbm",
            "relation": "produces",
            "claim_refs": "MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE#C3",
            "note_refs": "", "evidence_state": "unverified",
            "commercial_stage": "production", "materiality": "named_product",
            "exclusivity": "sole_source", "exclusivity_scope": "全球供應",
            "as_of": "2026-08-01", "review_due": "2026-08-15",
            "status": "active", "boundary": "不應發布",
            "next_trigger": "等待一手證據",
        }
        kg._edge_payload(
            fields, "test edge", nodes, topic_by_id, claim_by_ref, self.notes,
            {"MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE"}, errors,
        )
        self.assertIn("test edge unverified edge 不得宣稱供應集中度", errors)


if __name__ == "__main__":
    unittest.main()
