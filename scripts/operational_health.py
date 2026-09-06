"""整合原始資料、正式發布、排名、TDCC 與研究健康；DB 只經 db_ro 開啟。"""
import argparse
import datetime as dt
import json
import sqlite3
import subprocess

import audit_raw_data as raw
import audit_ranking_views as rankings
import db_ro
import evidence_status
import research_queue as rq
import research_worklist
from fetch_tdcc import LEVELS_FULL


def tdcc_status(con, stock_ids, data_date):
    latest = con.execute("SELECT MAX(date) FROM tdcc_holding WHERE date<=?", (data_date,)).fetchone()[0]
    levels = {}
    for sid, level in con.execute("SELECT stock_id,level FROM tdcc_holding WHERE date=?", (latest,)):
        levels.setdefault(sid, set()).add(level)
    expected = set(range(1, LEVELS_FULL + 1))
    complete = sum(expected <= levels.get(sid, set()) for sid in stock_ids)
    lag = (dt.date.fromisoformat(data_date) - dt.date.fromisoformat(latest)).days if latest else None
    return {"date": latest, "complete_stocks": complete, "stocks": len(stock_ids), "lag_days": lag,
            "status": "complete" if complete == len(stock_ids) and lag is not None and lag <= 7 else "degraded"}


def overall_status(checks):
    values = {c["status"] for c in checks.values()}
    if "failed" in values:
        return "failed"
    if "degraded" in values or "unknown" in values:
        return "degraded"
    return "complete"


def latest_data_dates(con):
    scored = con.execute("SELECT MAX(date) FROM daily_scores").fetchone()[0]
    raw_date = con.execute("""SELECT MAX(date) FROM (
        SELECT p.date FROM price p JOIN universe u USING(stock_id)
        UNION SELECT date FROM market)""").fetchone()[0]
    dates = [date for date in (scored, raw_date) if date]
    if not dates:
        raise ValueError("沒有價格、大盤或評分日期")
    return max(dates), scored


def publication_status(con, data_date, progress, registration_date):
    first = evidence_status.first_official_runs(con).get(data_date)
    snapshot_id = first["snapshot_id"] if first else None
    signals = con.execute("SELECT COUNT(*) FROM oos_signal_snapshots WHERE snapshot_id=?",
                          (snapshot_id,)).fetchone()[0]
    groups = con.execute("SELECT COUNT(*) FROM oos_group_snapshots WHERE snapshot_id=?",
                         (snapshot_id,)).fetchone()[0]
    market = con.execute("SELECT COUNT(*) FROM oos_market_snapshots WHERE snapshot_id=?",
                         (snapshot_id,)).fetchone()[0]
    # stock_count 是首次發布當時的有效母體（已扣官方零交易），不能改用今日 universe。
    complete = bool(first and signals and signals == first["stock_count"]
                    and groups == first["group_count"] and market == 1)
    if data_date >= registration_date and progress["current_spec_latest_date"] != data_date:
        complete = False
    return {"status": "complete" if complete else "failed", "snapshot_id": snapshot_id,
            "signals": signals, "expected": first["stock_count"] if first else None,
            "groups": groups, "expected_groups": first["group_count"] if first else None,
            "market_rows": market, "current_ranking_spec_latest": progress["current_spec_latest_date"],
            "ranking_phase": progress["phase"]}


