"""現有成員缺資料時不得續留或中斷報告。"""
from contextlib import closing
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

from test_screen_cli import run

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from screen import CAP_IN, CAP_OUT, LIQ_MIN, verdict_member


class ScreenMissingDataTest(unittest.TestCase):
    def test_member_verdict_requires_both_metrics(self):
        for cap, liq in ((None, None), (None, LIQ_MIN), (CAP_IN, None),
                         (0, None)):
            with self.subTest(cap=cap, liq=liq):
                verdict, reasons = verdict_member(cap, liq)
                self.assertEqual(verdict, "⚪ 資料不足")
                self.assertTrue(reasons)

    def test_complete_member_verdicts_are_unchanged(self):
        for cap, liq, expected in (
                (CAP_IN, LIQ_MIN, "✅ 續留"),
                (CAP_OUT, LIQ_MIN, "👀 緩衝觀察"),
                (CAP_IN, 0, "👀 緩衝觀察"),
                (0, LIQ_MIN, "🔻 建議剔除")):
            with self.subTest(cap=cap, liq=liq):
                self.assertEqual(verdict_member(cap, liq)[0], expected)

    def test_report_handles_missing_price_and_holding_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            db = Path(directory) / "screen.db"
            # SQLite's transaction context does not close the connection; close
            # this temporary fixture before Windows attempts to remove its file.
            with closing(sqlite3.connect(db)) as con, con:
                con.executescript("""
                    CREATE TABLE groups (grp TEXT, ord INTEGER);
                    CREATE TABLE universe (stock_id TEXT, name TEXT, grp TEXT, biz TEXT);
                    CREATE TABLE price (stock_id TEXT, date TEXT, close REAL, amount REAL);
                    CREATE TABLE holding (stock_id TEXT, date TEXT, shares_issued REAL);
                    INSERT INTO groups VALUES ('test', 1);
                    INSERT INTO universe VALUES ('0001', 'MissingBoth', 'test', '');
                    INSERT INTO universe VALUES ('0002', 'MissingHolding', 'test', '');
                    INSERT INTO universe VALUES ('0003', 'MissingPrice', 'test', '');
                    INSERT INTO universe VALUES ('0004', 'Complete', 'test', '');
                    INSERT INTO price VALUES ('0002', '2026-01-01', 100, 30000000);
                    INSERT INTO price VALUES ('0004', '2026-01-01', 100, 30000000);
                    INSERT INTO holding VALUES ('0003', '2026-01-01', 50000000);
                    INSERT INTO holding VALUES ('0004', '2026-01-01', 50000000);
                """)
            result = run("--db", str(db), "--no-candidates", "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            for sid, name, metrics in (
                    ('0001', 'MissingBoth', '— | —'),
                    ('0002', 'MissingHolding', '— | 30M'),
                    ('0003', 'MissingPrice', '— | —')):
                self.assertIn(f"| {sid} | {name} | test | {metrics} | ⚪ 資料不足",
                              result.stdout)
            self.assertIn("| 0004 | Complete | test | 50 | 30M | ✅ 續留 |",
                          result.stdout)


if __name__ == "__main__":
    unittest.main()
