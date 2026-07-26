# -*- coding: utf-8 -*-
"""時間尺度視角契約(2026-07-26)。

整套評分只有 20 日一個週期。這區把同一檔放到短(close/ma5)、波段(ret20)、
趨勢(ma20/ma60)三個尺度上各排一次族群內名次,讓「這檔強不強」在不同週期的
相反答案能被看見(2026-07-24:南電 tier=真強、波段與趨勢皆 100 分位,短期僅 9)。

兩條非顯而易見的規矩必須釘住:

1. **冗餘門檻**。三個視角若彼此高度相關就只是同一件事講三遍。門檻沿用分歧視角
   的 |ρ| ≥ 0.8。最初的趨勢定義 close_adj/ma60 對波段 +0.78、對 ma20/ma60 +0.79,
   逼近門檻且兩邊都像,已否決——本檔斷言它沒有被改回去。
2. **ρ 必須逐日算再取中位**。單日 ρ 很吵:2026-07-24 的 short-trend 是 −0.29,
   全期中位卻是 +0.04。文案宣稱「全期 N 日中位」時,payload 就必須真的是中位,
   不能拿單日值配上全期的天數(這個錯誤在實作時發生過一次)。
"""
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import signal_structure as sig


class TimeLensContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        cls.builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")

    # ---------- 視角定義 ----------

    def test_three_lenses_use_distinct_time_scales(self):
        keys = [k for k, _, _, _ in sig.TIME_LENSES]
        self.assertEqual(keys, ["short", "swing", "trend"])
        defs = {k: (n, d) for k, _, n, d in sig.TIME_LENSES}
        self.assertEqual(defs["short"], ("close_adj", "ma5"))
        self.assertEqual(defs["trend"], ("ma20", "ma60"))
        self.assertEqual(defs["swing"], (None, None), "波段直接用 ret20,不走比值")

    def test_rejected_trend_definition_is_not_reinstated(self):
        """close_adj/ma60 對波段 +0.78、對 ma20/ma60 +0.79,已因逼近冗餘門檻否決。"""
        defs = {k: (n, d) for k, _, n, d in sig.TIME_LENSES}
        self.assertNotIn(("close_adj", "ma60"), defs.values(),
                         "close_adj/ma60 與另外兩個視角都太像,不可作為趨勢欄")

    def test_percentiles_use_average_rank_so_order_does_not_matter(self):
        """s_* 那次的教訓:排序切片在平手時隨餵入順序而變。三欄一律走 lens_pct。"""
        rows = [{"stock_id": f"S{i}", "close_adj": 10.0, "ma5": 10.0, "ma20": 10.0,
                 "ma60": 10.0, "ret20": 0.0, "grp": "g"} for i in range(6)]
        rows[0]["ret20"] = 0.5
        asc = sig.time_lenses(rows)
        desc = sig.time_lenses(list(reversed(rows)))
        by_id = {x["stock_id"]: x for x in desc}
        for x in asc:
            self.assertAlmostEqual(x["pct"]["swing"], by_id[x["stock_id"]]["pct"]["swing"],
                                   places=9, msg="餵入順序改變了百分位")
            # 全平手時每檔都應拿到同一個百分位(平均秩),不是 0/20/40/60/80/100
            self.assertAlmostEqual(x["pct"]["trend"], 50.0, places=9)

    def test_stock_missing_any_lens_is_dropped_not_partially_ranked(self):
        """暖身不足只排得出兩欄時,極差會與三欄的不可比 —— 整檔略過。"""
        rows = [{"stock_id": f"S{i}", "close_adj": 10.0 + i, "ma5": 10.0, "ma20": 10.0,
                 "ma60": 10.0, "ret20": 0.01 * i, "grp": "g"} for i in range(4)]
        rows[0]["ma60"] = None
        out = sig.time_lenses(rows)
        self.assertEqual({x["stock_id"] for x in out}, {"S1", "S2", "S3"})

    def test_zero_denominator_does_not_raise(self):
        rows = [{"stock_id": "A", "close_adj": 10.0, "ma5": 0.0, "ma20": 1.0, "ma60": 1.0,
                 "ret20": 0.0, "grp": "g"},
                {"stock_id": "B", "close_adj": 10.0, "ma5": 5.0, "ma20": 1.0, "ma60": 1.0,
                 "ret20": 0.1, "grp": "g"},
                {"stock_id": "C", "close_adj": 12.0, "ma5": 5.0, "ma20": 1.0, "ma60": 1.0,
                 "ret20": 0.2, "grp": "g"}]
        self.assertEqual({x["stock_id"] for x in sig.time_lenses(rows)}, {"B", "C"})

    # ---------- ρ 的算法要對得上文案 ----------

    def test_builder_computes_rho_across_all_days_not_just_today(self):
        m = re.search(r"def build_lenses\(.*?\n(?=\n\ndef |\Z)", self.builder, re.S)
        self.assertIsNotNone(m)
        body = m.group(0)
        self.assertIn("rho_median", body)
        self.assertRegex(body, r"for d in days:", "ρ 中位必須逐日重算,不能只取最後一日")
        self.assertIn("statistics.median", body)

    def test_copy_labels_median_and_today_separately(self):
        """文案同時秀「全期中位 / 今日」,兩個值必須來自不同 payload 欄位。"""
        self.assertIn("const rho=k=>fx(L.rho_median[k]), rhoToday=k=>fx(L.rho[k]);", self.template)
        self.assertIn("全期 ${L.n_days} 日中位", self.template)

    def test_copy_discloses_short_window_and_no_standard_error(self):
        """趨勢欄要 60 日暖身,窗口比其他區短且幾乎全在同一段回檔——不可略過不提。"""
        for frag in ("60 個交易日暖身", "在別的行情下 ρ 未必相同", "不當假設檢定，故不附標準誤"):
            self.assertIn(frag, self.template)

    # ---------- 觀察層身分 ----------

    def test_lens_section_declares_it_is_not_a_signal(self):
        self.assertIn("這是描述，不是買賣訊號", self.template)
        self.assertIn("三欄都未計分、未進分層", self.template)

    def test_lens_payload_never_enters_scoring(self):
        """time_lenses 只讀 daily_metrics,不得寫任何表或碰 daily_scores。"""
        src = (SCRIPTS / "signal_structure.py").read_text(encoding="utf-8")
        m = re.search(r"def time_lens_summary\(.*?\n(?=\n\ndef )", src, re.S)
        self.assertIsNotNone(m)
        for banned in ("INSERT", "UPDATE", "daily_scores"):
            self.assertNotIn(banned, m.group(0))
        gm = re.search(r"def group_metric_rows\(.*?\n(?=\n\ndef |\Z)", src, re.S)
        # 只剝開頭的 docstring(它本來就會提到「不支援 snapshot_id」);
        # 不能無差別剝所有三引號字串,SQL 也是三引號寫的。
        code = re.sub(r'^(def [^\n]*\n\s*)""".*?"""', r"\1", gm.group(0), flags=re.S)
        self.assertNotIn("snapshot_id", code,
                         "快照表沒有均線欄,不可假裝支援 as-seen 快照")
        self.assertIn("daily_metrics", code)

    # ---------- 產出物 ----------

    def test_built_lens_section_is_present_and_consistent(self):
        index = ROOT / "index.html"
        if not index.exists():
            self.skipTest("index.html 尚未產生")
        html = index.read_text(encoding="utf-8")
        self.assertNotIn("__LENS_JSON__", html, "placeholder 未被替換")
        self.assertIn('<section id="lens"', html)
        self.assertIn('href="#lens"', html)
        L = json.JSONDecoder().raw_decode(html, html.index("LENS=") + len("LENS="))[0]
        self.assertIsNotNone(L, "LENS payload 是 null,整區會靜默消失")
        for k in ("short-swing", "short-trend", "swing-trend"):
            self.assertLess(abs(L["rho_median"][k]), 0.8,
                            f"{k} 全期中位 ρ 超過冗餘門檻,兩個視角其實是同一件事")
        for x in L["all"]:
            self.assertAlmostEqual(x["sp"], max(x["s"], x["w"], x["t"]) - min(x["s"], x["w"], x["t"]),
                                   places=1, msg=f"{x['id']} 的極差與三欄對不上")


if __name__ == "__main__":
    unittest.main()
