import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_daily as fd


class IncrementalFetchTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.executescript(fd.SCHEMA)
        self.ids = ["2330", "2454"]
        for day in ("2026-07-08", "2026-07-09"):
            for sid in self.ids:
                self.con.execute("INSERT INTO price VALUES(?,?,?,?,?,?,?,?)",
                                 (day, sid, 1, 2, 1, 2, 100, 200))
                self.con.execute("INSERT INTO inst VALUES(?,?,?,?,?)", (day, sid, 1, 2, 3))
                self.con.execute("INSERT INTO margin VALUES(?,?,?,?)", (day, sid, 10, 1))
                self.con.execute("INSERT INTO holding VALUES(?,?,?,?)", (day, sid, 20, 1000))
                self.con.execute("INSERT INTO sbl VALUES(?,?,?)", (day, sid, 10))
        self.con.commit()
        self.calls = []

    def tearDown(self):
        self.con.close()

    def fake_fetch(self, dataset, sid, start, end, token):
        self.calls.append((dataset, sid, start, end))
        if end != "2026-07-10":
            return []
        if dataset == "TaiwanStockPrice":
            return [{"date": "2026-07-10", "stock_id": sid, "open": 2, "max": 3,
                     "min": 2, "close": 3, "Trading_Volume": 100,
                     "Trading_money": 300}]
        if dataset == "TaiwanStockInstitutionalInvestorsBuySell":
            return [{"date": "2026-07-10", "stock_id": sid, "name": "Foreign_Investor",
                     "buy": 10, "sell": 2}]
        if dataset == "TaiwanStockMarginPurchaseShortSale":
            return [{"date": "2026-07-10", "stock_id": sid,
                     "MarginPurchaseTodayBalance": 10, "ShortSaleTodayBalance": 1}]
        if dataset == "TaiwanStockShareholding":
            return [{"date": "2026-07-10", "stock_id": sid,
                     "ForeignInvestmentSharesRatio": 20, "NumberOfSharesIssued": 1000}]
        if dataset == "TaiwanDailyShortSaleBalances":
            return [{"date": "2026-07-10", "stock_id": sid,
                     "SBLShortSalesCurrentDayBalance": 10}]
        raise AssertionError(dataset)

    def test_holiday_repeat_uses_only_one_probe(self):
        def empty_fetch(dataset, sid, start, end, token):
            self.calls.append((dataset, sid, start, end))
            return []

        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=empty_fetch)
        self.assertEqual(stats["requests"], 1)
        self.assertEqual(stats["probe_requests"], 1)
        self.assertEqual(stats["skipped_pairs"], 10)
        self.assertEqual(stats["rows"], 0)

    def test_new_trading_day_expands_only_missing_pairs(self):
        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=self.fake_fetch)
        # 1 次價格探針 + 其餘 9 個缺口；探針結果直接落地，不再抓 2330 price。
        self.assertEqual(stats["requests"], 10)
        self.assertEqual(stats["probe_requests"], 1)
        self.assertEqual(stats["skipped_pairs"], 1)
        self.assertEqual(stats["new_dates"], {"2026-07-10"})
        for table in fd.DATASET_TABLE.values():
            n = self.con.execute(f"SELECT COUNT(*) FROM {table} WHERE date='2026-07-10'").fetchone()[0]
            self.assertEqual(n, 2, table)

    def test_market_date_reveals_global_price_gap_without_probe(self):
        self.con.execute("INSERT INTO market VALUES('2026-07-10',100)")
        self.con.commit()
        stats = fd.fetch_missing_raw(
            self.con, self.ids, ["TaiwanStockPrice"], "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=self.fake_fetch)
        self.assertEqual(stats["probe_requests"], 0)
        self.assertEqual(stats["requests"], 2)
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM price WHERE date='2026-07-10'").fetchone()[0], 2)

    def test_only_existing_gap_is_requested(self):
        self.con.execute("DELETE FROM holding WHERE date='2026-07-09' AND stock_id='2454'")
        self.con.commit()
        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-09", "token",
            sleep=0, fetcher=self.fake_fetch)
        self.assertEqual(stats["requests"], 1)
        self.assertEqual(stats["probe_requests"], 0)
        self.assertEqual(self.calls, [
            ("TaiwanStockShareholding", "2454", "2026-07-09", "2026-07-09")])

    def test_coverage_migration_does_not_trust_legacy_empty_risk_flags(self):
        fd.initialize_fetch_coverage(self.con, self.ids, "2026-07-09")
        self.assertIsNone(fd._coverage_get(self.con, "risk_flags", "*"))
        self.assertEqual(fd._coverage_get(
            self.con, "TaiwanStockSplitPrice", "*"), "2026-07-09")

    def test_technical_windows_require_full_samples(self):
        values = list(range(1, 61))
        self.assertIsNone(fd._window_mean(values, 3, 5))
        self.assertEqual(fd._window_mean(values, 4, 5), 3)
        self.assertEqual(fd._window_mean(values, 59, 60), 30.5)
        values[58] = None
        self.assertIsNone(fd._window_mean(values, 59, 60))

    def test_wilder_rsi_handles_trending_and_flat_prices(self):
        rising = fd._wilder_rsi(list(range(1, 17)), 14)
        flat = fd._wilder_rsi([10] * 16, 14)
        self.assertIsNone(rising[13])
        self.assertEqual(rising[14], 100.0)
        self.assertEqual(flat[14], 50.0)


if __name__ == "__main__":
    unittest.main()
