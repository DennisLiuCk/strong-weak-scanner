#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""聚合質化筆記、領先假說、事件、財報覆蓋與市場議題的唯讀研究佇列。"""

import argparse
import csv
import datetime as dt
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict
from urllib.parse import urlparse

import db_ro
from leading_hypotheses import load_reports
from qual_notes import load_events, load_notes, note_review_status


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "data", "findmind.db")
UNIVERSE_CSV = os.path.join(ROOT, "config", "universe.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")
TOPICS_DIR = os.path.join(ROOT, "notes", "research_topics")
SCAN_LOG = os.path.join(TOPICS_DIR, "scan_log.csv")
ROTATION_ANCHOR = dt.date(2026, 7, 27)  # 星期一；A cohort 的第一個營運週
TAIPEI_TZ = dt.timezone(dt.timedelta(hours=8))

TOPIC_META_RE = re.compile(r"<!--\s*research_topic\s*(.*?)-->", re.S | re.I)
IMPACT_RE = re.compile(r"<!--\s*impact\s*(.*?)-->", re.S | re.I)
TRANSITION_RE = re.compile(r"<!--\s*transition\s*(.*?)-->", re.S | re.I)
TOPIC_ID_RE = re.compile(r"^MI-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+$")
HYPOTHESIS_REF_RE = re.compile(r"^(\d{4}):H(\d+)$")

TOPIC_STATUSES = {"inbox", "triaged", "promoted", "dismissed", "resolved"}
TOPIC_PRIORITIES = {"p0", "p1", "p2", "p3"}
SOURCE_TYPES = {
    "official_company", "official_policy", "official_exchange", "management_direct",
    "management_relay", "broker_relay", "media_report", "mixed",
}
EVIDENCE_ROLES = {"candidate_source", "trigger_only"}
ROUTES = {
    "undecided", "market_issue_watch", "formal_note_candidate",
    "hypothesis_candidate", "event_anchor_candidate", "policy_watch",
}
DIRECTIONS = {"tailwind", "headwind", "mixed", "uncertain"}
NOTE_ACTIONS = {"none", "watch", "review_due", "update_required", "done"}
ACTIVE_NOTE_ACTIONS = {"watch", "review_due", "update_required"}
ALLOWED_TRANSITIONS = {
    "initial": {"inbox"},
    "inbox": {"triaged", "dismissed"},
    "triaged": {"promoted", "dismissed", "resolved"},
    "promoted": {"resolved"},
    "dismissed": set(),
    "resolved": set(),
}


def _parse_fields(body):
    fields = {}
    for raw in body.strip().splitlines():
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = value.strip()
    return fields


def _csv_values(value):
    return [part.strip() for part in (value or "").split(",") if part.strip()]


