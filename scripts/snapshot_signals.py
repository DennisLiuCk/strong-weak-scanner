#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""凍結每日實際發布的 OOS as-seen 訊號。

`daily_scores` / `daily_metrics` 會隨策略、universe 與資料回補而全歷史重算；本檔把
「當下實際可見」的最新資料日另存至 append-only 表，供 validate.py 的 OOS 欄使用。

正式每日管線在 score.py 後、build_dashboard.py 前呼叫本檔。source 只記錄觸發來源；
GitHub Actions 與本地 runner 都能發布正式快照。驗證固定採最早正式發布的 run，後續
修正版仍留存供稽核，但不會覆寫原始判定。
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
import uuid

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
# 本功能於 2026-07-10 上線；更早日期只有 HTML archive、沒有同規格完整原始快照，
# 不可因第一個部署 run 尚抓不到新資料而把舊 restated 7/9 偽裝成正式 OOS。
MIN_DATA_DATE = "2026-07-10"

METRIC_COLS = (
    "close", "close_adj", "ma5", "ma20", "ma60", "rsi14", "volume",
    "vol_ma5", "vol_ma20", "vol_ma60", "vol_ratio20",
    "ret1", "ret20", "turnover_pct", "vol_ratio60",
    "dist_hi20", "dist_hi60", "rs20", "down_rs20", "foreign_pct", "fpct_chg5",
    "fpct_chg20", "dipbuy20", "dipbuy20_t", "trust5", "trust5_pct", "foreign5",
    "margin_bal", "margin_util_pct", "margin_chg5", "margin_chg10", "margin_chg20",
    "short_margin_ratio", "tdcc_date", "tdcc_big400_pct", "tdcc_big400_chg",
    "tdcc_big1000_pct", "tdcc_big1000_chg", "tdcc_people_chg", "sbl_pct",
    "sbl_chg5", "sbl_chg10", "sbl_chg20",
)
SCORE_COLS = (
    "s_price", "s_resil", "s_vol", "s_foreign", "s_trust", "s_dip", "s_margin",
    "composite", "composite_s", "tier_raw", "tier", "warn", "pending",
)

