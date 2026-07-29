import sqlite3
import sys
import unittest
from datetime import date
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import research_queue as rq
import leading_hypotheses as lh


def topic_text(stock_id="1234", group_id="serverodm"):
    return f"""# 測試議題

<!-- research_topic
topic_id: MI-2026-07-27-TEST
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-26
last_reviewed_at: 2026-07-27
review_due: 2026-08-03
source_type: official_company
publisher_domain: example.com
canonical_url: https://ir.example.com/news
source_chain_id: example-20260726
stock_ids: {stock_id}
group_ids: {group_id}
trigger_type: product_ramp
evidence_role: candidate_source
route: market_issue_watch
-->

<!-- transition
date: 2026-07-27
from: initial
to: inbox
reason: initial_capture
evidence: source_chain:example-20260726
-->
<!-- transition
date: 2026-07-27
from: inbox
to: triaged
reason: mapping_reviewed
evidence: source_chain:example-20260726
-->

<!-- impact
group_id: {group_id}
stock_ids: {stock_id}
direction: uncertain
hypothesis_refs: {stock_id}:H1
note_action: watch
action_due: 2026-08-03
rationale: 需要等公司正式揭露
evidence_boundary: 不構成訂單或營收事實
-->
"""


class ResearchTopicContractTest(unittest.TestCase):
    def setUp(self):
        self.universe = [
            {"stock_id": "1234", "name": "甲", "group": "serverodm", "biz": "x"},
            {"stock_id": "5678", "name": "乙", "group": "pcb", "biz": "y"},
        ]
        self.reports = {
            "1234": {"hypotheses": [{"id": "H1"}]},
            "5678": {"hypotheses": [{"id": "H1"}]},
        }

    def test_valid_topic_preserves_candidate_boundary_and_routes_to_known_stock(self):
        info = rq.analyse_topic(
            "topic.md", topic_text(), self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertFalse(info["quality_invalid"], info["quality_errors"])
        self.assertEqual(info["stock_ids"], ["1234"])
        self.assertEqual(info["impacts"][0]["hypothesis_refs"], ["1234:H1"])
        self.assertEqual(info["status"], "triaged")

    def test_stock_group_mismatch_is_rejected(self):
        info = rq.analyse_topic(
            "topic.md", topic_text(group_id="pcb"),
            self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertTrue(any("實際屬 serverodm" in error for error in info["quality_errors"]))

    def test_meta_must_declare_every_impact_stock_and_group(self):
        text = topic_text().replace("stock_ids: 1234", "stock_ids:", 1)
        text = text.replace("group_ids: serverodm", "group_ids:", 1)
        info = rq.analyse_topic(
            "topic.md", text, self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertIn(
            "meta stock_ids 必須等於所有 impact stock_ids 聯集",
            info["quality_errors"])
        self.assertIn(
            "meta group_ids 必須等於所有 impact group_id 聯集",
            info["quality_errors"])

    def test_broken_transition_chain_is_rejected(self):
        text = topic_text().replace("from: inbox", "from: initial", 1)
        info = rq.analyse_topic(
            "topic.md", text, self.universe, {"serverodm", "pcb"}, self.reports)
        self.assertTrue(any("未銜接上一狀態" in error for error in info["quality_errors"]))

    def test_repo_topic_register_and_scan_log_lint(self):
        topics = rq.load_topics(reports=lh.load_reports())
        scan = rq.load_scan_log(topic_ids=[topic["topic_id"] for topic in topics])
        self.assertEqual(len(topics), 3)
        self.assertFalse(any(topic["quality_errors"] for topic in topics))
        self.assertFalse(scan["errors"])
        self.assertEqual(scan["latest"]["scope"], "partial")

    def test_scan_log_rejects_empty_id_and_impossible_clock_order(self):
        text = (
            "scan_id,window_start,window_end,scanned_at,scope,source_domains,"
            "result_topic_ids,next_scan_due,coverage_note\n"
            ",2026-07-19,2026-07-27,2026-07-26,partial,example.com,none,"
            "2026-07-25,測試\n"
        )
        with mock.patch.object(rq.os.path, "exists", return_value=True):
            with mock.patch("builtins.open", mock.mock_open(read_data=text)):
                scan = rq.load_scan_log("scan.csv")

        self.assertTrue(any("scan_id 不可空白" in error for error in scan["errors"]))
        self.assertTrue(any("window_end 晚於 scanned_at" in error for error in scan["errors"]))
        self.assertTrue(any("scanned_at 晚於 next_scan_due" in error for error in scan["errors"]))
        self.assertIsNone(scan["latest"])


class ResearchScheduleTest(unittest.TestCase):
    def test_four_cohorts_cover_universe_once_and_are_balanced(self):
        universe = rq._load_universe()
        cohorts = rq.cohort_map(universe)
        flat = [row["stock_id"] for rows in cohorts.values() for row in rows]
        self.assertEqual(len(flat), 121)
        self.assertEqual(len(flat), len(set(flat)))
        self.assertEqual(sorted(map(len, cohorts.values())), [30, 30, 30, 31])
        for group_id in rq._load_groups():
            self.assertTrue(all(
                any(row["group"] == group_id for row in cohorts[label])
                for label in "ABCD"))

    def test_rotation_anchor_starts_with_a(self):
        self.assertEqual(rq.active_cohort(date(2026, 7, 27))[0], "A")
        self.assertEqual(rq.active_cohort(date(2026, 8, 3))[0], "B")

    def test_expected_month_respects_tenth_day_reporting_boundary(self):
        self.assertEqual(rq.expected_revenue_period(date(2026, 7, 10)), (2026, 5))
        self.assertEqual(rq.expected_revenue_period(date(2026, 7, 11)), (2026, 6))

    def test_expected_quarter_follows_filing_deadlines(self):
        self.assertEqual(rq.expected_quarter_date(date(2026, 3, 31)), date(2025, 9, 30))
        self.assertEqual(rq.expected_quarter_date(date(2026, 4, 1)), date(2025, 12, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 5, 15)), date(2025, 12, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 5, 16)), date(2026, 3, 31))
        self.assertEqual(rq.expected_quarter_date(date(2026, 8, 15)), date(2026, 6, 30))
        self.assertEqual(rq.expected_quarter_date(date(2026, 11, 15)), date(2026, 9, 30))

    def test_topic_priority_is_not_discarded_before_due_date(self):
        as_of = date(2026, 7, 27)
        due = date(2026, 8, 3)
        self.assertEqual(rq._topic_queue_priority("p0", due, as_of), "P0")
        self.assertEqual(rq._topic_queue_priority("p1", due, as_of), "P1")
        self.assertEqual(rq._topic_queue_priority("p2", due, as_of), "P2")
        self.assertEqual(
            rq._topic_queue_priority("p2", date(2026, 7, 26), as_of), "P1")

    def test_research_watch_is_read_only_and_runs_after_financial_fetch(self):
        text = (ROOT / ".github" / "workflows" / "research-watch.yml").read_text(
            encoding="utf-8")
        self.assertIn('cron: "0 1 * * 1"', text)
        self.assertIn('workflows: ["fetch-financials"]', text)
        self.assertIn("python scripts/research_queue.py --attention", text)
        self.assertIn("contents: read", text)
        self.assertNotIn("repo-main-writer", text)
        self.assertNotIn("git add", text)

        quality = (
            ROOT / ".github" / "workflows" / "qualitative-quality.yml"
        ).read_text(encoding="utf-8")
        self.assertIn("python scripts/research_queue.py --lint", quality)
        self.assertGreaterEqual(quality.count('"notes/research_topics/**"'), 2)
        self.assertGreaterEqual(quality.count('"tests/test_research_queue.py"'), 2)


class ResearchFinancialCoverageTest(unittest.TestCase):
    def test_financial_snapshot_reports_exact_missing_stock_read_only(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE month_revenue(
              date TEXT, stock_id TEXT, revenue INTEGER,
              revenue_month INTEGER, revenue_year INTEGER);
            CREATE TABLE financials(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE balance_sheet(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE cash_flow(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
        """)
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "1234", 1, 6, 2026))
        con.execute(
            "INSERT INTO month_revenue VALUES(?,?,?,?,?)",
            ("2026-07-01", "5678", None, 6, 2026))
        for table in ("financials", "balance_sheet", "cash_flow"):
            con.executemany(
                f"INSERT INTO {table} VALUES(?,?,?,?,?)",
                [
                    ("2026-03-31", "1234", "Revenue", 1.0, "x"),
                    ("2026-03-31", "5678", "Revenue", 1.0, "x"),
                    # 單一早報者不可把其餘 universe 推成新季缺口。
                    ("2026-06-30", "1234", "Revenue", 1.0, "x"),
                ],
            )
        con.commit()
        con.execute("PRAGMA query_only = 1")
        self.assertEqual(con.execute("PRAGMA query_only").fetchone()[0], 1)
        result = rq.financial_snapshot(
            con,
            [
                {"stock_id": "1234", "name": "甲", "group": "serverodm"},
                {"stock_id": "5678", "name": "乙", "group": "pcb"},
            ],
            date(2026, 7, 27),
        )
        con.close()

        self.assertEqual(result["expected_revenue_period"], "2026-06")
        self.assertEqual(result["revenue_missing"], ["5678"])
        self.assertEqual(result["expected_quarter_period"], "2026Q1")
        self.assertEqual(result["common_latest_period"], "2026Q1")
        self.assertTrue(all(
            item["covered"] == 2 for item in result["quarter_tables"].values()))

    def test_whole_batch_lag_cannot_self_report_as_complete(self):
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.executescript("""
            CREATE TABLE month_revenue(
              date TEXT, stock_id TEXT, revenue INTEGER,
              revenue_month INTEGER, revenue_year INTEGER);
            CREATE TABLE financials(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE balance_sheet(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
            CREATE TABLE cash_flow(
              date TEXT, stock_id TEXT, type TEXT, value REAL, origin_name TEXT);
        """)
        for table in ("financials", "balance_sheet", "cash_flow"):
            con.executemany(
                f"INSERT INTO {table} VALUES(?,?,?,?,?)",
                [
                    ("2026-03-31", "1234", "Revenue", 1.0, "x"),
                    ("2026-03-31", "5678", "Revenue", 1.0, "x"),
                ],
            )
        con.commit()
        con.execute("PRAGMA query_only = 1")
        result = rq.financial_snapshot(
            con,
            [
                {"stock_id": "1234", "name": "甲", "group": "serverodm"},
                {"stock_id": "5678", "name": "乙", "group": "pcb"},
            ],
            date(2026, 8, 15),
        )
        con.close()

        self.assertEqual(result["expected_quarter_period"], "2026Q2")
        self.assertIsNone(result["common_latest_period"])
        self.assertTrue(all(
            item["covered"] == 0
            and item["missing"] == ["1234", "5678"]
            for item in result["quarter_tables"].values()))


if __name__ == "__main__":
    unittest.main()
