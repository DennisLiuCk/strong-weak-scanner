"""成熟交易日不能冒充獨立觀測，首次空快照也不能被修正版掩蓋。"""
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import evidence_status as es
import build_dashboard as bd


class EvidenceStatusTest(unittest.TestCase):
    def test_28_days_do_not_pass_and_disjoint_spans_are_counted(self):
        spine = [f"2026-{i:04d}" for i in range(60)]
        snap = spine[2:12] + spine[16:24] + spine[28:38]
        result = es.maturity(snap + snap, spine, spine[0], 10)
        self.assertEqual((result["oos_days"], result["oos_mature"]), (28, 28))
        self.assertEqual((result["eff_obs"], result["episodes"]), (2.8, 3))
        self.assertTrue(result["se_blocked"])

    def test_minimum_sample_only_allows_per_metric_review(self):
        spine = list(range(45))
        result = es.maturity(spine, spine, -1, 10)
        self.assertEqual(result["oos_mature"], 35)
        self.assertEqual(result["status"], "per_metric_review_required")
        self.assertIn("尚非策略通過", result["label"])
        self.assertFalse(result["se_blocked"])

    def test_nontrading_dates_and_cutoff_are_excluded(self):
        result = es.maturity([1, 2, 4, 8], [1, 2, 3, 4, 5, 6], 1, 2)
        self.assertEqual((result["oos_days"], result["oos_mature"]), (2, 2))
        self.assertEqual(es.maturity([], [], "2026-01-01", 10)["episodes"], 0)
        with self.assertRaises(ValueError):
            es.maturity([], [], None, 0)

    def test_home_uses_first_nonempty_publication_and_asof_report(self):
        # Fixture writes only to an isolated in-memory DB.
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        self.addCleanup(con.close)
        con.executescript("""
            CREATE TABLE daily_scores(date TEXT);
            CREATE TABLE daily_metrics(date TEXT);
            CREATE TABLE oos_snapshot_runs(data_date TEXT, captured_at TEXT,
                snapshot_id TEXT, is_official INTEGER);
            CREATE TABLE oos_signal_snapshots(snapshot_id TEXT);
            INSERT INTO oos_snapshot_runs VALUES
              ('2026-08-01','01','empty',1), ('2026-08-01','02','later',1),
              ('2026-08-02','01','valid',1), ('2026-08-03','01','local',0);
            INSERT INTO oos_signal_snapshots VALUES ('later'),('valid'),('local');
        """)
        days = [(f"2026-08-{d:02d}",) for d in range(1, 21)]
        con.executemany("INSERT INTO daily_metrics VALUES (?)", days)
        con.executemany("INSERT INTO daily_scores VALUES (?)", days)
        with tempfile.TemporaryDirectory() as folder:
            reports = Path(folder, "reports")
            reports.mkdir()
            for name in ["validate_2026-08-14.md", "validate_2026-08-21.md", "validate_z.md"]:
                (reports / name).write_text("title\n## ② Tier\n", encoding="utf-8")
            with patch.object(bd, "ROOT", folder):
                result = bd.build_strategy_status(con, "2026-08-20")
        self.assertEqual(result["oos_days"], 1)
        self.assertEqual(result["evidence"]["oos_mature"], 1)
        self.assertEqual(result["report_date"], "2026-08-14")
        self.assertTrue(result["report_tier_url"].endswith("validate_2026-08-14.md#L2"))
