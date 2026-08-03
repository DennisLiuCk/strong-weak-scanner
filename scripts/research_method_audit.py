#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Longitudinal audit for the market-research method.

The topic ledger validates individual articles.  This module validates the
research process across articles without inventing an accuracy rate before
monitor outcomes exist.  Versioned snapshots are immutable baselines; the
monitor-review CSV is append-only and links due monitors to an explicit result.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from collections import Counter


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, SCRIPT_DIR)

from knowledge_graph import (  # noqa: E402
    GRAPH_DIR, HYPOTHESES_DIR, NOTES_DIR, TOPICS_DIR,
    build_knowledge_graph,
)
from leading_hypotheses import load_reports  # noqa: E402
from qual_notes import load_notes  # noqa: E402
from research_queue import (  # noqa: E402
    _source_independence_key, load_scan_log, load_topics, taipei_today,
)
from research_radar import SELECTION_LOG, load_research_radar  # noqa: E402


AUDIT_DIR = os.path.join(ROOT, "notes", "research_method_reviews")
REVIEW_LEDGER = os.path.join(AUDIT_DIR, "monitor_reviews.csv")
SNAPSHOT_RE = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}\.json$")
SNAPSHOT_ID_RE = re.compile(r"^RMA-\d{4}-\d{2}-\d{2}-\d{2}$")
REVIEW_ID_RE = re.compile(r"^MR-\d{4}-\d{2}-\d{2}-[A-Z0-9-]+$")
REVIEW_HEADER = (
    "review_id", "checked_at", "topic_id", "monitor_id", "result",
    "evidence_source_ids", "claim_action", "next_check", "notes",
)
REVIEW_RESULTS = {
    "new_support", "new_contrary", "no_new_evidence", "not_yet_testable",
}
CLAIM_ACTIONS = {
    "none", "new_claim", "superseded", "refuted", "monitor_retired",
}
EVIDENCE_RESULTS = {"new_support", "new_contrary"}
MIN_DESCRIPTIVE_OUTCOMES = 3


class ResearchMethodAuditError(ValueError):
    """Raised when method snapshots or monitor reviews violate the contract."""


def _valid_date(value: str) -> bool:
    try:
        dt.date.fromisoformat(value)
    except (TypeError, ValueError):
        return False
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", value or ""))


def _source_group(source: dict) -> str:
    """與逐篇 topic lint 共用同一個消息鏈邊界，避免總體 gate 高估覆蓋。"""
    return _source_independence_key(source)


def _load_context(as_of: dt.date):
    notes = load_notes(NOTES_DIR)
    reports = load_reports(HYPOTHESES_DIR, notes=notes)
    topics = load_topics(TOPICS_DIR, reports=reports, as_of=as_of)
    graph = build_knowledge_graph(topics, notes, strict=True)
    radar = load_research_radar(
        topic_ids={topic.get("topic_id", "") for topic in topics},
        graph_ids={item["id"] for item in graph["graphs"]},
        strict=True,
    )
    scan = load_scan_log(
        topic_ids={topic.get("topic_id", "") for topic in topics},
        as_of=as_of,
    )
    if scan.get("errors"):
        raise ResearchMethodAuditError("\n".join(scan["errors"]))
    return topics, graph, radar, scan


