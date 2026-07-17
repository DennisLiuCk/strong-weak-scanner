import io
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.error import HTTPError
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import fetch_daily as fd


class TokenPoolTest(unittest.TestCase):
    def setUp(self):
        self.old_tokens = fd._TOKENS
        self.old_token_i = fd._TOK_I
        self.old_disabled = fd._TOK_DISABLED
        fd._TOKENS = []
        fd._TOK_I = 0
        fd._TOK_DISABLED = set()

    def tearDown(self):
        fd._TOKENS = self.old_tokens
        fd._TOK_I = self.old_token_i
        fd._TOK_DISABLED = self.old_disabled

    def test_loads_three_distinct_tokens_and_deduplicates(self):
        env = {
            "FINMIND_TOKEN": " token-1 ",
            "FINMIND_TOKEN2": "\ufefftoken-2",
            "FINMIND_TOKEN3": "token-1",
        }
        with mock.patch.dict(os.environ, env, clear=True):
            self.assertEqual(fd.get_tokens(), ["token-1", "token-2"])

    def test_402_rotation_reaches_third_token(self):
        seen = []

        def fake_urlopen(req, timeout):
            seen.append(req.get_header("Authorization"))
            if len(seen) < 3:
                raise HTTPError(req.full_url, 402, "Payment Required", None, None)
            return io.BytesIO(b'{"data":[{"value":3}]}')

        env = {
            "FINMIND_TOKEN": "token-1",
            "FINMIND_TOKEN2": "token-2",
            "FINMIND_TOKEN3": "token-3",
        }
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch("fetch_daily.urllib.request.urlopen", side_effect=fake_urlopen):
            data = fd.api_get("dataset", "2330", "2026-07-17", "2026-07-17", "unused")
            again = fd.api_get("dataset", "2330", "2026-07-17", "2026-07-17", "unused")

        self.assertEqual(data, [{"value": 3}])
        self.assertEqual(again, [{"value": 3}])
        self.assertEqual(seen, ["Bearer token-1", "Bearer token-2",
                                "Bearer token-3", "Bearer token-3"])
        self.assertEqual(fd._TOK_DISABLED, {0, 1})

    def test_all_failed_tokens_stop_immediately_without_reuse(self):
        seen = []

        def always_402(req, timeout):
            seen.append(req.get_header("Authorization"))
            raise HTTPError(req.full_url, 402, "Payment Required", None, None)

        env = {
            "FINMIND_TOKEN": "token-1",
            "FINMIND_TOKEN2": "token-2",
            "FINMIND_TOKEN3": "token-3",
        }
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch("fetch_daily.urllib.request.urlopen", side_effect=always_402):
            with self.assertRaises(fd.TokenPoolExhausted):
                fd.api_get("dataset", "2330", "2026-07-17", "2026-07-17", "unused")

        self.assertEqual(seen, ["Bearer token-1", "Bearer token-2", "Bearer token-3"])
        self.assertEqual(fd._TOK_DISABLED, {0, 1, 2})


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

    def test_dividend_progress_is_committed_before_pool_exhaustion(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "checkpoint.db"
            con = sqlite3.connect(db)
            con.executescript(fd.SCHEMA)

            def fake_api(dataset, sid, start, end, token, return_status=False):
                if sid == "2330":
                    return [], True
                raise fd.TokenPoolExhausted("all tokens disabled")

            try:
                with mock.patch.object(fd, "api_get", side_effect=fake_api):
                    with self.assertRaises(fd.TokenPoolExhausted):
                        fd.fetch_dividends(
                            con, ["2330", "2454"], "token",
                            "2026-07-10", "2026-07-10", sleep=0)

                # 用另一條連線驗證第一檔的 coverage 已真正 commit 到檔案，不只留在 transaction。
                observer = sqlite3.connect(db)
                try:
                    self.assertEqual(
                        fd._coverage_get(observer, "TaiwanStockDividendResult", "2330"),
                        "2026-07-10")
                    self.assertIsNone(
                        fd._coverage_get(observer, "TaiwanStockDividendResult", "2454"))
                finally:
                    observer.close()
            finally:
                con.close()


class WorkflowCheckpointTest(unittest.TestCase):
    def test_failed_fetch_checkpoints_data_before_blocking_publish(self):
        workflow = (ROOT / ".github" / "workflows" / "daily-fetch.yml").read_text(
            encoding="utf-8")

        fetch_at = workflow.index("- name: 抓取五元素並重算 daily_metrics")
        checkpoint_at = workflow.index("- name: 保存未完成抓取進度")
        stop_at = workflow.index("- name: 抓取未完成，停止後續發布")
        score_at = workflow.index("- name: 計算五元素分數與 tier")
        self.assertLess(fetch_at, checkpoint_at)
        self.assertLess(checkpoint_at, stop_at)
        self.assertLess(stop_at, score_at)

        fetch_block = workflow[fetch_at:checkpoint_at]
        checkpoint_block = workflow[checkpoint_at:stop_at]
        stop_block = workflow[stop_at:score_at]
        self.assertIn("id: fetch_daily", fetch_block)
        self.assertIn("continue-on-error: true", fetch_block)
        self.assertIn("steps.fetch_daily.outcome == 'failure'", checkpoint_block)
        self.assertIn("git add data/", checkpoint_block)
        self.assertIn("每日抓取進度（未完成）", checkpoint_block)
        self.assertNotIn("index.html", checkpoint_block)
        self.assertIn("steps.fetch_daily.outcome == 'failure'", stop_block)
        self.assertIn("exit 1", stop_block)


if __name__ == "__main__":
    unittest.main()
