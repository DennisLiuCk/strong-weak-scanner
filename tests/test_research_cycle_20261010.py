"""Research follow-up: successor scope is not publication or project funding."""
import csv
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_dashboard as bd

PLP = "notes/research_topics/2026-08-02_panel_level_packaging_readiness.md"
DC = "notes/research_topics/2026-09-10_dc_phase_delivery.md"


def records(path, kind):
    text = (ROOT / path).read_text(encoding="utf8")
    return [dict((k.strip(), v.strip()) for k, v in
                 (line.split(":", 1) for line in body.splitlines() if ":" in line))
            for body in re.findall(r"<!-- " + kind + r"\s*\n(.*?)-->", text, re.S)]


class ResearchCycleOctober10Test(unittest.TestCase):
    def test_branch_updates_leave_main_evidence_clock(self):
        for path, claim, clock, due in (
            (PLP, "C8", "2026-08-12", "2026-09-12"),
            (DC, "C1", "2026-09-10", "2026-10-10"),
        ):
            meta = records(path, "research_topic")[0]
            self.assertEqual(meta["thesis_claim_id"], claim)
            self.assertEqual(meta["last_reviewed_at"], clock)
            self.assertEqual(meta["review_due"], due)
            self.assertEqual(meta["base_confidence"], "medium")

    def test_prepared_approved_published_and_observed_dates_are_separate(self):
        sources = {r["source_id"]: r for r in records(PLP, "research_source")}
        for key in ("S14", "S16"):
            self.assertEqual(sources[key]["source_kind"], "living_index")
            self.assertEqual(sources[key]["published_at"], "")
            self.assertEqual(sources[key]["captured_at"], "2026-10-10")
            self.assertIn("首次上網日未知", sources[key]["locator"])
        self.assertEqual(sources["S15"]["published_at"], "2026-09-24")
        self.assertIn("09/11/2026", sources["S15"]["locator"])
        claims = {r["claim_id"]: r for r in records(PLP, "research_claim")}
        self.assertIn("正式出版版號", claims["C18"]["boundary"])
        self.assertIn("不是完成日", claims["C19"]["boundary"])
        self.assertIn("不是相互矛盾", claims["C20"]["boundary"])
        self.assertEqual(claims["C11"]["as_of"], "2026-08-13")

    def test_successor_keeps_old_monitor_contract(self):
        monitors = {r["monitor_id"]: r for r in records(PLP, "monitoring_item")}
        self.assertEqual(monitors["T4"]["status"], "retired")
        self.assertEqual(monitors["T5"]["status"], "active")
        for key in ("metric", "trigger", "invalidation", "frequency",
                    "frequency_detail", "next_check"):
            self.assertEqual(monitors["T4"][key], monitors["T5"][key])
        self.assertIn("S18", monitors["T5"]["watch_source_ids"])
        edges = {r["edge_id"]: r for r in records(
            "notes/knowledge_graph/panel_level_packaging.md", "knowledge_edge")}
        for old, new in (("KG-PLP-C04", "KG-PLP-C05"), ("KG-PLP-I19", "KG-PLP-I22")):
            self.assertEqual(edges[old]["status"], "retired")
            self.assertEqual(edges[new]["status"], "active")
            for key in ("commercial_stage", "materiality", "exclusivity"):
                self.assertEqual(edges[old][key], edges[new][key])

    def test_due_results_do_not_count_missing_attachments_as_absence(self):
        with (ROOT / "notes/research_method_reviews/monitor_reviews.csv").open(
                encoding="utf8", newline="") as f:
            rows = {r["review_id"]: r for r in csv.DictReader(f)
                    if r["review_id"].startswith("MR-2026-10-10-")}
        self.assertEqual(len(rows), 6)  # Five due tasks plus one administrative successor.
        self.assertEqual(sum(r["result"] == "new_support" for r in rows.values()), 1)
        self.assertEqual(sum(r["result"] == "no_new_evidence" for r in rows.values()), 2)
        self.assertEqual(sum(r["result"] == "not_yet_testable" for r in rows.values()), 3)
        for suffix in ("COOLING-T9", "PLP-T5", "SECTION301-T5", "DC-PHASE-T1"):
            row = rows["MR-2026-10-10-" + suffix]
            self.assertEqual(row["evidence_source_ids"], "")
            self.assertEqual(row["claim_action"], "none")
        self.assertIn("HTTP403", rows["MR-2026-10-10-COOLING-T9"]["notes"])
        self.assertIn("完整trigger未命中", rows["MR-2026-10-10-PLP-T4"]["notes"])

    def test_parent_facility_does_not_rewrite_phase_delivery(self):
        claims = {r["claim_id"]: r for r in records(DC, "research_claim")}
        self.assertIn("交割日", claims["C8"]["claim"])
        self.assertIn("不可重複相加", claims["C8"]["boundary"])
        self.assertEqual(claims["C9"]["label"], "inference")
        self.assertIn("不宣稱第二期至今仍未融資", claims["C9"]["boundary"])
        self.assertEqual(claims["C4"]["as_of"], "2026-09-10")

    def test_both_article_revisions_reach_homepage(self):
        topics = []
        for path in (PLP, DC):
            meta = records(path, "research_topic")[0]
            transitions = [r for r in records(path, "transition") if r["date"] == "2026-10-10"]
            self.assertEqual(len(transitions), 1)
            topics.append({"topic_id": meta["topic_id"], "title": meta["topic_id"],
                           "relpath": path, "meta": meta, "transitions": transitions})
        recent = bd.build_recent_articles("2026-10-10", {}, {}, topics=topics)
        self.assertTrue({"topic-" + t["topic_id"] for t in topics} <=
                        {r["researchId"] for r in recent["items"]})

    def test_scan_preserves_daily_batch_gap_and_next_candidate_work(self):
        with (ROOT / "notes/research_topics/scan_log.csv").open(encoding="utf8", newline="") as f:
            row = next(r for r in csv.DictReader(f)
                       if r["scan_id"] == "scan-2026-10-10-successor-and-financing")
        self.assertEqual(row["scope"], "partial")
        for boundary in ("缺10/10", "PDF未核", "玻璃", "7篇source_internal"):
            self.assertIn(boundary, row["coverage_note"])


if __name__ == "__main__":
    unittest.main()
