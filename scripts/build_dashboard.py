#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_dashboard.py — 從 SQLite(daily_scores + daily_metrics)自動重生儀表板 HTML。
吃 scripts/dashboard_template.html(CSS/JS 外殼),只注入資料 → index.html,
並把同一份頁面凍結成 archive/<資料日>.html(as-seen 歷史快照,供日期選單回看)。
零第三方依賴。用法:  uv run --no-project python scripts/build_dashboard.py
"""
import json, os, re, sqlite3, sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# 個股層門檻單一事實來源(score.py CONFIG):權重 + 各元素 hint 引用的門檻,調旋鈕文字自動同步
from score import (WEIGHTS, VOLR_ACTIVE, VOLR_DRY, VOL_OVERHEAT, VOLR_OVERHEAT,
                   MARGIN_UTIL_HOT, MARGIN_UTIL_MID, MARGIN_DOWN_BIG, MARGIN_UP_BIG,
                   DZ_FOREIGN, DZ_TRUST, STEALTH_OFF_HIGH, _chip_signal)
# 族群/大盤門檻單一事實來源(fetch_daily 頂部旋鈕),族群卡與市場籤條 tooltip 顯示用
from fetch_daily import REGIME_DD, GS_OFF_HIGH, GS_BREADTH_LOW
# 個股質化筆記的時效與查核品質——單一事實來源在 qual_notes.py
from qual_notes import (load_notes, note_status, note_review_status,
                        TEMPLATE_VERSION as NOTE_TEMPLATE_VERSION)
from leading_hypotheses import (HYPOTHESIS_STATUS_INFO,
                                load_reports as load_hypothesis_reports)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
TEMPLATE = os.path.join(ROOT, "scripts", "dashboard_template.html")
OUT = os.path.join(ROOT, "index.html")   # 根目錄 index.html → GitHub Pages 乾淨網址
# 歷史快照:每日 build 原樣存檔,回看的是「當天使用者看到的報告」而非以現行規則重算
# (daily_scores 等衍生表每日全量重建,事後從 db 重繪會是 restated history,不可稽核)。
ARCHIVE = os.path.join(ROOT, "archive")
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
HYPOTHESES_DIR = os.path.join(ROOT, "notes", "leading_hypotheses")
# 筆記全文放 repo 裡,儀表板不 embed 全文(質化筆記是長文,不適合塞進 tooltip)——
# badge 點開直接連到 GitHub 的 render 版本,讀 repo remote 免寫死也行,但這裡固定
# 域名比較簡單(僅供內部 GitHub Pages 使用,repo 搬家機率低)
NOTE_REPO_BLOB = "https://github.com/DennisLiuCk/strong-weak-scanner/blob/main/"
NOTE_LABEL = {
    "ai_draft": "AI 草稿・未獨立查核",
    "partially_verified": "部分核驗",
    "independently_verified": "已獨立核對來源",
    "conflicted": "來源衝突・待釐清",
}

# 標題設定。TITLE_TAIL 是品牌尾綴、ALL_SCOPE 是「全部族群」時的範圍詞;篩選到單一族群時,
# 前端會把標題換成「族群名 · TITLE_TAIL」(見 dashboard_template.html 的 group filter JS)。
# 刻意不列舉族群、不寫死元素數——加族群或改元素都不必動這裡。PAGE_TITLE(<title>,分頁/SEO/
# 書籤)與 H1_TITLE(<h1>,頁面大標)是兩個獨立旋鈕,預設同字串,要各自演化改對應那行即可。
TITLE_TAIL = "汰弱留強掃描"          # 品牌尾綴;各族群動態標題共用
ALL_SCOPE  = "台股半導體與 AI 供應鏈"  # 「全部族群」時的範圍詞(2026-07-06 起含散熱/PCB,超出純半導體)
PAGE_TITLE = ALL_SCOPE + " · " + TITLE_TAIL   # <title> 預設(全部族群)
H1_TITLE   = ALL_SCOPE + " · " + TITLE_TAIL   # <h1> 預設(全部族群)

# 族群定義以 config/groups.csv → db `groups` 表為準;此處僅為舊 db 的退路預設
GROUP_ORDER = ["passive", "power", "packtest"]
GROUP_NM = {"passive": "被動元件", "power": "功率元件", "packtest": "封測"}
GROUP_TAG = {}
# 結論卡的族群標籤用短名(2~3 字,省空間);未列的族群自動退回全名。加族群時想更短就在這補一筆。
GROUP_SHORT = {"passive": "被動", "power": "功率", "packtest": "封測",
               "memory": "記憶體", "ipdesign": "矽智財", "semiequip": "設備"}
TIER_ORDER = ["真強", "蓄勢·外資佈局", "強但過熱", "潛在/中性", "真弱", "真弱·陷阱"]
TIER_VT = {"真強": 2, "蓄勢·外資佈局": 2, "強但過熱": 1, "潛在/中性": 0, "真弱": -2, "真弱·陷阱": -2}
TIER_COL = {"真強": "var(--strong)", "蓄勢·外資佈局": "var(--neutral)", "強但過熱": "var(--warn-line)",
            "潛在/中性": "var(--neutral)", "真弱": "var(--weak)", "真弱·陷阱": "var(--weak)"}
# DB tier key 是策略與 OOS 稽核契約,不可因 UI 改名而變動；畫面另用安全標籤，避免把
# 「族群內相對位置」誤讀成絕對買賣或保證強弱。
TIER_UI_LABEL = {
    "真強": "相對強勢",
    "蓄勢·外資佈局": "相對蓄勢",
    "強但過熱": "相對強勢·過熱",
    "潛在/中性": "中性觀察",
    "真弱": "相對弱勢",
    "真弱·陷阱": "相對弱勢·槓桿風險",
}
TIER_DESC = {
    "真強": "價格與籌碼指標多位於族群相對前段",
    "蓄勢·外資佈局": "籌碼指標相對位置靠前,價格尚未發動",
    "強但過熱": "價格相對靠前,但出現量能或融資過熱警示",
    "潛在/中性": "各指標相對位置分歧,持續觀察",
    "真弱": "價格與綜合指標位於族群相對後段",
    "真弱·陷阱": "外資相對位置靠後,且融資條件偏弱",
}

def pct(x, signed=False):
    """給『分數/比率』欄位(dist_hi、ret1、margin_chg):× 100 轉百分比。"""
    if x is None:
        return "-"
    return f"{x*100:+.1f}%" if signed else f"{x*100:.1f}%"


def pctp(x):
    """給『本身已是百分比』的欄位(turnover_pct / margin_util_pct):不再 × 100。"""
    return "-" if x is None else f"{x:.1f}%"

# 每個元素:score → 理由文字
R_PRICE = {2: "20日相對報酬位於族群前20%", 1: "20日相對報酬位於族群前20–40%",
           0: "20日相對報酬位於族群中段", -1: "20日相對報酬位於族群後20–40%",
           -2: "20日相對報酬位於族群後20%"}
R_RESIL = {2: "修正日抗跌程度位於族群前20%", -2: "修正日抗跌程度位於族群後20%"}
R_FOREIGN = {2: "外資變化位於族群前20%", 1: "外資變化位於族群前20–40%",
             0: "外資變化位於族群中段或雜訊區", -1: "外資變化位於族群後20–40%",
             -2: "外資變化位於族群後20%"}
R_TRUST = {2: "投信變化位於族群前20%", 1: "投信變化位於族群前20–40%",
           0: "投信變化位於族群中段或雜訊區", -1: "投信變化位於族群後20–40%",
           -2: "投信變化位於族群後20%"}
R_MARGIN = {2: "融資條件落在健康區", 1: "融資條件偏健康",
            0: "融資變化未觸發門檻", -1: "融資條件偏擁擠",
            -2: "融資增加幅度觸及高風險門檻"}
R_DIP = {2: "修正日買賣位於族群前20%", -2: "修正日買賣位於族群後20%"}
# 精簡標籤(給 vsub 用)
SALIENT = {("price", 2): "價格相對前段", ("price", -2): "價格相對後段",
           ("foreign", 2): "外資變化相對前段", ("foreign", -2): "外資變化相對後段",
           ("trust", 2): "投信變化相對前段", ("trust", -2): "投信變化相對後段",
           ("margin", 2): "融資條件偏健康", ("margin", -2): "融資槓桿風險偏高",
           ("dip", 2): "修正日買賣相對前段", ("dip", -2): "修正日買賣相對後段",
           ("resil", 2): "修正抗跌相對前段", ("resil", -2): "修正抗跌相對後段"}


def _relative_bucket(score):
    """排名分數的白話區間；0 也可能由死區強制歸零，故不可只寫「中間40%」。"""
    return {2: "族群前20%", 1: "族群前20–40%", 0: "族群中段或雜訊區",
            -1: "族群後20–40%", -2: "族群後20%"}.get(score, "族群相對位置未知")


def _cell(score, value, rows, reading, current, basis, warn=False, gfx=None):
    """固定 cell payload: [score,value,rows,reading,warn,current,basis,gfx]。

    current 是未經排名的當下方向；basis 才說明分數來自排名桶或固定門檻。兩者刻意分開，
    例如外資仍減持也可能因同業減持更多而落在族群前20%。
    gfx 是門檻制欄位(②量比/⑤融資水位)畫量尺用的原始數值;排名制欄位為 None
    (五分位條只需要分數本身)。
    """
    return [score, value, rows, reading, int(bool(warn)), current, basis, gfx]


def _value(row, key, default=None):
    """sqlite3.Row 與測試 dict 共用的安全取值。"""
    try:
        return row[key]
    except (KeyError, IndexError, TypeError):
        return default


def _fmt_price(x):
    if x is None:
        return "-"
    return f"{x:,.2f}".rstrip("0").rstrip(".")


def _fmt_volume(x):
    return "-" if x is None else f"{int(round(x)):,} 股"


def _fmt_lots(v):
    """張數帶正負號;0 不帶(避免顯示成「+0張」)。"""
    return f"{v:+,}張" if v else "0張"


def _ratio(a, b):
    return (a / b - 1) if (a is not None and b) else None


def _ma_price_position(close, ma_values):
    """白話列出現價相對三條均線的位置；不只拿 MA20 代表全部週期。"""
    above = [label for label, value in ma_values if close > value]
    below = [label for label, value in ma_values if close < value]
    equal = [label for label, value in ma_values if close == value]
    if len(above) == len(ma_values):
        return "現價高於MA5、MA20、MA60"
    if len(below) == len(ma_values):
        return "現價低於MA5、MA20、MA60"
    parts = []
    if above:
        parts.append("現價高於" + "、".join(above))
    if below:
        parts.append("低於" + "、".join(below))
    if equal:
        parts.append("約等於" + "、".join(equal))
    return "；".join(parts)


def _ma_distance_phrase(label, distance):
    if distance is None:
        return f"{label}距離資料不足"
    if distance > 0:
        return f"比{label}高{abs(distance)*100:.1f}%"
    if distance < 0:
        return f"比{label}低{abs(distance)*100:.1f}%"
    return f"約等於{label}"


def build_technical_view(m, history=None):
    """個股相對自身歷史的技術面觀察，不做族群排名、不影響分數或 tier。"""
    close = _value(m, "close_adj")
    ma5, ma20, ma60 = (_value(m, "ma5"), _value(m, "ma20"), _value(m, "ma60"))
    rsi = _value(m, "rsi14")
    volume, vma20, vr20 = (_value(m, "volume"), _value(m, "vol_ma20"),
                           _value(m, "vol_ratio20"))
    if any(v is None for v in (close, ma5, ma20, ma60, rsi)):
        return None

    series = list(history or [])
    current_date = _value(m, "date")
    if not series or (current_date and _value(series[-1], "date") != current_date):
        series.append(m)
    if current_date:
        series = [x for x in series if (_value(x, "date") or "") <= current_date]
    series.sort(key=lambda x: _value(x, "date", ""))
    prev = series[-2] if len(series) >= 2 else None
    five = series[-6] if len(series) >= 6 else None

    d5, d20, d60 = _ratio(close, ma5), _ratio(close, ma20), _ratio(close, ma60)
    ma_values = [("MA5", ma5), ("MA20", ma20), ("MA60", ma60)]
    price_position = _ma_price_position(close, ma_values)
    bull = ma5 > ma20 > ma60
    bear = ma5 < ma20 < ma60
    if bull:
        cls, label, structure = "up", "多頭排列", "MA5 > MA20 > MA60"
        structure_note = ("短、中、長期均線依序向上排列；" + price_position +
                          "。排列描述均線關係，不保證後續上漲")
    elif bear:
        cls, label, structure = "down", "空頭排列", "MA5 < MA20 < MA60"
        structure_note = ("短、中、長期均線依序向下排列；" + price_position +
                          "。排列描述均線關係，不代表已無反彈可能")
    elif close > ma20 and rsi >= 50:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "up", "趨勢偏多"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線尚未形成標準多頭排列（MA5 > MA20 > MA60）；" +
                          price_position + "，價格位置偏強")
    elif close < ma20 and rsi < 50:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "down", "趨勢偏弱"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線尚未形成標準空頭排列（MA5 < MA20 < MA60）；" +
                          price_position + "，價格位置偏弱")
    else:
        ordered = sorted(ma_values, key=lambda x: x[1], reverse=True)
        cls, label = "flat", "結構分歧"
        structure = "由高到低：" + " > ".join(x[0] for x in ordered)
        structure_note = ("均線與現價尚未形成一致方向；" + price_position +
                          "。不同週期訊號互相矛盾，單看一項指標容易誤判")

    if rsi >= 70:
        rsi_state = "上漲力道明顯較強"
        rsi_note = ("過去14個交易日的平均上漲力道明顯大於平均下跌力道；RSI≥70屬高檔區，"
                    "代表追價風險提高，但強趨勢中也可能維持高檔，不等於即將反轉")
    elif rsi <= 30:
        rsi_state = "下跌力道明顯較強"
        rsi_note = ("過去14個交易日的平均下跌力道明顯大於平均上漲力道；RSI≤30屬低檔區，"
                    "可能出現反彈，但不等於已經止跌")
    elif rsi >= 50:
        rsi_state = "上漲力道較強"
        rsi_note = ("過去14個交易日的平均上漲力道大於平均下跌力道；50是兩者的分界，"
                    "只描述近期力道，不代表股價一定續漲")
    else:
        rsi_state = "下跌力道較強"
        rsi_note = ("過去14個交易日的平均下跌力道大於平均上漲力道；50是兩者的分界，"
                    "只描述近期力道，不代表股價一定續跌")
    rsi5 = _value(five, "rsi14") if five else None
    rsi_delta = (rsi - rsi5) if rsi5 is not None else None
    rsi_display = f"{rsi:.1f} · {rsi_state}"
    if rsi_delta is not None:
        rsi_display += f"（較5日前 {rsi_delta:+.1f}）"

    ret1 = _value(m, "ret1")
    vol_state = ("量增" if vr20 is not None and vr20 >= 1.2 else
                 "量縮" if vr20 is not None and vr20 <= 0.8 else "量近平均")
    price_state = "價漲" if ret1 is not None and ret1 > 0 else "價跌" if ret1 is not None and ret1 < 0 else "價平"
    pv = price_state + vol_state
    pv_notes = {
        "價漲量增": "上漲伴隨高於20日均量的成交參與，價量方向互相確認",
        "價漲量縮": "價格上漲，但成交參與低於20日均量，延續力仍需後續量能確認",
        "價跌量增": "下跌伴隨高於20日均量的成交參與，短線賣壓較明顯",
        "價跌量縮": "價格下跌但成交參與有限，屬縮量整理或賣壓暫未擴大",
        "價平量增": "價格變化不大但成交活躍，可能處於換手，方向尚未表態",
        "價平量縮": "價格與成交都收斂，市場暫時觀望",
    }
    pv_note = pv_notes.get(pv, f"成交量約為20日均量的 {vr20:.2f}×，尚未出現明顯量增或量縮" if vr20 is not None else "量能樣本不足")

    events = []
    if prev:
        pc, pm20 = _value(prev, "close_adj"), _value(prev, "ma20")
        pm5 = _value(prev, "ma5")
        if None not in (pc, pm20):
            if pc <= pm20 and close > ma20:
                events.append("現價上穿MA20")
            elif pc >= pm20 and close < ma20:
                events.append("現價跌破MA20")
        if None not in (pm5, pm20):
            if pm5 <= pm20 and ma5 > ma20:
                events.append("MA5上穿MA20")
            elif pm5 >= pm20 and ma5 < ma20:
                events.append("MA5跌破MA20")
    if events:
        event_text = "、".join(events)
        event_note = "與前一交易日比較，發生上述跨越事件"
    elif prev:
        event_text = "無穿越事件"
        event_note = "與前一交易日比較：現價沒有跨越MA20，MA5也沒有跨越MA20"
    else:
        event_text = "穿越資料不足"
        event_note = "至少需要目前與前一個交易日的均線資料，才能判斷是否發生跨越"

    ma5_delta = _ratio(ma5, _value(five, "ma5")) if five else None
    ma20_delta = _ratio(ma20, _value(five, "ma20")) if five else None
    slope_text = (f"MA5較5日前 {pct(ma5_delta, True)}；MA20 {pct(ma20_delta, True)}"
                  if ma5_delta is not None and ma20_delta is not None else "均線5日變化樣本不足")
    distances = "、".join((_ma_distance_phrase("MA5", d5),
                            _ma_distance_phrase("MA20", d20),
                            _ma_distance_phrase("MA60", d60)))
    extension = ("其中與MA20的差距超過10%，代表現價和近20日平均價格距離較大；"
                 "不代表一定反彈或續跌" if d20 is not None and abs(d20) >= 0.10 else
                 f"與MA20的差距為{abs(d20)*100:.1f}%，仍在±10%觀察帶內"
                 if d20 is not None else "MA20距離資料不足")

    # 20日還原價+MA20 強調式小圖原料:主色=價、灰=MA20。刻意不畫三色均線——
    # MA20藍/MA60紫在綠色弱視下 ΔE 僅 6.2(驗證器實測不合格),圖走「一主一情境」,
    # MA5/MA60 資訊留在文字列。缺值日剔除、成對對齊,不足2點不出圖。
    chart_rows = [x for x in series[-20:]
                  if _value(x, "close_adj") is not None and _value(x, "ma20") is not None]
    chart = ({"px": [round(_value(x, "close_adj"), 2) for x in chart_rows],
              "ma": [round(_value(x, "ma20"), 2) for x in chart_rows]}
             if len(chart_rows) >= 2 else None)

    rows = [
        ["價格與均線",
         "／".join((f"現價 {_fmt_price(close)}", f"MA5 {_fmt_price(ma5)}",
                   f"MA20 {_fmt_price(ma20)}", f"MA60 {_fmt_price(ma60)}")),
         f"{price_position}：{distances}。{extension}"],
        ["均線結構", structure, structure_note],
        ["RSI14", rsi_display, rsi_note + "；括號是RSI較5個交易日前的增減，不是股價報酬率"],
        ["成交量 / 20日均量",
         f"{_fmt_volume(volume)} / {_fmt_volume(vma20)}" + (f"（{vr20:.2f}×）" if vr20 is not None else ""),
         "VOL以股數計；vol_ratio20=當日成交量÷20日平均成交量，≥1.2×視為量增、≤0.8×視為量縮"],
        ["今日價量關係", pv, pv_note],
        ["短線轉折（較前一交易日）", event_text, event_note + "；" + slope_text],
    ]
    why = f"{structure_note}；{rsi_note}；{pv_note}。"
    return {"cls": cls, "label": label, "rows": rows, "why": why,
            "chart": chart, "rsi": round(rsi, 1),
            "vr20": round(vr20, 2) if vr20 is not None else None,
            "series": [
                {"label": "現價", "value": _fmt_price(close), "cls": "price"},
                {"label": "MA5", "value": _fmt_price(ma5), "cls": "ma5"},
                {"label": "MA20", "value": _fmt_price(ma20), "cls": "ma20"},
                {"label": "MA60", "value": _fmt_price(ma60), "cls": "ma60"},
            ]}


def build_cells(sc, m, mkt20=None):
    """每格:[分數,格值,rows,相對判讀,過熱旗標,原始方向,計分依據]。

    原始方向與相對判讀不得合併：排名分數只表示「跟同族群相比」，不保證原始值為正。
    mkt20 = 大盤(報酬指數)20日報酬,全 universe 共用,僅供①價 tooltip 當基準線。"""
    cells = []
    # ① 價(族群內相對強弱;距高做輔助資訊)
    # 族群中位由定義還原(rs20 = ret20 − 族群中位),不必回 db 重算
    rs = m["rs20"]
    gmed = (m["ret20"] - rs) if (m["ret20"] is not None and rs is not None) else None
    rs_dyn = ("" if rs is None else
              (";目前=贏過至少一半同業" if rs > 0 else ";目前=輸給一半以上同業" if rs < 0 else ""))
    dist = m["dist_hi60"]
    dist_dyn = ("" if dist is None else
                (f";目前≤{STEALTH_OFF_HIGH*100:.0f}%=「價未動」(蓄勢條件之一)"
                 if dist <= STEALTH_OFF_HIGH else ";目前=接近波段高"))
    dr = m["down_rs20"]
    dr_dyn = ("" if dr is None else
              (";目前=修正日相對撐得住" if dr > 0 else ";目前=修正日跌得比同業重" if dr < 0 else ""))
    rows = [["20日報酬 − 族群中位", pct(rs, True),
             f"過去一個月跑贏同業多少——下面兩列相減;①價的分數就是此值的族群內排名{rs_dyn}"],
            ["└ 個股20日還原報酬", pct(m["ret20"], True)],
            ["└ 族群中位20日報酬", pct(gmed, True)],
            ["大盤20日(報酬指數,參考)", pct(mkt20, True),
             "全市場同窗口基準,不計分。個股與族群中位都贏大盤=強族群裡的強;只贏族群中位卻輸大盤=弱勢族群裡的相對強"],
            ["距60日高(還原價)", pct(dist),
             f"現價距近60日高點回落多少,0%=創新高附近{dist_dyn}"],
            ["修正日抗跌(20日)", f"{pct(dr, True)}(抗{sc['s_resil']:+d})",
             "族群下跌日平均比同業多漲(少跌)多少——大家一起跌時撐得住的才是真強"
             f"(獨立元素「抗」,權重{WEIGHTS['resil']},也是升蓄勢的品質門檻){dr_dyn}"],
            ["前一日漲跌", pct(m["ret1"], True)]]
    price_current = ("相對報酬資料不足" if rs is None else
                     f"20日相對報酬 {pct(rs, True)}，目前跑贏族群中位" if rs > 0 else
                     f"20日相對報酬 {pct(rs, True)}，目前跑輸族群中位" if rs < 0 else
                     "20日相對報酬 0.0%，目前與族群中位持平")
    # basis 只留會隨個股變動的排名桶;「分數=族群內排名」的常數語意放明細表欄位表頭
    # (dashboard_template 的 EL.sub),不跟著 98 檔逐格重複
    cells.append(_cell(
        sc["s_price"], pct(rs, True) if rs is not None else "-", rows, R_PRICE[sc["s_price"]],
        price_current, _relative_bucket(sc["s_price"])))
    # ② 量(量比 = 當日周轉率 / 自身60日中位)
    t = m["turnover_pct"]
    vr = m["vol_ratio60"]
    if t is not None and t >= 20:
        rv, warn = "周轉率過高、當沖過熱", 1
    elif vr is not None and vr >= 5:
        rv, warn = "量比爆增、過熱", 1
    elif sc["s_vol"] == 1:
        rv, warn = "量能健康活絡", 0
    elif sc["s_vol"] == -1:
        rv, warn = "量縮、人氣不足", 0
    else:
        rv, warn = "量能中等", 0
    vr_dyn = ("" if vr is None else
              (f";目前≥{VOLR_OVERHEAT:.0f}×=爆量過熱⚠" if vr >= VOLR_OVERHEAT else
               ";目前=健康活絡" if VOLR_ACTIVE[0] <= vr <= VOLR_ACTIVE[1] else
               f";目前<{VOLR_DRY}×=量縮無人氣" if vr < VOLR_DRY else ""))
    rows = [["量比(vs 自身60日中位)", f"{vr:.1f}×" if vr is not None else "樣本不足",
             "當日周轉率÷自己過去60日的常態(中位)——跟自己比,大型股不吃虧;"
             f"{VOLR_ACTIVE[0]}~{VOLR_ACTIVE[1]}×=健康活絡{vr_dyn}"],
            ["當日周轉率", pctp(t),
             f"成交股數佔發行股數%;≥{VOL_OVERHEAT:.0f}%=當沖過熱⚠(壓評級但不改分數)"]]
    vol_current = ("量比資料不足" if vr is None else
                   f"量比 {vr:.1f}×，高於自身60日常態" if vr > 1 else
                   f"量比 {vr:.1f}×，低於自身60日常態" if vr < 1 else
                   "量比 1.0×，與自身60日常態相當")
    # 固定門檻欄的門檻說明是常數(在欄位表頭與 tooltip),格內改放會變動的判讀語
    cells.append(_cell(
        sc["s_vol"], f"{vr:.1f}×" if vr is not None else "-", rows, rv, vol_current,
        rv,
        warn, round(vr, 2) if vr is not None else None))
    # ③ 外資
    fc = m["fpct_chg20"]
    fc_dyn = ("" if fc is None else
              (";目前=增持中" if fc > 0 else ";目前=減持中" if fc < 0 else ""))
    dp = m["dipbuy20"]
    dp_dyn = ("" if dp is None else
              (";目前=下跌日為外資淨買" if dp > 0 else ";目前=下跌日為外資淨賣" if dp < 0 else ""))
    rows = [["外資持股", f"{m['foreign_pct']:.1f}%" if m["foreign_pct"] is not None else "-",
             "外資目前持有比例(水位);看下列「變化」比看水位重要"],
            ["20日持股變化", f"{fc:+.2f}pp" if fc is not None else "-",
             f"近一個月外資增減持了多少百分點——③外資的分數即此值的族群內排名"
             f"(此檔 |變化| < {DZ_FOREIGN}pp 時視為雜訊並歸0分){fc_dyn}"],
            ["修正日買賣(20日)", f"{dp:+.2f}%股本(相對{sc['s_dip']:+d})" if dp is not None else "-",
             "族群下跌日外資買賣的20日累計佔股本%——正值是淨買,負值是淨賣"
             f"(括號分數為族群內排名,只用於蓄勢評級、不計分){dp_dyn}"]]
    # 「目前方向」句的慣例:動詞已帶方向(增持/減持、淨買/淨賣…)時數值用絕對值,
    # 避免「減持 -4.03pp」雙重否定;數據表 rows 是量值欄位,維持帶正負號。
    foreign_current = ("外資持股變化資料不足" if fc is None else
                       f"外資仍增持 {fc:.2f}pp" if fc > 0 else
                       f"外資仍減持 {abs(fc):.2f}pp" if fc < 0 else
                       "外資持股持平 0.00pp")
    cells.append(_cell(
        sc["s_foreign"], f"{fc:+.1f}pp" if fc is not None else "-", rows,
        R_FOREIGN[sc["s_foreign"]], foreign_current,
        _relative_bucket(sc["s_foreign"])))
    # ④ 投信
    t5 = m["trust5"] or 0
    tp = m["trust5_pct"]
    rows = [["近5日淨買賣", _fmt_lots(t5),
             "投信=本土基金；正值代表這5日累計淨買,負值代表累計淨賣"],
            ["佔股本", f"{tp:+.3f}%" if tp is not None else "-",
             f"上值換算佔股本%——④投信的分數即此值的族群內排名(消除股本大小差;"
             f"此檔 |佔股本變化| < {DZ_TRUST}% 時視為雜訊並歸0分)"]]
    if tp is not None:
        trust_current = (f"投信仍淨買 {abs(t5):,}張（{tp:.3f}%股本）" if tp > 0 else
                         f"投信仍淨賣 {abs(t5):,}張（{abs(tp):.3f}%股本）" if tp < 0 else
                         "投信買賣持平 0張（0.000%股本）")
    else:
        trust_current = "投信買賣資料不足"
    cells.append(_cell(
        sc["s_trust"], _fmt_lots(t5), rows, R_TRUST[sc["s_trust"]], trust_current,
        _relative_bucket(sc["s_trust"])))
    # ⑤ 融資券
    u = m["margin_util_pct"]
    u_dyn = ("" if u is None else
             (f";目前≥{MARGIN_UTIL_HOT:.0f}%=觸發過熱門檻⚠(分數封頂−1)" if u >= MARGIN_UTIL_HOT else
              f";目前≥{MARGIN_UTIL_MID:.0f}%=觸發中段水位門檻(分數封頂+1)" if u >= MARGIN_UTIL_MID else
              ";目前低於中段水位門檻"))
    mc10 = _value(m, "margin_chg10")
    mc5 = _value(m, "margin_chg5")
    mc = mc10 if mc10 is not None else mc5
    mc_window = 10 if mc10 is not None else 5 if mc5 is not None else None
    mc_dyn = ("" if mc is None else
              (";目前=融資餘額增加" if mc > 0 else ";目前=融資餘額下降" if mc < 0 else ""))
    rows = [["融資水位(融資/股本)", pctp(u),
             f"融資餘額佔股本%,用來觀察市場槓桿擁擠程度{u_dyn}"],
            [f"{mc_window}日融資變化" if mc_window else "融資變化", pct(mc, True),
             f"融資餘額增加或下降的幅度；與下列價格方向交互給分:價跌且融資下降代表槓桿同步降低,"
             f"價跌且融資明顯增加代表槓桿風險升高；10日缺值時採5日備援{mc_dyn}"],
            ["20日還原價報酬", pct(m["ret20"], True),
             "供上列交互判定的價格方向(與①價的原料同值)"],
            ["券資比", f"{(m['short_margin_ratio'] or 0):.1f}%",
             "融券餘額÷融資餘額;高=空方對作或軋空題材。參考欄位,未計分"]]
    fallback = "（5日備援）" if mc_window == 5 else ""
    margin_current = ("融資變化資料不足" if mc is None else
                      f"融資{mc_window}日仍增加 {pct(mc)}{fallback}" if mc > 0 else
                      f"融資{mc_window}日仍下降 {pct(abs(mc))}{fallback}" if mc < 0 else
                      f"融資{mc_window}日持平 0.0%{fallback}")
    if u is not None:
        margin_current += f"；目前水位 {u:.1f}%"
    cells.append(_cell(
        sc["s_margin"], pctp(u), rows, R_MARGIN[sc["s_margin"]], margin_current,
        R_MARGIN[sc["s_margin"]],
        u is not None and u >= 9, round(u, 2) if u is not None else None))
    return cells


def tier_ui_payload(sc):
    """保留策略 key，另提供不把相對排名說成絕對強弱的 UI label。"""
    confirmed = sc["tier"]
    raw = sc["tier_raw"]
    return {
        "tier_raw": raw,
        "tier_confirmed": confirmed,
        "tier_waiting": raw != confirmed,
        "tier_label": TIER_UI_LABEL.get(confirmed, confirmed),
        "tier_raw_label": TIER_UI_LABEL.get(raw, raw),
    }


def verdict(sc, comp_history=None):
    tier = sc["tier"]
    comp = sc["composite_s"]
    keys = [("price", sc["s_price"]), ("resil", sc["s_resil"]), ("vol", sc["s_vol"]),
            ("foreign", sc["s_foreign"]), ("trust", sc["s_trust"]), ("dip", sc["s_dip"]),
            ("margin", sc["s_margin"])]
    labels = [SALIENT[k] for k in keys if k in SALIENT]
    vsub = " · ".join(labels[:2]) if labels else f"綜合 {comp:+.1f}"
    chip = sc["s_foreign"] >= 2 or sc["s_dip"] >= 2
    if sc["pending"] and tier == "潛在/中性":       # 蓄勢候補(score.py 資料層算好)
        vsub = "◇ " + sc["pending"]
    elif chip and sc["s_resil"] <= -2:              # 衝突組合改方向性敘述,避免讀成自相矛盾
        vsub = "籌碼相對靠前·等抗跌轉正"
    drivers = []
    for name, ref in [("價", "s_price"), ("抗跌", "s_resil"), ("外資", "s_foreign"),
                      ("逆勢", "s_dip"), ("投信", "s_trust"), ("融資", "s_margin")]:
        s = sc[ref]
        if abs(s) >= 2:
            drivers.append({"外資": R_FOREIGN, "逆勢": R_DIP, "投信": R_TRUST,
                            "融資": R_MARGIN, "價": R_PRICE, "抗跌": R_RESIL}[name][s])
    vr = "；".join(drivers) if drivers else "訊號分歧,持續觀察"
    if sc["pending"] and tier == "潛在/中性":
        vr += (f"。◇ {sc['pending']}——籌碼相對位置條件已符；補齊後先成為今日初判,"
               "連2日相同初判才更新已確認層")
    elif chip and sc["s_resil"] <= -2:
        vr += ("。籌碼指標在族群相對靠前,但修正日價格位於相對後段——原始值未必是買超；"
               "此類歷史樣本表現分歧,詳見週報的同條件比較,等抗跌轉正再確認")
    # 元素 × 權重分解:依左側①②③④⑤自然順序(不依權重大小排,避免循環數字跳來跳去)。
    # 每列 = [標籤, 顯示值, hint(此表不用), 分數(供JS用scColor上色), 權重文字(muted顯示), flag,
    #         貢獻數值(供JS畫等尺度貢獻條;None=不畫)]
    # flag: "total"=加大加粗、"muted"=整列調淡(權重0=只供tier判定、不計入加總——由 WEIGHTS 動態判斷,
    # 不寫死是哪個元素,權重一旦調整就自動跟著變)
    def vrow(label, key, wkey):
        v = sc[key]
        weight = WEIGHTS[wkey]
        tier_only = weight == 0
        contribution = v * weight
        wt = f"× {weight:g} = {contribution:+.1f}" + ("  · 只供分層條件" if tier_only else "")
        return [label, f"{v:+d}", None, v, wt, "muted" if tier_only else "",
                None if tier_only else round(contribution, 2)]
    today = sc["composite"]
    vrows = [["今日分(未平滑)", f"{today:+.1f}", "下列各項元素分 × 權重的貢獻加總",
              round(today, 1), None, "total", round(today, 2)],
             vrow("①相對強弱", "s_price", "price"),
             vrow("①抗跌", "s_resil", "resil"),
             vrow("②量", "s_vol", "vol"),
             vrow("③外資", "s_foreign", "foreign"),
             vrow("③修正日相對位置", "s_dip", "dip"),
             vrow("④投信", "s_trust", "trust"),
             vrow("⑤融資券", "s_margin", "margin")]
    history = list(comp_history or [])[-3:]
    if history:
        parts, values = [], []
        for h in history:
            date, value = _value(h, "date"), _value(h, "composite")
            if value is None:
                continue
            values.append(value)
            date_label = f"{int(date[5:7])}/{int(date[8:10])}" if date else "-"
            parts.append(f"{date_label} {value:+.1f}")
        if values:
            equation = " + ".join(f"({v:+.1f})" for v in values)
            vrows.append(["近3個交易日", " → ".join(parts),
                          "每天依元素分與權重加總出的未平滑分", None, None, "", None])
            vrows.append(["3日平均(評級用)", f"{comp:+.1f}",
                          f"({equation}) ÷ {len(values)} = {comp:+.1f}", round(comp, 1), None, "total",
                          round(comp, 2)])
    else:
        vrows.append(["3日平均(評級用)", f"{comp:+.1f}",
                      "每日未平滑分歷史未提供；此值取自資料庫既有的三日平滑結果",
                      round(comp, 1), None, "total", round(comp, 2)])
    return TIER_VT.get(tier, 0), tier, vsub, vr, int(sc["warn"]), vrows


# 籌碼健康度(觀察層、純描述性,獨立於①價②量與 tier)——net_score/label 已由
# score.py 的 chip_health 表算好;這裡只重算「每個信號」的顯示明細(門檻沿用 score.py 匯入的
# 同一份常數,跟①②③④⑤ element cells 的 hint 現算是同一套慣例,不重複造輪子)。
CHIP_LABELS = ["外資20日變化(↑增持)", "投信近5日佔股本(↑買超)",
               "融資水位(低水位較健康)", "融資10日變化(↓去槓桿)",
               "大戶400張+週變化(↑集中·觀察)", "股東人數週變化(↓集中·觀察)",
               "借券餘額10日變化(↓減壓·觀察)"]


def _raw_direction(v, up, down, flat):
    if v is None:
        return "資料不足"
    if v > 0:
        return up
    if v < 0:
        return down
    return flat


def _chip_reading(direction, signal, observational=False):
    verdict = "健康訊號" if signal > 0 else "警示" if signal < 0 else "中性"
    note = "；方向尚未用規則定案後的新資料驗證" if observational else "；依既有校準門檻"
    if direction == "資料不足":
        return "資料不足 → 中性(不計健康/警示)" + ("；方向尚未用規則定案後的新資料驗證" if observational else "")
    return f"{direction} → 本欄判讀為{verdict}{note}"


def _chip_pp(v):
    """觀察欄保留微小正負方向；避免 ±0.004pp 被兩位小數顯示成 ±0.00pp。"""
    if v is None:
        return "-"
    if v == 0:
        return "0.00pp"
    if abs(v) < 0.00005:
        return ("+" if v > 0 else "-") + "<0.0001pp"
    if abs(v) < 0.005:
        return f"{v:+.4f}pp"
    return f"{v:+.2f}pp"


def build_chip_rows(m, risky):
    """回傳 (rows, n_health, n_warn)——rows 給 tooltip 表格,n_health/n_warn 給判讀句(不含官方否決項)。"""
    fc, tp, u, mc = m["fpct_chg20"], m["trust5_pct"], m["margin_util_pct"], m["margin_chg10"]
    tb, tpl, sb = m["tdcc_big400_chg"], m["tdcc_people_chg"], m["sbl_chg10"]
    sigs = [
        _chip_signal(fc, lambda v: v > DZ_FOREIGN, lambda v: v < -DZ_FOREIGN),
        _chip_signal(tp, lambda v: v > DZ_TRUST, lambda v: v < -DZ_TRUST),
        _chip_signal(u, lambda v: v < MARGIN_UTIL_MID, lambda v: v >= MARGIN_UTIL_HOT),
        _chip_signal(mc, lambda v: v <= MARGIN_DOWN_BIG, lambda v: v >= MARGIN_UP_BIG),
        _chip_signal(tb, lambda v: v > 0, lambda v: v < 0),
        _chip_signal(tpl, lambda v: v < 0, lambda v: v > 0),
        _chip_signal(sb, lambda v: v < 0, lambda v: v > 0),
    ]
    vals = [f"{fc:+.2f}pp" if fc is not None else "-",
            f"{tp:+.3f}%" if tp is not None else "-",
            pctp(u),
            pct(mc, True) if mc is not None else "-",
            _chip_pp(tb),
            pct(tpl, True) if tpl is not None else "-",
            _chip_pp(sb)]
    directions = [
        _raw_direction(fc, "外資增持", "外資減持", "外資持股持平"),
        _raw_direction(tp, "投信買超", "投信賣超", "投信持平"),
        ("資料不足" if u is None else
         "融資低水位" if sigs[2] > 0 else "融資高水位" if sigs[2] < 0 else "融資中等水位"),
        _raw_direction(mc, "融資增加(槓桿升高)", "融資下降(去槓桿)", "融資持平"),
        _raw_direction(tb, "大戶集中度上升", "大戶集中度下降", "大戶集中度持平"),
        _raw_direction(tpl, "股東人數增加(籌碼分散)", "股東人數下降(籌碼集中)", "股東人數持平"),
        _raw_direction(sb, "借券賣出餘額增加(壓力升高)", "借券賣出餘額下降(壓力減輕)",
                       "借券賣出餘額持平"),
    ]
    rows = [[lb, v, _chip_reading(direction, s, i >= 4), s, None, ""]
            for i, (lb, v, direction, s) in enumerate(zip(CHIP_LABELS, vals, directions, sigs))]
    rows.append(["官方處置/注意", "有列管" if risky else "無",
                 "交易所列管 → 一票否決為待觀察" if risky else "當天無交易所列管",
                 (-1 if risky else 0), None, ""])
    n_health = sum(1 for s in sigs if s > 0)
    n_warn = sum(1 for s in sigs if s < 0)
    return rows, n_health, n_warn


# 基本面參考(觀察層、不計分,獨立於①②③④⑤ tier)——月營收/季報由 fetch_financials.py
# 獨立排程填入(月/季頻,非每日,見 CLAUDE.md)。只用月營收 YoY/MoM + 損益表毛利率趨勢/EPS;
# 資產負債表/現金流量表型態太細(單期 ~90 個 type),不上儀表板,留供 Universe 治理(R1)查證用。
FUND_YOY_UP, FUND_YOY_DOWN = 0.10, -0.10   # 月營收年增分類門檻(僅供 badge 顏色分類,不影響 tier)


def _prev_month(y, m):
    return (y, m - 1) if m > 1 else (y - 1, 12)


def build_fund_map(con):
    """批次查詢全 universe 的基本面參考資料,回傳 {stock_id: tooltip payload}。
    缺資料(新股/尚未回補)的股票不進 dict,前端不顯示 badge——不強求每檔都有。"""
    mr_by_sid = defaultdict(list)
    for r in con.execute("""SELECT stock_id, date, revenue, revenue_year, revenue_month
                            FROM month_revenue ORDER BY stock_id, date DESC"""):
        mr_by_sid[r["stock_id"]].append(r)
    fin_by_sid = defaultdict(dict)
    for r in con.execute("""SELECT stock_id, date, type, value FROM financials
                            WHERE type IN ('Revenue','GrossProfit','EPS')"""):
        fin_by_sid[r["stock_id"]].setdefault(r["date"], {})[r["type"]] = r["value"]

    out = {}
    for sid, mrs in mr_by_sid.items():
        latest = mrs[0]
        py, pm = _prev_month(latest["revenue_year"], latest["revenue_month"])
        mom = (latest["revenue"] / mrs[1]["revenue"] - 1) if (
            len(mrs) > 1 and mrs[1]["revenue"] and
            mrs[1]["revenue_year"] == py and mrs[1]["revenue_month"] == pm) else None
        yoy_row = next((r for r in mrs[1:] if r["revenue_year"] == latest["revenue_year"] - 1
                        and r["revenue_month"] == latest["revenue_month"]), None)
        yoy = (latest["revenue"] / yoy_row["revenue"] - 1) if (yoy_row and yoy_row["revenue"]) else None

        fq = fin_by_sid.get(sid, {})
        fdates = sorted(fq)[-4:]   # 近4季,舊到新
        gms = [(d, (fq[d]["GrossProfit"] / fq[d]["Revenue"] * 100)
                if (fq[d].get("Revenue") and fq[d].get("GrossProfit") is not None) else None)
               for d in fdates]
        latest_eps = fq[fdates[-1]].get("EPS") if fdates else None

        if yoy is None and mom is None and not fdates:
            continue
        cls = ("up" if (yoy is not None and yoy >= FUND_YOY_UP) else
               "down" if (yoy is not None and yoy <= FUND_YOY_DOWN) else "flat")
        rows = [["最新月營收", f"{latest['revenue']/1e8:,.1f} 億元"
                 f"({latest['revenue_year']}/{latest['revenue_month']:02d})", None],
                ["月增(MoM)", f"{mom*100:+.1f}%" if mom is not None else "-", "與上月比"],
                ["年增(YoY)", f"{yoy*100:+.1f}%" if yoy is not None else "-",
                 "與去年同月比——台股最常見的營收動能指標"]]
        if gms:
            trend = " → ".join(f"{g:.1f}%" if g is not None else "-" for _, g in gms)
            rows.append(["近4季毛利率趨勢", trend, f"{fdates[0]} ~ {fdates[-1]},舊到新"])
        if latest_eps is not None:
            rows.append(["最新季EPS", f"{latest_eps:.2f} 元", f"季別:{fdates[-1]}"])
        # 近13個月營收柱形原料(舊到新,億元):第1柱≈最新月的去年同月,基期效應
        # (去年同月特別低造成的高YoY)看柱形一眼識破——與 why 文案的警告同源
        spark = [round(x["revenue"] / 1e8, 2) for x in mrs[:13]
                 if x["revenue"] is not None][::-1]
        label = f"營收YoY {yoy*100:+.0f}%" if yoy is not None else "營收YoY 資料不足"
        if yoy is not None:
            direction = "增加" if yoy > 0 else "減少" if yoy < 0 else "持平"
            why = (f"最新單月營收較去年同月{direction} {abs(yoy)*100:.1f}%。這只是已公告營收的"
                   "同比描述；營收不等於獲利,也不能單獨代表需求或整體營運變強/變弱。基期、"
                   "收入認列時點、工作天數、售價、併購與產品組合都可能影響單月數字,"
                   "需搭配公司筆記與季報判讀。")
        else:
            why = ("月營收年增樣本不足(上市未滿13個月或資料尚未回補齊)。營收不等於獲利或"
                   "整體營運強弱；即使有月增資料,仍可能受基期、收入認列時點、工作天數、售價、"
                   "併購與產品組合影響。")
        out[sid] = {"cls": cls, "label": label, "rows": rows, "why": why,
                    "spark": spark if len(spark) >= 2 else None}
    return out


# 族群狀態→顏色(狀態本身由 fetch_daily._gstate 在資料層算好,存 group_metrics.state)
# 蓄勢用 --warn 而非 --warn-line:此色會當「狀態文字」的前景色,warn-line(#d69e2e)在
# 淺色 surface 上對比僅約 2.2:1,warn 是同語彙的可讀文字版
STATE_COL = {"蓄勢·被佈局": "var(--warn)", "發動·領漲": "var(--strong)",
             "籌碼退潮": "var(--weak)"}

# 族群卡 tooltip 教學文字(門檻值 import 自 fetch_daily,改旋鈕自動同步)。
# 各指標的定義寫在每列數據自己的 hint(見 groups 組裝),這裡只留狀態判定規則。
GROUP_HOW = (
    f"族群狀態每日由上列指標判定(規則在資料層,非儀表板):蓄勢·被佈局=修正日中位買賣>0 且 "
    f"中位距60日高≤{GS_OFF_HIGH*100:+.0f}%(修正日外資為淨買,且價格尚未回高);"
    f"發動·領漲=20日動能贏全體 且 價近波段高;籌碼退潮=修正日遭調節 且 佈局廣度≤"
    f"{GS_BREADTH_LOW*100:.0f}%;其餘=中性觀察。修正日中位買賣為選族群主訊號(樣本外驗證中,"
    f"見週報)。卡片把『目前原始值』與『較5日前的變化』分欄顯示；改善不代表已轉為正值。")
GROUP_SRC = "個股五元素於族群層聚合(等權中位數/廣度);原始資料 FinMind"


def _streak(series):
    """最新狀態往回連續了幾個交易日、自哪天起。series 依日期升冪。"""
    if not series:
        return None, None
    cur, n = series[-1]["state"], 0
    for x in reversed(series):
        if x["state"] != cur:
            break
        n += 1
    d = series[-n]["date"]
    return n, f"{int(d[5:7])}/{int(d[8:10])}"


def _five_day_delta(series, key, eps, scale=1.0, digits=2):
    """回傳獨立的 5 日比較文字；較高一律稱改善，並保留 delta 正負號。"""
    if len(series) < 6:
        return "5日比較資料不足"
    cur, prev = series[-1][key], series[-6][key]
    if cur is None or prev is None:
        return "5日比較資料不足"
    delta = cur - prev
    direction = "改善" if delta >= eps else "惡化" if delta <= -eps else "持平"
    return f"較5日前{direction} {delta*scale:+.{digits}f}pp"


def _five_day_value(series, key):
    """圖像化座標的五日前 raw 值；樣本或欄位不足時明確回傳 null。"""
    if len(series) < 6:
        return None
    return series[-6][key]


def _current_dip(v):
    """動詞已帶方向 → 數值用絕對值(「淨賣 -0.27%」是雙重否定,且與 build_overview
    摘要句的「仍淨賣 0.27%股本」寫法不一致)。"""
    if v is None:
        return "-"
    if v > 0:
        return f"淨買 {v:.2f}%股本"
    if v < 0:
        return f"淨賣 {abs(v):.2f}%股本"
    return "買賣持平 0.00%股本"


def _current_relative(v):
    if v is None:
        return "-"
    if v > 0:
        return f"跑贏 {v*100:.1f}%"
    if v < 0:
        return f"跑輸 {abs(v)*100:.1f}%"
    return "與全體持平 0.0%"


def build_overview(grows):
    """首頁白話結論；明確區分『相對最好』與『原始值已轉正』。"""
    if not grows:
        return {"headline": "族群資料不足", "summary": "目前無法判讀族群強弱。",
                "points": [], "note": "請先確認 group_metrics 已更新。"}
    deployed = [r for r in grows if r["state"] == "蓄勢·被佈局"]
    dips = [r for r in grows if r["med_dip"] is not None]
    rels = [r for r in grows if r["rel20"] is not None]
    best_dip = max(dips, key=lambda r: r["med_dip"]) if dips else None
    best_rel = max(rels, key=lambda r: r["rel20"]) if rels else None

    if deployed:
        names = "、".join(GROUP_NM.get(r["grp"], r["grp"]) for r in deployed)
        headline = f"{names}目前符合「被佈局」條件"
        summary = "此狀態要求修正日中位買賣為正,並同時符合價格尚未回高的條件。"
        tone = "strong"
    elif best_dip and all(r["med_dip"] <= 0 for r in dips):
        nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
        headline = "目前沒有族群符合「被佈局」條件"
        summary = (f"{len(dips)}/{len(grows)} 族群的修正日中位皆為淨賣；{nm}的調節相對最少,"
                   f"但仍淨賣 {abs(best_dip['med_dip']):.2f}%股本；"
                   "相對最好不等於已出現買超。")
        tone = "warn"
    else:
        headline = "目前沒有族群符合「被佈局」條件"
        if best_dip:
            nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
            summary = (f"{nm}修正日淨買相對最高（{best_dip['med_dip']:+.2f}%股本）,"
                       "但尚未同時符合完整狀態條件。")
        else:
            summary = "修正日籌碼資料不足,暫不做族群佈局判讀。"
        tone = "neutral"

    points = []
    if best_dip:
        nm = GROUP_NM.get(best_dip["grp"], best_dip["grp"])
        points.append({"label": "籌碼相對位置", "text": f"{nm}：{_current_dip(best_dip['med_dip'])}",
                       "tone": "strong" if best_dip["med_dip"] > 0 else "warn"})
    if best_rel:
        nm = GROUP_NM.get(best_rel["grp"], best_rel["grp"])
        points.append({"label": "價格相對位置", "text": f"{nm}：{_current_relative(best_rel['rel20'])}",
                       "tone": "strong" if best_rel["rel20"] > 0 else "warn"})
    return {"headline": headline, "summary": summary, "points": points, "tone": tone,
            "note": "族群比較是相對結果；請同時閱讀目前原始值與5日變化。"}


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    last = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    if not last:
        print("daily_scores 沒有資料,請先跑 score.py")
        return
    rows = con.execute("""SELECT u.stock_id, u.name, u.grp, u.biz, sc.*, m.*
        FROM daily_scores sc JOIN universe u USING(stock_id) JOIN daily_metrics m USING(date, stock_id)
        WHERE sc.date=?""", (last,)).fetchall()
    # 使用每日未平滑 composite 讓使用者能驗算 composite_s；每檔只留最近3個交易日、舊到新。
    score_hist = defaultdict(list)
    for h in con.execute("""SELECT date, stock_id, composite FROM daily_scores
                            WHERE date<=? ORDER BY stock_id, date DESC""", (last,)):
        if len(score_hist[h["stock_id"]]) < 3:
            score_hist[h["stock_id"]].insert(0, h)
    # 個股技術面:穿越/變化解讀需今日、昨日與5個交易日前;強調式小圖需20日
    # 還原價+MA20 → 每檔保留最近20個交易日,舊到新。
    tech_hist = defaultdict(list)
    for h in con.execute("""SELECT date, stock_id, close_adj, ma5, ma20, ma60, rsi14,
                                    volume, vol_ma20, vol_ratio20, ret1
                             FROM daily_metrics WHERE date<=?
                             ORDER BY stock_id, date DESC""", (last,)):
        if len(tech_hist[h["stock_id"]]) < 20:
            tech_hist[h["stock_id"]].insert(0, h)
    try:   # 族群定義配置化:讀 groups 表(舊 db 缺表時退回檔頭預設)
        gmeta = con.execute("SELECT grp, name, tag FROM groups ORDER BY ord").fetchall()
        if gmeta:
            GROUP_ORDER[:] = [g["grp"] for g in gmeta]
            GROUP_NM.update({g["grp"]: g["name"] for g in gmeta})
            GROUP_TAG.update({g["grp"]: g["tag"] for g in gmeta})
    except sqlite3.OperationalError:
        pass
    try:   # 舊 db 尚無族群/大盤表 → 雷達留空(跑一次 fetch_daily 即補齊)
        grows = con.execute("SELECT * FROM group_metrics WHERE date=?", (last,)).fetchall()
        # 指數資料可能落後個股一日 → 取 ≤last 的最近一筆(顯示時標註日期)
        mk = con.execute("""SELECT * FROM market_daily WHERE date<=? AND dd20 IS NOT NULL
                            ORDER BY date DESC LIMIT 1""", (last,)).fetchone()
        # 大盤 20 日報酬(含息報酬指數):①價 tooltip 的基準線,與個股 ret20 同窗口
        mkrows = con.execute("""SELECT taiex FROM market_daily WHERE taiex IS NOT NULL
                                AND date<=? ORDER BY date""", (last,)).fetchall()
        mkt20 = (mkrows[-1]["taiex"] / mkrows[-21]["taiex"] - 1) if len(mkrows) >= 21 else None
        # 族群歷史:狀態連續天數 + 各欄獨立的 5 日變化說明
        ghist = con.execute("""SELECT date, grp, state, med_dip, breadth_f, rel20,
                                      med_dist60, breadth_t FROM group_metrics
                               WHERE date<=? ORDER BY date""", (last,)).fetchall()
    except sqlite3.OperationalError:
        grows, mk, mkt20, ghist = [], None, None, []
    gseries = {}
    for x in ghist:
        gseries.setdefault(x["grp"], []).append(x)
    # 廣度的分子/分母(與 fetch_daily 口徑一致:分母=當日有值的成員數)——tooltip 顯示 x/N 檔
    bcnt = {r["grp"]: r for r in con.execute("""SELECT u.grp,
            SUM(CASE WHEN m.fpct_chg20>0 THEN 1 ELSE 0 END) f_pos, COUNT(m.fpct_chg20) f_n,
            SUM(CASE WHEN m.trust5_pct>0 THEN 1 ELSE 0 END) t_pos, COUNT(m.trust5_pct) t_n
            FROM daily_metrics m JOIN universe u USING(stock_id)
            WHERE m.date=? GROUP BY u.grp""", (last,))}
    # 處置/注意股票(觀察層、不計分):交易所官方認證的異常價量列管,五元素分數看不到——
    # 只顯示當天名單,不判斷起訖(risk_flags 由 fetch_daily 每日整表重建)
    risk = {}
    try:
        for r in con.execute("SELECT stock_id, kind, reason, period FROM risk_flags WHERE date=?", (last,)):
            risk.setdefault(r["stock_id"], []).append(
                {"kind": r["kind"], "reason": r["reason"], "period": r["period"]})
    except sqlite3.OperationalError:
        pass
    # 籌碼健康度(觀察層、獨立新表,舊 db 未跑過新版 score.py 時沒有此表 → 全部從缺,不擋主管線)
    chip = {}
    try:
        for r in con.execute(
                "SELECT stock_id, label FROM chip_health WHERE date=?", (last,)):
            chip[r["stock_id"]] = {"label": r["label"]}
    except sqlite3.OperationalError:
        pass
    # 基本面參考(觀察層、獨立新表,fetch_financials.py 尚未跑過的 db 沒有這些表 → 從缺,不擋主管線)
    try:
        fund_map = build_fund_map(con)
    except sqlite3.OperationalError:
        fund_map = {}
    con.close()
    # 質化筆記(觀察層、AI 協作＋獨立 reviewer,見 notes/qualitative/):無筆記時 load_notes
    # 回傳空 dict,同 fund_map 的「從缺不擋主管線」慣例
    notes_map = load_notes(NOTES_DIR)
    # 領先假說是獨立觀察層；lint 會要求其錨定有效 independently_verified 正式筆記。
    hypotheses_map = load_hypothesis_reports(HYPOTHESES_DIR, notes=notes_map)

    CHIP_CLS = {"健康": "health", "中性": "neutral", "待觀察": "warn"}
    chip_by_grp = {}
    for r in rows:
        c = chip.get(r["stock_id"])
        if not c:
            continue
        cc = chip_by_grp.setdefault(r["grp"], {"health": 0, "neutral": 0, "warn": 0, "dots": []})
        cls = CHIP_CLS[c["label"]]
        cc[cls] += 1
        cc["dots"].append(cls)

    dip_rows = [x for x in grows if x["med_dip"] is not None]
    best_dip_row = max(dip_rows, key=lambda x: x["med_dip"]) if dip_rows else None
    best_dip = best_dip_row["grp"] if best_dip_row else None
    groups = []
    for g in GROUP_ORDER:
        r = next((x for x in grows if x["grp"] == g), None)
        if not r:
            continue
        note = r["note"] or ""
        if g == best_dip:
            if r["med_dip"] > 0:
                note += f"(★ 修正日淨買為 {len(GROUP_ORDER)} 族群最高)"
            elif r["med_dip"] < 0:
                note += f"(★ 修正日調節為 {len(GROUP_ORDER)} 族群相對最少,但仍是淨賣)"
            else:
                note += f"(★ 修正日買賣為 {len(GROUP_ORDER)} 族群相對最高,目前持平)"
        ser = gseries.get(g, [])
        n, since = _streak(ser)
        bc = bcnt.get(g)
        # stats 每列 = [標籤, 當下原始值, 白話解讀, 5日變化]；不可把方向箭頭黏在原始值後面。
        # 解讀句由「當下數值」生成(方向、對照門檻),不是通用定義——這是看得懂的關鍵。
        dip = r["med_dip"]
        dip_dyn = ("" if dip is None else
                   (";目前=族群修正日外資淨買" if dip > 0 else
                    ";目前=族群修正日外資淨賣" if dip < 0 else ";目前買賣持平"))
        rel = r["rel20"]
        rel_dyn = ("" if rel is None else
                   (";目前=跑贏其他族群" if rel > 0 else ";目前=落後其他族群" if rel < 0 else ""))
        dist = r["med_dist60"]
        dist_dyn = ("" if dist is None else
                    (f";目前≤{GS_OFF_HIGH*100:.0f}%=「價未回高」(蓄勢的前提)" if dist <= GS_OFF_HIGH
                     else ";目前接近波段高"))
        bf = r["breadth_f"]
        bf_dyn = ("" if bf is None else
                  (f";目前≤{GS_BREADTH_LOW*100:.0f}%=廣度低(個案而非族群現象)" if bf <= GS_BREADTH_LOW
                   else ";過半成員被增持=族群現象" if bf > 0.5 else ""))
        dist_value = ("-" if dist is None else
                      f"低於60日高 {abs(dist)*100:.1f}%" if dist < 0 else
                      "位於60日高 0.0%" if dist == 0 else
                      f"高於參考高點 {dist*100:+.1f}%")
        # stats 第5欄=圖形規格(前端渲染):{"spark":trend鍵}=30日迷你趨勢線、
        # {"meter":[值,滿格,門檻]}=廣度量尺;None=純文字列。文字欄完全不動。
        bt = r["breadth_t"]
        gobj = {"g": g, "nm": GROUP_NM.get(g, g), "state": r["state"],
                "col": STATE_COL.get(r["state"], "var(--neutral)"), "note": note,
                "axis": {"price": rel, "dip": dip,
                         "price5": _five_day_value(ser, "rel20"),
                         "dip5": _five_day_value(ser, "med_dip")},
                # 30個交易日的走勢原料(缺值日剔除,迷你圖只看形狀)
                "trend": {"dip": [round(x["med_dip"], 3) for x in ser[-30:]
                                  if x["med_dip"] is not None],
                          "rel": [round(x["rel20"] * 100, 2) for x in ser[-30:]
                                  if x["rel20"] is not None]},
                "stats": [
            ["修正日外資買賣中位",
             _current_dip(dip),
             "族群下跌日外資買賣的20日累計佔股本%(取成員中位)。"
             f"正=淨買、負=淨賣{dip_dyn}",
             _five_day_delta(ser, "med_dip", 0.01, 1, 2),
             {"spark": "dip"}],
            ["外資增持廣度",
             f"{bf*100:.0f}%成員增持({bc['f_pos']}/{bc['f_n']}檔)" if (bf is not None and bc) else "-",
             f"近20日外資持股增加的成員比例；用來分辨普遍現象或少數個案{bf_dyn}",
             _five_day_delta(ser, "breadth_f", 0.01, 100, 0),
             {"meter": [round(bf, 3), 1, 0.5]} if bf is not None else None],
            ["20日動能 vs 全體",
             _current_relative(rel),
             "族群中位20日報酬 − 全部掃描標的中位——族群跟其他族群比"
             f"(個股卡的①價是族群內比){rel_dyn}",
             _five_day_delta(ser, "rel20", 0.005, 100, 1),
             {"spark": "rel"}],
            ["中位距60日高",
             dist_value,
             f"成員距自己60日高點的中位數,衡量族群整體回檔深度{dist_dyn}",
             _five_day_delta(ser, "med_dist60", 0.001, 100, 1),
             None],
            ["投信買超廣度",
             f"{bt*100:.0f}%成員淨買({bc['t_pos']}/{bc['t_n']}檔)"
             if (bt is not None and bc) else "-",
             "近5日投信(本土基金)買超的成員比例,與外資廣度對照看參與度",
             _five_day_delta(ser, "breadth_t", 0.01, 100, 0),
             {"meter": [round(bt, 3), 1, 0.5]} if bt is not None else None],
        ]}
        if n:
            gobj["dur"] = f"第 {n} 個交易日(自 {since})"
        if g in chip_by_grp:
            gobj["chip"] = chip_by_grp[g]
        groups.append(gobj)
    overview = build_overview(grows)
    lag = f",指數至 {int(mk['date'][5:7])}/{int(mk['date'][8:10])}" if (mk and mk["date"] != last) else ""
    mchip = (f"市場 <b>{'⚠ 修正' if mk['regime'] else '多頭/中性'}</b>(報酬指數距20日高 {mk['dd20']*100:+.1f}%{lag})"
             if (mk and mk["dd20"] is not None) else "市場 <b>-</b>")
    mtip = None
    if mk and mk["dd20"] is not None:
        regime = bool(mk["regime"])
        mtip = {
            "el": "市場環境", "scLabel": "⚠ 修正" if regime else "多頭/中性",
            "scColor": "var(--warn-line)" if regime else "var(--neutral)",
            "scBg": "var(--neutral-tint)", "who": "加權報酬指數(含息)",
            "rows": [["指數日期", mk["date"]],
                     ["距20日高", f"{mk['dd20']*100:+.1f}%",
                      "含息指數距近20個交易日最高點回落多少;回檔深度的量尺"],
                     ["修正門檻", f"≤ {REGIME_DD*100:.0f}%",
                      "回落超過此值即判為修正市場情境,頁首籤條會轉「⚠ 修正」"],
                     ["20日報酬", pct(mkt20, True),
                      "全市場近一個月的基準線;個股①價 tooltip 的「大盤20日」同此值"]],
            "why": ("報酬指數距 20 日高回落超過門檻,判定為修正市場情境——此時「修正日抗跌」"
                    "「修正日外資買賣」等訊號較有辨識力,適合觀察哪個族群先止穩轉強。" if regime else
                    "距 20 日高回落未達門檻,市場處於多頭/中性,個股訊號以族群內相對強弱為主。"),
            "how": (f"距20日高 ≤ {REGIME_DD*100:.0f}% → 修正市場情境。使用「含息」報酬指數而非"
                    "價格指數,避免除息季的機械性下跌扭曲市場比較。"),
            "src": "FinMind 加權報酬指數(TAIEX 含息)"}

    data, tiers_map = [], {}
    for r in rows:
        tier_meta = tier_ui_payload(r)
        hist = score_hist.get(r["stock_id"]) or []
        vt, tier, vsub, vr, warn, vrows = verdict(r, hist)
        obj = {"g": r["grp"], "id": r["stock_id"], "nm": r["name"], "biz": r["biz"] or "",
               "vt": vt, "vlabel": tier_meta["tier_label"], "vkey": tier,
               "vsub": vsub, "vr": vr, "vrows": vrows,
               # 綜評條原料:3日平滑分(實條)+近3日未平滑分(殘影點),與 vrows 文字同源
               "comp": round(r["composite_s"], 2) if r["composite_s"] is not None else None,
               "comp3": [round(h["composite"], 2) for h in hist[-3:]
                         if h["composite"] is not None],
               "cells": build_cells(r, r, mkt20)}
        obj.update(tier_meta)
        tech = build_technical_view(r, tech_hist.get(r["stock_id"]))
        if tech:
            obj["tech"] = tech
        if warn:
            obj["warn"] = True
        risky = r["stock_id"] in risk
        if risky:
            obj["risk"] = risk[r["stock_id"]]
        c = chip.get(r["stock_id"])
        if c:
            chip_rows, n_health, n_warn = build_chip_rows(r, risky)
            why = f"{n_health} 項健康信號、{n_warn} 項警示；原始正負號不直接代表好壞"
            if risky:
                why += "；當天列處置/注意,官方警示一票否決"
            obj["chip"] = {"cls": CHIP_CLS[c["label"]], "label": c["label"],
                           "rows": chip_rows, "why": why}
        f = fund_map.get(r["stock_id"])
        if f:
            obj["fund"] = f
        n = notes_map.get(r["stock_id"])
        if n:
            # asof 用資料日(last)而非 wall-clock today——archive 快照才可重現(同一資料日重建,
            # 「建議複核」判定不會因為隔幾天重跑而改變)
            st = note_status(n, last)
            verification = note_review_status(n)
            label = NOTE_LABEL[verification]
            if n.get("quality_invalid"):
                label += "・品質契約未通過"
            if st == "due":
                label += "・待更新"
            elif st == "draft":
                label += "・未填更新日"
            elif st == "unscheduled":
                label += "・未排複核日"
            obj["note"] = {
                "cls": verification, "label": label,
                "freshness": st, "due": st == "due",
                "updated": n["last_updated"] or "-", "next": n["next_review"] or "-",
                "contentAsOf": n.get("content_as_of") or "-",
                "latestPeriod": n.get("latest_financial_period") or "-",
                "reviewedAt": n.get("reviewed_at") or "-",
                "reviewedBy": n.get("reviewed_by") or "-",
                "reviewScope": n.get("review_scope") or "-",
                "qualityInvalid": n.get("quality_invalid", False),
                "qualityErrors": n.get("quality_errors", []),
                "claimCount": n.get("claim_count", 0),
                "citedClaims": n.get("cited_claim_count", 0),
                "primaryClaims": n.get("primary_cited_claim_count", 0),
                "primarySources": n.get("primary_source_count", 0),
                "summary": n["summary"], "tmplOld": n["template_version"] < NOTE_TEMPLATE_VERSION,
                "url": NOTE_REPO_BLOB + n["relpath"], "sections": n["sections"],
            }
        hypothesis = hypotheses_map.get(r["stock_id"])
        if hypothesis:
            status_counts = defaultdict(int)
            capture_mode_counts = defaultdict(int)
            lifecycle_counts = defaultdict(int)
            due_count = 0
            independent_chains = 0
            for item in hypothesis.get("hypotheses", []):
                raw = item.get("fields", {}).get("目前狀態", "")
                match = re.search(r"`([a-z_]+)`", raw)
                status_counts[match.group(1) if match else "unknown"] += 1
                hmeta = item.get("meta", {})
                capture_mode_counts[hmeta.get("capture_mode") or "unknown"] += 1
                lifecycle_counts[hmeta.get("lifecycle") or "unknown"] += 1
                try:
                    independent_chains += int(hmeta.get("independent_chain_count") or 0)
                except ValueError:
                    pass
                if (hmeta.get("lifecycle") == "open"
                        and re.fullmatch(r"\d{4}-\d{2}-\d{2}", hmeta.get("review_due", ""))
                        and hmeta["review_due"] <= last):
                    due_count += 1
            count = hypothesis.get("hypothesis_count", 0)
            obj["hypothesis"] = {
                "label": f"領先假說 {count} 則",
                "count": count,
                "updated": hypothesis.get("last_updated") or "-",
                "contentAsOf": hypothesis.get("content_as_of") or "-",
                "next": hypothesis.get("next_review") or "-",
                "qualityInvalid": hypothesis.get("quality_invalid", False),
                "qualityErrors": hypothesis.get("quality_errors", []),
                "statusCounts": dict(status_counts),
                "statusInfo": HYPOTHESIS_STATUS_INFO,
                "captureModeCounts": dict(capture_mode_counts),
                "lifecycleCounts": dict(lifecycle_counts),
                "dueCount": due_count,
                "independentChains": independent_chains,
                "schemaVersion": hypothesis.get("report_version", 0),
                "sections": hypothesis.get("sections", []),
                "url": NOTE_REPO_BLOB + hypothesis["relpath"],
            }
        obj["_comp"] = r["composite_s"]
        data.append(obj)
        tiers_map.setdefault(tier, []).append((r["composite_s"], r["stock_id"]))

    # 排序:族群順序,族群內綜合分數由高到低
    data.sort(key=lambda o: (GROUP_ORDER.index(o["g"]), -o["_comp"]))
    for o in data:
        del o["_comp"]

    # ◇ 蓄勢候補獨立卡片:從中性池抽出、插在蓄勢旁(缺項少者排前)
    cands = sorted(((r["pending"].count("、"), -r["composite_s"], r["stock_id"], r["pending"])
                    for r in rows if r["pending"] and r["tier"] == "潛在/中性"))
    cand_ids = [c[2] for c in cands]
    cand_sub = {c[2]: c[3].replace("蓄勢候補·", "") for c in cands}

    tiers = []
    for t in TIER_ORDER:
        if t in tiers_map:
            ids = [sid for _, sid in sorted(tiers_map[t], reverse=True)]
            if t == "潛在/中性":
                ids = [i for i in ids if i not in cand_ids]
            tiers.append({"key": t, "t": TIER_UI_LABEL.get(t, t), "d": TIER_DESC.get(t, ""),
                          "col": TIER_COL.get(t, "var(--neutral)"), "ids": ids})
        if t == "蓄勢·外資佈局" and cand_ids:
            tiers.append({"key": "蓄勢候補", "t": "◇ 相對蓄勢候補",
                          "d": "籌碼相對位置靠前；補齊後先成為今日初判,連2日才更新已確認層",
                          "col": "var(--neutral)", "ids": cand_ids, "sub": cand_sub})

    y, mo, d = last.split("-")
    date_str = f"{y}/{int(mo)}/{int(d)}"
    grpmeta = {g: {"nm": GROUP_NM.get(g, g), "tag": GROUP_TAG.get(g, ""),
                   "short": GROUP_SHORT.get(g, GROUP_NM.get(g, g))} for g in GROUP_ORDER}
    html = open(TEMPLATE, encoding="utf-8").read()
    html = html.replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    html = html.replace("__TIERS_JSON__", json.dumps(tiers, ensure_ascii=False))
    html = html.replace("__GROUPS_JSON__", json.dumps(groups, ensure_ascii=False))
    html = html.replace("__OVERVIEW_JSON__", json.dumps(overview, ensure_ascii=False))
    html = html.replace("__GRPMETA_JSON__", json.dumps(grpmeta, ensure_ascii=False))
    html = html.replace("__GORDER_JSON__", json.dumps(GROUP_ORDER))
    html = html.replace("__WEIGHTS_JSON__", json.dumps(WEIGHTS))
    # 量尺門檻(②量比/⑤融資水位)——單一事實來源 score.py,調旋鈕量尺刻度自動同步
    html = html.replace("__THRESH_JSON__", json.dumps({
        "volr_active": list(VOLR_ACTIVE), "volr_dry": VOLR_DRY, "volr_overheat": VOLR_OVERHEAT,
        "margin_mid": MARGIN_UTIL_MID, "margin_hot": MARGIN_UTIL_HOT}))
    html = html.replace("__PAGE_TITLE__", PAGE_TITLE)
    html = html.replace("__H1__", H1_TITLE)
    html = html.replace("__TITLE_TAIL_JSON__", json.dumps(TITLE_TAIL, ensure_ascii=False))
    html = html.replace("__SCOPE__", f"{len(GROUP_ORDER)} 族群 · {len(data)} 檔")
    html = html.replace("__MARKET_CHIP__", mchip)
    html = html.replace("__MKT_TIP_JSON__", json.dumps(mtip, ensure_ascii=False))
    html = html.replace("__GROUP_HOW_JSON__", json.dumps({"how": GROUP_HOW, "src": GROUP_SRC},
                                                         ensure_ascii=False))
    html = html.replace("__DATE_ISO__", last)
    html = html.replace("__DATE__", date_str)
    # 快照日期清單(含本次):注入頁內當 fallback,另寫 manifest 供已凍結的舊頁抓最新清單
    os.makedirs(ARCHIVE, exist_ok=True)
    dates = sorted({f[:10] for f in os.listdir(ARCHIVE)
                    if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.html", f)} | {last})
    html = html.replace("__DATES_JSON__", json.dumps(dates))
    open(OUT, "w", encoding="utf-8").write(html)
    archive_path = os.path.join(ARCHIVE, f"{last}.html")
    archive_created = not os.path.exists(archive_path)
    if archive_created:
        open(archive_path, "w", encoding="utf-8").write(html)
    open(os.path.join(ARCHIVE, "manifest.json"), "w", encoding="utf-8").write(json.dumps(dates))
    print(f"已重生 {OUT} — 資料日 {date_str},{len(data)} 檔,{len(tiers)} 個 tier;"
          f"{'建立' if archive_created else '保留既有'}快照 archive/{last}.html,"
          f"manifest 共 {len(dates)} 日")


if __name__ == "__main__":
    main()
