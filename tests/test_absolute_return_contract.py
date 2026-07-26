# -*- coding: utf-8 -*-
"""相對分數 vs 絕對報酬的顯示契約(2026-07-26)。

整套評分都是**族群內相對排名**,不含任何絕對漲跌資訊。2026-07-24 當日
23 檔相對強勢裡有 15 檔 20 日絕對報酬為負(最深 凱美 −38.2%),而族群排行榜
「動能 vs 全體」第 3 名的電源供應絕對報酬是 −10.4%、10 檔裡只有 1 檔在漲——
只看相對數字會把「跌得比較少」讀成「在漲」。

本檔把「相對旁邊必須並列絕對」釘成契約。三個曾經真的踩到的坑各有一條斷言:

1. `ret20` 沒進 per-stock payload → 前端讀到 undefined,標記靜默不出現。
2. `D.allStocks` 投影漏欄位 / 欄名不一致(payload 用 `tier_confirmed`、
   投影後叫 `tier`)→ 篩選永遠空集合,警語變成空字串,版面看起來完全正常。
3. `toFixed(0)` 讓 −0.4% 印成「-0%」→ 正在跌被讀成持平。
"""
import json
import re
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))


class AbsoluteReturnContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        cls.builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")

    # ---------- builder 側:資料要真的送出去 ----------

    def test_per_stock_payload_carries_absolute_20d_return(self):
        self.assertIn('"ret20": round(r["ret20"] * 100, 1)', self.builder,
                      "per-stock payload 必須帶 20 日絕對報酬,否則前端只有相對分數")

    def test_group_payload_carries_absolute_median_and_breadth(self):
        self.assertIn('"abs20": gabs.get(g)', self.builder)
        # 中位數 + 上漲家數:單看中位數無法分辨「全族群一起小跌」與「少數重挫拉低」
        self.assertRegex(self.builder, r'(?s)gabs\[g\]\s*=\s*\{"med":.*?"pos":.*?"n":',
                         "族群絕對表現要同時給中位報酬與上漲家數/總家數")

    # ---------- 前端側:投影不能把欄位弄丟 ----------

    def test_all_stocks_projection_carries_r20(self):
        """D.allStocks 是分層帶與警語共用的投影;漏掉 r20 會讓兩者同時靜默失效。"""
        m = re.search(r"allStocks:DATA\.map\(function\(s\)\{return \{(.*?)\};\}\)", self.template)
        self.assertIsNotNone(m, "找不到 allStocks 投影,契約需同步更新")
        self.assertIn("r20:s.ret20", m.group(1))

    def test_caveat_and_pill_read_projected_field_names(self):
        """警語與個股列都吃 allStocks 投影,必須用投影後的欄名(r20/tier),
        不是 payload 原欄名(ret20/tier_confirmed)——用錯不會報錯,只會靜默空掉。"""
        m = re.search(r"function absCaveat\(\)\{(.*?)\n\n", self.template, re.S)
        self.assertIsNotNone(m)
        body = m.group(1)
        self.assertIn("D.allStocks", body)
        self.assertNotIn("tier_confirmed", body)
        self.assertNotIn("s.ret20", body)
        self.assertRegex(body, r"UPPER_TIERS\[s\.tier\]")
        self.assertRegex(body, r"s\.r20")

    def test_upper_tiers_matches_score_tier_names(self):
        """tier 名稱若在 score.py 改動而 UPPER_TIERS 沒同步,標記會全部消失且不報錯。"""
        m = re.search(r"const UPPER_TIERS=\{(.*?)\};", self.template)
        self.assertIsNotNone(m)
        names = set(re.findall(r"'([^']+)'", m.group(1)))
        self.assertEqual(names, {"真強", "蓄勢·外資佈局", "強但過熱"})
        # ORDER 是 score.py 函式內的區域變數,只能從原始碼取——它才是 tier 名稱的來源
        src = (SCRIPTS / "score.py").read_text(encoding="utf-8")
        order = re.search(r"ORDER = \[(.*?)\]", src)
        self.assertIsNotNone(order, "score.py 的 tier ORDER 找不到")
        known = set(re.findall(r'"([^"]+)"', order.group(1)))
        self.assertTrue(names.issubset(known),
                        f"UPPER_TIERS 有 score.py ORDER 不存在的 tier:{names - known}")

    def test_upper_tiers_is_top_level_not_nested(self):
        """absCaveat 在頂層、原本 UPPER_TIERS 被寫進 buildTiers 內部 → ReferenceError。"""
        for line in self.template.splitlines():
            if "const UPPER_TIERS=" in line:
                self.assertFalse(line.startswith(" "),
                                 "UPPER_TIERS 必須在頂層,否則頂層的 absCaveat 取不到")
                break
        else:
            self.fail("找不到 UPPER_TIERS")

    # ---------- 顯示格式 ----------

    def test_all_percent_rendering_goes_through_the_single_formatter(self):
        """小數位、U+2212 負號、−0 中性這三件事的**行為**由
        test_dashboard_js_behaviour 用 node 實際跑過;這裡只釘「沒有人繞過它」——
        行內各寫各的正是三個格式 bug 的來源。"""
        for spot in ("text:fmtPct(r)",                       # 分層帶個股列
                     "text:fmtPct(a.med,1)",                 # 族群排行榜絕對列
                     "text:fmtPct(s.r20,1)",                 # 族群內個股表格列
                     "text:'20日 '+fmtPct(r)"):              # 時間尺度卡
            self.assertIn(spot, self.template, f"{spot} 沒有走 fmtPct")
        self.assertNotIn("(r>=0?'+':'−')", self.template)
        self.assertNotIn("(a.med>=0?'+':'−')", self.template)

    def test_absolute_return_appears_on_every_per_stock_surface(self):
        """三個逐檔瀏覽介面都要有絕對報酬。原本只加在分層帶的 pill 上,
        族群內個股表格(主要瀏覽介面)仍只有相對綜合分,同一個數字在兩個畫面
        說不同的故事。"""
        self.assertIn("r20:s.ret20", self.template, "_slim 投影要帶 r20 給族群內個股表格")
        self.assertIn("r20:s.ret20,tier:s.tier_confirmed", self.template)
        self.assertIn('"r20": x["raw"]["swing"]', self.builder, "時間尺度卡要帶絕對報酬")

    def test_caveat_is_computed_from_live_data_never_hardcoded(self):
        """警語數字寫死會在行情反轉後變成假話;且 0 檔時整句必須消失。"""
        m = re.search(r"function absCaveat\(\)\{(.*?)\n\n", self.template, re.S)
        body = m.group(1)
        self.assertIn("if(!up.length||!neg.length) return '';", body)
        self.assertNotRegex(body, r"[「(（]\s*\d+\s*檔 20 日絕對報酬為負",
                            "檔數必須由當日資料現算")

    # ---------- 產出物 ----------

    def test_built_dashboard_has_full_absolute_coverage(self):
        index = ROOT / "index.html"
        if not index.exists():
            self.skipTest("index.html 尚未產生")
        html = index.read_text(encoding="utf-8")
        dec = json.JSONDecoder()
        i = html.index("const DATA=")
        stocks = dec.raw_decode(html, i + len("const DATA="))[0]
        groups = dec.raw_decode(html, html.index("GROUPS=", i) + len("GROUPS="))[0]
        missing = [s["id"] for s in stocks if s.get("ret20") is None]
        self.assertEqual(missing, [], f"這些個股缺 20 日絕對報酬:{missing}")
        for g in groups:
            a = g.get("abs20")
            self.assertIsNotNone(a, f"族群 {g['g']} 缺 abs20")
            self.assertGreater(a["n"], 0)
            self.assertLessEqual(a["pos"], a["n"])


if __name__ == "__main__":
    unittest.main()
