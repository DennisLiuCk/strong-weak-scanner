"""db_ro 的契約:唯讀必須是真的被強制,不是靠呼叫者自律。

背景(2026-07-26 檢討):當天我宣稱「分析全程唯讀」,清點後發現 15 支腳本有 11 支
用 `sqlite3.connect(DB)` 開正式庫。這組測試把「唯讀」從意圖變成可驗證的性質。
"""
import os
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import db_ro


class DbRoTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = os.path.join(self.tmp.name, "t.db")
        con = sqlite3.connect(self.path)
        con.execute("CREATE TABLE t(a INT)")
        con.execute("INSERT INTO t VALUES(1)")
        con.commit()
        con.close()

    def tearDown(self):
        self.tmp.cleanup()

    def test_reads_work(self):
        con = db_ro.connect(self.path)
        self.assertEqual(con.execute("SELECT a FROM t").fetchone()["a"], 1)
        con.close()

    def test_writes_are_rejected(self):
        con = db_ro.connect(self.path)
        for sql in ("INSERT INTO t VALUES(2)", "UPDATE t SET a=9",
                    "DELETE FROM t", "CREATE TABLE u(b INT)", "DROP TABLE t"):
            with self.assertRaises(sqlite3.OperationalError, msg=f"{sql} 竟然被允許"):
                con.execute(sql)
        con.close()

    def test_missing_file_raises_instead_of_creating_empty_db(self):
        """`sqlite3.connect` 對打錯的路徑會默默建空 db,讓人對著空表分析半天。"""
        ghost = os.path.join(self.tmp.name, "nope.db")
        with self.assertRaises(sqlite3.OperationalError):
            db_ro.connect(ghost)
        self.assertFalse(os.path.exists(ghost), "唯讀開啟不得建立檔案")

    def test_query_only_pragma_is_set(self):
        con = db_ro.connect(self.path)
        self.assertEqual(con.execute("PRAGMA query_only").fetchone()[0], 1)
        con.close()

    def test_row_factory_defaults_to_row_and_can_be_disabled(self):
        con = db_ro.connect(self.path)
        self.assertIsInstance(con.execute("SELECT * FROM t").fetchone(), sqlite3.Row)
        con.close()
        con = db_ro.connect(self.path, row=False)
        self.assertIsInstance(con.execute("SELECT * FROM t").fetchone(), tuple)
        con.close()

    def test_uri_handles_windows_drive_and_spaces(self):
        d = os.path.join(self.tmp.name, "有 空白")
        os.makedirs(d)
        p = os.path.join(d, "x.db")
        sqlite3.connect(p).close()
        con = db_ro.connect(p)      # 路徑含空白與非 ASCII 也要能開
        self.assertEqual(con.execute("SELECT 1").fetchone()[0], 1)
        con.close()

    def test_validate_enforces_its_own_read_only_claim(self):
        """validate.py 的 docstring 寫「讀 db 不寫 db」——那句話必須是被強制的,
        不是意圖。這正是 2026-07-26 檢討的核心教訓。"""
        src = (ROOT / "scripts" / "validate.py").read_text(encoding="utf-8")
        self.assertIn("db_ro.connect", src,
                      "validate.py 宣稱唯讀,就必須用 db_ro 開啟")
        self.assertNotIn("sqlite3.connect(args.db)", src)


if __name__ == "__main__":
    unittest.main()
