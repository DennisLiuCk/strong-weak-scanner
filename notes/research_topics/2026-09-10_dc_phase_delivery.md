# AI機房已全數簽租，何時才可交付？Beacon Point的兩期時間表

<!-- research_topic
topic_id: MI-2026-09-10-DC-PHASE-DELIVERY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-09-10
source_published_at: 2026-08-10
last_reviewed_at: 2026-09-10
review_due: 2026-10-10
source_type: mixed
publisher: J.P. Morgan
publisher_domain: jpmorgan.com
canonical_url: https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers
source_chain_id: beacon-point-phase-delivery-20260910
stock_ids:
group_ids: serverodm,powersupply,thermal
trigger_type: project_financing_and_phase_delivery
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C1
base_confidence: medium
confidence_basis: 機構文章提出融資與交付問題，公司逐期公告及季報提供可定位的差異；J.P. Morgan也是第一期承銷參與者，交易事實不算獨立信用驗證，實際交付仍待後續文件
cross_company_numbers: false
-->

<!-- transition
date: 2026-09-10
from: initial
to: inbox
reason: captured_institutional_project_finance_case
evidence: source_chain:beacon-point-phase-delivery-20260910
-->
<!-- transition
date: 2026-09-10
from: inbox
to: triaged
reason: separated_campus_lease_phase_financing_and_delivery_dates
evidence: sources:S1,S2,S3,S4,S5,S6
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Beacon Point**：Hut 8在美國德州Nueces County開發的資料中心園區，本文分開看兩期工程。
- **IT容量**：資料廳可供運算設備使用的功率；MW是功率單位，不是晶片數或實際運算量。
- **公用電力容量**：供應園區的電力規模，還要支應冷卻等設施；不能與IT容量混用。
- **全數簽租**：約定範圍已有租客承租，交付及付款仍依各期合約推進。
- **通電與資料廳交付**：前者是電力設施開始送電，後者是向客戶交付機房空間與約定設施，時間可以不同。
- **三淨租約（triple-net）**：通常由租客承擔約定的稅費、保險與維護支出，實際責任仍以合約為準。
- **無追索融資（non-recourse）**：本案債務由專案公司承擔，不能因此省略專案資產、限制用途資金與履約風險。

### 三句話抓重點

- Hut 8在7月為Beacon Point簽下第二期租約，但8月季報仍把第二期融資列為正在推進的工作。
- 第一期的初次通電與資料廳交付也排在不同季度，供應鏈要按期別及工作內容追蹤設備需求。
- 目前可研究的是合約如何走向實際交付；台灣供應商的訂單、驗收與收款仍需另外核對。

### 為什麼重要

看到「一座園區已全數簽租」，很容易把整座機房想成即將一起啟用。Beacon Point提供了
一個更具體的情境：同一租客承租兩期，兩期卻有不同的融資與交付進度。研究AI供應鏈時，
這個差別會改變下一份該找的資料——電源設備可能在配電施工階段交付，伺服器和散熱系統
則要再對準資料廳及客戶的安裝驗收安排。這是研究順序，不是本文已掌握的供應商出貨表。

### 接下來怎麼追

- 10月10日人工回查公司公告，先找第二期融資是否完成，再核對公告涵蓋的建設範圍。
- 按公司最新文件分別追蹤初次通電、第一期資料廳與第二期資料廳；取得租金起算及交付條款後再往現金流延伸。

### 想一想

- 如果第二期已簽租但仍待融資，新增租約最先增加的是需求可見度，還是已可使用的算力？
- 如果電力設施先通電，伺服器是否已安裝、驗收並開始替客戶工作，還需要哪些證據？

## 把兩期放回同一張時間表

J.P. Morgan在8月10日的公開文章把專案融資與供電限制放在一起討論，並以Beacon Point
的6月債券為案例。沿著這個案例回查，公司7月及8月文件已把園區拆成兩期。下表只列
有來源可定位的狀態；所有未來日期都是公司當時的目標，並非本站確認的完工日。

