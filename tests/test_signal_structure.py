"""signal_structure 的數學契約:用合成資料釘住定義,避免日後重構把指標算歪。

這些指標會出現在每日簡報與週報 §⑦,是判讀 §4-7 單柱風險的依據——算錯比沒有更糟。
"""
import sqlite3
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import signal_structure as sig


def rows(*specs):
    """specs = [(stock_id, s_price, s_resil, s_vol, s_foreign, s_trust, s_dip, s_margin), ...]"""
    keys = ["s_price", "s_resil", "s_vol", "s_foreign", "s_trust", "s_dip", "s_margin"]
    return [dict(zip(["stock_id"] + keys, s)) for s in specs]


class SignalStructureTest(unittest.TestCase):
    def test_variance_shares_sum_to_one(self):
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        shares = sig.variance_shares([g])
        self.assertAlmostEqual(sum(shares.values()), 1.0, places=9,
                               msg="變異貢獻分解必須完全加總為 1")

    def test_single_weight_gives_one_effective_factor(self):
        """只有一個元素有權重 → 有效因子數 = 1、composite 排名 = 該元素排名。"""
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        only = {k: (1.0 if k == "price" else 0.0) for k in sig.WEIGHTS}
        shares = sig.variance_shares([g], only)
        self.assertAlmostEqual(sig.effective_factors(shares), 1.0, places=6)
        self.assertAlmostEqual(sig.rank_rho([g], "price", only), 1.0, places=6)

    def test_equal_weights_give_more_effective_factors_than_current(self):
        """等權(7 個)的有效因子數應高於現行(集中在 price/resil)。"""
        g = rows(("A", 2, 1, 0, -1, 2, 0, 1), ("B", -2, 0, 1, 2, -1, 1, 0),
                 ("C", 1, -2, -1, 0, 0, -2, 2), ("D", 0, 2, 2, 1, 1, 2, -1),
                 ("E", -1, -1, 0, -2, 2, 1, 0), ("F", 2, 0, -2, 1, -2, 0, 1))
        eq = {k: 1.0 for k in sig.WEIGHTS}
        self.assertGreater(sig.effective_factors(sig.variance_shares([g], eq)),
                           sig.effective_factors(sig.variance_shares([g], sig.WEIGHTS)))

    def test_dropping_zero_weight_element_changes_nothing(self):
        """權重為 0 的元素移除後,前 N 名不可能易主——否則 composite_of 有 bug。"""
        g = rows(("A", 2, 1, 0, -1, 2, 2, 1), ("B", -2, 0, 1, 2, -1, -2, 0),
                 ("C", 1, -2, -1, 0, 0, 2, 2), ("D", 0, 2, 2, 1, 1, -2, -1))
        zero = [k for k, v in sig.WEIGHTS.items() if not v]
        for k in zero:
            self.assertEqual(sig.top_n_churn([g], k), 0, f"s_{k} 權重為 0 卻改變了名次")

    def test_get_accepts_sqlite_row_and_missing_column(self):
        """validate.py 餵 sqlite3.Row(無 .get);缺欄與 NULL 都要當 0。"""
        con = sqlite3.connect(":memory:")
        con.row_factory = sqlite3.Row
        con.execute("CREATE TABLE t(stock_id TEXT, s_price INT, s_resil INT)")
        con.execute("INSERT INTO t VALUES('A', 2, NULL)")
        r = con.execute("SELECT * FROM t").fetchone()
        self.assertEqual(sig._get(r, "s_price"), 2)
        self.assertEqual(sig._get(r, "s_resil"), 0, "NULL 應視為 0")
        self.assertEqual(sig._get(r, "s_vol"), 0, "缺欄應視為 0,不得拋錯")
        self.assertEqual(sig._get({"s_price": 2}, "s_trust"), 0)
        con.close()

    # ── tier 持續性(§⑧)──────────────────────────────────────
    def test_dwell_excludes_censored_tail(self):
        """尾段只看到一半,計入會低估停留天數 → 預設排除。"""
        dates = ["d1", "d2", "d3", "d4", "d5"]
        seqs = {"A": [("d1", "真強"), ("d2", "真強"), ("d3", "真弱"),
                      ("d4", "真弱"), ("d5", "真弱")]}
        runs = sig.dwell_runs(seqs, dates)
        self.assertEqual(runs, {"真強": [2]}, "真弱 是尾段(截尾),應被排除")
        self.assertEqual(sig.dwell_runs(seqs, dates, include_censored=True),
                         {"真強": [2], "真弱": [3]})

    def test_date_gap_breaks_a_run(self):
        """日期不連續(例:成員中途才加入)不可被當成同一段連續停留。"""
        dates = ["d1", "d2", "d3", "d4"]
        seqs = {"A": [("d1", "真強"), ("d4", "真強")]}   # 缺 d2/d3
        self.assertEqual(sig.dwell_runs(seqs, dates, include_censored=True),
                         {"真強": [1, 1]}, "跨斷點必須切成兩段")

    def test_round_trip_only_counts_return_within_window(self):
        dates = [f"d{i}" for i in range(1, 9)]
        # A:d2 變 真弱,d3 就變回 真強 → 視窗內反覆
        # B:d2 變 真弱,直到 d8 才變回 → 超出 5 日視窗,不算反覆
        seqs = {
            "A": [("d1", "真強"), ("d2", "真弱"), ("d3", "真強"), ("d4", "真強"),
                  ("d5", "真強"), ("d6", "真強"), ("d7", "真強"), ("d8", "真強")],
            "B": [("d1", "真強"), ("d2", "真弱"), ("d3", "真弱"), ("d4", "真弱"),
                  ("d5", "真弱"), ("d6", "真弱"), ("d7", "真弱"), ("d8", "真強")],
        }
        back, total, rate = sig.round_trip_rate(seqs, dates, within=5)
        self.assertEqual(total, 4, "A 兩次(d2、d3)、B 兩次(d2、d8);變動一律計入分母")
        self.assertEqual(back, 1, "只有 A 的 d2→真弱 在 5 日內變回;"
                                  "B 到 d8 才回頭(d2+6),已超出視窗")
        self.assertAlmostEqual(rate, 0.25)

    def test_membership_turnover_arithmetic(self):
        """名單固定不變 → 每日新進 0、全量換手需時 None(不可除以零)。"""
        dates = ["d1", "d2", "d3"]
        seqs = {s: [(d, "真強") for d in dates] for s in ("A", "B")}
        tv = sig.membership_turnover(seqs, dates, "真強")
        self.assertEqual(tv["avg_n"], 2)
        self.assertEqual(tv["avg_in"], 0)
        self.assertIsNone(tv["full_turn_days"])
        self.assertIsNone(tv["turns_per_year"])

    def test_dwell_vs_horizon_flags_only_short_tradable_tiers(self):
        dates = [f"d{i}" for i in range(1, 21)]
        # 真強 每 2 日換一次(短);潛在/中性 不在 TRADABLE_TIERS,不該被列
        seq = []
        for i, d in enumerate(dates):
            seq.append((d, "真強" if (i // 2) % 2 == 0 else "潛在/中性"))
        short = sig.dwell_vs_horizon({"A": seq}, dates, horizon=10)
        self.assertEqual([t for t, _ in short], ["真強"])
        self.assertEqual(sig.dwell_vs_horizon({"A": seq}, dates, horizon=1), [],
                         "量測窗短於停留時不該告警")

    def test_weights_come_from_score_config(self):
        """權重必須取自 score.WEIGHTS,不得在 signal_structure 另立一份。"""
        import score
        self.assertIs(sig.WEIGHTS, score.WEIGHTS)
        self.assertEqual(set(sig.ELEMENT_COLS.values()),
                         {f"s_{k}" for k in score.WEIGHTS})


if __name__ == "__main__":
    unittest.main()