def _read_review_text(text: str, topics: list[dict], as_of: dt.date) -> tuple[list[dict], list[str]]:
    errors: list[str] = []
    rows: list[dict] = []
    reader = csv.DictReader(io.StringIO(text))
    if tuple(reader.fieldnames or ()) != REVIEW_HEADER:
        errors.append("monitor_reviews.csv header 不符合契約")
        return rows, errors

    topic_by_id = {topic.get("topic_id"): topic for topic in topics}
    seen: set[str] = set()
    previous_date = ""
    for line_no, raw in enumerate(reader, 2):
        row = {key: (raw.get(key) or "").strip() for key in REVIEW_HEADER}
        label = f"monitor_reviews.csv line {line_no}"
        review_id = row["review_id"]
        if not REVIEW_ID_RE.fullmatch(review_id):
            errors.append(f"{label} review_id 格式錯誤:{review_id or '-'}")
        elif review_id in seen:
            errors.append(f"{label} review_id 重複:{review_id}")
        seen.add(review_id)
        if not _valid_date(row["checked_at"]):
            errors.append(f"{label} checked_at 必須是 YYYY-MM-DD")
        elif row["checked_at"] > as_of.isoformat():
            errors.append(f"{label} checked_at 晚於稽核日")
        elif previous_date and row["checked_at"] < previous_date:
            errors.append(f"{label} checked_at 不可早於前一筆")
        previous_date = row["checked_at"] if _valid_date(row["checked_at"]) else previous_date
        if row["result"] not in REVIEW_RESULTS:
            errors.append(f"{label} result 不在值域:{row['result'] or '-'}")
        if row["claim_action"] not in CLAIM_ACTIONS:
            errors.append(f"{label} claim_action 不在值域:{row['claim_action'] or '-'}")
        if not _valid_date(row["next_check"]):
            errors.append(f"{label} next_check 必須是 YYYY-MM-DD")
        elif _valid_date(row["checked_at"]) and row["next_check"] <= row["checked_at"]:
            errors.append(f"{label} next_check 必須晚於 checked_at")

        topic = topic_by_id.get(row["topic_id"])
        if not topic:
            errors.append(f"{label} 找不到 topic_id:{row['topic_id'] or '-'}")
            rows.append(row)
            continue
        monitor = next(
            (item for item in topic.get("monitoring", [])
             if item.get("monitor_id") == row["monitor_id"]), None)
        if not monitor:
            errors.append(f"{label} 找不到 monitor_id:{row['monitor_id'] or '-'}")
        source_ids = [item.strip() for item in row["evidence_source_ids"].split("|") if item.strip()]
        known_sources = {source.get("source_id") for source in topic.get("sources", [])}
        unknown_sources = set(source_ids) - known_sources
        if unknown_sources:
            errors.append(f"{label} evidence_source_ids 找不到:{','.join(sorted(unknown_sources))}")
        if row["result"] in EVIDENCE_RESULTS and not source_ids:
            errors.append(f"{label} {row['result']} 必須引用已登錄 source")
        if row["result"] not in EVIDENCE_RESULTS and source_ids:
            errors.append(f"{label} 無新 evidence 的結果不可刷新 source clock")
        if row["result"] in {"no_new_evidence", "not_yet_testable"} and row["claim_action"] != "none":
            errors.append(f"{label} 無新 evidence 時 claim_action 必須是 none")
        row["evidence_source_ids"] = source_ids
        rows.append(row)
    return rows, errors


def load_monitor_reviews(topics: list[dict], as_of: dt.date, *, strict: bool = True) -> list[dict]:
    if not os.path.exists(REVIEW_LEDGER):
        if strict:
            raise ResearchMethodAuditError(f"找不到 monitor review ledger:{REVIEW_LEDGER}")
        return []
    with open(REVIEW_LEDGER, encoding="utf-8-sig", newline="") as handle:
        text = handle.read()
    rows, errors = _read_review_text(text, topics, as_of)
    if strict and errors:
        raise ResearchMethodAuditError("\n".join(errors))
    return rows


