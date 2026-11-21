#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rank_change.py — 族群內名次變動解釋(唯讀,db_ro)。

比較最近兩個已完成交易週「最後交易日」的首次正式快照,說明某檔股票在族群內
升名或掉名的原因。名次 = 族群內 composite_s 由高到低的平均序位(同 score.average_ranks)。

選週規則(台北時間 + market 交易日曆):
  * 週五在 market 中 → 週五是交易日;首次正式快照在 as-of 前已擷取就採用本週。
    尚未到發布期限(資料日次日台北 09:00,同 snapshot_signals.publication_timing)
    視為本週未完成,改用前兩週;已過期限仍無快照 → 明示錯誤,不默默退回。
  * 週五不在 market → 期限前視為未完成;期限後明示「無法確認是休市還是抓取失敗」。
    repo 沒有獨立的交易所休市依據;「週五缺、週一有」也可能是週五抓取失敗、週一恢復,
    因此不以之後出現的交易日推定休市,也不退回該週前一交易日。
  * 交易日曆取 as-of 當下可見者(point-in-time):早於 as-of 台北日期的 market 日期;
    as-of 當日的日期須有已發布的首次正式快照,或 market_provenance.checked_at ≤ as-of。
    重播歷史 as-of 時,之後才出現的交易日不會被看見。
  * 平滑窗口:交易日有正式快照但缺該股列時,只有 trading_status/suspension_evidence
    可嚴格驗證的零成交/停牌才略過;原因不明的缺列標為窗口不完整。
  * 同日多份正式快照沿用 evidence_status.first_official_runs(首次正式發布);
    首次快照為空或不完整時明示錯誤,不以後來修正版取代。

用法(repo 根目錄):
  python scripts/rank_change.py                                   # 自動選週,列出所有名次變動
  python scripts/rank_change.py --stock 3443 --output tmp/rank_change_3443.txt
  python scripts/rank_change.py 2026-11-13 2026-11-20 --stock 3443
  python scripts/rank_change.py --run-sql "SELECT ..."             # 重跑報告引用的查詢
