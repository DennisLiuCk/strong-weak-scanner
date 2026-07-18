import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_raw_data as audit
import fetch_daily as fd


class RawDataAuditTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.executescript(fd.SCHEMA)
        self.ids = ["2330", "2454"]
        self.days = ["2026-07-08", "2026-07-10"]
        for day in self.days:
            self.con.execute("INSERT INTO market VALUES(?,?)", (day, 100.0))
            for sid in self.ids:
                self._insert_complete_pair(day, sid)
            fd.up_market_index(self.con, [{
                "date": day, "market": "TWSE", "index_key": fd.TWSE_TOTAL_RETURN_KEY,
                "index_name": fd.TWSE_TOTAL_RETURN_KEY, "index_type": "total_return",
                "close": 100.0,
            }, {
                "date": day, "market": "TPEx", "index_key": fd.TPEX_TOTAL_RETURN_KEY,
                "index_name": fd.TPEX_TOTAL_RETURN_KEY, "index_type": "total_return",
                "close": 100.0,
            }])
        self.con.commit()

    def tearDown(self):
        self.con.close()

    def _insert_complete_pair(self, day, sid):
        fd.up_price(self.con, [{
            "date": day, "stock_id": sid, "open": 10, "max": 12, "min": 9,
            "close": 11, "Trading_Volume": 1000, "Trading_money": 11000,
            "Trading_turnover": 20,
        }])
        fd.up_inst(self.con, [
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
        fd.up_margin(self.con, [{
            "date": day, "stock_id": sid, "MarginPurchaseTodayBalance": 1000,
            "ShortSaleTodayBalance": 50, "MarginPurchaseBuy": 30,
            "MarginPurchaseSell": 20, "MarginPurchaseCashRepayment": 2,
            "MarginPurchaseLimit": 5000, "ShortSaleSell": 8,
            "ShortSaleBuyback": 3, "ShortSaleStockRepayment": 1,
            "ShortSaleLimit": 1000, "MarginShortOffset": 4,
        }])
        fd.up_holding(self.con, [{
            "date": day, "stock_id": sid, "ForeignInvestmentSharesRatio": 72.5,
            "NumberOfSharesIssued": 10000, "ForeignInvestmentShares": 7250,
            "ForeignInvestmentAvailableShares": 750,
            "ForeignInvestmentAvailableRatio": 7.5,
            "ForeignInvestmentLimitRatio": 80,
        }])
        fd.up_sbl(self.con, [{
            "date": day, "stock_id": sid, "SBLShortSalesCurrentDayBalance": 120,
            "SBLShortSalesPreviousDayBalance": 100,
            "SBLShortSalesCurrentDaySell": 30,
            "SBLShortSalesCurrentDayReturn": 8,
            "SBLShortSalesCurrentDayAdjustment": -2,
            "SBLShortSalesNextDayLimit": 500,
        }])

    def test_complete_grid_and_formulas_pass(self):
        report = audit.audit_connection(self.con, self.ids)

        self.assertTrue(report["ok"])
        self.assertEqual(report["scope"]["expected_rows_per_table"], 4)
        for table in fd.DATASET_TABLE.values():
            self.assertEqual(report["tables"][table]["required_complete_rows"], 4)
            self.assertEqual(report["tables"][table]["expanded_complete_rows"], 4)
        self.assertTrue(all(item["mismatches"] == 0
                            for item in report["invariants"].values()))
        self.assertEqual(report["market_index"]["twse"]["complete_dates"], 2)
        self.assertEqual(report["market_index"]["tpex_latest_month"]["complete_dates"], 2)

    def test_null_expanded_field_fails_with_column_evidence(self):
        self.con.execute(
            "UPDATE margin SET margin_buy=NULL WHERE date='2026-07-08' AND stock_id='2454'")
        report = audit.audit_connection(self.con, self.ids)

        self.assertFalse(report["ok"])
        self.assertEqual(report["tables"]["margin"]["expanded_complete_rows"], 3)
        self.assertEqual(report["tables"]["margin"]["null_by_column"], {"margin_buy": 1})
        self.assertTrue(any("margin 必備欄為 NULL" in error for error in report["errors"]))

    def test_formula_mismatch_fails(self):
        self.con.execute(
            "UPDATE inst SET foreign_net=999 WHERE date='2026-07-08' AND stock_id='2330'")
        self.con.execute(
            "UPDATE sbl SET sbl_bal=999 WHERE date='2026-07-10' AND stock_id='2454'")
        report = audit.audit_connection(self.con, self.ids)

        self.assertFalse(report["ok"])
        self.assertEqual(report["invariants"]["inst.foreign_net"]["mismatches"], 1)
        self.assertEqual(report["invariants"]["sbl.balance"]["mismatches"], 1)

    def test_off_spine_rows_warn_but_do_not_fake_completeness(self):
        fd.up_inst(self.con, [{
            "date": "2026-07-09", "stock_id": "2330", "name": "Foreign_Investor",
            "buy": 10, "sell": 2, "net": 8,
        }])
        report = audit.audit_connection(
            self.con, self.ids, start="2026-07-08", end="2026-07-10")

        self.assertTrue(report["ok"])
        self.assertEqual(report["tables"]["inst"]["rows"], 4)
        self.assertEqual(report["tables"]["inst"]["off_spine_rows"], 1)
        self.assertTrue(any("price∪market spine" in warning for warning in report["warnings"]))

    def test_database_opens_in_readonly_mode(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "audit.db"
            writer = sqlite3.connect(path)
            writer.executescript(fd.SCHEMA)
            writer.close()

            reader = audit.open_readonly(path)
            try:
                with self.assertRaises(sqlite3.OperationalError):
                    reader.execute("CREATE TABLE forbidden(value INTEGER)")
            finally:
                reader.close()


if __name__ == "__main__":
    unittest.main()
