# 液冷不是 CDU 單點採購：FWS、TCS、ITE 與控制責任邊界決定可部署性

<!-- research_topic
topic_id: MI-2026-08-03-LIQUID-COOLING-LOOP-BOUNDARIES
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2022-10-18
last_reviewed_at: 2026-08-03
review_due: 2026-09-03
source_type: mixed
publisher: Open Compute Project
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf
source_chain_id: liquid-cooling-loop-boundary-primary-scan-20260803
stock_ids:
group_ids: thermal,powersupply,serverodm
trigger_type: interface_requirement_and_operations_contract
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: high
confidence_basis: OCP requirement document直接劃出 TCS／FWS／ITE 範圍，OCP 現行專案頁又把 cold plate、manifold、quick disconnect、coolant 與 CDU 拆成工作流；Lenovo 的部署指引及 NVIDIA 的 BMS 資料契約分別從系統實作與可觀測控制補強，因此可高信心建立責任邊界，但高信心只適用於架構，不延伸到個別供應商訂單或財務
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: captured_formal_loop_scope_and_operational_interfaces
evidence: source_chain:liquid-cooling-loop-boundary-primary-scan-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: rebuilt_fws_tcs_ite_control_and_maintenance_responsibility_map
evidence: sources:S1,S2,S3,S4,S5
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **FWS（Facility Water System）**：設施水系統，位於資料中心冷源與 CDU 的設施側；它負責把熱帶到冷卻塔、dry cooler 或 chiller，但 OCP Cold Plate Rev 2 不把它納入 TCS 規格範圍。
- **TCS（Technology Cooling System）**：技術冷卻系統，從 CDU 經 rack、manifold、ITE 冷板再回到 CDU 的二次迴路；冷卻液、管路、快接、壓力、流量與維護都在這一圈互相制約。
- **ITE（Information Technology Equipment）**：伺服器、加速器與內部冷板等 IT 設備。規格若只管 TCS，不代表 ITE 端所有設計與責任都已被涵蓋。
- **BMS（Building Management System）**：建築管理系統，收集溫度、流量、壓差、漏液與設備狀態，並在安全 guardrails 內執行控制或隔離。

### 三句話抓重點

- OCP Rev 2 明確說自己是 requirement document、不是完整 specification，且只涵蓋 CDU 到 rack、manifold、ITE 再回 CDU 的 TCS；FWS 與 ITE 本身都在文件範圍之外。
- Lenovo 的實作指引把 primary FWS 與 secondary technology loop 分開，並要求 CDU 備援、感測、閥件、漏液偵測、材料與水質維護；NVIDIA DSX 又把這些條件變成 BMS 可交換的資料與控制點。
- 因此單一 CDU 被平台列名或容量較大，只證明一個設備節點；完整部署還要通過流體、材料、連接器、manifold、ITE、控制、維護與責任交接，不能直接等同客戶驗收或供應商收入。

### 為什麼重要

現有液冷研究已能比較部分 CDU 額定容量與平台狀態，但「一台設備能帶走多少熱」沒有回答
「整套系統由誰負責、故障在哪裡被偵測、維修時如何隔離」。液冷的實際風險往往發生在
跨廠介面：FWS 水質影響 TCS 熱交換器、TCS 材料與流體影響腐蝕、快接與 manifold 影響
漏液及維修、ITE 阻力影響流量分配，BMS 則決定告警與隔離能不能真的執行。

### 接下來怎麼追

- 追 OCP Cold Plate 的 requirement、qualification checklist、cold plate base spec、coolant 與 UQD／blind-mate 規格是否升版並形成可重現測試。
- 追 NVIDIA DSX BMS contract 與 Marketplace 是否把設備 validation 延伸到 site-level commissioning、telemetry completeness、leak isolation 及 field reliability。
- 追台灣散熱、電源供應與伺服器 ODM 是否公開責任範圍：只供元件、供 rack loop、整合 CDU／BMS，或承擔場域驗收與維護；再核對量產與財務分母。

### 想一想

- CDU 通過平台驗證，但客戶現場的水質、壓差或 rackLocationId 映射不合格，這算產品問題、系統整合問題，還是設施責任？
- 快接、manifold、冷板與流體各自通過單件測試，是否足以證明混合多家供應商後仍能長期可靠運作？
- 同一家公司若同時賣電源、CDU 與控制，研究上應如何證明它真的承接較多價值，而不是只擁有較寬的產品型錄？

## 主張與證據帳本

