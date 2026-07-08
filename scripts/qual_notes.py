#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
qual_notes.py — notes/qualitative/*.md(個股質化筆記:年報 MD&A、法說會重點)狀態追蹤
與骨架建立。純唯讀盤點工具,不抓資料、不生內容——研究與撰寫仍由人工(搭配 Claude)完成,
避免把「需要判斷力」的質化解讀誤做成自動化管線。

每份筆記開頭用 HTML 註解放一個 meta 區塊(GitHub 渲染時隱形):
    <!-- meta
    stock_id: 6525
    template_version: 1
    last_updated: 2026-07-09
    next_review: 2027-03-31
    -->
本檔只認這個區塊,不解析其餘正文結構(業務概況摘要除外,見 _extract_summary)。

狀態判定(對照 config/universe.csv 全量名單):
    missing 尚無筆記檔案
    draft   筆記已建立但 last_updated 留空(骨架階段,尚未填入研究內容)
    fresh   已填入內容,且未過 next_review(或未設 next_review)
    due     已填入內容,但已過 next_review——建議複核,不代表內容過期作廢
另外(不影響上述四態、可疊加):template_version 落後本檔 TEMPLATE_VERSION 常數
→ 代表筆記模板改版後這篇還沒依新版重寫。

「已經更新過的類股不重新整理」的鐵律由這裡的狀態機保證:本檔從不覆寫既有筆記內容,
--new 對已存在的檔案預設拒絕(要覆寫需明确 --force)——重跑與否永遠是人的決定。

用法:
    uv run --no-project python scripts/qual_notes.py                # 全體 universe 狀態總覽
    uv run --no-project python scripts/qual_notes.py --missing       # 只列尚無筆記(全量建立/新增類股用)
    uv run --no-project python scripts/qual_notes.py --stale         # 只列已逾 next_review 的筆記
    uv run --no-project python scripts/qual_notes.py --outdated      # 只列模板版本落後的筆記
    uv run --no-project python scripts/qual_notes.py --new 6525      # 從模板建立骨架(自動帶入 universe.csv 的 name/group/biz)
    uv run --no-project python scripts/qual_notes.py --new 6525 --force  # 覆寫已存在的筆記骨架(內容會被清空,慎用)

build_dashboard.py 會 import 這裡的 load_notes()/note_status()/TEMPLATE_VERSION 把筆記狀態
顯示到儀表板(個股列的「筆記」badge)。
"""
import argparse, csv, glob, os, re, sys
from datetime import date

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
TEMPLATE_MD = os.path.join(NOTES_DIR, "_template.md")
UNIVERSE_CSV = os.path.join(ROOT, "config", "universe.csv")

# 模板結構版本——改了 _template.md 的章節結構就 +1,讓 --outdated 抓出所有舊筆記供覆核重寫。
TEMPLATE_VERSION = 1

_META_RE = re.compile(r"<!--\s*meta\s*(.*?)-->", re.S)
_KV_RE = re.compile(r"^\s*([\w_]+)\s*:\s*(.*?)\s*$")
_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
_SECTION_RE = re.compile(r"^##\s+(.+?)\s*$", re.M)
# 一次掃過**粗體**、[文字](網址) 與裸網址三種行內標記,依出現順序切成 runs——
# 網址字元集刻意排除中文/全形標點,避免緊貼在網址後的「(輸入股號...)」被吃進去
_TOKEN_RE = re.compile(
    r"\*\*(?P<bold>.+?)\*\*"
    r"|\[(?P<ltext>[^\]]+)\]\((?P<lurl>https?://[^\s)]+)\)"
    r"|(?P<url>https?://[A-Za-z0-9\-._~:/?#\[\]@!$&'*+,;=%]+)"
)
_TABLE_SEP_RE = re.compile(r":?-+:?")


def _parse_meta(text):
    m = _META_RE.search(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        km = _KV_RE.match(line)
        if km:
            out[km.group(1)] = km.group(2)
    return out


def _extract_summary(text, limit=160):
    """業務概況第一段,供儀表板 tooltip 當摘要——非完整筆記,只是一眼帶過用。"""
    m = re.search(r"##\s*業務概況\s*\n+(.*?)(?:\n\s*\n|\Z)", text, re.S)
    if not m:
        return ""
    s = re.sub(r"\*\*(.*?)\*\*", r"\1", m.group(1)).strip()
    s = re.sub(r"\n+", "", s)
    return s if len(s) <= limit else s[:limit] + "…"


def _runs(text):
    """一段文字 → [{s, b?, a?}, ...] 行內 runs(b=粗體、a=連結網址),供前端無 innerHTML 組 DOM。"""
    runs, pos = [], 0
    for m in _TOKEN_RE.finditer(text):
        if m.start() > pos:
            runs.append({"s": text[pos:m.start()]})
        if m.group("bold") is not None:
            runs.append({"s": m.group("bold"), "b": True})
        elif m.group("ltext") is not None:
            runs.append({"s": m.group("ltext"), "a": m.group("lurl")})
        else:
            runs.append({"s": m.group("url"), "a": m.group("url")})
        pos = m.end()
    if pos < len(text):
        runs.append({"s": text[pos:]})
    return runs


def _parse_body(text):
    """章節內文(不含 ## 標題)→ blocks:[{t:"p",runs}] / [{t:"ul",items:[runs,...]}] /
    [{t:"table",head:[runs,...],rows:[[runs,...],...]}]。沒有空行分隔的續行(筆記手動軟
    換行,中文不用空白接段)接回目前正在累積的段落或(若有)最後一個 list item——
    不能只認段落續行,否則 bullet 項目軟換行會被切成一句斷在一半的孤兒段落。"""
    lines = text.strip("\n").split("\n")
    blocks, para, items, i, n = [], [], [], 0, len(lines)

    def flush():
        if para:
            blocks.append({"t": "p", "runs": _runs("".join(para))})
            para.clear()
        if items:
            blocks.append({"t": "ul", "items": [_runs(it) for it in items]})
            items.clear()

    while i < n:
        line = lines[i].strip()
        if not line:
            flush()
        elif line.startswith("|"):
            flush()
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            if len(rows) >= 2 and all(_TABLE_SEP_RE.fullmatch(c) for c in rows[1]):
                rows.pop(1)
            blocks.append({"t": "table", "head": [_runs(c) for c in rows[0]],
                            "rows": [[_runs(c) for c in r] for r in rows[1:]]})
            continue
        elif line.startswith("- "):
            items.append(line[2:])
        elif items:
            items[-1] += line       # 續行接回最後一個 list item(無空行分隔)
        else:
            para.append(line)      # 續行接回段落
        i += 1
    flush()
    return blocks


def _extract_sections(text):
    """meta 區塊之後、每個 `## 標題` 章節解析成 {h, blocks}——供儀表板點筆記 badge 展開全文用。"""
    body = _META_RE.sub("", text)
    matches = list(_SECTION_RE.finditer(body))
    out = []
    for idx, m in enumerate(matches):
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(body)
        out.append({"h": m.group(1).strip(), "blocks": _parse_body(body[start:end])})
    return out


def load_notes(notes_dir=NOTES_DIR):
    """回傳 {stock_id: {path, relpath, template_version, last_updated, next_review, summary}}。
    資料夾不存在或無筆記回傳空 dict——不擋 build_dashboard 主管線(同 fund/chip 觀察層的慣例)。"""
    out = {}
    if not os.path.isdir(notes_dir):
        return out
    for path in glob.glob(os.path.join(notes_dir, "*.md")):
        if os.path.basename(path).startswith("_"):   # _template.md 等輔助檔不算筆記
            continue
        text = open(path, encoding="utf-8").read()
        meta = _parse_meta(text)
        sid = meta.get("stock_id") or os.path.basename(path).split("_", 1)[0]
        if not sid:
            continue
        out[sid] = {
            "path": path,
            "relpath": os.path.relpath(path, ROOT).replace("\\", "/"),
            "template_version": int(meta.get("template_version") or 0),
            "last_updated": meta.get("last_updated") or None,
            "next_review": meta.get("next_review") or None,
            "summary": _extract_summary(text),
            "sections": _extract_sections(text),
        }
    return out


def note_status(info, asof):
    """info=None(無筆記)或 load_notes() 的單筆 dict;asof=YYYY-MM-DD 字串比對基準日。"""
    if info is None:
        return "missing"
    lu = info.get("last_updated")
    if not lu or not _DATE_RE.match(lu):
        return "draft"
    nr = info.get("next_review")
    if nr and _DATE_RE.match(nr) and nr < asof:
        return "due"
    return "fresh"


def _load_universe():
    with open(UNIVERSE_CSV, encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("stock_id")]


def _status_rows(asof):
    notes = load_notes()
    rows = []
    for u in _load_universe():
        sid = u["stock_id"]
        info = notes.get(sid)
        rows.append({
            "stock_id": sid, "name": u["name"], "group": u["group"],
            "status": note_status(info, asof),
            "template_old": bool(info and info["template_version"] < TEMPLATE_VERSION),
            "last_updated": (info or {}).get("last_updated") or "-",
            "next_review": (info or {}).get("next_review") or "-",
        })
    return rows


def _scaffold(stock_id, force=False):
    uni = {r["stock_id"]: r for r in _load_universe()}
    if stock_id not in uni:
        print(f"{stock_id} 不在 config/universe.csv,無法帶入 name/group/biz")
        return
    row = uni[stock_id]
    out_path = os.path.join(NOTES_DIR, f"{stock_id}_{row['name']}.md")
    if os.path.exists(out_path) and not force:
        print(f"已存在 {out_path}——已有筆記不重新整理(如確定要覆寫骨架請加 --force)")
        return
    tmpl = open(TEMPLATE_MD, encoding="utf-8").read()
    text = (tmpl.replace("{{STOCK_ID}}", stock_id)
                .replace("{{NAME}}", row["name"])
                .replace("{{GROUP}}", row["group"])
                .replace("{{BIZ}}", row.get("biz", ""))
                .replace("{{TEMPLATE_VERSION}}", str(TEMPLATE_VERSION))
                .replace("{{TODAY}}", date.today().isoformat()))
    os.makedirs(NOTES_DIR, exist_ok=True)
    open(out_path, "w", encoding="utf-8").write(text)
    print(f"已建立骨架 {out_path}——填完研究內容後,記得把 meta 區塊的 "
          f"last_updated / next_review 改成實際日期(否則會一直顯示為 draft)")


STATUS_LABEL = {"missing": "無筆記", "draft": "草稿待填", "fresh": "已更新", "due": "建議複核"}


def main():
    ap = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    ap.add_argument("--asof", help="比對 next_review 用的基準日,預設今天(YYYY-MM-DD)")
    ap.add_argument("--missing", action="store_true", help="只列尚無筆記的股票")
    ap.add_argument("--stale", action="store_true", help="只列已逾 next_review 的筆記")
    ap.add_argument("--outdated", action="store_true", help="只列模板版本落後(模板改版後需重寫)的筆記")
    ap.add_argument("--new", metavar="STOCK_ID", help="從 _template.md 建立新筆記骨架")
    ap.add_argument("--force", action="store_true", help="配合 --new,允許覆寫已存在的筆記")
    args = ap.parse_args()

    if args.new:
        _scaffold(args.new, force=args.force)
        return

    asof = args.asof or date.today().isoformat()
    rows = _status_rows(asof)
    if args.missing:
        rows = [r for r in rows if r["status"] == "missing"]
    elif args.stale:
        rows = [r for r in rows if r["status"] == "due"]
    elif args.outdated:
        rows = [r for r in rows if r["template_old"]]

    if not rows:
        print("(無符合項目)")
        return
    for r in rows:
        flag = " ⚠模板待更新" if r["template_old"] else ""
        print(f"{r['stock_id']}\t{r['name']}\t{r['group']}\t{STATUS_LABEL[r['status']]}\t"
              f"最後更新:{r['last_updated']}\t建議複核:{r['next_review']}{flag}")

    all_rows = _status_rows(asof)
    n_missing = sum(1 for r in all_rows if r["status"] == "missing")
    n_draft = sum(1 for r in all_rows if r["status"] == "draft")
    n_due = sum(1 for r in all_rows if r["status"] == "due")
    print(f"\n共列 {len(rows)} 筆(全 universe {len(all_rows)} 檔:"
          f"缺筆記 {n_missing}、草稿待填 {n_draft}、建議複核 {n_due})")


if __name__ == "__main__":
    main()
