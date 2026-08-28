import contextlib
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import db_artifact as artifact


class DbArtifactTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.db = self.repo / "data/findmind.db"
        self.db.parent.mkdir()
        con = sqlite3.connect(self.db)
        con.executescript("""
            PRAGMA user_version=7;
            CREATE TABLE price(date TEXT, stock_id TEXT, close REAL);
            CREATE TABLE market(date TEXT, taiex REAL);
            CREATE TABLE daily_scores(date TEXT, stock_id TEXT, composite REAL);
            INSERT INTO price VALUES('2026-08-28','3711',100);
            INSERT INTO market VALUES('2026-08-28',30000);
            INSERT INTO daily_scores VALUES('2026-08-28','3711',1);
        """)
        con.close()
        self.git("init", "-q")
        self.commit = self.commit_db()
        self.original = self.db.read_bytes()
        self.bundle = self.root / "bundle"
        self.destination = self.root / "restored.db"
        self.published = artifact.create_artifact(self.commit, self.bundle, repo=self.repo)
        self.manifest_path = self.bundle / artifact.MANIFEST_NAME
        self.manifest = json.loads(self.manifest_path.read_bytes())
        self.compressed = self.bundle / self.manifest["artifact"]["filename"]
        self.pin = self.published["manifest_sha256"]

    def git(self, *args):
        return subprocess.check_output(
            ["git", "-c", "user.name=Artifact Test", "-c", "user.email=test@example.invalid",
             "-c", "commit.gpgsign=false", "-C", str(self.repo), *args],
            stderr=subprocess.PIPE, text=True).strip()

    def commit_db(self):
        self.git("add", "data/findmind.db")
        self.git("commit", "--no-verify", "-qm", "測試資料庫版本")
        return self.git("rev-parse", "HEAD")

    def restore(self, **overrides):
        args = dict(manifest_path=self.manifest_path, destination=self.destination,
                    expected_commit=self.commit, expected_manifest_sha256=self.pin)
        args.update(overrides)
        return artifact.restore_artifact(**args)

    def repin_manifest(self):
        self.manifest_path.write_bytes((json.dumps(self.manifest) + "\n").encode())
        self.pin = hashlib.sha256(self.manifest_path.read_bytes()).hexdigest()

    def assert_safe_failure(self, error=artifact.ArtifactError, **overrides):
        self.destination.write_bytes(self.original)
        before = artifact.file_state(self.destination)
        with self.assertRaises(error):
            self.restore(**overrides)
        self.assertEqual(self.destination.read_bytes(), self.original)
        self.assertEqual(artifact.file_state(self.destination), before)
        self.assertEqual(list(self.root.glob(".db-restore-*")), [])

    def test_publish_restores_exact_bytes_and_records_schema_and_separate_dates(self):
        result = self.restore()
        self.assertEqual(self.destination.read_bytes(), self.original)
        self.assertEqual(result["bytes"], len(self.original))
        self.assertEqual(result["database_sha256"], hashlib.sha256(self.original).hexdigest())
        self.assertEqual(result["sqlite"]["user_version"], 7)
        self.assertEqual(result["sqlite"]["latest_dates"],
                         dict.fromkeys(("price", "market", "daily_scores"), "2026-08-28"))
        self.assertEqual(gzip.decompress(self.compressed.read_bytes()), self.original)
        self.assertEqual(self.db.read_bytes(), self.original)

    def test_create_reads_committed_blob_not_uncommitted_worktree(self):
        con = sqlite3.connect(self.db)
        con.execute("UPDATE price SET close=200")
        con.commit()
        con.close()
        other = self.root / "second"
        packed = artifact.create_artifact(self.commit, other, repo=self.repo)
        self.assertEqual(packed["database"]["sha256"], hashlib.sha256(self.original).hexdigest())
        self.assertEqual(packed["manifest_sha256"], self.pin)
        self.assertNotEqual(self.db.read_bytes(), self.original)

    def test_commit_and_blob_replace_refs_cannot_relabel_other_database_bytes(self):
        con = sqlite3.connect(self.db)
        con.execute("UPDATE price SET close=200")
        con.commit()
        con.close()
        newer = self.commit_db()
        old_blob = self.git("rev-parse", self.commit + ":data/findmind.db")
        new_blob = self.git("rev-parse", newer + ":data/findmind.db")
        for label, old, new in (("commit", self.commit, newer), ("blob", old_blob, new_blob)):
            with self.subTest(label=label):
                self.git("replace", old, new)
                packed = artifact.create_artifact(self.commit, self.root / label, repo=self.repo)
                self.assertEqual(packed["database"]["sha256"], hashlib.sha256(self.original).hexdigest())
                self.assertEqual(packed["source_commit"], self.commit)
                self.git("replace", "-d", old)

    def test_all_database_connections_are_query_only(self):
        original_connect = artifact.db_ro.connect
        checked = []

        def inspect(path):
            con = original_connect(path)
            checked.append(con.execute("PRAGMA query_only").fetchone()[0])
            with self.assertRaises(sqlite3.OperationalError):
                con.execute("DELETE FROM price")
            return con

        with mock.patch.object(artifact.db_ro, "connect", side_effect=inspect):
            self.restore()
        self.assertTrue(checked)
        self.assertTrue(all(value == 1 for value in checked))

    def test_missing_truncated_and_wrong_hash_payload_do_not_replace_good_db(self):
        complete = self.compressed.read_bytes()
        for kind in ("missing", "truncated", "wrong_hash"):
            with self.subTest(kind=kind):
                if kind == "missing":
                    self.compressed.unlink()
                else:
                    self.compressed.write_bytes(complete[:-10] if kind == "truncated"
                                                else bytes([complete[0] ^ 1]) + complete[1:])
                self.assert_safe_failure()
                self.compressed.write_bytes(complete)

    def test_truncated_gzip_with_matching_outer_hash_still_fails_safely(self):
        self.compressed.write_bytes(self.compressed.read_bytes()[:-8])
        self.manifest["artifact"]["bytes"] = self.compressed.stat().st_size
        self.manifest["artifact"]["sha256"] = artifact.file_hash(self.compressed)
        self.repin_manifest()
        self.assert_safe_failure(EOFError)

    def test_invalid_json_and_deflate_return_cli_failure_without_touching_destination(self):
        original = self.compressed.read_bytes()
        self.compressed.write_bytes(original[:10] + bytes([7]) + original[11:])
        self.manifest["artifact"]["sha256"] = artifact.file_hash(self.compressed)
        self.repin_manifest()
        self.destination.write_bytes(self.original)
        command = ["restore", "--manifest", str(self.manifest_path), "--destination",
                   str(self.destination), "--expected-commit", self.commit,
                   "--expected-manifest-sha256"]
        with contextlib.redirect_stderr(io.StringIO()) as error:
            code = artifact.main([*command, self.pin])
        self.assertEqual(code, 2)
        self.assertIn("DB artifact failed", error.getvalue())
        self.assertEqual(self.destination.read_bytes(), self.original)
        for payload in (b"not JSON", b"\xff"):
            self.manifest_path.write_bytes(payload)
            pin = artifact.file_hash(self.manifest_path)
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(artifact.main([*command, pin]), 2)
            self.assertEqual(self.destination.read_bytes(), self.original)

    def test_wrong_inner_hash_size_schema_and_dates_fail_safely(self):
        for change in ("hash", "size", "schema", "date"):
            with self.subTest(change=change):
                self.manifest = json.loads(self.manifest_path.read_bytes())
                original_manifest = json.loads(json.dumps(self.manifest))
                if change == "hash":
                    self.manifest["database"]["sha256"] = "0" * 64
                    renamed = self.bundle / ("0" * 64 + ".sqlite.gz")
                    renamed.write_bytes(self.compressed.read_bytes())
                    self.manifest["artifact"]["filename"] = renamed.name
                elif change == "size":
                    self.manifest["database"]["bytes"] -= 1
                elif change == "schema":
                    self.manifest["database"]["sqlite"]["schema_version"] += 1
                else:
                    self.manifest["database"]["sqlite"]["latest_dates"]["price"] = "2026-08-27"
                self.repin_manifest()
                self.assert_safe_failure()
                self.manifest = original_manifest
                self.repin_manifest()

    def test_bad_or_stale_manifest_pin_and_wrong_commit_fail_safely(self):
        self.assert_safe_failure(expected_manifest_sha256="0" * 64)
        self.assert_safe_failure(expected_commit="0" * 40)
        self.manifest["source_commit"] = "1" * 40
        self.repin_manifest()
        self.assert_safe_failure()

    def test_manifest_rejects_path_traversal_duplicate_keys_bool_size_and_wrong_format(self):
        original = self.manifest_path.read_bytes()
        for change in ("path", "duplicate", "bool", "format", "missing"):
            with self.subTest(change=change):
                self.manifest = json.loads(original)
                if change == "path":
                    self.manifest["artifact"]["filename"] = "../outside.gz"
                elif change == "bool":
                    self.manifest["database"]["bytes"] = True
                elif change == "format":
                    self.manifest["format_version"] = 2
                elif change == "missing":
                    del self.manifest["database"]
                self.repin_manifest()
                if change == "duplicate":
                    self.manifest_path.write_bytes(original.replace(
                        b'"format_version": 1', b'"format_version": 1, "format_version": 1'))
                    self.pin = artifact.file_hash(self.manifest_path)
                self.assert_safe_failure()

    def test_interrupted_staging_preserves_existing_file_and_cleans_temp(self):
        def interrupted(source, target, limit):
            target.write(source.read(100))
            raise OSError("interrupted download/disk write")

        with mock.patch.object(artifact, "_copy_stream", side_effect=interrupted):
            self.assert_safe_failure(OSError)

    def test_atomic_switch_failure_preserves_good_destination(self):
        with mock.patch.object(artifact.os, "replace", side_effect=PermissionError("locked")):
            self.assert_safe_failure(PermissionError)

    def test_new_destination_is_not_created_on_failure(self):
        with self.assertRaises(artifact.ArtifactError):
            self.restore(expected_manifest_sha256="0" * 64)
        self.assertFalse(self.destination.exists())

    def test_existing_sidecars_and_wal_database_are_refused(self):
        for suffix in ("-wal", "-shm", "-journal"):
            with self.subTest(suffix=suffix):
                sidecar = Path(str(self.destination) + suffix)
                sidecar.touch()
                self.assert_safe_failure()
                self.assertTrue(sidecar.exists())
                sidecar.unlink()
        self.destination.write_bytes(self.original)
        con = sqlite3.connect(self.destination)
        con.execute("PRAGMA journal_mode=WAL")
        con.close()
        before = self.destination.read_bytes()
        with self.assertRaisesRegex(artifact.ArtifactError, "WAL"):
            self.restore()
        self.assertEqual(self.destination.read_bytes(), before)

    def test_wal_blob_cannot_be_published_as_complete_backup(self):
        con = sqlite3.connect(self.db)
        con.execute("PRAGMA journal_mode=WAL")
        con.close()
        commit = self.commit_db()
        output = self.root / "wal-bundle"
        with self.assertRaisesRegex(artifact.ArtifactError, "WAL"):
            artifact.create_artifact(commit, output, repo=self.repo)
        self.assertFalse(output.exists())

    def test_production_paths_symlinks_and_hardlinks_are_blocked(self):
        alias = self.root / "alias.db"
        alias.symlink_to(self.db)
        hardlink = self.root / "linked.db"
        os.link(self.db, hardlink)
        with mock.patch.object(artifact, "ROOT", self.repo):
            for path in (self.db, self.db.parent / "new.db", alias, hardlink):
                with self.subTest(path=path):
                    with self.assertRaises(artifact.ArtifactError):
                        self.restore(destination=path)
            with self.assertRaises(artifact.ArtifactError):
                artifact.create_artifact(self.commit, self.db.parent / "bundle", repo=self.repo)
        self.assertEqual(self.db.read_bytes(), self.original)

    def test_artifact_and_manifest_cannot_be_restore_destinations(self):
        for path in (self.manifest_path, self.compressed):
            before = path.read_bytes()
            with self.assertRaises(artifact.ArtifactError):
                self.restore(destination=path)
            self.assertEqual(path.read_bytes(), before)

    def test_publication_failure_leaves_no_partial_bundle_or_manifest(self):
        output = self.root / "failed"
        with mock.patch.object(artifact, "restore_artifact", side_effect=OSError("round-trip failed")):
            with self.assertRaises(OSError):
                artifact.create_artifact(self.commit, output, repo=self.repo)
        self.assertFalse(output.exists())
        self.assertEqual(list(self.root.glob(".db-artifact-*")), [])
        with self.assertRaises(artifact.ArtifactError):
            artifact.create_artifact(self.commit, self.bundle, repo=self.repo)
        self.assertEqual(artifact.file_hash(self.manifest_path), self.pin)

    def test_oversized_git_blob_is_refused_before_writing_snapshot(self):
        output = self.root / "too-large"
        with mock.patch.object(artifact.subprocess, "check_output",
                               side_effect=[self.commit + "\n", str(artifact.MAX_BYTES + 1) + "\n"]), \
             mock.patch.object(artifact.subprocess, "run") as extract:
            with self.assertRaisesRegex(artifact.ArtifactError, "size limit"):
                artifact.create_artifact(self.commit, output, repo=self.repo)
        extract.assert_not_called()
        self.assertFalse(output.exists())
        self.assertEqual(list(self.root.glob(".db-artifact-*")), [])

    def test_destination_replacement_during_validation_is_not_overwritten(self):
        self.destination.write_bytes(self.original)
        original_metadata = artifact.sqlite_metadata

        def replace_destination(path):
            result = original_metadata(path)
            if Path(path).name == "restored.db" and Path(path).parent != self.root:
                replacement = self.root / "other.db"
                replacement.write_bytes(self.original)
                os.replace(replacement, self.destination)
            return result

        with mock.patch.object(artifact, "sqlite_metadata", side_effect=replace_destination):
            with self.assertRaisesRegex(artifact.ArtifactError, "Destination changed"):
                self.restore()
        self.assertEqual(self.destination.read_bytes(), self.original)

    def test_offline_rollback_requires_deliberately_pinning_older_version(self):
        con = sqlite3.connect(self.db)
        con.execute("UPDATE price SET close=200")
        con.commit()
        con.close()
        newer = self.commit_db()
        packed = artifact.create_artifact(newer, self.root / "newer", repo=self.repo)
        self.restore(manifest_path=packed["manifest"], expected_commit=newer,
                     expected_manifest_sha256=packed["manifest_sha256"])
        self.assertEqual(self.destination.read_bytes(), self.db.read_bytes())
        with self.assertRaises(artifact.ArtifactError):
            self.restore(expected_commit=newer)
        self.assertEqual(self.destination.read_bytes(), self.db.read_bytes())
        self.restore()  # Explicit old commit + old manifest pin is the rollback.
        self.assertEqual(self.destination.read_bytes(), self.original)

    def test_cli_json_and_invalid_input_exit(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = artifact.main(["restore", "--manifest", str(self.manifest_path),
                                  "--destination", str(self.destination), "--expected-commit",
                                  self.commit, "--expected-manifest-sha256", self.pin])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["bytes"], len(self.original))
        with contextlib.redirect_stderr(io.StringIO()):
            code = artifact.main(["create", "--source-commit", "HEAD",
                                  "--output-dir", str(self.root / "bad")])
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
