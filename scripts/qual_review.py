#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""focused_v1 機器輔助複核 triage(唯讀,不做簽核、不改任何檔案)。

把獨立複核裡「在 render 裡找數字」這種機械搜尋交給機器,讓 reviewer 把時間
花在只有人能做的判讀(期間/單位/口徑/推論邊界)上:

1. 沿用 `qual_notes._claim_units` 的 claim block 定義解析筆記正文與 [S#] 引用。
2. 用 pdftotext 抽取 evidence pack 各 S# 的 cited/rendered 頁文字(逐頁,離線、同 pack)。
3. 每個 claim 數字對「該 claim 實際引用的 S# 的 cited 頁」做數值比對:
   同單位精確比對、千元↔億元/百萬元/萬元的換算比對(容差=宣告小數位的四捨五入半格)、
   以及 cited 頁上兩數相加的推導比對(捕捉「合計」型主張,如訊芯-KY 案例)。
4. 產出 triage 報告(UTF-8 檔案):
   - HARD:數字只在 rendered 鄰頁、不在 cited 頁命中 → cited_pages 缺頁,依 runbook 退回重建;
   - MISS:cited 頁完全找不到 → reviewer 必須人工重算或目視;
   - DERIVED:兩數相加命中 → reviewer 仍須核對兩個運算元的口徑;
   - HIT:cited 頁命中,附前後文摘錄 → reviewer 就 context 核期間/單位/口徑即可;
   - 高風險詞 claim 清單(第一/唯一/量產/在手訂單…)→ 一律逐字目視原 render;
   - 無文字層頁面清單 → 這些頁必須目視,機器比對對它們無效。

機器命中不是驗證通過:它只回答「這個數字在被引用頁上找得到」,期間、單位、
合併/歸母口徑與事實→推論邊界仍由 reviewer 判讀。品質契約與簽核流程不變
(`review_method` 仍是 offline_evidence_pack_independent_recalculation,本工具
只是該方法中的搜尋輔助)。

exit code:0=無 HARD 項目;1=有 HARD 項目;2=前置條件失敗(找不到筆記/pack/pdftotext)。
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

try:
    from qual_notes import _claim_units, _parse_meta_details
except ModuleNotFoundError:  # 支援以 scripts.qual_review 匯入。
    from scripts.qual_notes import _claim_units, _parse_meta_details

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_DIR = os.path.join(ROOT, "notes", "qualitative")
PACK_ROOT = os.path.join(ROOT, "tmp", "qualitative_evidence", "packs")
REPORT_DIR = os.path.join(ROOT, "tmp", "qualitative_review")

# 數字 token:千分位整數、小數、負號;排除前後緊貼英數字/小數點的片段。
_NUM_RE = re.compile(r"(?<![\w.,])-?\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.,%-])-?\d+(?:\.\d+)?")
# 高風險主張詞:命中的 claim 一律逐字目視原 render,不能只靠數值比對。
RISK_RE = re.compile(
    r"第一|唯一|領先|龍頭|市占|市佔|獨家|量產|試產|在手訂單|急單|認證|導入|打入"
    r"|新高|翻倍|滲透率|寡占|獨供|主要供應商"
)
# 千元敘事常見的放大係數:claim 用大單位(億/百萬/萬),來源表格用千元或元。
_SCALES = (1_000, 10_000, 100_000, 1_000_000, 100_000_000)
# 無文字層判定門檻:抽出字元數低於此值視為掃描頁/圖片頁。
MIN_TEXT_CHARS = 20
CONTEXT_CHARS = 32


def _decimals(raw):
    return len(raw.rsplit(".", 1)[1]) if "." in raw else 0


def _to_value(raw):
    return float(raw.replace(",", ""))


def extract_claim_numbers(text):
    """取 claim 文字中值得核對的數字;略過年份、日期、期間代碼與無單位小整數。"""
    out = []
    for match in _NUM_RE.finditer(text):
        raw = match.group(0)
        before = text[max(0, match.start() - 2):match.start()]
        after = text[match.end():match.end() + 3]
        value = _to_value(raw)
        decimals = _decimals(raw)
        # 日期(2026-07-18)與期間代碼(2026Q1/2026H1/115年度)不是待核數字。
        if after[:1] in "-/" or before[-1:] in "-/":
            continue
        if re.match(r"^[QqHh]\d", after):
            continue
        if decimals == 0 and 1900 <= value <= 2100 and "," not in raw:
            continue
        # 民國年(如 115 年度、114 年 12 月)。
        if (decimals == 0 and 100 <= value <= 150 and "," not in raw
                and after.lstrip()[:1] == "年"):
            continue
        is_pct = after[:1] in "%％"
        # 無小數、無千分位、非百分比的小整數(排名、家數、天數)噪音多於訊號。
        if decimals == 0 and not is_pct and "," not in raw and abs(value) < 100:
            continue
        unit = ""
        unit_match = re.match(r"\s?(億|百萬|萬|千元|元)", after)
        if unit_match:
            unit = unit_match.group(1)
        out.append({
            "raw": raw, "value": value, "decimals": decimals,
            "pct": is_pct, "unit": unit, "pos": match.start(),
        })
    return out


def page_number_tokens(page_text):
    """抽出來源頁的全部數字 token(含原始位置,供 context 摘錄)。"""
    tokens = []
    for match in _NUM_RE.finditer(page_text):
        tokens.append({
            "raw": match.group(0), "value": _to_value(match.group(0)),
            "start": match.start(), "end": match.end(),
        })
    return tokens


def _tolerance(decimals, scale=1):
    return 0.5 * (10 ** -decimals) * scale


def _scales_for(number):
    """依宣告單位限定換算倍率,避免大海撈針式誤命中。
    財報表格慣例是千元或元;百分比永遠不換算。"""
    if number["pct"]:
        return (1,)
    unit = number["unit"]
    if unit == "億":
        return (1, 100_000, 100_000_000)
    if unit == "百萬":
        return (1, 1_000, 1_000_000)
    if unit == "萬":
        return (1, 10, 10_000)
    return (1,)


def match_number(number, tokens):
    """回傳 (token, scale) 命中清單;scale=1 為同單位,>1 為 claim 大單位換算。
    以絕對值比對(財報以括號表達負數,正負號屬 reviewer 判讀的口徑)。"""
    hits = []
    value, decimals = number["value"], number["decimals"]
    money_unit = number["unit"] in ("億", "百萬", "萬")
    for token in tokens:
        for scale in _scales_for(number):
            scaled = abs(value) * scale
            if scale > 1 and (scaled < 1e3 or scaled > 1e13):
                continue
            # 大單位主張直接比對頁上裸小整數(頁碼、註腳)幾乎必是噪音。
            if (money_unit and scale == 1 and "." not in token["raw"]
                    and abs(token["value"]) < 100):
                continue
            if abs(abs(token["value"]) - scaled) <= _tolerance(decimals, scale):
                hits.append((token, scale))
                break
    hits.sort(key=lambda item: item[1])
    return hits


def pairwise_match(number, tokens):
    """cited 頁上兩數相加/相減命中(合計、差額型主張);回傳 (a, op, b, scale)。
    百分比是相除得來的比率,不做加減比對;運算元須達目標一成以上,排除湊數對。"""
    if number["pct"]:
        return []
    value, decimals = number["value"], number["decimals"]
    values = [token for token in tokens if abs(token["value"]) > 0]
    out = []
    for scale in _scales_for(number):
        target = abs(value) * scale
        if target < 1e3 or target > 1e13:
            continue
        tol = _tolerance(decimals, scale)
        floor = target * 0.1
        seen = {}
        for token in values:
            a = abs(token["value"])
            if a < floor:
                continue
            for other in values:
                if other is token or abs(other["value"]) < floor:
                    continue
                b = abs(other["value"])
                if abs(a + b - target) <= tol:
                    key = tuple(sorted((token["raw"], other["raw"]))) + ("+",)
                    seen.setdefault(key, (token, "+", other, scale))
                elif a > b and abs(a - b - target) <= tol:
                    key = (token["raw"], other["raw"], "-")
                    seen.setdefault(key, (token, "-", other, scale))
        out.extend(seen.values())
        if out:
            break
    return out[:3]


def _context(page_text, token):
    start = max(0, token["start"] - CONTEXT_CHARS)
    end = min(len(page_text), token["end"] + CONTEXT_CHARS)
    return re.sub(r"\s+", " ", page_text[start:end]).strip()


def classify_claims(units, docs):
    """核心比對(純函式,方便測試):units 來自 _claim_units,docs 為
    [{id, cited_pages, rendered_pages, page_text: {page: text}}]。"""
    doc_map = {doc["id"]: doc for doc in docs}
    findings = []
    for idx, unit in enumerate(units, 1):
        numbers, seen_numbers = [], set()
        for number in extract_claim_numbers(unit["text"]):
            key = (number["raw"], number["unit"], number["pct"])
            if key not in seen_numbers:
                seen_numbers.add(key)
                numbers.append(number)
        risk_terms = sorted(set(RISK_RE.findall(unit["text"])))
        refs = [ref for ref in unit["refs"] if ref in doc_map]
        unknown_refs = [ref for ref in unit["refs"] if ref not in doc_map]
        results = []
        for number in numbers:
            hit_cited, hit_neighbor, derived = [], [], []
            for ref in refs:
                doc = doc_map[ref]
                cited = set(doc["cited_pages"])
                for page in sorted(doc["page_text"]):
                    text = doc["page_text"][page]
                    hits = match_number(number, page_number_tokens(text))
                    for token, scale in hits:
                        entry = {"sid": ref, "page": page, "scale": scale,
                                 "token": token["raw"], "context": _context(text, token)}
                        (hit_cited if page in cited else hit_neighbor).append(entry)
                if not hit_cited:
                    cited_tokens = []
                    for page in sorted(cited):
                        for token in page_number_tokens(doc["page_text"].get(page, "")):
                            token = dict(token, page=page)
                            cited_tokens.append(token)
                    for a, op, b, scale in pairwise_match(number, cited_tokens):
                        derived.append({"sid": ref, "scale": scale, "op": op,
                                        "operands": (f"{a['raw']}(p.{a['page']})",
                                                     f"{b['raw']}(p.{b['page']})")})
            # 推導命中優先於僅鄰頁:運算元頁已被引用即符合契約(6451 案例準則),
            # 鄰頁字面值只是可補列 cited 的提示;真正的缺頁是連推導都不成立時。
            if hit_cited:
                status = "hit"
            elif derived:
                status = "derived"
            elif hit_neighbor:
                status = "neighbor_only"
            else:
                status = "miss"
            results.append({"number": number, "status": status, "hit_cited": hit_cited[:4],
                            "hit_neighbor": hit_neighbor[:4], "derived": derived})
        findings.append({
            "index": idx, "unit": unit, "numbers": results,
            "risk_terms": risk_terms, "unknown_refs": unknown_refs,
        })
    return findings


# ── 檔案與外部工具 ─────────────────────────────────────────────────


def _find_note(stock_id):
    for name in sorted(os.listdir(NOTES_DIR)):
        if name.startswith(f"{stock_id}_") and name.endswith(".md"):
            return os.path.join(NOTES_DIR, name)
    return None


def _resolve_pdftotext(explicit):
    if explicit:
        return explicit
    found = shutil.which("pdftotext")
    if found:
        return found
    candidates = []
    cache = os.path.join(os.path.expanduser("~"), ".cache", "codex-runtimes")
    if os.path.isdir(cache):
        for base, _dirs, files in os.walk(cache):
            if "pdftotext.exe" in files and re.search(r"[\\/]poppler[\\/]", base):
                candidates.append(os.path.join(base, "pdftotext.exe"))
    git_poppler = r"C:\Program Files\Git\mingw64\bin\pdftotext.exe"
    if os.path.isfile(git_poppler):
        candidates.append(git_poppler)
    return candidates[0] if candidates else None


def _extract_pages(pdftotext, pdf_path, pages):
    out = {}
    for page in sorted(set(pages)):
        result = subprocess.run(
            [pdftotext, "-enc", "UTF-8", "-f", str(page), "-l", str(page),
             str(pdf_path), "-"],
            shell=False, capture_output=True, timeout=60,
        )
        out[page] = result.stdout.decode("utf-8", "replace") if result.returncode == 0 else ""
    return out


def _load_docs(manifest, pack_dir, pdftotext):
    docs, textless = [], []
    for document in manifest["documents"]:
        pdf_path = Path(pack_dir) / document["file"]
        pages = sorted(set(document["cited_pages"]) | set(document["rendered_pages"]))
        page_text = _extract_pages(pdftotext, pdf_path, pages)
        for page, text in page_text.items():
            if len(re.sub(r"\s", "", text)) < MIN_TEXT_CHARS:
                textless.append({"sid": document["id"], "page": page,
                                 "cited": page in document["cited_pages"]})
        docs.append({
            "id": document["id"], "cited_pages": document["cited_pages"],
            "rendered_pages": document["rendered_pages"], "page_text": page_text,
        })
    return docs, textless


def _render_qa(manifest, pack_dir):
    """render PNG 存在性與可疑小檔(近空白)檢查;缺檔屬 HARD。"""
    issues = []
    render_root = Path(pack_dir).parent / "renders" / manifest["pack_sha256"]
    for document in manifest["documents"]:
        for page in document["rendered_pages"]:
            png = render_root / document["id"] / f"p-{page:04d}.png"
            if not png.is_file():
                issues.append({"sid": document["id"], "page": page, "kind": "missing"})
            elif png.stat().st_size < 5_000:
                issues.append({"sid": document["id"], "page": page, "kind": "tiny"})
    return issues


def _format_number(entry):
    number = entry["number"]
    unit = number["unit"] or ("%" if number["pct"] else "")
    return f"`{number['raw']}{unit}`"


def build_report(stock_id, note_path, manifest, findings, textless, render_issues):
    hard, miss, derived, risky = [], [], [], []
    hit_lines = []
    for finding in findings:
        label = f"claim#{finding['index']}"
        excerpt = finding["unit"]["text"][:60]
        if finding["risk_terms"]:
            risky.append(f"- {label}(詞:{'、'.join(finding['risk_terms'])}):{excerpt}…")
        if finding["unknown_refs"]:
            hard.append(f"- {label} 引用了 manifest 沒有的 {','.join(finding['unknown_refs'])}:{excerpt}…")
        for entry in finding["numbers"]:
            num = _format_number(entry)
            if entry["status"] == "neighbor_only":
                pages = "、".join(f"{h['sid']} p.{h['page']}" for h in entry["hit_neighbor"])
                hard.append(f"- {label} {num} 只在鄰頁命中({pages}),cited_pages 缺頁:{excerpt}…")
            elif entry["status"] == "miss":
                kind = "比率類,重算分子/分母" if entry["number"]["pct"] else "人工重算或目視"
                miss.append(f"- {label} {num}({kind};引用 "
                            f"{','.join(finding['unit']['refs']) or '無'}):{excerpt}…")
            elif entry["status"] == "derived":
                ops = ";".join(f"{d['sid']}:{d['operands'][0]}{d['op']}{d['operands'][1]}"
                               f"(×{d['scale']})" for d in entry["derived"][:2])
                note = ""
                if entry["hit_neighbor"]:
                    pages = "、".join(f"{h['sid']} p.{h['page']}" for h in entry["hit_neighbor"][:2])
                    note = f"(字面值另見鄰頁 {pages},可補列 cited 更乾淨)"
                derived.append(f"- {label} {num} ≈ {ops}{note}:{excerpt}…")
            else:
                top = entry["hit_cited"][0]
                scale_note = "" if top["scale"] == 1 else f"(claim×{top['scale']:,})"
                hit_lines.append(f"- {label} {num}{scale_note} @ {top['sid']} p.{top['page']}:"
                                 f"…{top['context']}…")
    textless_cited = [item for item in textless if item["cited"]]
    total_numbers = sum(len(finding["numbers"]) for finding in findings)
    hard_render = [issue for issue in render_issues if issue["kind"] == "missing"]

    lines = [
        f"# {stock_id} 機器輔助複核 triage(產生日 {date.today().isoformat()})",
        "",
        f"- 筆記:`{os.path.relpath(note_path, ROOT)}`;pack `{manifest['pack_sha256'][:16]}…`",
        f"- claim block {len(findings)} 個;待核數字 {total_numbers} 個;"
        f"cited 命中 {len(hit_lines)}、推導命中 {len(derived)}、未命中 {len(miss)}、"
        f"HARD {len(hard) + len(hard_render)}",
        "",
        "機器命中只代表「數字在被引用頁找得到」;期間、單位、合併/歸母口徑與事實→推論",
        "邊界仍由 reviewer 依 context 或原 render 判讀。本報告不進版控。",
        "",
        "## ① HARD:必須先解決才可簽核",
        *(hard or ["- (無)"]),
        *(f"- render 缺檔:{issue['sid']} p.{issue['page']}" for issue in hard_render),
        "",
        "## ② 未命中:人工重算或目視原 render",
        *(miss or ["- (無)"]),
        "",
        "## ③ 推導命中:核對兩個運算元的口徑後放行",
        *(derived or ["- (無)"]),
        "",
        "## ④ 高風險詞 claim:一律逐字目視原 render",
        *(risky or ["- (無)"]),
        "",
        "## ⑤ 無文字層頁面:機器比對無效,必須目視",
        *([f"- {item['sid']} p.{item['page']}{'(cited)' if item['cited'] else '(鄰頁)'}"
           for item in textless] or ["- (無)"]),
        *([f"- 近空白 PNG(疑似壞頁):{issue['sid']} p.{issue['page']}"
           for issue in render_issues if issue["kind"] == "tiny"]),
        "",
        "## ⑥ cited 命中明細(核 context 的期間/單位/口徑)",
        *(hit_lines or ["- (無)"]),
        "",
    ]
    hard_count = len(hard) + len(hard_render)
    return "\n".join(lines), hard_count, {
        "claims": len(findings), "numbers": total_numbers, "hit": len(hit_lines),
        "derived": len(derived), "miss": len(miss), "hard": hard_count,
        "textless_cited": len(textless_cited),
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description="focused_v1 機器輔助複核 triage(唯讀)")
    parser.add_argument("stock_id", help="四位數股號")
    parser.add_argument("--pack-dir", help="evidence pack 目錄(預設依 meta 於 tmp/ 尋找)")
    parser.add_argument("--pdftotext", help="pdftotext 執行檔路徑")
    parser.add_argument("--out", help="triage 報告輸出路徑(預設 tmp/qualitative_review/)")
    args = parser.parse_args(argv)

    note_path = _find_note(args.stock_id)
    if not note_path:
        print(f"[FAIL] no note for {args.stock_id}")
        return 2
    with open(note_path, encoding="utf-8") as handle:
        text = handle.read()
    meta, _meta_errors = _parse_meta_details(text)
    manifest_rel = meta.get("evidence_pack_manifest", "")
    manifest_path = os.path.join(ROOT, manifest_rel)
    if not manifest_rel or not os.path.isfile(manifest_path):
        print(f"[FAIL] evidence manifest missing: {manifest_rel or '-'}")
        return 2
    with open(manifest_path, encoding="utf-8") as handle:
        manifest = json.load(handle)
    if meta.get("evidence_pack_sha256", "") != manifest.get("pack_sha256", ""):
        print("[FAIL] note meta evidence_pack_sha256 != manifest pack_sha256")
        return 2
    pack_dir = args.pack_dir or os.path.join(PACK_ROOT, args.stock_id, manifest["pack_sha256"])
    if not os.path.isdir(pack_dir):
        print(f"[FAIL] pack dir not found: {pack_dir} (pass --pack-dir)")
        return 2
    pdftotext = _resolve_pdftotext(args.pdftotext)
    if not pdftotext:
        print("[FAIL] pdftotext not found (pass --pdftotext)")
        return 2

    units = [unit for unit in _claim_units(text)]
    docs, textless = _load_docs(manifest, pack_dir, pdftotext)
    findings = classify_claims(units, docs)
    render_issues = _render_qa(manifest, pack_dir)
    report, hard_count, stats = build_report(
        args.stock_id, note_path, manifest, findings, textless, render_issues)

    os.makedirs(REPORT_DIR, exist_ok=True)
    out_path = args.out or os.path.join(
        REPORT_DIR, f"{args.stock_id}_review_{date.today().isoformat()}.md")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(report)
    print(f"claims={stats['claims']} numbers={stats['numbers']} hit={stats['hit']} "
          f"derived={stats['derived']} miss={stats['miss']} hard={stats['hard']} "
          f"textless_cited={stats['textless_cited']}")
    print(f"report: {os.path.relpath(out_path, ROOT)}")
    return 1 if hard_count else 0


if __name__ == "__main__":
    sys.exit(main())
