# -*- coding: utf-8 -*-
"""儀表板 UX 契約(2026-07-19 redesign 版)。

模板於 2026-07-19 換成 claude.ai/design 專案的純 JS/SVG 重寫版
(adapter 層吃同一組 __*_JSON__ placeholder,build_dashboard.py 零改動)。
本檔對齊新模板重寫;builder 側、策略凍結、公開文案與 2330 鐵律斷言原樣保留。

明示放棄、待日後裁決是否回補的舊功能(原斷言見 git 歷史 183a8f1 之前版本):
- 術語 glossary(appendGlossary)
- MA/RSI/VOL 教學區(technical-guide)
- 圖表節點 tooltip 與鍵盤左右鍵導覽(bindChartNode/registerChartKeyboard)
(官方資料數據解剖已於 2026-07-19 以 flowSection+#flow-guide 回補,契約見
 test_observation_dashboard.py)
"""
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

import build_dashboard as bd
import fetch_daily as fd
import score
import validate


class DashboardUxContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.template = (SCRIPTS / "dashboard_template.html").read_text(encoding="utf-8")
        cls.builder = (SCRIPTS / "build_dashboard.py").read_text(encoding="utf-8")

    # ---------- 文件骨架與導覽 ----------

    def test_template_is_a_complete_traditional_chinese_document(self):
        html = self.template.strip()
        self.assertTrue(html.lower().startswith("<!doctype html>"))
        self.assertIn('<html lang="zh-Hant-TW">', html)
        self.assertIn('<meta charset="utf-8">', html)
        self.assertIn('name="viewport" content="width=device-width, initial-scale=1"', html)
        self.assertIn('<main id="main">', html)
        self.assertTrue(html.endswith("</html>"))

    def test_quicknav_reaches_every_section(self):
        self.assertIn('aria-label="快速導覽"', self.template)
        for anchor in ("ov", "tsmc", "grp", "tier", "stocks", "flow-guide"):
            self.assertIn(f'href="#{anchor}"', self.template)
            self.assertIn(f'<section id="{anchor}"', self.template)
        # 個股詳情只由點列開抽屜,不再有底部常駐展示區(設計稿 demo 殘留,已移除)
        self.assertNotIn('<section id="detail"', self.template)
        # 提案文件的螢幕編號/選項徽章不得出現在正式版面
        for artifact in ("畫面 1", "畫面 2", "畫面 3", "畫面 4", "畫面 5",
                         "optHead(", "badgeid", "最白話"):
            self.assertNotIn(artifact, self.template)
        # header kicker 用動態範圍詞,不與 __H1__ 重複同文
        self.assertIn('<p class="kicker" style="color:var(--strong)">__SCOPE__</p>',
                      self.template)

    # ---------- 資料契約:placeholder 注入與 adapter ----------

    def test_placeholders_are_injected_and_adapted(self):
        pairs = ("__DATA_JSON__", "__GROUPS_JSON__", "__TIERS_JSON__",
                 "__TIER_FLOW_JSON__", "__OVERVIEW_JSON__", "__GRPMETA_JSON__",
                 "__WEIGHTS_JSON__", "__THRESH_JSON__", "__TSMC_JSON__",
                 "__DATE_ISO__", "__DATE__", "__PAGE_TITLE__", "__H1__",
                 "__SCOPE__")
        for ph in pairs:
            self.assertIn(ph, self.template)
            self.assertIn(f'"{ph}"', self.builder)
        # adapter 把完整 DATA 轉成 render 層的 slim 形狀;點列時用 byId 取完整物件
        self.assertIn("function _slim(s)", self.template)
        self.assertIn("_adaptTSMC", self.template)
        self.assertIn("D.byId", self.template)
        self.assertIn("tier:s.tier_confirmed", self.template)
        self.assertIn("tierLabel:s.tier_label", self.template)
        self.assertIn("waiting:s.tier_waiting", self.template)

    def test_first_screen_overview_headline_from_builder(self):
        self.assertIn("function buildOverview()", self.template)
        self.assertIn("今日分層概況", self.template)
        overview = bd.build_overview([
            {"grp": "passive", "state": "中性觀察", "med_dip": -0.27, "rel20": 0.01},
            {"grp": "power", "state": "中性觀察", "med_dip": -0.80, "rel20": -0.02},
        ])
        self.assertIn("沒有族群符合", overview["headline"])
        self.assertIn("2/2 族群", overview["summary"])
        self.assertIn("仍淨賣", overview["summary"])
        self.assertIn("相對最好不等於已出現買超", overview["summary"])

    # ---------- 族群層:四象限 + 熱圖 + 排行榜 ----------

    def test_group_section_has_quadrant_heatmap_and_leaderboard(self):
        for marker in ("function buildGroup()", "quadEl", "族群價籌四象限", "族群熱圖",
                       "rankClass", "openGroupSheet", 'class:\'hscroll\''):
            self.assertIn(marker, self.template)
        # 熱圖五欄對應 builder 的族群 heat payload
        for key in ("'dip'", "'breadth_f'", "'rel20'", "'dist60'", "'breadth_t'"):
            self.assertIn(key, self.template)
        # 族群數動態帶入,不得寫死
        self.assertIn("${G.length} 族群", self.template)
        self.assertNotIn("11 族群", self.template)
        # dist60 是小數(−0.36=−36%),顯示必須 ×100——設計稿 demo 資料曾假設已是百分比
        self.assertIn("{k:'dist60',label:'距60日高',hint:'離高點多遠',fmt:v=>(v*100).toFixed(1)+'%'}",
                      self.template)
        for marker in ('"heat": {', '"states": states', '"lastChange": last_change',
                       'html.replace("__TIER_FLOW_JSON__"'):
            self.assertIn(marker, self.builder)
        self.assertIn("LIMIT 5", self.builder)

    def test_tier_bands_and_five_day_flow(self):
        for marker in ("function buildTier()", "flowSpark", "近 5 日變層軌跡",
                       "D.tierFlow", "蓄勢候補", "不是買賣指示"):
            self.assertIn(marker, self.template)
        # 分層區可依族群篩選(選定=全列)、全部模式「＋N 檔」可展開、chip/變層列點開明細
        for marker in ("'aria-label':'分層篩選族群'", "檔 展開",
                       "onclick:()=>{expanded[k]=true;renderBands();}"):
            self.assertIn(marker, self.template)
        # 檔數不得寫死——用 D.allStocks.length 動態帶入
        self.assertIn("${D.allStocks.length}", self.template)
        self.assertNotIn("把全 121 檔", self.template)

    # ---------- 個股層:族群選單 + 搜尋排序 + 點列開詳情 ----------

    def test_stock_list_has_group_selector_search_sort_and_detail_click(self):
        for marker in ("function buildStocks1c()", "'aria-label':'選擇族群'",
                       "openStockDetail(s.id)", "class:'msearch'", "class:'sortbtn'",
                       "plainVerdict"):
            self.assertIn(marker, self.template)
        # 不得寫死示範族群
        self.assertNotIn("s.g==='passive'", self.template)
        self.assertNotIn("示範族群", self.template)

    def test_clickable_rows_support_keyboard(self):
        self.assertIn("role:'button'", self.template)
        self.assertIn("tabindex:'0'", self.template)
        self.assertIn("e.key==='Enter'||e.key===' '", self.template)
        self.assertIn(".clickrow:focus-visible", self.template)

    # ---------- 個股詳情:七因子 + null 防護 ----------

    def test_stock_detail_has_seven_factor_profile_with_null_guards(self):
        for marker in ("function buildDetail()", "七因子拆解", "diverg(f.score,2",
                       "(d.tech||{}).chart", "d.note&&h(",
                       "if(d.note)card.appendChild(researchTabs(d));"):
            self.assertIn(marker, self.template)
        # 綜合分尺度由注入的 WEIGHTS 導出,不得寫死(改權重時長條刻度須自動跟上)
        self.assertIn("const COMP_MAX=2*Object.values(WEIGHTS)", self.template)
        self.assertNotIn("8.8", self.template)
        # 趨勢標籤與營收 YoY 的顏色跟著資料方向走,不得沿用設計稿 demo 股的寫死色
        # (趨勢標籤自 1f 起在 priceChart() 內渲染,tech 為其參數)
        self.assertIn("tech.cls==='up'?'var(--strong)'", self.template)
        self.assertIn("String(yoy).trim().startsWith('-')?'var(--weak)'", self.template)
        for label in ("①相對強弱", "①抗跌", "②量", "③外資", "③修正日買賣",
                      "④投信", "⑤融資券"):
            self.assertIn(f'"label": "{label}"', self.builder)
        # builder 圖表資料必附日期(archive 快照可稽核)
        for marker in (
            '"dates": [_value(x, "date") for x in chart_rows]',
            '"sparkDates": spark_dates',
            '"dipDates": [x["date"]',
            '"relDates": [x["date"]',
            '"date5": ser[-6]["date"]',
            '"comp3Dates": [h["date"] for h in comp_hist]',
        ):
            self.assertIn(marker, self.builder)

    # ---------- 行動版與觸控 ----------

    def test_mobile_layout_collapses_grids_and_meets_touch_targets(self):
        for marker in ("@media (max-width:720px)", "min-height:44px",
                       ".srow{grid-template-columns:1fr", ".shead{display:none}",
                       ".bhead{display:none}", ".hscroll{overflow-x:auto}"):
            self.assertIn(marker, self.template)
        # 桌機鎖寬已移除,窄視口不得水平溢位
        self.assertNotIn("min-width:1180px", self.template)

    # ---------- 抽屜:focus 管理 ----------

    def test_sheet_manages_focus_and_escape(self):
        for marker in ("lastSheetFocus=document.activeElement",
                       "if(c) c.focus()",
                       "lastSheetFocus.focus()",
                       "if(e.key==='Escape')closeSheet();",
                       "role:'dialog'", "'aria-modal':'true'"):
            self.assertIn(marker, self.template)
        # 桌機抽屜要夠寬,個股詳情卡才能維持兩欄可讀排版
        self.assertIn("width:min(880px,100%)", self.template)

    # ---------- MA 色彩(區分週期,非強弱語意) ----------

    def test_ma_series_have_distinct_colors_in_both_themes(self):
        for marker in ("--ma5:#b26a12", "--ma20:#0b66b2", "--ma60:#6f4ba8",   # light
                       "--ma5:#ff9d4d", "--ma20:#62b5ff", "--ma60:#c4a7ff"):  # dark
            self.assertIn(marker, self.template)
        # 圖例帶文字標籤與數值,不只靠顏色(1f 起圖例=priceChart 的指標 chip:
        # 色塊+文字標籤+最新值,勾選狀態另以 ✓ 雙編碼)
        self.assertIn("h('span',{class:'mono',style:'font-size:10.5px;color:var(--muted)'}, val)",
                      self.template)
        self.assertIn("onx?'✓':''", self.template)

    # ---------- 策略凍結(原樣保留) ----------

    def test_strategy_constants_and_oos_cutoff_are_frozen(self):
        self.assertEqual(score.RANK_MAP, [(0.8, 2), (0.6, 1), (0.4, 0), (0.2, -1)])
        self.assertEqual(score.WEIGHTS, {
            "price": 1.4, "resil": 1.0, "vol": 0.3, "foreign": 0.5,
            "trust": 0.8, "dip": 0.0, "margin": 0.4,
        })
        self.assertEqual(
            (score.DZ_FOREIGN, score.DZ_TRUST, score.DZ_DIP),
            (0.3, 0.03, 0.03),
        )
        self.assertEqual(
            (score.VOLR_ACTIVE, score.VOLR_DRY, score.VOL_OVERHEAT, score.VOLR_OVERHEAT),
            ((1.2, 3.0), 0.5, 20.0, 5.0),
        )
        self.assertEqual(
            (score.MARGIN_DOWN_BIG, score.MARGIN_UP_MID, score.MARGIN_UP_BIG,
             score.MARGIN_UTIL_MID, score.MARGIN_UTIL_HOT),
            (-0.05, 0.06, 0.20, 6.0, 9.0),
        )
        self.assertEqual(
            (score.STEALTH_OFF_HIGH, score.SMOOTH_N, score.STRONG_MIN,
             score.WEAK_ABS, score.STEALTH_MIN),
            (-0.03, 3, 2.5, -3.5, 1.5),
        )
        self.assertEqual(
            (fd.REGIME_DD, fd.DD_MIN_OBS, fd.GRP_MIN_N, fd.GS_OFF_HIGH,
             fd.GS_BREADTH_LOW, fd.TDCC_LAG_DAYS),
            (-0.03, 10, 6, -0.05, 0.4, 3),
        )
        self.assertEqual(validate.IS_CUTOFF, "2026-07-05")

    # ---------- 台積電專區:觀察層鐵律(原樣保留 + 新模板 marker) ----------

    def test_tsmc_section_is_observation_layer_only(self):
        self.assertIn('id="tsmc"', self.template)
        self.assertIn("TSMC=__TSMC_JSON__", self.template)
        self.assertIn("上游錨點 · 觀察層（不計分）", self.template)
        self.assertIn("不在掃描範圍、不參與任何排名與評分", self.template)
        # 期別與查核狀態 chip 一律吃事件錨點資料,不得寫死
        self.assertIn("'台積電官方 IR · '+T.quarter", self.template)
        self.assertNotIn("2026 Q2", self.template)
        self.assertIn("scMap[T.status]", self.template)
        self.assertIn('html.replace("__TSMC_JSON__"', self.builder)
        self.assertIn("load_events", self.builder)
        self.assertIn("ref_price", self.builder)
        # 鐵律守護:2330 只能是觀察層參考個股——不在 universe、score.py 不讀 ref 表
        self.assertEqual(fd.REF_IDS, ["2330"])
        universe_csv = (ROOT / "config" / "universe.csv").read_text(encoding="utf-8")
        self.assertFalse(any(line.startswith("2330,") for line in universe_csv.splitlines()))
        score_src = (SCRIPTS / "score.py").read_text(encoding="utf-8")
        self.assertNotIn("ref_price", score_src)
        self.assertNotIn("ref_holding", score_src)

    # ---------- 公開文案鐵律(原樣保留) ----------

    def test_public_copy_avoids_absolute_or_actionable_rank_claims(self):
        public_copy = self.builder + "\n" + self.template
        forbidden = (
            "外資強力吃貨",
            "外資倒貨/大幅撤出",
            "投信強力認養",
            "投信大幅賣超",
            "外資出、散戶接",
            "價籌俱弱",
            "別追高",
            "補齊即升蓄勢",
            "修正日買超 9 族群最高",
            "營運動能向上",
            "營運動能轉弱",
            "默默接貨",
            "全部數據取自 FinMind",
        )
        for phrase in forbidden:
            self.assertNotIn(phrase, public_copy)

        for guardrail in (
            "不代表原始值為正或股價會漲",
            "不宣稱法人一定買進或賣出",
            "相對分靠前不保證原始值為正",
            "營收不等於獲利",
        ):
            self.assertIn(guardrail, public_copy)
        # 頁尾必須有資料來源說明(header sub 的承諾要有對應落點)
        self.assertIn("資料來源：TWSE／TPEx 官方每日批次與公告", self.template)

    # ---------- 筆記查核狀態:動態呈現,不得寫死「已核驗」 ----------

    def test_note_verification_status_is_dynamic_never_hardcoded(self):
        for status in ("ai_draft", "partially_verified", "independently_verified",
                       "conflicted"):
            self.assertIn(status, self.builder)
        for field in ("reviewedBy", "reviewedAt", "reviewScope", "qualityInvalid",
                      "claimCount", "citedClaims", "primaryClaims", "contentAsOf"):
            self.assertIn(field, self.builder)
        # 模板必須吃真實 note.label/cls/reviewScope,勿退回設計稿寫死的「✓ 已獨立核驗」
        self.assertIn("noteVerifyMeta", self.template)
        self.assertIn("d.note.label", self.template)
        self.assertNotIn("metaBox('查核狀態','✓ 已獨立核驗'", self.template)
        self.assertNotIn(">全部重要主張</b>'", self.template)
        # 已核章 chip 只給 independently_verified
        self.assertIn("s.note[0]==='independently_verified'", self.template)
        self.assertIn("✓已核筆記", self.template)

    # ---------- 研究面板:正式筆記與領先假說分層 ----------

    def test_research_tabs_split_formal_note_and_hypotheses(self):
        for marker in ("function researchTabs(d)", "正式筆記", "領先假說",
                       "可證偽", "不代表已證實", "narrativeBlock",
                       "勝負手 · 可觀測裁決點",
                       "不得作為生命週期轉移證據"):
            self.assertIn(marker, self.template)
        # 筆記/假說內容單一歸屬研究面板——右欄不得再放品質框或假說 teaser 複述
        self.assertNotIn("研究筆記品質", self.template)
        self.assertNotIn("sec30", self.template)
        for marker in ("load_hypothesis_reports", 'obj["hypothesis"]',
                       '"statusCounts"', '"sections"', '"statusInfo"',
                       '"captureModeCounts"', '"lifecycleCounts"', '"dueCount"',
                       '"independentChains"', '"schemaVersion"'):
            self.assertIn(marker, self.builder)


if __name__ == "__main__":
    unittest.main()
