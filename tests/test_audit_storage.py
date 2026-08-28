import contextlib
import gzip
import hashlib
import io
import json
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import audit_storage as storage


class StorageAuditTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.db = Path(self.temp.name) / "fixture.db"
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE samples(id INTEGER PRIMARY KEY, payload TEXT)")
        con.execute("CREATE INDEX samples_payload ON samples(payload)")
        con.executemany("INSERT INTO samples VALUES(?,?)",
                        [(i, "sample-" + str(i) + "-" + "x" * 200) for i in range(80)])
        con.commit()
        con.close()

    def test_census_keeps_bytes_and_accounts_for_indexes(self):
        before = self.db.read_bytes()
        report = storage.audit_storage(self.db)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(report["bytes"], len(before))
        self.assertEqual(report["sqlite"]["page_size"] * report["sqlite"]["page_count"], len(before))
        self.assertEqual(report["sqlite"]["query_only"], 1)
        self.assertTrue(report["consistent_observation"])
        self.assertEqual(report["errors"], [])
        if report["tables"] is not None:
            sample = next(r for r in report["tables"] if r["name"] == "samples")
            self.assertGreater(sample["index_bytes"], 0)
            self.assertEqual(sample["total_bytes"], sample["table_bytes"] + sample["index_bytes"])

    def test_gzip_probe_matches_independent_bytes_and_creates_no_files(self):
        before = self.db.read_bytes()
        names = sorted(p.name for p in self.db.parent.iterdir())
        report = storage.audit_storage(self.db, probe_gzip=True)
        probe = report["gzip"]
        expected_hash = hashlib.sha256(before).hexdigest()
        self.assertEqual(probe["source_sha256"], expected_hash)
        self.assertEqual(probe["restored_sha256"], expected_hash)
        self.assertEqual(probe["restored_bytes"], len(before))
        self.assertEqual(probe["compressed_bytes"], len(gzip.compress(before, compresslevel=6, mtime=0)))
        self.assertEqual(sorted(p.name for p in self.db.parent.iterdir()), names)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(report["errors"], [])

    def test_thresholds_use_bytes_and_only_exceeding_is_flagged(self):
        for size, expected in (
            (50 * storage.MIB, "ok"),
            (50 * storage.MIB + 1, "warning"),
            (100 * storage.MIB, "warning"),
            (100 * storage.MIB + 1, "blocked"),
        ):
            with self.subTest(size=size):
                self.assertEqual(storage.size_status(size), expected)

    def test_missing_dbstat_is_explicit_and_does_not_break_size_census(self):
        with mock.patch.object(storage, "table_allocations",
                               side_effect=sqlite3.OperationalError("no such table: dbstat")):
            report = storage.audit_storage(self.db)
        self.assertIsNone(report["tables"])
        self.assertTrue(any("dbstat unavailable" in text for text in report["warnings"]))
        self.assertEqual(report["bytes"], self.db.stat().st_size)
        self.assertEqual(report["errors"], [])

    def test_wal_probe_refused_instead_of_claiming_complete_backup(self):
        writer = sqlite3.connect(self.db)
        try:
            writer.execute("PRAGMA journal_mode=WAL")
            writer.execute("INSERT INTO samples VALUES(1000,'pending-in-wal')")
            writer.commit()
            with mock.patch.object(storage, "gzip_probe") as probe:
                report = storage.audit_storage(self.db, probe_gzip=True)
            probe.assert_not_called()
            self.assertTrue(any("WAL" in text for text in report["errors"]))
            self.assertNotIn("gzip", report)
        finally:
            writer.close()

    def test_unexpected_sql_error_is_not_downgraded_to_missing_dbstat(self):
        with mock.patch.object(storage, "table_allocations",
                               side_effect=sqlite3.OperationalError("interrupted")):
            with self.assertRaises(sqlite3.OperationalError):
                storage.audit_storage(self.db)

    def test_user_table_cannot_supply_fake_dbstat_allocations(self):
        con = sqlite3.connect(self.db)
        con.execute("CREATE TABLE dbstat(name TEXT, pgsize INTEGER)")
        con.execute("INSERT INTO dbstat VALUES('invented_owner',123456789)")
        con.commit()
        con.close()
        with contextlib.redirect_stderr(io.StringIO()) as error:
            code = storage.main(["--db", str(self.db), "--json"])
        self.assertEqual(code, 2)
        self.assertIn("dbstat", error.getvalue())

    def test_atomic_replacement_then_restored_bytes_is_not_consistent(self):
        original_bytes = self.db.read_bytes()
        replacement = self.db.parent / "replacement.db"
        replacement.write_bytes(original_bytes)
        con = sqlite3.connect(replacement)
        con.execute("INSERT INTO samples VALUES(1000,zeroblob(200000))")
        con.commit()
        con.close()
        original_connect = storage.db_ro.connect
        original_hash = storage.file_hash
        hash_calls = 0

        def connect_replacement(path):
            os.replace(replacement, path)
            return original_connect(path)

        def restore_before_last_hash(path):
            nonlocal hash_calls
            hash_calls += 1
            if hash_calls == 2:
                restored = self.db.parent / "restored.db"
                restored.write_bytes(original_bytes)
                os.replace(restored, path)
            return original_hash(path)

        with mock.patch.object(storage.db_ro, "connect", side_effect=connect_replacement), \
             mock.patch.object(storage, "file_hash", side_effect=restore_before_last_hash):
            report = storage.audit_storage(self.db)
        self.assertEqual(self.db.read_bytes(), original_bytes)
        self.assertFalse(report["consistent_observation"])
        self.assertTrue(any("page census" in text for text in report["errors"]))
        self.assertTrue(any("changed during observation" in text for text in report["errors"]))

    def test_change_during_probe_invalidates_measurement(self):
        original = storage.gzip_probe

        def update_after_probe(path):
            result = original(path)
            writer = sqlite3.connect(path)
            writer.execute("UPDATE samples SET payload='changed' WHERE id=1")
            writer.commit()
            writer.close()
            return result

        with mock.patch.object(storage, "gzip_probe", side_effect=update_after_probe):
            report = storage.audit_storage(self.db, probe_gzip=True)
        self.assertFalse(report["consistent_observation"])
        self.assertTrue(any("changed during observation" in text for text in report["errors"]))

    def test_identical_bytes_replacement_is_detected_by_file_state(self):
        original = storage.gzip_probe

        def replace_after_probe(path):
            result = original(path)
            replacement = self.db.parent / "identical.db"
            replacement.write_bytes(path.read_bytes())
            os.replace(replacement, path)
            return result

        with mock.patch.object(storage, "gzip_probe", side_effect=replace_after_probe):
            report = storage.audit_storage(self.db, probe_gzip=True)
        self.assertTrue(report["gzip"]["round_trip_ok"])
        self.assertFalse(report["consistent_observation"])
        self.assertTrue(report["errors"])

    def test_valid_trailing_bytes_are_counted_with_warning(self):
        with self.db.open("ab") as stream:
            stream.write(b"\0" * 4096)
        report = storage.audit_storage(self.db, probe_gzip=True)
        self.assertEqual(report["sqlite"]["trailing_bytes"], 4096)
        self.assertEqual(report["bytes"], self.db.stat().st_size)
        self.assertTrue(report["consistent_observation"])
        self.assertEqual(report["errors"], [])
        self.assertTrue(any("trailing bytes" in text for text in report["warnings"]))

    def test_cli_json_and_missing_path_exit(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = storage.main(["--db", str(self.db), "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(json.loads(output.getvalue())["bytes"], self.db.stat().st_size)
        missing = self.db.parent / "does-not-exist.db"
        with contextlib.redirect_stderr(io.StringIO()):
            code = storage.main(["--db", str(missing)])
        self.assertEqual(code, 2)
        self.assertFalse(missing.exists())


if __name__ == "__main__":
    unittest.main()
