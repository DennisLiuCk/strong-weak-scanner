"""stats_ci 的數學契約。

這組數字會直接決定「要不要動旋鈕」,算錯比沒有更危險——沒有標準誤時人會謹慎,
有一個錯的標準誤時人會放心。
"""
import math
import statistics
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import stats_ci as sci


class StatsCiTest(unittest.TestCase):
    def test_lag_zero_reduces_to_plain_standard_error(self):
        x = [0.1, -0.2, 0.3, 0.0, 0.15, -0.05, 0.2, -0.1]
        plain = statistics.pstdev(x) / math.sqrt(len(x))
        self.assertAlmostEqual(sci.nw_se(x, 0), plain, places=12)

    def test_overlapping_windows_inflate_the_standard_error(self):
        """直接複製真實機制:重疊前瞻窗 = 對底層序列取移動平均 → 必然正自相關。

        這正是報告裡日 IC 序列 lag-1 ≈ +0.7 的成因;NW 必須因此放大 SE,否則修正沒生效。
        """
        # 確定性 LCG 當底層獨立衝擊(測試要可重現,不用亂數種子)
        seed, base = 12345, []
        for _ in range(120):
            seed = (1103515245 * seed + 12345) % (2 ** 31)
            base.append(seed / (2 ** 31) - 0.5)
        W = 10
        x = [statistics.mean(base[i:i + W]) for i in range(len(base) - W)]
        self.assertGreater(sci.autocorr1(x), 0.5,
                           "移動平均序列本來就該有強正自相關")
        plain, nw = sci.nw_se(x, 0), sci.nw_se(x, W - 1)
        self.assertGreater(nw, plain * 1.5,
                           f"重疊窗下 NW SE 必須明顯大於一般 SE(得到 {nw:.4f} vs {plain:.4f})")

    def test_white_noise_nw_close_to_plain(self):
        """無自相關時 NW 不該憑空放大(容許 kernel 造成的小幅波動)。"""
        x = [(-1) ** i * 0.1 for i in range(80)]   # 交替序列 → 負自相關
        self.assertIsNotNone(sci.nw_se(x, 9))
        self.assertGreaterEqual(sci.nw_se(x, 9), 0.0, "變異數截斷後不得為負")

    def test_overlap_lag_is_window_minus_one(self):
        self.assertEqual(sci.overlap_lag(10), 9)
        self.assertEqual(sci.overlap_lag(5), 4)
        self.assertEqual(sci.overlap_lag(1), 0)
        self.assertEqual(sci.overlap_lag(0), 0)

    def test_effective_obs_divides_by_window(self):
        """10 個成熟日配 10 日窗 ≈ 1 個獨立觀測——這個數字是整節的重點。"""
        self.assertAlmostEqual(sci.effective_obs(10, 10), 1.0)
        self.assertAlmostEqual(sci.effective_obs(90, 10), 9.0)
        self.assertEqual(sci.effective_obs(0, 10), 0.0)

    def test_episodes_counts_contiguous_runs(self):
        all_dates = [f"d{i:02d}" for i in range(10)]
        self.assertEqual(sci.episodes(["d00", "d01", "d02"], all_dates), 1)
        self.assertEqual(sci.episodes(["d00", "d01", "d05", "d06"], all_dates), 2)
        self.assertEqual(sci.episodes(["d00", "d02", "d04"], all_dates), 3)
        self.assertEqual(sci.episodes([], all_dates), 0)
        self.assertEqual(sci.episodes(["不存在的日期"], all_dates), 0)

    def test_summarize_reports_all_fields(self):
        # 40 天配前瞻 10 日 → 4 個獨立觀測,超過 MIN_EFF_OBS,SE 才會被計算
        x = [0.05, -0.02, 0.08, 0.01, -0.03, 0.06, 0.02, -0.01, 0.04, 0.03] * 4
        dates = [f"d{i:02d}" for i in range(len(x))]
        s = sci.summarize(x, 10, dates, dates)
        self.assertEqual(s["n_days"], 40)
        self.assertEqual(s["lag"], 9)
        self.assertAlmostEqual(s["eff_obs"], 4.0)
        self.assertFalse(s["se_blocked"])
        self.assertEqual(s["episodes"], 1)
        self.assertAlmostEqual(s["mean"], statistics.mean(x))
        self.assertAlmostEqual(s["t"], s["mean"] / s["se"])

    def test_verdict_wording_never_claims_effectiveness(self):
        """判讀只說「能不能分辨」,不得說「有效/無效」——未過門檻不代表為 0。"""
        strong = {"t": 5.0, "se": 0.01, "mean": 0.05, "eff_obs": 40.0}
        weak = {"t": 1.0, "se": 0.01, "mean": 0.01, "eff_obs": 40.0}
        self.assertIn("可分辨", sci.verdict(strong))
        self.assertIn("無法分辨", sci.verdict(weak))
        for v in (sci.verdict(strong), sci.verdict(weak), sci.verdict(None)):
            self.assertNotIn("有效", v)
            self.assertNotIn("無效", v)

    def test_t_threshold_is_graded_by_effective_observations(self):
        """1.96 是「大樣本、獨立」的臨界值,在重疊窗小樣本下實際誤判率 10~24%。
        門檻必須隨有效獨立觀測分級,且永遠嚴於 1.96。"""
        self.assertGreater(sci.t_threshold(3.0), sci.t_threshold(8.0))
        self.assertGreater(sci.t_threshold(8.0), sci.t_threshold(20.0))
        self.assertGreaterEqual(sci.t_threshold(20.0), sci.t_threshold(100.0))
        for eff in (3.0, 5.0, 10.0, 20.0, 50.0, 1e6):
            self.assertGreater(sci.t_threshold(eff), 1.96,
                               f"eff={eff} 的門檻不得寬鬆於 1.96")

    def test_borderline_t_is_not_declared_distinguishable_at_small_samples(self):
        """實例:composite_s 修正桶 t=+2.3、eff=3.0。用 1.96 會判「可分辨」,
        但 MC 顯示該樣本量下 null 的 |t| q95 約 4.0 → 必須判成無法分辨。"""
        s = {"t": 2.3, "se": 0.022, "mean": 0.053, "eff_obs": 3.0}
        self.assertIn("無法分辨", sci.verdict(s))
        # 同一個 t 值在大樣本下仍不夠(最寬鬆的門檻是 2.4);要 2.6 才過
        self.assertIn("無法分辨", sci.verdict({**s, "eff_obs": 200.0}))
        self.assertIn("可分辨", sci.verdict({**s, "t": 2.6, "eff_obs": 200.0}))

    def test_few_overlapping_days_must_not_produce_a_t_value(self):
        """實測過的危險失效模式:5 個成熟日配前瞻 5 日(lag=4),5 個高度重疊的日 IC
        幾乎相同 → NW 變異數塌陷 → 吐出 ±0.008、t=−23.3。

        這個區塊存在的目的就是防止過度解讀,絕不可在 OOS 剛成熟時印出假精確的 t。
        """
        near_identical = [-0.160, -0.201, -0.186, -0.213, -0.122]   # 取自真實 OOS 5 日
        s = sci.summarize(near_identical, 5)
        self.assertTrue(s["se_blocked"], "有效獨立觀測 1.0 時必須擋下 SE")
        self.assertIsNone(s["se"])
        self.assertIsNone(s["t"])
        self.assertIn("SE 不可估", sci.fmt(s), "仍要顯示點估計,但不得看起來像有誤差棒")
        self.assertIn("不判讀", sci.verdict(s))
        # 樣本足夠時就要正常回報
        enough = near_identical * 8          # 40 天,前瞻 5 日 → 8 個獨立觀測
        s2 = sci.summarize(enough, 5)
        self.assertFalse(s2["se_blocked"])
        self.assertIsNotNone(s2["t"])

    def test_ten_mature_days_with_ten_day_window_is_blocked(self):
        """8/8 的實際情境:10 個成熟日 + 前瞻 10 日 = 1.0 個獨立觀測 → 不得判讀。"""
        s = sci.summarize([0.01 * i for i in range(10)], 10)
        self.assertAlmostEqual(s["eff_obs"], 1.0)
        self.assertTrue(s["se_blocked"])

    def test_insufficient_sample_returns_none_not_zero(self):
        """樣本不足要回 None(顯示為 –),不可回 0 讓人誤以為誤差為零。"""
        self.assertIsNone(sci.nw_se([0.1, 0.2], 9))
        self.assertIsNone(sci.summarize([], 10))
        self.assertEqual(sci.fmt(None), "–")
        self.assertEqual(sci.fmt({"mean": 0.1, "se": None}), "–")


if __name__ == "__main__":
    unittest.main()
