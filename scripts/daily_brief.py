#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
daily_brief.py — 盤後日常簡報(唯讀,不寫 db)。給「當日檢視/討論」的 session 一份現成議程:
資料鮮度 → 市場/族群雷達 → tier 變動(誰升誰降)→ 蓄勢候補變動 → 綜合分大變動 → 資料品質快檢。

用法:  git pull 之後  uv run --no-project python scripts/daily_brief.py
注意:  db 由 GitHub Actions 每日更新並 commit——不先 git pull 就是在看舊資料。
"""
import datetime, os, sqlite3, sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")


def main():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    uni = {r["stock_id"]: (r["name"], r["grp"]) for r in con.execute("SELECT stock_id, name, grp FROM universe")}
    dates = [r[0] for r in con.execute("SELECT DISTINCT date FROM daily_scores ORDER BY date")]
    if len(dates) < 2:
        print("daily_scores 資料不足")
        return
    last, prev = dates[-1], dates[-2]

    # ── 1. 資料鮮度 ──
    today = datetime.date.today()
    lag = (today - datetime.date.fromisoformat(last)).days
    n_last = con.execute("SELECT COUNT(*) FROM daily_scores WHERE date=?", (last,)).fetchone()[0]
    print(f"■ 資料鮮度:最新評分日 {last}(距今 {lag} 天{';週末/假日屬正常' if lag <= 3 else ' ⚠ 偏舊——先確認 git pull 與 Actions'})")
    print(f"  覆蓋 {n_last}/{len(uni)} 檔" + ("" if n_last == len(uni) else " ⚠ 有缺——查 Actions log 的 stderr 警告"))

    # ── 2. 市場 + 族群雷達 ──
    mk = con.execute("""SELECT * FROM market_daily WHERE date<=? AND dd20 IS NOT NULL
                        ORDER BY date DESC LIMIT 1""", (last,)).fetchone()
    if mk:
        lagn = "" if mk["date"] == last else f"(指數至 {mk['date']})"
        print(f"\n■ 市場:報酬指數距20日高 {mk['dd20']*100:+.1f}%{lagn} → "
              f"{'⚠ 修正 regime' if mk['regime'] else '多頭/中性'}")
    print("■ 族群雷達:")
    for g in con.execute("SELECT * FROM group_metrics WHERE date=? ORDER BY grp", (last,)):
        def f(v, fmt):
            return fmt.format(v) if v is not None else "-"
        print(f"   {g['grp']:<9} {g['state']:<7} 修正日淨買{f(g['med_dip'], '{:+.2f}%')} "
              f"廣度{f(g['breadth_f'], '{:.0%}')} 動能vs全體{f(g['rel20'], '{:+.1%}')}")

    # ── 3. tier 變動(確認後 tier;含待確認)──
    cur = {r["stock_id"]: r for r in con.execute("SELECT * FROM daily_scores WHERE date=?", (last,))}
    pre = {r["stock_id"]: r for r in con.execute("SELECT * FROM daily_scores WHERE date=?", (prev,))}
    moves = [(pre[s]["tier"], cur[s]["tier"], s) for s in cur if s in pre and cur[s]["tier"] != pre[s]["tier"]]
    print(f"\n■ tier 變動({prev} → {last}):{len(moves)} 檔")
    for a, b, s in sorted(moves, key=lambda x: -cur[x[2]]["composite_s"]):
        print(f"   {s} {uni[s][0]:<5} [{uni[s][1]:<8}] {a} → {b}(綜 {cur[s]['composite_s']:+.1f})")
    pending = [(s, r["tier_raw"]) for s, r in cur.items()
               if r["tier_raw"] != r["tier"]]
    if pending:
        print("  待確認(明日同向即轉層):" + "、".join(
            f"{uni[s][0]}→{t}" for s, t in pending))

    # ── 4. 蓄勢候補變動 ──
    cp = {s: r["pending"] for s, r in cur.items() if r["pending"]}
    pp = {s: r["pending"] for s, r in pre.items() if r["pending"]}
    if cp or pp:
        print("\n■ 蓄勢候補:")
        for s in sorted(cp, key=lambda s: cp[s]):
            mark = "(新進)" if s not in pp else ("(缺項變動)" if pp[s] != cp[s] else "")
            print(f"   {s} {uni[s][0]:<5} ◇{cp[s]}{mark}")
        for s in pp:
            if s not in cp:
                if "蓄勢" in cur[s]["tier"]:
                    why = "升蓄勢!"
                elif "蓄勢" in cur[s]["tier_raw"]:
                    why = "升蓄勢待確認(明日同向即轉層)"
                else:
                    why = f"退出(現 {cur[s]['tier']})"
                print(f"   {s} {uni[s][0]:<5} 離開候補 → {why}")

    # ── 5. 綜合分大變動(討論素材)──
    delta = sorted(((cur[s]["composite_s"] - pre[s]["composite_s"], s) for s in cur if s in pre),
                   key=lambda x: -abs(x[0]))[:5]
    print("\n■ 綜合分變動 Top5:")
    for d, s in delta:
        print(f"   {s} {uni[s][0]:<5} {pre[s]['composite_s']:+.1f} → {cur[s]['composite_s']:+.1f}({d:+.1f})")

    # ── 6. 資料品質快檢 ──
    issues = []
    for tbl in ("price", "inst", "margin", "holding"):
        n = con.execute(f"SELECT COUNT(*) FROM {tbl} WHERE date=?", (last,)).fetchone()[0]
        if n < len(uni):
            issues.append(f"{tbl} 最新日僅 {n}/{len(uni)} 列")
    miss_adj = con.execute("""SELECT COUNT(*) FROM price p JOIN universe u USING(stock_id)
                              LEFT JOIN price_adj a ON a.date=p.date AND a.stock_id=p.stock_id
                              WHERE p.date=? AND p.close IS NOT NULL AND a.close IS NULL""",
                           (last,)).fetchone()[0]
    if miss_adj:
        issues.append(f"price_adj 最新日缺 {miss_adj} 列")
    jumps = con.execute("""SELECT stock_id, ret1 FROM daily_metrics
                           WHERE date=? AND ret1 IS NOT NULL AND ABS(ret1) > 0.105""", (last,)).fetchall()
    for j in jumps:
        issues.append(f"{j['stock_id']} {uni.get(j['stock_id'], ('?',))[0]} 還原後日變動 "
                      f"{j['ret1']*100:+.1f}%(>漲跌停,疑缺除權息/減資事件)")
    print("\n■ 資料品質:" + ("無異常" if not issues else ""))
    for i in issues:
        print(f"   ⚠ {i}")
    con.close()


if __name__ == "__main__":
    main()
