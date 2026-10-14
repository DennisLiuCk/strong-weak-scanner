"""October 14: message delivery is not actuation; partial census stays partial."""
import unittest

from test_research_cycle_20261012 import records, ledger, bd, ROOT

TOPIC = "notes/research_topics/2026-08-07_ai_rack_action_contract.md"
GRAPH = "notes/knowledge_graph/ai_rack_action_contract.md"
RADAR = "notes/research_candidates/2026-09-13_verification_gaps.md"
# Frozen before reviews: all 13 effective work deadlines were October 14.
DUE = {
    ("MI-2026-07-23-US-SECTION301-TAIWAN", "T5"),
    ("MI-2026-08-01-AI-CAPEX-CASH-CONVERSION", "T4"),
    *{("MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER", t)
      for t in ("T9", "T4", "T5", "T6", "T7")},
    *{("MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES", t) for t in ("T1", "T3")},
    *{("MI-2026-08-07-AI-RACK-ACTION-CONTRACT", t) for t in ("T1", "T2", "T4")},
    ("MI-2026-08-08-AI-RACK-TRUST-ROOT", "T1"),
}


class ResearchCycleOctober14Test(unittest.TestCase):
    def test_frozen_due_cohort_has_one_honest_review_each(self):
        rows = [r for r in ledger("notes/research_method_reviews/monitor_reviews.csv")
                if r["review_id"].startswith("MR-2026-10-14-")]
        self.assertEqual(len(rows), 13)
        self.assertEqual({(r["topic_id"], r["monitor_id"]) for r in rows}, DUE)
        for row in rows:
            self.assertEqual(row["result"], "not_yet_testable")
            self.assertEqual(row["evidence_source_ids"], "")
            self.assertEqual(row["claim_action"], "none")
            self.assertIn("原有效期限10/14", row["notes"])
            self.assertGreater(row["next_check"], "2026-10-14")

    def test_main_clock_and_source_publication_boundary_are_preserved(self):
        meta = records(TOPIC, "research_topic")[0]
        self.assertEqual(meta["thesis_claim_id"], "C4")
        self.assertEqual(meta["last_reviewed_at"], "2026-08-07")
        self.assertEqual(meta["review_due"], "2026-08-31")
        sources = {r["source_id"]: r for r in records(TOPIC, "research_source")}
        self.assertEqual(sources["S1"]["captured_at"], "2026-08-07")
        self.assertEqual(sources["S15"]["captured_at"], "2026-10-14")
        self.assertEqual(sources["S15"]["published_at"], "")
        self.assertEqual(sources["S15"]["independence_group"], "nvidia-dsx")
        self.assertIn("不能借用BMS 1.0.0", sources["S15"]["limitation"])
        prose = (ROOT / TOPIC).read_text(encoding="utf8")
        self.assertNotIn("為何可信度是中等", prose)
        self.assertIn("有效可信度已降為低", prose)

    def test_message_termini_do_not_claim_physical_or_financial_results(self):
        claim = next(r for r in records(TOPIC, "research_claim") if r["claim_id"] == "C19")
        self.assertEqual(claim["label"], "verified")
        for word in ("本地Kind", "不定義產品目標", "broker確認", "subscriber收件"):
            self.assertIn(word, claim["claim"])
        for word in ("沒有實測延遲", "閥門", "財務"):
            self.assertIn(word, claim["boundary"])
        edge = next(r for r in records(GRAPH, "knowledge_edge") if r["edge_id"] == "KG-RAC-I20")
        self.assertEqual(edge["materiality"], "adjacent")
        self.assertEqual(edge["commercial_stage"], "concept")
        self.assertEqual(edge["exclusivity"], "unknown")
        self.assertTrue(edge["claim_refs"].endswith("#C19"))
        self.assertIn("不是實測數值", edge["boundary"])
        monitor = next(r for r in records(TOPIC, "monitoring_item") if r["monitor_id"] == "T6")
        self.assertEqual(monitor["next_check"], "2026-11-14")
        self.assertIn("獨立感測", monitor["trigger"])
        self.assertIn("不得", monitor["invalidation"])

    def test_revision_is_in_homepage_recent_articles(self):
        meta = records(TOPIC, "research_topic")[0]
        transitions = [r for r in records(TOPIC, "transition") if r["date"] == "2026-10-14"]
        self.assertEqual(len(transitions), 1)
        topic = {"topic_id": meta["topic_id"], "title": meta["topic_id"],
                 "relpath": TOPIC, "meta": meta, "transitions": transitions}
        recent = bd.build_recent_articles("2026-10-14", {}, {}, topics=[topic])
        self.assertIn("topic-" + meta["topic_id"], {r["researchId"] for r in recent["items"]})

    def test_radar_frozen_ranks_and_work_dates_are_not_reselected(self):
        candidates = records(RADAR, "research_candidate")
        self.assertEqual([r["rank"] for r in candidates], ["1", "2", "3"])
        self.assertEqual([r["next_check"] for r in candidates],
                         ["2026-10-15", "2026-10-15", "2026-10-19"])
        self.assertTrue(all(r["route"] == "watch_only" and r["status"] == "watch" for r in candidates))

    def test_partial_event_scan_and_index_failures_are_not_negative_evidence(self):
        row = next(r for r in ledger("notes/research_topics/scan_log.csv")
                   if r["scan_id"] == "scan-2026-10-14-message-boundaries-and-event-triage")
        self.assertEqual(row["scope"], "partial")
        self.assertEqual(row["next_scan_due"], "2026-10-16")
        for boundary in ("18列命中14家", "缺10/12及10/14", "12家公司MOPS索引成功",
                         "三家解析失敗不能記無檔", "PDF未核", "10/17"):
            self.assertIn(boundary, row["coverage_note"])


if __name__ == "__main__":
    unittest.main()
