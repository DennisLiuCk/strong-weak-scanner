import sqlite3
import sys
import unittest
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import observation_metrics as om
import fetch_daily as fd


def trading_dates(n):
    start = date(2026, 1, 5)
    return [(start + timedelta(days=i)).isoformat() for i in range(n)]


class ObservationMetricsTest(unittest.TestCase):
    def setUp(self):
        self.con = sqlite3.connect(":memory:")
        self.con.row_factory = sqlite3.Row
        self.con.executescript("""
            CREATE TABLE universe(stock_id TEXT PRIMARY KEY,name TEXT,grp TEXT,biz TEXT);
            CREATE TABLE price(date TEXT,stock_id TEXT,open REAL,high REAL,low REAL,close REAL,
                volume INTEGER,amount REAL,trades INTEGER,PRIMARY KEY(date,stock_id));
            CREATE TABLE price_adj(date TEXT,stock_id TEXT,close REAL,PRIMARY KEY(date,stock_id));
            CREATE TABLE inst(date TEXT,stock_id TEXT,foreign_net INTEGER,trust_net INTEGER,dealer_net INTEGER,
                foreign_buy INTEGER,foreign_sell INTEGER,trust_buy INTEGER,trust_sell INTEGER,
                dealer_self_buy INTEGER,dealer_self_sell INTEGER,dealer_self_net INTEGER,
                dealer_hedge_buy INTEGER,dealer_hedge_sell INTEGER,dealer_hedge_net INTEGER,
                PRIMARY KEY(date,stock_id));
            CREATE TABLE margin(date TEXT,stock_id TEXT,margin_bal INTEGER,short_bal INTEGER,
                margin_buy INTEGER,margin_sell INTEGER,margin_cash_repay INTEGER,margin_limit INTEGER,
                short_sell INTEGER,short_buyback INTEGER,short_stock_repay INTEGER,short_limit INTEGER,
                offset_volume INTEGER,margin_prev_bal INTEGER,short_prev_bal INTEGER,
                PRIMARY KEY(date,stock_id));
            CREATE TABLE holding(date TEXT,stock_id TEXT,foreign_pct REAL,shares_issued INTEGER,
                foreign_shares INTEGER,foreign_available_shares INTEGER,foreign_available_pct REAL,
                foreign_limit_pct REAL,PRIMARY KEY(date,stock_id));
            CREATE TABLE sbl(date TEXT,stock_id TEXT,sbl_bal INTEGER,sbl_prev_bal INTEGER,
                sbl_sell INTEGER,sbl_return INTEGER,sbl_adjustment INTEGER,sbl_next_limit INTEGER,
                PRIMARY KEY(date,stock_id));
            CREATE TABLE market_index(date TEXT,market TEXT,index_key TEXT,index_name TEXT,index_type TEXT,
                close REAL,PRIMARY KEY(date,market,index_key));
            CREATE TABLE security_market(stock_id TEXT PRIMARY KEY,market TEXT,observed_date TEXT);
        """)

    def tearDown(self):
        self.con.close()

    def seed(self, market="TWSE", stocks=6, index_days=21):
        dates = trading_dates(21)
        benchmark = "TWSE報酬" if market == "TWSE" else "櫃買報酬"
        index_dates = dates[-index_days:]
        for day in index_dates:
            k = dates.index(day)
            self.con.execute(
                "INSERT INTO market_index VALUES(?,?,?,?,?,?)",
                (day, market, benchmark, benchmark, "total_return", 100 * (1.01 ** k)),
            )
        for number in range(stocks):
            sid = str(1001 + number)
            self.con.execute("INSERT INTO universe VALUES(?,?,?,?)", (sid, sid, "g", "biz"))
            self.con.execute("INSERT INTO security_market VALUES(?,?,?)", (sid, market, dates[-1]))
            sbl_previous = 1_000_000
            for k, day in enumerate(dates):
                close = 50 * (1.02 ** k)
                self.con.execute(
                    "INSERT INTO price VALUES(?,?,?,?,?,?,?,?,?)",
                    (day, sid, close, close, close, close, 1_000_000, 100_000_000, 1_000),
                )
                self.con.execute("INSERT INTO price_adj VALUES(?,?,?)", (day, sid, close))
                self.con.execute(
                    "INSERT INTO inst VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (day, sid, 200_000, -200_000, -20_000,
                     600_000, 400_000, 100_000, 300_000,
                     80_000, 20_000, 60_000, 10_000, 90_000, -80_000),
                )
                self.con.execute(
                    "INSERT INTO margin VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                    (day, sid, 1_000 + 10 * k, 100 + 4 * k,
                     20, 5, 5, 2_000, 8, 3, 1, 500, 2,
                     1_000 + 10 * k - 10, 100 + 4 * k - 4),
                )
                foreign_shares = 20_000_000 + 100_000 * k
                available = 50_000_000 - foreign_shares
                self.con.execute(
                    "INSERT INTO holding VALUES(?,?,?,?,?,?,?,?)",
                    (day, sid, foreign_shares / 1_000_000, 100_000_000, foreign_shares,
                     available, available / 1_000_000, 50.0),
                )
                sbl_current = sbl_previous + 100_000 - 40_000 - 10_000
                self.con.execute(
                    "INSERT INTO sbl VALUES(?,?,?,?,?,?,?,?)",
                    (day, sid, sbl_current, sbl_previous, 100_000, 40_000, -10_000, 200_000),
                )
                sbl_previous = sbl_current
        self.con.commit()
        return dates, benchmark

    def test_all_eight_observation_dimensions_reconcile(self):
        dates, benchmark = self.seed()
        counts = om.build_observation_metrics(
            self.con, twse_key=benchmark, tpex_key="櫃買報酬", min_group_n=6)
        self.assertEqual(counts, {"stock_rows": 126, "group_rows": 21})

        row = self.con.execute(
            "SELECT * FROM observation_metrics WHERE date=? AND stock_id='1001'", (dates[-1],)
        ).fetchone()
        self.assertEqual(row["market"], "TWSE")
        self.assertEqual(row["benchmark_name"], benchmark)
        self.assertAlmostEqual(row["avg_shares_per_trade"], 1_000)
        self.assertAlmostEqual(row["avg_value_per_trade"], 100_000)
        self.assertAlmostEqual(row["foreign_imbalance_pct"], 20.0)
        self.assertAlmostEqual(row["trust_imbalance_pct"], -50.0)
        self.assertAlmostEqual(row["dealer_self_imbalance_pct"], 60.0)
        self.assertAlmostEqual(row["dealer_hedge_imbalance_pct"], -80.0)
        self.assertEqual(row["inst_gross"], 1_600_000)
        self.assertAlmostEqual(row["inst_participation_pct"], 80.0)

        self.assertEqual(row["margin_net_flow"], 10)
        self.assertEqual(row["margin_balance_change"], 10)
        self.assertEqual(row["margin_flow_residual"], 0)
        self.assertEqual(row["short_net_flow"], 4)
        self.assertEqual(row["short_balance_change"], 4)
        self.assertEqual(row["short_flow_residual"], 0)
        self.assertAlmostEqual(row["margin_limit_util_pct"], 60.0)
        self.assertAlmostEqual(row["short_limit_util_pct"], 36.0)
        self.assertEqual(row["foreign_shares_change"], 100_000)
        self.assertAlmostEqual(row["foreign_limit_used_pct"], 44.0)

        self.assertEqual(row["sbl_net_flow"], 50_000)
        self.assertEqual(row["sbl_balance_change"], 50_000)
        self.assertEqual(row["sbl_flow_residual"], 0)
        self.assertAlmostEqual(row["sbl_sell_limit_pct"], 50.0)

        expected_stock5 = 1.02 ** 5 - 1
        expected_index5 = 1.01 ** 5 - 1
        self.assertAlmostEqual(row["stock_ret5"], expected_stock5)
        self.assertAlmostEqual(row["index_ret5"], expected_index5)
        self.assertAlmostEqual(row["excess_ret5"], expected_stock5 - expected_index5)

        group = self.con.execute(
            "SELECT * FROM group_observation_metrics WHERE date=? AND grp='g'", (dates[-1],)
        ).fetchone()
        self.assertEqual(group["n"], 6)
        self.assertEqual(group["n_excess20"], 6)
        self.assertAlmostEqual(group["foreign_buy_breadth"], 1.0)
        self.assertAlmostEqual(group["trust_buy_breadth"], 0.0)
        self.assertAlmostEqual(group["med_inst_participation_pct"], 80.0)
        self.assertAlmostEqual(group["med_excess_ret5"], expected_stock5 - expected_index5)
        self.assertAlmostEqual(group["excess_breadth5"], 1.0)

    def test_short_tpex_history_leaves_20_day_excess_missing_not_zero(self):
        dates, benchmark = self.seed(market="TPEx", stocks=1, index_days=12)
        om.build_observation_metrics(
            self.con, twse_key="TWSE報酬", tpex_key=benchmark, min_group_n=1)
        row = self.con.execute(
            "SELECT * FROM observation_metrics WHERE date=? AND stock_id='1001'", (dates[-1],)
        ).fetchone()
        self.assertIsNotNone(row["excess_ret1"])
        self.assertIsNotNone(row["excess_ret5"])
        self.assertIsNone(row["index_ret20"])
        self.assertIsNone(row["excess_ret20"])


class SecurityMarketCheckpointTest(unittest.TestCase):
    def test_price_source_persists_stock_market_for_benchmark_matching(self):
        con = sqlite3.connect(":memory:")
        fd.ensure_schema(con)

        def fetcher(source, day, wanted):
            sid = "1001" if source == "TWSE" else "1002"
            return ([fd._price_row(day, sid, 10, 11, 9, 10, 1000, 10_000, 20)], True, [])

        fd.fetch_exchange_prices(con, ["1001", "1002"], {"2026-07-17"}, fetcher=fetcher)
        markets = dict(con.execute("SELECT stock_id,market FROM security_market"))
        con.close()
        self.assertEqual(markets, {"1001": "TWSE", "1002": "TPEx"})


if __name__ == "__main__":
    unittest.main()
