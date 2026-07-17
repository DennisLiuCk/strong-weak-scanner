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


class OfficialPriceBatchTest(unittest.TestCase):
    def test_parse_twse_filters_universe_and_normalizes_numbers(self):
        payload = {
            "stat": "OK",
            "date": "20260717",
            "tables": [{
                "fields": [
                    "證券代號", "證券名稱", "成交股數", "成交筆數", "成交金額",
                    "開盤價", "最高價", "最低價", "收盤價",
                ],
                "data": [
                    ["2330", "台積電", "12,345", "100", "12,345,000",
                     "1,000.00", "1,020.00", "995.00", "1,010.00"],
                    ["1101", "台泥", "200", "10", "8,000",
                     "40.00", "41.00", "39.50", "40.50"],
                ],
            }],
        }

        rows, has_market_data = fd.parse_twse_price(
            payload, "2026-07-17", {"2330"})

        self.assertTrue(has_market_data)
        self.assertEqual(rows, [{
            "date": "2026-07-17",
            "stock_id": "2330",
            "open": 1000.0,
            "max": 1020.0,
            "min": 995.0,
            "close": 1010.0,
            "Trading_Volume": 12345,
            "Trading_money": 12345000.0,
        }])

    def test_parse_twse_no_data_is_a_holiday_not_an_error(self):
        rows, has_market_data = fd.parse_twse_price(
            {"stat": "很抱歉，沒有符合條件的資料!", "date": ""},
            "2026-07-18", {"2330"})
        self.assertEqual(rows, [])
        self.assertFalse(has_market_data)

    def test_parse_tpex_empty_daily_tables_are_a_holiday(self):
        payload = {
            "stat": "ok",
            "date": "20260718",
            "tables": [{
                "fields": [
                    "代號", "收盤", "開盤", "最高", "最低", "成交股數", "成交金額(元)",
                ],
                "data": [],
            }],
        }
        rows, has_market_data = fd.parse_tpex_price(
            payload, "2026-07-18", {"2454"})
        self.assertEqual(rows, [])
        self.assertFalse(has_market_data)

    def test_parse_tpex_reads_all_matching_tables_and_handles_no_trade(self):
        fields = [
            "代號", "名稱", "收盤", "漲跌", "開盤", "最高", "最低", "均價",
            "成交股數", "成交金額(元)",
        ]
        payload = {
            "stat": "ok",
            "date": "20260717",
            "tables": [
                {"fields": fields, "data": [
                    ["2454", "聯發科", "1,310.00", "+10", "1,300.00",
                     "1,320.00", "1,295.00", "1,308.00", "9,876", "12,345,678"],
                ]},
                {"fields": fields, "data": [
                    ["9999", "測試", "--", "--", "--", "--", "--", "--", "0", "0"],
                ]},
            ],
        }

        rows, has_market_data = fd.parse_tpex_price(
            payload, "2026-07-17", {"2454", "9999"})

        self.assertTrue(has_market_data)
        self.assertEqual(rows[0]["stock_id"], "2454")
        self.assertEqual(rows[0]["close"], 1310.0)
        self.assertEqual(rows[0]["Trading_Volume"], 9876)
        self.assertEqual(rows[0]["Trading_money"], 12345678.0)
        self.assertEqual(rows[1]["stock_id"], "9999")
        self.assertIsNone(rows[1]["open"])
        self.assertIsNone(rows[1]["close"])
        self.assertEqual(rows[1]["Trading_Volume"], 0)

    def test_successful_market_is_committed_before_other_market_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "price-checkpoint.db"
            con = sqlite3.connect(db)
            con.executescript(fd.SCHEMA)
            calls = []

            def partial_fetch(source, day, wanted_ids):
                calls.append((source, day, set(wanted_ids)))
                if source == "TPEx":
                    raise OSError("temporary TPEx failure")
                return [{
                    "date": day, "stock_id": "2330", "open": 1000,
                    "max": 1020, "min": 995, "close": 1010,
                    "Trading_Volume": 12345, "Trading_money": 12345000,
                }], True

            try:
                with self.assertRaises(fd.ExchangePriceFetchError):
                    fd.fetch_exchange_prices(
                        con, ["2330", "2454"], {"2026-07-17"},
                        fetcher=partial_fetch)

                observer = sqlite3.connect(db)
                try:
                    self.assertEqual(observer.execute(
                        "SELECT stock_id,close FROM price WHERE date='2026-07-17'"
                    ).fetchall(), [("2330", 1010.0)])
                finally:
                    observer.close()
            finally:
                con.close()

        self.assertEqual([call[0] for call in calls], ["TWSE", "TPEx"])


