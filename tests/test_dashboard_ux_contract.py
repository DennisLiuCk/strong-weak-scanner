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
        for anchor in ("ov", "grp", "diverge", "tier", "stocks", "flow-guide"):
            self.assertIn(f'href="#{anchor}"', self.template)
            self.assertIn(f'<section id="{anchor}"', self.template)
        # 指定日期快照是首頁可見任務，不再只藏在 utility menu 底部。
        self.assertIn('href="#date-snapshots"', self.template)
        self.assertIn("id:'date-snapshots'", self.template)
        self.assertIn('mobileShortlist,\n      buildArchiveNavigation(),\n      signals,', self.template)
        self.assertNotIn("document.querySelector('.quicknav').appendChild(buildArchiveNavigation())", self.template)
        self.assertNotIn('href="#tsmc"', self.template)
        self.assertNotIn('<section id="tsmc"', self.template)
        # 個股詳情只由點列開抽屜,不再有底部常駐展示區(設計稿 demo 殘留,已移除)
        self.assertNotIn('<section id="detail"', self.template)
        # 提案文件的螢幕編號/選項徽章不得出現在正式版面
        for artifact in ("畫面 1", "畫面 2", "畫面 3", "畫面 4", "畫面 5",
                         "optHead(", "badgeid", "最白話"):
            self.assertNotIn(artifact, self.template)
        # A 版用緊湊 utility header 分出每日掃描與研究中心；範圍資訊退到輔助層。
        self.assertIn('<header class="sitebar">', self.template)
        self.assertIn('<nav class="primarynav" aria-label="主要區域">', self.template)
        self.assertIn('aria-current="page">市場掃描</a>', self.template)
        self.assertIn('<span class="brand-scope">__H1__</span>', self.template)
        self.assertIn('<span class="menu-scope">__SCOPE__</span>', self.template)
        # 選完錨點就收起 utility menu；點外部與 Escape 也都能關閉。
        self.assertIn("link.closest('.utility-menu')", self.template)
        self.assertIn("if(menu)menu.open=false", self.template)
        self.assertIn("if(!menu.contains(event.target))menu.open=false", self.template)
        self.assertIn("if(event.key==='Escape')", self.template)

    def test_daily_workspace_prioritises_scan_then_research_and_trust(self):
        """首頁順序就是產品決策：今日焦點→族群→個股→研究→深層分析→方法證據。"""
        order = [
            '<section id="ov"', '<section id="grp"', '<section id="tier"',
            '<section id="recent"', '<section id="diverge"', '<section id="lens"',
            '<section id="stocks"', '<section id="flow-guide"', '<section id="trust"',
        ]
        positions = [self.template.index(marker) for marker in order]
        self.assertEqual(positions, sorted(positions))
        self.assertIn("class:'command-grid'", self.template)
        self.assertIn("text:'進入族群比較 ↓'", self.template)
        self.assertIn("text:'今日強弱個股名單'", self.template)

    def test_single_column_overview_keeps_stock_shortlist_visible(self):
        """手機單欄時，個股名單入口要在首屏主要任務旁，而不是排在動能族群卡之後。"""
        overview = self.template[self.template.index("function buildOverview()"):
                                 self.template.index("function buildStrategyStatus()")]
        self.assertIn("const mobileShortlist=", overview)
        self.assertIn("class:'card shortlist-cta shortlist-cta-mobile'", overview)
        self.assertLess(overview.index("mobileShortlist,"), overview.index("buildArchiveNavigation()"))
        self.assertIn("text:'看今日強弱個股名單'", overview)
        self.assertIn("href:'#tier-primary-list'", overview)
        self.assertIn("if(location.hash==='#tier-primary-list')", self.template)
        self.assertIn("${strong} 強勢 · ${accum} 蓄勢 · ${weak} 弱勢", overview)
        self.assertIn(".shortlist-cta-mobile{display:none}", self.template)
        self.assertIn(".shortlist-cta-mobile{display:flex", self.template)
        self.assertIn(".command-side>.shortlist-cta{display:none}", self.template)
        self.assertIn("@media (max-width:720px) and (max-height:640px)", self.template)
        self.assertIn(".command-headline{font-size:24px;line-height:1.18}", self.template)
        self.assertIn(".lookup{margin-top:12px}", self.template)

    # ---------- 資料契約:placeholder 注入與 adapter ----------

    def test_placeholders_are_injected_and_adapted(self):
        pairs = ("__DATA_JSON__", "__GROUPS_JSON__", "__TIERS_JSON__",
                 "__TIER_FLOW_JSON__", "__OVERVIEW_JSON__", "__GRPMETA_JSON__",
                 "__WEIGHTS_JSON__", "__THRESH_JSON__",
                 "__STRATEGY_JSON__", "__DIVERGE_JSON__",
                 "__MKT_TIP_JSON__", "__DATE_ISO__", "__DATE__", "__PAGE_TITLE__", "__H1__",
                 "__SCOPE__", "__RANK_CHANGE_JSON__")
        for ph in pairs:
            self.assertIn(ph, self.template)
            self.assertIn(f'"{ph}"', self.builder)
        # adapter 把完整 DATA 轉成 render 層的 slim 形狀;點列時用 byId 取完整物件
        self.assertIn("function _slim(s)", self.template)
        self.assertIn("D.byId", self.template)
        self.assertIn("tier:s.tier_confirmed", self.template)
        self.assertIn("tierLabel:s.tier_label", self.template)
        self.assertIn("waiting:s.tier_waiting", self.template)

    def test_market_source_note_discloses_primary_crosscheck_and_fallback(self):
        self.assertIn("MKT=__MKT_TIP_JSON__", self.template)
        self.assertIn("text:MKT.src", self.template)
        self.assertIn("market-source-note", self.template)
        self.assertEqual(
            bd.market_source_text({
                "canonical_source": fd.MARKET_SOURCE_TWSE,
                "finmind_taiex": 100.0,
            }),
            "TWSE 官方 MI_INDEX 發行量加權股價報酬指數（FinMind 已交叉驗證）")
        self.assertIn("FinMind 待交叉驗證", bd.market_source_text({
            "canonical_source": fd.MARKET_SOURCE_TWSE,
            "finmind_taiex": None,
        }))
        self.assertIn("TWSE 官方缺值備援", bd.market_source_text({
            "canonical_source": fd.MARKET_SOURCE_FINMIND,
            "finmind_taiex": 100.0,
        }))
        self.assertIn("來源異常", bd.market_source_text({
            "canonical_source": fd.MARKET_SOURCE_CONFLICT,
            "finmind_taiex": 101.0,
        }))

    def test_strategy_status_card_shows_evidence_state_not_judgement(self):
        """頁尾折疊「策略狀態」:只放證據狀態與結構事實,不得放個別因子判斷。

        儀表板原本只傳達「透明可追溯」,沒有傳達「這套規則有多可信」——分層看起來很確定,
        但預測力還在累積樣本外證據。這張卡補上那一軸;同時它不可以變成把 in-sample 的
        IC 結論公開宣告的地方。
        """
        self.assertIn("function buildStrategyStatus()", self.template)
        self.assertIn("buildStrategyStatus()", self.template)
        self.assertIn("id:'strategy-status'", self.template)
        self.assertIn("h('details',{class:'card strategy-disclosure',id:'strategy-status'}", self.template)
        self.assertIn("document.getElementById('trust').append(buildStrategyStatus())", self.template)
        # 四項事實都要在
        for key in ("權重校準窗", "樣本外驗證", "訊號集中度", "分層穩定度"):
            self.assertIn(key, self.template, f"策略狀態卡缺「{key}」")
        # 校準窗與成熟門檻不得寫死:IS_CUTOFF 由 validate 取、前瞻窗由 signal_structure 取
        self.assertIn("from validate import IS_CUTOFF", self.builder)
        self.assertNotIn(validate.IS_CUTOFF, self.template,
                         "IS_CUTOFF 不可寫死在模板——改權重時會忘記同步")
        self.assertIn("sig.EVAL_HORIZON_DAYS", self.builder)
        # 績效數字不可複製到儀表板,只能連向週報(避免與 validate.py §② 各算一份而漂移)。
        # 卡片可以「提到」超額/勝率並指路,但 builder 必須連算不出來:禁止在此碰前瞻報酬。
        src = self._builder_strategy_source()
        # 與週報共用 daily_metrics 的交易日 spine 是成熟度所需，不能誤禁日期查詢。
        for banned in ("close_adj", "spearman", "SELECT * FROM daily_metrics"):
            self.assertNotIn(banned, src,
                             f"build_strategy_status 不得計算績效({banned})——只放證據狀態與結構")
        self.assertIn("report_url", self.builder)
        self.assertIn("report_tier_url", self.builder)
        # §② 的錨點必須是掃出來的行號,不可寫死(報告每週重生,行號會變)
        self.assertIn('startswith("## ②")', src)
        self.assertNotIn("#L", self.template.split("function buildStrategyStatus()")[0][-4000:])
        # 守護語:必須明說這些是事實而非判斷,且分層不是買賣指示
        card = self._strategy_card_source()
        self.assertIn("不是對個別因子有效性的判斷", card)
        self.assertIn("不是買賣指示", card)
        self.assertIn("觀察名單", card)

    def test_strategy_payload_float_is_stable_across_python_minor_versions(self):
        """3.11/3.12 可能只差約 1e-15；公開靜態頁不得因此產生不同 blob。"""
        old = 2.815964541124785
        new = 2.8159645411247847
        self.assertNotEqual(old, new, "測例必須真的包含兩個不同 binary float")
        self.assertEqual(bd._stable_payload_float(old),
                         bd._stable_payload_float(new))
        self.assertEqual(bd._stable_payload_float(old), 2.815964541125)
        self.assertEqual(bd._stable_payload_float(-0.0), 0.0,
                         "JSON 不應因負零再產生無意義的跨版本差異")

    def _strategy_card_source(self):
        """取出模板裡 buildStrategyStatus 的函式本體,避免斷言誤中頁面其他區塊。"""
        start = self.template.index("function buildStrategyStatus()")
        end = self.template.index("\nfunction ", start + 10)
        return self.template[start:end]

    def _builder_strategy_source(self):
        """取出 build_dashboard.build_strategy_status 的函式本體。"""
        start = self.builder.index("def build_strategy_status(")
        end = self.builder.index("\ndef ", start + 10)
        return self.builder[start:end]

    def test_tier_section_warns_that_layers_turn_over(self):
        """個股分層區必須提醒名單會頻繁變動(中位停留 4~5 日),並連到策略狀態。"""
        self.assertIn("各層停留天數不長", self.template)
        self.assertIn("STRATEGY.dwell", self.template)
        self.assertIn("#strategy-status", self.template)
        # 首屏概況標題要標明是相對分層,不可讓「11 強勢」讀成絕對強弱
        self.assertIn("今日分層概況（相對分層）", self.template)

    def test_divergence_section_is_描述_not_signal(self):
        """兩視角分歧是**描述**,不是買賣訊號。它有沒有預測力正由 H1 檢定中(§⑪),
        所以畫面必須(a)明說不是訊號、(b)指向 H1、(c)不裸讀單日 ρ、
        (d)用平均秩而非排序切片——後者在整數分數上會平手,結果隨資料順序而變。"""
        self.assertIn("function buildDiverge()", self.template)
        sec = self._diverge_source()
        self.assertIn("不是買賣訊號", sec)
        self.assertIn("H1", sec)
        self.assertIn("平均秩", sec, "必須說明百分位用平均秩(與資料順序無關)")
        # 單日 ρ 必須附歷史脈絡
        for ctx in ("百分位", "近 5 日", "標準差"):
            self.assertIn(ctx, sec, f"單日 ρ 必須附「{ctx}」等脈絡,不可裸讀")
        # 籌碼定義必須就是 H1 檢定的那一個,不可另立一份
        b = self.builder
        self.assertIn("hyp.CHIP_WEIGHTS", b,
                      "畫面顯示的籌碼分數必須與 H1 檢定的定義相同")
        # 靜默失敗防護:資料層以外的錯誤不得被吞掉
        self.assertIn("except sqlite3.Error:", b)
        i = b.index("def build_divergence(")
        body = b[i:b.index("\ndef ", i + 10)]
        self.assertNotIn("except Exception:", body,
                         "build_divergence 不得用 bare except 吞掉程式錯誤")

    def _diverge_source(self):
        start = self.template.index("function buildDiverge()")
        # 往前含註解區塊,往後到下一個函式
        head = self.template.rindex("/*", 0, start)
        return self.template[head:self.template.index("\nfunction ", start + 10)]

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
        for marker in ("role:'tablist'", "grp-tab-board", "selectView(key)",
                       "① 動能排序 · 族群排行榜"):
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
        # 族群明細先回答「為什麼領先／有人接」：五項指標在成分股導覽之前；
        # 手機首屏不能被一整組成分股按鈕占滿。成分股仍保留在同一面板下方。
        group_sheet = self.template[self.template.index("function openGroupSheet"):
                                    self.template.index("// 分層 pill 用")]
        self.assertIn("text:'族群五項指標'}),statList,memberLinks];", group_sheet)
        self.assertNotIn("text:g.note}),memberLinks", group_sheet)
        # 狀態摘要不能把「持續時間」與三類成分股籌碼狀態縮成無單位數字；
        # 手機沒有 hover，必須直接看出幾檔個股屬於各狀態。
        self.assertIn("text:'目前狀態'+g.dur", group_sheet)
        self.assertIn("text:'籌碼健康 '+g.chip.health+' 檔'", group_sheet)
        self.assertIn("text:'中性 '+g.chip.neutral+' 檔'", group_sheet)
        self.assertIn("text:'待觀察 '+g.chip.warn+' 檔'", group_sheet)
        self.assertIn('gobj["dur"] = f"已持續 {n} 個交易日(自 {since})"', self.builder)
        # 成分股導覽不能只列名字：使用者在族群明細內就要能分辨誰值得先看，
        # 且相對綜合分必須與 20 日絕對報酬並列，避免把相對強誤讀成絕對上漲。
        for marker in ("class:'group-member-grid'", "group-member-btn", "group-member-rank",
                       "text:'綜合'", "text:'20日'", "fmtPct(s.r20,1)",
                       "按鈕列出排序、綜合分與20日絕對報酬"):
            self.assertIn(marker, group_sheet)

    def test_tier_bands_and_five_day_flow(self):
        for marker in ("function buildTier()", "flowSpark", "近 5 日變層軌跡",
                       "D.tierFlow", "蓄勢候補", "不是買賣指示"):
            self.assertIn(marker, self.template)
        for marker in ("class:'tier-snapshot'", "id:idx===0?'tier-primary-list':null", "相對強勢", "相對蓄勢", "相對弱勢",
                       "class:'tier-full'", "完整八層、族群篩選與近 5 日變層軌跡"):
            self.assertIn(marker, self.template)
        # 主要分層 pill 直接標出兩個數值的口徑，避免把綜合分與 20 日絕對報酬混在一起
        for marker in ("function tierPillMetric", "tierPillMetric('綜合'", "tierPillMetric('20日'",
                       "tier-snapshot-legend", "五面向骨架｜綜合分｜20日絕對報酬"):
            self.assertIn(marker, self.template)
        # 分層區可依族群篩選(選定=全列)、全部模式「＋N 檔」可展開、chip/變層列點開明細
        for marker in ("'aria-label':'分層篩選族群'", "檔 展開",
                       "onclick:()=>{expanded[k]=true;renderBands();}"):
            self.assertIn(marker, self.template)
        # 檔數不得寫死——用 D.allStocks.length 動態帶入
        self.assertIn("${D.allStocks.length}", self.template)
        self.assertNotIn("把全 121 檔", self.template)

    # ---------- 首屏直接查個股 ----------

    def test_first_screen_has_direct_stock_lookup(self):
        for marker in ("function buildHeroLookup()", "function stockLookupMatches(",
                       "role:'combobox'", "'aria-autocomplete':'list'",
                       "role:'listbox'", "hero-stock-lookup", "快速查個股"):
            self.assertIn(marker, self.template)
        self.assertIn("stockLookupMatches(D.allStocks,q)", self.template)
        self.assertIn("placeholder:'輸入股號或名稱，例如 3443'", self.template)
        self.assertIn("openStockDetail(stock.id,null,null,input)", self.template)
        overview = self.template[self.template.index("function buildOverview()"):
                                 self.template.index("function buildStrategyStatus()")]
        self.assertIn("buildHeroLookup()", overview)
        self.assertLess(overview.index("buildHeroLookup()"), overview.index("class:'command-foot'"))

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
        # 多視角詳情的五張視角卡會重 render；鍵盤切換後焦點要搬到新卡，不可落回 BODY。
        for marker in ("'data-rv-lens':key", "onclick:event=>onFocus(key,event.currentTarget)",
                       "function setFocus(key,source)", "source.classList.contains('rv-score-card')",
                       "replacement.focus({preventScroll:true})"):
            self.assertIn(marker, self.template)

    # ---------- 個股詳情:七因子 + null 防護 ----------

    def test_stock_detail_has_seven_factor_profile_with_null_guards(self):
        for marker in ("function buildDetail(", "七因子拆解", "diverg(f.score,2",
                       "(d.tech||{}).chart", "d.note&&h(",
                       "if(d.note)card.appendChild(researchEntry(d));"):
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

    def test_stock_detail_has_weekly_rank_change_with_summary_then_details(self):
        fn = self.template[self.template.index("function rankChangeSection(d)"):
                           self.template.index("function buildDetail(")]
        detail = self.template[self.template.index("function buildDetail("):]
        self.assertIn("rankChangeSection(d)", detail[:detail.index("d.note&&")])
        self.assertIn("(RANKCHG.stocks||{})[d.id]", fn)          # 依目前股票取資料,不綁定單一代號
        self.assertNotIn("3443", fn)
        self.assertIn("'本週排名變化'", fn)
        self.assertIn("h('ul',{class:'rkc-sum'},...x.summary", fn)
        # 排名依據與當日分數在收合摘要可比較；明細保留同業、窗口與因子分解。
        self.assertLess(fn.index("'),scores,drivers,"), fn.index("h('details'"))
        self.assertIn("text:'排名依據｜三日平滑分數'", fn)
        self.assertIn("text:'因子拆解｜當日綜合分數'", fn)
        self.assertIn("當日分數主要拖累", fn)
        self.assertIn("當日分數主要推升", fn)
        self.assertIn(".sort((a,b)=>Math.abs(b.contrib)-Math.abs(a.contrib)).slice(0,2)", fn)
        self.assertIn("scores,drivers,", fn)
        self.assertIn("括號為分數差額，不是名次變動", fn)
        self.assertIn("h('details',{},h('summary',{text:'看明細：同業名次、兩週分數與日期'}),", fn)
        self.assertIn("...(x.rankDetail||[]).map(t=>h('p',{text:t}))),peers,smooth,daily,meta)", fn)
        self.assertIn("'當日綜合分數變動（composite", fn)
        self.assertIn("'三日平滑分數變動（composite_s；名次只依這個分數）'", fn)
        self.assertIn("line('上週 → 本週（差額）',dl.line)", fn)
        self.assertIn("line('上週 → 本週（差額）',sm.line)", fn)
        self.assertIn("text:x.posA+' → '+x.posB", fn)
        self.assertNotIn("x.rankA+'/'", fn)
        self.assertIn("if(!RANKCHG)return null", fn)
        self.assertIn("RANKCHG.error", fn)
        self.assertIn("x.available", fn)
        self.assertIn(".rkc details>summary{cursor:pointer;display:flex;align-items:center;min-height:44px", self.template)
        self.assertIn(".rkc-row.rkc-peer{grid-template-columns:1fr", self.template)
        self.assertIn("rank_change.dashboard_payload(", self.builder)
        self.assertIn('"--rank-change"', self.builder)

    def test_mobile_layout_collapses_grids_and_meets_touch_targets(self):
        for marker in ("@media (max-width:720px)", "min-height:44px",
                       ".srow{grid-template-columns:1fr", ".shead{display:none}",
                       ".bhead{display:none}", ".hscroll{overflow-x:auto}"):
            self.assertIn(marker, self.template)
        # 族群排行榜在手機藏起欄位表頭後,每個數值仍要自帶維度標籤(與熱圖 cell label 同一模式)。
        for marker in (".board-metric-label{display:none}",
                       ".board-metric-label{display:inline",
                       ".board-metric-label{flex-basis:100%}",
                       "metricCell(mom,fmtPct(mom,1),pctCol(mom),md,25,'動能 vs 全體')",
                       "dd,3,'修正日外資'"):
            self.assertIn(marker, self.template)
        # 多視角主分頁與詳情都標示五個位置，手機不得把任何一個藏進橫向捲軸；兩列排列仍維持原文字標籤。
        for marker in (".rv-lens-tabs{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));overflow:hidden}",
                       ".rv-lens-tab:nth-child(4){grid-column:2/span 2}",
                       ".rv-lens-tab:nth-child(5){grid-column:4/span 2}",
                       ".rv-score-grid{grid-template-columns:repeat(6,minmax(0,1fr));overflow:hidden}",
                       ".rv-score-card:nth-child(4){grid-column:2/span 2}",
                       ".rv-score-card:nth-child(5){grid-column:4/span 2}",
                       ".rv-score-card span:not(.material-symbols-rounded){white-space:normal;line-height:1.25}",
                       ".rv-detail-action{min-width:44px;min-height:44px",
                       ".rv-group-select{min-height:44px}"):
            self.assertIn(marker, self.template)
        for marker in ("const moveTabFocus=(key,event)=>",
                       "ArrowLeft:-1,ArrowUp:-1,ArrowRight:1,ArrowDown:1",
                       "else if(event.key==='Home')nextIndex=0",
                       "else if(event.key==='End')nextIndex=RV_KEYS.length-1",
                       "onkeydown:event=>moveTabFocus(key,event)"):
            self.assertIn(marker, self.template)
        # 手機列表沒有欄位表頭；百分位方向與同儕敏感口徑要在進入列前可讀，row 內也要保留維度標籤。
        for marker in ("class:'rv-table-note'",
                       "百分位越高代表在本族群中相對靠前",
                       "「同儕敏感」是移除單一同族群成分股後",
                       ".rv-sensitivity-label{display:none",
                       ".rv-sensitivity-label{display:inline}",
                       "class:'rv-sensitivity-label',text:'同儕敏感'",
                       "title:'移除單一同族群成分股後，排名所屬五分位組別改變的情境比例'"):
            self.assertIn(marker, self.template)
        self.assertNotIn(".rv-score-grid{grid-template-columns:repeat(5,86px);overflow-x:auto}", self.template)
        # 桌機鎖寬已移除,窄視口不得水平溢位；詳情抽屜在窄屏也要把寬度留給圖表，
        # 不可讓 sheet/card/chart 三層寬鬆 padding 把 SVG 壓到 200px 左右。
        self.assertNotIn("min-width:1180px", self.template)
        for marker in (".stock-detail-card{padding:30px 32px}",
                       ".history-chart-card{padding:20px 22px}",
                       "#sheet{width:100%;height:auto;max-height:86vh;border-left:none;border-radius:18px 18px 0 0;transform:translateY(100%);padding:18px 12px 32px}",
                       ".stock-detail-card{padding:20px 16px}",
                       ".history-chart-card{padding:16px 12px}",
                       ".chart-canvas{padding:10px 6px 4px}",
                       ".chart-range-btn,.chart-chip-btn{min-height:44px}"):
            self.assertIn(marker, self.template)
        # 圖表日期可點選後，區間與指標仍是行動版必要控制；不得留在 26–32px 的桌機滑鼠尺寸。
        self.assertIn("class:'chart-range-btn'", self.template)
        self.assertIn("class:'chart-chip-btn'", self.template)

    # ---------- 抽屜:focus 管理 ----------

    def test_sheet_manages_focus_and_escape(self):
        for marker in ("lastSheetFocus=opener||document.activeElement",
                       "if(c) c.focus()",
                       "opener.focus({preventScroll:true})",
                       "if(e.key==='Escape'){e.preventDefault();closeSheet();return;}",
                       "sheetEl.querySelectorAll('a[href],button:not([disabled])",
                       "item.el.inert=true",
                       "item.el.inert=false",
                       "sheetwrap.setAttribute('aria-hidden','false')",
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
        # 字級走 --fs-* token(手機斷點統一抬高下限),這裡釘的是「有數值文字」而非某個 px
        self.assertIn("h('span',{class:'mono',style:'font-size:var(--fs-105);color:var(--muted)'}, val)",
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
        self.assertEqual(validate.IS_CUTOFF, score.SCORE_EFFECTIVE_FROM)

    # ---------- 台積電法說:搬到研究中心，族群指引與觀察層鐵律保留 ----------

    def test_tsmc_event_moved_to_research_center_without_entering_scores(self):
        self.assertNotIn('href="#tsmc"', self.template)
        self.assertNotIn('<section id="tsmc"', self.template)
        self.assertNotIn("document.getElementById('tsmc')", self.template)
        self.assertNotIn("function buildTSMC", self.template)
        self.assertNotIn("TSMC=__TSMC_JSON__", self.template)
        self.assertNotIn('html.replace("__TSMC_JSON__"', self.builder)
        self.assertIn("load_events", self.builder)
        self.assertIn('"eventKind": "tsmc_earnings"', self.builder)
        self.assertIn('"type": "topic", "typeLabel": "市場議題"', self.builder)
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

    # ---------- 研究內容移往獨立頁；首頁個股面板只留入口 ----------

    def test_research_entry_links_to_formal_note_and_narrative(self):
        for marker in ("function researchEntry(d)", "閱讀正式筆記",
                       "閱讀多空小作文", "RESEARCH_BASE", "全文閱讀已移到研究中心"):
            self.assertIn(marker, self.template)
        self.assertNotIn("function researchTabs(d)", self.template)
        # 首頁 payload 不再重複塞入兩套長文 sections，避免 5MB 首頁繼續膨脹。
        note_payload = self.builder[self.builder.index('obj["note"]'):self.builder.index(
            'hypothesis = hypotheses_map.get', self.builder.index('obj["note"]'))]
        hypothesis_payload = self.builder[self.builder.index('obj["hypothesis"]'):self.builder.index(
            'obj["_comp"]', self.builder.index('obj["hypothesis"]'))]
        self.assertNotIn('"sections"', note_payload)
        self.assertNotIn('"sections"', hypothesis_payload)
        self.assertIn('"researchUrl"', note_payload)
        self.assertIn('"researchUrl"', hypothesis_payload)
        self.assertNotIn("研究筆記品質", self.template)
        self.assertNotIn("sec30", self.template)
        for marker in ("load_hypothesis_reports", 'obj["hypothesis"]',
                       '"statusCounts"', '"statusInfo"',
                       '"captureModeCounts"', '"lifecycleCounts"', '"dueCount"',
                       '"independentChains"', '"schemaVersion"'):
            self.assertIn(marker, self.builder)


if __name__ == "__main__":
    unittest.main()
