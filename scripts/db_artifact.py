#!/usr/bin/env python
"""Isolated, offline DB artifact prototype; never restores into production data/."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import subprocess
import sys
import tempfile
import zlib

import db_ro
from audit_storage import file_hash, file_state

ROOT = Path(__file__).resolve().parents[1]
DATABASE_PATH = "data/findmind.db"
MAX_BYTES = 1024 ** 3  # A bounded prototype, not an unlimited decompression service.
BLOCK = 1024 ** 2
MANIFEST_NAME = "manifest.json"


class ArtifactError(ValueError):
    pass


def _hex(value, length, label):
    if not isinstance(value, str) or not re.fullmatch(r"[0-9a-f]{%d}" % length, value):
        raise ArtifactError(f"{label} must be a full lowercase {length}-digit hex value")
    return value


def _isolated_path(path):
    """An accidental-write guard, not a security boundary against local writers."""
    path = Path(path).absolute()
    if path.is_symlink():
        raise ArtifactError("Symlink output is not allowed")
    resolved = path.resolve()
    production = (ROOT / "data").resolve()
    if (str(resolved).casefold() == str(production).casefold()
            or str(resolved).casefold().startswith(str(production).casefold() + os.sep)):
        raise ArtifactError("Production data/ cannot be an artifact or restore destination")
    db = ROOT / DATABASE_PATH
    if path.exists() and db.exists() and path.samefile(db):
        raise ArtifactError("Destination aliases the production database")
    return resolved


def _no_sidecars(path):
    for suffix in ("-wal", "-shm", "-journal"):
        if os.path.lexists(str(path) + suffix):
            raise ArtifactError("SQLite sidecar present; require an offline snapshot: " + suffix)


def sqlite_metadata(path):
    """Inspect a closed snapshot through the repository's enforced read-only entry."""
    _no_sidecars(path)
    with open(path, "rb") as stream:
        header = stream.read(20)
    if header[:16] != b"SQLite format 3\x00" or len(header) != 20:
        raise ArtifactError("Not a SQLite database")
    # Reject WAL before opening: a read-only connection can otherwise try to
    # create missing WAL/SHM bookkeeping, even for an apparently closed main file.
    if 2 in header[18:20]:
        raise ArtifactError("WAL main file is not a complete backup; snapshot it separately")
    con = db_ro.connect(path)
    try:
        mode = con.execute("PRAGMA journal_mode").fetchone()[0]
        if mode == "wal":
            raise ArtifactError("WAL main file is not a complete backup; snapshot it separately")
        if [row[0] for row in con.execute("PRAGMA integrity_check")] != ["ok"]:
            raise ArtifactError("SQLite integrity_check failed")
        pragmas = {name: con.execute("PRAGMA " + name).fetchone()[0]
                   for name in ("schema_version", "user_version", "application_id",
                                "page_size", "page_count")}
        schema = [list(row) for row in con.execute(
            "SELECT type,name,tbl_name,sql FROM sqlite_schema ORDER BY type,name")]
        schema_bytes = json.dumps(schema, ensure_ascii=True, separators=(",", ":")).encode()
        tables = {row[1] for row in schema if row[0] == "table"}
        dates = {name: con.execute("SELECT MAX(date) FROM " + name).fetchone()[0]
                 if name in tables else None for name in ("price", "market", "daily_scores")}
        for value in dates.values():
            if value is not None and (not isinstance(value, str)
                                      or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value)):
                raise ArtifactError("Unexpected data date in snapshot")
        return {**pragmas, "journal_mode": mode,
                "schema_sha256": hashlib.sha256(schema_bytes).hexdigest(),
                "latest_dates": dates}
    finally:
        con.close()


def _copy_stream(source, target, limit=MAX_BYTES):
    count = 0
    digest = hashlib.sha256()
    while block := source.read(min(BLOCK, limit - count + 1)):
        count += len(block)
        if count > limit:
            raise ArtifactError("Payload exceeds its permitted byte length")
        target.write(block)
        digest.update(block)
    return count, digest.hexdigest()


def _fsync(stream):
    stream.flush()
    os.fsync(stream.fileno())


