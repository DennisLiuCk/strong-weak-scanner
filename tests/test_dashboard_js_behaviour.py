# -*- coding: utf-8 -*-
"""把模板裡幾個純函式**真的執行過**,而不是比對原始碼字串(2026-07-26)。

起因:2026-07-26 的複核指出,新加的「契約測試」大多只 assertIn 一段原始碼。
那種測試擋得住有人刪掉那行,擋不住有人改壞行為——例如把 `statistics.median(v)`
換成 `median(v[-1:])`,字串全在、行為全錯;也擋不住註解裡出現同一段字。
更糟的是儀表板上最容易誤導人的一段(`lensShape` 的白話標籤)完全沒有測試。

這裡改用 node 直接跑模板抽出來的函式。node 在 GitHub ubuntu runner 上是預裝的;
真的沒有就 skip,不讓它變成硬相依(專案鐵律:零第三方依賴)。

抽函式而不是載入整個模板,是因為模板要等 build 注入 __*_JSON__ 才是合法 JS。
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
TEMPLATE = SCRIPTS / "dashboard_template.html"
NODE = shutil.which("node")


def extract(name):
    """抽出模板裡某個 top-level function 的完整原始碼(以下一個 top-level 宣告為界)。

    重複定義會讓這整套測試靜默失效:`re.search` 取第一個,若有人後面又定義一次
    (JS 是後者勝),測試會一直驗證那個被遮蔽的死版本而照樣通過。所以先擋重複。
    截斷的情況不必特別處理——抽壞了餵給 node 會語法錯誤、returncode != 0,是大聲失敗。
    """
    src = TEMPLATE.read_text(encoding="utf-8")
    pat = r"^(?:function %s\(|const %s=)" % (name, name)
    hits = list(re.finditer(pat, src, re.M))
    if not hits:
        raise AssertionError(f"模板裡找不到 top-level 的 {name}")
    if len(hits) > 1:
        raise AssertionError(
            f"{name} 有 {len(hits)} 個 top-level 定義 —— JS 取最後一個,"
            f"但本測試抽第一個,會驗到被遮蔽的死版本")
    m = hits[0]
    rest = src[m.start():]
    nxt = re.search(r"^(?:function |const |document\.getElementById)", rest[1:], re.M)
    return rest[:nxt.start() + 1] if nxt else rest


@unittest.skipIf(NODE is None, "node 不在 PATH,跳過 JS 行為測試")
class DashboardJsBehaviourTest(unittest.TestCase):
    def run_js(self, prelude, expr_cases):
        """expr_cases: [(說明, JS 運算式)] → 回傳每個運算式的 JSON 結果。"""
        body = prelude + "\nconst __out=[];\n" + "".join(
            f"__out.push({e});\n" for _, e in expr_cases
        ) + "console.log(JSON.stringify(__out));"
        with tempfile.NamedTemporaryFile("w", suffix=".mjs", delete=False,
                                         encoding="utf-8") as f:
            f.write(body)
            path = f.name
        try:
            r = subprocess.run([NODE, path], capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=60)
            self.assertEqual(r.returncode, 0, f"node 失敗:{r.stderr}")
            return json.loads(r.stdout.strip().splitlines()[-1])
        finally:
            Path(path).unlink(missing_ok=True)

    # ---------- fmtPct:唯一的百分比格式化入口 ----------

    def test_stock_lookup_matches_exact_id_before_loose_matches(self):
        pre = extract("stockLookupMatches") + r"""
const stocks=[
  {id:'2000',nm:'創意電子'},
  {id:'3443',nm:'創意'},
  {id:'3000',nm:'測試3443'},
  {id:'3661',nm:'世芯-KY'},
];
"""
        got = self.run_js(pre, [
            ('空白不搜尋', "stockLookupMatches(stocks,'  ').length"),
            ('完整股號唯一且第一', "stockLookupMatches(stocks,'3443').map(x=>x.id)"),
            ('名稱含股號可找到', "stockLookupMatches(stocks,'測試3443').map(x=>x.id)"),
            ('名稱關鍵字可找到', "stockLookupMatches(stocks,'世芯').map(x=>x.id)"),
        ])
        self.assertEqual(got[0], 0)
        self.assertEqual(got[1][0], '3443')
        self.assertIn('3000', got[1])
        self.assertEqual(got[2], ['3000'])
        self.assertEqual(got[3], ['3661'])


    def chart_dom(self):
        return r"""
