"""Execute the dashboard's sheet/history lifecycle against an async history model."""
import shutil
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NODE = shutil.which("node")


@unittest.skipUnless(NODE, "node 不在 PATH")
class SheetHistoryTest(unittest.TestCase):
    def test_back_forward_close_peer_navigation_and_guide_link(self):
        source = (ROOT / "scripts/dashboard_template.html").read_text(encoding="utf-8")
        lifecycle = source[source.index("let lastSheetFocus=null;"):
                           source.index("function openStockDetail(")]
        harness = r"""
const assert=require('node:assert/strict');
let scrollY=700,focusCalls=[],frames=[],listeners={},pending=[];
function element(tag='DIV',attrs={}){return {tagName:tag,style:{},attrs,inert:false,isConnected:true,
 getAttribute(k){return this.attrs[k]??null},setAttribute(k,v){this.attrs[k]=v},removeAttribute(k){delete this.attrs[k]},
 focus(options){focusCalls.push({el:this,options});document.activeElement=this;if(!options?.preventScroll)scrollY+=88;}}}
const opener=element('BUTTON'),header=element('HEADER',{'aria-hidden':'false'}),main=element('MAIN'),script=element('SCRIPT');
const sheetwrap=element();sheetwrap.classList={open:false,contains(){return this.open},add(){this.open=true},remove(){this.open=false}};
const closer=element('BUTTON');
const sheetEl=element();sheetEl.querySelector=()=>closer;
const document={activeElement:opener,body:{style:{overflow:'auto'},children:[header,main,script,sheetwrap]}};
const location={assign(href){navigated.push(href)}};let navigated=[];
const window={requestAnimationFrame(fn){frames.push(fn)},addEventListener(type,fn){listeners[type]=fn}};
// A fragment entry already exists: opening/closing the sheet must not consume it.
const entries=[{state:null,url:'/'},{state:{existing:'keep'},url:'/#tier'}];let index=1;
const history={get state(){return entries[index].state},
 pushState(state,title,url){assert.equal(url,undefined);entries.splice(index+1);entries.push({state,url:entries[index].url});index++},
 back(){pending.push(()=>{if(index>0){index--;listeners.popstate({state:this.state})}})},
 forward(){pending.push(()=>{if(index<entries.length-1){index++;listeners.popstate({state:this.state})}})}};
function flush(){while(pending.length)pending.shift()();while(frames.length)frames.shift()()}
let currentView='';
function render(view,trigger=null){currentView=view;showSheet(()=>render(view,trigger),trigger)}
"""
        cases = r"""
assert.equal(typeof listeners.popstate,'function');
render('stock-3661');flush();scrollY=700;
assert.equal(index,2);assert.equal(entries.length,3);assert.equal(history.state.existing,'keep');
assert.equal(entries[index].url,'/#tier');assert.equal(main.inert,true);
assert.equal(header.getAttribute('aria-hidden'),'true');assert.equal(document.body.style.overflow,'hidden');
// Changing peers replaces the sheet's view, not the browser history entry.
render('stock-peer');flush();scrollY=700;assert.equal(index,2);assert.equal(entries.length,3);
history.back();flush();
assert.equal(index,1);assert.equal(sheetwrap.classList.open,false);assert.equal(main.inert,false);
assert.equal(main.getAttribute('aria-hidden'),null);assert.equal(header.getAttribute('aria-hidden'),'false');
assert.equal(document.body.style.overflow,'auto');assert.equal(document.activeElement,opener);
assert.deepEqual(focusCalls.at(-1).options,{preventScroll:true});assert.equal(scrollY,700);
history.forward();flush();scrollY=700;
assert.equal(currentView,'stock-peer');assert.equal(sheetwrap.classList.open,true);assert.equal(index,2);assert.equal(entries.length,3);
// Rapid Escape/close/backdrop requests must enqueue only one traversal.
closeSheet();closeSheet();assert.equal(pending.length,1);flush();
assert.equal(index,1);assert.equal(sheetwrap.classList.open,false);assert.equal(scrollY,700);
// Touch activation of a custom role=button may leave BODY active: use currentTarget.
document.activeElement=document.body;render('stock-touch',opener);flush();scrollY=700;closeSheet();flush();
assert.equal(document.activeElement,opener);assert.equal(scrollY,700);assert.equal(index,1);
// A nested group -> stock -> group transition also takes only one entry.
render('group');render('stock-in-group');render('group-return');flush();scrollY=700;
assert.equal(entries.length,3);closeSheet();flush();assert.equal(index,1);
history.forward();flush();assert.equal(currentView,'group-return');assert.equal(index,2);
// A guide anchor must run after the sheet entry has been consumed.
let prevented=false;const guide={currentTarget:{tagName:'A',href:'http://localhost/#flow-guide'},preventDefault(){prevented=true}};
closeSheet(guide);assert.equal(prevented,true);assert.deepEqual(navigated,[]);flush();
assert.equal(index,1);assert.deepEqual(navigated,['http://localhost/#flow-guide']);assert.equal(sheetwrap.classList.open,false);
// A disconnected opener and a late animation callback must not steal focus.
document.activeElement=opener;opener.isConnected=false;render('stock-rapid');
const focusBeforeClose=focusCalls.length;closeSheet();flush();
assert.equal(focusCalls.length,focusBeforeClose);assert.equal(sheetwrap.classList.open,false);opener.isConnected=true;
// Foreign or stale history states are not treated as our sheet.
listeners.popstate({state:{scannerSheet:'old-document'}});assert.equal(sheetwrap.classList.open,false);
// A real next Back still leaves the list; the list entry was not overwritten.
history.back();flush();assert.equal(index,0);assert.equal(entries[index].url,'/');
console.log('sheet Back/Forward, one-entry peer/group navigation, explicit close, guide link, focus and state preservation passed');
"""
        result = subprocess.run([NODE, "-e", harness + lifecycle + cases],
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
