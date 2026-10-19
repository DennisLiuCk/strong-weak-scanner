"""October 19: source publication, shipping and scheduled work are distinct."""
import csv
import json
import unittest
from collections import Counter

from test_research_cycle_20261012 import ROOT, bd, records

COOLING = "notes/research_topics/2026-08-02_liquid_cooling_qualification_ladder.md"
FABRICS = "notes/research_topics/2026-08-02_open_ai_fabrics.md"


def keyed(path, block, key):
    return {row[key]: row for row in records(path, block)}


class ResearchCycleOctober19Test(unittest.TestCase):
    def test_review_cohort_is_bounded_not_fifty_four_validations(self):
        with (ROOT / "notes/research_method_reviews/monitor_reviews.csv").open(
                encoding="utf-8", newline="") as stream:
            rows = [r for r in csv.DictReader(stream) if r["checked_at"] == "2026-10-19"]
        self.assertEqual(len(rows), 54)
        self.assertEqual(len({(r["topic_id"], r["monitor_id"]) for r in rows}), 54)
        self.assertEqual(Counter(r["result"] for r in rows),
                         {"new_support": 1, "no_new_evidence": 1, "not_yet_testable": 52})
        for row in rows:
            self.assertIn("未完成／邊界", row["notes"])
            self.assertIn("來源：", row["notes"])
            self.assertGreater(row["next_check"], row["checked_at"])
            if row["result"] == "new_support":
                self.assertEqual(row["monitor_id"], "T7")
                self.assertEqual(row["evidence_source_ids"], "S36")
                self.assertEqual(row["claim_action"], "new_claim")
            else:
                self.assertEqual(row["claim_action"], "none")
                self.assertFalse(row["evidence_source_ids"])

    def test_pg_document_identity_and_representative_values_are_bounded(self):
        sources = keyed(COOLING, "research_source", "source_id")
        claims = keyed(COOLING, "research_claim", "claim_id")
        source = sources["S36"]
        self.assertEqual(source["published_at"], "2026-09-15")
        self.assertEqual(source["captured_at"], "2026-10-19")
        self.assertIn("5731d7036848e15612229a33b65d2af948b68477a6359e256f198885037a7f43",
                      source["locator"])
        self.assertIn("同一下載檔", source["locator"])
        self.assertIn("不宣稱完成全95頁", source["limitation"])
        for cid in ("C43", "C44", "C45"):
            self.assertEqual(claims[cid]["supporting_source_ids"], "S36")
        self.assertIn("不涵蓋FWS", claims["C43"]["claim"])
        self.assertIn("不應解讀為規格", claims["C45"]["claim"])

    def test_graph_separates_method_from_self_reported_shipping(self):
        cooling = keyed("notes/knowledge_graph/liquid_cooling.md", "knowledge_edge", "edge_id")["KG-LC-I23"]
        fabrics = keyed("notes/knowledge_graph/open_ai_fabrics.md", "knowledge_edge", "edge_id")["KG-FAB-C06"]
        self.assertEqual(cooling["commercial_stage"], "concept")
        self.assertEqual(cooling["materiality"], "adjacent")
        self.assertEqual(fabrics["commercial_stage"], "shipment")
        self.assertEqual(fabrics["materiality"], "named_product")
        self.assertEqual(fabrics["exclusivity"], "unknown")
        self.assertIn("不是客戶收貨完成", fabrics["boundary"])
        self.assertIn("#C25", fabrics["claim_refs"])

    def test_side_updates_reach_homepage_without_resetting_main_clock(self):
        topics = []
        for path, clock in ((COOLING, ("C21", "2026-08-14", "2026-08-16")),
                            (FABRICS, ("C18", "2026-08-12", "2026-08-17"))):
            meta = records(path, "research_topic")[0]
            self.assertEqual(tuple(meta[k] for k in
                                   ("thesis_claim_id", "last_reviewed_at", "review_due")), clock)
            transitions = records(path, "transition")
            self.assertTrue(any(t["date"] == "2026-10-19" and
                                t["evidence"].startswith("sources:") for t in transitions))
            topic = {"topic_id": meta["topic_id"], "title": meta["topic_id"],
                     "relpath": path, "meta": meta, "transitions": transitions}
            self.assertGreaterEqual(bd._topic_content_date(topic), "2026-10-19")
            topics.append(topic)
        recent = bd.build_recent_articles("2026-10-19", {}, {}, topics=topics)
        self.assertEqual({r["researchId"] for r in recent["items"]},
                         {"topic-" + t["topic_id"] for t in topics})

    def test_scan_records_missing_dates_not_zero_market_events(self):
        with (ROOT / "notes/research_topics/scan_log.csv").open(encoding="utf-8", newline="") as stream:
            row = next(r for r in csv.DictReader(stream)
                       if r["scan_id"] == "scan-2026-10-19-work-dates-and-document-boundaries")
        self.assertEqual(row["scope"], "partial")
        self.assertEqual(row["next_scan_due"], "2026-10-21")
        self.assertIn("缺10/17及10/19", row["coverage_note"])
        self.assertIn("仍partial而非全窗口無公告", row["coverage_note"])

    def test_snapshot_preserves_staleness_after_work_is_rescheduled(self):
        snapshot = json.loads((ROOT / "notes/research_method_reviews/2026-10-19_01.json")
                              .read_text(encoding="utf-8"))
        self.assertEqual(snapshot["monitors"]["dueOrOverdue"], 0)
        self.assertEqual(snapshot["freshness"]["staleTopics"], 40)
        self.assertEqual(snapshot["corrections"]["monitorReviewEvents"], 677)
        self.assertEqual(snapshot["scans"]["latestScope"], "partial")
        self.assertEqual(snapshot["claims"]["active"], 900)


if __name__ == "__main__":
    unittest.main()
