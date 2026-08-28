#!/usr/bin/env python
"""Read-only SQLite size census and optional in-memory gzip round-trip probe."""
import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import platform
import sqlite3
import sys

import db_ro

ROOT = Path(__file__).resolve().parent.parent
MIB = 1024 * 1024
WARNING_BYTES = 50 * MIB
LIMIT_BYTES = 100 * MIB


def file_hash(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for block in iter(lambda: stream.read(MIB), b""):
            digest.update(block)
    return digest.hexdigest()


def file_state(path):
    stat = path.stat()
    return {name: getattr(stat, name)
            for name in ("st_dev", "st_ino", "st_size", "st_mtime_ns", "st_ctime_ns")}


def size_status(size):
    if size > LIMIT_BYTES:
        return "blocked"
    if size > WARNING_BYTES:
        return "warning"
    return "ok"


def table_allocations(con):
    """Group dbstat allocation by owning table, including its indexes."""
    schema = {r["name"]: (r["tbl_name"], r["type"])
              for r in con.execute("SELECT name,tbl_name,type FROM sqlite_schema")}
    owners = {}
    # Table-valued syntax fails if a user table shadows the virtual dbstat module.
    for row in con.execute("SELECT name,SUM(pgsize) AS bytes FROM dbstat('main') GROUP BY name"):
        owner, kind = schema.get(row["name"], (row["name"], "internal"))
        item = owners.setdefault(owner, {"name": owner, "table_bytes": 0,
                                         "index_bytes": 0, "total_bytes": 0})
        item["index_bytes" if kind == "index" else "table_bytes"] += row["bytes"]
        item["total_bytes"] += row["bytes"]
    return sorted(owners.values(), key=lambda row: (-row["total_bytes"], row["name"]))


def gzip_probe(path):
    """Compress in memory; compare restored bytes with the observed source."""
    buffer = io.BytesIO()
    source = hashlib.sha256()
    with open(path, "rb") as stream, gzip.GzipFile(
        filename="", mode="wb", fileobj=buffer, compresslevel=6, mtime=0
    ) as compressed:
        for block in iter(lambda: stream.read(MIB), b""):
            source.update(block)
            compressed.write(block)
    compressed_size = buffer.tell()
    buffer.seek(0)
    restored = hashlib.sha256()
    restored_bytes = 0
    with gzip.GzipFile(fileobj=buffer, mode="rb") as stream:
        for block in iter(lambda: stream.read(MIB), b""):
            restored.update(block)
            restored_bytes += len(block)
    return {"level": 6, "mtime": 0, "compressed_bytes": compressed_size,
            "restored_bytes": restored_bytes, "source_sha256": source.hexdigest(),
            "restored_sha256": restored.hexdigest(),
            "round_trip_ok": source.hexdigest() == restored.hexdigest()}


def audit_storage(db, *, probe_gzip=False):
    db = Path(db).resolve()
    state_before = file_state(db)
    before = file_hash(db)
    size = state_before["st_size"]
    wal = Path(str(db) + "-wal")
    wal_state_before = file_state(wal) if wal.exists() else None
    wal_before = file_hash(wal) if wal_state_before is not None else None
    report = {
        "db": str(db), "bytes": size, "mib": size / MIB,
        "size_status": size_status(size), "warning_bytes": WARNING_BYTES,
        "limit_bytes": LIMIT_BYTES, "headroom_bytes": LIMIT_BYTES - size,
        "errors": [], "warnings": [],
        "environment": {"python": platform.python_version(), "platform": platform.platform(),
                        "sqlite": sqlite3.sqlite_version, "stdout_encoding": sys.stdout.encoding},
    }
    con = db_ro.connect(db)
    try:
        con.execute("BEGIN")
        report["sqlite"] = {
            name: con.execute("PRAGMA " + name).fetchone()[0]
            for name in ("page_size", "page_count", "freelist_count", "query_only", "journal_mode")
        }
        report["sqlite"]["freelist_bytes"] = (
            report["sqlite"]["freelist_count"] * report["sqlite"]["page_size"])
        report["sqlite"]["logical_bytes"] = (
            report["sqlite"]["page_count"] * report["sqlite"]["page_size"])
        try:
            report["tables"] = table_allocations(con)
        except sqlite3.OperationalError as exc:
            if not any(text in str(exc).lower()
                       for text in ("no such table: dbstat", "no such module: dbstat")):
                raise
            report["tables"] = None
            report["warnings"].append("dbstat unavailable: " + str(exc))
    finally:
        con.close()
    if report["size_status"] == "warning":
        report["warnings"].append("Database exceeds GitHub's 50 MiB warning threshold.")
    elif report["size_status"] == "blocked":
        report["errors"].append("Database exceeds GitHub's 100 MiB regular-Git file limit.")
    if report["sqlite"]["journal_mode"] == "wal":
        report["warnings"].append("WAL database: the main file alone is not a verified backup.")
    logical_size_valid = (
        report["sqlite"]["journal_mode"] == "wal" or report["sqlite"]["logical_bytes"] <= size)
    if not logical_size_valid:
        report["errors"].append("SQLite page census exceeds the observed main-file size.")
    elif report["sqlite"]["journal_mode"] != "wal":
        trailing = size - report["sqlite"]["logical_bytes"]
        report["sqlite"]["trailing_bytes"] = trailing
        if trailing:
            report["warnings"].append(f"Main file has {trailing} trailing bytes outside the page census.")
    if probe_gzip:
        if report["sqlite"]["journal_mode"] == "wal" or wal_before is not None:
            report["errors"].append("Gzip probe refused for WAL; use a separate consistent snapshot.")
        else:
            report["gzip"] = gzip_probe(db)
            if (not report["gzip"]["round_trip_ok"]
                    or report["gzip"]["source_sha256"] != before
                    or report["gzip"]["restored_bytes"] != size):
                report["errors"].append("Gzip did not restore the originally observed database bytes.")
    after = file_hash(db)
    wal_after = file_hash(wal) if wal.exists() else None
    state_after = file_state(db)
    wal_state_after = file_state(wal) if wal.exists() else None
    report["db_sha256"] = before
    report["file_observations"] = {
        "db_before": state_before, "db_after": state_after,
        "wal_before": wal_state_before, "wal_after": wal_state_after,
    }
    report["consistent_observation"] = (
        before == after and wal_before == wal_after
        and state_before == state_after and wal_state_before == wal_state_after
        and logical_size_valid)
    if not report["consistent_observation"]:
        report["errors"].append("Database/WAL changed during observation; discard and retry.")
    return report


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=ROOT / "data/findmind.db")
    parser.add_argument("--gzip-probe", action="store_true", help="In-memory gzip and SHA-256 restore check")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        report = audit_storage(args.db, probe_gzip=args.gzip_probe)
    except (OSError, sqlite3.Error) as exc:
        print("Storage audit failed: " + str(exc), file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=True))
    else:
        print(f"SQLite: {report['mib']:.2f} MiB ({report['bytes']} bytes); {report['size_status']}")
        print(f"Freelist: {report['sqlite']['freelist_bytes']} bytes")
        for row in (report["tables"] or [])[:10]:
            print(f"  {row['name']}: {row['total_bytes'] / MIB:.2f} MiB including indexes")
        if "gzip" in report:
            print(f"Gzip: {report['gzip']['compressed_bytes'] / MIB:.2f} MiB; "
                  f"round_trip_ok={report['gzip']['round_trip_ok']}")
        for kind in ("warnings", "errors"):
            for message in report[kind]:
                print(f"{kind.upper()}: {message}")
    return 1 if report["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
