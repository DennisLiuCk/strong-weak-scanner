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
            '3260 威剛 — topic', '3260 威剛 — unknown',
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

    def test_routes_push_once_and_preserve_the_document_path_and_query(self):
        result = self.run_helper('setRouteHash', """
const location=new URL('https://example.test/project/research.html?lang=zh');
const entries=[],saved=[];
const history={pushState(state,title,path){entries.push({state,path});location.href=new URL(path,location).href}};
function rememberNavigation(){saved.push(location.hash)}
function queueMicrotask(callback){callback()}
setRouteHash('topic-a');setRouteHash('topic-a');setRouteHash('topic-b');setRouteHash('');
console.log(JSON.stringify({entries,saved}));
""")
        self.assertEqual([entry['path'] for entry in result['entries']], [
            '/project/research.html?lang=zh#topic-a',
            '/project/research.html?lang=zh#topic-b',
            '/project/research.html?lang=zh',
        ])
        self.assertTrue(all(entry['state']['research'] for entry in result['entries']))
        self.assertEqual(result['saved'], ['#topic-a', '#topic-a', '#topic-b', ''])

    def test_history_snapshot_serializes_filters_origins_and_both_scroll_positions(self):
        result = self.run_helper('navigationSnapshot', """
const state={surface:'library',search:'信驊',selected:'topic-a',groups:new Set(['ic']),
  statuses:new Set(['review']),graphEvidence:new Set(['verified']),
  radarContextStates:new Map([['candidate',{open:true}]]),articleOrigin:{kind:'graph',graphId:'g1'}};
const location={hash:'#topic-a'},window={scrollY:320},catalogReturnPosition={catalogTop:180,articleId:'topic-a'};
const document={body:{classList:{contains:()=>true}},querySelector:s=>({scrollTop:s==='.catalog'?180:60}),
  getElementById:()=>({scrollTop:940})};
console.log(JSON.stringify(navigationSnapshot()));
""")
        self.assertEqual(result['view']['groups'], ['ic'])
        self.assertEqual(result['view']['statuses'], ['review'])
        self.assertEqual(result['view']['radarContextStates'], [['candidate', {'open': True}]])
        self.assertEqual(result['view']['articleOrigin'], {'kind': 'graph', 'graphId': 'g1'})
        self.assertEqual(result['scroll'], {'window': 320, 'catalog': 180, 'reader': 940, 'content': 60})
        self.assertTrue(result['articleOpen'])

    def test_body_preserves_authored_order_and_blocks_but_leaves_aids_to_panels(self):
        result = self.run_helper('renderArticleBody', """
function node(tag,attrs={},children=[]){return {tag,attrs,children,appendChild(child){this.children.push(child)},querySelectorAll(){return[]}}}
function h(tag,attrs,...children){return node(tag,attrs,children)}
const document={createDocumentFragment:()=>node('fragment')},ANALYST_HEADINGS=new Set(['研究摘要']);
function isArticleAuditSection(article,section){return section.h==='來源'}
function sectionId(index){return 'section-'+index}
function appendBlocks(parent,blocks){blocks.forEach(block=>parent.appendChild(block))}
const sections=[{h:'新手先讀：這篇在講什麼',blocks:[{text:'導讀'}]},
  {h:'研究摘要',blocks:[{text:'摘要'}]}, {h:'正文一',blocks:[{text:'已知 [S1]'}, {text:'尚未證實'}]},
  {h:'來源',blocks:[{text:'一手文件'}]}, {h:'還不能下哪些結論',blocks:[{text:'不能外推'}]}];
const before=JSON.stringify(sections),body=renderArticleBody({type:'topic',sections});
console.log(JSON.stringify({body,unchanged:before===JSON.stringify(sections)}));
""")
        self.assertTrue(result['unchanged'])
        self.assertEqual([section['attrs']['id'] for section in result['body']['children']],
                         ['section-2', 'section-4'])
        self.assertEqual(result['body']['children'][0]['children'][1:],
                         [{'text': '已知 [S1]'}, {'text': '尚未證實'}])
        self.assertEqual(result['body']['children'][1]['children'][1:], [{'text': '不能外推'}])