中文 stdout 在 Windows console 可能亂碼;建議用 --output(UTF-8、LF)。
"""
import argparse
import datetime as dt
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import db_ro
import evidence_status
import trading_status

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))
ELEMENTS = ["price", "resil", "vol", "foreign", "trust", "dip", "margin"]
EL_NAME = {"price": "20日相對強弱", "resil": "修正日抗跌", "vol": "量能", "foreign": "外資",
           "trust": "投信", "dip": "逆勢買超", "margin": "融資"}
EPS = 1e-9
SMOOTH_N = 3

Q_RUNS = ("SELECT snapshot_id, data_date, captured_at, is_official FROM oos_snapshot_runs "
          "WHERE data_date='{d}' AND is_official=1 ORDER BY captured_at, snapshot_id")
Q_ROWS = ("SELECT stock_id, grp, composite, composite_s, tier, "
          + ", ".join("s_" + e for e in ELEMENTS)
          + " FROM oos_signal_snapshots WHERE snapshot_id='{sid}' ORDER BY grp, composite_s DESC")
Q_WINDOW = ("SELECT date, snapshot_id, composite, composite_s FROM oos_signal_snapshots "
            "WHERE stock_id='{stock}' AND snapshot_id IN ({sids}) ORDER BY date DESC")
Q_MARKET = "SELECT date FROM market WHERE date BETWEEN '{d0}' AND '{d1}' ORDER BY date"


class SelectionError(RuntimeError):
    """應有資料卻無法依規則選出快照;呼叫端必須明示,不得默默改用其他日期。"""


# ── 選週 ──────────────────────────────────────────────────────────
def _aware(value):
    moment = dt.datetime.fromisoformat(value) if isinstance(value, str) else value
    if moment.tzinfo is None:
        raise ValueError(f"時間必須帶時區:{value}")
    return moment


def publish_deadline(day):
    """資料日次日台北 09:00;與 snapshot_signals.publication_timing 的 OOS 期限一致。"""
    return dt.datetime.combine(dt.date.fromisoformat(day) + dt.timedelta(days=1),
                               dt.time(9), tzinfo=TAIPEI_TZ)


def published_first_runs(con, as_of):
    """首次正式發布(evidence_status 規則);as-of 之後才擷取者視為尚未發布。"""
    return {d: r for d, r in evidence_status.first_official_runs(con).items()
            if _aware(r["captured_at"]) <= as_of}


def _utc(text):
    moment = dt.datetime.fromisoformat(text.replace(" ", "T"))
    return moment if moment.tzinfo else moment.replace(tzinfo=dt.timezone.utc)


def trading_calendar(con, as_of=None, firsts=None):
    """market 交易日;給 as_of 時只回傳 as-of 當下已可見的日期(見模組說明)。"""
    dates = [r[0] for r in con.execute("SELECT date FROM market ORDER BY date")]
    if as_of is None:
        return dates
    today = str(_aware(as_of).astimezone(TAIPEI_TZ).date())
    checked = {}
    if con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='market_provenance'").fetchone():
        checked = {d: c for d, c in con.execute(
            "SELECT date, checked_at FROM market_provenance WHERE date=?", (today,))}
    seen_today = today in (firsts or {}) or (today in checked and checked[today]
                                             and _utc(checked[today]) <= as_of)
    return [d for d in dates if d < today or (d == today and seen_today)]


def require_complete(con, run):
    n = con.execute("SELECT COUNT(*) FROM oos_signal_snapshots WHERE snapshot_id=?",
                    (run["snapshot_id"],)).fetchone()[0]
    if not n or n != run["stock_count"]:
        raise SelectionError(f"{run['data_date']} 首次正式快照 {run['snapshot_id']} 只有 {n}/"
                             f"{run['stock_count']} 列;不以後來修正版取代")


def week_end(con, monday, as_of, cal, firsts):
    """回傳 {'status': complete|pending, 'date', 'run', 'note'};應有卻缺或無法確認則 raise。"""
    sunday, friday = monday + dt.timedelta(days=6), str(monday + dt.timedelta(days=4))
    days = [d for d in cal if str(monday) <= d <= str(sunday)]
    note = None
    if friday not in days:
        if as_of < publish_deadline(friday):
            return {"status": "pending",
                    "note": f"週五 {friday} 交易日曆與正式快照尚未發布(期限 {publish_deadline(friday).isoformat()})"}
        later = [d for d in cal if d > friday]
        seen = f"market 其後有交易日 {later[0]},但這不能區分休市與週五抓取失敗後恢復" if later \
            else "market 也沒有之後的交易日"
        raise SelectionError(
            f"週五 {friday} 已過發布期限 {publish_deadline(friday).isoformat()},但 market 沒有該日;"
            f"{seen}。repo 沒有獨立的休市依據,無法確認是休市還是抓取失敗,不退回該週前一交易日")
    last = max(days)
    run = firsts.get(last)
    if run is None:
        if as_of < publish_deadline(last):
            return {"status": "pending", "note": f"{last} 正式快照尚未發布(期限 {publish_deadline(last).isoformat()})"}
        raise SelectionError(f"{last} 是交易日且已過發布期限 {publish_deadline(last).isoformat()},"
                             f"但沒有正式快照")
    require_complete(con, run)
    return {"status": "complete", "date": last, "run": run, "note": note}


def select_weeks(con, as_of, n=2, max_weeks=60):
    as_of = _aware(as_of)
    firsts = published_first_runs(con, as_of)
    cal = trading_calendar(con, as_of, firsts)
    monday = as_of.astimezone(TAIPEI_TZ).date()
    monday -= dt.timedelta(days=monday.weekday())
    picked, notes = [], []
    for _ in range(max_weeks):
        if not cal or str(monday + dt.timedelta(days=6)) < cal[0]:
            break
        w = week_end(con, monday, as_of, cal, firsts)
        if w["status"] == "complete":
            picked.append(w)
            if w["note"]:
                notes.append(w["note"])
            if len(picked) == n:
                return list(reversed(picked)), notes
        else:
            notes.append(f"略過 {monday} 當週:{w['note']}")
        monday -= dt.timedelta(days=7)
    raise SelectionError(f"找不到 {n} 個已完成交易週")


def run_build(run):
    """平滑可比性用的建置指紋:universe 與評分規格;舊快照缺欄位時為 None。"""
    keys = run.keys()
    quality = json.loads(run["quality_json"] or "{}") if "quality_json" in keys else {}
    return {"universe_hash": run["universe_hash"] if "universe_hash" in keys else None,
            "score_spec_sha": quality.get("score_spec_sha")}


def smoothing_window(con, firsts, cal, stock, day, n=SMOOTH_N):
    """composite_s 的平滑窗口:該股最近 n 個「不同」交易日的首次正式快照 composite。
    每格 status:ok;no_trade(可嚴格驗證的零成交/停牌,不評分、不佔窗口);
    no_snapshot(交易日缺正式快照)與 missing_row(快照缺該股列且原因不明)→ 窗口不完整。
    每格附 build 指紋;各快照凍結的是自己那次建置的 composite,不同建置不可混算。"""
    slots, used = [], 0
    for d in reversed([x for x in cal if x <= day]):
        if used == n:
            break
        run = firsts.get(d)
        slot = {"date": d, "snapshot_id": run["snapshot_id"] if run else None,
                "composite": None, "composite_s": None}
        if run is None:
            slot["status"] = "no_snapshot"
        else:
            row = con.execute("SELECT composite, composite_s FROM oos_signal_snapshots "
                              "WHERE snapshot_id=? AND stock_id=?", (run["snapshot_id"], stock)).fetchone()
            if row is not None:
                slot.update(status="ok", build=run_build(run),
                            composite=row["composite"], composite_s=row["composite_s"])
            elif stock in trading_status.verified_exclusion_ids(con, d, [stock]):
                slot["status"] = "no_trade"
            else:
                slot["status"] = "missing_row"
        slots.append(slot)
        used += slot["status"] != "no_trade"
    if len({s["date"] for s in slots}) != len(slots):
        raise AssertionError("平滑窗口出現重複交易日")
    return slots


# ── 名次拆解(純函式) ───────────────────────────────────────────────
def position_value(peer_cs, target_cs):
    """對目標名次的貢獻:排在前面 1、同分 0.5、後面 0。名次 = 1 + Σ貢獻。"""
    if peer_cs > target_cs + EPS:
        return 1.0
    if abs(peer_cs - target_cs) <= EPS:
        return 0.5
    return 0.0


def rank_group(rows):
    """rows: {stock_id: row}(同族群)。composite_s 缺值不排名。
    回傳 {stock_id: (rank, n_ranked, n_tied_others)};rank 是整數時仍可能同分。"""
    ranked = {s: r for s, r in rows.items() if r.get("composite_s") is not None}
    out = {}
    for s, r in ranked.items():
        vals = [position_value(o["composite_s"], r["composite_s"]) for k, o in ranked.items() if k != s]
        out[s] = (1 + sum(vals), len(ranked), sum(1 for v in vals if v == 0.5))
    return out


def unranked_reason(stock, snap_all, grp):
    r = snap_all.get(stock)
    if r is None:
        return "absent", "快照無此股"
    if r["grp"] != grp:
        return "moved", f"在族群 {r['grp']}"
    return "null", "composite_s 缺值"


def explain(A_all, B_all, stock):
    tA, tB = A_all.get(stock), B_all.get(stock)
    if tA is None or tB is None or tA.get("composite_s") is None or tB.get("composite_s") is None:
        raise ValueError(f"{stock} 兩期都必須有快照且 composite_s 非空")
    if tA["grp"] != tB["grp"]:
        raise ValueError(f"{stock} 換族群 {tA['grp']}→{tB['grp']},族群內名次不可比")
    g = tA["grp"]
    gA = {s: r for s, r in A_all.items() if r["grp"] == g}
    gB = {s: r for s, r in B_all.items() if r["grp"] == g}
    rkA, rkB = rank_group(gA), rank_group(gB)
    others = {s for s in set(A_all) | set(B_all) if s != stock}
    peers = sorted(s for s in others if s in gA or s in gB)
    cats = {k: [] for k in ("overtook_target", "overtaken_by_target", "tie_change", "unchanged",
                            "left", "joined", "unranked_both")}
    rows, delta = [], 0.0
    for p in peers:
        vA = position_value(gA[p]["composite_s"], tA["composite_s"]) if p in rkA else None
        vB = position_value(gB[p]["composite_s"], tB["composite_s"]) if p in rkB else None
        whyA = None if p in rkA else unranked_reason(p, A_all, g)
        whyB = None if p in rkB else unranked_reason(p, B_all, g)
        delta += (vB or 0) - (vA or 0)
        if vA is not None and vB is not None:
            cat = ("overtook_target" if (vA, vB) == (0, 1) else
                   "overtaken_by_target" if (vA, vB) == (1, 0) else
                   "tie_change" if vA != vB else "unchanged")
        else:
            cat = "left" if vA is not None else "joined" if vB is not None else "unranked_both"
        cats[cat].append(p)
        rows.append(dict(stock=p, vA=vA, vB=vB, whyA=whyA, whyB=whyB, cat=cat,
                         csA=gA[p]["composite_s"] if vA is not None else None,
                         csB=gB[p]["composite_s"] if vB is not None else None,
                         rankA=rkA[p][0] if p in rkA else None, rankB=rkB[p][0] if p in rkB else None))
    rA, nA, tieA = rkA[stock]
    rB, nB, tieB = rkB[stock]
    if abs((rB - rA) - delta) > EPS:
        raise AssertionError("名次差必須等於同業貢獻加總")
    elements = None
    if all(("s_" + e) in tA and tA["s_" + e] is not None and tB["s_" + e] is not None for e in ELEMENTS):
        from score import WEIGHTS
        elements = [(e, tA["s_" + e], tB["s_" + e], round(WEIGHTS[e] * (tB["s_" + e] - tA["s_" + e]), 2))
                    for e in ELEMENTS]
    return dict(stock=stock, grp=g, rankA=rA, rankB=rB, nA=nA, nB=nB, tieA=tieA, tieB=tieB,
                csA=tA["composite_s"], csB=tB["composite_s"], compA=tA.get("composite"),
                compB=tB.get("composite"), peers=rows, cats=cats, elements=elements)


def fmt_rank(rank, n, tied):
    return f"{rank:g}/{n}" + (f"(與 {tied} 檔同分,共 {tied + 1} 檔)" if tied else "")


def _side_counts(rows, key):
    c = {1.0: 0, 0.5: 0, 0.0: 0}
    for r in rows:
        c[r[key]] += 1
    return f"前 {c[1.0]:g}、同分 {c[0.5]:g}、後 {c[0.0]:g}"


def _reason_counts(rows, key):
    c = {"absent": 0, "moved": 0, "null": 0}
    for r in rows:
        c[r[key][0]] += 1
    return f"快照無此股 {c['absent']}、轉族群 {c['moved']}、composite_s 缺值 {c['null']}"


SLOT_LABEL = {"no_snapshot": "缺正式快照", "missing_row": "快照缺該股列(原因不明)",
              "no_trade": "已確認零成交/停牌(不佔窗口)"}


def window_mismatch(win, mean):
    """窗口不能當作端點 composite_s 平滑輸入的原因;空串列=可驗證。"""
    why = []
    end = win[0].get("build") or {}
    for key, label in (("universe_hash", "universe"), ("score_spec_sha", "評分規格")):
        vals = [(s.get("build") or {}).get(key) for s in win]
        if None in vals:
            why.append(f"部分快照缺 {label} 指紋")
        elif any(v != end.get(key) for v in vals):
            diff = [s["date"] for s, v in zip(win, vals) if v != end.get(key)]
            why.append(f"{label} 與端點不同({', '.join(sorted(diff))})")
    if win[0]["composite_s"] is None or abs(mean - win[0]["composite_s"]) >= 0.006:
        why.append("平均不等於快照 composite_s")
    return why


def render(ex, dA, dB, cite=None, window=None):
    cite = cite or {}
    c = lambda k: f" [{cite[k]}]" if k in cite else ""
    K, byp = ex["cats"], {r["stock"]: r for r in ex["peers"]}
    move = ex["rankA"] - ex["rankB"]
    verb = (f"名次上升 {move:g} 席" if move > 0 else f"名次下降 {-move:g} 席" if move < 0 else "名次不變")
    left = [byp[p] for p in K["left"]]
    joined = [byp[p] for p in K["joined"]]
    L = [f"== {ex['stock']} 族群 {ex['grp']}:{dA} {fmt_rank(ex['rankA'], ex['nA'], ex['tieA'])} → "
         f"{dB} {fmt_rank(ex['rankB'], ex['nB'], ex['tieB'])}{c('rows')}",
         f"結論:{verb};實際超越 {len(K['overtaken_by_target'])} 檔、被超越 {len(K['overtook_target'])} 檔;"
         f"同分狀態改變 {len(K['tie_change'])} 檔;"
         f"{len(left)} 檔未列入本週族群排名" + (f"(上週{_side_counts(left, 'vA')};{_reason_counts(left, 'whyB')})" if left else "")
         + f";{len(joined)} 檔本週新列入族群排名"
         + (f"(本週{_side_counts(joined, 'vB')};上週{_reason_counts(joined, 'whyA')})" if joined else "") + "。",
         f"族群可排名檔數 {ex['nA']} → {ex['nB']}{c('rows')}"]
    labels = [("overtaken_by_target", "被目標超越(原在前→現在後)"), ("overtook_target", "超越目標(原在後→現在前)"),
              ("tie_change", "同分狀態改變"), ("left", "未列入本週族群排名"), ("joined", "本週新列入族群排名"),
              ("unranked_both", "兩期皆未列入排名")]
    for k, lab in labels:
        for p in K[k]:
            r = byp[p]
            a = f"{r['rankA']:g} cs={r['csA']:+.2f}" if r["rankA"] is not None else f"—({r['whyA'][1]})"
            b = f"{r['rankB']:g} cs={r['csB']:+.2f}" if r["rankB"] is not None else f"—({r['whyB'][1]})"
            L.append(f"  [{lab}] {p}: {dA} {a} → {dB} {b}")
    for p in K["unchanged"]:
        r = byp[p]
        side = {1.0: "前", 0.5: "同分", 0.0: "後"}[r["vA"]]
        L.append(f"  [相對位置不變:{side}] {p}: {r['rankA']:g} cs={r['csA']:+.2f} → {r['rankB']:g} cs={r['csB']:+.2f}")
    if ex["compA"] is not None and ex["compB"] is not None:
        d1 = round(ex["compB"] - ex["compA"], 2)
        L.append(f"(1) 當日分數 composite:{ex['compA']:+.2f} → {ex['compB']:+.2f},變動 {d1:+.2f}{c('rows')}")
        if ex["elements"]:
            tot = round(sum(w for *_, w in ex["elements"]), 2)
            for e, a, b, w in ex["elements"]:
                if a != b:
                    L.append(f"    {EL_NAME[e]}: {a:+d} → {b:+d},權重後 {w:+.2f}")
            L.append(f"    元素加總 {tot:+.2f}(與當日分數變動{'一致' if abs(tot - d1) < 0.005 else '不一致!'})")
    L.append(f"(2) 三日平滑排名分數 composite_s:{ex['csA']:+.2f} → {ex['csB']:+.2f},"
             f"變動 {round(ex['csB'] - ex['csA'], 2):+.2f}{c('rows')}  ← 名次只依這個分數")
    for tag, d, all_slots in zip("AB", (dA, dB), window or ()):
        win = [s for s in all_slots if s["status"] == "ok"]
        parts = ", ".join(f"{s['date']} " + (f"{s['composite']:+.2f}" if s["status"] == "ok" else SLOT_LABEL[s["status"]])
                          for s in reversed(all_slots))
        if len(win) != len([s for s in all_slots if s["status"] != "no_trade"]) or not win:
            L.append(f"    {d} 窗口{c('win' + tag)}: {parts} → 不完整,無法以快照驗算")
            continue
        mean = round(sum(s["composite"] for s in win) / len(win), 2)
        why = window_mismatch(win, mean)
        if why:
            L.append(f"    {d} 先前發布觀測值{c('win' + tag)}: {parts}(平均 {mean:+.2f},快照 composite_s "
                     f"{win[0]['composite_s']:+.2f})→ {';'.join(why)};原始平滑輸入無法以快照驗證")
            continue
        L.append(f"    {d} 窗口{c('win' + tag)}: {parts} → {len(win)} 個不同交易日平均 {mean:+.2f}"
                 f"(與快照 composite_s {win[0]['composite_s']:+.2f} 一致,建置指紋相同)")
    return "\n".join(L)


# ── CLI ───────────────────────────────────────────────────────────
def _load(con, sid):
    return {r["stock_id"]: dict(r) for r in con.execute(Q_ROWS.format(sid=sid))}


def build_report(con, as_of, dates=None, stock=None):
    as_of = _aware(as_of)
    firsts = published_first_runs(con, as_of)
    cal = trading_calendar(con, as_of, firsts)
    out = [f"as-of {as_of.astimezone(TAIPEI_TZ).isoformat()}(台北)"]
    if dates:
        runs = []
        for d in dates:
            if d not in firsts:
                raise SelectionError(f"{d} 在 as-of 前沒有首次正式快照")
            require_complete(con, firsts[d])
            runs.append(firsts[d])
        notes = []
    else:
        picked, notes = select_weeks(con, as_of)
        runs = [w["run"] for w in picked]
    (dA, rA), (dB, rB) = [(r["data_date"], r) for r in runs]
    for tag, r in (("A", rA), ("B", rB)):
        out.append(f"{tag}={r['data_date']} {r['snapshot_id']} captured_at={r['captured_at']} "
                   f"oos_eligible={evidence_status.oos_eligible(r)} [Q1{tag.lower()}]")
    out += [f"選週說明:{n}" for n in notes]
    A, B = _load(con, rA["snapshot_id"]), _load(con, rB["snapshot_id"])
    out.append(f"成員:只在A {sorted(set(A) - set(B))} 只在B {sorted(set(B) - set(A))} "
               f"換族群 {[(s, A[s]['grp'], B[s]['grp']) for s in sorted(A) if s in B and A[s]['grp'] != B[s]['grp']]} [Q2]")
    for tag, S in (("A", A), ("B", B)):
        out.append(f"{tag} composite_s 缺值:{sorted(s for s, r in S.items() if r['composite_s'] is None)} [Q2]")
    queries = [("Q1a", Q_RUNS.format(d=dA)), ("Q1b", Q_RUNS.format(d=dB)),
               ("Q2", Q_ROWS.format(sid=rA["snapshot_id"])), ("Q2", Q_ROWS.format(sid=rB["snapshot_id"]))]
    if not stock:
        for g in sorted({r["grp"] for r in B.values()}):
            ra = rank_group({s: r for s, r in A.items() if r["grp"] == g})
            rb = rank_group({s: r for s, r in B.items() if r["grp"] == g})
            for s in sorted(rb, key=lambda s: rb[s][0]):
                if s in ra and ra[s][0] != rb[s][0]:
                    out.append(f"  {g:<11} {s} {fmt_rank(*ra[s])} → {fmt_rank(*rb[s])}")
    else:
        ex = explain(A, B, stock)
        win = [smoothing_window(con, firsts, cal, stock, d) for d in (dA, dB)]
        out.append("")
        out.append(render(ex, dA, dB, {"rows": "Q2", "winA": "Q3a", "winB": "Q3b"}, win))
        for tag, w in zip("ab", win):
            sids = ",".join(f"'{s['snapshot_id']}'" for s in w if s["snapshot_id"])
            queries.append((f"Q3{tag}", Q_WINDOW.format(stock=stock, sids=sids)))
            queries.append((f"Q4{tag}", Q_MARKET.format(d0=w[-1]["date"], d1=w[0]["date"])))
    out.append("\n可重跑查詢(python scripts/rank_change.py --run-sql \"<SQL>\";Q1 第一列=首次正式發布):")
    out += [f"  {k} {sql}" for k, sql in queries]
    return "\n".join(out)


def _same_file(out, db):
    for target in (db, db + "-wal", db + "-shm", db + "-journal"):
        if os.path.realpath(out) == os.path.realpath(target):
            return True
        if os.path.exists(out) and os.path.exists(target) and os.path.samefile(out, target):
            return True
    return False


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dates", nargs="*", help="兩個資料日;省略則依選週規則自動選")
    ap.add_argument("--stock")
    ap.add_argument("--as-of", help="帶時區 ISO 時間;預設現在(台北)")
    ap.add_argument("--db", default=DB)
    ap.add_argument("--output", help="寫成 UTF-8/LF 檔案")
    ap.add_argument("--run-sql")
    a = ap.parse_args(argv)
    if a.dates and len(a.dates) != 2:
        ap.error("請給兩個日期")
    if a.output and _same_file(a.output, a.db):
        ap.error(f"--output 指向輸入資料庫 {a.db}(或其 -wal/-shm/-journal);拒絕覆寫")
    con = db_ro.connect(a.db)
    try:
        if a.run_sql:
            text = "\n".join(str(tuple(r)) for r in con.execute(a.run_sql))
        else:
            as_of = _aware(a.as_of) if a.as_of else dt.datetime.now(TAIPEI_TZ)
            text = build_report(con, as_of, a.dates or None, a.stock)
    except SelectionError as exc:
        print(f"選週失敗:{exc}", file=sys.stderr)
        return 2
    finally:
        con.close()
    if a.output:
        os.makedirs(os.path.dirname(os.path.abspath(a.output)), exist_ok=True)
        with open(a.output, "wb") as fh:
            fh.write((text + "\n").encode("utf-8"))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
