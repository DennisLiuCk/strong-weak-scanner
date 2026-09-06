"""將研究警示合併為有限工作清單；保留全部原始警示、期限與證據狀態。"""
import argparse
import datetime as dt
import json

import research_queue as rq


def build_worklist(snapshot, limit=5, topic_schedule=None):
    if limit < 1:
        raise ValueError("limit 必須至少 1")
    grouped = {}
    for item in snapshot["items"]:
        # 未提供結構化 target 的全域警示保持獨立，不能由自由文字猜股號。
        key = item.get("target") or f"{item['kind']}:{item['detail']}"
        group = grouped.setdefault(key, {"target": key, "items": []})
        if item not in group["items"]:
            group["items"].append(item)
    for group in grouped.values():
        items = group["items"]
        group["priority"] = min(i["priority"] for i in items)
        group["due"] = min(i["due"] for i in items)
        group["financial_update"] = any(i["kind"] == "formal_note_financial_period" for i in items)
        group["hypotheses_due"] = sum(i["kind"] == "hypothesis_due" for i in items)
        group["next_work_check"] = (topic_schedule or {}).get(group["target"])
        # 只延後已由有效 monitor ledger 完成的純議題回查；正式筆記／impact action／P0 不可被順延。
        group["reviewed_waiting"] = bool(
            group["next_work_check"] and group["next_work_check"] > snapshot["as_of"]
            and all(i["kind"] in {"topic_due", "topic_upcoming"} for i in items)
            and group["priority"] != "P0")
        group["reason"] = (
            "先排除品質或正式資料缺口" if group["priority"] == "P0" else
            "已有新季報可複核，合併檢查正式筆記與到期假說" if group["financial_update"] else
            "到期假說須回查原判準與一手證據" if group["hypotheses_due"] else
            "依既有期限完成議題或例行回查")
    ordered = sorted(grouped.values(), key=lambda g: (
        g["priority"], not g["financial_update"], -g["hypotheses_due"], g["due"], g["target"]))
    urgent = [g for g in ordered if g["priority"] == "P0"]
    remaining = [g for g in ordered if g["priority"] != "P0" and not g["reviewed_waiting"]]
    selected = urgent + remaining[:limit]
    return {"as_of": snapshot["as_of"], "raw_alerts": len(snapshot["items"]),
            "work_items": len(ordered), "selected": selected,
            "remaining": len(ordered) - len(selected), "limit": limit,
            "reviewed_waiting": [g for g in ordered if g["reviewed_waiting"]]}


def load_topic_schedule(as_of):
    from research_method_audit import effective_monitor_schedule, load_monitor_reviews
    topics = rq.load_topics(as_of=as_of)
    reviews = load_monitor_reviews(topics, as_of)
    schedule = effective_monitor_schedule(topics, reviews)
    grouped = {}
    for (topic_id, _monitor_id), due in schedule.items():
        grouped.setdefault("topic:" + topic_id, []).append(due)
    return {target: min(dates) for target, dates in grouped.items() if all(dates)}


def render(worklist):
    lines = ["# 研究優先工作清單", "", f"研究日：{worklist['as_of']}", "",
             f"{worklist['raw_alerts']} 條警示合併成 {worklist['work_items']} 件工作；"
             f"本次列出 {len(worklist['selected'])} 件，另 {worklist['remaining']} 件保留原佇列。",
             "P0 全列；其餘同優先級依新季報、到期假說數、原期限排序。"
             "這是工作量普查，不是獨立樣本或投資評分；使用頻率未量測，不參與排序。",
             "合併不等於結案；未找到新證據時保留原文章時鐘，在 monitor review／scan log 記錄回查。", ""]
    for index, group in enumerate(worklist["selected"], 1):
        lines += [f"## {index}. {group['target']} · {group['priority']}", "",
                  f"最早原期限 {group['due']}；{group['reason']}。", ""]
        for item in group["items"]:
            lines.append(f"- `{item['kind']}` {item['due']}：{item['detail']}")
        lines.append("")
    if worklist["reviewed_waiting"]:
        lines += ["## 已回查、等待下一個工作期限", "",
                  "下列只移動工作提醒；原文章證據過期狀態及原期限維持不變。", ""]
        for group in worklist["reviewed_waiting"]:
            lines.append(f"- {group['target']}：下次工作 {group['next_work_check']}；原文章期限 {group['due']}")
    return "\n".join(lines) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--as-of")
    parser.add_argument("--db", default=rq.DB)
    parser.add_argument("--limit", type=int, default=5, help="P0 以外最多列幾件，預設 5")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--output")
    args = parser.parse_args()
    try:
        as_of = dt.date.fromisoformat(args.as_of) if args.as_of else rq.taipei_today()
        snapshot = rq.build_attention(as_of, db_path=args.db)
        worklist = build_worklist(snapshot, args.limit, load_topic_schedule(as_of))
    except ValueError as exc:
        parser.error(str(exc))
    rq._write_output(json.dumps(worklist, ensure_ascii=False, indent=2) + "\n"
                     if args.json else render(worklist), args.output)
    return 1 if snapshot["topic_errors"] or snapshot["scan"]["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