class OfficialRawBatchTest(unittest.TestCase):
    @staticmethod
    def _nets(rows):
        return {row["name"]: row["buy"] - row["sell"] for row in rows}

    def test_institutional_parsers_map_exact_net_columns(self):
        twse_fields = [
            "證券代號", "外陸資買賣超股數(不含外資自營商)",
            "投信買賣超股數", "自營商買賣超股數",
        ]
        twse = {"stat": "OK", "date": "20260717", "fields": twse_fields,
                "data": [["2330", "1,200", "-300", "45"]]}
        rows, available = fd.parse_twse_inst(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual(self._nets(rows), {
            "Foreign_Investor": 1200, "Investment_Trust": -300, "Dealer_self": 45})

        tpex_fields = ["代號", "名稱"] + ["欄"] * 21 + ["三大法人買賣超股數合計"]
        raw = ["2454", "聯發科"] + ["0"] * 22
        raw[4], raw[13], raw[22] = "-900", "700", "-50"
        tpex = {"stat": "ok", "date": "20260717",
                "tables": [{"fields": tpex_fields, "data": [raw]}]}
        rows, available = fd.parse_tpex_inst(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual(self._nets(rows), {
            "Foreign_Investor": -900, "Investment_Trust": 700, "Dealer_self": -50})

    def test_margin_parsers_map_current_balances(self):
        twse_fields = ["代號", "名稱", "買進", "賣出", "現金償還", "前日餘額",
                       "今日餘額", "次一營業日限額", "買進", "賣出", "現券償還",
                       "前日餘額", "今日餘額", "次一營業日限額", "資券互抵", "註記"]
        twse_raw = ["2330", "台積電"] + ["0"] * 14
        twse_raw[6], twse_raw[12] = "12,345", "678"
        twse = {"stat": "OK", "date": "20260717",
                "tables": [{"fields": twse_fields, "data": [twse_raw]}]}
        rows, available = fd.parse_twse_margin(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["MarginPurchaseTodayBalance"],
                          rows[0]["ShortSaleTodayBalance"]), (12345, 678))

        tpex = {"stat": "ok", "date": "20260717", "tables": [{
            "fields": ["代號", "資餘額", "券餘額"],
            "data": [["2454", "9,876", "54"]],
        }]}
        rows, available = fd.parse_tpex_margin(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["MarginPurchaseTodayBalance"],
                          rows[0]["ShortSaleTodayBalance"]), (9876, 54))

    def test_holding_parsers_map_percentage_and_issued_shares(self):
        twse = {"stat": "OK", "date": "20260717",
                "fields": ["證券代號", "發行股數", "全體外資及陸資持股比率"],
                "data": [["2330", "25,933,804,458", "72.54"]]}
        rows, available = fd.parse_twse_holding(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["ForeignInvestmentSharesRatio"],
                          rows[0]["NumberOfSharesIssued"]), (72.54, 25933804458))

        tpex = {"stat": "ok", "date": "20260717", "tables": [{
            "fields": ["代號", "發行股數(A)", "僑外資及陸資持股比率(E=C/A)"],
            "data": [["2454", "1,591,673,608", "58.12%"]],
        }]}
        rows, available = fd.parse_tpex_holding(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["ForeignInvestmentSharesRatio"],
                          rows[0]["NumberOfSharesIssued"]), (58.12, 1591673608))

    def test_sbl_parsers_use_borrowed_short_sale_current_balance(self):
        fields = ["代號", "名稱"] + ["欄"] * 10 + ["當日餘額"]
        raw = ["2330", "台積電"] + ["0"] * 10 + ["8,765,432"]
        twse = {"stat": "OK", "date": "20260717", "fields": fields, "data": [raw]}
        rows, available = fd.parse_twse_sbl(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual(rows[0]["SBLShortSalesCurrentDayBalance"], 8765432)

        tpex_fields = ["股票代號", "股票名稱"] + ["欄"] * 10 + ["當日餘額"]
        tpex_raw = ["2454", "聯發科"] + ["0"] * 10 + ["123,456"]
        tpex = {"stat": "ok", "date": "20260717",
                "tables": [{"fields": tpex_fields, "data": [tpex_raw]}]}
        rows, available = fd.parse_tpex_sbl(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual(rows[0]["SBLShortSalesCurrentDayBalance"], 123456)

    def test_wrong_response_date_is_rejected(self):
        payload = {"stat": "OK", "date": "20260716", "fields": [], "data": []}
        with self.assertRaises(ValueError):
            fd.parse_twse_inst(payload, "2026-07-17", {"2330"})

    def test_successful_market_is_committed_before_other_raw_market_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            db = Path(tmp) / "raw-checkpoint.db"
            con = sqlite3.connect(db)
            con.executescript(fd.SCHEMA)

            def partial_fetch(dataset, source, day, wanted_ids):
                if source == "TPEx":
                    raise OSError("temporary TPEx failure")
                return [
                    {"date": day, "stock_id": "2330", "name": "Foreign_Investor",
                     "buy": 10, "sell": 2},
                ], True

            try:
                with self.assertRaises(fd.ExchangeRawFetchError):
                    fd.fetch_exchange_raw_dataset(
                        con, ["2330", "2454"],
                        "TaiwanStockInstitutionalInvestorsBuySell", {"2026-07-17"},
                        fetcher=partial_fetch)
                observer = sqlite3.connect(db)
                try:
                    self.assertEqual(observer.execute(
                        "SELECT stock_id,foreign_net FROM inst WHERE date='2026-07-17'"
                    ).fetchall(), [("2330", 8)])
                finally:
                    observer.close()
            finally:
                con.close()


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
        self.price_calls = []

    def tearDown(self):
        self.con.close()

    def fake_fetch(self, dataset, source, day, wanted_ids):
        self.calls.append((dataset, source, day, set(wanted_ids)))
        sid = "2330" if source == "TWSE" else "2454"
        if sid not in wanted_ids:
            return [], True
        if dataset == "TaiwanStockInstitutionalInvestorsBuySell":
            return [{"date": day, "stock_id": sid, "name": "Foreign_Investor",
                     "buy": 10, "sell": 2}], True
        if dataset == "TaiwanStockMarginPurchaseShortSale":
            return [{"date": day, "stock_id": sid,
                     "MarginPurchaseTodayBalance": 10, "ShortSaleTodayBalance": 1}], True
        if dataset == "TaiwanStockShareholding":
            return [{"date": day, "stock_id": sid,
                     "ForeignInvestmentSharesRatio": 20, "NumberOfSharesIssued": 1000}], True
        if dataset == "TaiwanDailyShortSaleBalances":
            return [{"date": day, "stock_id": sid,
                     "SBLShortSalesCurrentDayBalance": 10}], True
        raise AssertionError(dataset)

    def fake_price_fetch(self, source, day, wanted_ids):
        self.price_calls.append((source, day, set(wanted_ids)))
        if day != "2026-07-10":
            return [], False
        sid = "2330" if source == "TWSE" else "2454"
        rows = [{
            "date": day, "stock_id": sid, "open": 2, "max": 3,
            "min": 2, "close": 3, "Trading_Volume": 100,
            "Trading_money": 300,
        }] if sid in wanted_ids else []
        return rows, True

    def test_holiday_repeat_uses_one_daily_batch_per_market(self):
        def empty_fetch(dataset, source, day, wanted_ids):
            self.calls.append((dataset, source, day, set(wanted_ids)))
            return [], False

        def empty_price(source, day, wanted_ids):
            self.price_calls.append((source, day, set(wanted_ids)))
            return [], False

        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=empty_fetch, price_fetcher=empty_price)
        self.assertEqual(stats["requests"], 2)
        self.assertEqual(stats["finmind_requests"], 0)
        self.assertEqual(stats["exchange_requests"], 2)
        self.assertEqual(stats["probe_requests"], 2)
        self.assertEqual(stats["skipped_batches"], 4)
        self.assertEqual(stats["rows"], 0)

    def test_new_trading_day_expands_only_missing_pairs(self):
        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=self.fake_fetch, price_fetcher=self.fake_price_fetch)
        # 價格 + 其餘四張原始表，各自 TWSE/TPEx 各 1 次。
        self.assertEqual(stats["requests"], 10)
        self.assertEqual(stats["finmind_requests"], 0)
        self.assertEqual(stats["exchange_requests"], 10)
        self.assertEqual(stats["probe_requests"], 2)
        self.assertEqual(stats["skipped_batches"], 0)
        self.assertEqual(stats["new_dates"], {"2026-07-10"})
        for table in fd.DATASET_TABLE.values():
            n = self.con.execute(f"SELECT COUNT(*) FROM {table} WHERE date='2026-07-10'").fetchone()[0]
            self.assertEqual(n, 2, table)

    def test_market_date_reveals_global_price_gap_without_probe(self):
        self.con.execute("INSERT INTO market VALUES('2026-07-10',100)")
        self.con.commit()
        stats = fd.fetch_missing_raw(
            self.con, self.ids, ["TaiwanStockPrice"], "2026-07-08", "2026-07-10", "token",
            sleep=0, fetcher=self.fake_fetch, price_fetcher=self.fake_price_fetch)
        self.assertEqual(stats["probe_requests"], 0)
        self.assertEqual(stats["requests"], 2)
        self.assertEqual(stats["finmind_requests"], 0)
        self.assertEqual(stats["exchange_requests"], 2)
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM price WHERE date='2026-07-10'").fetchone()[0], 2)

    def test_only_existing_gap_is_requested(self):
        self.con.execute("DELETE FROM holding WHERE date='2026-07-09' AND stock_id='2454'")
        self.con.commit()
        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-09", "token",
            sleep=0, fetcher=self.fake_fetch, price_fetcher=self.fake_price_fetch)
        self.assertEqual(stats["requests"], 2)
        self.assertEqual(stats["probe_requests"], 0)
        self.assertEqual(stats["skipped_batches"], 3)
        self.assertEqual(self.price_calls, [])
        self.assertEqual(self.calls, [
            ("TaiwanStockShareholding", "TWSE", "2026-07-09", {"2454"}),
            ("TaiwanStockShareholding", "TPEx", "2026-07-09", {"2454"}),
        ])

    def test_final_pass_refreshes_latest_holding_once(self):
        calls = []

        def final_holding(dataset, source, day, wanted_ids):
            calls.append((dataset, source, day, set(wanted_ids)))
            sid = "2330" if source == "TWSE" else "2454"
            pct = 30 if source == "TWSE" else 40
            return ([{"date": day, "stock_id": sid,
                      "ForeignInvestmentSharesRatio": pct,
                      "NumberOfSharesIssued": 2000}], True)

        stats = fd.fetch_missing_raw(
            self.con, self.ids, ["TaiwanStockShareholding"],
            "2026-07-09", "2026-07-09", None, sleep=0,
            fetcher=final_holding, final_pass=True)

        self.assertEqual(stats["requests"], 2)
        self.assertEqual(self.con.execute(
            "SELECT stock_id,foreign_pct,shares_issued FROM holding "
            "WHERE date='2026-07-09' ORDER BY stock_id").fetchall(),
            [("2330", 30.0, 2000), ("2454", 40.0, 2000)])
        self.assertEqual(fd._coverage_get(
            self.con, "exchange_final", "TaiwanStockShareholding"), "2026-07-09")

        calls.clear()
        repeat = fd.fetch_missing_raw(
            self.con, self.ids, ["TaiwanStockShareholding"],
            "2026-07-09", "2026-07-09", None, sleep=0,
            fetcher=final_holding, final_pass=True)
        self.assertEqual(repeat["requests"], 0)
        self.assertEqual(calls, [])

    def test_incomplete_price_batch_checkpoints_and_stops_before_other_raw_tables(self):
        def incomplete_price(source, day, wanted_ids):
            if source == "TWSE":
                return [{
                    "date": day, "stock_id": "2330", "open": 2, "max": 3,
                    "min": 2, "close": 3, "Trading_Volume": 100,
                    "Trading_money": 300,
                }], True
            return [], True

        with self.assertRaises(fd.ExchangePriceFetchError):
            fd.fetch_missing_raw(
                self.con, self.ids, fd.DATASETS,
                "2026-07-08", "2026-07-10", "token", sleep=0,
                fetcher=self.fake_fetch, price_fetcher=incomplete_price)
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM price WHERE date='2026-07-10'").fetchone()[0], 1)
        self.assertEqual(self.calls, [])

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

        fetch_at = workflow.index("- name: 抓取本階段原始資料")
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
        self.assertIn('cron: "17 12 * * 1-5"', workflow)
        self.assertIn('cron: "40 15 * * 1-5"', workflow)
        self.assertIn("--raw-only", fetch_block)
        self.assertIn("--final-pass", fetch_block)
        self.assertIn("steps.mode.outputs.mode == 'complete'", workflow[score_at:])


class RawOnlyModeTest(unittest.TestCase):
    def test_raw_only_needs_no_token_and_skips_derived_rebuild(self):
        stats = {
            "rows": 0, "finmind_requests": 0, "exchange_requests": 0,
            "probe_requests": 0, "skipped_batches": 2, "expected_dates": set(),
        }
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "raw-only.db")
            argv = [
                "fetch_daily.py", "--start", "2026-07-18", "--end", "2026-07-18",
                "--datasets",
                "TaiwanStockPrice,TaiwanStockInstitutionalInvestorsBuySell",
                "--raw-only",
            ]
            with mock.patch.object(fd, "DB", db), \
                    mock.patch.object(sys, "argv", argv), \
                    mock.patch.object(fd, "load_universe", return_value=[]), \
                    mock.patch.object(fd, "fetch_missing_raw", return_value=stats), \
                    mock.patch.object(fd, "get_token") as get_token, \
                    mock.patch.object(fd, "build_metrics") as build_metrics:
                fd.main()

            get_token.assert_not_called()
            build_metrics.assert_not_called()


if __name__ == "__main__":
    unittest.main()
