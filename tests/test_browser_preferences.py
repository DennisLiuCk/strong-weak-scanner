"""Execute preference reads, theme clicks and focus clicks with denied browser storage."""
import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "node 不在 PATH")
class BrowserPreferencesTest(unittest.TestCase):
    def test_radar_review_deadline_distinguishes_past_today_future_and_missing(self):
        source = (ROOT / 'scripts/research_template.html').read_text(encoding='utf-8')
        start = source.index('function fmtDate(')
        end = source.index('\nfunction ', source.index('function radarReviewDeadline(') + 10)
        script = source[start:end] + """
console.log(JSON.stringify(['2026-08-16','2026-09-10','2026-09-11',''].map(
  date=>radarReviewDeadline(date,'2026-09-10'))));
"""
        result = subprocess.run([NODE, '-e', script], capture_output=True,
                                text=True, encoding='utf-8', timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), [
            {'text':'總檢查已到期 2026/08/16','overdue':True},
            {'text':'總檢查今日到期 2026/09/10','overdue':False},
            {'text':'下次總檢查 2026/09/11','overdue':False},
            {'text':'總檢查日期未設定','overdue':False},
        ])

    def test_storage_failure_does_not_interrupt_theme_or_reading_mode(self):
        for template, read, write in (
            ("dashboard_template.html", "rvStored", "rvRemember"),
            ("research_template.html", "readPreference", "writePreference"),
        ):
            source = (ROOT / "scripts" / template).read_text(encoding="utf-8")
            helpers = "\n".join(line for line in source.splitlines()
                                if line.startswith((f"function {read}(", f"function {write}(")))
            # Every actual storage access must go through the exception boundary.
            accesses = [line for line in source.splitlines() if "localStorage." in line]
            self.assertEqual(accesses, helpers.splitlines())
            theme = (source[source.index("const _html="):source.index("/* ---------- 詳情面板")]
                     if template.startswith("dashboard") else
                     source[source.index("const root=document.documentElement;"):source.index("function hashArticleId()")])
            focus = ""
            if template.startswith("research"):
                declaration = re.search(r"let focusModeRequested=[^;]+;", source)[0]
                listener = next(line for line in source.splitlines()
                                if line.startswith("focusToggleButton.addEventListener"))
                focus = declaration + listener + "listeners.focusToggle();"
            for storage in (
                "Object.defineProperty(globalThis,'localStorage',{get(){throw Error('denied')}});",
                "const localStorage={getItem(){return 'dark'},setItem(){throw Error('quota')}};",
                "const values={dashTheme:'dark'};const localStorage={getItem:k=>values[k],setItem:(k,v)=>values[k]=v};",
            ):
                with self.subTest(template=template, storage=storage):
                    script = """
const listeners={}, dataset={};let applied=0;
const document={documentElement:{dataset},querySelectorAll:()=>[],addEventListener(){},
  getElementById:id=>({addEventListener:(_,fn)=>listeners[id]=fn})};
const matchMedia=()=>({matches:false});
const focusToggleButton=document.getElementById('focusToggle');
const focusMedia={addEventListener(){}};
function applyFocusMode(){applied++}
""" + storage + helpers + theme + focus + """
listeners.themeBtn();listeners.themeBtn();
console.log(JSON.stringify({theme:dataset.theme,applied}));
"""
                    result = subprocess.run([NODE, "-e", script], capture_output=True,
                                            text=True, encoding="utf-8", timeout=15)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    output = json.loads(result.stdout)
                    self.assertIn(output["theme"], ("light", "dark"))
                    if focus:
                        self.assertEqual(output["applied"], 2)
