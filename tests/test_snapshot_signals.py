import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import snapshot_signals as ss


class SnapshotSignalsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "scripts").mkdir()
        (self.root / "config").mkdir()
        for rel in ("scripts/score.py", "scripts/fetch_daily.py",
                    "config/universe.csv", "config/groups.csv"):
            (self.root / rel).write_text(rel, encoding="utf-8")
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        metric_defs = ",".join(f"{c} REAL" for c in ss.METRIC_COLS)
        score_defs = ",".join(f"{c} REAL" for c in ss.SCORE_COLS)
        self.con.executescript(f"""
        CREATE TABLE universe(stock_id TEXT PRIMARY KEY, name TEXT, grp TEXT, biz TEXT);
        CREATE TABLE groups(grp TEXT PRIMARY KEY, name TEXT, tag TEXT, ord INTEGER);
        CREATE TABLE daily_metrics(date TEXT, stock_id TEXT, {metric_defs}, PRIMARY KEY(date,stock_id));
        CREATE TABLE daily_scores(date TEXT, stock_id TEXT, {score_defs}, PRIMARY KEY(date,stock_id));
        CREATE TABLE chip_health(date TEXT, stock_id TEXT, net_score INTEGER, label TEXT,
                                 grp_rank INTEGER, grp_n INTEGER, PRIMARY KEY(date,stock_id));
        CREATE TABLE group_metrics(date TEXT, grp TEXT, breadth_f REAL, med_dist60 REAL,
          rel20 REAL, med_dip REAL, breadth_t REAL, state TEXT, note TEXT, PRIMARY KEY(date,grp));
        CREATE TABLE market_daily(date TEXT PRIMARY KEY, taiex REAL, dd20 REAL, regime INTEGER);
        CREATE TABLE risk_flags(date TEXT, stock_id TEXT, kind TEXT, reason TEXT, period TEXT);
        CREATE TABLE price(date TEXT, stock_id TEXT);
        CREATE TABLE inst(date TEXT, stock_id TEXT);
        CREATE TABLE margin(date TEXT, stock_id TEXT);
        CREATE TABLE holding(date TEXT, stock_id TEXT);
        CREATE TABLE sbl(date TEXT, stock_id TEXT);
        """)
        self.date = "2026-07-10"
        self.con.execute("INSERT INTO groups VALUES('g','測試族群','測',1)")
        metric_values = {c: 1.0 for c in ss.METRIC_COLS}
        metric_values["tdcc_date"] = "2026-07-03"
        score_values = {c: 1 for c in ss.SCORE_COLS}
        score_values.update({"composite": 3.5, "composite_s": 3.0,
                             "tier_raw": "真強", "tier": "真強", "pending": None})
        for i, sid in enumerate(("1001", "1002"), 1):
            self.con.execute("INSERT INTO universe VALUES(?,?,?,?)", (sid, f"股{i}", "g", "biz"))
            self.con.execute(
                f"INSERT INTO daily_metrics VALUES({','.join('?' for _ in range(2 + len(ss.METRIC_COLS)))})",
                (self.date, sid, *(metric_values[c] for c in ss.METRIC_COLS)))
            self.con.execute(
                f"INSERT INTO daily_scores VALUES({','.join('?' for _ in range(2 + len(ss.SCORE_COLS)))})",
                (self.date, sid, *(score_values[c] for c in ss.SCORE_COLS)))
            self.con.execute("INSERT INTO chip_health VALUES(?,?,?,?,?,?)",
                             (self.date, sid, 2, "健康", i, 2))
            for table in ("price", "inst", "margin", "holding", "sbl"):
                self.con.execute(f"INSERT INTO {table} VALUES(?,?)", (self.date, sid))
        self.con.execute("INSERT INTO group_metrics VALUES(?,?,?,?,?,?,?,?,?)",
                         (self.date, "g", .5, -.1, .02, .03, .5, "中性觀察", "test"))
        self.con.execute("INSERT INTO market_daily VALUES(?,?,?,?)", (self.date, 100.0, -.04, 1))
        self.con.execute("INSERT INTO risk_flags VALUES(?,?,?,?,?)",
                         (self.date, "1001", "注意", "test", None))
        self.con.commit()

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def capture(self, run_id, captured_at):
        return ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id=run_id, captured_at=captured_at,
            source="github-actions", publish=True, git_sha="deadbeef")

    def test_append_only_runs_keep_original_and_revision(self):
        sid, date_, created = self.capture("run-1", "2026-07-10T14:00:00+00:00")
        self.assertEqual((sid, date_, created), ("run-1", self.date, True))
        first = self.con.execute(
            "SELECT tier, composite_s, risk_flags_json FROM oos_signal_snapshots "
            "WHERE snapshot_id='run-1' AND stock_id='1001'").fetchone()
        self.assertEqual(first["tier"], "真強")
        self.assertEqual(first["composite_s"], 3.0)
        self.assertIn("注意", first["risk_flags_json"])

        self.con.execute("UPDATE daily_scores SET tier='真弱', composite_s=-4 WHERE stock_id='1001'")
        self.con.commit()
        self.capture("run-2", "2026-07-10T15:00:00+00:00")
        original = self.con.execute(
            "SELECT tier, composite_s FROM oos_signal_snapshots "
            "WHERE snapshot_id='run-1' AND stock_id='1001'").fetchone()
        revision = self.con.execute(
            "SELECT tier, composite_s FROM oos_signal_snapshots "
            "WHERE snapshot_id='run-2' AND stock_id='1001'").fetchone()
        self.assertEqual(tuple(original), ("真強", 3.0))
        self.assertEqual(tuple(revision), ("真弱", -4.0))
        canonical = self.con.execute(
            "SELECT snapshot_id FROM oos_snapshot_runs WHERE is_official=1 "
            "ORDER BY data_date, captured_at, snapshot_id LIMIT 1").fetchone()[0]
        self.assertEqual(canonical, "run-1")

    def test_same_run_is_idempotent(self):
        self.capture("run-1", "2026-07-10T14:00:00+00:00")
        _, _, created = self.capture("run-1", "2026-07-10T14:00:00+00:00")
        self.assertFalse(created)
        self.assertEqual(
            self.con.execute("SELECT COUNT(*) FROM oos_signal_snapshots").fetchone()[0], 2)

    def test_identical_holiday_run_does_not_create_revision(self):
        self.capture("run-1", "2026-07-10T14:00:00+00:00")
        sid, _, created = self.capture("run-holiday", "2026-07-13T14:00:00+00:00")
        self.assertEqual(sid, "run-1")
        self.assertFalse(created)
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM oos_snapshot_runs").fetchone()[0], 1)

    def test_incomplete_latest_date_is_rejected(self):
        self.con.execute("DELETE FROM daily_scores WHERE stock_id='1002'")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "拒絕凍結不完整快照"):
            self.capture("run-bad", "2026-07-10T14:00:00+00:00")
        self.assertIsNone(self.con.execute(
            "SELECT 1 FROM oos_snapshot_runs WHERE snapshot_id='run-bad'").fetchone())

    def test_prelaunch_restated_date_is_skipped(self):
        sid, date_, created = ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id="prelaunch",
            captured_at="2026-07-10T14:00:00+00:00", source="github-actions",
            publish=True, min_data_date="2026-07-11")
        self.assertEqual((sid, date_, created), (None, self.date, False))
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM oos_snapshot_runs").fetchone()[0], 0)

    def test_local_publish_is_official_and_dedupes_later_action(self):
        sid, _, created = ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id="local-1",
            captured_at="2026-07-10T13:30:00+00:00", source="local", publish=True)
        self.assertEqual((sid, created), ("local-1", True))
        row = self.con.execute(
            "SELECT source,is_official FROM oos_snapshot_runs WHERE snapshot_id=?", (sid,)).fetchone()
        self.assertEqual(tuple(row), ("local", 1))

        sid2, _, created2 = ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id="gh-later",
            captured_at="2026-07-10T14:00:00+00:00", source="github-actions", publish=True)
        self.assertEqual((sid2, created2), ("local-1", False))
        self.assertEqual(self.con.execute("SELECT COUNT(*) FROM oos_snapshot_runs").fetchone()[0], 1)

    def test_local_preview_is_not_official(self):
        sid, _, created = ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id="preview",
            captured_at="2026-07-10T13:00:00+00:00", source="local", publish=False)
        self.assertTrue(created)
        self.assertEqual(self.con.execute(
            "SELECT is_official FROM oos_snapshot_runs WHERE snapshot_id=?", (sid,)).fetchone()[0], 0)

    def test_official_publish_rejects_incomplete_raw_tables(self):
        self.con.execute("DELETE FROM holding WHERE stock_id='1002'")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "原始資料不完整"):
            self.capture("run-raw-gap", "2026-07-10T14:00:00+00:00")

    def test_official_publish_rejects_stale_market(self):
        self.con.execute("UPDATE market_daily SET date='2026-07-09'")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "大盤資料未同步"):
            self.capture("run-market-lag", "2026-07-10T14:00:00+00:00")

    def test_official_publish_rejects_lagging_event_coverage(self):
        self.con.execute("""CREATE TABLE fetch_coverage(
          dataset TEXT,data_id TEXT,covered_through TEXT,updated_at TEXT,
          PRIMARY KEY(dataset,data_id))""")
        rows = [("TaiwanStockDividendResult", sid, self.date, "now")
                for sid in ("1001", "1002")]
        rows.append(("TaiwanStockSplitPrice", "*", self.date, "now"))
        rows.append(("risk_flags", "*", "2026-07-09", "now"))
        self.con.executemany("INSERT INTO fetch_coverage VALUES(?,?,?,?)", rows)
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "coverage 未同步"):
            self.capture("run-coverage-lag", "2026-07-10T14:00:00+00:00")


if __name__ == "__main__":
    unittest.main()
