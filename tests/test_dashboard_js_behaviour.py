# -*- coding: utf-8 -*-
"""把模板裡幾個純函式**真的執行過**,而不是比對原始碼字串(2026-07-26)。

起因:2026-07-26 的複核指出,新加的「契約測試」大多只 assertIn 一段原始碼。
那種測試擋得住有人刪掉那行,擋不住有人改壞行為——例如把 `statistics.median(v)`
換成 `median(v[-1:])`,字串全在、行為全錯;也擋不住註解裡出現同一段字。
更糟的是儀表板上最容易誤導人的一段(`lensShape` 的白話標籤)完全沒有測試。

這裡改用 node 直接跑模板抽出來的函式。node 在 GitHub ubuntu runner 上是預裝的;
真的沒有就 skip,不讓它變成硬相依(專案鐵律:零第三方依賴)。

抽函式而不是載入整個模板,是因為模板要等 build 注入 __*_JSON__ 才是合法 JS。
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TEMPLATE = SCRIPTS / "dashboard_template.html"
NODE = shutil.which("node")


def extract(name):
    """抽出模板裡某個 top-level function 的完整原始碼(以下一個 top-level 宣告為界)。"""
    src = TEMPLATE.read_text(encoding="utf-8")
    m = re.search(r"^(?:function %s\(|const %s=)" % (name, name), src, re.M)
    if not m:
        raise AssertionError(f"模板裡找不到 top-level 的 {name}")
    rest = src[m.start():]
    nxt = re.search(r"^(?:function |const |document\.getElementById)", rest[1:], re.M)
    return rest[:nxt.start() + 1] if nxt else rest


@unittest.skipIf(NODE is None, "node 不在 PATH,跳過 JS 行為測試")
class DashboardJsBehaviourTest(unittest.TestCase):
    def run_js(self, prelude, expr_cases):
        """expr_cases: [(說明, JS 運算式)] → 回傳每個運算式的 JSON 結果。"""
        body = prelude + "\nconst __out=[];\n" + "".join(
            f"__out.push({e});\n" for _, e in expr_cases
        ) + "console.log(JSON.stringify(__out));"
        with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False,
                                         encoding="utf-8") as f:
            f.write(body)
            path = f.name
        try:
            r = subprocess.run([NODE, path], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=60)
            self.assertEqual(r.returncode, 0, f"node 失敗:{r.stderr}")
            return json.loads(r.stdout.strip().splitlines()[-1])
        finally:
            Path(path).unlink(missing_ok=True)

    # ---------- fmtPct:唯一的百分比格式化入口 ----------

    def test_fmtPct_behaviour(self):
        pre = extract("fmtPct")
        cases = [
            # (輸入, 預期輸出, 為什麼這格重要)
            ("-0.4", "−0.4%", "小負數不可印成 -0%,那會把在跌讀成持平"),
            ("-0.0", "0.0%", "後端 round(−0.04,1) 會得到 −0.0;JS 的 -0>=0 是 true,"
                             "用 v>=0?'+':'−' 會印成綠色的「+0.0%」"),
            ("0", "0.0%", "零不給正負號"),
            ("6.2", "+6%", "|v|≥1 取整數"),
            ("-21.75", "−22%", "負號要 U+2212,不是 ASCII hyphen"),
            ("-38.24", "−38%", ""),
            ("null", "—", "缺值不可印成 NaN%"),
        ]
        got = self.run_js(pre, [(c[2], f"fmtPct({c[0]})") for c in cases])
        for (inp, want, why), g in zip(cases, got):
            self.assertEqual(g, want, f"fmtPct({inp}) = {g!r},應為 {want!r}。{why}")
        # 明確帶 dp 時要照做
        self.assertEqual(self.run_js(pre, [("", "fmtPct(-38.24,1)")])[0], "−38.2%")

    def test_pctCol_treats_zero_and_negative_zero_as_neutral(self):
        pre = extract("fmtPct") + "\n" + extract("pctCol")
        got = self.run_js(pre, [("", f"pctCol({v})") for v in ("3", "-3", "0", "-0.0", "null")])
        self.assertEqual(got, ["var(--strong)", "var(--weak)", "var(--muted)",
                               "var(--muted)", "var(--muted)"],
                         "0 與 −0 不可上漲跌色")

    def test_only_one_percent_formatter_exists(self):
        """單一入口才擋得住「兩個畫面同一個數字長得不一樣」。"""
        src = TEMPLATE.read_text(encoding="utf-8")
        # 舊的行內寫法各自處理正負號與小數位,是這次三個格式 bug 的來源
        self.assertNotIn("(r>=0?'+':'−')", src)
        self.assertNotIn("(a.med>=0?'+':'−')", src)
        self.assertNotIn("r.toFixed(0)+'%'", src)
        self.assertEqual(len(re.findall(r"^function fmtPct\(", src, re.M)), 1)

    # ---------- lensShape:全站最容易誤導人的一段文案 ----------

    def test_lensShape_never_narrates_price_direction(self):
        """三欄是族群內橫斷面名次,不含漲跌資訊。標籤講「轉強/回檔/反彈」等於
        用名次宣稱價格事件——2026-07-24 有 10/14 檔被標「波段轉強」而 20 日
        絕對報酬是負的(最深 −34.9%)。標籤一律只能講名次。"""
        pre = extract("LENS_HI") + "\n" + extract("lensShape")
        pts = (0, 20, 39, 40, 50, 59, 60, 80, 100)
        cases = [(f"{a},{b},{c}", f"lensShape({a},{b},{c})")
                 for a in pts for b in pts for c in pts]
        labels = set(self.run_js(pre, cases))
        banned = ["轉強", "轉弱", "回檔", "反彈", "領漲", "落後", "跟上", "起漲",
                  "突破", "止跌", "翻多", "翻空", "會漲", "會跌"]
        for lab in labels:
            for word in banned:
                self.assertNotIn(word, lab,
                                 f"標籤「{lab}」用名次敘述價格事件(禁用詞:{word})")
            self.assertIn("名次", lab, f"標籤「{lab}」沒說清楚講的是名次")
        self.assertGreaterEqual(len(labels), 5, "標籤沒有分辨力")

    def test_lensShape_is_total_and_order_consistent(self):
        """任何百分位組合都要有標籤(不可回 undefined),且對稱輸入給對稱答案。"""
        pre = extract("LENS_HI") + "\n" + extract("lensShape")
        got = self.run_js(pre, [
            ("全高", "lensShape(100,100,100)"), ("全低", "lensShape(0,0,0)"),
            ("邊界 60", "lensShape(60,60,60)"), ("邊界 39.9", "lensShape(39.9,39.9,39.9)"),
            ("中間", "lensShape(50,50,50)"),
            ("波高趨低", "lensShape(50,100,0)"), ("趨高波低", "lensShape(50,0,100)"),
        ])
        self.assertNotIn(None, got)
        self.assertEqual(got[0], "三個週期名次都靠前")
        self.assertEqual(got[1], "三個週期名次都靠後")
        self.assertEqual(got[2], "三個週期名次都靠前", "60 是靠前的下界(含)")
        self.assertEqual(got[3], "三個週期名次都靠後", "39.9 仍算靠後")
        self.assertNotEqual(got[5], got[6], "波段↔趨勢對調應給不同標籤")

    def test_absCaveat_disappears_when_nothing_to_warn_about(self):
        """多頭時沒有「相對強但絕對跌」的個股,警語必須整句消失,不留半句空話。"""
        pre = ("const UPPER_TIERS={'真強':1,'蓄勢·外資佈局':1,'強但過熱':1};\n"
               "let D={allStocks:[]};\n" + extract("absCaveat"))
        got = self.run_js(pre, [
            ("空集合", "(D.allStocks=[],absCaveat())"),
            ("全為正", "(D.allStocks=[{nm:'A',tier:'真強',r20:5},"
                       "{nm:'B',tier:'真強',r20:1}],absCaveat())"),
            ("有負值", "(D.allStocks=[{nm:'A',tier:'真強',r20:5},"
                       "{nm:'B',tier:'真強',r20:-3.5}],absCaveat())"),
            ("−0 不算負", "(D.allStocks=[{nm:'A',tier:'真強',r20:-0.0}],absCaveat())"),
            ("弱層不計入", "(D.allStocks=[{nm:'A',tier:'真弱',r20:-30}],absCaveat())"),
        ])
        self.assertEqual(got[0], "")
        self.assertEqual(got[1], "")
        self.assertIn("1 檔 20 日絕對報酬為負", got[2])
        self.assertIn("B", got[2], "最深的那檔要指名")
        self.assertEqual(got[3], "", "−0 不是負值")
        self.assertEqual(got[4], "", "只看上層 tier")


if __name__ == "__main__":
    unittest.main()