class Element {
  constructor(tag) { this.tag=tag; this.nodeType=1; this.attrs={}; this.style={}; this.children=[]; this.events={}; }
  setAttribute(k,v) { this.attrs[k]=v; }
  set textContent(v) { this.children=[]; this.text=String(v); }
  get textContent() { return (this.text||'')+this.children.map(c=>c.textContent).join(''); }
  appendChild(c) { this.children.push(c); return c; }
  append(...cs) { cs.forEach(c=>this.appendChild(c)); }
  replaceChildren(...cs) { this.text=''; this.children=cs.filter(Boolean); }
  addEventListener(k,f) { (this.events[k]??=[]).push(f); }
  fire(k,e={}) { (this.events[k]||[]).forEach(f=>f(e)); }
  find(f) { if(f(this))return this; for(const c of this.children){const x=c.find?.(f);if(x)return x;} }
  querySelector(tag) { return this.find(e=>e.tag===tag); }
  getBoundingClientRect() { return {left:0,width:680}; }
}
const document={createElement:t=>new Element(t),createElementNS:(_,t)=>new Element(t),
  createTextNode:t=>({nodeType:3,textContent:String(t)})};
const NS='http://www.w3.org/2000/svg';
let now=1000;const Date={now:()=>now};
"""

    def test_price_chart_keeps_tapped_date_and_supports_keyboard_without_losing_hover(self):
        # 跑完整 priceChart 與事件處理器；SVG 重繪後容器事件仍須有效。
        dom = self.chart_dom()
        setup = r"""
const n=65, vals=Array.from({length:n},(_,i)=>100+i);
const host=priceChart({px:vals,dates:vals.map((_,i)=>'day'+i),ma5:vals,ma:vals,ma60:vals,
  rsi:vals.map(()=>0),vol:vals.map(()=>0),foreign:vals.map(()=>0),trust:vals.map(()=>null)});
const box=()=>host.find(e=>e.attrs.role==='group');
const output=()=>host.find(e=>e.attrs.role==='status');
const state=()=>({hidden:output().hidden,text:output().textContent});
const fire=(type,e)=>{box().fire(type,e);return state();};
const tap=x=>{const e={pointerType:'touch',pointerId:1,isPrimary:true,button:0,clientX:x,clientY:100};
  box().fire('pointerdown',e);box().fire('pointerup',e);return state();};
