#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""本地 daily pipeline：與 GitHub Actions 同序、可安全重複執行。

預設會正式發布 OOS as-seen 快照，但不做 git commit/push。當日上游資料尚未齊全時，
snapshot_signals.py 會讓流程失敗；稍後重跑只補缺口，不重抓已完整資料。
"""
import argparse
import os
import subprocess
import sys


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run(script, *args):
    cmd = [sys.executable, os.path.join(ROOT, "scripts", script), *args]
    print(f"\n▶ {script}", flush=True)
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    ap = argparse.ArgumentParser(description="本地執行可重入的正式 daily pipeline")
    ap.add_argument("--start")
    ap.add_argument("--end")
    ap.add_argument("--days", type=int)
    ap.add_argument("--sleep", type=float)
    ap.add_argument("--datasets")
    ap.add_argument("--stocks")
    ap.add_argument("--force", action="store_true", help="強制重抓指定範圍")
    ap.add_argument("--skip-tdcc", action="store_true", help="略過 TDCC 週快照")
    ap.add_argument("--preview", action="store_true",
                    help="只建立非正式預覽快照；不進 OOS canonical")
    args = ap.parse_args()

    if not args.skip_tdcc:
        run("fetch_tdcc.py")

    fetch_args = []
    for name in ("start", "end", "days", "sleep", "datasets", "stocks"):
        value = getattr(args, name)
        if value is not None:
            fetch_args += [f"--{name}", str(value)]
    if args.force:
        fetch_args.append("--force")
    run("fetch_daily.py", *fetch_args)
    run("score.py")

    snapshot_args = ["--source", "local"]
    if not args.preview:
        snapshot_args.append("--publish")
    run("snapshot_signals.py", *snapshot_args)
    run("build_dashboard.py")
    print("\n本地 daily pipeline 完成；尚未 git commit/push。", flush=True)


if __name__ == "__main__":
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(f"\n流程停止:{os.path.basename(exc.cmd[1])} exit {exc.returncode}", file=sys.stderr)
        raise SystemExit(exc.returncode)
