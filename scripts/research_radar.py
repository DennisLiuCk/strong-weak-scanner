#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Structured candidate-research radar for the research center.

The radar is deliberately separate from published topic claims.  It ranks what
deserves research next, while knowledge-graph edges remain constrained to
active claims in a schema-v3 topic or independently verified company note.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
from urllib.parse import urlparse


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
RADAR_DIR = os.path.join(ROOT, "notes", "research_candidates")

META_RE = re.compile(r"<!--\s*research_radar\b(.*?)-->", re.S | re.I)
CANDIDATE_RE = re.compile(r"<!--\s*research_candidate\b(.*?)-->", re.S | re.I)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
CANDIDATE_ID_RE = re.compile(r"RC-[A-Z0-9-]+")
TOPIC_ID_RE = re.compile(r"MI-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+")

PRIORITIES = {"p1", "p2", "p3"}
KNOWLEDGE_VALUES = {"high", "medium", "low"}
STATUSES = {"promoted", "expand_existing", "watch", "deferred"}
EVIDENCE_POSTURES = {"research_grade", "preliminary", "assumption_led"}
ROUTES = {"article_and_graph", "fold_into_graph", "expand_existing_article", "watch_only"}

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


def load_research_radar(
    radar_dir: str = RADAR_DIR,
    *,
    topic_ids: set[str] | None = None,
    graph_ids: set[str] | None = None,
    strict: bool = True,
) -> dict:
    """Load the one active radar and return a dashboard-ready payload."""
    errors: list[str] = []
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
    meta_allowed = {"schema_version", "radar_id", "as_of", "next_review", "status", "method"}
    candidate_allowed = {
        "candidate_id", "rank", "title", "priority", "knowledge_value", "status",
        "evidence_posture", "why_now", "knowledge_gain", "first_rejection",
        "next_evidence", "next_check", "route", "article_topic_id", "graph_id", "sources",
    }
    candidate_required = candidate_allowed - {"article_topic_id", "graph_id"}

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
        for key in meta_allowed:
            if not meta.get(key):
                errors.append(f"{label} meta 缺少欄位：{key}")
        if meta.get("schema_version") != "1":
            errors.append(f"{label} schema_version 必須是 1")
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
        if meta.get("status") == "active":
            active_payloads.append((meta, candidates, label))

    if len(active_payloads) != 1:
        errors.append(f"研究雷達必須剛好有一份 active，目前為 {len(active_payloads)}")

    meta, candidates, source_file = active_payloads[0] if active_payloads else ({}, [], "")
    ids = [row["id"] for row in candidates]
    ranks = [row["rank"] for row in candidates]
    if len(ids) != len(set(ids)):
        errors.append("active 研究雷達 candidate_id 不可重複")
    if len(ranks) != len(set(ranks)):
        errors.append("active 研究雷達 rank 不可重複")
    if ranks and sorted(ranks) != list(range(1, len(ranks) + 1)):
        errors.append("active 研究雷達 rank 必須由 1 連續排列")
    candidates.sort(key=lambda row: row["rank"])

    payload = {
        "schemaVersion": 1,
        "id": meta.get("radar_id", ""),
        "asOf": meta.get("as_of", ""),
        "nextReview": meta.get("next_review", ""),
        "method": meta.get("method", ""),
        "sourceFile": source_file,
        "candidates": candidates,
        "stats": {
            "candidates": len(candidates),
            "promoted": sum(row["status"] == "promoted" for row in candidates),
            "highKnowledge": sum(row["knowledgeValue"] == "high" for row in candidates),
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
            f"{stats['promoted']} 已升格，{stats['highKnowledge']} 個高知識價值"
        )
        for error in payload["errors"]:
            print(f"ERROR：{error}")
    return 1 if payload["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
