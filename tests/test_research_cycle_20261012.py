"""October 12: current list capture is not new deployment or a refreshed clock."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_dashboard as bd

TOPIC = "notes/research_topics/2026-08-03_pcie6_compliance_ladder.md"
GRAPH = "notes/knowledge_graph/pcie6_compliance_ladder.md"
RADAR = "notes/research_candidates/2026-09-13_verification_gaps.md"
# Starting due cohort, frozen before changing any review dates (40 tasks).
DUE = [
    [
        "MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP",
        "T3"
    ],
    [
        "MI-2026-07-29-PRIORITY-Q2-DISCLOSURES",
        "T9"
    ],
    [
        "MI-2026-07-30-YAGEO-Q2-EARNINGS-CALL",
        "T5"
    ],
    [
        "MI-2026-07-31-MISSED-PRIORITY-Q2",
        "T11"
    ],
    [
        "MI-2026-08-01-800VDC-EXECUTION-READINESS",
        "T3"
    ],
    [
        "MI-2026-08-01-AI-CAPEX-CASH-CONVERSION",
        "T5"
    ],
    [
        "MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE",
        "T4"
    ],
    [
        "MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER",
        "T6"
    ],
    [
        "MI-2026-08-02-BACKSIDE-POWER-DELIVERY",
        "T7"
    ],
    [
        "MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION",
        "T3"
    ],
    [
        "MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER",
        "T4"
    ],
    [
        "MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER",
        "T5"
    ],
    [
        "MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER",
        "T6"
    ],
    [
        "MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER",
        "T7"
    ],
    [
        "MI-2026-08-02-OPEN-AI-FABRICS",
        "T5"
    ],
    [
        "MI-2026-08-03-800VDC-PROTECTION-LAYERS",
        "T1"
    ],
    [
        "MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES",
        "T1"
    ],
    [
        "MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES",
        "T2"
    ],
    [
        "MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES",
        "T3"
    ],
    [
        "MI-2026-08-03-PCIE6-COMPLIANCE-LADDER",
        "T7"
    ],
    [
        "MI-2026-08-03-PCIE6-COMPLIANCE-LADDER",
        "T9"
    ],
    [
        "MI-2026-08-07-AI-RACK-ACTION-CONTRACT",
        "T1"
    ],
    [
        "MI-2026-08-07-AI-RACK-ACTION-CONTRACT",
        "T2"
    ],
    [
        "MI-2026-08-07-AI-RACK-ACTION-CONTRACT",
        "T3"
    ],
    [
        "MI-2026-08-07-AI-RACK-ACTION-CONTRACT",
        "T4"
    ],
    [
        "MI-2026-08-08-AI-RACK-TRUST-ROOT",
        "T1"
    ],
    [
        "MI-2026-08-09-AI-RACK-EMC-CERTIFICATION",
        "T1"
    ],
    [
        "MI-2026-08-09-AI-RACK-EMC-CERTIFICATION",
        "T2"
    ],
    [
        "MI-2026-08-09-AI-RACK-EMC-CERTIFICATION",
        "T3"
    ],
    [
        "MI-2026-08-09-AI-STORAGE-DATA-PLANE",
        "T1"
    ],
    [
        "MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN",
        "T1"
    ],
    [
        "MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN",
        "T2"
    ],
    [
        "MI-2026-08-12-224G-PCB-QUALIFICATION-CHAIN",
        "T3"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T3"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T4"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T5"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T6"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T7"
    ],
    [
        "MI-2026-08-02-AI-MEMORY-HIERARCHY",
        "T8"
    ],
    [
        "MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS",
        "T2"
    ]
]


def records(path, kind):
    text = (ROOT / path).read_text(encoding="utf8")
    return [dict((k.strip(), v.strip()) for k, v in
                 (line.split(":", 1) for line in body.splitlines() if ":" in line))
            for body in re.findall(r"<!-- " + kind + r"\s*\n(.*?)-->", text, re.S)]


def ledger(path):
    with (ROOT / path).open(encoding="utf8", newline="") as handle:
        return list(csv.DictReader(handle))


class ResearchCycleOctober12Test(unittest.TestCase):
    def test_starting_due_cohort_has_exactly_one_honest_review_each(self):
        rows = [r for r in ledger("notes/research_method_reviews/monitor_reviews.csv")
                if r["review_id"].startswith("MR-2026-10-12-")]
        self.assertEqual(len(rows), 40)
        self.assertEqual({(r["topic_id"], r["monitor_id"]) for r in rows},
                         {tuple(p) for p in DUE})
        self.assertEqual(sum(r["result"] == "new_support" for r in rows), 1)
        self.assertEqual(sum(r["result"] == "no_new_evidence" for r in rows), 2)
        self.assertEqual(sum(r["result"] == "not_yet_testable" for r in rows), 37)
        for row in rows:
            self.assertEqual(row["claim_action"], "none")
            if row["result"] != "new_support":
                self.assertEqual(row["evidence_source_ids"], "")

    def test_old_capture_and_main_clock_are_preserved(self):
        meta = records(TOPIC, "research_topic")[0]
        self.assertEqual(meta["thesis_claim_id"], "C25")
        self.assertEqual(meta["last_reviewed_at"], "2026-08-24")
        self.assertEqual(meta["review_due"], "2026-08-31")
        sources = {r["source_id"]: r for r in records(TOPIC, "research_source")}
        self.assertEqual(sources["S2"]["captured_at"], "2026-08-03")
        self.assertEqual(sources["S18"]["captured_at"], "2026-08-24")
        self.assertEqual(sources["S20"]["captured_at"], "2026-10-12")
        self.assertEqual(sources["S2"]["url"], sources["S20"]["url"])
        self.assertEqual(sources["S2"]["independence_group"], sources["S20"]["independence_group"])
        self.assertEqual(sources["S20"]["published_at"], "")

    def test_row_count_is_not_product_delta_or_deployment(self):
        claims = {r["claim_id"]: r for r in records(TOPIC, "research_claim")}
        for word in ("21", "System 3", "AIC 11", "retimer 3", "switch/bridge 4", "2026-10-05"):
            self.assertIn(word, claims["C27"]["claim"])
        self.assertIn("不是測試日或出貨日", claims["C27"]["boundary"])
        self.assertIn("差額", claims["C28"]["claim"])
        self.assertIn("歷史", claims["C28"]["basis"])
        edges = {r["edge_id"]: r for r in records(GRAPH, "knowledge_edge")}
        self.assertEqual(edges["KG-PCIE6-I04"]["status"], "retired")
        for key in ("KG-PCIE6-I30", "KG-PCIE6-C04"):
            self.assertEqual(edges[key]["commercial_stage"], "platform_listing")
            self.assertEqual(edges[key]["materiality"], "named_product")
            self.assertEqual(edges[key]["exclusivity"], "unknown")
            self.assertTrue(edges[key]["claim_refs"].endswith("#C27"))

    def test_pcie_revision_is_in_homepage_recent_articles(self):
        meta = records(TOPIC, "research_topic")[0]
        transitions = [r for r in records(TOPIC, "transition") if r["date"] == "2026-10-12"]
        self.assertEqual(len(transitions), 1)
        topic = {"topic_id": meta["topic_id"], "title": meta["topic_id"],
                 "relpath": TOPIC, "meta": meta, "transitions": transitions}
        recent = bd.build_recent_articles("2026-10-12", {}, {}, topics=[topic])
        self.assertIn("topic-" + meta["topic_id"], {r["researchId"] for r in recent["items"]})

    def test_existing_pack_progress_is_not_new_financial_recalculation(self):
        rows = {r["review_id"]: r for r in ledger("notes/research_method_reviews/monitor_reviews.csv")}
        progress = rows["MR-2026-10-12-MISSED-Q2-T11"]
        self.assertEqual(progress["result"], "new_support")
        self.assertEqual(progress["evidence_source_ids"], "S21|S24")
        self.assertIn("行政進度", progress["notes"])
        self.assertIn("不是本輪重算PDF", progress["notes"])
        pcie = rows["MR-2026-10-12-PCIE6-T9"]
        self.assertEqual(pcie["result"], "not_yet_testable")
        self.assertIn("不計原T9完整trigger新支持", pcie["notes"])

    def test_radar_keeps_three_watch_candidates_and_followup_contract(self):
        candidates = records(RADAR, "research_candidate")
        self.assertEqual(len(candidates), 3)
        self.assertEqual([r["rank"] for r in candidates], ["1", "2", "3"])
        # Work dates can move after a documented review; frozen selection ranks cannot.
        for row, original_due in zip(candidates, ["2026-10-15", "2026-10-15", "2026-10-19"]):
            self.assertGreaterEqual(row["next_check"], original_due)
            self.assertTrue(row["next_evidence"])
        for row in candidates:
            self.assertEqual(row["status"], "watch")
            self.assertEqual(row["route"], "watch_only")

    def test_scan_is_partial_despite_zero_announcement_hits(self):
        row = next(r for r in ledger("notes/research_topics/scan_log.csv")
                   if r["scan_id"] == "scan-2026-10-12-listing-and-verification-gaps")
        self.assertEqual(row["scope"], "partial")
        self.assertEqual(row["next_scan_due"], "2026-10-14")
        for boundary in ("缺10/10及10/12", "PDF未核", "7篇source_internal", "10/17"):
            self.assertIn(boundary, row["coverage_note"])


if __name__ == "__main__":
    unittest.main()