const key=k=>{let prevented=false;box().fire('keydown',{key:k,preventDefault(){prevented=true;}});return {...state(),prevented};};
const button=text=>host.find(e=>e.tag==='button'&&e.textContent===text);
"""
        pre = dom + '\n'.join(extract(f) for f in ('h', 'sv', 'svg', 'priceChart')) + setup
        got = self.run_js(pre, [
            ('初始未選日期', 'state()'),
            ('桌機 hover', "fire('pointermove',{pointerType:'mouse',clientX:8})"),
            ('桌機離開清除預覽', "fire('pointerleave',{pointerType:'mouse'})"),
            ('手指拖曳不攔截捲動也不選日期', "fire('pointermove',{pointerType:'touch',clientX:8})"),
            ('點按保留首日', 'tap(8)'),
            ('手指離開仍保留', "fire('pointerleave',{pointerType:'touch'})"),
            ('桌機移入可暫看別日', "(now+=801,fire('pointermove',{pointerType:'mouse',clientX:628}))"),
            ('移出恢復點選日期', "fire('pointerleave',{pointerType:'mouse'})"),
            ('鍵盤下一交易日', "key('ArrowRight')"),
            ('鍵盤到最早', "key('Home')"),
            ('不越過最早', "key('ArrowLeft')"),
            ('鍵盤到最新', "key('End')"),
            ('不越過最新', "key('ArrowRight')"),
            ('其他按鍵不攔截', "key('Tab')"),
            ('換區間清除舊日期', "(button('20 日').fire('click'),state())"),
            ('換區間後首日正確', "key('Home')"),
            ('指標切換保留日期與零值', "(host.find(e=>e.tag==='button'&&e.textContent.includes('外資')).fire('click'),state())"),
            ('滑動取消後相容 click 不可選日期', "(()=>{const e={pointerType:'touch',pointerId:1,isPrimary:true,button:0,clientX:8,clientY:100};box().fire('pointerdown',e);box().fire('pointermove',{...e,clientY:75});box().fire('pointercancel',e);box().fire('pointerup',e);return fire('click',{clientX:628});})()"),
            ('滑動後的相容 mousemove 不可蓋掉讀數', "fire('pointermove',{pointerType:'mouse',clientX:628})"),
            ('超出點按距離不可選日期，即使沒有 cancel', "(()=>{const e={pointerType:'touch',pointerId:1,isPrimary:true,button:0,clientX:628,clientY:100};box().fire('pointerdown',e);return fire('pointerup',{...e,clientY:125});})()"),
            ('滑鼠直接拖出容器再回原點放開不可釘選', "(()=>{key('End');now+=801;const e={pointerType:'mouse',pointerId:2,isPrimary:true,button:0,clientX:8,clientY:100};box().fire('pointerdown',e);box().fire('pointerleave',e);box().fire('pointermove',e);box().fire('pointerup',e);return fire('pointerleave',e);})()"),
            ('取消拖曳後仍可正常點選另一日期', "(()=>{const e={pointerType:'mouse',pointerId:2,isPrimary:true,button:0,clientX:8,clientY:100};box().fire('pointerdown',e);box().fire('pointerup',e);return fire('pointerleave',e);})()"),
        ])
        for i in (0, 2, 3, 14):
            self.assertTrue(got[i]['hidden'])
            self.assertEqual(got[i]['text'], '')
        for i in (1, 4, 5, 7, 9, 10):
            self.assertFalse(got[i]['hidden'])
            self.assertIn('日期day5', got[i]['text'])
            self.assertIn('現價105.00', got[i]['text'])
            self.assertIn('RSI0.0', got[i]['text'])
        self.assertIn('日期day6', got[8]['text'])
        for i in (6, 11, 12, 13):
            self.assertIn('日期day64', got[i]['text'])
        for i in (8, 9, 10, 11, 12, 15):
            self.assertTrue(got[i]['prevented'])
        self.assertFalse(got[13]['prevented'])
        for i in (15, 16, 17, 18, 19):
            self.assertIn('日期day45', got[i]['text'])
        self.assertIn('外資+0', got[16]['text'])
        self.assertNotIn('投信', got[16]['text'])
        self.assertIn('日期day64', got[20]['text'])
        self.assertIn('日期day45', got[21]['text'])

    def test_chart_date_select_pins_exact_date_and_survives_indicator_toggle(self):
        pre = self.chart_dom() + '\n'.join(extract(f) for f in ('h', 'sv', 'svg', 'priceChart')) + r"""
const vals=Array.from({length:65},(_,i)=>100+i);
const host=priceChart({px:vals,dates:vals.map((_,i)=>'day'+i),ma5:vals,ma:vals,ma60:vals,
  rsi:vals.map(()=>0),vol:vals.map(()=>0),foreign:vals.map(()=>0),trust:vals.map(()=>null)},{});
const output=()=>host.find(e=>e.attrs.role==='status');
const box=()=>host.find(e=>e.attrs.role==='group');
const select=()=>host.find(e=>e.className==='chart-date-picker').find(e=>e.tag==='select');
const choose=d=>{select().value=d;select().fire('change',{target:select()});return {text:output().textContent,value:select().value};};
const key=k=>{box().fire('keydown',{key:k,preventDefault(){}});return {text:output().textContent,value:select().value};};
const button=text=>host.find(e=>e.tag==='button'&&e.textContent.includes(text));
"""
        got = self.run_js(pre, [
            ('最新日期排在最前', "select().children.slice(0,4).map(x=>x.textContent)"),
            ('直接選日期', "choose('day10')"),
            ('鍵盤移動同步選單', "key('ArrowRight')"),
            ('切換指標保留日期', "(button('外資').fire('click'),{text:output().textContent,value:select().value})"),
            ('切換區間清除日期並縮短清單', "(button('20 日').fire('click'),{hidden:output().hidden,value:select().value||'',count:select().children.length,first:select().children[1].textContent,last:select().children.at(-1).textContent})"),
        ])
        self.assertEqual(got[0], ['選擇交易日…', 'day64', 'day63', 'day62'])
        self.assertIn('日期day10', got[1]['text'])
        self.assertEqual(got[1]['value'], 'day10')
        self.assertIn('日期day11', got[2]['text'])
        self.assertEqual(got[2]['value'], 'day11')
        self.assertIn('日期day11', got[3]['text'])
        self.assertEqual(got[3]['value'], 'day11')
        self.assertEqual(got[4], {
            'hidden': True, 'value': '', 'count': 21,
            'first': 'day64', 'last': 'day45'})

    def test_chart_peer_comparison_uses_pinned_date_not_hover_and_aligns_exact_dates(self):
        pre = self.chart_dom() + '\n'.join(extract(f) for f in ('h', 'sv', 'svg', 'priceChart')) + r"""
