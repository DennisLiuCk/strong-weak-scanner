# -*- coding: utf-8 -*-
"""研究中心知識圖譜的 evidence contract 與 MVP 發布資料。"""
import re
import tempfile
import unittest
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import knowledge_graph as kg
import build_dashboard as bd


class KnowledgeGraphTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.topics, cls.notes = kg._load_default_context()
        cls.payload = kg.build_knowledge_graph(cls.topics, cls.notes, strict=True)

    def test_publishes_valid_hubs_and_two_separate_views(self):
        graphs = self.payload["graphs"]
        self.assertEqual(
            self.payload["stats"],
            {
                "graphs": len(graphs),
                "nodes": len({node["id"] for graph in graphs for node in graph["nodes"]}),
                "edges": sum(len(graph["edges"]) for graph in graphs),
                "financialAssessments": sum(
                    len(graph["financialAssessments"]) for graph in graphs),
            },
        )
        graph_ids = {graph["id"] for graph in graphs}
        self.assertEqual(len(graph_ids), len(graphs))
        registered_ids = set()
        for path in (ROOT / "notes" / "knowledge_graph").glob("*.md"):
            if path.name.startswith("_"):
                continue
            match = re.search(
                r"<!-- knowledge_graph_meta\s+(.*?)-->",
                path.read_text(encoding="utf-8"),
                re.DOTALL,
            )
            self.assertIsNotNone(match, path.name)
            fields = dict(
                line.split(":", 1)
                for line in match.group(1).splitlines()
                if ":" in line
            )
            if fields.get("status", "").strip() == "active":
                registered_ids.add(fields["graph_id"].strip())
        self.assertEqual(graph_ids, registered_ids)
        self.assertGreater(len(graphs), 0)
        topic_article_ids = {f"topic-{topic['topic_id']}" for topic in self.topics}
        for graph in graphs:
            self.assertTrue(graph["articleIds"], graph["id"])
            self.assertTrue(
                set(graph["articleIds"]).issubset(topic_article_ids),
                graph["id"],
            )
            self.assertEqual({edge["view"] for edge in graph["edges"]},
                             {"company", "industry"})
            for edge in graph["edges"]:
                self.assertIn(graph["rootNodeId"], {edge["from"], edge["to"]})

    def test_reader_learning_routes_cover_every_active_graph_once(self):
        graph_ids = {graph["id"] for graph in self.payload["graphs"]}
        graph_by_id = {graph["id"]: graph for graph in self.payload["graphs"]}
        routed_ids = [
            graph_id
            for route in bd.RESEARCH_LEARNING_ROUTES
            for graph_id in route["graphIds"]
        ]
        self.assertEqual(len(routed_ids), len(set(routed_ids)))
        self.assertEqual(set(routed_ids), graph_ids)
        self.assertTrue(all(route["description"] for route in bd.RESEARCH_LEARNING_ROUTES))
        primary_articles = [graph_by_id[graph_id]["articleIds"][0] for graph_id in routed_ids]
        self.assertEqual(len(primary_articles), len(set(primary_articles)))

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

    def test_financial_materiality_v2_separates_denominator_from_topic_attribution(self):
        assessments = [
            item for graph in self.payload["graphs"]
            for item in graph["financialAssessments"]
        ]
        self.assertEqual(
            {item["id"] for item in assessments},
            {"FM-YQ2-2327-01", "FM-LC-3017-01", "FM-LC-2308-01", "FM-LC-2301-01"},
        )
        self.assertEqual(
            self.payload["stats"]["financialAssessments"], len(assessments),
        )
        for item in assessments:
            self.assertEqual(item["contractVersion"], 2)
            self.assertTrue(item["metricDefinition"], item["id"])
            self.assertTrue(item["denominatorDefinition"], item["id"])
            self.assertTrue(item["sourceRefs"], item["id"])
            self.assertTrue(item["boundary"], item["id"])
            self.assertTrue(item["nextTrigger"], item["id"])
        yageo = next(item for item in assessments if item["id"] == "FM-YQ2-2327-01")
        self.assertEqual(yageo["financialScope"], "company_total")
        self.assertEqual(yageo["attributionStatus"], "not_disclosed")
        self.assertEqual(yageo["sharePercent"], "")
        proxies = [item for item in assessments if item["attributionStatus"] == "bounded_proxy"]
        self.assertEqual(len(proxies), 3)
        self.assertTrue(all(item["financialScope"] in {"segment", "product"}
                            for item in proxies))
        self.assertTrue(all(item["sharePercent"] for item in proxies))
        self.assertFalse(any(
            edge["materiality"] == "financial"
            for graph in self.payload["graphs"] for edge in graph["edges"]
        ))

    def test_v2_lint_rejects_company_total_as_direct_topic_revenue(self):
        errors = []
        nodes = kg.load_nodes(errors)
        edge = {
            "id": "E-FIN", "status": "active", "view": "company",
            "from": "company:2327", "to": "concept:yageo-q2-financial-materiality",
            "evidenceState": "verified", "commercialStage": "financial",
            "materiality": "financial", "sources": [{"ref": "QUAL-2327#S1"}],
        }
        fields = {
            "contract_version": "2", "assessment_id": "FM-INVALID", "edge_id": "E-FIN",
            "financial_scope": "company_total", "metric": "consolidated_revenue",
            "value_kind": "reported", "reported_value": "100", "unit": "TWD_100m",
            "period_start": "2026-01-01", "period_end": "2026-03-31",
            "period_basis": "quarter", "denominator_metric": "consolidated_revenue",
            "denominator_value": "100", "denominator_unit": "TWD_100m",
            "share_percent": "100", "attribution_status": "direct",
            "source_refs": "QUAL-2327#S1", "calculation": "",
            "as_of": "2026-05-01", "review_due": "2026-06-01", "status": "active",
            "metric_definition": "公司總營收", "denominator_definition": "公司總營收",
            "boundary": "不得視為題材收入", "next_trigger": "等待產品揭露",
        }
        kg._financial_materiality_payload(fields, "test assessment", {"E-FIN": edge}, nodes, errors)
        self.assertIn("test assessment direct 不得使用 company_total scope", errors)

    def test_financial_edge_cannot_publish_without_active_v2_direct_assessment(self):
        source = """# test
<!-- knowledge_graph_meta
schema_version: 1
graph_id: test-financial-gate
root_node_id: concept:yageo-q2-financial-materiality
label: test
summary: test
article_ids: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL
status: active
-->
<!-- knowledge_edge
edge_id: TEST-FIN-C01
view: company
from_id: company:2327
to_id: concept:yageo-q2-financial-materiality
relation: reports_financials
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C5
note_refs:
evidence_state: verified
commercial_stage: financial
materiality: financial
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-23
status: active
boundary: test boundary
next_trigger: test trigger
-->
<!-- knowledge_edge
edge_id: TEST-FIN-I01
view: industry
from_id: concept:yageo-q2-financial-materiality
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL#C5
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-09
review_due: 2026-08-23
status: active
boundary: test boundary
next_trigger: test trigger
-->
"""
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "test.md").write_text(source, encoding="utf-8")
            payload = kg.build_knowledge_graph(
                self.topics, self.notes, graph_dir=tmp, strict=False,
            )
        self.assertTrue(any(
            "financial materiality 缺少 active v2 direct assessment" in error
            for error in payload["errors"]
        ))

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