SCHEMA = """
CREATE TABLE IF NOT EXISTS oos_snapshot_runs(
  snapshot_id TEXT PRIMARY KEY,
  data_date TEXT NOT NULL,
  captured_at TEXT NOT NULL,
  source TEXT NOT NULL,
  is_official INTEGER NOT NULL DEFAULT 0,
  git_sha TEXT,
  content_hash TEXT NOT NULL,
  score_hash TEXT NOT NULL,
  metrics_hash TEXT NOT NULL,
  universe_hash TEXT NOT NULL,
  groups_hash TEXT NOT NULL,
  stock_count INTEGER NOT NULL,
  group_count INTEGER NOT NULL,
  quality_json TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS oos_signal_snapshots(
  snapshot_id TEXT NOT NULL,
  date TEXT NOT NULL,
  stock_id TEXT NOT NULL,
  grp TEXT NOT NULL,
  close REAL, close_adj REAL,
  ma5 REAL, ma20 REAL, ma60 REAL, rsi14 REAL,
  volume INTEGER, vol_ma5 REAL, vol_ma20 REAL, vol_ma60 REAL, vol_ratio20 REAL,
  ret1 REAL, ret20 REAL,
  turnover_pct REAL, vol_ratio60 REAL, dist_hi20 REAL, dist_hi60 REAL,
  rs20 REAL, down_rs20 REAL,
  foreign_pct REAL, fpct_chg5 REAL, fpct_chg20 REAL,
  dipbuy20 REAL, dipbuy20_t REAL,
  trust5 INTEGER, trust5_pct REAL, foreign5 INTEGER,
  margin_bal INTEGER, margin_util_pct REAL,
  margin_chg5 REAL, margin_chg10 REAL, margin_chg20 REAL,
  short_margin_ratio REAL,
  tdcc_date TEXT, tdcc_big400_pct REAL, tdcc_big400_chg REAL,
  tdcc_big1000_pct REAL, tdcc_big1000_chg REAL, tdcc_people_chg REAL,
  sbl_pct REAL, sbl_chg5 REAL, sbl_chg10 REAL, sbl_chg20 REAL,
  s_price INTEGER, s_resil INTEGER, s_vol INTEGER, s_foreign INTEGER,
  s_trust INTEGER, s_dip INTEGER, s_margin INTEGER,
  composite REAL, composite_s REAL, tier_raw TEXT, tier TEXT, warn INTEGER, pending TEXT,
  chip_net_score INTEGER, chip_label TEXT, chip_grp_rank INTEGER, chip_grp_n INTEGER,
  risk_flags_json TEXT NOT NULL,
  PRIMARY KEY(snapshot_id, stock_id),
  FOREIGN KEY(snapshot_id) REFERENCES oos_snapshot_runs(snapshot_id)
);
CREATE INDEX IF NOT EXISTS idx_oos_signals_date_stock
  ON oos_signal_snapshots(date, stock_id, snapshot_id);

CREATE TABLE IF NOT EXISTS oos_group_snapshots(
  snapshot_id TEXT NOT NULL,
  date TEXT NOT NULL,
  grp TEXT NOT NULL,
  group_name TEXT, tag TEXT, ord INTEGER,
  breadth_f REAL, med_dist60 REAL, rel20 REAL, med_dip REAL, breadth_t REAL,
  state TEXT, note TEXT,
  PRIMARY KEY(snapshot_id, grp),
  FOREIGN KEY(snapshot_id) REFERENCES oos_snapshot_runs(snapshot_id)
);

CREATE TABLE IF NOT EXISTS oos_market_snapshots(
  snapshot_id TEXT PRIMARY KEY,
  data_date TEXT NOT NULL,
  market_date TEXT,
  taiex REAL, dd20 REAL, regime INTEGER,
  FOREIGN KEY(snapshot_id) REFERENCES oos_snapshot_runs(snapshot_id)
);
"""


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _utc_now():
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def _default_snapshot_id(captured_at):
    run = os.environ.get("GITHUB_RUN_ID")
    if run:
        return f"gh-{run}-{os.environ.get('GITHUB_RUN_ATTEMPT', '1')}"
    stamp = captured_at.replace("-", "").replace(":", "").replace("+00:00", "Z")
    return f"local-{stamp}-{uuid.uuid4().hex[:8]}"


def _current_git_sha(root):
    try:
        return subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=root, check=True,
            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True).stdout.strip() or None
    except (OSError, subprocess.CalledProcessError):
        return None


def ensure_schema(con):
    con.executescript(SCHEMA)
    # 開發期/舊 db 若已建立早期 schema,採向前相容 migration；既有 run 的 hash 留 NULL,
    # 仍可稽核且不影響「最早 captured_at」的 canonical 選取。
    cols = {r[1] for r in con.execute("PRAGMA table_info(oos_snapshot_runs)")}
    if "content_hash" not in cols:
        con.execute("ALTER TABLE oos_snapshot_runs ADD COLUMN content_hash TEXT")
    if "is_official" not in cols:
        con.execute("ALTER TABLE oos_snapshot_runs ADD COLUMN is_official INTEGER NOT NULL DEFAULT 0")
        # 舊版只有 GitHub Actions 被視為正式；migration 保留既有語意。
        con.execute("UPDATE oos_snapshot_runs SET is_official=1 WHERE source='github-actions'")
    # daily_metrics 新增的觀察欄也必須進 as-seen 快照。舊快照保留 NULL，不能回填
    # 現行規則重算值冒充當時可見資料。
    signal_cols = {r[1] for r in con.execute("PRAGMA table_info(oos_signal_snapshots)")}
    signal_types = {"volume": "INTEGER"}
    for name in METRIC_COLS:
        if name not in signal_cols:
            con.execute(
                f"ALTER TABLE oos_signal_snapshots ADD COLUMN {name} {signal_types.get(name, 'REAL')}")
    con.execute("""CREATE INDEX IF NOT EXISTS idx_oos_runs_official ON oos_snapshot_runs(
                   data_date, is_official, captured_at, snapshot_id)""")
    con.commit()