| 要看的事 | 第一期 | 第二期 |
|---|---|---|
| 已簽約的IT容量 | 352 MW | 另352 MW，租客與第一期相同 |
| 融資 | 6月9日完成42.5億美元專案債券 | 8月4日季報仍稱正在尋求建設融資 |
| 施工與通電 | 8月4日稱一期及變電站施工中，目標2027年第1季初次通電 | 7月簽租後進入公司「施工中」分類，未因此等同已交付 |
| 初次資料廳交付 | 8月4日目標為2027年第3季 | 7月20日公告及8月4日季報預期2028年第2季開始 |

容量與第二期時程見[S2：7月租約公告](https://www.hut8.com/news-insights/press-releases/hut-8-fully-commercializes-1-gw-beacon-point-ai-data-center-campus-with-second-352-mw-it-lease)；
一期工程目標見[S3：8月財報稿](https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results)；
第二期融資狀態見[S4：季報第66頁](https://www.sec.gov/Archives/edgar/data/1964789/000110465926090025/hut-20260630x10q.htm)；
債券完成日期見[S5：融資公告](https://www.hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data)。

另一個容易混淆的地方是園區標題中的「1 GW」。7月公告將它用於公用電力容量，兩期
合計簽約IT容量為704 MW。讀者應保留這兩個名稱，不能把它們相減後就推成冷卻耗電、
能效或閒置率；目前缺少同一運轉負載下的實測資料。

## 錢先到位，下一關仍要逐期完成

銀行看長期租約，可以評估專案未來用什麼收入償債；設備供應商看同一份消息，還需要
知道哪一批工程已發包、何時交貨及由誰驗收。兩者都重視需求，卻使用不同的時間單位。
一張多年租約可以提高規劃的可見度，設備收入則要回到各筆契約和實際履行。

在本案，第一期已募得的資金有指定用途，包括資料中心、變電站、償債準備金及交易費用。
季報也說明，建設及償債專戶中的款項列為限制用途現金，租金預期是債券償付的主要來源。
這讓後續追蹤有了清楚順序：先辨認是哪一期的資金，再找工程、交付與現金開始流入的條件。
本文沒有取得足以裁決延遲交付時租金起算及賠償責任的完整條款，因此沒有替專案推算回收年限。

「無追索」也有指定對象。季報說這筆債務由Beacon Point專案公司承擔，母公司及租客
不提供保證。這是在說償債責任，不能順手寫成專案沒有負債，或由投資等級租客保證債券。
專案財務與母公司財務應各自查看。

## 有哪些證據支持繼續追蹤

目前的進度並非只剩規模宣傳。7月公司公告稱，園區完整電力容量已有AEP Texas的
電力輸送互聯協議，場地準備進行中，長交期關鍵設備也已採購。8月財報稿再列出第一期
及變電站施工。這些公司披露支持繼續追工程進度，也縮小了「只有意向、尚未執行」的疑慮。
不過，採購、送電及資料廳交付在文件中仍是不同節點；下一次更新應各自增加證據。

同時，J.P. Morgan明示自己是第一期債券的承銷參與者。它的公開說明很適合用來理解
融資結構及執行風險，但不能與Hut 8的同案公告相加，當成兩家互不相關機構替信用品質
背書。本文採用的是「機構提出問題，公司文件核對細節」的方法，而不是投行招牌的投票。

## 對台股族群，下一份有價值的資料長什麼樣

| 族群 | 下一步值得找的具體資料 | 它能解答什麼 |
|---|---|---|
| 電源供應 | 具名專案期別、設備交期、送電及系統驗收責任 | 設備是否能配合該期工程，而非只知道園區需要用電 |
| 散熱 | 冷卻設備的採購範圍、資料廳負載與現場驗收紀錄 | 從設計能力走到可維護、可交付的系統 |
| 伺服器組裝／機構 | 買方平台、安裝批次、交付驗收及付款安排 | 機房建設何時對上IT設備的實際需求 |

這三組問題是本案的研究路由。本輪未找到足以把Beacon Point訂單或營收歸到本站
台灣公司的證據，因此文章保留族群觀察，沒有填入個股受惠名單。若之後公司公布具名
產品或客戶，應先對上期別，再接出貨與財務資料。

10月的人工回查會先問：第二期是否取得確定融資？兩期交付目標有無調整？已採購設備
是否開始到貨、通電或驗收？若融資與交付條件已有實質進展，研究重心應隨之移動；若
日期延後或新增成本，則追延後的原因與責任。重複公告園區總規模，本身不增加交付證據。

## 主張與證據帳本

公司披露的合約及時點不是抽樣統計，SE／t不適用；未來交付目標未附誤差帶。
本案只有一個園區，不能據此估計整體產業的延遲率、回收期或台廠受惠程度。

<!-- research_source
source_id: S1
role: market_estimate
source_kind: document
publisher: J.P. Morgan Investment Banking
title: Powering progress: Financing the infrastructure behind US data center growth
published_at: 2026-08-10
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers
locator: How debt financing structures AI infrastructure capital；Why time to power is the critical constraint；Beacon Point承銷角色段
limitation: 投行業務團隊公開分析且參與第一期交易；不算同案信用的獨立驗證，本文未採CapEx總額與利差排名
independence_group: jpmorgan-project-finance-analysis
-->
<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Hut 8
title: Hut 8 Fully Commercializes 1 GW Beacon Point AI Data Center Campus with Second 352 MW IT Lease
published_at: 2026-07-20
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.hut8.com/news-insights/press-releases/hut-8-fully-commercializes-1-gw-beacon-point-ai-data-center-campus-with-second-352-mw-it-lease
locator: Transaction Highlights與Partnership-driven execution段；原HTML的公開Nuxt正文資料
limitation: 公司宣告的簽約與工程狀態；交付目標前瞻，互聯協議不等於實際送電，沒有台灣供應商財務歸因
independence_group: hut8-beacon-point
-->
<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Hut 8
title: Hut 8 Reports Second Quarter 2026 Results
published_at: 2026-08-04
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.hut8.com/news-insights/press-releases/hut-8-reports-second-quarter-2026-results
locator: Digital Infrastructure施工段、Capital Strategy第二期融資段；涵蓋截至6/30季度及7月後續事件
limitation: 2027通電與交付屬公司目標；頁面表格與正文分開，不能只讀搜尋摘要
independence_group: hut8-beacon-point
-->
<!-- research_source
source_id: S4
role: company_filing
source_kind: document
publisher: Hut 8／SEC
title: Form 10-Q for the quarter ended June 30, 2026
published_at: 2026-08-04
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.sec.gov/Archives/edgar/data/1964789/000110465926090025/hut-20260630x10q.htm
locator: p.27 Beacon Point Notes；p.49 Phase 2；p.52施工分類；p.66第二期融資；SEC filing index為8/4、期末6/30
limitation: 季報兼有期末狀態與7月後續事件，須逐段讀時點；未在本輪取得足以裁決延遲交付租金起算的完整條款
independence_group: hut8-beacon-point
-->
<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: Hut 8
title: Hut 8 Closes $4.25 Billion of Investment-Grade Senior Secured Notes for Beacon Point Data Center Project
published_at: 2026-06-09
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.hut8.com/news-insights/press-releases/hut-8-closes-usd4-25-billion-of-investment-grade-senior-secured-notes-for-beacon-point-data
locator: 發債完成首段與Issuer intends to use the proceeds三項用途
limitation: 本次融資對應352 MW第一期及相關設施，不自動涵蓋7月才簽租的第二期
independence_group: hut8-beacon-point
-->
<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Hut 8
title: Press Releases
published_at:
captured_at: 2026-09-10
accepted_at: 2026-09-10
status: active
url: https://www.hut8.com/news-insights/press-releases
locator: 9/10可見8/10社區與電網公開信、8/4季度財報及7/20第二期租約；最新公開信仍描述Beacon Point開發中
limitation: 持續變動索引只作回查入口；當日未見新融資稿不能證明場外沒有事件
independence_group: hut8-beacon-point
-->

<!-- research_claim
claim_id: C1
label: inference
status: active
claim: Beacon Point的下一個資訊增量在分期融資、通電與資料廳交付，園區全數簽租應拆成各期進度追蹤
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-09-10
basis: 機構提出執行風險，公司文件顯示兩期融資與交付時點不同
boundary: 這是單案研究框架，不是產業延遲率或債券信用判定
verification_needed:
-->
<!-- research_claim
claim_id: C2
label: verified
status: active
claim: 7/20公司公告第二期352 MW IT租約，兩期合計704 MW IT，對應園區1,000 MW公用電力容量
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-09-10
basis: 公告首段區分IT與utility capacity及同一租客
boundary: 簽約容量不是在運容量，也不提供可推算能效的實測分母
verification_needed:
-->
<!-- research_claim
claim_id: C3
label: verified
status: active
claim: 第一期42.5億美元債券於6/9完成；8/4季報仍稱正為第二期尋求建設融資
supporting_source_ids: S4,S5
contrary_source_ids:
as_of: 2026-09-10
basis: 融資公告與季報p.66逐期對照
boundary: 僅重述各文件時點，不宣稱第二期在9/10必然仍未融資
verification_needed:
-->
<!-- research_claim
claim_id: C4
label: verified
status: active
claim: 公司目標為一期2027Q1初次通電、2027Q3初次資料廳交付；第二期預期2028Q2開始交付
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-09-10
basis: S3一期施工段與S2第二期Delivery Timeline
boundary: 只證實公司公布這些目標，不證實如期實現、全期完工或已起租
verification_needed:
-->
<!-- research_claim
claim_id: C5
label: verified
status: active
claim: 公司7月披露互聯協議、場地準備及長交期設備採購，8月披露第一期與變電站施工中
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-09-10
basis: S2執行段與S3 Digital Infrastructure
boundary: 為公司工程披露，未由電網或承包商獨立驗收，也不代表資料廳交付
verification_needed:
-->
<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 季報將建設及償債專戶款項列限制用途現金；第一期債券由專案公司承擔，母公司與租客未保證
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-09-10
basis: p.27 Beacon Point Notes的擔保與專戶說明
boundary: 不把無追索改寫成沒有負債，亦未評價債券償付機率
verification_needed:
-->
<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: 各期租金起算、延遲交付責任及台灣供應商的具名驗收與收款，尚待取得可對應條款及公司證據
supporting_source_ids:
contrary_source_ids:
as_of: 2026-09-10
basis: 現有文件尚不能完成這些逐期及供應商層級判斷
boundary: 不由長約、客戶評級或園區容量推台廠訂單與收益
verification_needed: 合約起租及延遲條款、具名供應商公告和同一期別的驗收收款資料
-->

## 來源與證據邊界

- [S1：機構公開融資分析及交易參與角色](https://www.jpmorgan.com/insights/banking/capital-markets/financing-ai-infrastructure-data-centers)
- S2–S5已在時間表逐項連到原文；均為同一公司的不同文件，不增加獨立公司樣本。
- [S6：公司後續公告入口](https://www.hut8.com/news-insights/press-releases)。下一輪只在新文件改變主張時追加證據。

## 影響路由

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-10
rationale: 對照資料廳期別與IT設備安裝驗收
evidence_boundary: 缺少台灣公司的具名訂單與收款證據
-->
<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-10
rationale: 核對工程供電設備的交貨及送電條件
evidence_boundary: 園區電力容量不能換算供應商營收
-->
<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-10
rationale: 對照各期冷卻系統負載與現場驗收
evidence_boundary: 缺少台灣供應商的採購範圍及實績
-->

## 持續驗證清單

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C3,C4,C5
metric: 第二期融資、各期通電與資料廳交付進度
source_ids: S2,S3,S4,S5
watch_source_ids: S6
frequency: monthly
next_check: 2026-10-10
trigger: 公司發布第二期融資完成、新工程時點或交付更新
invalidation: 原融資缺口已解決則移轉研究重心；時程延後或工程條件變更則修正進度判讀
-->
<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C6,C7
metric: 專案資金用途、起租條件及供應商驗收與收款
source_ids: S4,S5
watch_source_ids: S6
frequency: quarterly
next_check: 2026-11-10
trigger: 新季報或合約附件可對上期別、起租與實際現金流
invalidation: 若付款條件或工程範圍與原解讀不同，縮窄主張；仍缺供應商證據則維持觀察
-->