const vals=Array.from({length:65},(_,i)=>100+i);
const chart={px:vals,dates:vals.map((_,i)=>'day'+i),ma5:vals,foreign:vals};
let target, context;
const comparison={name:'甲 1111',peers:[null,{id:'2222',name:'乙',available:true}],
  navigate:(id,state)=>{target=id;context=state;}};
const host=priceChart(chart,{},comparison);
const find=(host,tag,text)=>host.find(e=>e.tag===tag&&e.textContent.includes(text));
const next=host=>find(host,'button','同日看 乙');
const output=host=>host.find(e=>e.attrs.role==='status');
const box=host=>host.find(e=>e.attrs.role==='group');
const key=(host,k)=>box(host).fire('keydown',{key:k,preventDefault(){}});
"""
        got = self.run_js(pre, [
            ('未選日期不可比較', '[next(host).disabled,find(host,"button","無上一檔").disabled]'),
            ('hover 不啟用同日比較', "(box(host).fire('pointermove',{pointerType:'mouse',clientX:628}),next(host).disabled)"),
            ('釘選、改指標、再 hover 其他日', "(key(host,'Home'),find(host,'button','外資').fire('click'),box(host).fire('pointermove',{pointerType:'mouse',clientX:628}),next(host).fire('click'),{target,context})"),
            ('下一檔中間少一天仍按日期對齊', "(()=>{const keep=a=>a.filter((_,i)=>i!==20);const c={...chart,px:keep(vals),dates:keep(chart.dates),ma5:keep(vals),foreign:keep(vals)};const peer=priceChart(c,{}, {...comparison,context});return output(peer).textContent;})()"),
            ('缺該日不能偷換到鄰日', "(()=>{const c={...chart,dates:chart.dates.map(d=>d==='day5'?'other':d)};const peer=priceChart(c,{}, {...comparison,context});return {hidden:output(peer).hidden,disabled:next(peer).disabled,text:peer.textContent};})()"),
            ('缺日後可另選日期並比較', "(()=>{const peer=priceChart(chart,{}, {...comparison,context:{...context,date:'missing'}});key(peer,'End');next(peer).fire('click');return context.date;})()"),
            ('換區間仍清除日期', "(find(host,'button','20 日').fire('click'),{hidden:output(host).hidden,disabled:next(host).disabled})"),
            ('無歷史圖表的同業不能比較', "(()=>{const peer=priceChart(chart,{}, {...comparison,context,peers:[null,{id:'2222',name:'乙',available:false}]});return next(peer).disabled;})()"),
        ])
        self.assertEqual(got[0], [True, True])
        self.assertTrue(got[1])
        self.assertEqual(got[2]['target'], '2222')
        self.assertEqual(got[2]['context']['date'], 'day5')
        self.assertEqual(got[2]['context']['range'], 60)
        self.assertTrue(got[2]['context']['ind']['foreign'])
        self.assertIn('日期day5', got[3])
        self.assertIn('現價105.00', got[3])
        self.assertIn('外資+105', got[3])
        self.assertTrue(got[4]['hidden'])
        self.assertTrue(got[4]['disabled'])
        self.assertIn('無 day5', got[4]['text'])
        self.assertEqual(got[5], 'day64')
        self.assertEqual(got[6], {'hidden': True, 'disabled': True})
        self.assertTrue(got[7])

    def test_compact_mobile_chart_moves_scaled_labels_into_html(self):
        """窄幅圖不再把 680px SVG 縮到一半還硬塞小字:座標與提示只留 HTML。"""
        pre = self.chart_dom() + "let narrow=true;const listeners={};const window={matchMedia:q=>({matches:narrow}),addEventListener:(type,fn)=>{(listeners[type]=listeners[type]||[]).push(fn)}};\n" + '\n'.join(extract(f) for f in ('h', 'sv', 'svg', 'priceChart')) + r"""
