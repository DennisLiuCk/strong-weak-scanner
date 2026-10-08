import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import snapshot_signals as ss
import score
from test_suspension_events import add_evidence


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
        CREATE TABLE market_provenance(
          date TEXT PRIMARY KEY, canonical_source TEXT NOT NULL, official_taiex REAL,
          finmind_taiex REAL, abs_diff REAL, checked_at TEXT);
        CREATE TABLE risk_flags(date TEXT, stock_id TEXT, kind TEXT, reason TEXT, period TEXT);
        CREATE TABLE price(date TEXT, stock_id TEXT, open REAL, high REAL, low REAL,
                           close REAL, volume INTEGER, amount REAL, trades INTEGER);
        CREATE TABLE inst(date TEXT, stock_id TEXT);
        CREATE TABLE margin(date TEXT, stock_id TEXT);
        CREATE TABLE holding(date TEXT, stock_id TEXT);
        CREATE TABLE sbl(date TEXT, stock_id TEXT);
        CREATE TABLE trading_status(date TEXT, stock_id TEXT, status TEXT, source TEXT,
                                    reason TEXT, PRIMARY KEY(date,stock_id));
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
            self.con.execute("INSERT INTO price VALUES(?,?,?,?,?,?,?,?,?)",
                             (self.date, sid, 10, 10, 10, 10, 100, 1000, 10))
            for table in ("inst", "margin", "holding", "sbl"):
                self.con.execute(f"INSERT INTO {table} VALUES(?,?)", (self.date, sid))
        self.con.execute("INSERT INTO group_metrics VALUES(?,?,?,?,?,?,?,?,?)",
                         (self.date, "g", .5, -.1, .02, .03, .5, "中性觀察", "test"))
        self.con.execute("INSERT INTO market_daily VALUES(?,?,?,?)", (self.date, 100.0, -.04, 1))
        self.con.execute(
            "INSERT INTO market_provenance VALUES(?,?,?,?,?,?)",
            (self.date, "TWSE_MI_INDEX", 100.0, 100.0, 0.0, "now"))
        self.con.execute("INSERT INTO risk_flags VALUES(?,?,?,?,?)",
                         (self.date, "1001", "注意", "test", None))
        score.record_score_build(self.con)
        self.con.commit()

    def tearDown(self):
        self.con.close()
        self.tmp.cleanup()

    def capture(self, run_id, captured_at):
        return ss.capture_snapshot(
            self.con, root=str(self.root), snapshot_id=run_id, captured_at=captured_at,
            source="github-actions", publish=True, git_sha="deadbeef")

    def test_official_reduction_absence_is_captured_with_evidence(self):
        for table in ("price", "inst", "daily_metrics", "daily_scores", "chip_health"):
            self.con.execute(f"DELETE FROM {table} WHERE stock_id='1002'")
        add_evidence(self.con, "1002", self.date, "1150710", "1150720")
        self.capture("reduction", "2026-07-10T16:00:00+00:00")
        quality = json.loads(self.con.execute(
            "SELECT quality_json FROM oos_snapshot_runs WHERE snapshot_id='reduction'").fetchone()[0])
        self.assertEqual(quality["eligible"], 1)
        self.assertEqual(quality["raw_expected"], {"price": 1, "inst": 1, "margin": 2,
                                                   "holding": 2, "sbl": 2})
        self.assertIn("SHA256=", quality["excluded"][0]["reason"])
        self.con.execute("DELETE FROM holding WHERE stock_id='1002'")
        with self.assertRaisesRegex(RuntimeError, "holding"):
            self.capture("still-missing", "2026-07-10T16:10:00+00:00")

    def test_strict_ranking_roles_cover_full_universe_when_one_stock_is_suspended(self):
        import ranking_views as rv
        roles = self.root / "config" / "ranking_roles.csv"
        roles.write_text("stock_id,group,role,role_label,basis\n"
                         "1001,g,test,Test,basis\n1002,g,test,Test,basis\n", encoding="utf-8")
        self.con.execute("DELETE FROM daily_scores WHERE stock_id='1002'")
        self.con.execute("DELETE FROM daily_metrics WHERE stock_id='1002'")
        payload = rv.build_from_db(self.con, self.date, roles_path=str(roles), strict_roles=True)
        self.assertEqual([r["stock_id"] for r in payload["rows"]], ["1001"])
        roles.write_text(roles.read_text(encoding="utf-8") + "9999,g,test,Test,basis\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "extra"):
            rv.build_from_db(self.con, self.date, roles_path=str(roles), strict_roles=True)

    def test_late_recovery_keeps_actual_time_and_is_not_oos_evidence(self):
        self.capture("late", "2026-07-11T01:00:00+00:00")
        row = self.con.execute("SELECT * FROM oos_snapshot_runs WHERE snapshot_id='late'").fetchone()
        self.assertEqual(row["captured_at"], "2026-07-11T01:00:00+00:00")
        quality = json.loads(row["quality_json"])
        self.assertFalse(quality["oos_eligible"])
        self.assertEqual(quality["publication_timing"], "late_recovery")
        import evidence_status
        self.assertEqual(list(evidence_status.first_official_runs(self.con)), [self.date])
        self.assertEqual(evidence_status.first_official_runs(self.con, eligible_only=True), {})
        duplicate = self.capture("repeat", "2026-07-12T12:00:00+00:00")
        self.assertEqual(duplicate, ("late", self.date, False))

    def test_timing_boundary_and_timezone_are_explicit(self):
        self.assertTrue(ss.publication_timing(self.date, "2026-07-11T00:59:59+00:00")["oos_eligible"])
        self.assertFalse(ss.publication_timing(self.date, "2026-07-11T09:00:00+08:00")["oos_eligible"])
        with self.assertRaisesRegex(ValueError, "時區"):
            ss.publication_timing(self.date, "2026-07-11T09:00:00")

    def test_append_only_runs_keep_original_and_revision(self):
        sid, date_, created = self.capture("run-1", "2026-07-10T14:00:00+00:00")
        self.assertEqual((sid, date_, created), ("run-1", self.date, True))
        first = self.con.execute(
            "SELECT tier, composite_s, ma5, rsi14, volume, vol_ratio20, risk_flags_json "
            "FROM oos_signal_snapshots "
            "WHERE snapshot_id='run-1' AND stock_id='1001'").fetchone()
        self.assertEqual(first["tier"], "真強")
        self.assertEqual(first["composite_s"], 3.0)
        self.assertEqual((first["ma5"], first["rsi14"], first["volume"], first["vol_ratio20"]),
                         (1.0, 1.0, 1, 1.0))
        self.assertIn("注意", first["risk_flags_json"])
        ranking = self.con.execute(
            """SELECT spec_sha,champion_pct,lens_a,lens_b,lens_c,payload_json
               FROM oos_ranking_view_snapshots
               WHERE snapshot_id='run-1' AND stock_id='1001'""").fetchone()
        self.assertRegex(ranking["spec_sha"], r"^[0-9a-f]{64}$")
        self.assertIsNotNone(ranking["champion_pct"])
        self.assertIn("peer_sensitivity", ranking["payload_json"])
        quality = json.loads(self.con.execute(
            "SELECT quality_json FROM oos_snapshot_runs WHERE snapshot_id='run-1'"
        ).fetchone()[0])
        self.assertEqual(quality["ranking_views"], 2)
        self.assertRegex(quality["ranking_spec_sha"], r"^[0-9a-f]{64}$")
        self.assertIn("ranking_lens_d", quality)
        self.assertIn("ranking_role_rank", quality)
        self.assertEqual(quality["score_version"], score.SCORE_VERSION)
        self.assertEqual(quality["score_spec_sha"], score.score_spec_digest())

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
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM oos_ranking_view_snapshots"
        ).fetchone()[0], 4)
        canonical = self.con.execute(
            "SELECT snapshot_id FROM oos_snapshot_runs WHERE is_official=1 "
            "ORDER BY data_date, captured_at, snapshot_id LIMIT 1").fetchone()[0]
        self.assertEqual(canonical, "run-1")

    def test_missing_or_stale_score_build_cannot_be_published_as_new_rules(self):
        self.con.execute("DELETE FROM score_build_metadata")
        with self.assertRaisesRegex(RuntimeError, "score 規則版本"):
            self.capture("missing-build", "2026-07-10T14:00:00+00:00")
        score.record_score_build(self.con)
        self.con.execute("UPDATE score_build_metadata SET score_spec_sha='old'")
        with self.assertRaisesRegex(RuntimeError, "score 規則版本"):
            self.capture("stale-build", "2026-07-10T14:00:00+00:00")

    def test_pre_effective_rebuild_is_not_new_rule_oos(self):
        self.capture("before-effective", "2026-07-10T14:00:00+00:00")
        quality = json.loads(self.con.execute(
            "SELECT quality_json FROM oos_snapshot_runs WHERE snapshot_id='before-effective'"
        ).fetchone()[0])
        self.assertFalse(quality["score_rules_effective"])
        self.assertFalse(quality["oos_eligible"])
        self.assertEqual(quality["publication_timing"], "before_score_rule_effective_date")

    def test_c3_snapshot_roundtrip_and_original_values_are_immutable(self):
        new_date = "2026-10-12"
        for table in ("daily_metrics", "daily_scores", "chip_health", "price", "inst", "margin",
                      "holding", "sbl", "group_metrics", "market_daily", "market_provenance", "risk_flags"):
            self.con.execute(f"UPDATE {table} SET date=?", (new_date,))
        self.capture("c3-first", "2026-10-12T15:50:00+00:00")
        before = tuple(self.con.execute(
            "SELECT shadow_resil05,payload_json FROM oos_ranking_view_snapshots "
            "WHERE snapshot_id='c3-first' AND stock_id='1001'").fetchone())
        self.assertEqual(before[0], 50.0)
        self.assertEqual(json.loads(before[1])["shadow_resil05"], before[0])
        self.con.execute("UPDATE daily_scores SET s_resil=2 WHERE stock_id='1001'")
        self.capture("c3-revision", "2026-10-12T15:55:00+00:00")
        after = tuple(self.con.execute(
            "SELECT shadow_resil05,payload_json FROM oos_ranking_view_snapshots "
            "WHERE snapshot_id='c3-first' AND stock_id='1001'").fetchone())
        changed = self.con.execute(
            "SELECT shadow_resil05 FROM oos_ranking_view_snapshots "
            "WHERE snapshot_id='c3-revision' AND stock_id='1001'").fetchone()[0]
        self.assertEqual(before, after)
        self.assertEqual(changed, 100.0)

    def test_c3_schema_migration_does_not_backfill_or_rewrite_old_rows(self):
        legacy_schema = ss.SCHEMA.replace("shadow_price10 REAL, shadow_resil05 REAL", "shadow_price10 REAL")
        self.con.executescript(legacy_schema)
        self.con.execute("""INSERT INTO oos_ranking_view_snapshots
            (snapshot_id,date,stock_id,grp,spec_sha,payload_json)
            VALUES('legacy','2026-09-07','1001','g','old-spec','{"legacy":true}')""")
        before = tuple(self.con.execute("SELECT * FROM oos_ranking_view_snapshots").fetchone())
        ss.ensure_schema(self.con)
        after = tuple(self.con.execute("SELECT * FROM oos_ranking_view_snapshots").fetchone())
        self.assertEqual(after[:-1], before)
        self.assertIsNone(after[-1])

    def test_same_run_is_idempotent(self):
        self.capture("run-1", "2026-07-10T14:00:00+00:00")
        _, _, created = self.capture("run-1", "2026-07-10T14:00:00+00:00")
        self.assertFalse(created)
        self.assertEqual(
            self.con.execute("SELECT COUNT(*) FROM oos_signal_snapshots").fetchone()[0], 2)
        self.assertEqual(
            self.con.execute("SELECT COUNT(*) FROM oos_ranking_view_snapshots").fetchone()[0], 2)

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

    def test_documented_zero_trade_stock_uses_eligible_universe(self):
        self.con.execute("DELETE FROM daily_scores WHERE stock_id='1002'")
        self.con.execute("DELETE FROM daily_metrics WHERE stock_id='1002'")
        self.con.execute("DELETE FROM chip_health WHERE stock_id='1002'")
        self.con.execute("DELETE FROM inst WHERE stock_id='1002'")
        self.con.execute(
            "UPDATE price SET open=NULL,high=NULL,low=NULL,close=NULL,volume=0,amount=0,trades=0 "
            "WHERE stock_id='1002'")
        self.con.execute("INSERT INTO trading_status VALUES(?,?,?,?,?)", (
            self.date, "1002", "no_trade", "official_price_zero_trade", "官方零交易"))
        self.con.commit()

        sid, date_, created = self.capture("run-halt", "2026-07-10T14:00:00+00:00")
        self.assertEqual((sid, date_, created), ("run-halt", self.date, True))
        run = self.con.execute(
            "SELECT stock_count,quality_json FROM oos_snapshot_runs WHERE snapshot_id='run-halt'"
        ).fetchone()
        self.assertEqual(run["stock_count"], 1)
        import json
        quality = json.loads(run["quality_json"])
        self.assertEqual((quality["universe"], quality["eligible"], quality["inst"]),
                         (2, 1, 1))
        self.assertEqual(quality["excluded"][0]["stock_id"], "1002")
        self.assertEqual(quality["market_source"], "TWSE_MI_INDEX")
        self.assertEqual(quality["market_abs_diff"], 0.0)
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM oos_signal_snapshots WHERE snapshot_id='run-halt'"
        ).fetchone()[0], 1)

    def test_unverified_status_cannot_hide_active_gap(self):
        self.con.execute("DELETE FROM daily_scores WHERE stock_id='1002'")
        self.con.execute("DELETE FROM daily_metrics WHERE stock_id='1002'")
        self.con.execute("DELETE FROM inst WHERE stock_id='1002'")
        self.con.execute("INSERT INTO trading_status VALUES(?,?,?,?,?)", (
            self.date, "1002", "no_trade", "official_price_zero_trade", "錯誤標記"))
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "拒絕凍結不完整快照"):
            self.capture("run-unverified", "2026-07-10T14:00:00+00:00")

    def test_official_publish_rejects_stale_market(self):
        self.con.execute("UPDATE market_daily SET date='2026-07-09'")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "大盤資料未同步"):
            self.capture("run-market-lag", "2026-07-10T14:00:00+00:00")

    def test_official_publish_rejects_market_source_conflict(self):
        self.con.execute(
            """UPDATE market_provenance
               SET canonical_source='conflict',official_taiex=100,finmind_taiex=101,abs_diff=1""")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "來源／canonical 不一致"):
            self.capture("run-market-conflict", "2026-07-10T14:00:00+00:00")

    def test_official_publish_accepts_finmind_fallback_with_provenance(self):
        self.con.execute(
            """UPDATE market_provenance
               SET canonical_source='FinMind_fallback',official_taiex=NULL,
                   finmind_taiex=100,abs_diff=NULL""")
        self.con.commit()
        sid, _date, created = self.capture(
            "run-market-fallback", "2026-07-10T14:00:00+00:00")
        self.assertEqual((sid, created), ("run-market-fallback", True))

    def test_official_publish_rejects_missing_market_provenance_table(self):
        self.con.execute("DROP TABLE market_provenance")
        self.con.commit()
        with self.assertRaisesRegex(RuntimeError, "缺 provenance 表"):
            self.capture("run-market-no-source", "2026-07-10T14:00:00+00:00")

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