def _registry_fingerprint(
    topics: list[dict], graph: dict, radar: dict, reviews: list[dict], scan: dict,
) -> str:
    def ref_value(ref) -> str:
        return ref.get("ref", "") if isinstance(ref, dict) else str(ref)

    topic_rows = []
    for topic in sorted(topics, key=lambda item: item.get("topic_id", "")):
        topic_rows.append({
            "id": topic.get("topic_id"),
            "status": topic.get("status"),
            "review_due": topic.get("review_due"),
            "sources": [
                [source.get("source_id"), source.get("status"), source.get("accepted_at")]
                for source in topic.get("sources", [])
            ],
            "claims": [
                [claim.get("claim_id"), claim.get("label"), claim.get("status"),
                 claim.get("supporting_source_ids"), claim.get("contrary_source_ids"),
                 claim.get("verification_needed")]
                for claim in topic.get("claims", [])
            ],
            "monitors": [
                [item.get("monitor_id"), item.get("status"), item.get("next_check"),
                 item.get("claim_ids"), item.get("source_ids"), item.get("watch_source_ids")]
                for item in topic.get("monitoring", [])
            ],
        })
    edge_rows = sorted(
        [edge.get("id"), edge.get("status"), edge.get("evidenceState"),
         edge.get("commercialStage"), edge.get("materiality"), edge.get("reviewDue"),
         [ref_value(ref) for ref in edge.get("claimRefs", [])],
         [ref_value(ref) for ref in edge.get("noteRefs", [])]]
        for item in graph.get("graphs", []) for edge in item.get("edges", [])
    )
    radar_rows = [
        [row.get("id"), row.get("rank"), row.get("status"), row.get("evidencePosture"),
         row.get("nextCheck"), row.get("articleTopicId"), row.get("graphId")]
        for row in radar.get("candidates", [])
    ]
    selection_rows = [
        [row.get("selection_id"), row.get("cycle_id"), row.get("selected_at"),
         row.get("candidate_id"), row.get("rank"), row.get("priority"),
         row.get("knowledge_value"), row.get("evidence_posture"),
         row.get("selection_decision"), row.get("selection_reason"),
         row.get("first_rejection"), row.get("next_evidence")]
        for row in radar.get("selectionLog", [])
    ]
    scan_rows = [
        [row.get("scan_id"), row.get("window_start"), row.get("window_end"),
         row.get("scanned_at"), row.get("scope"), row.get("source_domains"),
         row.get("result_topic_ids"), row.get("next_scan_due"), row.get("coverage_note")]
        for row in sorted(scan.get("rows", []), key=lambda item: item.get("scan_id", ""))
    ]
    payload = {
        "topics": topic_rows,
        "edges": edge_rows,
        "radar": radar_rows,
        "selectionLog": selection_rows,
        "reviews": reviews,
        "scanLog": scan_rows,
    }
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def compute_method_audit(
    topics: list[dict], graph: dict, radar: dict, reviews: list[dict], scan: dict,
    as_of: dt.date,
) -> dict:
    active_topics = [topic for topic in topics if topic.get("status") not in {"dismissed", "resolved"}]
    active_claims = [
        claim for topic in active_topics for claim in topic.get("claims", [])
        if claim.get("status") == "active"
    ]
    active_sources = [
        source for topic in active_topics for source in topic.get("sources", [])
        if source.get("status") == "active"
    ]
    active_monitors = [
        (topic, monitor) for topic in active_topics for monitor in topic.get("monitoring", [])
        if monitor.get("status") == "active"
    ]
    graph_edges = [
        edge for item in graph.get("graphs", []) for edge in item.get("edges", [])
        if edge.get("status") == "active"
    ]
    date_text = as_of.isoformat()
    mature_monitors = [
        (topic, monitor) for topic, monitor in active_monitors
        if _valid_date(monitor.get("next_check")) and monitor["next_check"] <= date_text
    ]
    review_groups: dict[tuple[str, str], list[dict]] = {}
    for row in reviews:
        review_groups.setdefault((row["topic_id"], row["monitor_id"]), []).append(row)
    effective_due: dict[tuple[str, str], str] = {}
    mature_review_events = 0
    for topic, monitor in active_monitors:
        pair = (topic.get("topic_id"), monitor.get("monitor_id"))
        expected_due = monitor.get("next_check", "")
        for row in review_groups.get(pair, []):
            if _valid_date(expected_due) and row["checked_at"] >= expected_due:
                mature_review_events += 1
            expected_due = row["next_check"]
        effective_due[pair] = expected_due
    mature_monitors = [
        (topic, monitor) for topic, monitor in active_monitors
        if _valid_date(effective_due[(topic.get("topic_id"), monitor.get("monitor_id"))])
        and effective_due[(topic.get("topic_id"), monitor.get("monitor_id"))] <= date_text
    ]
    overdue_monitors = [
        (topic, monitor) for topic, monitor in mature_monitors
        if effective_due[(topic.get("topic_id"), monitor.get("monitor_id"))] < date_text
    ]
    result_counts = Counter(row["result"] for row in reviews)
    evidence_outcomes = result_counts["new_support"] + result_counts["new_contrary"]

    claim_counts = Counter(claim.get("label") for claim in active_claims)
    source_complete = sum(
        bool(source.get("locator") and source.get("limitation")) for source in active_sources
    )
    boundary_complete = sum(bool(claim.get("boundary")) for claim in active_claims)
    unverified_claims = [claim for claim in active_claims if claim.get("label") == "unverified"]
    verification_complete = sum(bool(claim.get("verification_needed")) for claim in unverified_claims)
    monitor_watch_complete = 0
    for topic, monitor in active_monitors:
        source_by_id = {source.get("source_id"): source for source in topic.get("sources", [])}
        if any((source_by_id.get(source_id) or {}).get("source_kind") == "living_index"
               for source_id in monitor.get("watch_source_ids", [])):
            monitor_watch_complete += 1

    thesis_cross_checked = 0
    theses_needing_second_group: list[str] = []
    for topic in active_topics:
        thesis_id = (topic.get("meta") or {}).get("thesis_claim_id")
        thesis = next((claim for claim in topic.get("claims", [])
                       if claim.get("claim_id") == thesis_id), {})
        source_by_id = {source.get("source_id"): source for source in topic.get("sources", [])}
        thesis_source_ids = {
            source_id
            for key in ("supporting_source_ids", "contrary_source_ids")
            for source_id in thesis.get(key, [])
        }
        groups = {
            _source_group(source_by_id[source_id])
            for source_id in thesis_source_ids
            if source_id in source_by_id and source_by_id[source_id].get("status") == "active"
        }
        if len(groups) >= 2:
            thesis_cross_checked += 1
        else:
            theses_needing_second_group.append(topic.get("topic_id") or "-")
    theses_needing_second_group.sort()

    graph_traceable = sum(bool(edge.get("claimRefs") or edge.get("noteRefs")) for edge in graph_edges)
    stale_edges = sum(
        _valid_date(edge.get("reviewDue")) and edge["reviewDue"] < date_text
        for edge in graph_edges
    )
    stale_topics = sum(bool((topic.get("confidence") or {}).get("stale")) for topic in active_topics)
    corrected_claims = [
        claim for topic in topics for claim in topic.get("claims", [])
        if claim.get("status") in {"superseded", "refuted"}
    ]
    comparisons = [item for topic in topics for item in topic.get("comparisons", [])]
    scan_rows = scan.get("rows", [])
    full_scans = [row for row in scan_rows if row.get("scope") == "full"]
    partial_scans = [row for row in scan_rows if row.get("scope") == "partial"]
    latest_scan = scan.get("latest") or {}
    # scan row 是歷史事件，不是會被關閉的 work item。若把每一列的舊期限都累加，
    # 已完成的掃描也會永久顯示逾期。現階段只量最新一輪的全域 cadence；個別 scope
    # 是否被後續掃描覆蓋，必須等 scan lineage 契約後才能誠實量化。
    overdue_scans = [latest_scan] if (
        _valid_date(latest_scan.get("next_scan_due"))
        and latest_scan["next_scan_due"] < date_text
    ) else []

    radar_candidates = radar.get("stats", {}).get("candidates", 0)
    frozen_selections = radar.get("stats", {}).get("selectionFrozen", 0)
    selection_advance = radar.get("stats", {}).get("selectedAdvance", 0)
    promoted_after_research = sum(
        row.get("selectionOutcome") == "promoted_after_research"
        for row in radar.get("candidates", [])
    )
    rejected_after_research = sum(
        row.get("selectionOutcome") == "rejected_after_research"
        for row in radar.get("candidates", [])
    )
    selection_accountable = bool(
        radar.get("schemaVersion") == 2
        and radar_candidates
        and frozen_selections == radar_candidates
    )

    trace_ok = graph_traceable == len(graph_edges) and boundary_complete == len(active_claims)
    cross_check_ok = not theses_needing_second_group
    falsifiable_ok = (
        all(sum(item.get("status") == "active" for item in topic.get("monitoring", [])) >= 2
            for topic in active_topics)
        and verification_complete == len(unverified_claims)
        and monitor_watch_complete == len(active_monitors)
    )
    if mature_monitors:
        correction_status = "attention"
        correction_observed = f"{len(mature_monitors)} 個 monitor 目前待回顧；歷史已完成 {mature_review_events} 次到期回顧；累積 {len(corrected_claims)} 個已修正 claim"
    elif mature_review_events:
        correction_status = "pass"
        correction_observed = f"目前沒有待回顧 monitor；歷史已完成 {mature_review_events} 次到期回顧；累積 {len(corrected_claims)} 個已修正 claim"
    else:
        correction_status = "not_ready"
        correction_observed = f"尚無到期 review event；不能把未被檢驗視為成功；累積 {len(corrected_claims)} 個已修正 claim"

    descriptive_ready = (
        not mature_monitors
        and mature_review_events > 0
        and evidence_outcomes >= MIN_DESCRIPTIVE_OUTCOMES
    )
    support_rate = (
        round(result_counts["new_support"] / evidence_outcomes, 4)
        if descriptive_ready and evidence_outcomes else None
    )

    core = {
        "schemaVersion": 1,
        "asOf": date_text,
        "methodologyVersion": "1.4",
        "registryFingerprint": _registry_fingerprint(topics, graph, radar, reviews, scan),
        "scope": {
            "topics": len(topics),
            "activeTopics": len(active_topics),
            "radarCandidates": radar.get("stats", {}).get("candidates", 0),
            "promotedCandidates": radar.get("stats", {}).get("promoted", 0),
            "graphs": graph.get("stats", {}).get("graphs", 0),
            "scanEvents": len(scan_rows),
        },
        "selection": {
            "cycleId": radar.get("selectionCycleId", ""),
            "candidates": radar_candidates,
            "frozenBeforeResearch": frozen_selections,
            "advanceDecisions": selection_advance,
            "promotedAfterResearch": promoted_after_research,
            "rejectedAfterResearch": rejected_after_research,
            "accountable": selection_accountable,
            "boundary": "凍結紀錄只能證明選擇與拒絕條件可被事後稽核；升格是研究產出，不是選題正確率或投資命中率。",
        },
        "claims": {
            "active": len(active_claims),
            "verified": claim_counts["verified"],
            "inference": claim_counts["inference"],
            "unverified": claim_counts["unverified"],
            "withBoundary": boundary_complete,
            "unverifiedWithNextEvidence": verification_complete,
            "comparisonObservations": len(comparisons),
        },
        "sources": {
            "active": len(active_sources),
            "withLocatorAndLimitation": source_complete,
            "thesesWithTwoIndependentGroups": thesis_cross_checked,
            "activeTheses": len(active_topics),
            "thesesNeedingSecondIndependentGroup": theses_needing_second_group,
        },
        "monitors": {
            "active": len(active_monitors),
            "withLivingWatchSource": monitor_watch_complete,
            "dueOrOverdue": len(mature_monitors),
            "overdue": len(overdue_monitors),
            "reviewedMature": mature_review_events,
        },
        "freshness": {
            "staleTopics": stale_topics,
            "staleEdges": stale_edges,
        },
        "scans": {
            "events": len(scan_rows),
            "full": len(full_scans),
            "partial": len(partial_scans),
            "overdue": len(overdue_scans),
            "latestAt": latest_scan.get("scanned_at"),
            "latestId": latest_scan.get("scan_id"),
            "latestScope": latest_scan.get("scope"),
        },
        "corrections": {
            "supersededOrRefutedClaims": len(corrected_claims),
            "monitorReviewEvents": len(reviews),
            "resultCounts": {key: result_counts[key] for key in sorted(REVIEW_RESULTS)},
        },
        "calibration": {
            "evidenceBearingOutcomes": evidence_outcomes,
            "minimumOutcomesForDescriptiveRate": MIN_DESCRIPTIVE_OUTCOMES,
            "descriptiveRateReady": descriptive_ready,
            "supportRate": support_rate,
            "boundary": "此處只描述到期 monitor 的證據結果，不是投資命中率、報酬率或因果效果。",
        },
        "graphs": {
            "activeEdges": len(graph_edges),
            "traceableEdges": graph_traceable,
            "verified": sum(edge.get("evidenceState") == "verified" for edge in graph_edges),
            "inference": sum(edge.get("evidenceState") == "inference" for edge in graph_edges),
            "unverified": sum(edge.get("evidenceState") == "unverified" for edge in graph_edges),
            "financialMateriality": sum(edge.get("materiality") == "financial" for edge in graph_edges),
        },
        "gates": [
            {
                "id": "selection_accountability", "label": "選題前承諾",
                "status": "pass" if selection_accountable else "attention",
                "observed": (
                    f"{frozen_selections}/{radar_candidates} 個本輪候選有研究前凍結；"
                    f"{selection_advance} 個 advance 中 {promoted_after_research} 個完成升格、"
                    f"{rejected_after_research} 個研究後拒絕"
                ),
                "boundary": "通過只代表初始排名、第一拒絕與下一份證據沒有被事後改寫；不能由單輪升格率判定方法有效。",
            },
            {
                "id": "traceability", "label": "可追溯性",
                "status": "pass" if trace_ok else "attention",
                "observed": f"{graph_traceable}/{len(graph_edges)} 條圖譜線可回查；{boundary_complete}/{len(active_claims)} 個 active claim 有邊界",
                "boundary": "通過代表引用完整，不代表主張一定為真。",
            },
            {
                "id": "cross_check_depth", "label": "獨立交叉驗證",
                "status": "pass" if cross_check_ok else "attention",
                "observed": f"{thesis_cross_checked}/{len(active_topics)} 個主命題有至少兩條獨立來源鏈；缺口 {','.join(theses_needing_second_group) or '無'}",
                "boundary": "兩條獨立消息鏈只能降低單一來源偏誤，不代表主張一定為真。",
            },
            {
                "id": "falsifiability", "label": "可證偽性",
                "status": "pass" if falsifiable_ok else "attention",
                "observed": f"{monitor_watch_complete}/{len(active_monitors)} 個 monitor 有 living watch source；{verification_complete}/{len(unverified_claims)} 個待驗證 claim 寫明下一份證據",
                "boundary": "Monitor 完整不等於結果已成熟。",
            },
            {
                "id": "freshness", "label": "新鮮度",
                "status": "attention" if stale_topics or stale_edges or overdue_monitors else "pass",
                "observed": f"{stale_topics} 篇 topic、{stale_edges} 條 edge 過期；{len(overdue_monitors)} 個 monitor 逾期",
                "boundary": "過期會降可信度，但不自動判定主張錯誤。",
            },
            {
                "id": "correction_learning", "label": "修正學習",
                "status": correction_status,
                "observed": correction_observed,
                "boundary": "沒有新證據必須留下 no_new_evidence，而不能刷新 evidence clock。",
            },
            {
                "id": "scan_accountability", "label": "掃描覆蓋問責",
                "status": "pass" if full_scans and not overdue_scans else "attention",
                "observed": f"{len(scan_rows)} 次掃描：{len(full_scans)} 次 full、{len(partial_scans)} 次 partial；最新 cadence 逾期 {len(overdue_scans)} 次；最新 {latest_scan.get('scan_id') or '無'}",
                "boundary": "Partial 只證明指定來源與題材已查過，不能證明全市場沒有其他重要主題；逾期只檢查最新全域 cadence，尚未量化每個歷史 scope 是否被後續掃描覆蓋；通過也不代表每則公告都被正確解讀。",
            },
            {
                "id": "calibration", "label": "校準可用性",
                "status": "pass" if descriptive_ready else "not_ready",
                "observed": f"{evidence_outcomes} 個具新證據的到期結果；最低揭露門檻 {MIN_DESCRIPTIVE_OUTCOMES}",
                "boundary": "樣本不足時不報支持率；即使可報也只附樣本數，不稱為投資命中率。",
            },
        ],
        "caveats": [
            "選題前凍結與升格結果分開保存；至少累積多輪到期結果前，不計算選題命中率。",
            "升格候選數是研究流程產出，不是研究正確率。",
            "獨立來源鏈覆蓋是交叉檢查深度，不是多數決或真實性分數。",
            "尚未到期或 not_yet_testable 的 monitor 不能算支持或反對。",
            "no_new_evidence 是一次有紀錄的檢查，不得刷新 claim 的證據時鐘。",
            "Partial scan 不等於全 universe 或全市場覆蓋；研究漏網風險必須持續顯示。",
            "Scan overdue 目前只量最新全域 cadence；尚無 scope lineage 前，不把歷史期限累加成永久逾期。",
        ],
    }
    return core