const n=65, vals=Array.from({length:n},(_,i)=>100+i);
const chart={px:vals,dates:vals.map((_,i)=>'day'+i),ma5:vals,ma:vals,ma60:vals,
  rsi:vals.map(()=>0),vol:vals.map(()=>0),foreign:vals.map(()=>0),trust:vals.map(()=>null)};
const mobile=priceChart(chart,{});
narrow=false;
const desktop=priceChart(chart,{});
const firstSvg=host=>host.find(e=>e.tag==='svg');
const meta=host=>host.find(e=>e.className==='chart-meta');
"""
        got = self.run_js(pre, [
            ('手機 SVG 無被縮小文字', "(()=>{const svg=firstSvg(mobile);return {noText:!svg.find(e=>e.tag==='text'),meta:meta(mobile)?.textContent||'',viewBox:svg.attrs.viewBox};})()"),
            ('桌機保留 SVG 座標文字且手機 meta 隱藏', "(()=>{const svg=firstSvg(desktop);return {hasText:!!svg.find(e=>e.tag==='text'),metaHidden:meta(desktop)?.hidden,viewBox:svg.attrs.viewBox};})()"),
            ('桌機開啟後 resize 到手機可補上 meta', "(()=>{narrow=true;(listeners.resize||[]).forEach(fn=>fn());const svg=firstSvg(desktop);return {noText:!svg.find(e=>e.tag==='text'),meta:meta(desktop)?.textContent||'',metaHidden:meta(desktop)?.hidden};})()"),
        ])
        self.assertTrue(got[0]['noText'])
        self.assertIn('60 日 · day5 → day64', got[0]['meta'])
        self.assertIn('現價低 105.0 · 高 164.0', got[0]['meta'])
        self.assertTrue(got[0]['viewBox'].startswith('0 0 680 '))
        self.assertTrue(got[1]['hasText'])
        self.assertTrue(got[1]['metaHidden'])
        self.assertTrue(got[2]['noText'])
        self.assertIn('60 日 · day5 → day64', got[2]['meta'])
        self.assertFalse(got[2]['metaHidden'])

    def test_archive_links_resolve_from_live_and_historical_pages(self):
        got = self.run_js(extract('archiveSnapshotHref'), [
            ('首頁', "archiveSnapshotHref('2026-09-08','/strong-weak-scanner/index.html')"),
            ('歷史頁', "archiveSnapshotHref('2026-09-08','/strong-weak-scanner/archive/2026-09-09.html')"),
            ('非法路徑', "archiveSnapshotHref('../index','/strong-weak-scanner/')"),
        ])
        self.assertEqual(got, ['archive/2026-09-08.html', '2026-09-08.html', None])

    def test_archive_nav_dates_merge_manifest_with_embedded_fallback(self):
        pre = extract('archiveSnapshotHref') + extract('archiveNavDates') + """
const embedded=['2026-11-18','2026-11-19'];
const page='/strong-weak-scanner/archive/2026-11-19.html';
"""
        got = self.run_js(pre, [
            ('僅內嵌清單', "archiveNavDates(embedded,page)"),
            ('manifest 補上較新日期', "archiveNavDates(embedded.concat(['2026-11-18','2026-11-19','2026-11-20']),page)"),
            ('manifest 缺漏不刪內嵌日期', "archiveNavDates(embedded.concat(['2026-11-20']),page)"),
            ('過濾非法項目', "archiveNavDates(embedded.concat(['../index','2026-11-20']),page)"),
        ])
        self.assertEqual(got[0], ['2026-11-19', '2026-11-18'])
        for merged in got[1:]:
            self.assertEqual(merged, ['2026-11-20', '2026-11-19', '2026-11-18'])

    def test_stock_search_groups_preserve_scope_rank_and_suspended_order(self):
        pre = extract('stockSearchGroups') + """
