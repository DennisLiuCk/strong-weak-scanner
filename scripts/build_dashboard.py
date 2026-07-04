#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_dashboard.py — 從 SQLite(daily_scores + daily_metrics)自動重生儀表板 HTML。
吃 scripts/dashboard_template.html(CSS/JS 外殼),只注入資料 → dashboard.html。
零第三方依賴。用法:  uv run --no-project python scripts/build_dashboard.py
"""
import json, os, sqlite3, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
TEMPLATE = os.path.join(ROOT, "scripts", "dashboard_template.html")
OUT = os.path.join(ROOT, "dashboard.html")

GROUP_ORDER = ["passive", "power", "packtest"]
TIER_ORDER = ["真強", "蓄勢·外資佈局", "強但過熱", "潛在/中性", "真弱", "真弱·陷阱"]
TIER_VT = {"真強": 2, "蓄勢·外資佈局": 2, "強但過熱": 1, "潛在/中性": 0, "真弱": -2, "真弱·陷阱": -2}
TIER_COL = {"真強": "var(--strong)", "蓄勢·外資佈局": "var(--neutral)", "強但過熱": "var(--warn-line)",
            "潛在/中性": "var(--neutral)", "真弱": "var(--weak)", "真弱·陷阱": "var(--weak)"}
TIER_DESC = {"真強": "價強且籌碼扎實", "蓄勢·外資佈局": "外資/投信吃貨,價未發動",
             "強但過熱": "價強但散戶滿載,別追高", "潛在/中性": "訊號分歧,觀察",
             "真弱": "價籌俱弱", "真弱·陷阱": "外資出、散戶接"}

def pct(x, signed=False):
    if x is None:
        return "-"
    return f"{x*100:+.1f}%" if signed else f"{x*100:.1f}%"

# 每個元素:score → 理由文字
R_PRICE = {2: "在波段高檔/創新高", 1: "接近波段高檔", 0: "距高中等、區間整理", -1: "明顯拉回", -2: "深跌、族群落後"}
R_FOREIGN = {2: "外資強力吃貨", 1: "外資淨買", 0: "外資中性", -1: "外資調節", -2: "外資倒貨/大幅撤出"}
R_TRUST = {2: "投信強力認養", 1: "投信淨買", 0: "投信中性/未參與", -1: "投信調節", -2: "投信大幅賣超"}
R_MARGIN = {2: "散戶大幅洗清", 1: "融資減、籌碼漸乾淨", 0: "融資平穩", -1: "融資增、散戶追高", -2: "散戶槓桿滿載、賣壓重"}
# 精簡標籤(給 vsub 用)
SALIENT = {("price", 2): "價高檔", ("price", -2): "價落後", ("foreign", 2): "外資吃貨", ("foreign", -2): "外資倒貨",
           ("trust", 2): "投信認養", ("trust", -2): "投信賣超", ("margin", 2): "散戶洗清", ("margin", -2): "散戶滿載"}


def build_cells(sc, m):
    cells = []
    # ① 價
    d60 = m["dist_hi60"]
    val = "新高" if (d60 is not None and d60 >= -0.005) else pct(d60)
    detail = f"距60日高 {pct(d60)};距20日高 {pct(m['dist_hi20'])};前一日 {pct(m['ret1'], True)}"
    cells.append([sc["s_price"], val, detail, R_PRICE[sc["s_price"]]])
    # ② 量
    t = m["turnover_pct"]
    if t is not None and t >= 20:
        rv, warn = "周轉率過高、當沖過熱", 1
    elif sc["s_vol"] == 1:
        rv, warn = "量能健康活絡", 0
    elif t is not None and t < 1:
        rv, warn = "量縮、人氣不足", 0
    else:
        rv, warn = "量能中等", 0
    c = [sc["s_vol"], pct(t) if t is not None else "-", f"周轉率 {pct(t)}(當日量/發行股數)", rv]
    if warn:
        c.append(1)
    cells.append(c)
    # ③ 外資
    fc = m["fpct_chg20"]
    val = f"{fc:+.1f}pp" if fc is not None else "-"
    detail = f"外資持股 {m['foreign_pct']:.1f}%;20日變化 {fc:+.2f}pp" if fc is not None else "外資持股資料不足"
    cells.append([sc["s_foreign"], val, detail, R_FOREIGN[sc["s_foreign"]]])
    # ④ 投信
    t5 = m["trust5"] or 0
    cells.append([sc["s_trust"], f"{t5:+,}張", f"投信近5日淨額 {t5:+,}張", R_TRUST[sc["s_trust"]]])
    # ⑤ 融資券
    u = m["margin_util_pct"]
    detail = f"散戶水位 {pct(u)};10日融資 {pct(m['margin_chg10'], True)};券資比 {(m['short_margin_ratio'] or 0):.1f}%"
    c = [sc["s_margin"], pct(u) if u is not None else "-", detail, R_MARGIN[sc["s_margin"]]]
    if u is not None and u >= 9:
        c.append(1)
    cells.append(c)
    return cells


def verdict(sc):
    tier = sc["tier"]
    comp = sc["composite"]
    keys = [("price", sc["s_price"]), ("vol", sc["s_vol"]), ("foreign", sc["s_foreign"]),
            ("trust", sc["s_trust"]), ("margin", sc["s_margin"])]
    labels = [SALIENT[k] for k in keys if k in SALIENT]
    vsub = " · ".join(labels[:2]) if labels else f"綜合 {comp:+.1f}"
    drivers = []
    for name, ref in [("外資", "s_foreign"), ("投信", "s_trust"), ("融資", "s_margin"), ("價", "s_price")]:
        s = sc[ref]
        if abs(s) >= 2:
            drivers.append({"外資": R_FOREIGN, "投信": R_TRUST, "融資": R_MARGIN, "價": R_PRICE}[name][s])
    vr = f"綜合 {comp:+.1f}(價{sc['s_price']:+d} 量{sc['s_vol']:+d} 外{sc['s_foreign']:+d} " \
         f"投{sc['s_trust']:+d} 融{sc['s_margin']:+d})。" + ("；".join(drivers) if drivers else "訊號分歧")
    return TIER_VT.get(tier, 0), tier, vsub, vr, int(sc["warn"])


def main():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    last = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    if not last:
        print("daily_scores 沒有資料,請先跑 score.py")
        return
    rows = con.execute("""SELECT u.stock_id, u.name, u.grp, sc.*, m.*
        FROM daily_scores sc JOIN universe u USING(stock_id) JOIN daily_metrics m USING(date, stock_id)
        WHERE sc.date=?""", (last,)).fetchall()
    con.close()

    data, tiers_map = [], {}
    for r in rows:
        vt, tier, vsub, vr, warn = verdict(r)
        obj = {"g": r["grp"], "id": r["stock_id"], "nm": r["name"], "vt": vt,
               "vlabel": tier, "vsub": vsub, "vr": vr, "cells": build_cells(r, r)}
        if warn:
            obj["warn"] = True
        obj["_comp"] = r["composite"]
        data.append(obj)
        tiers_map.setdefault(tier, []).append((r["composite"], r["stock_id"]))

    # 排序:族群順序,族群內綜合分數由高到低
    data.sort(key=lambda o: (GROUP_ORDER.index(o["g"]), -o["_comp"]))
    for o in data:
        del o["_comp"]

    tiers = []
    for t in TIER_ORDER:
        if t in tiers_map:
            ids = [sid for _, sid in sorted(tiers_map[t], reverse=True)]
            tiers.append({"t": t, "d": TIER_DESC.get(t, ""), "col": TIER_COL.get(t, "var(--neutral)"), "ids": ids})

    y, mo, d = last.split("-")
    date_str = f"{y}/{int(mo)}/{int(d)}"
    html = open(TEMPLATE, encoding="utf-8").read()
    html = html.replace("__DATA_JSON__", json.dumps(data, ensure_ascii=False))
    html = html.replace("__TIERS_JSON__", json.dumps(tiers, ensure_ascii=False))
    html = html.replace("__DATE__", date_str)
    open(OUT, "w", encoding="utf-8").write(html)
    print(f"已重生 {OUT} — 資料日 {date_str},{len(data)} 檔,{len(tiers)} 個 tier")


if __name__ == "__main__":
    main()
