import copy
import json
import sqlite3
import sys
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_daily as fd
import suspension_events as se
import trading_status as ts


def tpex_payload(sid="6173", start="1151007", resume="1151019"):
    # 2026-10-08 官方 bulletin/decap 格式；保留停復牌相關欄位。
    return {"stat": "ok", "date": "20261008", "tables": [{
        "fields": ["代號", "名稱", "停止買賣日期", "減資原因", "恢復買賣日期"],
        "totalCount": 1, "data": [[sid, "信昌電", start, "現金減資", resume]],
    }]}


def add_evidence(con, sid="6173", day="2026-10-07", start="1151007", resume="1151019"):
    return se.record_evidence(con, day, {sid}, "TPEx",
                              json.dumps(tpex_payload(sid, start, resume), ensure_ascii=False),
                              "2026-10-08T16:00:00+08:00")


class SuspensionEvidenceTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.executescript(fd.SCHEMA)

    def tearDown(self):
        self.con.close()

    def test_twse_and_tpex_dates_use_resume_exclusive_interval(self):
        tpex = se.parse_notices("TPEx", tpex_payload())
        twse = {"stat": "OK", "fields": ["停止買賣日期", "股票代號", "恢復買賣日期", "減資原因"],
                "data": [["115/10/07", "6173", "115/10/19", "現金減資"]]}
        self.assertEqual(se.parse_notices("TWSE", twse), tpex)
        for day, expected in [("2026-10-06", []), ("2026-10-07", ["6173"]),
                              ("2026-10-16", ["6173"]), ("2026-10-19", [])]:
            payload = tpex_payload()
            payload["date"] = "20261020"
            result = se.record_evidence(self.con, day, {"6173"}, "TPEx", json.dumps(payload),
                                        "2026-10-20T12:00:00+08:00")
            self.assertEqual(result, expected)

    def test_absence_is_exempt_only_for_price_and_inst_without_synthetic_rows(self):
        add_evidence(self.con)
        for table in ("price", "inst"):
            self.assertEqual(ts.expected_ids(self.con, table, {"6173", "2330"}, "2026-10-07"), {"2330"})
        for table in ("margin", "holding", "sbl"):
            self.assertEqual(ts.expected_ids(self.con, table, {"6173"}, "2026-10-07"), {"6173"})
        self.assertEqual(self.con.execute("SELECT COUNT(*) FROM price").fetchone()[0], 0)
        self.assertEqual(ts.verified_exclusion_ids(self.con, "2026-10-07"), {"6173"})

    def test_old_receipt_cannot_authorize_next_day_or_resume_day(self):
        add_evidence(self.con)
        for day in ("2026-10-08", "2026-10-19"):
            self.assertEqual(ts.expected_ids(self.con, "price", {"6173"}, day), {"6173"})

    def test_unknown_stock_still_missing(self):
        add_evidence(self.con)
        self.assertEqual(ts.expected_ids(self.con, "price", {"9999"}, "2026-10-07"), {"9999"})

    def test_tampered_payload_cannot_grant_exemption(self):
        add_evidence(self.con)
        self.con.execute("UPDATE suspension_evidence SET payload_json='{}'")
        with self.assertRaisesRegex(ValueError, "SHA"):
            ts.expected_ids(self.con, "price", {"6173"}, "2026-10-07")

    def test_status_flag_alone_does_not_grant_exemption(self):
        self.con.execute("INSERT INTO trading_status VALUES(?,?,?,?,?)",
                         ("2026-10-07", "6173", "no_trade", se.SOURCE, "人工標記"))
        self.assertEqual(ts.verified_exclusion_ids(self.con, "2026-10-07"), set())

    def test_receipt_moved_outside_interval_fails(self):
        add_evidence(self.con)
        self.con.execute("UPDATE suspension_evidence SET date='2026-10-19'")
        with self.assertRaisesRegex(ValueError, "日期"):
            se.verified(self.con, "2026-10-19")

    def test_wrong_source_or_stale_payload_fails(self):
        payload = tpex_payload()
        payload["date"] = "20261006"
        with self.assertRaisesRegex(ValueError, "落後"):
            se.record_evidence(self.con, "2026-10-07", {"6173"}, "TPEx", json.dumps(payload),
                               "2026-10-08T12:00:00+08:00")
        add_evidence(self.con)
        self.con.execute("UPDATE suspension_evidence SET source_url='https://example.com'")
        with self.assertRaisesRegex(ValueError, "來源"):
            se.verified(self.con, "2026-10-07")

    def test_future_day_cannot_be_pre_authorized(self):
        with self.assertRaisesRegex(ValueError, "未來"):
            se.record_evidence(self.con, "2026-10-09", {"6173"}, "TPEx", json.dumps(tpex_payload()),
                               "2026-10-08T12:00:00+08:00")

    def test_real_trading_conflict_is_not_hidden(self):
        add_evidence(self.con)
        self.con.execute("INSERT INTO price VALUES('2026-10-07','6173',1,1,1,1,10,10,1)")
        with self.assertRaisesRegex(ValueError, "價格衝突"):
            ts.verified_exclusions(self.con, "2026-10-07")

    def test_wrong_exchange_and_future_response_date_are_rejected(self):
        self.con.execute("INSERT INTO security_market VALUES('6173','TWSE','2026-10-06')")
        with self.assertRaisesRegex(ValueError, "市場衝突"):
            add_evidence(self.con)
        payload = tpex_payload();payload["date"] = "20261009"
        with self.assertRaises(ValueError):
            se.record_evidence(self.con, "2026-10-07", {"6173"}, "TPEx", json.dumps(payload),
                               "2026-10-08T12:00:00+08:00")

    def test_malformed_and_open_ended_notices_fail_closed(self):
        samples = []
        for start, resume in [("", "1151019"), ("1151007", ""), ("1151019", "1151007"),
                              ("1150230", "1151019")]:
            samples.append(tpex_payload(start=start, resume=resume))
        bad = tpex_payload(); bad["stat"] = "error"; samples.append(bad)
        bad = tpex_payload(); bad["tables"][0]["totalCount"] = 2; samples.append(bad)
        bad = tpex_payload(); bad["tables"][0]["fields"][2] = "新欄名"; samples.append(bad)
        for payload in samples:
            with self.subTest(payload=payload), self.assertRaises(ValueError):
                se.parse_notices("TPEx", payload)

    def test_conflicting_notices_fail(self):
        payload = tpex_payload()
        row = copy.deepcopy(payload["tables"][0]["data"][0]); row[-1] = "1151020"
        payload["tables"][0]["data"].append(row); payload["tables"][0]["totalCount"] = 2
        with self.assertRaisesRegex(ValueError, "衝突"):
            se.parse_notices("TPEx", payload)

    def test_outage_does_not_exempt_missing_stock(self):
        with mock.patch("builtins.print"):
            result = se.resolve_missing_prices(self.con, "2026-10-07", {"6173"},
                                               fetcher=mock.Mock(side_effect=OSError("offline")))
        self.assertEqual(len(result["errors"]), 2)
        self.assertEqual(ts.expected_ids(self.con, "price", {"6173"}, "2026-10-07"), {"6173"})

    def test_pipeline_resumes_and_repeated_run_uses_no_network(self):
        ids = ["2330", "6173"]
        def price(source, day, wanted):
            rows = ([{"date": day, "stock_id": "2330", "open": 10, "max": 10,
                      "min": 10, "close": 10, "Trading_Volume": 1, "Trading_money": 10,
                      "Trading_turnover": 1}] if source == "TWSE" else [])
            return rows, True
        def resolve(con, day, wanted):
            add_evidence(con)
            return {"requests": 2}
        resolver = mock.Mock(side_effect=resolve)
        first = fd.fetch_missing_raw(self.con, ids, ["TaiwanStockPrice"], "2026-10-07",
                                     "2026-10-07", None, price_fetcher=price,
                                     suspension_resolver=resolver)
        self.assertEqual(first["suspension_requests"], 2)
        self.assertEqual(first["expected_dates"], {"2026-10-07"})
        second = fd.fetch_missing_raw(self.con, ids, ["TaiwanStockPrice"], "2026-10-07",
                                      "2026-10-07", None,
                                      price_fetcher=mock.Mock(side_effect=AssertionError("network")),
                                      suspension_resolver=resolver)
        self.assertEqual(second["requests"], 0)
        self.assertEqual(second["suspension_requests"], 0)
        self.assertEqual(resolver.call_count, 1)


if __name__ == "__main__":
    unittest.main()