def _snapshot_paths() -> list[str]:
    if not os.path.isdir(AUDIT_DIR):
        return []
    return [
        os.path.join(AUDIT_DIR, name)
        for name in sorted(os.listdir(AUDIT_DIR))
        if SNAPSHOT_RE.fullmatch(name)
    ]


def load_snapshots(*, strict: bool = True) -> list[dict]:
    errors: list[str] = []
    snapshots: list[dict] = []
    seen_ids: set[str] = set()
    previous_key = ("", "")
    for path in _snapshot_paths():
        try:
            with open(path, encoding="utf-8") as handle:
                item = json.load(handle)
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{os.path.basename(path)} 無法讀取:{exc}")
            continue
        snapshot_id = item.get("snapshotId", "")
        if item.get("schemaVersion") != 1:
            errors.append(f"{os.path.basename(path)} schemaVersion 必須是 1")
        if not SNAPSHOT_ID_RE.fullmatch(snapshot_id):
            errors.append(f"{os.path.basename(path)} snapshotId 格式錯誤")
        elif snapshot_id in seen_ids:
            errors.append(f"snapshotId 重複:{snapshot_id}")
        seen_ids.add(snapshot_id)
        if not _valid_date(item.get("asOf", "")):
            errors.append(f"{os.path.basename(path)} asOf 格式錯誤")
        key = (item.get("asOf", ""), snapshot_id)
        if key <= previous_key:
            errors.append("method audit snapshots 必須依 asOf／sequence 遞增")
        previous_key = key
        snapshots.append(item)
    if strict and errors:
        raise ResearchMethodAuditError("\n".join(errors))
    return snapshots