本篇把「要求文件」「平台資料契約」「產品列名」「場域部署」「財務認列」分開。
證實的責任邊界不自動證明某一家供應商能提供完整方案，更不證明台灣公司已取得訂單。

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project
title: Cold Plate Cooling Loop Requirements Rev 2
published_at: 2022-10-18
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf
locator: p.5 Introduction；文件自稱 requirement document and not a specification，並定義 TCS 為 CDU 至 rack、manifold、ITE 再回 CDU；FWS 與 ITE 本身不在範圍內
limitation: PDF 正文未標可定位的批准日，published_at 採 Rev 2 在 2022 OCP Global Summit 首次公開展示的 2022-10-18 作 public anchor；本文件是要求框架，不是單一產品、完整場域設計或客戶驗收證據
independence_group: open-compute-project
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Cold Plate Sub-Project
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://www.opencompute.org/community/cold-plate
locator: 2026-08-03 Scope；TCS from cold plate to CDU，列出 cold plates、tubing、manifolds、QDs、CDUs，並連到現行 workstreams
limitation: 動態專案頁只證明捕捉日的專案範圍與工作流；不提供各文件固定版本、產品 qualification、客戶部署、供應商份額或財務貢獻
independence_group: open-compute-project
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Lenovo
title: Lenovo Neptune Direct Water-Cooling Standards
published_at: 2024-09-13
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://lenovopress.lenovo.com/lp2018-lenovo-neptune-direct-water-cooling-standards
locator: Solution tiers 的 FWS／TCS separate loops；Neptune compliant data center design 與 Cooling Distribution Units；另見 Direct Water-Cooling Quality、Water Treatment、Monitoring
limitation: Lenovo 文件是自家平台實作與建議，不是所有資料中心的唯一標準；產品案例、tier 與建議不能直接外推為跨供應商測試結果、採購量或財務貢獻
independence_group: lenovo
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DSX Exchange BMS Integration Companion Guide
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://docs.nvidia.com/dsx-exchange/bms-integration
locator: Object Types and Point Types；RackLiquidSupplyTemperature、ReturnTemperature、Flow、DifferentialPressure、LeakDetect、LiquidIsolationStatus／Request，以及 BMS guardrails 與 rackLocationId pre-deployment requirement
limitation: 動態技術文件是 NVIDIA DSX 的資料與控制契約，不證明特定 site 已完整實作、感測器精度、field reliability、設備供應商或財務結果
independence_group: nvidia
-->

