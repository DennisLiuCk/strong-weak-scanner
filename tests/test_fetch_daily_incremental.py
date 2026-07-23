import io
import os
import sqlite3
import sys
import tempfile
import unittest
from datetime import datetime, timezone
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


class SchemaMigrationTest(unittest.TestCase):
    def test_legacy_raw_tables_are_upgraded_in_place_idempotently(self):
        con = sqlite3.connect(":memory:")
        con.executescript("""
            CREATE TABLE price(date TEXT, stock_id TEXT, open REAL, high REAL, low REAL,
              close REAL, volume INTEGER, amount REAL, PRIMARY KEY(date,stock_id));
            CREATE TABLE inst(date TEXT, stock_id TEXT, foreign_net INTEGER, trust_net INTEGER,
              dealer_net INTEGER, PRIMARY KEY(date,stock_id));
            CREATE TABLE margin(date TEXT, stock_id TEXT, margin_bal INTEGER, short_bal INTEGER,
              PRIMARY KEY(date,stock_id));
            CREATE TABLE holding(date TEXT, stock_id TEXT, foreign_pct REAL, shares_issued INTEGER,
              PRIMARY KEY(date,stock_id));
            CREATE TABLE sbl(date TEXT, stock_id TEXT, sbl_bal INTEGER,
              PRIMARY KEY(date,stock_id));
            INSERT INTO price VALUES('2026-07-17','2330',1,2,1,2,100,200);
        """)

        fd.ensure_schema(con)
        fd.ensure_schema(con)

        for table, columns in fd.RAW_COLUMN_MIGRATIONS.items():
            actual = {row[1] for row in con.execute(f"PRAGMA table_info({table})")}
            self.assertTrue({name for name, _ in columns}.issubset(actual), table)
        self.assertEqual(con.execute(
            "SELECT close,volume,amount,trades FROM price WHERE stock_id='2330'"
        ).fetchone(), (2.0, 100, 200.0, None))
        self.assertIsNotNone(con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='market_index'"
        ).fetchone())
        con.close()


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
            "Trading_turnover": 100,
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
                    "成交筆數",
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
            "成交股數", "成交金額(元)", "成交筆數",
        ]
        payload = {
            "stat": "ok",
            "date": "20260717",
            "tables": [
                {"fields": fields, "data": [
                    ["2454", "聯發科", "1,310.00", "+10", "1,300.00",
                     "1,320.00", "1,295.00", "1,308.00", "9,876", "12,345,678", "321"],
                ]},
                {"fields": fields, "data": [
                    ["9999", "測試", "--", "--", "--", "--", "--", "--", "0", "0", "0"],
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
        self.assertEqual(rows[0]["Trading_turnover"], 321)
        self.assertEqual(rows[1]["stock_id"], "9999")
        self.assertIsNone(rows[1]["open"])
        self.assertIsNone(rows[1]["close"])
        self.assertEqual(rows[1]["Trading_Volume"], 0)

    def test_market_index_parsers_keep_total_return_series(self):
        twse = {
            "stat": "OK", "date": "20260717", "tables": [
                {"fields": ["指數", "收盤指數"],
                 "data": [["發行量加權股價指數", "42,671.27"]]},
                {"fields": ["報酬指數", "收盤指數"],
                 "data": [[fd.TWSE_TOTAL_RETURN_KEY, "98,228.75"],
                          ["半導體類報酬指數", "12,345.67"]]},
            ],
        }
        rows = fd.parse_twse_market_indices(twse, "2026-07-17")
        self.assertEqual([(row["index_key"], row["close"]) for row in rows], [
            (fd.TWSE_TOTAL_RETURN_KEY, 98228.75), ("半導體類報酬指數", 12345.67)])
        self.assertTrue(all(row["index_type"] == "total_return" for row in rows))

        rows = fd.parse_tpex_market_indices([
            {"Date": "1150716", "TPExIndex": "390.00",
             "TPExTotalReturnIndex": "710.25"},
            {"Date": "1150717", "TPExIndex": "378.44",
             "TPExTotalReturnIndex": "699.92"},
        ])
        self.assertEqual([(row["date"], row["index_key"], row["close"]) for row in rows], [
            ("2026-07-16", fd.TPEX_TOTAL_RETURN_KEY, 710.25),
            ("2026-07-17", fd.TPEX_TOTAL_RETURN_KEY, 699.92),
        ])

    def test_missing_twse_index_subtable_does_not_block_price(self):
        payload = {
            "stat": "OK", "date": "20260717", "tables": [{
                "fields": ["證券代號", "成交股數", "成交筆數", "成交金額", "開盤價",
                           "最高價", "最低價", "收盤價"],
                "data": [["2330", "100", "9", "200", "1", "2", "1", "2"]],
            }],
        }
        with mock.patch.object(fd, "_request_json", return_value=payload), \
                mock.patch("sys.stderr", new_callable=io.StringIO) as stderr:
            rows, available, indices = fd.fetch_exchange_price_source(
                "TWSE", "2026-07-17", {"2330"}, retries=1)
        self.assertTrue(available)
        self.assertEqual(rows[0]["close"], 2.0)
        self.assertEqual(indices, [])
        self.assertIn("market_index 順手解析失敗", stderr.getvalue())

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
                }], True, [{
                    "date": day, "market": "TWSE",
                    "index_key": fd.TWSE_TOTAL_RETURN_KEY,
                    "index_name": fd.TWSE_TOTAL_RETURN_KEY,
                    "index_type": "total_return", "close": 98228.75,
                }]

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
                    self.assertEqual(observer.execute(
                        "SELECT index_key,close FROM market_index WHERE date='2026-07-17'"
                    ).fetchall(), [(fd.TWSE_TOTAL_RETURN_KEY, 98228.75)])
                finally:
                    observer.close()
            finally:
                con.close()

        self.assertEqual([call[0] for call in calls], ["TWSE", "TPEx"])

    def test_market_index_backfill_is_latest_only_and_idempotent(self):
        con = sqlite3.connect(":memory:")
        con.executescript(fd.SCHEMA)
        calls = []

        def twse_fetch(day):
            calls.append(("TWSE", day))
            return [{
                "date": day, "market": "TWSE", "index_key": fd.TWSE_TOTAL_RETURN_KEY,
                "index_name": fd.TWSE_TOTAL_RETURN_KEY, "index_type": "total_return",
                "close": 98228.75,
            }]

        def tpex_fetch():
            calls.append(("TPEx", None))
            return [{
                "date": day, "market": "TPEx", "index_key": fd.TPEX_TOTAL_RETURN_KEY,
                "index_name": fd.TPEX_TOTAL_RETURN_KEY, "index_type": "total_return",
                "close": close,
            } for day, close in (("2026-07-16", 710.25), ("2026-07-17", 699.92))]

        stats = fd.fetch_missing_market_indices(
            con, {"2026-07-16", "2026-07-17"},
            twse_fetcher=twse_fetch, tpex_fetcher=tpex_fetch)
        self.assertEqual(stats, {"rows": 3, "requests": 2, "errors": []})
        self.assertEqual(calls, [("TWSE", "2026-07-17"), ("TPEx", None)])
        self.assertEqual(con.execute("SELECT COUNT(*) FROM market_index").fetchone()[0], 3)

        calls.clear()
        repeat = fd.fetch_missing_market_indices(
            con, {"2026-07-16", "2026-07-17"},
            twse_fetcher=twse_fetch, tpex_fetcher=tpex_fetch)
        self.assertEqual(repeat, {"rows": 0, "requests": 0, "errors": []})
        self.assertEqual(calls, [])
        con.close()

    def test_market_index_source_failures_are_reported_but_not_raised(self):
        con = sqlite3.connect(":memory:")
        con.executescript(fd.SCHEMA)

        def fail_twse(day):
            raise OSError(f"TWSE unavailable {day}")

        def fail_tpex():
            raise OSError("TPEx unavailable")

        stats = fd.fetch_missing_market_indices(
            con, {"2026-07-17"}, twse_fetcher=fail_twse, tpex_fetcher=fail_tpex)
        self.assertEqual(stats["rows"], 0)
        self.assertEqual(stats["requests"], 2)
        self.assertEqual(len(stats["errors"]), 2)
        self.assertIn("TWSE 2026-07-17", stats["errors"][0])
        self.assertIn("TPEx 2026-07-17", stats["errors"][1])
        con.close()


class OfficialRawBatchTest(unittest.TestCase):
    @staticmethod
    def _nets(rows):
        return {row["name"]: row.get("net", row["buy"] - row["sell"]) for row in rows}

    def test_institutional_parsers_map_exact_net_columns(self):
        twse_fields = [
            "證券代號",
            "外陸資買進股數(不含外資自營商)",
            "外陸資賣出股數(不含外資自營商)",
            "外陸資買賣超股數(不含外資自營商)",
            "投信買進股數", "投信賣出股數", "投信買賣超股數",
            "自營商買賣超股數",
            "自營商買進股數(自行買賣)", "自營商賣出股數(自行買賣)",
            "自營商買賣超股數(自行買賣)",
            "自營商買進股數(避險)", "自營商賣出股數(避險)",
            "自營商買賣超股數(避險)",
        ]
        twse = {"stat": "OK", "date": "20260717", "fields": twse_fields,
                "data": [["2330", "2,000", "800", "1,200", "100", "400", "-300",
                          "45", "100", "80", "20", "50", "25", "25"]]}
        rows, available = fd.parse_twse_inst(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual(self._nets(rows), {
            "Foreign_Investor": 1200, "Investment_Trust": -300,
            "Dealer_self": 20, "Dealer_Hedging": 25, "Dealer_Total": 45})
        self.assertEqual((rows[0]["buy"], rows[0]["sell"], rows[0]["net"]),
                         (2000, 800, 1200))

        triplet = ["買進股數", "賣出股數", "買賣超股數"]
        tpex_fields = ["代號", "名稱"] + triplet * 7 + ["三大法人買賣超股數合計"]
        raw = ["2454", "聯發科"] + ["0"] * 22
        raw[2:5] = ["100", "1,000", "-900"]
        raw[11:14] = ["900", "200", "700"]
        raw[14:17] = ["30", "40", "-10"]
        raw[17:20] = ["20", "60", "-40"]
        raw[20:23] = ["50", "100", "-50"]
        tpex = {"stat": "ok", "date": "20260717",
                "tables": [{"fields": tpex_fields, "data": [raw]}]}
        rows, available = fd.parse_tpex_inst(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual(self._nets(rows), {
            "Foreign_Investor": -900, "Investment_Trust": 700,
            "Dealer_self": -10, "Dealer_Hedging": -40, "Dealer_Total": -50})

    def test_margin_parsers_map_current_balances(self):
        twse_fields = ["代號", "名稱", "買進", "賣出", "現金償還", "前日餘額",
                       "今日餘額", "次一營業日限額", "買進", "賣出", "現券償還",
                       "前日餘額", "今日餘額", "次一營業日限額", "資券互抵", "註記"]
        twse_raw = ["2330", "台積電"] + ["0"] * 14
        twse_raw[2:8] = ["100", "80", "5", "12,330", "12,345", "20,000"]
        twse_raw[8:15] = ["7", "9", "1", "676", "678", "5,000", "4"]
        twse = {"stat": "OK", "date": "20260717",
                "tables": [{"fields": twse_fields, "data": [twse_raw]}]}
        rows, available = fd.parse_twse_margin(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["MarginPurchaseTodayBalance"],
                          rows[0]["ShortSaleTodayBalance"]), (12345, 678))
        self.assertEqual((rows[0]["MarginPurchasePreviousDayBalance"],
                          rows[0]["ShortSalePreviousDayBalance"]), (12330, 676))
        self.assertEqual(
            [rows[0][key] for key in ("MarginPurchaseBuy", "MarginPurchaseSell",
                                      "MarginPurchaseCashRepayment", "MarginPurchaseLimit",
                                      "ShortSaleSell", "ShortSaleBuyback",
                                      "ShortSaleStockRepayment", "ShortSaleLimit",
                                      "MarginShortOffset")],
            [100, 80, 5, 20000, 9, 7, 1, 5000, 4])

        tpex_fields = [
            "代號", "名稱", "前資餘額(張)", "資買", "資賣", "現償", "資餘額",
            "資屬證金", "資使用率(%)", "資限額", "前券餘額(張)", "券賣", "券買",
            "券償", "券餘額", "券屬證金", "券使用率(%)", "券限額",
            "資券相抵(張)", "備註",
        ]
        tpex_raw = ["2454", "聯發科", "9,850", "40", "10", "4", "9,876", "0",
                    "1.2", "20,000", "50", "8", "3", "1", "54", "0", "0.1",
                    "5,000", "2", ""]
        tpex = {"stat": "ok", "date": "20260717", "tables": [{
            "fields": tpex_fields, "data": [tpex_raw],
        }]}
        rows, available = fd.parse_tpex_margin(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["MarginPurchaseTodayBalance"],
                          rows[0]["ShortSaleTodayBalance"]), (9876, 54))
        self.assertEqual((rows[0]["MarginPurchasePreviousDayBalance"],
                          rows[0]["ShortSalePreviousDayBalance"]), (9850, 50))
        self.assertEqual((rows[0]["MarginPurchaseBuy"], rows[0]["ShortSaleSell"],
                          rows[0]["ShortSaleBuyback"], rows[0]["MarginShortOffset"]),
                         (40, 8, 3, 2))

    def test_holding_parsers_map_percentage_and_issued_shares(self):
        twse_fields = ["證券代號", "發行股數", "外資及陸資尚可投資股數",
                       "全體外資及陸資持有股數", "外資及陸資尚可投資比率",
                       "全體外資及陸資持股比率", "外資及陸資共用法令投資上限比率"]
        twse = {"stat": "OK", "date": "20260717", "fields": twse_fields,
                "data": [["2330", "25,933,804,458", "1,944,000,000",
                          "18,815,000,000", "7.49", "72.54", "80.00"]]}
        rows, available = fd.parse_twse_holding(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["ForeignInvestmentSharesRatio"],
                          rows[0]["NumberOfSharesIssued"]), (72.54, 25933804458))
        self.assertEqual((rows[0]["ForeignInvestmentShares"],
                          rows[0]["ForeignInvestmentAvailableShares"],
                          rows[0]["ForeignInvestmentAvailableRatio"],
                          rows[0]["ForeignInvestmentLimitRatio"]),
                         (18815000000, 1944000000, 7.49, 80.0))

        tpex_fields = ["代號", "發行股數(A)", "僑外資及陸資尚可投資股數B=A*F-C",
                       "僑外資及陸資持有股數(C)", "僑外資及陸資尚可投資比率(D=B/A)",
                       "僑外資及陸資持股比率(E=C/A)", "法令投資上限比率(F)"]
        tpex = {"stat": "ok", "date": "20260717", "tables": [{
            "fields": tpex_fields,
            "data": [["2454", "1,591,673,608", "348,000,000", "925,000,000",
                      "21.86%", "58.12%", "80.00%"]],
        }]}
        rows, available = fd.parse_tpex_holding(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual((rows[0]["ForeignInvestmentSharesRatio"],
                          rows[0]["NumberOfSharesIssued"]), (58.12, 1591673608))
        self.assertEqual((rows[0]["ForeignInvestmentShares"],
                          rows[0]["ForeignInvestmentAvailableShares"],
                          rows[0]["ForeignInvestmentAvailableRatio"],
                          rows[0]["ForeignInvestmentLimitRatio"]),
                         (925000000, 348000000, 21.86, 80.0))

    def test_sbl_parsers_use_borrowed_short_sale_current_balance(self):
        fields = ["代號", "名稱", "前日餘額", "賣出", "買進", "現券", "今日餘額",
                  "次一營業日限額", "前日餘額", "當日賣出", "當日還券", "當日調整",
                  "當日餘額", "次一營業日可限額", "備註"]
        raw = ["2330", "台積電", "0", "0", "0", "0", "0", "0", "8,700,000",
               "100,000", "30,000", "-4,568", "8,765,432", "12,000,000", ""]
        twse = {"stat": "OK", "date": "20260717", "fields": fields, "data": [raw]}
        rows, available = fd.parse_twse_sbl(twse, "2026-07-17", {"2330"})
        self.assertTrue(available)
        self.assertEqual(rows[0]["SBLShortSalesCurrentDayBalance"], 8765432)
        self.assertEqual((rows[0]["SBLShortSalesPreviousDayBalance"],
                          rows[0]["SBLShortSalesCurrentDaySell"],
                          rows[0]["SBLShortSalesCurrentDayReturn"],
                          rows[0]["SBLShortSalesCurrentDayAdjustment"],
                          rows[0]["SBLShortSalesNextDayLimit"]),
                         (8700000, 100000, 30000, -4568, 12000000))

        tpex_fields = ["股票代號", "股票名稱", "前日餘額", "賣出", "買進", "現券",
                       "當日餘額", "限額", "前日餘額", "當日賣出", "當日還券",
                       "當日調整數額", "當日餘額", "次一營業日可借券賣出限額", "備註"]
        tpex_raw = ["2454", "聯發科", "0", "0", "0", "0", "0", "0", "120,000",
                    "10,000", "5,000", "-1,544", "123,456", "500,000", ""]
        tpex = {"stat": "ok", "date": "20260717",
                "tables": [{"fields": tpex_fields, "data": [tpex_raw]}]}
        rows, available = fd.parse_tpex_sbl(tpex, "2026-07-17", {"2454"})
        self.assertTrue(available)
        self.assertEqual(rows[0]["SBLShortSalesCurrentDayBalance"], 123456)

    def test_upserts_persist_all_expanded_raw_columns(self):
        con = sqlite3.connect(":memory:")
        con.executescript(fd.SCHEMA)
        day, sid = "2026-07-17", "2330"
        fd.up_price(con, [{
            "date": day, "stock_id": sid, "open": 1, "max": 2, "min": 1,
            "close": 2, "Trading_Volume": 100, "Trading_money": 200,
            "Trading_turnover": 9,
        }])
        fd.up_inst(con, [
            {"date": day, "stock_id": sid, "name": "Foreign_Investor",
             "buy": 100, "sell": 20, "net": 80},
            {"date": day, "stock_id": sid, "name": "Investment_Trust",
             "buy": 30, "sell": 10, "net": 20},
            {"date": day, "stock_id": sid, "name": "Dealer_self",
             "buy": 8, "sell": 3, "net": 5},
            {"date": day, "stock_id": sid, "name": "Dealer_Hedging",
             "buy": 7, "sell": 9, "net": -2},
            {"date": day, "stock_id": sid, "name": "Dealer_Total",
             "buy": 15, "sell": 12, "net": 3},
        ])
        fd.up_margin(con, [{
            "date": day, "stock_id": sid, "MarginPurchaseTodayBalance": 1000,
            "MarginPurchasePreviousDayBalance": 992,
            "ShortSaleTodayBalance": 50, "ShortSalePreviousDayBalance": 46,
            "MarginPurchaseBuy": 30,
            "MarginPurchaseSell": 20, "MarginPurchaseCashRepayment": 2,
            "MarginPurchaseLimit": 5000, "ShortSaleSell": 8,
            "ShortSaleBuyback": 3, "ShortSaleStockRepayment": 1,
            "ShortSaleLimit": 1000, "MarginShortOffset": 4,
        }])
        fd.up_holding(con, [{
            "date": day, "stock_id": sid, "ForeignInvestmentSharesRatio": 72.5,
            "NumberOfSharesIssued": 10000, "ForeignInvestmentShares": 7250,
            "ForeignInvestmentAvailableShares": 750,
            "ForeignInvestmentAvailableRatio": 7.5, "ForeignInvestmentLimitRatio": 80,
        }])
        fd.up_sbl(con, [{
            "date": day, "stock_id": sid, "SBLShortSalesCurrentDayBalance": 120,
            "SBLShortSalesPreviousDayBalance": 100, "SBLShortSalesCurrentDaySell": 30,
            "SBLShortSalesCurrentDayReturn": 8, "SBLShortSalesCurrentDayAdjustment": -2,
            "SBLShortSalesNextDayLimit": 500,
        }])

        self.assertEqual(con.execute(
            "SELECT trades FROM price WHERE date=? AND stock_id=?", (day, sid)).fetchone(), (9,))
        self.assertEqual(con.execute(
            "SELECT foreign_buy,foreign_sell,foreign_net,trust_buy,trust_sell,trust_net,"
            "dealer_self_buy,dealer_self_sell,dealer_self_net,dealer_hedge_buy,"
            "dealer_hedge_sell,dealer_hedge_net,dealer_net FROM inst"
        ).fetchone(), (100, 20, 80, 30, 10, 20, 8, 3, 5, 7, 9, -2, 3))
        self.assertEqual(con.execute(
            "SELECT margin_buy,margin_sell,margin_cash_repay,margin_limit,short_sell,"
            "short_buyback,short_stock_repay,short_limit,offset_volume,margin_prev_bal,"
            "short_prev_bal FROM margin"
        ).fetchone(), (30, 20, 2, 5000, 8, 3, 1, 1000, 4, 992, 46))
        self.assertEqual(con.execute(
            "SELECT foreign_shares,foreign_available_shares,foreign_available_pct,"
            "foreign_limit_pct FROM holding"
        ).fetchone(), (7250, 750, 7.5, 80.0))
        self.assertEqual(con.execute(
            "SELECT sbl_prev_bal,sbl_sell,sbl_return,sbl_adjustment,sbl_next_limit FROM sbl"
        ).fetchone(), (100, 30, 8, -2, 500))
        con.close()

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
                self.con.execute(
                    "INSERT INTO price(date,stock_id,open,high,low,close,volume,amount) "
                    "VALUES(?,?,?,?,?,?,?,?)",
                                 (day, sid, 1, 2, 1, 2, 100, 200))
                self.con.execute(
                    "INSERT INTO inst(date,stock_id,foreign_net,trust_net,dealer_net) "
                    "VALUES(?,?,?,?,?)", (day, sid, 1, 2, 3))
                self.con.execute(
                    "INSERT INTO margin(date,stock_id,margin_bal,short_bal) VALUES(?,?,?,?)",
                    (day, sid, 10, 1))
                self.con.execute(
                    "INSERT INTO holding(date,stock_id,foreign_pct,shares_issued) VALUES(?,?,?,?)",
                    (day, sid, 20, 1000))
                self.con.execute(
                    "INSERT INTO sbl(date,stock_id,sbl_bal) VALUES(?,?,?)", (day, sid, 10))
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

    def expanded_price_fetch(self, source, day, wanted_ids):
        self.price_calls.append((source, day, set(wanted_ids)))
        sid = "2330" if source == "TWSE" else "2454"
        rows = [{
            "date": day, "stock_id": sid, "open": 2, "max": 3,
            "min": 2, "close": 3, "Trading_Volume": 100,
            "Trading_money": 300, "Trading_turnover": 9,
        }] if sid in wanted_ids else []
        return rows, True

    def expanded_raw_fetch(self, dataset, source, day, wanted_ids):
        self.calls.append((dataset, source, day, set(wanted_ids)))
        sid = "2330" if source == "TWSE" else "2454"
        if sid not in wanted_ids:
            return [], True
        if dataset == "TaiwanStockInstitutionalInvestorsBuySell":
            return [{"date": day, "stock_id": sid, "name": "Foreign_Investor",
                     "buy": 10, "sell": 2, "net": 8}], True
        if dataset == "TaiwanStockMarginPurchaseShortSale":
            return [{
                "date": day, "stock_id": sid,
                "MarginPurchasePreviousDayBalance": 10,
                "MarginPurchaseTodayBalance": 10,
                "ShortSalePreviousDayBalance": 0,
                "ShortSaleTodayBalance": 1,
                "MarginPurchaseBuy": 3, "MarginPurchaseSell": 2,
                "MarginPurchaseCashRepayment": 1, "MarginPurchaseLimit": 100,
                "ShortSaleSell": 2, "ShortSaleBuyback": 1,
                "ShortSaleStockRepayment": 0, "ShortSaleLimit": 50,
                "MarginShortOffset": 0,
            }], True
        if dataset == "TaiwanStockShareholding":
            return [{
                "date": day, "stock_id": sid,
                "ForeignInvestmentSharesRatio": 20,
                "NumberOfSharesIssued": 1000,
                "ForeignInvestmentShares": 200,
                "ForeignInvestmentAvailableShares": 600,
                "ForeignInvestmentAvailableRatio": 60,
                "ForeignInvestmentLimitRatio": 80,
            }], True
        if dataset == "TaiwanDailyShortSaleBalances":
            return [{
                "date": day, "stock_id": sid,
                "SBLShortSalesCurrentDayBalance": 10,
                "SBLShortSalesPreviousDayBalance": 8,
                "SBLShortSalesCurrentDaySell": 3,
                "SBLShortSalesCurrentDayReturn": 1,
                "SBLShortSalesCurrentDayAdjustment": 0,
                "SBLShortSalesNextDayLimit": 50,
            }], True
        raise AssertionError(dataset)

    def test_expanded_field_backfill_uses_known_dates_and_becomes_zero_request(self):
        stats = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", None,
            sleep=0, fetcher=self.expanded_raw_fetch,
            price_fetcher=self.expanded_price_fetch,
            backfill_expanded_fields=True)

        # 只掃 DB 已知的 07-08/07-09，不探測尚未知的 07-10：5 表 × 2 日 × 2 市場。
        self.assertEqual(stats["requests"], 20)
        self.assertEqual(stats["probe_requests"], 0)
        self.assertEqual({call[1] for call in self.price_calls},
                         {"2026-07-08", "2026-07-09"})
        for table, columns in fd.RAW_EXPANDED_COLUMNS.items():
            null_sql = " OR ".join(f'"{column}" IS NULL' for column in columns)
            self.assertEqual(self.con.execute(
                f"SELECT COUNT(*) FROM {table} WHERE {null_sql}").fetchone()[0], 0, table)

        self.calls.clear()
        self.price_calls.clear()
        repeat = fd.fetch_missing_raw(
            self.con, self.ids, fd.DATASETS, "2026-07-08", "2026-07-10", None,
            sleep=0, fetcher=self.expanded_raw_fetch,
            price_fetcher=self.expanded_price_fetch,
            backfill_expanded_fields=True)
        self.assertEqual(repeat["requests"], 0)
        self.assertEqual(self.calls, [])
        self.assertEqual(self.price_calls, [])

    def test_expanded_field_backfill_resumes_after_source_checkpoint(self):
        def fail_tpex(dataset, source, day, wanted_ids):
            if source == "TPEx":
                raise OSError("temporary TPEx failure")
            return self.expanded_raw_fetch(dataset, source, day, wanted_ids)

        with self.assertRaises(fd.ExchangeRawFetchError):
            fd.fetch_missing_raw(
                self.con, self.ids, ["TaiwanStockMarginPurchaseShortSale"],
                "2026-07-08", "2026-07-08", None, sleep=0,
                fetcher=fail_tpex, backfill_expanded_fields=True)

        self.assertIsNotNone(self.con.execute(
            "SELECT margin_buy FROM margin WHERE date='2026-07-08' AND stock_id='2330'"
        ).fetchone()[0])
        self.assertIsNone(self.con.execute(
            "SELECT margin_buy FROM margin WHERE date='2026-07-08' AND stock_id='2454'"
        ).fetchone()[0])

        self.calls.clear()
        resumed = fd.fetch_missing_raw(
            self.con, self.ids, ["TaiwanStockMarginPurchaseShortSale"],
            "2026-07-08", "2026-07-08", None, sleep=0,
            fetcher=self.expanded_raw_fetch, backfill_expanded_fields=True)
        self.assertEqual(resumed["requests"], 2)
        self.assertTrue(all(call[3] == {"2454"} for call in self.calls))
        self.assertEqual(self.con.execute(
            "SELECT COUNT(*) FROM margin WHERE date='2026-07-08' AND margin_buy IS NULL"
        ).fetchone()[0], 0)

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
        publish_block = workflow[workflow.index("- name: commit 回 repo(有變動才提交)"):]
        self.assertIn("id: fetch_daily", fetch_block)
        self.assertIn("continue-on-error: true", fetch_block)
        self.assertIn("steps.fetch_daily.outcome == 'failure'", checkpoint_block)
        self.assertIn("git add data/", checkpoint_block)
        self.assertIn("每日抓取進度（未完成）", checkpoint_block)
        self.assertNotIn("index.html", checkpoint_block)
        self.assertIn("steps.fetch_daily.outcome == 'failure'", stop_block)
        self.assertIn("exit 1", stop_block)
        self.assertIn('cron: "7 10 * * 1-5"', workflow)
        self.assertIn('cron: "7 11 * * 1-5"', workflow)
        self.assertIn('cron: "47 13 * * 1-5"', workflow)
        self.assertIn('cron: "47 15 * * 1-5"', workflow)
        self.assertIn('[ "$SCHEDULE" = "7 10 * * 1-5" ]', workflow)
        self.assertIn('[ "$SCHEDULE" = "7 11 * * 1-5" ]', workflow)
        self.assertIn('[ "$SCHEDULE" = "47 13 * * 1-5" ]', workflow)
        self.assertIn('$(date -u +%H%M)', workflow)
        self.assertIn('target_date=$(date -u +%F)', workflow)
        self.assertIn('TARGET_DATE: ${{ steps.mode.outputs.target_date }}', workflow)
        self.assertIn("--raw-only", fetch_block)
        self.assertIn("--final-pass", fetch_block)
        self.assertIn('--final-pass --end "$TARGET_DATE"', fetch_block)
        self.assertIn("steps.mode.outputs.mode == 'complete'", workflow[score_at:])
        self.assertIn("git merge-base --is-ancestor", publish_block)
        self.assertIn("id: commit_push", workflow)
        self.assertIn("pages: read", workflow)
        self.assertIn("steps.commit_push.outputs.commit_sha", workflow)
        self.assertIn("pages/builds/latest", workflow)
        self.assertIn('page_commit" = "$COMMIT_SHA', workflow)
        conflict_at = publish_block.index("::error::rebase 衝突")
        self.assertIn("exit 1", publish_block[conflict_at:])

    def test_all_main_writers_serialize_and_checkout_fresh_main(self):
        workflows = ROOT / ".github" / "workflows"
        for name in ("daily-fetch.yml", "fetch-financials.yml", "weekly-validate.yml"):
            text = (workflows / name).read_text(encoding="utf-8")
            with self.subTest(workflow=name):
                self.assertIn("group: repo-main-writer", text)
                self.assertIn("queue: max", text)
                self.assertIn("uses: actions/checkout@v6", text)
                self.assertIn("ref: main", text)
                self.assertIn("fetch-depth: 0", text)
                self.assertIn("uses: actions/setup-python@v6", text)

        financial = (workflows / "fetch-financials.yml").read_text(encoding="utf-8")
        conflict_at = financial.index("::error::rebase 衝突")
        self.assertIn("exit 1", financial[conflict_at:])

        quality = (workflows / "qualitative-quality.yml").read_text(encoding="utf-8")
        self.assertIn("uses: actions/checkout@v6", quality)
        self.assertIn("uses: actions/setup-python@v6", quality)


class FinalPassReadinessTest(unittest.TestCase):
    def test_today_requires_taipei_2340_cutoff(self):
        before = datetime(2026, 7, 22, 15, 39, tzinfo=timezone.utc)
        ready = datetime(2026, 7, 22, 15, 40, tzinfo=timezone.utc)
        self.assertFalse(fd.final_pass_ready("2026-07-22", before))
        self.assertTrue(fd.final_pass_ready("2026-07-22", ready))

    def test_historical_backfill_is_allowed_but_future_date_is_not(self):
        now = datetime(2026, 7, 22, 15, 40, tzinfo=timezone.utc)
        self.assertTrue(fd.final_pass_ready("2026-07-21", now))
        self.assertFalse(fd.final_pass_ready("2026-07-23", now))

    def test_cli_rejects_same_day_final_pass_before_cutoff(self):
        before = datetime(2026, 7, 22, 15, 39, tzinfo=timezone.utc)
        argv = ["fetch_daily.py", "--final-pass", "--end", "2026-07-22"]
        with mock.patch.object(sys, "argv", argv), \
                mock.patch.object(fd, "taipei_now", return_value=before):
            with self.assertRaises(SystemExit) as raised:
                fd.main()
        self.assertIn("拒絕過早 final-pass", str(raised.exception))


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

    def test_expanded_field_backfill_is_automatically_raw_only(self):
        stats = {
            "rows": 0, "finmind_requests": 0, "exchange_requests": 0,
            "probe_requests": 0, "skipped_batches": 5, "expected_dates": set(),
        }
        with tempfile.TemporaryDirectory() as tmp:
            db = str(Path(tmp) / "expanded-backfill.db")
            argv = [
                "fetch_daily.py", "--backfill-expanded-fields",
                "--start", "2026-03-02", "--end", "2026-07-17",
            ]
            with mock.patch.object(fd, "DB", db), \
                    mock.patch.object(sys, "argv", argv), \
                    mock.patch.object(fd, "load_universe", return_value=[]), \
                    mock.patch.object(fd, "fetch_missing_raw", return_value=stats) as fetch_raw, \
                    mock.patch.object(fd, "get_token") as get_token, \
                    mock.patch.object(fd, "build_metrics") as build_metrics:
                fd.main()

            get_token.assert_not_called()
            build_metrics.assert_not_called()
            self.assertTrue(fetch_raw.call_args.kwargs["backfill_expanded_fields"])

    def test_expanded_field_backfill_requires_explicit_start(self):
        with mock.patch.object(sys, "argv", ["fetch_daily.py", "--backfill-expanded-fields"]):
            with self.assertRaises(SystemExit) as raised:
                fd.main()
        self.assertEqual(raised.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