def load_method_audit(*, strict: bool = True) -> dict:
    snapshots = load_snapshots(strict=strict)
    if not snapshots:
        if strict:
            raise ResearchMethodAuditError("找不到 research method audit snapshot")
        return {}
    latest = dict(snapshots[-1])
    latest["history"] = [
        {
            "snapshotId": item.get("snapshotId"),
            "asOf": item.get("asOf"),
            "topics": (item.get("scope") or {}).get("topics", 0),
            "matureMonitors": (item.get("monitors") or {}).get("dueOrOverdue", 0),
            "reviewEvents": (item.get("corrections") or {}).get("monitorReviewEvents", 0),
        }
        for item in snapshots
    ]
    return latest


def _baseline_errors(baseline_ref: str) -> list[str]:
    errors: list[str] = []
    prefix = "notes/research_method_reviews/"
    try:
        listed = subprocess.run(
            ["git", "ls-tree", "-r", "--name-only", baseline_ref, prefix],
            cwd=ROOT, text=True, capture_output=True, check=True,
        ).stdout.splitlines()
    except subprocess.CalledProcessError as exc:
        return [f"無法讀取 baseline {baseline_ref}:{exc.stderr.strip()}"]
    for relpath in listed:
        if not (relpath.endswith(".json") or relpath.endswith("monitor_reviews.csv")):
            continue
        try:
            old = subprocess.run(
                ["git", "show", f"{baseline_ref}:{relpath}"], cwd=ROOT,
                text=True, encoding="utf-8", capture_output=True, check=True,
            ).stdout
        except subprocess.CalledProcessError as exc:
            errors.append(f"無法讀取 baseline 檔案 {relpath}:{exc.stderr.strip()}")
            continue
        current_path = os.path.join(ROOT, relpath.replace("/", os.sep))
        if not os.path.exists(current_path):
            errors.append(f"歷史 method audit 檔案不可刪除:{relpath}")
            continue
        with open(current_path, encoding="utf-8-sig", newline="") as handle:
            current = handle.read()
        if relpath.endswith(".json") and current != old:
            errors.append(f"歷史 method audit snapshot 不可改寫:{relpath}")
        elif relpath.endswith("monitor_reviews.csv"):
            old_lines = old.splitlines()
            current_lines = current.splitlines()
            if current_lines[:len(old_lines)] != old_lines:
                errors.append("monitor_reviews.csv 必須 append-only，既有列不可改寫或刪除")
    selection_relpath = os.path.relpath(SELECTION_LOG, ROOT).replace(os.sep, "/")
    try:
        old_selection = subprocess.run(
            ["git", "show", f"{baseline_ref}:{selection_relpath}"], cwd=ROOT,
            text=True, encoding="utf-8", capture_output=True, check=True,
        ).stdout
    except subprocess.CalledProcessError:
        old_selection = ""
    if old_selection:
        if not os.path.exists(SELECTION_LOG):
            errors.append("歷史 selection_log.csv 不可刪除")
        else:
            with open(SELECTION_LOG, encoding="utf-8-sig", newline="") as handle:
                current_selection = handle.read()
            old_lines = old_selection.splitlines()
            current_lines = current_selection.splitlines()
            if current_lines[:len(old_lines)] != old_lines:
                errors.append("selection_log.csv 必須 append-only，研究前凍結列不可改寫或刪除")
    return errors


