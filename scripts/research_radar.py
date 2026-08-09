#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structured candidate-research radar for the research center.

The radar is deliberately separate from published topic claims.  It ranks what
deserves research next, while knowledge-graph edges remain constrained to
active claims in a schema-v3 topic or independently verified company note.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
import json
import os
import re
import sys
from urllib.parse import urlparse


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
RADAR_DIR = os.path.join(ROOT, "notes", "research_candidates")
SELECTION_LOG = os.path.join(RADAR_DIR, "selection_log.csv")
GROUPS_CSV = os.path.join(ROOT, "config", "groups.csv")

META_RE = re.compile(r"<!--\s*research_radar\b(.*?)-->", re.S | re.I)
CANDIDATE_RE = re.compile(r"<!--\s*research_candidate\b(.*?)-->", re.S | re.I)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
CANDIDATE_ID_RE = re.compile(r"RC-[A-Z0-9-]+")
TOPIC_ID_RE = re.compile(r"MI-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+")
SELECTION_ID_RE = re.compile(r"RS-\d{4}-\d{2}-\d{2}-\d{2}-[A-Z0-9-]+")
CYCLE_ID_RE = re.compile(r"RS-\d{4}-\d{2}-\d{2}-\d{2}")
EARLY_TRIGGER_RE = re.compile(
    r"early_trigger:(?P<title>[^@；]+)@(?P<date>\d{4}-\d{2}-\d{2})=>"
    r"(?P<url>https://[^；\s]+)"
)
EARLY_TRIGGER_REQUIRED_FROM = "2026-08-07"

PRIORITIES = {"p1", "p2", "p3"}
KNOWLEDGE_VALUES = {"high", "medium", "low"}
STATUSES = {"promoted", "expand_existing", "watch", "deferred"}
EVIDENCE_POSTURES = {"research_grade", "preliminary", "assumption_led"}
ROUTES = {"article_and_graph", "fold_into_graph", "expand_existing_article", "watch_only"}
SELECTION_DECISIONS = {"advance", "watch", "defer"}
SELECTION_HEADER = (
    "selection_id", "cycle_id", "selected_at", "candidate_id", "rank",
    "priority", "knowledge_value", "evidence_posture", "selection_decision",
    "selection_reason", "first_rejection", "next_evidence",
)

PRIORITY_LABELS = {"p1": "P1 立即研究", "p2": "P2 排程驗證", "p3": "P3 低頻追蹤"}
KNOWLEDGE_LABELS = {"high": "知識價值高", "medium": "知識價值中", "low": "知識價值低"}
STATUS_LABELS = {
    "promoted": "已升格文章＋圖譜",
    "expand_existing": "併入既有研究",
    "watch": "觀察證據成熟度",
    "deferred": "暫緩",
}
EVIDENCE_LABELS = {
    "research_grade": "研究級證據",
    "preliminary": "初步證據",
    "assumption_led": "假設主導",
}


class ResearchRadarError(ValueError):
    """Raised when the candidate radar violates its publishing contract."""


