"""研究發布前共同閘門：先驗 Git 基準，再驗 append-only、測試與隔離重建一致性。"""
import argparse
import contextlib
import datetime as dt
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def resolve_baseline(reference, root=ROOT):
    """不存在或非祖先基準直接失敗，不能以 HEAD／空樹暗中取代。"""
    if not reference or reference.startswith("-"):
        raise ValueError("必須明確指定有效的 baseline-ref")
    result = subprocess.run(["git", "--no-replace-objects", "rev-parse", "--verify", reference + "^{commit}"],
                            cwd=root, capture_output=True, text=True)
    if result.returncode:
        raise ValueError(f"比較基準不存在：{reference}；先取回正確原始 commit，不使用替代基準")
    sha = result.stdout.strip()
    if subprocess.run(["git", "--no-replace-objects", "merge-base", "--is-ancestor", sha, "HEAD"], cwd=root).returncode:
        raise ValueError("比較基準不是 HEAD 祖先，請確認要保護的歷史範圍")
    return sha


def digest(path):
    with Path(path).open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def protected_hashes():
    paths = [ROOT / "data/findmind.db", *sorted((ROOT / "archive").glob("*.html"))]
    return {str(p.relative_to(ROOT)): digest(p) for p in paths}


def verify_build(folder):
    """以 archive 副本重建；不修改首頁、研究頁或正式歷史快照。"""
    import build_dashboard as dashboard
    folder.mkdir()
    shutil.copytree(ROOT / "archive", folder / "archive")
    saved = {key: getattr(dashboard, key) for key in ("OUT", "RESEARCH_OUT", "ARCHIVE")}
    before = {p.name: digest(p) for p in (folder / "archive").glob("*.html")}
    try:
        dashboard.OUT = str(folder / "index.html")
        dashboard.RESEARCH_OUT = str(folder / "research.html")
        dashboard.ARCHIVE = str(folder / "archive")
        with (folder / "build.log").open("w", encoding="utf-8", newline="\n") as log:
            with contextlib.redirect_stdout(log):
                dashboard.main()
    finally:
        for key, value in saved.items():
            setattr(dashboard, key, value)
    after = {p.name: digest(p) for p in (folder / "archive").glob("*.html")}
    if before != after:
        raise ValueError("隔離重建改變 archive：應先由正式每日發布建立新日快照")
    mismatches = [name for name in ("index.html", "research.html") if digest(folder / name) != digest(ROOT / name)]
    if mismatches:
        raise ValueError("產出物與目前來源不一致，先執行 build_dashboard.py：" + ",".join(mismatches))


def run(reference, folder):
    baseline = resolve_baseline(reference)
    folder = Path(folder).resolve()
    if not folder.is_relative_to(ROOT / "tmp"):
        raise ValueError("檢查輸出必須在本專案 tmp/ 內")
    folder.mkdir(parents=True, exist_ok=False)
    before = protected_hashes()
    result = {"baseline": baseline, "python": sys.version, "platform": platform.platform(),
              "utf8_mode": sys.flags.utf8_mode, "PYTHONUTF8": os.environ.get("PYTHONUTF8"),
              "checks": {}, "ok": False}
    commands = {
        "notes": ["scripts/qual_notes.py", "--lint"],
        "hypotheses": ["scripts/leading_hypotheses.py", "--lint"],
        "topic_history": ["scripts/research_queue.py", "--lint", "--baseline-ref", baseline],
        "graph": ["scripts/knowledge_graph.py", "--lint"],
        "radar": ["scripts/research_radar.py", "--lint"],
        "method_history": ["scripts/research_method_audit.py", "--lint", "--baseline-ref", baseline],
        "tests": ["-m", "unittest", "discover", "-s", "tests", "-q"],
    }
    try:
        for name, args in commands.items():
            with (folder / (name + ".log")).open("wb") as log:
                process = subprocess.run([sys.executable, *args], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
            result["checks"][name] = process.returncode
            print(f"{name}: exit {process.returncode}", flush=True)
            if process.returncode:
                raise ValueError(f"{name} 未通過，詳見 {folder / (name + '.log')}")
        verify_build(folder / "build")
        result["checks"]["isolated_build"] = 0
        result["ok"] = True
    except Exception as exc:
        result["error"] = str(exc)
        raise
    finally:
        result["protected_unchanged"] = protected_hashes() == before
        result["ok"] = result["ok"] and result["protected_unchanged"]
        (folder / "verification.json").write_bytes((json.dumps(result, ensure_ascii=True, indent=2) + "\n").encode())
    if not result["ok"]:
        raise ValueError("正式 DB 或 archive 被改動")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline-ref", required=True)
    parser.add_argument("--output-dir", default="tmp/prepublish/" + dt.datetime.now().strftime("%Y%m%d-%H%M%S"))
    args = parser.parse_args()
    try:
        result = run(args.baseline_ref, args.output_dir)
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(1, f"prepublish failed: {exc}\n")
    print(json.dumps(result, ensure_ascii=True, indent=2))


if __name__ == "__main__":
    main()
