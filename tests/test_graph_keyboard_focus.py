"""Execute SVG graph keyboard handlers with a focus-aware DOM harness."""
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which('node')


@unittest.skipUnless(NODE, 'node 不在 PATH')
class GraphKeyboardFocusTest(unittest.TestCase):
    def test_keyboard_activation_preserves_node_and_edge_focus(self):
        source = (ROOT / 'scripts/research_template.html').read_text(encoding='utf-8')
        functions = []
        for name in ('fitGraphLabel', 'fitGraphRootLabel', 'selectGraphEdge', 'selectGraphNode', 'graphKeyboard', 'renderGraphSvg'):
            start = source.index('function ' + name + '(')
            functions.append(source[start:source.index('\nfunction ', start + 10)])
        script = r"""
const assert=require('node:assert/strict');
const body={};
const document={activeElement:body,getElementById:()=>root};
function svgEl(tag,attrs){return {tag,attrs,children:[],style:{},textContent:attrs.text||'',isConnected:false,handlers:{},
 append(...items){items.forEach(item=>this.appendChild(item))},
 appendChild(item){this.children.push(item);item.isConnected=this.isConnected},
 addEventListener(type,handler){this.handlers[type]=handler},
 getAttribute(name){return this.attrs[name]??null},
 setAttribute(name,value){this.attrs[name]=value},
 contains(el){return this===el||this.children.some(child=>child.contains(el))},
 querySelectorAll(selector){return this.children.filter(child=>selector==='text'?child.tag==='text':child.attrs['data-graph-control'])},
 focus(){document.activeElement=this},
 replaceChildren(){this.children.forEach(child=>{child.isConnected=false});this.children=[];document.activeElement=body}
}}
const root=svgEl('svg',{});root.isConnected=true;
const state={graphView:'company',graphSelection:null};
const graph={label:'Graph',rootNodeId:'root'};
const nodes=[{id:'root',label:'Root',type:'concept'},{id:'other',label:'Other',type:'company'}];
const edges=[{id:'edge',from:'root',to:'other',materiality:'unknown'}];
const nodeMap=new Map(nodes.map(node=>[node.id,node]));
function renderGraphExposureRings(){}
function graphPositions(){return new Map(nodes.map(node=>[node.id,{x:0,y:0}]))}
function graphNodeEdges(){return new Map()}
function edgeIsStale(){return false}
function graphMaterialityShort(){return ''}
function graphMaterialityWidth(){return 1}
function graphTypeLabel(){return ''}
function shortGraphLabel(label){return label}
function renderGraph(){renderGraphSvg(graph,edges,nodes,nodeMap)}
renderGraph();
for(const [type,selector,id] of [['node','graph-node','root'],['edge','graph-edge-group','edge']]){
 for(const key of ['Enter',' ']){
  const old=root.children.find(child=>(child.attrs.class||'').split(' ').includes(selector));
  old.focus();let prevented=false;
  old.handlers.keydown({key,preventDefault(){prevented=true}});
  assert.deepEqual(state.graphSelection,{type,id});
  const replacement=root.children.find(child=>(child.attrs.class||'').split(' ').includes(selector));
  assert.notEqual(replacement,old);
  assert.equal(document.activeElement,replacement,type+' '+key+' must focus replacement');
  assert.equal(replacement.isConnected,true);assert.equal(prevented,true);
 }
}
const control=root.children.find(child=>child.attrs.class?.includes('graph-node'));
control.focus();control.handlers.keydown({key:'Escape',preventDefault(){throw Error('unexpected prevention')}});
assert.equal(document.activeElement,control);
document.activeElement=body;control.handlers.click();assert.equal(document.activeElement,body);
assert.equal(state.graphSelection.type,'node');
control.focus();nodes.length=0;edges.length=0;renderGraph();assert.equal(document.activeElement,body);
document.activeElement=body;renderGraph();assert.equal(document.activeElement,body);
console.log('node and edge: Enter/Space retain connected replacement focus; external focus unchanged');
"""
        result = subprocess.run([NODE, '-e', '\n'.join(functions) + script],
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