def build_health(db_path=rq.DB, *, as_of=None, check_pages=False):
    as_of = as_of or rq.taipei_today()
    checks = {}
    with db_ro.connect(db_path) as con:
        ids = [r[0] for r in con.execute("SELECT stock_id FROM universe")]
        last, scored = latest_data_dates(con)
        audit = raw.audit_connection(con, ids, start=last, end=last)
        checks["raw"] = {"status": "complete" if audit["ok"] else "failed",
                         "scope": audit["scope"], "tables": audit["tables"],
                         "errors": audit["errors"], "warnings": audit["warnings"]}
        ranking = rankings.build_audit(con, date=last)
        progress = ranking["formal_progress"]
        partial = any(v < ranking["current"]["stocks"] for v in ranking["current"]["coverage"].values())
        checks["ranking"] = {"status": "failed" if ranking["hard_errors"] else "degraded" if partial else "complete",
                             "coverage": ranking["current"]["coverage"], "stocks": ranking["current"]["stocks"],
                             "fundamental": ranking["fundamental"], "warnings": ranking["warnings"],
                             "errors": ranking["hard_errors"], "spec_sha": ranking["spec_sha"]}
        checks["publication"] = publication_status(con, last, progress, rankings.rv.REGISTERED_AT[:10])
        checks["publication"]["latest_score_date"] = scored
        if scored != last:
            checks["publication"]["status"] = "failed"
        checks["tdcc"] = tdcc_status(con, ids, last)
    snapshot = rq.build_attention(as_of, db_path=db_path)
    worklist = research_worklist.build_worklist(snapshot)
    p0_count = sum(item["priority"] == "P0" for item in snapshot["items"])
    checks["research"] = {"status": "degraded" if p0_count or snapshot["draft_ids"] or snapshot["topic_errors"]
                          or snapshot["scan"]["errors"] or snapshot["stale_topic_count"] else "complete",
                          "verified_notes": snapshot["verified_note_count"], "notes": snapshot["note_count"],
                          "active_topics": snapshot["active_topic_count"], "stale_topics": snapshot["stale_topic_count"],
                          "raw_alerts": worklist["raw_alerts"], "work_items": worklist["work_items"],
                          "p0_alerts": p0_count}
    lag = (as_of - dt.date.fromisoformat(last)).days
    checks["freshness"] = {"status": "degraded" if lag > 3 else "complete", "lag_calendar_days": lag,
                           "note": "超過三個日曆日只提示回查；此處未連線查交易所休市日。"}
    if check_pages:
        process = subprocess.run(["gh", "api", "repos/DennisLiuCk/strong-weak-scanner/pages/builds/latest"],
                                 capture_output=True, text=True, encoding="utf-8", timeout=45)
        page = json.loads(process.stdout) if process.returncode == 0 else {}
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=rq.ROOT).strip()
        state = ("failed" if page.get("status") == "errored" else
                 "complete" if page.get("status") == "built" and page.get("commit") == head else "unknown")
        checks["pages"] = {"status": state, "build_status": page.get("status"),
                           "commit": page.get("commit"), "expected_commit": head}
    return {"as_of": as_of.isoformat(), "data_date": last, "status": overall_status(checks),
            "scope": "本機資料與研究；Pages " + ("已查詢" if check_pages else "未查詢"), "checks": checks}


def render(health):
    labels = {"complete": "完整", "degraded": "部分功能或研究需處理", "failed": "資料／發布檢查未通過", "unknown": "未確認"}
    c = health["checks"]
    lines = [f"■ 整體健康：{labels[health['status']]}（資料日 {health['data_date']}；{health['scope']}）",
             f"  原始資料：{labels[c['raw']['status']]}；正式訊號：{labels[c['publication']['status']]}",
             f"  排名覆蓋：{c['ranking']['coverage']}／{c['ranking']['stocks']} 檔",
             f"  TDCC：{c['tdcc']['date']}，{c['tdcc']['complete_stocks']}/{c['tdcc']['stocks']} 檔級距完整；{labels[c['tdcc']['status']]}",
             f"  研究：{c['research']['stale_topics']}/{c['research']['active_topics']} 篇活躍議題證據過期；"
             f"{c['research']['raw_alerts']} 條警示／{c['research']['work_items']} 件工作，P0 {c['research']['p0_alerts']} 條"]
    if c["publication"]["status"] != "complete":
        p = c["publication"]
        lines.append(f"  發布缺口：評分日 {p['latest_score_date']}；首次正式訊號 {p['signals']}/{p['expected']}，"
                     f"族群 {p['groups']}/{p['expected_groups']}，大盤 {p['market_rows']}/1。")
    f = c["ranking"].get("fundamental") or {}
    if f.get("period_status") == "pending_new_period":
        lines.append(f"  基本面共同月份 {f.get('month_period')}；新月份 {f.get('latest_month_period')} 已收 {f.get('latest_month_coverage')}/{f.get('scope_stocks')} 檔（待到齊，不屬抓取失敗）")
    if c["publication"]["current_ranking_spec_latest"] != health["data_date"]:
        lines.append("  新排名 spec 尚無此資料日正式快照；現行頁面為重算，既有 OOS 不串接。")
    if c["freshness"]["status"] != "complete":
        lines.append(f"  資料距研究日 {c['freshness']['lag_calendar_days']} 個日曆日；{c['freshness']['note']}")
    for key in ("raw", "ranking"):
        for error in c[key].get("errors", []):
            lines.append(f"  ERROR {key}: {error}")
    if "pages" in c:
        lines.append(f"  Pages：{labels[c['pages']['status']]}，commit {c['pages']['commit']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default=rq.DB)
    parser.add_argument("--as-of")
    parser.add_argument("--check-pages", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        health = build_health(args.db, as_of=dt.date.fromisoformat(args.as_of) if args.as_of else None,
                              check_pages=args.check_pages)
    except (ValueError, OSError, sqlite3.Error, subprocess.SubprocessError) as exc:
        parser.exit(2, f"health check failed: {exc}\n")
    rq._write_output(json.dumps(health, ensure_ascii=False, indent=2) + "\n" if args.json else render(health), args.output)
    return 1 if health["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