<!-- research_source
source_id: S5
role: other_primary
source_kind: living_index
publisher: NVIDIA Marketplace
title: DSX Infrastructure for AI Factory validated CDU list
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/
locator: 2026-08-03 CDU 清單的 vendor、model、cooling capacity、validation type、wetted materials 與 supply chain status 欄位
limitation: 動態清單沒有不可變版本、完整跨廠測試協定、site commissioning、field reliability、訂單或財務資料；列名只是一個資格節點
independence_group: nvidia-marketplace
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-03 起追蹤 thermal、powersupply、serverodm 族群公司的法說、季報與重大訊息
limitation: 索引頁本身不證明液冷責任範圍、客戶、驗收、量產、收入或毛利；命中文件後須另建 document source 並雙向核對
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP Cold Plate Cooling Loop Requirements Rev 2 是 requirement document 而非完整 specification；其適用範圍是 CDU 經 rack、manifold 與 ITE 再回 CDU 的 TCS，FWS 與 ITE 本身不在文件範圍內
supporting_source_ids: S1
contrary_source_ids:
as_of: 2022-10-18
basis: S1 p.5 直接描述文件性質、TCS 流路及兩個排除範圍
boundary: 只證實該要求文件的 scope；不代表 FWS／ITE 不重要，也不表示任一設備符合要求、完成 specification 或已被客戶驗收
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: OCP Cold Plate Sub-Project 的現行範圍從 cold plate 到 CDU，並把 tubing、manifold、quick disconnect、coolant 與 CDU 等介面列入不同文件或工作流
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-03
basis: S2 Scope 與 current workstreams 直接列出 TCS ingredients 與持續標準化項目
boundary: 專案範圍與工作流不等於所有項目已有 final specification、跨廠 qualification 或量產部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Lenovo 的部署指引把 facility primary loop 與 technology secondary loop 分開，並把 CDU 備援、可維修性、過濾、溫度／壓力／流量感測、閥件、漏液偵測以及 fluid chemistry 納入系統要求
supporting_source_ids: S3
contrary_source_ids:
as_of: 2024-09-13
basis: S3 separate loops、quality／water treatment／monitoring 與 Cooling Distribution Units 段落共同列出設計和營運條件
boundary: 這是 Lenovo reference practice，不是所有平台共同的最低規格，也不形成 CDU 供應商的跨公司排名或採購證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: NVIDIA DSX BMS contract 為 rack 液冷定義 supply／return temperature、flow、differential pressure、leak detection 與 liquid isolation 等資料或控制點，並要求 BMS 對外部 setpoint／action request 套用安全 guardrails
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-03
basis: S4 Object Types and Point Types、Guardrails 與 Integration-Published Points 直接列出欄位、權責和控制原則
boundary: 資料契約只代表可被交換的語意，不證明每個 site 感測完整、數值正確、控制已 commissioned 或隔離動作在 field 成功
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: 液冷可部署性是一份跨 FWS、TCS、ITE、控制與維護的介面契約；單一 CDU 的額定容量、平台列名或單件 qualification 是必要但不足的成熟度證據
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-03
basis: S1 劃出範圍缺口，S2 顯示多個介面仍各自標準化，S3 把設計延伸到水質與維護，S4 定義可觀測與隔離責任，S5 則只提供設備列名欄位；五者共同顯示 site readiness 超出單一設備
boundary: 這是系統工程推論，不宣稱每個專案採相同拓撲、每個介面同等重要、單一 integrator 必須承擔全部責任，亦不評估供應商市占或財務
verification_needed: 需具名客戶的 interface control document、site acceptance test、commissioning、field reliability 及責任矩陣驗證實際部署
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 台灣 thermal、powersupply、serverodm 族群已有公司承擔可辨識的完整液冷迴路整合、site acceptance 與維護責任，並取得具財務重大性的量產收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有一手來源能證明架構與若干產品資格，不能由公司產品型錄或平台列名重建合約責任、部署分母、收入與毛利
boundary: 不把 CDU／cold plate／server 系統產品存在、MOU、PoC 或平台列名改寫成完整責任與財務事實
verification_needed: 需客戶驗收或合約範圍、公司法說／季報、具名部署數量與售後責任交叉核對
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: NVIDIA Marketplace 的 CDU 清單把 vendor、model、cooling capacity、validation type、wetted materials 與 supply chain status 作為設備層欄位，但沒有 site acceptance、commissioning 或 field reliability 欄位
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-03
basis: S5 捕捉日可定位清單欄位；未出現的 site-level 證據依頁面可見欄位邊界判讀
boundary: 動態頁面可能更新，本文不保存不可變外部快照；缺欄位不代表供應商沒有內部資料，只表示該公開清單不能支持 site-level 結論
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 一張責任地圖

| 邊界 | 主要對象 | 必須交接的資訊 | 典型失效 | 本輪證據層級 |
|---|---|---|---|---|
| FWS ↔ CDU | 設施冷源、heat exchanger、primary piping | 供回水溫、壓力、流量、水質、可用性 | 冷源不足、污染、壓差不合、維修責任不清 | OCP scope 排除＋Lenovo 實作指引 |
| CDU ↔ TCS | 泵、heat exchanger、secondary loop、控制 | setpoint、流量、壓差、過濾、備援、告警 | 泵故障、過濾堵塞、控制不穩 | Lenovo 指引＋NVIDIA BMS points |
| TCS ↔ rack／manifold | piping、QD、manifold、valve | 介面尺寸、材料、壓降、漏液與隔離 | 快接漏液、流量失衡、不可不停機維修 | OCP workstreams＋NVIDIA isolation points |
| manifold ↔ ITE／cold plate | server tray、cold plate、內部 tubing | 熱負載、阻力、流量、材料、污染控制 | hotspot、腐蝕、堵塞、冷板失效 | OCP requirement boundary＋Lenovo quality guidance |
| BMS ↔ IT／OT | sensor、event bus、cluster manager、operator | stable ID、value quality、guardrail、action ownership | 錯 rack 隔離、無效 setpoint、告警無人負責 | NVIDIA DSX contract |

這張表刻意不指定「誰一定是贏家」。同一專案可以由 ODM、冷卻設備商、機電承包商、
設施營運方與平台商分別負責不同列；真正的商業價值要看合約責任、驗收、維護與收入分母，
不是產品型錄涵蓋的方框數。

## 成熟度階梯：列名只是中段，不是終點

