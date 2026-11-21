import contextlib
import io
from pathlib import Path
import sys
import unittest
from unittest import mock


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import run_daily


class DailyPreviewTest(unittest.TestCase):
    def invoke(self, *args):
        with mock.patch.object(sys, "argv", ["run_daily.py", *args]), \
                mock.patch.object(run_daily, "run") as run, \
                contextlib.redirect_stdout(io.StringIO()) as output:
            run_daily.main()
        return run, output.getvalue()

    def test_preview_routes_builder_away_from_published_pages(self):
        run, output = self.invoke("--preview", "--skip-tdcc")
        destination = str(Path(run_daily.ROOT) / "tmp" / "preview")
        self.assertIn(mock.call("build_dashboard.py", "--output-dir", destination),
                      run.call_args_list)
        self.assertIn(str(Path(destination) / "index.html"), output)
        self.assertIn(mock.call("snapshot_signals.py", "--source", "local"),
                      run.call_args_list)
        self.assertIn(mock.call("audit_ranking_views.py", "--compact"),
                      run.call_args_list)

    def test_official_run_keeps_published_destination_and_gates(self):
        run, _ = self.invoke()
        self.assertIn(mock.call("build_dashboard.py"), run.call_args_list)
        self.assertIn(mock.call("snapshot_signals.py", "--source", "local", "--publish"),
                      run.call_args_list)
        self.assertIn(mock.call("audit_ranking_views.py", "--compact",
                               "--require-current-snapshot"), run.call_args_list)

    def test_preview_stops_if_upstream_fails(self):
        with mock.patch.object(sys, "argv", ["run_daily.py", "--preview"]), \
                mock.patch.object(run_daily, "run", side_effect=RuntimeError("failed")) as run:
            with self.assertRaisesRegex(RuntimeError, "failed"):
                run_daily.main()
        run.assert_called_once_with("fetch_tdcc.py")