def create_artifact(source_commit, output_dir, *, repo=ROOT):
    """Publish a new bundle from a Git blob, not the potentially changing worktree DB."""
    _hex(source_commit, 40, "source_commit")
    output_dir = _isolated_path(output_dir)
    if output_dir.exists():
        raise ArtifactError("Output directory already exists; use a new version directory")
    output_dir.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".db-artifact-", dir=output_dir.parent) as temp:
        temp = Path(temp)
        source = temp / "snapshot.db"
        # A fixed commit object is required; a tag or mutable branch is not a pin.
        resolved = subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(repo), "rev-parse", "--verify",
             source_commit + "^{commit}"],
            stderr=subprocess.PIPE, text=True).strip()
        if resolved != source_commit:
            raise ArtifactError("source_commit does not identify that exact commit")
        expected_size = int(subprocess.check_output(
            ["git", "--no-replace-objects", "-C", str(repo), "cat-file", "-s",
             source_commit + ":" + DATABASE_PATH], stderr=subprocess.PIPE, text=True).strip())
        if not 0 < expected_size <= MAX_BYTES:
            raise ArtifactError("Snapshot is empty or exceeds the prototype size limit")
        with source.open("xb") as stream:
            subprocess.run(["git", "--no-replace-objects", "-C", str(repo), "cat-file", "blob",
                            source_commit + ":" + DATABASE_PATH],
                           stdout=stream, stderr=subprocess.PIPE, check=True)
        if source.stat().st_size != expected_size:
            raise ArtifactError("Git blob size changed during snapshot extraction")
        before = file_state(source)
        database = {"bytes": source.stat().st_size, "sha256": file_hash(source),
                    "sqlite": sqlite_metadata(source)}
        bundle = temp / "bundle"
        bundle.mkdir()
        filename = database["sha256"] + ".sqlite.gz"
        compressed = bundle / filename
        with source.open("rb") as stream, compressed.open("xb") as out:
            with gzip.GzipFile(filename="", mode="wb", fileobj=out,
                               compresslevel=6, mtime=0) as archive:
                copied, digest = _copy_stream(stream, archive)
            _fsync(out)
        if (file_state(source) != before or copied != database["bytes"]
                or digest != database["sha256"] or file_hash(source) != digest):
            raise ArtifactError("Snapshot changed during compression")
        manifest = {"format_version": 1, "source_commit": source_commit,
                    "database_path": DATABASE_PATH, "database": database,
                    "artifact": {"filename": filename, "compression": "gzip",
                                 "bytes": compressed.stat().st_size,
                                 "sha256": file_hash(compressed)}}
        # Manifest is written only after the complete payload. The bundle becomes
        # visible together via a same-filesystem directory rename, never piecemeal.
        with (bundle / MANIFEST_NAME).open("xb") as stream:
            stream.write((json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode())
            _fsync(stream)
        manifest_sha = file_hash(bundle / MANIFEST_NAME)
        # Exercise the actual restore checks before publishing any pointer.
        restore_artifact(bundle / MANIFEST_NAME, temp / "roundtrip.db",
                         expected_commit=source_commit, expected_manifest_sha256=manifest_sha)
        if output_dir.exists():
            raise ArtifactError("Output appeared while preparing bundle; refusing replacement")
        bundle.rename(output_dir)
    return {"manifest": str(output_dir / MANIFEST_NAME),
            "manifest_sha256": manifest_sha, "source_commit": source_commit,
            "database": database, "artifact": manifest["artifact"]}


def _unique_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ArtifactError("Duplicate JSON key: " + key)
        result[key] = value
    return result


def read_manifest(path, expected_commit, expected_manifest_sha256):
    _hex(expected_commit, 40, "expected_commit")
    _hex(expected_manifest_sha256, 64, "expected_manifest_sha256")
    path = Path(path)
    if path.is_symlink() or not path.is_file() or path.stat().st_size > 65536:
        raise ArtifactError("Manifest must be a small regular file, not a symlink")
    payload = path.read_bytes()
    if hashlib.sha256(payload).hexdigest() != expected_manifest_sha256:
        raise ArtifactError("Manifest SHA-256 does not match the trusted pin")
    try:
        manifest = json.loads(payload, object_pairs_hook=_unique_keys)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ArtifactError("Manifest is not valid UTF-8 JSON") from exc
    try:
        if (type(manifest["format_version"]) is not int or manifest["format_version"] != 1
                or manifest["source_commit"] != expected_commit
                or manifest["database_path"] != DATABASE_PATH):
            raise ArtifactError("Manifest format, source commit or database path mismatch")
        database, artifact = manifest["database"], manifest["artifact"]
        for label, entry in (("database", database), ("artifact", artifact)):
            _hex(entry["sha256"], 64, label + " SHA-256")
            if type(entry["bytes"]) is not int or not 0 < entry["bytes"] <= MAX_BYTES:
                raise ArtifactError(label + " byte length is invalid")
        if (artifact["compression"] != "gzip"
                or artifact["filename"] != database["sha256"] + ".sqlite.gz"
                or not isinstance(database["sqlite"], dict)):
            raise ArtifactError("Unexpected artifact filename, compression or SQLite metadata")
    except (KeyError, TypeError) as exc:
        raise ArtifactError("Incomplete manifest") from exc
    return manifest


def _destination_state(destination):
    _no_sidecars(destination)
    if not destination.exists():
        return None
    if not destination.is_file() or destination.stat().st_nlink != 1:
        raise ArtifactError("Restore destination must be a regular file without hard links")
    sqlite_metadata(destination)
    return file_state(destination), file_hash(destination)


def restore_artifact(manifest_path, destination, *, expected_commit, expected_manifest_sha256):
    """Validate everything in staging before atomically replacing an offline test DB.

    Callers obtain both pins from a trusted channel, not the downloaded manifest.
    This is not a live-database restore, multi-writer lock, or power-loss guarantee.
    """
    destination = _isolated_path(destination)
    manifest_path = Path(manifest_path).absolute()
    manifest = read_manifest(manifest_path, expected_commit, expected_manifest_sha256)
    artifact = manifest["artifact"]
    compressed = manifest_path.parent / artifact["filename"]
    if compressed.is_symlink() or not compressed.is_file():
        raise ArtifactError("Compressed artifact is missing or a symlink")
    if destination in (manifest_path.resolve(), compressed.resolve()):
        raise ArtifactError("Cannot overwrite the artifact or its manifest")
    compressed_state = file_state(compressed)
    if (compressed_state["st_size"] != artifact["bytes"]
            or file_hash(compressed) != artifact["sha256"]):
        raise ArtifactError("Compressed artifact size or SHA-256 mismatch")
    before = _destination_state(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".db-restore-", dir=destination.parent) as temp:
        staged = Path(temp) / "restored.db"
        with gzip.open(compressed, "rb") as stream, staged.open("xb") as out:
            size, digest = _copy_stream(stream, out, manifest["database"]["bytes"])
            _fsync(out)
        if size != manifest["database"]["bytes"] or digest != manifest["database"]["sha256"]:
            raise ArtifactError("Restored database size or SHA-256 mismatch")
        if sqlite_metadata(staged) != manifest["database"]["sqlite"]:
            raise ArtifactError("Restored SQLite schema or data dates mismatch")
        if (file_state(compressed) != compressed_state
                or file_hash(compressed) != artifact["sha256"]
                or file_hash(manifest_path) != expected_manifest_sha256):
            raise ArtifactError("Artifact or manifest changed during restore")
        # Recheck immediately before switching; callers still must exclude writers.
        if _isolated_path(destination) != destination or _destination_state(destination) != before:
            raise ArtifactError("Destination changed during restore; refusing replacement")
        os.replace(staged, destination)
    return {"destination": str(destination), "source_commit": expected_commit,
            "database_sha256": digest, "bytes": size, "sqlite": manifest["database"]["sqlite"]}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("create", help="Publish a new local bundle from a fixed Git commit")
    create.add_argument("--source-commit", required=True)
    create.add_argument("--output-dir", required=True, type=Path)
    restore = commands.add_parser("restore", help="Restore only to an isolated, offline destination")
    restore.add_argument("--manifest", required=True, type=Path)
    restore.add_argument("--destination", required=True, type=Path)
    restore.add_argument("--expected-commit", required=True)
    restore.add_argument("--expected-manifest-sha256", required=True)
    args = parser.parse_args(argv)
    try:
        if args.command == "create":
            result = create_artifact(args.source_commit, args.output_dir)
        else:
            result = restore_artifact(args.manifest, args.destination,
                                      expected_commit=args.expected_commit,
                                      expected_manifest_sha256=args.expected_manifest_sha256)
    except (ArtifactError, OSError, sqlite3.Error, EOFError, zlib.error,
            subprocess.CalledProcessError) as exc:
        print("DB artifact failed: " + str(exc), file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, ensure_ascii=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
