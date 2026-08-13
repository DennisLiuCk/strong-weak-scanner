# -*- coding: utf-8 -*-
"""平行視角健康稽核的 exact-census 與 append-only 契約。"""
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import audit_ranking_views as audit
import ranking_views as rv


def view_row(stock_id, grp, value, *, pareto=False, sensitivity=0, role=False):
    return {
        "stock_id": stock_id,
        "grp": grp,
        "champion_pct": value,
        "lens_a": value,
        "lens_b": 100 - value,
        "lens_c": value,
        "lens_d": value,
        "a_components": {"short": value, "swing": value, "trend": value},
        "b_components": {
            "resilience": value, "leverage_safety": value, "heat_safety": value,
        },
        "c_components": {"core": value, "tdcc": None, "sbl_relief": None},
        "d_components": {
            "revenue_3m_yoy": value, "revenue_accel": value,
            "operating_margin": value, "operating_margin_yoy_delta": value,
        },
        "consensus_count": 3 if value >= 80 else 0,
        "pareto": pareto,
        "peer_sensitivity": sensitivity,
        "role_pct": value if role else None,
    }


class CurrentCensusTest(unittest.TestCase):
    def test_ties_are_counted_within_group_not_across_groups(self):
        rows = []
        for grp in ("g1", "g2"):
            rows.extend(view_row(f"{grp}-{i}", grp, value) for i, value in enumerate(
                (0, 50, 100)
            ))
        result = audit.analyze_rows(rows)
        self.assertEqual(result["stocks"], 6)
        self.assertEqual(result["groups"], 2)
        self.assertEqual(result["tie_exposed"]["lens_a"], 0)
        self.assertEqual(result["median_unique_share_by_group"]["lens_a"], 1.0)

        rows[1]["lens_a"] = 0
        result = audit.analyze_rows(rows)
        self.assertEqual(result["tie_exposed"]["lens_a"], 2)
        self.assertEqual(result["tie_rate"]["lens_a"], round(2 / 6, 4))

    def test_health_counts_are_exact_and_component_specific(self):
        rows = [
            view_row("A", "g", 100, pareto=True, sensitivity=25, role=True),
            view_row("B", "g", 50),
            view_row("C", "g", 0),
            view_row("D", "g", 80, pareto=True, role=True),
        ]
        rows[-1]["d_components"]["revenue_accel"] = None
        result = audit.analyze_rows(rows)
        self.assertEqual(result["coverage"]["lens_d"], 4)
        self.assertEqual(result["component_coverage"]["lens_d"]["revenue_accel"], 3)
        self.assertEqual(result["consensus2"], 2)
        self.assertEqual(result["pareto"], 2)
        self.assertEqual(result["peer_sensitivity_ge_25"], 1)
        self.assertEqual(result["role_rank_coverage"], 2)

    def test_formal_structure_keeps_groups_equal_weight_and_tracks_retention(self):
        day1 = [
            view_row("A", "g1", 0), view_row("B", "g1", 50),
            view_row("C", "g1", 100),
            view_row("D", "g2", 0), view_row("E", "g2", 50),
            view_row("F", "g2", 100),
        ]
        day2 = [dict(row) for row in day1]
        for row in day2:
            row["lens_d"] = 100 - row["lens_d"]
        result = audit.formal_structure({"2026-08-01": day1, "2026-08-02": day2})
        self.assertEqual(result["days"], 2)
        self.assertFalse(result["performance_claim"])
        self.assertEqual(
            result["pairwise_rank_correlation_equal_group_weight"]
            ["lens_a__lens_c"]["median"],
            1.0,
        )
        self.assertEqual(
            result["adjacent_snapshot_top20_retention"]["lens_a"]["days"], 1
        )
        self.assertEqual(result["tie_rate"]["lens_a"]["latest"], 0.0)


class FormalProgressTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.con.executescript("""
          CREATE TABLE oos_snapshot_runs(
            snapshot_id TEXT PRIMARY KEY,data_date TEXT,captured_at TEXT,
            stock_count INTEGER,is_official INTEGER);
          CREATE TABLE oos_ranking_view_snapshots(
            snapshot_id TEXT,date TEXT,stock_id TEXT,grp TEXT,spec_sha TEXT,
            payload_json TEXT);
          CREATE TABLE price_adj(date TEXT,stock_id TEXT,close_adj REAL);
        """)
        for day in range(1, 8):
            self.con.execute(
                "INSERT INTO price_adj VALUES(?,?,?)", (f"2026-08-{day:02d}", "A", 10)
            )

    def tearDown(self):
        self.con.close()

    def add_run(self, run_id, date, captured, spec, *, expected=2, actual=2):
        self.con.execute(
            "INSERT INTO oos_snapshot_runs VALUES(?,?,?,?,1)",
            (run_id, date, captured, expected),
        )
        for index in range(actual):
            row = view_row(chr(65 + index), "g", index * 100)
            self.con.execute(
                "INSERT INTO oos_ranking_view_snapshots VALUES(?,?,?,?,?,?)",
                (run_id, date, row["stock_id"], "g", spec,
                 json.dumps(row, ensure_ascii=False)),
            )

    def test_progress_keeps_old_spec_separate_and_uses_earliest_run(self):
        self.add_run("old", "2026-08-01", "2026-08-01T12:00:00Z", "old-spec")
        self.add_run("current", "2026-08-02", "2026-08-02T12:00:00Z", rv.SPEC_SHA)
        # 同日較晚 revision 不可取代 validate.py 認定的首次正式發布。
        self.add_run("later", "2026-08-02", "2026-08-02T13:00:00Z", "other-spec")
        result = audit.formal_progress(self.con, rv.SPEC_SHA, fwd=2)
        self.assertEqual(result["canonical_official_days"], 2)
        self.assertEqual(result["historical_other_spec_days"], 1)
        self.assertEqual(result["current_spec_days"], 1)
        self.assertEqual(result["current_spec_latest_date"], "2026-08-02")
        self.assertEqual(result["mature_10d_days"], 1)
        self.assertEqual(result["invalid_runs"], [])
        self.assertEqual(result["structural_history"]["days"], 1)

    def test_incomplete_snapshot_is_reported_as_invalid(self):
        self.add_run(
            "broken", "2026-08-03", "2026-08-03T12:00:00Z", rv.SPEC_SHA,
            expected=2, actual=1,
        )
        result = audit.formal_progress(self.con, rv.SPEC_SHA, fwd=2)
        self.assertEqual(result["current_spec_days"], 0)
        self.assertEqual(len(result["invalid_runs"]), 1)
        self.assertEqual(result["invalid_runs"][0]["actual_rows"], 1)


class OutputContractTest(unittest.TestCase):
    def test_json_writer_uses_utf8_lf(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "audit.json"
            audit.write_json(path, {"label": "多視角", "ok": True})
            raw = path.read_bytes()
        self.assertTrue(raw.endswith(b"\n"))
        self.assertNotIn(b"\r\n", raw)
        self.assertEqual(json.loads(raw), {"label": "多視角", "ok": True})

    def test_cli_source_forces_read_only_db(self):
        source = (SCRIPTS / "audit_ranking_views.py").read_text(encoding="utf-8")
        self.assertIn("db_ro.connect", source)
        self.assertNotIn("sqlite3.connect", source)


class PipelineWiringTest(unittest.TestCase):
    def test_daily_workflow_audits_published_snapshot_before_dashboard(self):
        workflow = (
            ROOT / ".github" / "workflows" / "daily-fetch.yml"
        ).read_text(encoding="utf-8")
        snapshot_at = workflow.index("python scripts/snapshot_signals.py --publish")
        audit_at = workflow.index(
            "python scripts/audit_ranking_views.py --compact "
            "--require-current-snapshot"
        )
        dashboard_at = workflow.index("python scripts/build_dashboard.py")
        self.assertLess(snapshot_at, audit_at)
        self.assertLess(audit_at, dashboard_at)
        audit_block = workflow[
            workflow.index("- name: 稽核平行視角排名快照"):dashboard_at
        ]
        self.assertIn("steps.mode.outputs.mode == 'complete'", audit_block)

    def test_local_pipeline_requires_official_snapshot_except_preview(self):
        source = (ROOT / "scripts" / "run_daily.py").read_text(encoding="utf-8")
        snapshot_at = source.index('run("snapshot_signals.py", *snapshot_args)')
        audit_at = source.index('run("audit_ranking_views.py", *audit_args)')
        dashboard_at = source.index('run("build_dashboard.py")')
        self.assertLess(snapshot_at, audit_at)
        self.assertLess(audit_at, dashboard_at)
        audit_block = source[source.index('audit_args = ["--compact"]'):audit_at]
        self.assertIn("if not args.preview:", audit_block)
        self.assertIn('audit_args.append("--require-current-snapshot")', audit_block)


if __name__ == "__main__":
    unittest.main()
