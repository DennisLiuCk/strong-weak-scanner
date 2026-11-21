import contextlib
import io
import os
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import research_queue as rq
import research_worklist as rw


class OutputSafetyTest(unittest.TestCase):
    def run_cli(self, module, db, output):
        snapshot = {'items': [], 'as_of': '2026-11-21',
                    'topic_errors': [], 'scan': {'errors': []}}
        argv = ['research', '--db', str(db), '--json']
        if output is not None:
            argv += ['--output', str(output)]
        with mock.patch.object(sys, 'argv', argv), \
                mock.patch.object(rq, 'build_attention', return_value=snapshot), \
                mock.patch.object(rw, 'load_topic_schedule', return_value={}), \
                contextlib.redirect_stdout(io.StringIO()) as stdout, \
                contextlib.redirect_stderr(io.StringIO()) as stderr:
            try:
                code = module.main()
            except SystemExit as exc:
                code = exc.code
        return code, stdout.getvalue(), stderr.getvalue()

    def test_rejects_database_aliases_without_writing(self):
        for module in (rq, rw):
            for alias in ('same', 'relative', 'symlink', 'hardlink'):
                with self.subTest(module=module.__name__, alias=alias), \
                        tempfile.TemporaryDirectory() as directory:
                    db = Path(directory) / 'input.db'
                    with sqlite3.connect(db) as conn:
                        conn.execute('CREATE TABLE sentinel (value TEXT)')
                    before = db.read_bytes()
                    output = db
                    if alias == 'relative':
                        output = Path(os.path.relpath(db))
                    elif alias in ('symlink', 'hardlink'):
                        output = db.with_name('alias.db')
                        if alias == 'symlink':
                            output.symlink_to(db)
                        else:
                            os.link(db, output)
                    code, stdout, stderr = self.run_cli(module, db, output)
                    self.assertNotEqual(code, 0)
                    self.assertIn('--output', stderr)
                    self.assertIn('--db', stderr)
                    self.assertEqual(stdout, '')
                    self.assertEqual(db.read_bytes(), before)

    def test_distinct_output_and_stdout_remain_supported(self):
        for module in (rq, rw):
            with self.subTest(module=module.__name__), tempfile.TemporaryDirectory() as directory:
                db = Path(directory) / 'input.db'
                db.write_bytes(b'sentinel')
                output = Path(directory) / 'new' / 'report.json'
                code, _, stderr = self.run_cli(module, db, output)
                self.assertEqual((code, stderr), (0, ''))
                self.assertIn('"items"' if module is rq else '"selected"', output.read_text())
                code, stdout, stderr = self.run_cli(module, db, None)
                self.assertEqual((code, stderr), (0, ''))
                self.assertIn('"as_of"', stdout)
                self.assertEqual(db.read_bytes(), b'sentinel')

    def test_symlink_parent_dotdot_matches_database_opened_by_db_ro(self):
        for module in (rq, rw):
            for alias in ('actual', 'hardlink', 'distinct'):
                with self.subTest(module=module.__name__, alias=alias), \
                        tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    work = root / 'work'
                    run = root / 'snapshots' / 'run'
                    work.mkdir()
                    run.mkdir(parents=True)
                    (work / 'link').symlink_to(run, target_is_directory=True)
                    actual = work / 'input.db'
                    distinct = run.parent / 'input.db'
                    for path, marker in ((actual, 'actual'), (distinct, 'distinct')):
                        with sqlite3.connect(path) as conn:
                            conn.execute('CREATE TABLE sentinel (value TEXT)')
                            conn.execute('INSERT INTO sentinel VALUES (?)', (marker,))
                    db = work / 'link' / '..' / 'input.db'
                    with rq.db_ro.connect(db) as conn:
                        self.assertEqual(conn.execute('SELECT value FROM sentinel').fetchone()[0],
                                         'actual')
                    before = actual.read_bytes()
                    output = actual
                    if alias == 'hardlink':
                        output = work / 'alias.db'
                        os.link(actual, output)
                    elif alias == 'distinct':
                        output = db
                    code, stdout, stderr = self.run_cli(module, db, output)
                    if alias == 'distinct':
                        self.assertEqual((code, stderr), (0, ''))
                        self.assertIn('"as_of"', distinct.read_text())
                    else:
                        self.assertNotEqual(code, 0)
                        self.assertIn('--output', stderr)
                        self.assertIn('--db', stderr)
                        self.assertEqual(stdout, '')
                    self.assertEqual(actual.read_bytes(), before)
