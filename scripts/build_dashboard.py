#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_dashboard.py — 從 SQLite(daily_scores + daily_metrics)自動重生儀表板 HTML。
吃 scripts/dashboard_template.html(CSS/JS 外殼),只注入資料 → index.html,
並把同一份頁面凍結成 archive/<資料日>.html(as-seen 歷史快照,供日期選單回看)。
零第三方依賴。用法:  uv run --no-project python scripts/build_dashboard.py
"""
import json, os, re, sqlite3, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import WEIGHTS   # 權重單一事實來源(score.py CONFIG),tooltip 顯示用
# 族群/大盤門檻單一事實來源(fetch_daily 頂部旋鈕),族群卡與市場籤條 tooltip 顯示用
from fetch_daily import REGIME_DD, GS_OFF_HIGH, GS_BREADTH_LOW

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
TEMPLATE = os.path.join(ROOT, "scripts", "dashboard_template.html")
OUT = os.path.join(ROOT, "index.html")   # 根目錄 index.html → GitHub Pages 乾淨網址
# 歷史快照:每日 build 原樣存檔,回看的是「當天使用者看到的報告」而非以現行規則重算
# (daily_scores 等衍生表每日全量重建,事後從 db 重繪會是 restated history,不可稽核)。
ARCHIVE = os.path.join(ROOT, "archive")

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
TIER_DESC = {"真強": "價強且籌碼扎實", "蓄勢·外資佈局": "外資/投信吃貨,價未發動",
             "強但過熱": "價強但散戶滿載,別追高", "潛在/中性": "訊號分歧,觀察",
             "真弱": "價籌俱弱", "真弱·陷阱": "外資出、散戶接"}

def pct(x, signed=False):
    """給『分數/比率』欄位(dist_hi、ret1、margin_chg):× 100 轉百分比。"""
    if x is None:
        return "-"
    return f"{x*100:+.1f}%" if signed else f"{x*100:.1f}%"


def pctp(x):
    """給『本身已是百分比』的欄位(turnover_pct / margin_util_pct):不再 × 100。"""
    return "-" if x is None else f"{x:.1f}%"

# 每個元素:score → 理由文字
R_PRICE = {2: "族群內領漲", 1: "強於族群", 0: "與族群同步", -1: "弱於族群", -2: "族群內落後"}
R_RESIL = {2: "修正日明顯抗跌", -2: "修正日領跌"}
R_FOREIGN = {2: "外資強力吃貨", 1: "外資淨買", 0: "外資中性", -1: "外資調節", -2: "外資倒貨/大幅撤出"}
R_TRUST = {2: "投信強力認養", 1: "投信淨買", 0: "投信中性/未參與", -1: "投信調節", -2: "投信大幅賣超"}
R_MARGIN = {2: "散戶大幅洗清", 1: "融資減、籌碼漸乾淨", 0: "融資平穩", -1: "融資增、散戶追高", -2: "散戶槓桿滿載、賣壓重"}
R_DIP = {2: "修正日外資逆勢吃貨", -2: "修正日外資逆勢倒貨"}
# 精簡標籤(給 vsub 用)
SALIENT = {("price", 2): "族群領漲", ("price", -2): "族群落後", ("foreign", 2): "外資吃貨", ("foreign", -2): "外資倒貨",
           ("trust", 2): "投信認養", ("trust", -2): "投信賣超", ("margin", 2): "散戶洗清", ("margin", -2): "散戶滿載",
           ("dip", 2): "修正日吃貨", ("dip", -2): "修正日遭倒", ("resil", 2): "修正抗跌", ("resil", -2): "修正領跌"}


def build_cells(sc, m, mkt20=None):
    """每格:[分數, 格值, 數據rows(標籤/數值對), 判讀, 過熱旗標?]——rows 供 tooltip 表格化顯示。
    mkt20 = 大盤(報酬指數)20日報酬,全 universe 共用,僅供①價 tooltip 當基準線。"""
    cells = []
    # ① 價(族群內相對強弱;距高做輔助資訊)
    # 族群中位由定義還原(rs20 = ret20 − 族群中位),不必回 db 重算
    rs = m["rs20"]
    gmed = (m["ret20"] - rs) if (m["ret20"] is not None and rs is not None) else None
    rows = [["20日報酬 − 族群中位", pct(rs, True)],
            ["└ 個股20日還原報酬", pct(m["ret20"], True)],
            ["└ 族群中位20日報酬", pct(gmed, True)],
            ["大盤20日(報酬指數,參考)", pct(mkt20, True)],
            ["距60日高(還原價)", pct(m["dist_hi60"])],
            ["修正日抗跌(20日)", f"{pct(m['down_rs20'], True)}(抗{sc['s_resil']:+d})"],
            ["前一日漲跌", pct(m["ret1"], True)]]
    cells.append([sc["s_price"], pct(rs, True) if rs is not None else "-", rows, R_PRICE[sc["s_price"]]])
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
    rows = [["量比(vs 自身60日中位)", f"{vr:.1f}×" if vr is not None else "樣本不足"],
            ["當日周轉率", pctp(t)]]
    c = [sc["s_vol"], f"{vr:.1f}×" if vr is not None else "-", rows, rv]
    if warn:
        c.append(1)
    cells.append(c)
    # ③ 外資
    fc = m["fpct_chg20"]
    rows = [["外資持股", f"{m['foreign_pct']:.1f}%" if m["foreign_pct"] is not None else "-"],
            ["20日持股變化", f"{fc:+.2f}pp" if fc is not None else "-"],
            ["修正日淨買(20日)", f"{m['dipbuy20']:+.2f}%股本(逆{sc['s_dip']:+d})"
             if m["dipbuy20"] is not None else "-"]]
    cells.append([sc["s_foreign"], f"{fc:+.1f}pp" if fc is not None else "-", rows,
                  R_FOREIGN[sc["s_foreign"]]])
    # ④ 投信
    t5 = m["trust5"] or 0
    tp = m["trust5_pct"]
    rows = [["近5日淨買賣", f"{t5:+,}張"],
            ["佔股本", f"{tp:+.3f}%" if tp is not None else "-"]]
    cells.append([sc["s_trust"], f"{t5:+,}張", rows, R_TRUST[sc["s_trust"]]])
    # ⑤ 融資券
    u = m["margin_util_pct"]
    rows = [["散戶水位(融資/股本)", pctp(u)],
            ["10日融資變化", pct(m["margin_chg10"], True)],
            ["20日還原價報酬", pct(m["ret20"], True)],
            ["券資比", f"{(m['short_margin_ratio'] or 0):.1f}%"]]
    c = [sc["s_margin"], pctp(u), rows, R_MARGIN[sc["s_margin"]]]
    if u is not None and u >= 9:
        c.append(1)
    cells.append(c)
    return cells


def verdict(sc):
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
        vsub = "吃貨中·等抗跌轉正"
    drivers = []
    for name, ref in [("價", "s_price"), ("抗跌", "s_resil"), ("外資", "s_foreign"),
                      ("逆勢", "s_dip"), ("投信", "s_trust"), ("融資", "s_margin")]:
        s = sc[ref]
        if abs(s) >= 2:
            drivers.append({"外資": R_FOREIGN, "逆勢": R_DIP, "投信": R_TRUST,
                            "融資": R_MARGIN, "價": R_PRICE, "抗跌": R_RESIL}[name][s])
    vr = "；".join(drivers) if drivers else "訊號分歧,持續觀察"
    if sc["pending"] and tier == "潛在/中性":
        vr += f"。◇ {sc['pending']}——籌碼條件已符,補齊即升蓄勢"
    elif chip and sc["s_resil"] <= -2:
        vr += "。籌碼在買但修正日領跌——此組合歷史表現分歧(見週報濾網 cohort),等抗跌轉正再確認"
    # 元素 × 權重分解(權重來自 score.py CONFIG,單一事實來源)
    vrows = [["綜合分(3日平滑)", f"{comp:+.1f}"],
             ["①相對強弱", f"{sc['s_price']:+d} × {WEIGHTS['price']}"],
             ["①抗跌", f"{sc['s_resil']:+d} × {WEIGHTS['resil']}"],
             ["④投信", f"{sc['s_trust']:+d} × {WEIGHTS['trust']}"],
             ["③外資", f"{sc['s_foreign']:+d} × {WEIGHTS['foreign']}"],
             ["⑤融資券", f"{sc['s_margin']:+d} × {WEIGHTS['margin']}"],
             ["②量", f"{sc['s_vol']:+d} × {WEIGHTS['vol']}"],
             ["③′逆勢買超", f"{sc['s_dip']:+d} × {WEIGHTS['dip']}(供tier)"]]
    return TIER_VT.get(tier, 0), tier, vsub, vr, int(sc["warn"]), vrows


# 族群狀態→顏色(狀態本身由 fetch_daily._gstate 在資料層算好,存 group_metrics.state)
STATE_COL = {"蓄勢·被佈局": "var(--warn-line)", "發動·領漲": "var(--strong)",
             "籌碼退潮": "var(--weak)"}

# 族群卡 tooltip 教學文字(門檻值 import 自 fetch_daily,改旋鈕自動同步)
GROUP_HOW = (
    f"族群狀態每日由聚合指標判定(規則在資料層,非儀表板):蓄勢·被佈局=修正日中位淨買>0 且 "
    f"中位距60日高≤{GS_OFF_HIGH*100:+.0f}%(下跌時有人接貨、價還沒回到高點——佈局特徵);"
    f"發動·領漲=20日動能贏全體 且 價近波段高;籌碼退潮=修正日遭調節 且 佈局廣度≤"
    f"{GS_BREADTH_LOW*100:.0f}%;其餘=中性觀察。「修正日中位淨買」=族群下跌日外資淨買20日累計"
    f"佔股本%的族群中位數——選族群的主訊號(樣本外驗證中,見週報);「外資佈局廣度」=20日外資"
    f"增持的成員比例;「20日動能 vs 全體」=族群中位20日報酬 − 全部掃描個股中位。"
    f"↗/↘/→ = 與 5 個交易日前相比的方向。")
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


def _arrow(series, key, eps):
    """與 5 個交易日前相比的方向箭頭;樣本不足或缺值回空字串。"""
    if len(series) < 6:
        return ""
    cur, prev = series[-1][key], series[-6][key]
    if cur is None or prev is None:
        return ""
    if cur - prev >= eps:
        return " ↗"
    if prev - cur >= eps:
        return " ↘"
    return " →"


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
        # 族群歷史:狀態連續天數(「首先轉強」要看得出先後)+ 5 日方向箭頭
        ghist = con.execute("""SELECT date, grp, state, med_dip, rel20 FROM group_metrics
                               WHERE date<=? ORDER BY date""", (last,)).fetchall()
    except sqlite3.OperationalError:
        grows, mk, mkt20, ghist = [], None, None, []
    gseries = {}
    for x in ghist:
        gseries.setdefault(x["grp"], []).append(x)
    con.close()

    dips = [(x["med_dip"], x["grp"]) for x in grows if x["med_dip"] is not None]
    best_dip = max(dips)[1] if dips else None      # 修正日買超最高的族群(選族群主訊號)
    groups = []
    for g in GROUP_ORDER:
        r = next((x for x in grows if x["grp"] == g), None)
        if not r:
            continue
        note = r["note"] + (f"(★ 修正日買超 {len(GROUP_ORDER)} 族群最高)" if g == best_dip else "")
        ser = gseries.get(g, [])
        n, since = _streak(ser)
        a_dip = _arrow(ser, "med_dip", 0.01)     # %股本,顯示 2 位小數 → 死區 0.01
        a_rel = _arrow(ser, "rel20", 0.005)      # 比率,顯示 0.1% 一位 → 死區 0.5pp
        gobj = {"g": g, "nm": GROUP_NM.get(g, g), "state": r["state"],
                "col": STATE_COL.get(r["state"], "var(--neutral)"), "note": note, "stats": [
            ["修正日中位淨買", f"{r['med_dip']:+.2f}%股本{a_dip}" if r["med_dip"] is not None else "-"],
            ["外資佈局廣度", f"{r['breadth_f']*100:.0f}%" if r["breadth_f"] is not None else "-"],
            ["20日動能 vs 全體", f"{pct(r['rel20'], True)}{a_rel}" if r["rel20"] is not None else "-"],
            ["中位距60日高", pct(r["med_dist60"]) if r["med_dist60"] is not None else "-"],
            ["投信買超廣度", f"{r['breadth_t']*100:.0f}%" if r["breadth_t"] is not None else "-"],
        ]}
        if n:
            gobj["dur"] = f"第 {n} 個交易日(自 {since})"
        groups.append(gobj)
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
                     ["距20日高", f"{mk['dd20']*100:+.1f}%"],
                     ["修正門檻", f"≤ {REGIME_DD*100:.0f}%"],
                     ["20日報酬", pct(mkt20, True)]],
            "why": ("報酬指數距 20 日高回落超過門檻,判定為修正 regime——此時「修正日抗跌」"
                    "「修正日買超」等訊號鑑別度最高,適合觀察哪個族群先止穩轉強。" if regime else
                    "距 20 日高回落未達門檻,市場處於多頭/中性,個股訊號以族群內相對強弱為主。"),
            "how": (f"距20日高 ≤ {REGIME_DD*100:.0f}% → 修正 regime。刻意用「含息」報酬指數而非"
                    "價格指數——除息季價格指數會機械性下跌,含息指數才反映真實市場強弱。"),
            "src": "FinMind 加權報酬指數(TAIEX 含息)"}

    data, tiers_map = [], {}
    for r in rows:
        vt, tier, vsub, vr, warn, vrows = verdict(r)
        obj = {"g": r["grp"], "id": r["stock_id"], "nm": r["name"], "biz": r["biz"] or "",
               "vt": vt, "vlabel": tier, "vsub": vsub, "vr": vr, "vrows": vrows,
               "cells": build_cells(r, r, mkt20)}
        if warn:
            obj["warn"] = True
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
            tiers.append({"t": t, "d": TIER_DESC.get(t, ""), "col": TIER_COL.get(t, "var(--neutral)"), "ids": ids})
        if t == "蓄勢·外資佈局" and cand_ids:
            tiers.append({"t": "◇ 蓄勢候補", "d": "籌碼已吃貨(屬潛在/中性),補齊缺項即升蓄勢",
                          "col": "var(--neutral)", "ids": cand_ids, "sub": cand_sub})

    y, mo, d = last.split("-")
    date_str = f"{y}/{int(mo)}/{int(d)}"
    grpmeta = {g: {"nm": GROUP_NM.get(g, g), "tag": GROUP_TAG.get(g, ""),
                   "short": GROUP_SHORT.get(g, GROUP_NM.get(g, g))} for g in GROUP_ORDER}
    html = open(TEMPLATE, encoding="utf-8").read()
    html = html.replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    html = html.replace("__TIERS_JSON__", json.dumps(tiers, ensure_ascii=False))
    html = html.replace("__GROUPS_JSON__", json.dumps(groups, ensure_ascii=False))
    html = html.replace("__GRPMETA_JSON__", json.dumps(grpmeta, ensure_ascii=False))
    html = html.replace("__GORDER_JSON__", json.dumps(GROUP_ORDER))
    html = html.replace("__WEIGHTS_JSON__", json.dumps(WEIGHTS))
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
    open(os.path.join(ARCHIVE, f"{last}.html"), "w", encoding="utf-8").write(html)
    open(os.path.join(ARCHIVE, "manifest.json"), "w", encoding="utf-8").write(json.dumps(dates))
    print(f"已重生 {OUT} — 資料日 {date_str},{len(data)} 檔,{len(tiers)} 個 tier;"
          f"快照 archive/{last}.html,manifest 共 {len(dates)} 日")


if __name__ == "__main__":
    main()
