import sqlite3
import sys
import unittest
from contextlib import closing
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import fetch_daily as fd
import fetch_tdcc


class TdccMetricsTest(unittest.TestCase):
    def metrics(self, missing=None, null_pct=False, empty=False, zero=False):
        with closing(sqlite3.connect(":memory:")) as con:
            con.executescript(fd.SCHEMA)
            con.execute(fetch_tdcc.SCHEMA)
            con.execute("INSERT INTO universe VALUES('A','測試','g','biz')")
            con.execute("INSERT INTO price(date,stock_id,close,volume) "
                        "VALUES('2026-07-13','A',10,100)")
            for week, day in enumerate(("2026-07-03", "2026-07-10")):
                for level in range(1, 18):
                    if empty or missing == (week, level):
                        continue
                    pct = 0.0 if zero else float(level + week)
                    if null_pct and week == 1 and level == 15:
                        pct = None
                    con.execute("INSERT INTO tdcc_holding VALUES(?,?,?,?,?,?)",
                                (day, "A", level, 100, 1000, pct))
            fd.build_metrics(con)
            return con.execute("SELECT tdcc_date,tdcc_big400_pct,tdcc_big1000_pct,"
                               "tdcc_big400_chg,tdcc_big1000_chg FROM daily_metrics").fetchone()

    def test_complete_and_zero_snapshots(self):
        self.assertEqual(self.metrics(), ("2026-07-10", 58.0, 16.0, 4.0, 1.0))
        self.assertEqual(self.metrics(zero=True), ("2026-07-10", 0.0, 0.0, 0.0, 0.0))

    def test_empty_snapshots(self):
        self.assertEqual(self.metrics(empty=True), (None,) * 5)

    def test_missing_current_level_invalidates_concentrations(self):
        for level in range(1, 18):
            with self.subTest(level=level):
                self.assertEqual(self.metrics(missing=(1, level)),
                                 ("2026-07-10", None, None, None, None))

    def test_missing_comparison_level_invalidates_changes(self):
        for level in range(1, 18):
            with self.subTest(level=level):
                self.assertEqual(self.metrics(missing=(0, level)),
                                 ("2026-07-10", 58.0, 16.0, None, None))

    def test_null_required_percentage_is_not_zero(self):
        self.assertEqual(self.metrics(null_pct=True),
                         ("2026-07-10", None, None, None, None))