def _table_count(con, table, data_date):
    return con.execute(f"SELECT COUNT(*) FROM {table} WHERE date=?", (data_date,)).fetchone()[0]


def _universe_table_count(con, table, data_date):
    return con.execute(
        f"""SELECT COUNT(DISTINCT t.stock_id) FROM {table} t
            JOIN universe u ON u.stock_id=t.stock_id WHERE t.date=?""", (data_date,)).fetchone()[0]


def capture_snapshot(con, *, root=ROOT, snapshot_id=None, captured_at=None,
                     source=None, publish=None, git_sha=None, min_data_date=MIN_DATA_DATE):
    """凍結最新資料日並回傳 snapshot_id；相同 snapshot_id 重跑為冪等。"""
    con.row_factory = sqlite3.Row
    ensure_schema(con)
    captured_at = captured_at or _utc_now()
    snapshot_id = snapshot_id or _default_snapshot_id(captured_at)
    source = source or ("github-actions" if os.environ.get("GITHUB_ACTIONS") == "true" else "local")
    is_official = int(source == "github-actions" if publish is None else publish)
    git_sha = git_sha or os.environ.get("GITHUB_SHA") or _current_git_sha(root)

    old = con.execute("SELECT data_date FROM oos_snapshot_runs WHERE snapshot_id=?", (snapshot_id,)).fetchone()
    if old:
        return snapshot_id, old["data_date"], False

    score_date = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    metric_date = con.execute("SELECT MAX(date) FROM daily_metrics").fetchone()[0]
    if not score_date or score_date != metric_date:
        raise RuntimeError(f"daily_scores({score_date}) 與 daily_metrics({metric_date}) 最新日不一致")
    data_date = score_date
    if min_data_date and data_date < min_data_date:
        return None, data_date, False
    universe_n = con.execute("SELECT COUNT(*) FROM universe").fetchone()[0]
    score_n = _table_count(con, "daily_scores", data_date)
    metric_n = _table_count(con, "daily_metrics", data_date)
    if score_n != universe_n or metric_n != universe_n:
        raise RuntimeError(
            f"拒絕凍結不完整快照 {data_date}:universe={universe_n},scores={score_n},metrics={metric_n}")

    group_n = con.execute("SELECT COUNT(DISTINCT grp) FROM universe").fetchone()[0]
    gm_n = _table_count(con, "group_metrics", data_date)
    if gm_n != group_n:
        raise RuntimeError(f"拒絕凍結不完整族群快照 {data_date}:groups={group_n},group_metrics={gm_n}")

    raw_tables = ("price", "inst", "margin", "holding", "sbl")
    counts = {t: _universe_table_count(con, t, data_date) for t in raw_tables}
    counts["risk_flags"] = _table_count(con, "risk_flags", data_date)
    if is_official:
        missing = {t: universe_n - counts[t] for t in raw_tables if counts[t] != universe_n}
        if missing:
            detail = ",".join(f"{t}={counts[t]}/{universe_n}" for t in missing)
            raise RuntimeError(f"拒絕發布原始資料不完整快照 {data_date}:{detail}")
    market = con.execute(
        "SELECT * FROM market_daily WHERE date<=? ORDER BY date DESC LIMIT 1", (data_date,)).fetchone()
    if is_official and (not market or market["date"] != data_date):
        got = market["date"] if market else None
        raise RuntimeError(f"拒絕發布大盤資料未同步快照 {data_date}:market_daily={got}")
    counts.update({"universe": universe_n, "daily_scores": score_n, "daily_metrics": metric_n,
                   "group_metrics": gm_n, "market_date": market["date"] if market else None})

    # 空事件/空風險名單在事件表本身看不出「已檢查」；fetch_daily 以 coverage 保存負面
    # 證據。升級前 db 沒有此表時維持相容，升級後正式發布必須全部檢查到資料日。
    have_coverage = con.execute(
        "SELECT 1 FROM sqlite_master WHERE type='table' AND name='fetch_coverage'").fetchone()
    if have_coverage:
        coverage = {(r[0], r[1]): r[2] for r in con.execute(
            "SELECT dataset,data_id,covered_through FROM fetch_coverage")}
        required = [("TaiwanStockDividendResult", r[0])
                    for r in con.execute("SELECT stock_id FROM universe")]
        required += [("TaiwanStockSplitPrice", "*"), ("risk_flags", "*")]
        lagging = [(ds, did, coverage.get((ds, did))) for ds, did in required
                   if (coverage.get((ds, did)) or "") < data_date]
        counts["coverage_through"] = data_date if not lagging else None
        if is_official and lagging:
            sample = ",".join(f"{ds}:{did}={through}" for ds, did, through in lagging[:5])
            raise RuntimeError(
                f"拒絕發布事件/風險 coverage 未同步快照 {data_date}:"
                f"{len(lagging)} 項落後({sample})")

    paths = {
        "score_hash": os.path.join(root, "scripts", "score.py"),
        "metrics_hash": os.path.join(root, "scripts", "fetch_daily.py"),
        "universe_hash": os.path.join(root, "config", "universe.csv"),
        "groups_hash": os.path.join(root, "config", "groups.csv"),
    }
    hashes = {k: _sha256(p) for k, p in paths.items()}

    risks = {}
    for r in con.execute("""SELECT stock_id, kind, reason, period FROM risk_flags
                            WHERE date=? ORDER BY stock_id, kind""", (data_date,)):
        risks.setdefault(r["stock_id"], []).append(
            {"kind": r["kind"], "reason": r["reason"], "period": r["period"]})

    sql = f"""SELECT m.*, u.grp,
                     {', '.join('s.' + c for c in SCORE_COLS)},
                     c.net_score chip_net_score, c.label chip_label,
                     c.grp_rank chip_grp_rank, c.grp_n chip_grp_n
              FROM daily_metrics m
              JOIN daily_scores s USING(date, stock_id)
              JOIN universe u USING(stock_id)
              LEFT JOIN chip_health c USING(date, stock_id)
              WHERE m.date=? ORDER BY u.grp, m.stock_id"""
    signals = con.execute(sql, (data_date,)).fetchall()
    if len(signals) != universe_n:
        raise RuntimeError(f"拒絕凍結 join 不完整快照 {data_date}:universe={universe_n},joined={len(signals)}")

    groups = con.execute(
        """SELECT gm.*, g.name group_name, g.tag, g.ord
           FROM group_metrics gm LEFT JOIN groups g USING(grp)
           WHERE gm.date=? ORDER BY COALESCE(g.ord, 999), gm.grp""", (data_date,)).fetchall()
    # 同一資料日遇台股假日/無新資料時,每日 workflow 不應製造一份完全相同的 revision。
    # fingerprint 含原始值、分數、風險旗標、族群/市場與策略/universe hash；任一修復或
    # 規則改變都會得到新 hash,仍會 append 保存修正版。
    payload = {
        "date": data_date,
        "hashes": hashes,
        "quality": counts,
        "signals": [[r["stock_id"], r["grp"], *(r[c] for c in METRIC_COLS),
                     *(r[c] for c in SCORE_COLS), r["chip_net_score"], r["chip_label"],
                     r["chip_grp_rank"], r["chip_grp_n"], risks.get(r["stock_id"], [])]
                    for r in signals],
        "groups": [list(r) for r in groups],
        "market": list(market) if market else None,
    }
    content_hash = hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), default=str)
        .encode("utf-8")).hexdigest()
    if is_official:
        duplicate = con.execute(
            """SELECT snapshot_id FROM oos_snapshot_runs
               WHERE data_date=? AND is_official=1 AND content_hash=?
               ORDER BY captured_at, snapshot_id LIMIT 1""",
            (data_date, content_hash)).fetchone()
        if duplicate:
            return duplicate["snapshot_id"], data_date, False

    con.execute("BEGIN IMMEDIATE")
    try:
        con.execute(
            """INSERT INTO oos_snapshot_runs(
                 snapshot_id,data_date,captured_at,source,is_official,git_sha,content_hash,
                 score_hash,metrics_hash,universe_hash,groups_hash,stock_count,group_count,quality_json)
               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            (snapshot_id, data_date, captured_at, source, is_official, git_sha, content_hash,
             hashes["score_hash"], hashes["metrics_hash"], hashes["universe_hash"],
             hashes["groups_hash"], universe_n, group_n,
             json.dumps(counts, ensure_ascii=False, sort_keys=True)))

        signal_cols = ("snapshot_id", "date", "stock_id", "grp") + METRIC_COLS + SCORE_COLS + (
            "chip_net_score", "chip_label", "chip_grp_rank", "chip_grp_n", "risk_flags_json")
        placeholders = ",".join("?" for _ in signal_cols)
        out = []
        for r in signals:
            out.append((snapshot_id, data_date, r["stock_id"], r["grp"],
                        *(r[c] for c in METRIC_COLS), *(r[c] for c in SCORE_COLS),
                        r["chip_net_score"], r["chip_label"], r["chip_grp_rank"], r["chip_grp_n"],
                        json.dumps(risks.get(r["stock_id"], []), ensure_ascii=False, sort_keys=True)))
        con.executemany(
            f"INSERT INTO oos_signal_snapshots({','.join(signal_cols)}) VALUES({placeholders})", out)

        con.executemany(
            """INSERT INTO oos_group_snapshots VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
            [(snapshot_id, data_date, r["grp"], r["group_name"], r["tag"], r["ord"],
              r["breadth_f"], r["med_dist60"], r["rel20"], r["med_dip"], r["breadth_t"],
              r["state"], r["note"]) for r in groups])
        con.execute(
            "INSERT INTO oos_market_snapshots VALUES(?,?,?,?,?,?)",
            (snapshot_id, data_date, market["date"] if market else None,
             market["taiex"] if market else None, market["dd20"] if market else None,
             market["regime"] if market else None))
        con.commit()
    except Exception:
        con.rollback()
        raise
    return snapshot_id, data_date, True


