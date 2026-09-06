import sqlite3
import sys
import unittest
from pathlib import Path
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import operational_health as health


class HealthTest(unittest.TestCase):
    def test_invalid_hypothesis_anchor_remains_a_p0_work_item(self):
        rq = health.rq
        reports = rq.load_reports(notes=rq.load_notes())
        reports["3260"]["quality_invalid"] = True
        reports["3260"]["quality_errors"] = ["formal note anchor mismatch"]
        with patch.object(rq, "load_reports", return_value=reports):
            snapshot = rq.build_attention(rq.taipei_today())
        failures = [item for item in snapshot["items"] if item["kind"] == "hypothesis_report_quality"
                    and item.get("target") == "stock:3260"]
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["priority"], "P0")

    def test_newer_universe_raw_day_cannot_hide_behind_old_complete_scores(self):
        with sqlite3.connect(":memory:") as con:
            con.executescript("""CREATE TABLE universe(stock_id);
                CREATE TABLE price(stock_id,date); CREATE TABLE market(date);
                CREATE TABLE daily_scores(date);
                INSERT INTO universe VALUES ('A');
                INSERT INTO daily_scores VALUES ('2026-09-04');
                INSERT INTO price VALUES ('A','2026-09-07'),('REF','2026-09-09');
                INSERT INTO market VALUES ('2026-09-04');""")
            self.assertEqual(health.latest_data_dates(con), ("2026-09-07", "2026-09-04"))
            con.execute("INSERT INTO market VALUES ('2026-09-08')")
            self.assertEqual(health.latest_data_dates(con), ("2026-09-08", "2026-09-04"))

    def test_publication_uses_first_official_run_and_requires_groups_market_and_spec(self):
        with sqlite3.connect(":memory:") as con:
            con.row_factory = sqlite3.Row
            con.executescript("""CREATE TABLE oos_snapshot_runs(
                snapshot_id,data_date,captured_at,is_official,stock_count,group_count);
                CREATE TABLE oos_signal_snapshots(snapshot_id,stock_id);
                CREATE TABLE oos_group_snapshots(snapshot_id,grp);
                CREATE TABLE oos_market_snapshots(snapshot_id);
                INSERT INTO oos_snapshot_runs VALUES
                    ('first','2026-09-07','2026-09-07T23:47',1,2,1),
                    ('revision','2026-09-07','2026-09-08T01:00',1,2,1);
                INSERT INTO oos_signal_snapshots VALUES ('first','A'),('revision','A'),('revision','B');
                INSERT INTO oos_group_snapshots VALUES ('first','g'),('revision','g');
                INSERT INTO oos_market_snapshots VALUES ('first'),('revision');""")
            progress = {"current_spec_latest_date": "2026-09-07", "phase": "collecting_operational_history"}
            def status():
                return health.publication_status(con, "2026-09-07", progress, "2026-09-07")
            # 完整修正版不能補救首次正式快照缺列。
            self.assertEqual(status()["status"], "failed")
            con.execute("INSERT INTO oos_signal_snapshots VALUES ('first','B')")
            self.assertEqual(status()["status"], "complete")
            con.execute("DELETE FROM oos_market_snapshots WHERE snapshot_id='first'")
            self.assertEqual(status()["status"], "failed")
            con.execute("INSERT INTO oos_market_snapshots VALUES ('first')")
            con.execute("DELETE FROM oos_group_snapshots WHERE snapshot_id='first'")
            self.assertEqual(status()["status"], "failed")
            con.execute("INSERT INTO oos_group_snapshots VALUES ('first','g')")
            progress["current_spec_latest_date"] = None
            self.assertEqual(status()["status"], "failed")
            self.assertEqual(health.publication_status(con, "2026-09-07", progress, "2026-09-08")["status"], "complete")

    def test_degraded_views_cannot_be_hidden_by_green_raw_data(self):
        checks = {"raw": {"status": "complete"}, "ranking": {"status": "degraded"}}
        self.assertEqual(health.overall_status(checks), "degraded")
        checks["pages"] = {"status": "failed"}
        self.assertEqual(health.overall_status(checks), "failed")
        self.assertEqual(health.overall_status({"pages": {"status": "unknown"}}), "degraded")

    def test_tdcc_requires_all_levels_in_universe_and_timely_week(self):
        with sqlite3.connect(":memory:") as con:
            con.execute("CREATE TABLE tdcc_holding(date,stock_id,level)")
            rows = [("2026-08-28", sid, level) for sid in ["A", "REF"] for level in range(1, 18)]
            rows += [("2026-08-28", "B", level) for level in range(1, 17)]
            con.executemany("INSERT INTO tdcc_holding VALUES (?,?,?)", rows)
            result = health.tdcc_status(con, ["A", "B"], "2026-09-04")
            self.assertEqual((result["complete_stocks"], result["status"]), (1, "degraded"))
            con.execute("INSERT INTO tdcc_holding VALUES ('2026-08-28','B',17)")
            self.assertEqual(health.tdcc_status(con, ["A", "B"], "2026-09-04")["status"], "complete")
            self.assertEqual(health.tdcc_status(con, ["A", "B"], "2026-09-07")["status"], "degraded")