def _semicolon_values(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def _valid_date(value):
    try:
        dt.date.fromisoformat(value)
        return True
    except (TypeError, ValueError):
        return False


def taipei_today():
    return dt.datetime.now(TAIPEI_TZ).date()


def _load_universe(path=UNIVERSE_CSV):
    with open(path, encoding="utf-8") as handle:
        return [row for row in csv.DictReader(handle) if row.get("stock_id")]


def _load_groups(path=GROUPS_CSV):
    with open(path, encoding="utf-8") as handle:
        return {row["group"] for row in csv.DictReader(handle) if row.get("group")}


def _publisher_matches_url(publisher_domain, url):
    hostname = (urlparse(url).hostname or "").lower()
    domain = (publisher_domain or "").lower()
    return bool(domain and hostname and (hostname == domain or hostname.endswith("." + domain)))


def _hypothesis_ids(reports):
    return {
        f"{sid}:{item['id']}"
        for sid, report in reports.items()
        for item in report.get("hypotheses", [])
    }


def analyse_topic(path, text, universe_rows=None, group_ids=None, reports=None):
    """解析單一候選議題；議題只負責路由，不把主張升格成正式公司事實。"""
    universe_rows = universe_rows if universe_rows is not None else _load_universe()
    group_ids = group_ids if group_ids is not None else _load_groups()
    reports = reports or {}
    universe = {row["stock_id"]: row for row in universe_rows}
    known_hypotheses = _hypothesis_ids(reports)
    errors, warnings = [], []

    matches = TOPIC_META_RE.findall(text)
    if len(matches) != 1:
        errors.append("每個議題必須且只能有一個 research_topic meta")
    meta = _parse_fields(matches[0]) if matches else {}
    required = (
        "topic_id", "schema_version", "status", "priority", "captured_at",
        "source_published_at", "last_reviewed_at", "review_due", "source_type",
        "publisher_domain", "canonical_url", "source_chain_id", "trigger_type",
        "evidence_role", "route",
    )
    for key in required:
        if not meta.get(key):
            errors.append(f"research_topic meta 缺少必填欄位:{key}")

    topic_id = meta.get("topic_id", "")
    if topic_id and not TOPIC_ID_RE.fullmatch(topic_id):
        errors.append(f"topic_id 格式錯誤:{topic_id}")
    if meta.get("schema_version") and meta["schema_version"] != "1":
        errors.append("schema_version 必須是 1")
    if meta.get("status") and meta["status"] not in TOPIC_STATUSES:
        errors.append(f"status 不在值域:{meta['status']}")
    if meta.get("priority") and meta["priority"] not in TOPIC_PRIORITIES:
        errors.append(f"priority 不在值域:{meta['priority']}")
    if meta.get("source_type") and meta["source_type"] not in SOURCE_TYPES:
        errors.append(f"source_type 不在值域:{meta['source_type']}")
    if meta.get("evidence_role") and meta["evidence_role"] not in EVIDENCE_ROLES:
        errors.append(f"evidence_role 不在值域:{meta['evidence_role']}")
    if meta.get("route") and meta["route"] not in ROUTES:
        errors.append(f"route 不在值域:{meta['route']}")

    for key in ("source_published_at", "captured_at", "last_reviewed_at", "review_due"):
        value = meta.get(key)
        if value and not _valid_date(value):
            errors.append(f"{key} 不是 YYYY-MM-DD:{value}")
    if (_valid_date(meta.get("source_published_at"))
            and _valid_date(meta.get("captured_at"))
            and meta["source_published_at"] > meta["captured_at"]):
        errors.append("source_published_at 不可晚於 captured_at")
    if (_valid_date(meta.get("captured_at"))
            and _valid_date(meta.get("last_reviewed_at"))
            and meta["last_reviewed_at"] < meta["captured_at"]):
        errors.append("last_reviewed_at 不可早於 captured_at")
    if (_valid_date(meta.get("captured_at"))
            and _valid_date(meta.get("review_due"))
            and meta["review_due"] < meta["captured_at"]):
        errors.append("review_due 不可早於 captured_at")

    canonical_url = meta.get("canonical_url", "")
    if canonical_url:
        parsed = urlparse(canonical_url)
        if parsed.scheme != "https" or not parsed.hostname:
            errors.append("canonical_url 必須是有效 https URL")
        elif not _publisher_matches_url(meta.get("publisher_domain"), canonical_url):
            errors.append("publisher_domain 與 canonical_url 主機不一致")

    declared_stocks = _csv_values(meta.get("stock_ids"))
    declared_groups = _csv_values(meta.get("group_ids"))
    for sid in declared_stocks:
        if sid not in universe:
            errors.append(f"stock_ids 含非 universe 成員:{sid}")
    for group_id in declared_groups:
        if group_id not in group_ids:
            errors.append(f"group_ids 含未知族群:{group_id}")

    impacts = []
    impact_stocks, impact_groups = set(), set()
    for idx, body in enumerate(IMPACT_RE.findall(text), 1):
        impact = _parse_fields(body)
        group_id = impact.get("group_id", "")
        stock_ids = _csv_values(impact.get("stock_ids"))
        hypothesis_refs = _csv_values(impact.get("hypothesis_refs"))
        if not group_id:
            errors.append(f"impact {idx} 缺少 group_id")
        elif group_id not in group_ids:
            errors.append(f"impact {idx} 未知 group_id:{group_id}")
        else:
            impact_groups.add(group_id)
        if impact.get("direction") not in DIRECTIONS:
            errors.append(f"impact {idx} direction 不在值域")
        action = impact.get("note_action")
        if action not in NOTE_ACTIONS:
            errors.append(f"impact {idx} note_action 不在值域")
        if action in ACTIVE_NOTE_ACTIONS:
            due = impact.get("action_due")
            if not _valid_date(due):
                errors.append(f"impact {idx} 的 {action} 必須有合法 action_due")
        if not impact.get("rationale"):
            errors.append(f"impact {idx} 缺少 rationale")
        if not impact.get("evidence_boundary"):
            errors.append(f"impact {idx} 缺少 evidence_boundary")
        for sid in stock_ids:
            impact_stocks.add(sid)
            if sid not in universe:
                errors.append(f"impact {idx} 含非 universe 成員:{sid}")
            elif group_id in group_ids and universe[sid]["group"] != group_id:
                errors.append(
                    f"impact {idx} 的 {sid} 實際屬 {universe[sid]['group']}，非 {group_id}")
        for ref in hypothesis_refs:
            if not HYPOTHESIS_REF_RE.fullmatch(ref):
                errors.append(f"impact {idx} hypothesis_ref 格式錯誤:{ref}")
            elif ref not in known_hypotheses:
                errors.append(f"impact {idx} 找不到 hypothesis_ref:{ref}")
        impact["stock_ids"] = stock_ids
        impact["hypothesis_refs"] = hypothesis_refs
        impacts.append(impact)

    if set(declared_stocks) != impact_stocks:
        errors.append("meta stock_ids 必須等於所有 impact stock_ids 聯集")
    if set(declared_groups) != impact_groups:
        errors.append("meta group_ids 必須等於所有 impact group_id 聯集")

    transitions = [_parse_fields(body) for body in TRANSITION_RE.findall(text)]
    if not transitions:
        errors.append("議題必須保留至少一筆 transition")
    state, previous_date = "initial", None
    for idx, transition in enumerate(transitions, 1):
        value = transition.get("date")
        if not _valid_date(value):
            errors.append(f"transition {idx} 日期不合法")
        elif previous_date and value < previous_date:
            errors.append(f"transition {idx} 日期早於前一筆")
        if transition.get("from") != state:
            errors.append(f"transition {idx} 未銜接上一狀態 {state}")
        target = transition.get("to", "")
        if target not in ALLOWED_TRANSITIONS.get(state, set()):
            errors.append(f"transition {idx} 不允許 {state}→{target}")
        if not transition.get("reason"):
            errors.append(f"transition {idx} 缺少 reason")
        if not transition.get("evidence"):
            errors.append(f"transition {idx} 缺少 evidence")
        state = target or state
        previous_date = value if _valid_date(value) else previous_date
    if transitions and meta.get("status") and state != meta["status"]:
        errors.append(f"最後 transition 狀態 {state} 與 meta status {meta['status']} 不一致")

    title_match = re.search(r"^#\s+(.+?)\s*$", TOPIC_META_RE.sub("", text), re.M)
    if not title_match:
        errors.append("議題缺少 H1 標題")
    title = title_match.group(1).strip() if title_match else os.path.basename(path)
    if not impacts:
        warnings.append("尚無 impact；在完成產業/個股映射前不可路由進正式筆記")

    return {
        "path": path,
        "relpath": os.path.relpath(path, ROOT).replace("\\", "/"),
        "title": title,
        "meta": meta,
        "topic_id": topic_id,
        "status": meta.get("status"),
        "priority": meta.get("priority"),
        "captured_at": meta.get("captured_at"),
        "review_due": meta.get("review_due"),
        "stock_ids": declared_stocks,
        "group_ids": declared_groups,
        "impacts": impacts,
        "transitions": transitions,
        "quality_errors": errors,
        "quality_warnings": warnings,
        "quality_invalid": bool(errors),
    }


def load_topics(topics_dir=TOPICS_DIR, universe_rows=None, group_ids=None, reports=None):
    universe_rows = universe_rows if universe_rows is not None else _load_universe()
    group_ids = group_ids if group_ids is not None else _load_groups()
    reports = reports or {}
    topics, seen = [], {}
    if not os.path.isdir(topics_dir):
        return topics
    for path in sorted(glob.glob(os.path.join(topics_dir, "*.md"))):
        if os.path.basename(path).startswith("_"):
            continue
        with open(path, encoding="utf-8") as handle:
            topic = analyse_topic(path, handle.read(), universe_rows, group_ids, reports)
        if topic["topic_id"] in seen:
            topic["quality_errors"].append(
                f"topic_id 重複:{os.path.basename(seen[topic['topic_id']]['path'])}")
            topic["quality_invalid"] = True
            seen[topic["topic_id"]]["quality_errors"].append(
                f"topic_id 重複:{os.path.basename(path)}")
            seen[topic["topic_id"]]["quality_invalid"] = True
        else:
            seen[topic["topic_id"]] = topic
        topics.append(topic)
    return topics


def load_scan_log(path=SCAN_LOG, topic_ids=None):
    """讀取有證據的掃描紀錄；partial 明確不等於完整涵蓋窗口。"""
    topic_ids = set(topic_ids or [])
    rows, errors = [], []
    if not os.path.exists(path):
        return {"rows": [], "latest": None, "errors": ["缺少 scan_log.csv"]}
    required = {
        "scan_id", "window_start", "window_end", "scanned_at", "scope",
        "source_domains", "result_topic_ids", "next_scan_due", "coverage_note",
    }
    with open(path, encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = required - set(reader.fieldnames or [])
        if missing:
            errors.append(f"scan_log 缺欄:{','.join(sorted(missing))}")
        for lineno, row in enumerate(reader, 2):
            row_errors = []
            if not row.get("scan_id"):
                row_errors.append("scan_id 不可空白")
            for key in ("window_start", "window_end", "scanned_at", "next_scan_due"):
                if not _valid_date(row.get(key)):
                    row_errors.append(f"{key} 不是 YYYY-MM-DD")
            if (all(_valid_date(row.get(k)) for k in ("window_start", "window_end"))
                    and row["window_start"] > row["window_end"]):
                row_errors.append("window_start 晚於 window_end")
            if (all(_valid_date(row.get(k)) for k in ("window_end", "scanned_at"))
                    and row["window_end"] > row["scanned_at"]):
                row_errors.append("window_end 晚於 scanned_at")
            if (all(_valid_date(row.get(k)) for k in ("scanned_at", "next_scan_due"))
                    and row["scanned_at"] > row["next_scan_due"]):
                row_errors.append("scanned_at 晚於 next_scan_due")
            if row.get("scope") not in {"full", "partial"}:
                row_errors.append("scope 必須是 full 或 partial")
            if not _semicolon_values(row.get("source_domains")):
                row_errors.append("source_domains 不可空白")
            if not row.get("coverage_note"):
                row_errors.append("coverage_note 不可空白")
            result_ids = _semicolon_values(row.get("result_topic_ids"))
            if result_ids == ["none"]:
                result_ids = []
            for topic_id in result_ids:
                if topic_id not in topic_ids:
                    row_errors.append(f"result_topic_ids 找不到:{topic_id}")
            row["result_topic_ids"] = result_ids
            row["quality_errors"] = row_errors
            errors.extend(f"scan_log:{lineno}:{issue}" for issue in row_errors)
            rows.append(row)
    seen = Counter(row.get("scan_id") for row in rows)
    for scan_id, count in seen.items():
        if scan_id and count > 1:
            errors.append(f"scan_id 重複:{scan_id}")
    valid = [
        row for row in rows
        if _valid_date(row.get("scanned_at")) and not row["quality_errors"]
    ]
    latest = max(valid, key=lambda row: (row["scanned_at"], row.get("scan_id", ""))) if valid else None
    return {"rows": rows, "latest": latest, "errors": errors}


def expected_revenue_period(as_of):
    """月營收法定申報日在次月 10 日；10 日以前只要求再前一月。"""
    target = as_of.replace(day=1)
    months_back = 1 if as_of.day >= 11 else 2
    for _ in range(months_back):
        target = (target - dt.timedelta(days=1)).replace(day=1)
    return target.year, target.month


def _quarter_token(value):
    if not value or not _valid_date(value):
        return None
    period = dt.date.fromisoformat(value)
    return f"{period.year}Q{(period.month - 1) // 3 + 1}"


def expected_quarter_date(as_of):
    """依申報截止日推導已應公布的最新季度，避免以 DB MAX(date) 自我證明完整。"""
    year = as_of.year
    if as_of >= dt.date(year, 11, 15):  # Q3 截止 11/14
        return dt.date(year, 9, 30)
    if as_of >= dt.date(year, 8, 15):   # Q2 截止 8/14
        return dt.date(year, 6, 30)
    if as_of >= dt.date(year, 5, 16):   # Q1 截止 5/15
        return dt.date(year, 3, 31)
    if as_of >= dt.date(year, 4, 1):    # 年報截止 3/31
        return dt.date(year - 1, 12, 31)
    return dt.date(year - 1, 9, 30)


def financial_snapshot(con, universe_rows, as_of):
    ids = [row["stock_id"] for row in universe_rows]
    placeholders = ",".join("?" for _ in ids)
    year, month = expected_revenue_period(as_of)
    present = {
        row["stock_id"]
        for row in con.execute(
            f"SELECT DISTINCT stock_id FROM month_revenue "
            f"WHERE revenue_year=? AND revenue_month=? AND revenue IS NOT NULL "
            f"AND stock_id IN ({placeholders})",
            (year, month, *ids),
        )
    }
    missing_revenue = [sid for sid in ids if sid not in present]
    expected_quarter = expected_quarter_date(as_of)
    expected_quarter_iso = expected_quarter.isoformat()
    expected_quarter_period = _quarter_token(expected_quarter_iso)
    quarter_tables = {}
    for table in ("financials", "balance_sheet", "cash_flow"):
        covered = {
            row["stock_id"]
            for row in con.execute(
                f"SELECT DISTINCT stock_id FROM {table} "
                f"WHERE date=? AND value IS NOT NULL AND stock_id IN ({placeholders})",
                (expected_quarter_iso, *ids),
            )
        }
        quarter_tables[table] = {
            "expected_date": expected_quarter_iso,
            "period": expected_quarter_period,
            "covered": len(covered),
            "missing": [sid for sid in ids if sid not in covered],
        }
    common_latest_period = (
        expected_quarter_period
        if all(item["covered"] == len(ids) for item in quarter_tables.values())
        else None
    )
    return {
        "expected_revenue_period": f"{year}-{month:02d}",
        "expected_quarter_period": expected_quarter_period,
        "revenue_covered": len(present),
        "revenue_missing": missing_revenue,
        "quarter_tables": quarter_tables,
        "common_latest_period": common_latest_period,
    }


def cohort_map(universe_rows):
    """把每個族群輪流分到 A–D，121 檔目前為 31/30/30/30。"""
    grouped = defaultdict(list)
    for row in universe_rows:
        grouped[row["group"]].append(row)
    cohorts = {label: [] for label in "ABCD"}
    offset = 0
    for group_id in sorted(grouped):
        members = sorted(grouped[group_id], key=lambda row: row["stock_id"])
        for index, row in enumerate(members):
            cohorts["ABCD"[(offset + index) % 4]].append(row)
        offset = (offset + len(members)) % 4
    return cohorts


def active_cohort(as_of):
    monday = as_of - dt.timedelta(days=as_of.weekday())
    weeks = (monday - ROTATION_ANCHOR).days // 7
    return "ABCD"[weeks % 4], monday


def _current_hypothesis_transition(hypothesis, as_of):
    visible = [
        item for item in hypothesis.get("transitions", [])
        if _valid_date(item.get("date")) and item["date"] <= as_of.isoformat()
    ]
    return visible[-1] if visible else None


def _append_item(items, priority, kind, due, detail):
    items.append({"priority": priority, "kind": kind, "due": due, "detail": detail})


def _topic_queue_priority(priority, due_date, as_of):
    """研究 priority 是營運優先級；期限到期至少升為 P1。"""
    if priority == "p0":
        return "P0"
    if priority == "p1" or due_date <= as_of:
        return "P1"
    return "P2"


def build_attention(as_of, db_path=DB, horizon=30, topics_dir=TOPICS_DIR,
                    scan_log_path=SCAN_LOG):
    universe_rows = _load_universe()
    names = {row["stock_id"]: row["name"] for row in universe_rows}
    notes = load_notes()
    reports = load_reports(notes=notes)
    groups = _load_groups()
    topics = load_topics(topics_dir, universe_rows, groups, reports)
    scan = load_scan_log(scan_log_path, [topic["topic_id"] for topic in topics])
    end = as_of + dt.timedelta(days=horizon)
    items = []

    draft_ids = []
    note_deadlines = Counter()
    for row in universe_rows:
        sid, info = row["stock_id"], notes.get(row["stock_id"])
        verification = note_review_status(info)
        if info is None or info.get("quality_invalid") or verification != "independently_verified":
            draft_ids.append(sid)
            _append_item(
                items, "P0", "formal_note_quality", as_of.isoformat(),
                f"{sid} {names[sid]}：{verification}"
                + ("，品質契約 invalid" if info and info.get("quality_invalid") else ""),
            )
        due = (info or {}).get("next_review")
        if _valid_date(due):
            due_date = dt.date.fromisoformat(due)
            note_deadlines[due] += 1
            if due_date <= as_of:
                _append_item(items, "P1", "formal_note_due", due, f"{sid} {names[sid]}")
            elif due_date <= end:
                _append_item(items, "P2", "formal_note_upcoming", due, f"{sid} {names[sid]}")

    hypothesis_deadlines = Counter()
    for sid, report in reports.items():
        for hypothesis in report.get("hypotheses", []):
            current = _current_hypothesis_transition(hypothesis, as_of)
            if not current or current.get("to") != "open":
                continue
            due = current.get("review_due")
            if not _valid_date(due):
                continue
            due_date = dt.date.fromisoformat(due)
            hypothesis_deadlines[due] += 1
            detail = f"{sid}:{hypothesis['id']} {hypothesis['title']}"
            if due_date <= as_of:
                _append_item(items, "P1", "hypothesis_due", due, detail)
            elif due_date <= end:
                _append_item(items, "P2", "hypothesis_upcoming", due, detail)

    event_deadlines = Counter()
    events = load_events()
    for event in events.get("all", []):
        due = event.get("next_review")
        if not _valid_date(due):
            continue
        event_deadlines[due] += 1
        due_date = dt.date.fromisoformat(due)
        detail = f"{event.get('subject')} {event.get('fiscal_quarter')} ({event.get('event_date')})"
        if due_date <= as_of:
            _append_item(items, "P1", "event_due", due, detail)
        elif due_date <= end:
            _append_item(items, "P2", "event_upcoming", due, detail)

    con = db_ro.connect(db_path)
    try:
        financial = financial_snapshot(con, universe_rows, as_of)
    finally:
        con.close()
    if financial["revenue_missing"]:
        detail = "、".join(
            f"{sid} {names.get(sid, '')}".strip() for sid in financial["revenue_missing"])
        _append_item(
            items, "P0", "month_revenue_gap", as_of.isoformat(),
            f"{financial['expected_revenue_period']} 缺 {len(financial['revenue_missing'])} 檔：{detail}",
        )
    for table, result in financial["quarter_tables"].items():
        if result["missing"]:
            _append_item(
                items, "P0", "quarterly_financial_gap", as_of.isoformat(),
                f"{table} {result['period']} 缺 {len(result['missing'])} 檔",
            )

    latest_period = financial["common_latest_period"]
    financial_note_stale = []
    if latest_period:
        for sid, info in notes.items():
            declared = re.sub(r"\s+", "", info.get("latest_financial_period") or "")
            if latest_period not in declared:
                financial_note_stale.append(sid)
                _append_item(
                    items, "P2", "formal_note_financial_period", as_of.isoformat(),
                    f"{sid} {names.get(sid, '')} 仍標 {info.get('latest_financial_period') or '-'}；"
                    f"DB 已有 {latest_period}",
                )

    for topic in topics:
        if topic["quality_invalid"]:
            _append_item(
                items, "P0", "topic_contract", as_of.isoformat(),
                f"{topic['relpath']}：{'; '.join(topic['quality_errors'])}",
            )
            continue
        if topic["status"] in {"dismissed", "resolved"}:
            continue
        due = topic.get("review_due")
        if _valid_date(due):
            due_date = dt.date.fromisoformat(due)
            priority = _topic_queue_priority(topic.get("priority"), due_date, as_of)
            if due_date <= end or priority in {"P0", "P1"}:
                kind = "topic_due" if due_date <= as_of else "topic_upcoming"
                _append_item(items, priority, kind, due, topic["topic_id"])
        for impact in topic["impacts"]:
            action = impact.get("note_action")
            due = impact.get("action_due")
            if action not in ACTIVE_NOTE_ACTIONS or not _valid_date(due):
                continue
            due_date = dt.date.fromisoformat(due)
            detail = (
                f"{topic['topic_id']} → {impact.get('group_id')}"
                + (f" ({','.join(impact['stock_ids'])})" if impact["stock_ids"] else "")
                + f"：{action}"
            )
            if due_date <= as_of:
                _append_item(items, "P1", "topic_action_due", due, detail)
            elif due_date <= end:
                _append_item(items, "P2", "topic_action_upcoming", due, detail)

        for sid in topic["stock_ids"]:
            report = reports.get(sid)
            narrative = (report or {}).get("narrative")
            if (narrative and _valid_date(narrative.get("updated"))
                    and _valid_date(topic.get("captured_at"))
                    and narrative["updated"] < topic["captured_at"]):
                _append_item(
                    items, "P2", "narrative_review",
                    topic.get("review_due") or as_of.isoformat(),
                    f"{sid} {names.get(sid, '')} 小作文 {narrative['updated']} 早於"
                    f"議題 {topic['topic_id']} 的捕捉日 {topic['captured_at']}；只需判斷是否相關，"
                    "不可自動改寫",
                )

    if scan["errors"]:
        for issue in scan["errors"]:
            _append_item(items, "P0", "scan_log_contract", as_of.isoformat(), issue)
    elif scan["latest"] is None:
        _append_item(items, "P1", "scan_missing", as_of.isoformat(), "尚無市場議題掃描紀錄")
    else:
        latest_scan = scan["latest"]
        if latest_scan["scope"] == "partial":
            _append_item(
                items, "P1", "scan_partial", latest_scan["next_scan_due"],
                f"最近一次掃描 {latest_scan['scan_id']} 為 partial："
                f"{latest_scan['coverage_note']}",
            )
        if (_valid_date(latest_scan.get("next_scan_due"))
                and latest_scan["next_scan_due"] <= as_of.isoformat()):
            _append_item(
                items, "P1", "scan_due", latest_scan["next_scan_due"],
                f"上次掃描 {latest_scan['scanned_at']}，下一次已到期",
            )

    items.sort(key=lambda item: (
        {"P0": 0, "P1": 1, "P2": 2}[item["priority"]],
        item["due"], item["kind"], item["detail"],
    ))
    cohorts = cohort_map(universe_rows)
    cohort, monday = active_cohort(as_of)
    return {
        "as_of": as_of.isoformat(),
        "horizon_days": horizon,
        "universe_count": len(universe_rows),
        "note_count": len(notes),
        "verified_note_count": sum(
            note_review_status(info) == "independently_verified" for info in notes.values()),
        "draft_ids": draft_ids,
        "report_count": len(reports),
        "hypothesis_count": sum(
            len(report.get("hypotheses", [])) for report in reports.values()),
        "topic_count": len(topics),
        "items": items,
        "financial": financial,
        "financial_note_stale": financial_note_stale,
        "deadline_distribution": {
            "formal_notes": dict(sorted(note_deadlines.items())),
            "hypotheses": dict(sorted(hypothesis_deadlines.items())),
            "events": dict(sorted(event_deadlines.items())),
        },
        "active_cohort": cohort,
        "active_week": monday.isoformat(),
        "cohorts": {
            label: [
                {"stock_id": row["stock_id"], "name": row["name"], "group": row["group"]}
                for row in members
            ]
            for label, members in cohorts.items()
        },
        "topic_errors": [
            f"{topic['relpath']}: {error}"
            for topic in topics for error in topic["quality_errors"]
        ],
        "topic_warnings": [
            f"{topic['relpath']}: {warning}"
            for topic in topics for warning in topic["quality_warnings"]
        ],
        "scan": scan,
    }


def _deadline_rows(snapshot):
    dates = set()
    for values in snapshot["deadline_distribution"].values():
        dates.update(values)
    return [
        (
            due,
            snapshot["deadline_distribution"]["formal_notes"].get(due, 0),
            snapshot["deadline_distribution"]["hypotheses"].get(due, 0),
            snapshot["deadline_distribution"]["events"].get(due, 0),
        )
        for due in sorted(dates)
    ]


def render_attention(snapshot):
    financial = snapshot["financial"]
    lines = [
        "# 研究維護佇列",
        "",
        f"- as_of：{snapshot['as_of']}（台灣研究日）",
        f"- universe：{snapshot['universe_count']} 檔；正式筆記 "
        f"{snapshot['note_count']} 篇（已獨立核驗 {snapshot['verified_note_count']}）",
        f"- 領先假說：{snapshot['report_count']} 份報告／"
        f"{snapshot['hypothesis_count']} 則；候選市場議題 {snapshot['topic_count']} 則",
        "- 數字是全 universe 普查，不是抽樣估計；因此不附 SE。",
        "",
        "## 財務資料覆蓋",
        "",
        "| 資料 | 最新要求／期間 | 覆蓋 | 缺口 |",
        "|---|---:|---:|---:|",
        f"| 月營收 | {financial['expected_revenue_period']} | "
        f"{financial['revenue_covered']}/{snapshot['universe_count']} | "
        f"{len(financial['revenue_missing'])} |",
    ]
    for table, result in financial["quarter_tables"].items():
        lines.append(
            f"| {table} | {result['period'] or '-'} | "
            f"{result['covered']}/{snapshot['universe_count']} | {len(result['missing'])} |")

    lines += ["", "## 需處理", ""]
    for priority in ("P0", "P1", "P2"):
        selected = [item for item in snapshot["items"] if item["priority"] == priority]
        lines.append(f"### {priority}（{len(selected)}）")
        lines.append("")
        if not selected:
            lines.append("- 無")
        else:
            for item in selected:
                lines.append(
                    f"- `{item['due']}` `{item['kind']}` — {item['detail']}")
        lines.append("")

    lines += [
        "## 硬期限分布",
        "",
        "| 日期 | 正式筆記 | H# | 事件錨點 |",
        "|---|---:|---:|---:|",
    ]
    for due, notes, hypotheses, events in _deadline_rows(snapshot):
        lines.append(f"| {due} | {notes} | {hypotheses} | {events} |")

    cohort = snapshot["active_cohort"]
    lines += [
        "",
        f"## 本週輪掃：{cohort} cohort（{snapshot['active_week']} 起）",
        "",
    ]
    grouped = defaultdict(list)
    for row in snapshot["cohorts"][cohort]:
        grouped[row["group"]].append(f"{row['stock_id']} {row['name']}")
    for group_id in sorted(grouped):
        lines.append(f"- **{group_id}：** " + "、".join(grouped[group_id]))
    lines += [
        "",
        "> 到期與輪掃是營運提示，不是新的投資訊號；月營收、價格或籌碼異常只能觸發查找，"
        "不得直接當作 H# 生命週期轉移或正式筆記事實。",
    ]
    return "\n".join(lines) + "\n"


def render_calendar(snapshot, weeks):
    as_of = dt.date.fromisoformat(snapshot["as_of"])
    monday = as_of - dt.timedelta(days=as_of.weekday())
    lines = [
        "# 研究輪掃時間表",
        "",
        f"- 產生基準：{snapshot['as_of']}",
        "- 四週一循環，每週約 30 檔；這是 delta scan，不是每月重寫完整筆記。",
        "- P0/P1 事件與正式期限永遠優先於 cohort。",
        "",
    ]
    for index in range(weeks):
        week = monday + dt.timedelta(days=7 * index)
        label = "ABCD"[((week - ROTATION_ANCHOR).days // 7) % 4]
        members = snapshot["cohorts"][label]
        lines += [
            f"## {week.isoformat()}｜{label} cohort（{len(members)} 檔）",
            "",
        ]
        grouped = defaultdict(list)
        for row in members:
            grouped[row["group"]].append(f"{row['stock_id']} {row['name']}")
        for group_id in sorted(grouped):
            lines.append(f"- **{group_id}：** " + "、".join(grouped[group_id]))
        lines.append("")
    lines += [
        "## 已登錄硬期限",
        "",
        "| 日期 | 正式筆記 | H# | 事件錨點 |",
        "|---|---:|---:|---:|",
    ]
    for due, notes, hypotheses, events in _deadline_rows(snapshot):
        lines.append(f"| {due} | {notes} | {hypotheses} | {events} |")
    return "\n".join(lines) + "\n"


def render_lint(topics, scan):
    lines = []
    error_count = warning_count = 0
    for topic in topics:
        for issue in topic["quality_errors"]:
            lines.append(f"ERROR\t{topic['relpath']}\t{issue}")
            error_count += 1
        for issue in topic["quality_warnings"]:
            lines.append(f"WARN\t{topic['relpath']}\t{issue}")
            warning_count += 1
    for issue in scan["errors"]:
        lines.append(f"ERROR\tnotes/research_topics/scan_log.csv\t{issue}")
        error_count += 1
    lines.append(
        f"研究議題:{len(topics)} 則；scan:{len(scan['rows'])} 筆；"
        f"{error_count} errors，{warning_count} warnings")
    return "\n".join(lines) + "\n", error_count


def _write_output(text, output):
    if output:
        parent = os.path.dirname(os.path.abspath(output))
        os.makedirs(parent, exist_ok=True)
        with open(output, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        print(f"output: {os.path.relpath(output, ROOT)}")
    else:
        print(text, end="")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--attention", action="store_true", help="輸出統一研究待辦（預設）")
    mode.add_argument("--calendar", action="store_true", help="輸出四週循環時間表")
    mode.add_argument("--lint", action="store_true", help="稽核 research_topics 與 scan log")
    parser.add_argument("--as-of", help="台灣研究日 YYYY-MM-DD；預設今天")
    parser.add_argument("--horizon", type=int, default=30, help="待辦前瞻日數")
    parser.add_argument("--weeks", type=int, default=8, help="--calendar 輸出週數")
    parser.add_argument("--db", default=DB, help="正式 SQLite 路徑（唯讀）")
    parser.add_argument("--output", help="UTF-8 輸出檔；省略則印 stdout")
    parser.add_argument("--json", action="store_true", help="--attention 輸出 JSON")
    args = parser.parse_args(argv)

    try:
        as_of = dt.date.fromisoformat(args.as_of) if args.as_of else taipei_today()
    except ValueError:
        parser.error("--as-of 必須是 YYYY-MM-DD")
    if args.horizon < 0:
        parser.error("--horizon 不可小於 0")
    if args.weeks < 1:
        parser.error("--weeks 必須至少 1")

    if args.lint:
        universe_rows = _load_universe()
        notes = load_notes()
        reports = load_reports(notes=notes)
        topics = load_topics(TOPICS_DIR, universe_rows, _load_groups(), reports)
        scan = load_scan_log(SCAN_LOG, [topic["topic_id"] for topic in topics])
        rendered, errors = render_lint(topics, scan)
        _write_output(rendered, args.output)
        return 1 if errors else 0

    snapshot = build_attention(as_of, args.db, args.horizon)
    if args.calendar:
        rendered = render_calendar(snapshot, args.weeks)
    elif args.json:
        rendered = json.dumps(snapshot, ensure_ascii=False, indent=2, default=str) + "\n"
    else:
        rendered = render_attention(snapshot)
    _write_output(rendered, args.output)
    return 1 if snapshot["topic_errors"] or snapshot["scan"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