| 階段 | 可接受證據 | 還不能知道 |
|---|---|---|
| Requirement／scope | OCP 定義 TCS 介面與排除範圍 | 某產品是否合格、某 site 如何實作 |
| Component／equipment qualification | cold plate、QD、manifold、CDU 的可重現測試 | 混合多家產品後能否通過整套系統驗收 |
| Platform listing | NVIDIA Marketplace 的具名型號與狀態 | 現場水質、BMS、commissioning、客戶採購與收入 |
| Site acceptance | 具名場域的 interface control、SAT、漏液／隔離與冗餘測試 | 長期可靠度與全生命週期維護成本 |
| Field operation／financial | 部署分母、故障率、維護紀錄與供應商財報 | 未揭露專案仍不能被反向猜測 |

## 研究判定

- **可高信心發布**：液冷是跨 FWS、TCS、ITE、控制與維護的介面系統，單一 CDU 列名不足以代表場域部署成熟。
- **高信心的邊界**：只涵蓋架構與證據階梯；公司供貨、訂單、收入、市占、毛利及完整方案責任仍未驗證。
- **相對現有研究的新增知識**：從「容量與供應狀態」前進到「責任、可觀測性、隔離與維運」，不是再做另一張 CDU 排名。
- **升格為公司研究的條件**：客戶與供應商雙向確認 interface scope、site acceptance、deployment denominator 與可辨識財務結果。

## 來源

- [OCP：Cold Plate Cooling Loop Requirements Rev 2](https://www.opencompute.org/documents/cold-plate-cooling-loop-requirements-rev-2-pdf)
- [OCP：Cold Plate Sub-Project](https://www.opencompute.org/community/cold-plate)
- [Lenovo：Neptune Direct Water-Cooling Standards](https://lenovopress.lenovo.com/lp2018-lenovo-neptune-direct-water-cooling-standards)
- [NVIDIA：DSX Exchange BMS Integration](https://docs.nvidia.com/dsx-exchange/bms-integration)
- [NVIDIA Marketplace：DSX Infrastructure validated CDU list](https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: cold plate、QD、manifold、CDU、流體與 leak isolation 都是散熱族群的可驗證搜尋路由，且責任邊界比單一容量更能區分商業成熟度
evidence_boundary: 不把產品存在、平台列名或規格必要性改寫成具名客戶、site acceptance、訂單、收入或毛利
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: CDU 泵浦、控制、冗餘電源、BMS 與 rack 電液隔離形成電源供應族群的相鄰整合路由
evidence_boundary: 產品組合較寬不等於承擔完整 liquid loop 合約或取得較高財務價值，需合約與分部資料驗證
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: ODM 位於 ITE、rack manifold、BMC／cluster manager 與 site integrator 的交界，可能承擔介面整合與驗收責任
evidence_boundary: 平台生態系列名、伺服器產品或 MOU 不證明 ODM 承包 site-level FWS／TCS、維護或財務貢獻
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5,C7
metric: OCP 與 NVIDIA 是否發布新版 requirement、qualification、BMS contract 或 site-level validation，改變 FWS／TCS／ITE／control 責任邊界
source_ids: S1,S3
watch_source_ids: S2,S4,S5
frequency: monthly
next_check: 2026-09-03
trigger: 新文件提供可重現 interface test、site commissioning、leak isolation、field reliability 或責任矩陣
invalidation: 新版標準或 field evidence 顯示單一設備 qualification 已足以覆蓋本文所列介面與場域風險
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C6
metric: 台灣 thermal、powersupply、serverodm 公司是否公開可雙向核對的液冷合約責任、site acceptance、部署分母與財務貢獻
source_ids: S1,S3,S4
watch_source_ids: S6
frequency: quarterly
next_check: 2026-09-30
trigger: 客戶與公司文件共同指向具名場域、責任範圍、驗收、量產部署及收入／毛利分母
invalidation: 公司明確只供單件且不承擔整合，或專案長期停在 MOU／PoC／sample 而未進場域驗收
-->

## 什麼會推翻這篇

- 具名 production site 的文件顯示 CDU qualification 已內含 FWS、TCS、ITE、BMS、流體、維護與 field reliability 的完整共同驗收，沒有額外介面缺口。
- OCP 或平台商刪除多數 interface workstreams，並以可重現 field data 證明模組化混搭不再需要個別材料、流體、QD、manifold 與控制驗證。
- 若台灣公司的公開文件始終無法說明責任範圍與部署分母，族群圖譜只應保留搜尋路由，不應升格為公司商業曝險。