def main():
    ap = argparse.ArgumentParser(description="凍結最新資料日的 append-only OOS as-seen 訊號")
    ap.add_argument("--db", default=DB)
    ap.add_argument("--snapshot-id", help="測試/重跑用；正式 Actions 自動採 run id")
    ap.add_argument("--captured-at", help="ISO-8601 UTC；省略用目前時間")
    ap.add_argument("--source", choices=("github-actions", "local", "manual"),
                    help="只記錄觸發來源；省略則由環境自動判定")
    ap.add_argument("--publish", action="store_true", default=None,
                    help="發布為正式 OOS；GitHub Actions 預設自動發布，本地需明確指定")
    ap.add_argument("--min-date", default=MIN_DATA_DATE,
                    help="最早可凍結資料日;防首個 run 把上線前 restated 歷史偽裝成 OOS")
    args = ap.parse_args()
    con = sqlite3.connect(args.db)
    try:
        sid, data_date, created = capture_snapshot(
            con, snapshot_id=args.snapshot_id, captured_at=args.captured_at, source=args.source,
            publish=args.publish, min_data_date=args.min_date)
        if sid is None:
            print(f"OOS as-seen 快照略過:最新資料日 {data_date} 早於上線日 {args.min_date}")
        else:
            mode = "正式" if (args.publish or (args.publish is None and
                            (args.source == "github-actions" or
                             (args.source is None and os.environ.get("GITHUB_ACTIONS") == "true")))) else "預覽"
            print(f"OOS as-seen {mode}快照 {'已凍結' if created else '已存在'}:{data_date} · {sid}")
    finally:
        con.close()


if __name__ == "__main__":
    main()
