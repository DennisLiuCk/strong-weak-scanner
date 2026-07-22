#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
daily_brief.py — 盤後日常簡報(唯讀,不寫 db)。給「當日檢視/討論」的 session 一份現成議程:
資料鮮度 → 市場/族群雷達 → tier 變動(誰升誰降)→ 蓄勢候補變動 → 綜合分大變動 → 資料品質快檢。

用法:  git pull 之後  uv run --no-project python scripts/daily_brief.py
注意:  db 通常由 GitHub Actions 更新，也可由本地 runner 正式發布；不先 git pull 可能是在看舊資料。
"""
import datetime, os, sqlite3, sys
from snapshot_signals import MIN_DATA_DATE as OOS_SNAPSHOT_START

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
    for tbl in ("price", "inst", "margin", "holding", "sbl"):
        n = con.execute(f"SELECT COUNT(*) FROM {tbl} WHERE date=?", (last,)).fetchone()[0]
        if n < len(uni):
            issues.append(f"{tbl} 最新日僅 {n}/{len(uni)} 列")
    # 正式 OOS 只認 append-only 正式快照(可由 Actions 或本地 runner 發布)。表不存在/
    # 最新日未凍結都代表本日訊號
    # 日後只能當 restated history,不可進 OOS；快照步驟設計為 hard fail,此處再做事後守門。
    if last >= OOS_SNAPSHOT_START:
        have_oos = con.execute(
            "SELECT 1 FROM sqlite_master WHERE type='table' AND name='oos_snapshot_runs'").fetchone()
        if not have_oos:
            issues.append("OOS as-seen 快照表尚不存在——最新資料日不得計入 OOS")
        else:
            run_cols = {r[1] for r in con.execute("PRAGMA table_info(oos_snapshot_runs)")}
            official_where = "is_official=1" if "is_official" in run_cols else "source='github-actions'"
            run = con.execute(f"""SELECT snapshot_id FROM oos_snapshot_runs
                                  WHERE data_date=? AND {official_where}
                                  ORDER BY captured_at, snapshot_id LIMIT 1""", (last,)).fetchone()
            if not run:
                issues.append(f"OOS as-seen 快照缺 {last}——該日不得計入 OOS")
            else:
                n_snap = con.execute(
                    "SELECT COUNT(*) FROM oos_signal_snapshots WHERE snapshot_id=?", (run[0],)).fetchone()[0]
                if n_snap != len(uni):
                    issues.append(f"OOS as-seen 快照 {last} 僅 {n_snap}/{len(uni)} 檔")
    # TDCC 週快照鮮度:正常最大 age = 10 天(週一 23:47 完整場前);>10 = 漏抓一週(不可回補,永久洞)
    if con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tdcc_holding'").fetchone():
        td_last = con.execute("SELECT MAX(date) FROM tdcc_holding").fetchone()[0]
        if td_last and (today - datetime.date.fromisoformat(td_last)).days > 10:
            issues.append(f"tdcc_holding 最新快照 {td_last},疑漏抓一週(TDCC 不可回補)")
    else:
        issues.append("tdcc_holding 表不存在——fetch_tdcc 尚未跑過")
    # risk_flags 抓取健康度:TWSE/TPEx 四端點任一失敗只印 stderr、exit 0 不擋管線(綠燈看不出來),
    # 且當天名單整表重建、不保留前一天資料——用「前一有資料日 vs 今日」比對偵測「處置/注意」
    # 從非零掉到零(2026-07-09 實測:TWSE+TPEx 處置雙雙失敗,3 檔仍在官方列管期內的股票當天
    # 從名單消失,品質快檢原本測不出來)。
    if con.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='risk_flags'").fetchone():
        rf_dates = [r[0] for r in con.execute("SELECT DISTINCT date FROM risk_flags ORDER BY date")]
        if last not in rf_dates:
            issues.append(f"risk_flags 無 {last} 資料——TWSE/TPEx 處置+注意四端點疑似全數抓取失敗")
        else:
            idx = rf_dates.index(last)
            if idx > 0:
                prev_d = rf_dates[idx - 1]
                for kind in ("處置", "注意"):
                    n_today = con.execute("SELECT COUNT(*) FROM risk_flags WHERE date=? AND kind=?",
                                          (last, kind)).fetchone()[0]
                    n_prev = con.execute("SELECT COUNT(*) FROM risk_flags WHERE date=? AND kind=?",
                                         (prev_d, kind)).fetchone()[0]
                    if n_prev > 0 and n_today == 0:
                        issues.append(f"risk_flags「{kind}」從 {prev_d} 的 {n_prev} 筆掉到 {last} 的 0 筆,"
                                      f"疑似 TWSE/TPEx 端點抓取失敗——chip_health 一票否決可能漏判")
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
