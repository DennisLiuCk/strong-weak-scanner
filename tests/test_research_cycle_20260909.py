# -*- coding: utf-8 -*-
"""Recorded September evidence corrections must not refresh thesis clocks."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_dashboard as bd


def blocks(text, kind):
    return [dict(line.strip().split(":", 1) for line in body.splitlines() if ":" in line)
            for body in re.findall(r"<!-- " + kind + r"\s*\n(.*?)-->", text, re.S)]


def records(text, kind):
    return [{k.strip(): v.strip() for k, v in row.items()} for row in blocks(text, kind)]


class SeptemberResearchCycleTest(unittest.TestCase):
    def test_cpo_correction_preserves_original_monitor_contract_and_edge_dates(self):
        text = (ROOT / "notes/research_topics/2026-08-01_cpo_pluggable_coexistence.md").read_text(encoding="utf8")
        claims = {c["claim_id"]: c for c in records(text, "research_claim")}
        self.assertEqual(claims["C1"]["status"], "superseded")
        self.assertEqual(claims["C1"]["corrected_by_claim_id"], "C24")
        self.assertIn("now in production", claims["C24"]["claim"])
        monitors = {m["monitor_id"]: m for m in records(text, "monitoring_item")}
        self.assertEqual(monitors["T3"]["status"], "retired")
        for field in ("metric", "trigger", "invalidation", "next_check", "frequency"):
            self.assertEqual(monitors["T5"][field], monitors["T3"][field])
        graph = (ROOT / "notes/knowledge_graph/cpo_networking.md").read_text(encoding="utf8")
        corrected = [e for e in records(graph, "knowledge_edge") if e["claim_refs"].endswith("#C24")]
        self.assertEqual(len(corrected), 4)
        for edge in corrected:
            self.assertEqual(edge["as_of"], "2026-05-31")
            self.assertEqual(edge["review_due"], "2026-08-26")

    def test_mpi_company_denominator_does_not_become_ai_materiality(self):
        text = (ROOT / "notes/knowledge_graph/inference_compute_test_demand.md").read_text(encoding="utf8")
        edge = next(e for e in records(text, "knowledge_edge") if e["edge_id"] == "KG-ITD-C06")
        financial = next(f for f in records(text, "financial_materiality") if f["assessment_id"] == "FM-ITD-6223-01")
        self.assertEqual(edge["materiality"], "adjacent")
        self.assertEqual(financial["attribution_status"], "not_disclosed")
        self.assertEqual(financial["financial_scope"], "company_total")
        self.assertEqual(financial["reported_value"], "5233387")
        self.assertEqual(financial["unit"], "TWD_thousand")
        self.assertEqual(financial["share_percent"], "")

    def test_both_article_revisions_reach_recent_feed_with_old_thesis_dates(self):
        topics = []
        for filename, expected_clock, expected_due, reason in (
            ("2026-08-01_cpo_pluggable_coexistence.md", "2026-08-12", "2026-08-26",
             "narrow_spectrum_x_production_wording_to_original_subject_without_refreshing_thesis_clock"),
            ("2026-08-01_inference_compute_tester_tam.md", "2026-08-14", "2026-08-15",
             "add_mpi_q2_product_mix_and_same_period_denominator_without_ai_attribution_or_clock_refresh"),
            ("2026-07-29_priority_q2_disclosures.md", "2026-08-12", "2026-08-15",
             "recorded_tonghsing_english_q2_attachment_delta_without_claiming_content_verification"),
        ):
            text = (ROOT / "notes/research_topics" / filename).read_text(encoding="utf8")
            meta = records(text, "research_topic")[0]
            transition = next(t for t in records(text, "transition") if t["reason"] == reason)
            self.assertEqual(meta["last_reviewed_at"], expected_clock)
            self.assertEqual(meta["review_due"], expected_due)
            topics.append({"topic_id": meta["topic_id"], "title": meta["topic_id"],
                           "relpath": "notes/research_topics/" + filename,
                           "meta": meta, "transitions": [transition]})
        recent = bd.build_recent_articles("2026-09-08", {}, {}, topics=topics)
        self.assertEqual(recent["anchor"], "2026-09-09")
        self.assertEqual({item["researchId"] for item in recent["items"]},
                         {"topic-" + t["topic_id"] for t in topics})


if __name__ == "__main__":
    unittest.main()
