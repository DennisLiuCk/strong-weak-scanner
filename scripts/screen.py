#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
screen.py — universe 季度體檢 + 候選提名。中立規則篩選,人只覆核「歸類」。
輸出 reports/screen_<今日>.md + console 摘要。

納入/剔除規則(與 README 治理章節同步):
  R1 業務歸屬:主營收 >50% 屬族群定義業務(人工判斷 → candidates.csv 的 group/biz 欄)
  R2 規模(遲滯防 churn):市值 ≥ CAP_IN 納入;「現有成員」跌破 CAP_OUT 才剔除
  R3 流動性:近 20 日中位成交值 ≥ LIQ_MIN(死魚股會讓族群內排名變雜訊)
  R4 上市滿 MIN_DAYS 個交易日(配合 60 日冷啟動視窗)

資料來源:
  現有 universe → 本地 db(0 API call)
  候選(config/candidates.csv)→ FinMind:TaiwanStockInfo(1 call,全市場名稱/產業)
  + 每檔近 150 日價量、近 10 日股本(2 calls/檔)

用法:  uv run --no-project python scripts/screen.py
節奏:  每季跑一次;變更 universe.csv 後跑回補,並記入 CHANGELOG.md
"""
import csv, datetime, os, sqlite3, statistics, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fetch_daily import api_get, get_token   # 重用抓取層(retry/限流退避一致)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
CANDIDATES = os.path.join(ROOT, "config", "candidates.csv")
REPORTS = os.path.join(ROOT, "reports")

# ── 規則旋鈕 ──────────────────────────────────────────────
CAP_IN   = 50e8    # 市值 ≥ 50 億 → 可納入
CAP_OUT  = 30e8    # 現有成員 < 30 億 → 建議剔除(30~50 億 = 緩衝帶,維持現狀)
LIQ_MIN  = 3e7     # 近 20 日中位成交值 ≥ 3,000 萬
MIN_DAYS = 60      # 上市至少 60 個交易日

# R1 業務歸屬關鍵字複檢(零 API,純字串比對):抓「服務型業務被歸到產品型族群」
# 的疏漏(2026-07-09 6525 捷敏-KY 案例——biz 寫「封測」卻歸 power)。命中僅供
# 人工覆核,不自動改 universe.csv。
BIZ_OSAT_KW     = ("封測", "OSAT", "IC測試")   # 封測/測試代工型業務 → 理應歸 packtest
BIZ_CONTRACT_KW = ("代工",)                     # 廣義代工 → packtest 或 semiequip 皆合理
BIZ_CHANNEL_KW  = ("通路",)                     # 純通路商需確認非主業(R1 前例:至上/崇越/華立)
# ──────────────────────────────────────────────────────────


def check_biz_grp(con):
    """R1 業務歸屬關鍵字一致性檢查:biz 含服務型/代工型關鍵字但族群歸類疑似不符時
    列出,供人工覆核(不自動改分類)。回傳 [(icon, stock_id, name, grp, biz, why), ...]。"""
    flags = []
    for r in con.execute("SELECT stock_id, name, grp, biz FROM universe ORDER BY stock_id"):
        biz = r["biz"] or ""
        if any(k in biz for k in BIZ_OSAT_KW) and r["grp"] != "packtest":
            flags.append(("🔴", r["stock_id"], r["name"], r["grp"], biz,
                          "biz 含封測/OSAT/IC測試關鍵字,但族群非 packtest"))
        elif any(k in biz for k in BIZ_CONTRACT_KW) and r["grp"] not in ("packtest", "semiequip"):
            flags.append(("🟡", r["stock_id"], r["name"], r["grp"], biz,
                          "biz 含代工關鍵字,但族群非 packtest/semiequip"))
        elif any(k in biz for k in BIZ_CHANNEL_KW):
            flags.append(("🟡", r["stock_id"], r["name"], r["grp"], biz,
                          "biz 含通路關鍵字,確認主業非純通路(同前例:至上/崇越/華立)"))
    return flags


def verdict_new(cap, liq, days):
    """候選:三規則全過才建議納入。回傳 (結論, 原因list)。"""
    fails = []
    if cap is None or cap < CAP_IN:
        fails.append(f"市值 {cap/1e8 if cap else 0:,.0f} 億 < {CAP_IN/1e8:.0f} 億")
    if liq is None or liq < LIQ_MIN:
        fails.append(f"20日中位成交值 {liq/1e6 if liq else 0:,.0f}M < {LIQ_MIN/1e6:.0f}M")
    if days < MIN_DAYS:
        fails.append(f"交易日 {days} < {MIN_DAYS}")
    return ("✅ 建議納入" if not fails else "❌ 不納入"), fails


def verdict_member(cap, liq):
    """現有成員:遲滯剔除線 + 流動性。"""
    if cap is not None and cap < CAP_OUT:
        return "🔻 建議剔除", [f"市值 {cap/1e8:,.0f} 億 < 剔除線 {CAP_OUT/1e8:.0f} 億"]
    fails = []
    if cap is not None and cap < CAP_IN:
        fails.append(f"市值 {cap/1e8:,.0f} 億(緩衝帶 {CAP_OUT/1e8:.0f}~{CAP_IN/1e8:.0f} 億)")
    if liq is not None and liq < LIQ_MIN:
        fails.append(f"20日中位成交值 {liq/1e6:,.0f}M 偏低")
    return ("👀 緩衝觀察" if fails else "✅ 續留"), fails


def main():
    today = datetime.date.today().isoformat()
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    L, w = [], None
    L.append(f"# Universe 體檢與候選提名 · {today}")
    L.append("")
    L.append(f"規則:納入 市值≥{CAP_IN/1e8:.0f}億 / 剔除 <{CAP_OUT/1e8:.0f}億(遲滯)"
             f";20日中位成交值 ≥{LIQ_MIN/1e6:.0f}M;上市 ≥{MIN_DAYS} 交易日。"
             "業務歸類為人工判斷項。")

    # ── A. 現有 universe 體檢(本地 db)──
    L.append("")
    L.append("## A. 現有成員體檢")
    L.append("")
    L.append("| 代號 | 名稱 | 族群 | 市值(億) | 20日中位成交值 | 結論 |")
    L.append("|---|---|---|---|---|---|")
    actions = []
    for r in con.execute("""SELECT u.stock_id, u.name, u.grp FROM universe u
                            JOIN groups g ON g.grp=u.grp ORDER BY g.ord, u.stock_id"""):
        sid = r["stock_id"]
        px = con.execute("""SELECT close, amount FROM price WHERE stock_id=?
                            ORDER BY date DESC LIMIT 20""", (sid,)).fetchall()
        sh = con.execute("""SELECT shares_issued FROM holding WHERE stock_id=? AND shares_issued
                            IS NOT NULL ORDER BY date DESC LIMIT 1""", (sid,)).fetchone()
        cap = px[0]["close"] * sh[0] if (px and sh and px[0]["close"]) else None
        amts = [p["amount"] for p in px if p["amount"]]
        liq = statistics.median(amts) if amts else None
        vd, why = verdict_member(cap, liq)
        if vd != "✅ 續留":
            actions.append(f"{vd} {sid} {r['name']}:{';'.join(why)}")
        L.append(f"| {sid} | {r['name']} | {r['grp']} | {cap/1e8:,.0f} | "
                 f"{liq/1e6:,.0f}M | {vd}{('(' + ';'.join(why) + ')') if why else ''} |")

    # ── A2. 業務歸屬關鍵字複檢(R1,零 API)──
    L.append("")
    L.append("## A2. 業務歸屬關鍵字一致性檢查(R1 免API複檢)")
    L.append("")
    biz_flags = check_biz_grp(con)
    if biz_flags:
        L.append("| | 代號 | 名稱 | 現族群 | biz | 提醒 |")
        L.append("|---|---|---|---|---|---|")
        for icon, sid, nm, grp, biz, why in biz_flags:
            L.append(f"| {icon} | {sid} | {nm} | {grp} | {biz} | {why} |")
            if icon == "🔴":
                actions.append(f"🔴 {sid} {nm}:{why}——建議覆核族群歸屬")
    else:
        L.append("(無關鍵字疑義)")

    # ── B. 候選體檢(FinMind)──
    L.append("")
    L.append("## B. 候選提名(config/candidates.csv)")
    L.append("")
    cands = list(csv.DictReader(open(CANDIDATES, encoding="utf-8")))
    token = get_token()
    info = {d["stock_id"]: d for d in api_get("TaiwanStockInfo", None, "", "", token)}
    start = (datetime.date.today() - datetime.timedelta(days=220)).isoformat()
    L.append("| 代號 | 名稱 | 擬歸類 | 產業別 | 市值(億) | 20日中位成交值 | 結論 |")
    L.append("|---|---|---|---|---|---|---|")
    for c in cands:
        sid = c["stock_id"].strip()
        meta = info.get(sid)
        if not meta:
            L.append(f"| {sid} | ?(TaiwanStockInfo 查無) | {c['group']} | - | - | - | ❌ 代號有誤或已下市 |")
            actions.append(f"❌ {sid}({c.get('note','')}):代號查無,請確認")
            continue
        px = api_get("TaiwanStockPrice", sid, start, today, token)
        hold = api_get("TaiwanStockShareholding", sid,
                       (datetime.date.today() - datetime.timedelta(days=15)).isoformat(), today, token)
        shares = next((d.get("NumberOfSharesIssued") for d in reversed(hold)
                       if d.get("NumberOfSharesIssued")), None)
        closes = [d for d in px if d.get("close")]
        cap = closes[-1]["close"] * shares if (closes and shares) else None
        amts = [d.get("Trading_money") for d in closes[-20:] if d.get("Trading_money")]
        liq = statistics.median(amts) if amts else None
        vd, why = verdict_new(cap, liq, len(closes))
        nm = meta.get("stock_name", c.get("note", ""))
        if vd.startswith("✅"):
            actions.append(f"✅ 納入 {sid} {nm} → {c['group']}({c['biz']};"
                           f"市值 {cap/1e8:,.0f} 億)")
        L.append(f"| {sid} | {nm} | {c['group']} | {meta.get('industry_category','-')} | "
                 f"{(cap/1e8 if cap else 0):,.0f} | {(liq/1e6 if liq else 0):,.0f}M | "
                 f"{vd}{('(' + ';'.join(why) + ')') if why else ''} |")

    L.append("")
    L.append("## C. 建議動作(覆核後執行:改 universe.csv → 回補 → 記 CHANGELOG)")
    L.append("")
    for a in (actions or ["(無)"]):
        L.append(f"- {a}")

    os.makedirs(REPORTS, exist_ok=True)
    path = os.path.join(REPORTS, f"screen_{today}.md")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L) + "\n")
    print(f"報告已寫入 {path}\n")
    for a in (actions or ["全部 ✅ 續留,無建議動作"]):
        print(" ", a)
    con.close()


if __name__ == "__main__":
    main()
