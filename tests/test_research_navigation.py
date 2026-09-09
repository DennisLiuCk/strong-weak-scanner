"""Execute browser navigation helpers; UI integration is also checked in the browser."""
import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which('node')


@unittest.skipUnless(NODE, 'node 不在 PATH')
class ResearchNavigationTest(unittest.TestCase):
    def run_helper(self, name, script):
        source = (ROOT / 'scripts/research_template.html').read_text(encoding='utf-8')
        start = source.index('function ' + name + '(')
        end = source.index('\nfunction ', start + 10)
        result = subprocess.run([NODE, '-e', source[start:end] + '\n' + script],
                                capture_output=True, text=True, encoding='utf-8', timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout)

    def test_filter_tab_order_keeps_only_the_selected_radio_in_each_group(self):
        result = self.run_helper('filterTabStops', """
const controls=[
  {id:'clear'}, {id:'close'}, {id:'group',type:'checkbox'},
  {id:'all',type:'radio',name:'date',checked:true},
  {id:'latest',type:'radio',name:'date'},
  {id:'week',type:'radio',name:'date'},
  {id:'month',type:'radio',name:'date'},
  {id:'another-group',type:'radio',name:'other',checked:true},
  {id:'done'}, {id:'hidden',hidden:true}
].map(el=>({...el,offsetParent:el.hidden?null:{}}));
const panel={querySelectorAll:()=>controls};
const initial=filterTabStops(panel).map(el=>el.id);
controls.find(el=>el.id==='all').checked=false;
controls.find(el=>el.id==='month').checked=true;
console.log(JSON.stringify([initial,filterTabStops(panel).map(el=>el.id)]));
""")
        self.assertEqual(result, [
            ['clear', 'close', 'group', 'all', 'another-group', 'done'],
            ['clear', 'close', 'group', 'month', 'another-group', 'done'],
        ])
