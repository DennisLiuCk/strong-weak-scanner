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

    def test_template_is_a_complete_traditional_chinese_document(self):
        html = self.template.strip()
        self.assertTrue(html.lower().startswith("<!doctype html>"))
        self.assertIn('<html lang="zh-Hant-TW">', html)
        self.assertIn('<meta charset="utf-8">', html)
        self.assertIn('name="viewport" content="width=device-width, initial-scale=1"', html)
        self.assertIn('<main id="main">', html)
        self.assertTrue(html.endswith("</html>"))

    def test_first_screen_overview_has_navigation_and_injected_payload(self):
        for anchor in ("overview", "groups-section", "tiers-section", "stocks-section", "method"):
            self.assertIn(f'href="#{anchor}"', self.template)
        self.assertIn('id="overview" aria-labelledby="overviewTitle"', self.template)
        self.assertIn('id="overviewSummary"', self.template)
        self.assertIn('id="overviewPoints"', self.template)
        self.assertIn("var OVERVIEW = __OVERVIEW_JSON__;", self.template)
        self.assertIn('html.replace("__OVERVIEW_JSON__"', self.builder)

        overview = bd.build_overview([
            {"grp": "passive", "state": "中性觀察", "med_dip": -0.27, "rel20": 0.01},
            {"grp": "power", "state": "中性觀察", "med_dip": -0.80, "rel20": -0.02},
        ])
        self.assertIn("沒有族群符合", overview["headline"])
        self.assertIn("2/2 族群", overview["summary"])
        self.assertIn("仍淨賣", overview["summary"])
        self.assertIn("相對最好不等於已出現買超", overview["summary"])

    def test_group_heatmap_and_five_day_tier_flow_share_group_filter(self):
        for marker in (
            'id="groupHeatShell"', 'id="groupHeat"', "function rankOf(g,key)",
            'id="tierFlowShell"', 'id="tierFlow"', "var TIER_FLOW = __TIER_FLOW_JSON__;",
            'groupHeat.querySelectorAll("tbody tr[data-g]")',
            'tierFlowHost.querySelectorAll(".flow-row[data-g]")',
        ):
            self.assertIn(marker, self.template)
        self.assertNotIn('textContent="39 檔', self.template)
        for marker in ('"heat": {', '"states": states', '"lastChange": last_change',
                       'html.replace("__TIER_FLOW_JSON__"'):
            self.assertIn(marker, self.builder)
        self.assertIn("LIMIT 5", self.builder)

    def test_stock_verdict_drawer_has_seven_factor_diverging_profile(self):
        for marker in (
            "function renderFactorProfile(box, factors)", "七因子分數輪廓",
            "gDivergeBar(score,2)", "if(html.factors && html.factors.length)",
            "條長表示元素分的相對位置", "factors:row.factors",
        ):
            self.assertIn(marker, self.template)
        self.assertEqual(self.template.count("factors:row.factors"), 3)
        for label in ("①相對強弱", "①抗跌", "②量", "③外資", "③修正日買賣", "④投信", "⑤融資券"):
            self.assertIn(f'"label": "{label}"', self.builder)

    def test_mobile_cards_replace_the_wide_matrix_and_share_filters_search(self):
        required = (
            'class="mobile-stocks" id="mobileStocks"',
            "function mobileStockCard(row)",
            "var mobileCards = mobileStocks ?",
            'mobileStocks.querySelectorAll("[data-g]")',
            "mobileCards.forEach(function(card)",
            "@media (max-width:720px)",
            ".scroller{display:none}",
            ".mobile-stocks{display:block}",
            "min-height:44px",
        )
        for marker in required:
            self.assertIn(marker, self.template)
        self.assertIn("target.scrollIntoView", self.template)
        self.assertIn("快速導覽若直接改 hash 會把篩選清掉", self.template)

    def test_glossary_is_available_in_metric_and_note_drawers(self):
        for term in ("NRE", "Tape-out", "ASIC", "CoWoS", "CSP", "ODM", "CCL",
                     "YoY", "MoM", "EPS", "毛利率"):
            self.assertIn(f'"{term}":[', self.template)
        self.assertIn("function appendGlossary(container, source)", self.template)
        self.assertEqual(self.template.count("appendGlossary(box,"), 2)
        self.assertIn("本文術語白話解釋", self.template)

    def test_technical_guide_explains_meaning_and_reading_order(self):
        for marker in (
            'id="technical-guide"', "MA／RSI／VOL 的意義與盤讀順序",
            "比較近14日平均上漲力道與平均下跌力道", "50是兩種力道的分界",
            "建議盤讀順序", "常見組合怎麼讀", "均線向上＋RSI下降",
            "什麼叫「穿越」", "前一交易日現價在MA20下方或相等",
            'howHref:"#technical-guide"', 'jl.href=html.howHref||"#method"',
        ):
            self.assertIn(marker, self.template)

    def test_ma_series_use_distinct_non_semantic_colors_with_text_labels(self):
        for marker in (
            "--ma5:#b84e00", "--ma20:#0b66b2", "--ma60:#6f4ba8",
            "MA5 橘色 · 短線", "MA20 藍色 · 中期", "MA60 紫色 · 較長期",
            "顏色只區分週期，不代表強弱", "function appendMaText(node,t)",
            "function appendTechSeriesRow(labelNode,valueNode,series)",
            "techSeries:row.tech.series",
        ):
            self.assertIn(marker, self.template)

    def test_chart_nodes_expose_dates_values_meanings_and_sources_across_input_modes(self):
        for marker in (
            'id="chartTip" role="status" aria-live="polite"',
            "function bindChartNode(mark,payload,guide)",
            'mark.addEventListener("mouseenter"',
            'mark.addEventListener("click"',
            "function registerChartKeyboard(svg,entries,label)",
            'e.key==="ArrowLeft"||e.key==="ArrowRight"',
            "滑過節點；鍵盤可用左右方向鍵",
            "點按圖中日期／柱體看數值",
            "chart-tip-source",
            "FinMind TaiwanStockMonthRevenue",
            "daily_scores：七因子元素分 × 權重",
            "bindChartNode(startHit",
            "bindChartNode(endHit",
            "五日變層軌跡",
        ):
            self.assertIn(marker, self.template)
        for marker in (
            '"dates": [_value(x, "date") for x in chart_rows]',
            '"sparkDates": spark_dates',
            '"dipDates": [x["date"]',
            '"relDates": [x["date"]',
            '"date5": ser[-6]["date"]',
            '"comp3Dates": [h["date"] for h in comp_hist]',
        ):
            self.assertIn(marker, self.builder)
        self.assertEqual(self.template.count("fundSparkDates:"), 2)
        self.assertEqual(self.template.count("gCompositeBar(row.comp"), 2)

    def test_first_desktop_click_opens_persistent_drawer(self):
        touch_click_to_drawer = (
            'node.addEventListener("click", function(){ hideTip(); '
            'openSheet(payload(),null,node); });'
        )
        desktop_click_to_drawer = (
            'node.addEventListener("click", function(){ cancelHover(); '
            'openSheet(payload(),null,node); });'
        )
        # TOUCH 先關 tooltip；hover-capable desktop 同時取消延遲 timer，再開持續 drawer。
        self.assertIn(touch_click_to_drawer, self.template)
        self.assertIn(desktop_click_to_drawer, self.template)
        self.assertNotIn('if(tip.classList.contains("on")) { hideTip(); }', self.template)
        self.assertNotIn('else { showTip(payload()', self.template)
        self.assertIn('node.setAttribute("aria-haspopup","dialog")', self.template)
        self.assertIn('function openSheet(html, renderFn, trigger)', self.template)
        self.assertIn("lastSheetFocus = trigger || document.activeElement", self.template)
        self.assertIn("window.requestAnimationFrame(function(){ if(sheetClose) sheetClose.focus(); })",
                      self.template)
        self.assertIn('if(e.key==="Escape"){ closeSheet(); return; }', self.template)
        self.assertIn("lastSheetFocus.focus", self.template)

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

    def test_note_badges_expose_verification_separately_from_freshness(self):
        for status in ("ai_draft", "partially_verified", "independently_verified", "conflicted"):
            self.assertIn(status, self.template)
            self.assertIn(status, self.builder)
        for field in ("reviewedBy", "reviewedAt", "reviewScope", "qualityInvalid",
                      "claimCount", "citedClaims", "primaryClaims", "contentAsOf"):
            self.assertIn(field, self.template)
            self.assertIn(field, self.builder)
        self.assertIn('row.note.cls+(row.note.due?" due":"")', self.template)
        self.assertIn("最後更新日只代表編修日期", self.template)
        self.assertIn("其餘內容仍視為 AI 草稿", self.template)
        self.assertIn("不把公司說法自動視為客觀真相", self.template)
        self.assertIn("仍保留來源衝突警示", self.template)
        self.assertIn('note.className="toggle note-toggle "+row.note.cls+(row.note.due?" due":"")',
                      self.template)
        self.assertIn('note.textContent="📝 "+row.note.label', self.template)
        self.assertIn('bl.t==="ul"||bl.t==="ol"', self.template)
        self.assertIn('bl.t==="h3"', self.template)
        self.assertNotIn("質化研究筆記則由人工整理公開資訊", self.template)

    def test_research_drawer_tabs_formal_note_and_leading_hypotheses(self):
        for marker in (
            "function researchPayload(row)", "function renderResearchDetail(box, research)",
            "function renderHypothesisDetail(box, hypothesis)", 'setText(noteTab,"正式筆記")',
            'setText(hypTab,"領先假說 "+research.hypothesis.count+" 則")',
            "可證偽", "多篇轉載同一消息鏈不視為獨立確認", "has-hypothesis",
        ):
            self.assertIn(marker, self.template)
        for marker in ("load_hypothesis_reports", 'obj["hypothesis"]',
                       '"statusCounts"', '"sections"'):
            self.assertIn(marker, self.builder)

    def test_hypothesis_statuses_are_reader_facing_and_explain_the_state_machine(self):
        for marker in (
            "這些狀態如何變化？", "初次捕捉 → 持續觀察或證據警示",
            "已驗證成立／已驗證不成立", "meta.label||key",
        ):
            self.assertIn(marker, self.template)
        self.assertIn('"statusInfo"', self.builder)
        self.assertNotIn('parts.push(key+" "+counts[key])', self.template)

    def test_hypothesis_v2_audit_dimensions_are_visible(self):
        for marker in (
            "樣本性質：前瞻捕捉", "回溯基線", "到期未決", "獨立消息鏈",
            "閱讀狀態由生命週期、證據強度與警示組合而成",
        ):
            self.assertIn(marker, self.template)
        for marker in (
            '"captureModeCounts"', '"lifecycleCounts"', '"dueCount"',
            '"independentChains"', '"schemaVersion"',
        ):
            self.assertIn(marker, self.builder)


if __name__ == "__main__":
    unittest.main()
