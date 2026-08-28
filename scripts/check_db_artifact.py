#!/usr/bin/env python
"""Exercise an artifact against the checked-out commit without replacing its DB."""
from __future__ import annotations

import argparse
import contextlib
import json
import os
from pathlib import Path
import platform
import shutil
import sqlite3
import subprocess
import sys
import zlib

import db_artifact as artifact

ROOT = Path(__file__).resolve().parents[1]


def protected_hashes():
    return {str(path.relative_to(ROOT)): artifact.file_hash(path)
            for path in [ROOT / artifact.DATABASE_PATH, *sorted((ROOT / "archive").rglob("*"))]
            if path.is_file()}


def run_checks(manifest, expected_commit, expected_manifest_sha256, output_dir):
    output_dir = artifact._isolated_path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=False)
    before = protected_hashes()
    report = {"python": sys.version, "platform": platform.platform(),
              "sqlite": sqlite3.sqlite_version, "stdout_encoding": sys.stdout.encoding,
              "utf8_mode": sys.flags.utf8_mode,
              "PYTHONUTF8": os.environ.get("PYTHONUTF8"),
              "source_commit": expected_commit, "checks": {}}
    try:
        head = subprocess.check_output(["git", "--no-replace-objects", "rev-parse", "HEAD"],
                                       cwd=ROOT, text=True).strip()
        if head != expected_commit:
            raise artifact.ArtifactError("Check out the pinned commit before this rehearsal")
        restored = output_dir / "restored.db"
        result = artifact.restore_artifact(
            manifest, restored, expected_commit=expected_commit,
            expected_manifest_sha256=expected_manifest_sha256)
        report["restore"] = result
        if before[artifact.DATABASE_PATH] != result["database_sha256"]:
            raise artifact.ArtifactError("Checked-out DB does not match the restored commit")
        # Independent streaming byte comparison, in addition to SHA validation.
        with restored.open("rb") as left, (ROOT / artifact.DATABASE_PATH).open("rb") as right:
            while True:
                block = left.read(artifact.BLOCK)
                if block != right.read(artifact.BLOCK):
                    raise artifact.ArtifactError("Restored DB differs byte-for-byte")
                if not block:
                    break
        report["byte_equal"] = True
        commands = {
            "raw": ["scripts/audit_raw_data.py", "--db", str(restored)],
            "ranking_oos": ["scripts/audit_ranking_views.py", "--db", str(restored),
                            "--compact", "--require-current-snapshot"],
            "validate": ["scripts/validate.py", "--db", str(restored),
                         "--reports", str(output_dir / "reports")],
            "tests": ["-m", "unittest", "discover", "-s", "tests", "-q"],
        }
        for name, args in commands.items():
            with (output_dir / (name + ".log")).open("wb") as stream:
                process = subprocess.run([sys.executable, *args], cwd=ROOT,
                                         stdout=stream, stderr=subprocess.STDOUT)
            report["checks"][name] = process.returncode
            print(f"{name}: exit {process.returncode}", flush=True)
            if process.returncode:
                raise artifact.ArtifactError(name + " failed; see isolated log")

        # The builder already exposes these module paths; no production code or
        # default path changes are needed. Copy archives, never regenerate history.
        import build_dashboard as dashboard
        outputs = []
        for name, db in (("source", ROOT / artifact.DATABASE_PATH), ("restored", restored)):
            folder = output_dir / name
            folder.mkdir()
            shutil.copytree(ROOT / "archive", folder / "archive")
            dashboard.DB = str(db)
            dashboard.OUT = str(folder / "index.html")
            dashboard.RESEARCH_OUT = str(folder / "research.html")
            dashboard.ARCHIVE = str(folder / "archive")
            archived = {p.name: artifact.file_hash(p) for p in (folder / "archive").glob("*.html")}
            with (output_dir / (name + "_dashboard.log")).open("w", encoding="utf-8") as stream:
                with contextlib.redirect_stdout(stream):
                    dashboard.main()
            if archived != {p.name: artifact.file_hash(p)
                            for p in (folder / "archive").glob("*.html")}:
                raise artifact.ArtifactError("Dashboard changed the as-seen archive inventory")
            outputs.append({file: artifact.file_hash(folder / file)
                            for file in ("index.html", "research.html")})
        report["dashboard_equal"] = outputs[0] == outputs[1]
        report["dashboard_sha256"] = outputs
        if not report["dashboard_equal"]:
            raise artifact.ArtifactError("Source and restored DB generated different HTML")
        if artifact.file_hash(restored) != result["database_sha256"]:
            raise artifact.ArtifactError("A consumer modified the restored database")
        report["ok"] = True
    except Exception as exc:
        report["ok"] = False
        report["error"] = str(exc)
        raise
    finally:
        report["protected_unchanged"] = protected_hashes() == before
        if not report["protected_unchanged"]:
            report["ok"] = False
        (output_dir / "verification.json").write_bytes(
            (json.dumps(report, indent=2, ensure_ascii=True) + "\n").encode())
    if not report["protected_unchanged"]:
        raise artifact.ArtifactError("Production DB or archives changed during rehearsal")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--expected-commit", required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        report = run_checks(args.manifest, args.expected_commit,
                            args.expected_manifest_sha256, args.output_dir)
    except (artifact.ArtifactError, OSError, sqlite3.Error, EOFError, zlib.error,
            subprocess.CalledProcessError) as exc:
        print("Artifact rehearsal failed: " + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(report, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