const groups=[{g:'memory'},{g:'ip'}];
const stocks=[
 {g:'memory',id:'3260',nm:'威剛',comp:3,cs:[1]},
 {g:'memory',id:'2344',nm:'華邦電',comp:5,cs:[2]},
 {g:'memory',id:'9999',nm:'暫停',comp:9,cs:[2],trading:{}},
 {g:'ip',id:'6643',nm:'M31',comp:2,cs:[1]}];
const search=(g,q,desc=true)=>stockSearchGroups(stocks,groups,g,q,'comp',desc);
"""
        got = self.run_js(pre, [
            ('跨族群保留原位置', "search('', ' 3260 ')") ,
            ('不區分大小寫', "search('', 'm31')"),
            ('尊重明確族群篩選', "search('ip', '3260')"),
            ('反向排序暫停仍置底', "search('memory', '', false)"),
            ('無結果', "search('', '不存在')"),
        ])
        self.assertEqual(got[0][0]['rows'][0]['rank'], 2)
        self.assertEqual(got[0][0]['total'], 3)
        self.assertEqual(got[1][1]['rows'][0]['stock']['id'], '6643')
        self.assertEqual(got[2][0]['rows'], [])
        self.assertEqual([r['stock']['id'] for r in got[3][0]['rows']], ['3260', '2344', '9999'])
        self.assertIsNone(got[3][0]['rows'][-1]['rank'])
        self.assertTrue(all(not g['rows'] for g in got[4]))

    def test_fmtPct_behaviour(self):
        pre = extract("fmtPct")
        cases = [
            # (輸入, 預期輸出, 為什麼這格重要)
            ("-0.4", "−0.4%", "小負數不可印成 -0%,那會把在跌讀成持平"),
            ("-0.0", "0.0%", "後端 round(−0.04,1) 會得到 −0.0;JS 的 -0>=0 是 true,"
                             "用 v>=0?'+':'−' 會印成綠色的「+0.0%」"),
            ("0", "0.0%", "零不給正負號"),
            ("6.2", "+6%", "|v|≥1 取整數"),
            ("-21.75", "−22%", "負號要 U+2212,不是 ASCII hyphen"),
            ("-38.24", "−38%", ""),
            ("null", "—", "缺值不可印成 NaN%"),
        ]
        got = self.run_js(pre, [(c[2], f"fmtPct({c[0]})") for c in cases])
        for (inp, want, why), g in zip(cases, got):
            self.assertEqual(g, want, f"fmtPct({inp}) = {g!r},應為 {want!r}。{why}")
        # 明確帶 dp 時要照做
        self.assertEqual(self.run_js(pre, [("", "fmtPct(-38.24,1)")])[0], "−38.2%")

    def test_pctCol_treats_zero_and_negative_zero_as_neutral(self):
        pre = extract("fmtPct") + "\n" + extract("pctCol")
        got = self.run_js(pre, [("", f"pctCol({v})") for v in ("3", "-3", "0", "-0.0", "null")])
        self.assertEqual(got, ["var(--strong)", "var(--weak)", "var(--muted)",
                               "var(--muted)", "var(--muted)"],
                         "0 與 −0 不可上漲跌色")

    def test_no_inline_percent_formatter_bypasses_fmtPct(self):
        """單一入口才擋得住「同一個數字在兩個畫面長得不一樣」與 −0 的漏網。

        原本這條只檢查兩個舊拼法就宣稱「單一入口」,而模板裡還有 5 處自寫正負號
        (lensBar tooltip、熱圖 rel20、族群動能欄、台積電專區兩處),其中
        `mom>=0?strong:weak` 會把 −0.0 印成漲色的「+0.0%」——正是 fmtPct 要殺的 bug。
        改成掃全檔:任何「判正負號後接 % 或 pp」的寫法都不准繞過 fmtPct。"""
        src = TEMPLATE.read_text(encoding="utf-8")
        own = set(extract("fmtPct").splitlines())   # fmtPct 自己當然要判正負號
        bad = []
        for n, line in enumerate(src.splitlines(), 1):
            s = line.strip()
            if s.startswith(("/*", "*", "//")) or line in own:
                continue
            if re.search(r"[><]=?\s*0\s*\?\s*'[+−-]?'", line) and \
               re.search(r"'%'|%）|%\)|'pp'|\+'%", line):
                bad.append(f"L{n}: {s[:90]}")
        self.assertEqual(bad, [], "這些地方自己處理正負號,沒走 fmtPct:\n" + "\n".join(bad))
        self.assertEqual(len(re.findall(r"^function fmtPct\(", src, re.M)), 1)

    # ---------- lensShape:全站最容易誤導人的一段文案 ----------

    def test_lensShape_never_narrates_price_direction(self):
        """三欄是族群內橫斷面名次,不含漲跌資訊。標籤講「轉強/回檔/反彈」等於
        用名次宣稱價格事件——2026-07-24 有 10/14 檔被標「波段轉強」而 20 日
        絕對報酬是負的(最深 −34.9%)。標籤一律只能講名次。"""
        pre = extract("LENS_HI") + "\n" + extract("lensShape")
        pts = (0, 20, 39, 40, 50, 59, 60, 80, 100)
        cases = [(f"{a},{b},{c}", f"lensShape({a},{b},{c})")
                 for a in pts for b in pts for c in pts]
        labels = set(self.run_js(pre, cases))
        banned = ["轉強", "轉弱", "回檔", "反彈", "領漲", "落後", "跟上", "起漲",
                  "突破", "止跌", "翻多", "翻空", "會漲", "會跌"]
        for lab in labels:
            for word in banned:
                self.assertNotIn(word, lab,
                                 f"標籤「{lab}」用名次敘述價格事件(禁用詞:{word})")
            self.assertIn("名次", lab, f"標籤「{lab}」沒說清楚講的是名次")
        self.assertGreaterEqual(len(labels), 5, "標籤沒有分辨力")

    def test_lensShape_is_total_and_order_consistent(self):
        """任何百分位組合都要有標籤(不可回 undefined),且對稱輸入給對稱答案。"""
        pre = extract("LENS_HI") + "\n" + extract("lensShape")
        got = self.run_js(pre, [
            ("全高", "lensShape(100,100,100)"), ("全低", "lensShape(0,0,0)"),
            ("邊界 60", "lensShape(60,60,60)"), ("邊界 39.9", "lensShape(39.9,39.9,39.9)"),
            ("中間", "lensShape(50,50,50)"),
            ("波高趨低", "lensShape(50,100,0)"), ("趨高波低", "lensShape(50,0,100)"),
        ])
        self.assertNotIn(None, got)
        self.assertEqual(got[0], "三個週期名次都靠前")
        self.assertEqual(got[1], "三個週期名次都靠後")
        self.assertEqual(got[2], "三個週期名次都靠前", "60 是靠前的下界(含)")
        self.assertEqual(got[3], "三個週期名次都靠後", "39.9 仍算靠後")
        self.assertNotEqual(got[5], got[6], "波段↔趨勢對調應給不同標籤")

    def test_absCaveat_disappears_when_nothing_to_warn_about(self):
        """多頭時沒有「相對強但絕對跌」的個股,警語必須整句消失,不留半句空話。"""
        pre = ("const UPPER_TIERS={'真強':1,'蓄勢·外資佈局':1,'強但過熱':1};\n"
               "let D={allStocks:[]};\n" + extract("absCaveat"))
        got = self.run_js(pre, [
            ("空集合", "(D.allStocks=[],absCaveat())"),
            ("全為正", "(D.allStocks=[{nm:'A',tier:'真強',r20:5},"
                       "{nm:'B',tier:'真強',r20:1}],absCaveat())"),
            ("有負值", "(D.allStocks=[{nm:'A',tier:'真強',r20:5},"
                       "{nm:'B',tier:'真強',r20:-3.5}],absCaveat())"),
            ("−0 不算負", "(D.allStocks=[{nm:'A',tier:'真強',r20:-0.0}],absCaveat())"),
            ("弱層不計入", "(D.allStocks=[{nm:'A',tier:'真弱',r20:-30}],absCaveat())"),
        ])
        self.assertEqual(got[0], "")
        self.assertEqual(got[1], "")
        self.assertIn("1 檔 20 日絕對報酬為負", got[2])
        self.assertIn("B", got[2], "最深的那檔要指名")
        self.assertEqual(got[3], "", "−0 不是負值")
        self.assertEqual(got[4], "", "只看上層 tier")


if __name__ == "__main__":
    unittest.main()