def _suggest_snapshot_id(as_of: dt.date) -> str:
    existing = [item for item in load_snapshots(strict=False) if item.get("asOf") == as_of.isoformat()]
    return f"RMA-{as_of.isoformat()}-{len(existing) + 1:02d}"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="研究方法長期稽核與 append-only 快照驗證")
    parser.add_argument("--lint", action="store_true")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--baseline-ref")
    args = parser.parse_args(argv)
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    as_of = taipei_today()
    errors: list[str] = []
    try:
        topics, graph, radar, scan = _load_context(as_of)
        reviews = load_monitor_reviews(topics, as_of, strict=True)
        current = compute_method_audit(topics, graph, radar, reviews, scan, as_of)
    except (ResearchMethodAuditError, ValueError) as exc:
        print(f"ERROR：{exc}")
        return 1

    snapshots = load_snapshots(strict=False)
    if args.lint:
        if not snapshots:
            errors.append("至少需要一份 method audit snapshot")
        else:
            latest = snapshots[-1]
            if latest.get("registryFingerprint") != current.get("registryFingerprint"):
                errors.append("研究 registry 已變動，必須新增 method audit snapshot；不可沿用舊基線")
        if args.baseline_ref:
            errors.extend(_baseline_errors(args.baseline_ref))

    if args.json:
        payload = dict(current)
        payload["snapshotId"] = _suggest_snapshot_id(as_of)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(
            f"research method audit：{current['scope']['topics']} topics，"
            f"{current['claims']['active']} active claims，"
            f"{current['monitors']['dueOrOverdue']} due monitors，"
            f"{current['corrections']['monitorReviewEvents']} review events"
        )
        for gate in current["gates"]:
            print(f"{gate['status'].upper()}\t{gate['label']}\t{gate['observed']}")
        for error in errors:
            print(f"ERROR：{error}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
