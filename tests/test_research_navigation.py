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

    def test_company_heading_identifies_the_document_without_repeating_the_mission(self):
        result = self.run_helper('articleReaderHeading', """
function h(tag,attrs,...children){return {tag,attrs,children}}
function catalogReaderQuestion(article){return article.question||''}
function articleReaderTitleLabel(){return '研究題名：'}
const TYPE_INFO={formal_note:{label:'正式筆記'},narrative:{label:'多空小作文'}};
function headings(node){if(typeof node!=='object')return[];return node.tag==='h1'?[node.attrs]:node.children.flatMap(headings)}
const rows=['formal_note','narrative','topic','unknown'].map(type=>({
  id:type,type,readerTitle:'3260 威剛 — '+type,
  question:type==='unknown'?'':'這家公司做什麼？'
}));
console.log(JSON.stringify(rows.map(article=>headings(articleReaderHeading(article)))));
""")
        self.assertEqual([row[0]['text'] for row in result], [
            '3260 威剛 — formal_note', '3260 威剛 — narrative',
            '這家公司做什麼？', '3260 威剛 — unknown',
        ])
        self.assertEqual([row[0]['data-reader-heading-focus'] for row in result],
                         ['formal_note', 'narrative', 'topic', 'unknown'])
        self.assertTrue(all(row[0]['tabindex'] == '-1' for row in result))

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