def _parse_fields(body: str, label: str, errors: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if ":" not in line:
            errors.append(f"{label} 欄位必須使用 key: value：{line}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        if key in result:
            errors.append(f"{label} 欄位重複：{key}")
        result[key] = value.strip()
    return result


def _valid_date(value: str) -> bool:
    if not DATE_RE.fullmatch(value or ""):
        return False
    try:
        dt.date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _sources(value: str, label: str, errors: list[str]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for item in [part.strip() for part in (value or "").split("|") if part.strip()]:
        if "=>" not in item:
            errors.append(f"{label} sources 必須使用 標題 => https://URL：{item}")
            continue
        title, url = [part.strip() for part in item.split("=>", 1)]
        parsed = urlparse(url)
        if not title or parsed.scheme != "https" or not parsed.hostname:
            errors.append(f"{label} source 無效：{item}")
            continue
        rows.append({"title": title, "url": url})
    if len(rows) < 2:
        errors.append(f"{label} 至少需要兩個可定位的一手來源")
    if len({row["url"] for row in rows}) != len(rows):
        errors.append(f"{label} sources 不可重複 URL")
    return rows


def _reader_terms(value: str, label: str, errors: list[str]) -> list[dict[str, str]]:
    """Parse editorial term definitions used only by the reader-facing radar card."""
    rows: list[dict[str, str]] = []
    for item in [part.strip() for part in (value or "").split("|") if part.strip()]:
        if "=>" not in item:
            errors.append(f"{label} reader_terms 必須使用 術語 => 白話解釋：{item}")
            continue
        term, explanation = [part.strip() for part in item.split("=>", 1)]
        if not term or not explanation:
            errors.append(f"{label} reader_terms 術語與解釋不可留空：{item}")
            continue
        rows.append({"term": term, "explanation": explanation})
    if value and not 2 <= len(rows) <= 4:
        errors.append(f"{label} reader_terms 必須提供 2–4 個關鍵詞")
    if len({row["term"] for row in rows}) != len(rows):
        errors.append(f"{label} reader_terms 術語不可重複")
    return rows


def _candidate_group_ids(value: str, label: str, errors: list[str]) -> list[str]:
    """Parse formal research-group routes without treating them as beneficiaries."""
    if not value:
        return []
    rows = [item.strip() for item in (value or "").split(",") if item.strip()]
    if value and not 1 <= len(rows) <= 4:
        errors.append(f"{label} group_ids 必須提供 1–4 個正式族群")
    if len(rows) != len(set(rows)):
        errors.append(f"{label} group_ids 不可重複")
    known: set[str] = set()
    try:
        with open(GROUPS_CSV, encoding="utf-8-sig", newline="") as handle:
            known = {
                row.get("group", "").strip()
                for row in csv.DictReader(handle)
                if row.get("group", "").strip()
            }
    except OSError as exc:
        errors.append(f"{label} 無法讀取正式族群設定：{exc}")
    unknown = [item for item in rows if known and item not in known]
    if unknown:
        errors.append(f"{label} group_ids 不在正式族群：{','.join(unknown)}")
    return rows


def _candidate_group_questions(
    value: str,
    group_ids: list[str],
    label: str,
    errors: list[str],
) -> list[dict[str, str]]:
    """Parse one novice-facing research question for every declared group route."""
    rows: list[dict[str, str]] = []
    for item in [part.strip() for part in (value or "").split("|") if part.strip()]:
        if "=>" not in item:
            errors.append(
                f"{label} reader_group_questions 必須使用 group_id => 白話問句：{item}"
            )
            continue
        group_id, question = [part.strip() for part in item.split("=>", 1)]
        if not group_id or not question:
            errors.append(
                f"{label} reader_group_questions 族群與問句不可留空：{item}"
            )
            continue
        if not question.endswith(("？", "?")):
            errors.append(
                f"{label} reader_group_questions 必須是問句：{group_id}"
            )
        rows.append({"groupId": group_id, "question": question})
    ids = [row["groupId"] for row in rows]
    if len(ids) != len(set(ids)):
        errors.append(f"{label} reader_group_questions 族群不可重複")
    if value and ids != group_ids:
        errors.append(
            f"{label} reader_group_questions 必須依 group_ids 順序逐一提供問句"
        )
    return rows


def _valid_timestamp(value: str) -> bool:
    try:
        parsed = dt.datetime.fromisoformat(value)
    except (TypeError, ValueError):
        return False
    return parsed.tzinfo is not None and parsed.utcoffset() == dt.timedelta(hours=8)


def _early_trigger(reason: str, selected_date: str, prior_source_urls: set[str]) -> dict:
    """Parse a frozen early-reselection trigger without pretending it proves the thesis.

    A previously missed source can legitimately trigger an early revisit even when its
    publication date predates the previous selection.  The accountable conditions are
    therefore: a frozen title/date/URL, a date no later than selection, and a URL that
    was not already listed on the prior radar candidate.
    """
    match = EARLY_TRIGGER_RE.search(reason or "")
    if not match:
        return {"documented": False, "valid": False, "title": "", "date": "", "url": ""}
    item = match.groupdict()
    parsed = urlparse(item["url"])
    valid = bool(
        item["title"].strip()
        and _valid_date(item["date"])
        and _valid_date(selected_date)
        and item["date"] <= selected_date
        and parsed.scheme == "https"
        and parsed.hostname
        and item["url"] not in prior_source_urls
    )
    return {"documented": True, "valid": valid, **item}


def _read_selection_text(text: str) -> tuple[list[dict], list[str]]:
    """Parse the append-only, pre-research selection ledger."""
    errors: list[str] = []
    rows: list[dict] = []
    reader = csv.DictReader(io.StringIO(text))
    if tuple(reader.fieldnames or ()) != SELECTION_HEADER:
        return rows, ["selection_log.csv header 不符合契約"]

    seen_ids: set[str] = set()
    cycle_rows: dict[str, list[dict]] = {}
    previous_timestamp = ""
    for line_no, raw in enumerate(reader, 2):
        row = {key: (raw.get(key) or "").strip() for key in SELECTION_HEADER}
        label = f"selection_log.csv line {line_no}"
        if not SELECTION_ID_RE.fullmatch(row["selection_id"]):
            errors.append(f"{label} selection_id 格式錯誤:{row['selection_id'] or '-'}")
        elif row["selection_id"] in seen_ids:
            errors.append(f"{label} selection_id 重複:{row['selection_id']}")
        seen_ids.add(row["selection_id"])
        if not CYCLE_ID_RE.fullmatch(row["cycle_id"]):
            errors.append(f"{label} cycle_id 格式錯誤:{row['cycle_id'] or '-'}")
        elif not row["selection_id"].startswith(f"{row['cycle_id']}-"):
            errors.append(f"{label} selection_id 必須以 cycle_id 開頭")
        if not _valid_timestamp(row["selected_at"]):
            errors.append(f"{label} selected_at 必須是含 +08:00 的 ISO timestamp")
        elif previous_timestamp and row["selected_at"] < previous_timestamp:
            errors.append(f"{label} selected_at 不可早於前一筆")
        previous_timestamp = row["selected_at"] if _valid_timestamp(row["selected_at"]) else previous_timestamp
        if not CANDIDATE_ID_RE.fullmatch(row["candidate_id"]):
            errors.append(f"{label} candidate_id 格式錯誤:{row['candidate_id'] or '-'}")
        try:
            rank = int(row["rank"])
            if rank < 1:
                raise ValueError
        except ValueError:
            rank = 0
            errors.append(f"{label} rank 必須是正整數")
        row["rank"] = rank
        if row["priority"] not in PRIORITIES:
            errors.append(f"{label} priority 不在值域:{row['priority'] or '-'}")
        if row["knowledge_value"] not in KNOWLEDGE_VALUES:
            errors.append(f"{label} knowledge_value 不在值域:{row['knowledge_value'] or '-'}")
        if row["evidence_posture"] not in EVIDENCE_POSTURES:
            errors.append(f"{label} evidence_posture 不在值域:{row['evidence_posture'] or '-'}")
        if row["selection_decision"] not in SELECTION_DECISIONS:
            errors.append(f"{label} selection_decision 不在值域:{row['selection_decision'] or '-'}")
        for key in ("selection_reason", "first_rejection", "next_evidence"):
            if not row[key]:
                errors.append(f"{label} 缺少欄位:{key}")
        rows.append(row)
        cycle_rows.setdefault(row["cycle_id"], []).append(row)

    for cycle_id, items in cycle_rows.items():
        ids = [item["candidate_id"] for item in items]
        ranks = [item["rank"] for item in items]
        timestamps = {item["selected_at"] for item in items}
        if len(ids) != len(set(ids)):
            errors.append(f"{cycle_id} candidate_id 不可重複")
        if sorted(ranks) != list(range(1, len(ranks) + 1)):
            errors.append(f"{cycle_id} rank 必須由 1 連續排列")
        if len(timestamps) != 1:
            errors.append(f"{cycle_id} 同一輪候選必須共用 selected_at")
    return rows, errors


def load_selection_log(path: str = SELECTION_LOG, *, strict: bool = True) -> list[dict]:
    if not os.path.exists(path):
        if strict:
            raise ResearchRadarError(f"找不到 selection log：{path}")
        return []
    with open(path, encoding="utf-8-sig", newline="") as handle:
        rows, errors = _read_selection_text(handle.read())
    if strict and errors:
        raise ResearchRadarError("\n".join(errors))
    return rows


def load_research_radar(
    radar_dir: str = RADAR_DIR,
    *,
    selection_log_path: str | None = None,
    topic_ids: set[str] | None = None,
    graph_ids: set[str] | None = None,
    strict: bool = True,
) -> dict:
    """Load the one active radar and return a dashboard-ready payload."""
    errors: list[str] = []
    selection_rows: list[dict] = []
    selection_log_path = selection_log_path or os.path.join(radar_dir, "selection_log.csv")
    if os.path.exists(selection_log_path):
        with open(selection_log_path, encoding="utf-8-sig", newline="") as handle:
            selection_rows, selection_errors = _read_selection_text(handle.read())
        errors.extend(selection_errors)
    else:
        errors.append(f"找不到 selection log：{selection_log_path}")
    files = []
    if os.path.isdir(radar_dir):
        files = [
            os.path.join(radar_dir, name)
            for name in sorted(os.listdir(radar_dir))
            if name.endswith(".md") and not name.startswith("_")
        ]
    if not files:
        errors.append(f"找不到研究雷達：{radar_dir}")

    active_payloads: list[tuple[dict[str, str], list[dict], str]] = []
    radar_payloads: list[tuple[dict[str, str], list[dict], str]] = []
    meta_allowed = {
        "schema_version", "radar_id", "as_of", "next_review", "status", "method",
        "selection_cycle_id",
    }
    candidate_allowed = {
        "candidate_id", "rank", "title", "priority", "knowledge_value", "status",
        "evidence_posture", "why_now", "knowledge_gain", "first_rejection",
        "next_evidence", "next_check", "route", "article_topic_id", "graph_id", "sources",
        "reader_question", "reader_terms", "reader_next_step", "group_ids",
        "reader_group_questions",
    }
    candidate_required = candidate_allowed - {
        "article_topic_id", "graph_id",
        "reader_question", "reader_terms", "reader_next_step", "group_ids",
        "reader_group_questions",
    }

    for path in files:
        with open(path, encoding="utf-8") as handle:
            text = handle.read()
        label = os.path.relpath(path, ROOT).replace(os.sep, "/")
        metas = META_RE.findall(text)
        if len(metas) != 1:
            errors.append(f"{label} 必須且只能有一個 research_radar")
            continue
        meta = _parse_fields(metas[0], f"{label} meta", errors)
        unknown = set(meta) - meta_allowed
        if unknown:
            errors.append(f"{label} meta 未知欄位：{','.join(sorted(unknown))}")
        for key in meta_allowed - {"selection_cycle_id"}:
            if not meta.get(key):
                errors.append(f"{label} meta 缺少欄位：{key}")
        if meta.get("schema_version") not in {"1", "2"}:
            errors.append(f"{label} schema_version 必須是 1 或 2")
        if meta.get("schema_version") == "2" and not meta.get("selection_cycle_id"):
            errors.append(f"{label} schema 2 必須提供 selection_cycle_id")
        if meta.get("selection_cycle_id") and not CYCLE_ID_RE.fullmatch(meta["selection_cycle_id"]):
            errors.append(f"{label} selection_cycle_id 格式錯誤")
        if meta.get("status") not in {"active", "retired"}:
            errors.append(f"{label} status 不在值域")
        for key in ("as_of", "next_review"):
            if not _valid_date(meta.get(key, "")):
                errors.append(f"{label} {key} 必須是 YYYY-MM-DD")
        if (_valid_date(meta.get("as_of", "")) and _valid_date(meta.get("next_review", ""))
                and meta["next_review"] <= meta["as_of"]):
            errors.append(f"{label} next_review 必須晚於 as_of")

        candidates: list[dict] = []
        for index, body in enumerate(CANDIDATE_RE.findall(text), 1):
            row_label = f"{label} candidate {index}"
            fields = _parse_fields(body, row_label, errors)
            unknown = set(fields) - candidate_allowed
            if unknown:
                errors.append(f"{row_label} 未知欄位：{','.join(sorted(unknown))}")
            for key in sorted(candidate_required):
                if not fields.get(key):
                    errors.append(f"{row_label} 缺少欄位：{key}")
            if meta.get("status") == "active":
                for key in (
                    "reader_question", "reader_terms", "reader_next_step", "group_ids",
                    "reader_group_questions",
                ):
                    if not fields.get(key):
                        errors.append(f"{row_label} active radar 缺少讀者欄位：{key}")
                question = fields.get("reader_question", "")
                if question and not question.endswith(("？", "?")):
                    errors.append(f"{row_label} reader_question 必須是問句")

            candidate_id = fields.get("candidate_id", "")
            if not CANDIDATE_ID_RE.fullmatch(candidate_id):
                errors.append(f"{row_label} candidate_id 格式錯誤：{candidate_id or '-'}")
            try:
                rank = int(fields.get("rank", ""))
                if rank < 1:
                    raise ValueError
            except ValueError:
                rank = 0
                errors.append(f"{row_label} rank 必須是正整數")
            priority = fields.get("priority", "")
            knowledge = fields.get("knowledge_value", "")
            status = fields.get("status", "")
            posture = fields.get("evidence_posture", "")
            route = fields.get("route", "")
            if priority not in PRIORITIES:
                errors.append(f"{row_label} priority 不在值域：{priority or '-'}")
            if knowledge not in KNOWLEDGE_VALUES:
                errors.append(f"{row_label} knowledge_value 不在值域：{knowledge or '-'}")
            if status not in STATUSES:
                errors.append(f"{row_label} status 不在值域：{status or '-'}")
            if posture not in EVIDENCE_POSTURES:
                errors.append(f"{row_label} evidence_posture 不在值域：{posture or '-'}")
            if route not in ROUTES:
                errors.append(f"{row_label} route 不在值域：{route or '-'}")
            next_check = fields.get("next_check", "")
            if not _valid_date(next_check):
                errors.append(f"{row_label} next_check 必須是 YYYY-MM-DD")
            elif _valid_date(meta.get("as_of", "")) and next_check <= meta["as_of"]:
                errors.append(f"{row_label} next_check 必須晚於雷達 as_of")

            article_topic_id = fields.get("article_topic_id", "")
            graph_id = fields.get("graph_id", "")
            if article_topic_id and not TOPIC_ID_RE.fullmatch(article_topic_id):
                errors.append(f"{row_label} article_topic_id 格式錯誤：{article_topic_id}")
            if topic_ids is not None and article_topic_id and article_topic_id not in topic_ids:
                errors.append(f"{row_label} 找不到 article_topic_id：{article_topic_id}")
            if graph_ids is not None and graph_id and graph_id not in graph_ids:
                errors.append(f"{row_label} 找不到 graph_id：{graph_id}")
            if status == "promoted" and (not article_topic_id or not graph_id):
                errors.append(f"{row_label} promoted 必須同時連到文章與圖譜")
            if route == "article_and_graph" and (not article_topic_id or not graph_id):
                errors.append(f"{row_label} article_and_graph 必須同時連到文章與圖譜")
            if route == "fold_into_graph" and not graph_id:
                errors.append(f"{row_label} fold_into_graph 必須提供 graph_id")
            if route == "expand_existing_article" and not article_topic_id:
                errors.append(f"{row_label} expand_existing_article 必須提供 article_topic_id")

            source_rows = _sources(fields.get("sources", ""), row_label, errors)
            reader_terms = _reader_terms(fields.get("reader_terms", ""), row_label, errors)
            group_ids = _candidate_group_ids(fields.get("group_ids", ""), row_label, errors)
            group_questions = _candidate_group_questions(
                fields.get("reader_group_questions", ""), group_ids, row_label, errors,
            )
            candidates.append({
                "id": candidate_id,
                "rank": rank,
                "title": fields.get("title", ""),
                "priority": priority,
                "priorityLabel": PRIORITY_LABELS.get(priority, priority),
                "knowledgeValue": knowledge,
                "knowledgeLabel": KNOWLEDGE_LABELS.get(knowledge, knowledge),
                "status": status,
                "statusLabel": STATUS_LABELS.get(status, status),
                "evidencePosture": posture,
                "evidenceLabel": EVIDENCE_LABELS.get(posture, posture),
                "whyNow": fields.get("why_now", ""),
                "readerQuestion": fields.get("reader_question", ""),
                "readerTerms": reader_terms,
                "readerNextStep": fields.get("reader_next_step", ""),
                "groupIds": group_ids,
                "readerGroupQuestions": group_questions,
                "knowledgeGain": fields.get("knowledge_gain", ""),
                "firstRejection": fields.get("first_rejection", ""),
                "nextEvidence": fields.get("next_evidence", ""),
                "nextCheck": next_check,
                "route": route,
                "articleId": f"topic-{article_topic_id}" if article_topic_id else "",
                "articleTopicId": article_topic_id,
                "graphId": graph_id,
                "sources": source_rows,
            })
        radar_payloads.append((meta, candidates, label))
        if meta.get("status") == "active":
            active_payloads.append((meta, candidates, label))

    if len(active_payloads) != 1:
        errors.append(f"研究雷達必須剛好有一份 active，目前為 {len(active_payloads)}")

    history: list[dict] = []
    for radar_meta, radar_candidates, radar_file in radar_payloads:
        ids = [row["id"] for row in radar_candidates]
        ranks = [row["rank"] for row in radar_candidates]
        prefix = radar_file
        if len(ids) != len(set(ids)):
            errors.append(f"{prefix} candidate_id 不可重複")
        if len(ranks) != len(set(ranks)):
            errors.append(f"{prefix} rank 不可重複")
        if ranks and sorted(ranks) != list(range(1, len(ranks) + 1)):
            errors.append(f"{prefix} rank 必須由 1 連續排列")
        radar_candidates.sort(key=lambda row: row["rank"])

        cycle_id = radar_meta.get("selection_cycle_id", "")
        selected_rows = [row for row in selection_rows if row["cycle_id"] == cycle_id]
        selected_by_id = {row["candidate_id"]: row for row in selected_rows}
        accountable = radar_meta.get("schema_version") != "2"
        if radar_meta.get("schema_version") == "2":
            if not selected_rows:
                errors.append(f"{prefix} 找不到 selection cycle：{cycle_id or '-'}")
            candidate_set = set(ids)
            selection_set = set(selected_by_id)
            accountable = bool(selected_rows and candidate_set == selection_set)
            if candidate_set != selection_set:
                errors.append(
                    f"{prefix} 候選必須等於凍結 selection cycle；"
                    f"雷達獨有 {','.join(sorted(candidate_set - selection_set)) or '無'}；"
                    f"紀錄獨有 {','.join(sorted(selection_set - candidate_set)) or '無'}"
                )
            for candidate in radar_candidates:
                frozen = selected_by_id.get(candidate["id"])
                if not frozen:
                    continue
                for radar_key, selection_key in (
                    ("rank", "rank"), ("priority", "priority"),
                    ("knowledgeValue", "knowledge_value"),
                    ("firstRejection", "first_rejection"),
                    ("nextEvidence", "next_evidence"),
                ):
                    if candidate[radar_key] != frozen[selection_key]:
                        accountable = False
                        errors.append(
                            f"{prefix} {candidate['id']} 的 {radar_key} "
                            "不可改寫研究前凍結值")
                selected_date = frozen["selected_at"][:10]
                if (_valid_date(radar_meta.get("as_of", ""))
                        and selected_date > radar_meta["as_of"]):
                    accountable = False
                    errors.append(
                        f"{prefix} {candidate['id']} selected_at 不可晚於雷達 as_of")
                candidate["selectedAt"] = frozen["selected_at"]
                candidate["selectionDecision"] = frozen["selection_decision"]
                candidate["selectionReason"] = frozen["selection_reason"]
                candidate["initialEvidencePosture"] = frozen["evidence_posture"]
                if frozen["selection_decision"] == "advance":
                    candidate["selectionOutcome"] = (
                        "promoted_after_research" if candidate["status"] == "promoted"
                        else "rejected_after_research"
                    )
                elif frozen["selection_decision"] == "watch":
                    candidate["selectionOutcome"] = (
                        "promoted_from_watch" if candidate["status"] == "promoted"
                        else "remained_watch"
                    )
                else:
                    candidate["selectionOutcome"] = (
                        "promoted_from_defer" if candidate["status"] == "promoted"
                        else "remained_deferred"
                    )
        history.append({
            "id": radar_meta.get("radar_id", ""),
            "schemaVersion": int(radar_meta.get("schema_version") or 1),
            "cycleId": cycle_id,
            "asOf": radar_meta.get("as_of", ""),
            "nextReview": radar_meta.get("next_review", ""),
            "status": radar_meta.get("status", ""),
            "sourceFile": radar_file,
            "candidates": radar_candidates,
            "selectionLog": selected_rows,
            "accountable": accountable,
        })

    early_reselections: list[dict] = []
    occurrences: dict[str, list[dict]] = {}
    for item in history:
        if item["schemaVersion"] != 2:
            continue
        for candidate in item["candidates"]:
            if not candidate.get("selectedAt"):
                continue
            occurrences.setdefault(candidate["id"], []).append({
                "candidate": candidate,
                "cycleId": item["cycleId"],
                "selectedAt": candidate["selectedAt"],
                "nextCheck": candidate["nextCheck"],
                "sourceUrls": {source["url"] for source in candidate.get("sources", [])},
            })
    for candidate_id, items in occurrences.items():
        items.sort(key=lambda row: (row["selectedAt"], row["cycleId"]))
        for prior, current in zip(items, items[1:]):
            selected_date = current["selectedAt"][:10]
            if not (_valid_date(prior["nextCheck"]) and selected_date < prior["nextCheck"]):
                continue
            trigger = _early_trigger(
                current["candidate"].get("selectionReason", ""),
                selected_date,
                prior["sourceUrls"],
            )
            required = selected_date >= EARLY_TRIGGER_REQUIRED_FROM
            if required and not trigger["valid"]:
                errors.append(
                    f"{current['cycleId']} {candidate_id} 在前次 next_check "
                    f"{prior['nextCheck']} 前重選，必須凍結新的 early_trigger:title@date=>https://URL，"
                    "且 URL 不可已存在前輪來源"
                )
            early_reselections.append({
                "candidateId": candidate_id,
                "priorCycleId": prior["cycleId"],
                "cycleId": current["cycleId"],
                "selectedAt": current["selectedAt"],
                "priorNextCheck": prior["nextCheck"],
                "documented": trigger["documented"],
                "valid": trigger["valid"],
                "required": required,
                "grandfathered": not required and not trigger["valid"],
                "triggerTitle": trigger["title"],
                "triggerDate": trigger["date"],
                "triggerUrl": trigger["url"],
            })

    meta, candidates, source_file = active_payloads[0] if active_payloads else ({}, [], "")
    active_history = next(
        (item for item in history if item["sourceFile"] == source_file), {})
    selection_cycle_id = meta.get("selection_cycle_id", "")
    selected = active_history.get("selectionLog", [])

    payload = {
        "schemaVersion": int(meta.get("schema_version") or 1),
        "id": meta.get("radar_id", ""),
        "selectionCycleId": selection_cycle_id,
        "asOf": meta.get("as_of", ""),
        "nextReview": meta.get("next_review", ""),
        "method": meta.get("method", ""),
        "sourceFile": source_file,
        "candidates": candidates,
        "stats": {
            "candidates": len(candidates),
            "promoted": sum(row["status"] == "promoted" for row in candidates),
            "highKnowledge": sum(row["knowledgeValue"] == "high" for row in candidates),
            "selectionFrozen": len(selected),
            "selectedAdvance": sum(row["selection_decision"] == "advance" for row in selected),
            "selectedWatch": sum(row["selection_decision"] == "watch" for row in selected),
            "selectedDefer": sum(row["selection_decision"] == "defer" for row in selected),
        },
        "selectionLog": selected,
        "history": history,
        "earlyReselections": early_reselections,
        "historyStats": {
            "radars": len(history),
            "schema2Cycles": sum(item["schemaVersion"] == 2 for item in history),
            "candidates": sum(len(item["candidates"]) for item in history),
            "accountableSchema2Cycles": sum(
                item["schemaVersion"] == 2 and item["accountable"] for item in history),
            "earlyReselections": len(early_reselections),
            "documentedEarlyTriggers": sum(
                item["valid"] for item in early_reselections),
            "grandfatheredEarlyReselections": sum(
                item["grandfathered"] for item in early_reselections),
        },
        "errors": errors,
    }
    if strict and errors:
        raise ResearchRadarError("\n".join(errors))
    return payload


def _default_refs() -> tuple[set[str], set[str]]:
    from knowledge_graph import build_knowledge_graph, _load_default_context

    topics, notes = _load_default_context()
    graph = build_knowledge_graph(topics, notes, strict=True)
    topic_ids = {topic.get("meta", {}).get("topic_id", "") for topic in topics}
    graph_ids = {item["id"] for item in graph["graphs"]}
    return topic_ids, graph_ids


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="研究候選雷達 lint 與 JSON 輸出")
    parser.add_argument("--lint", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    topic_ids, graph_ids = _default_refs()
    payload = load_research_radar(topic_ids=topic_ids, graph_ids=graph_ids, strict=False)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        stats = payload["stats"]
        print(
            f"research radar：{stats['candidates']} 候選，"
            f"{stats['promoted']} 已升格，{stats['highKnowledge']} 個高知識價值，"
            f"{stats['selectionFrozen']} 個研究前凍結"
        )
        for error in payload["errors"]:
            print(f"ERROR：{error}")
    return 1 if payload["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
