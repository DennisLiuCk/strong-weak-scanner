# AI 機櫃控制契約：Telemetry 要連到隔離動作才有營運意義

<!-- research_topic
topic_id: MI-2026-08-07-AI-RACK-ACTION-CONTRACT
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-07
source_published_at: 2026-07-31
last_reviewed_at: 2026-08-07
review_due: 2026-08-31
source_type: mixed
publisher: NVIDIA
publisher_domain: docs.nvidia.com
canonical_url: https://docs.nvidia.com/dsx-exchange/schema/bms-event-bus/overview
source_chain_id: ai-rack-action-contract-primary-scan-20260807
stock_ids:
group_ids: serverodm,powersupply,thermal
trigger_type: platform_control_contract
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: NVIDIA DSX BMS Event Bus 1.0.0 已把 rack identity、value／metadata、integration publisher、liquid／electrical isolation request 與 isolation status 放進同一資料契約；OCP OpenRMC 與 DMTF Redfish 另從 rack manager 與通用管理介面提供獨立邊界。公開資料仍缺 production handshake、動作延遲、失敗與復原紀錄、跨平台 conformance，以及台灣公司合約與財務證據
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-07
from: initial
to: inbox
reason: captured_dsx_event_and_isolation_contract
evidence: source_chain:ai-rack-action-contract-primary-scan-20260807
-->
<!-- transition
date: 2026-08-07
from: inbox
to: triaged
reason: separated_telemetry_semantics_action_ownership_and_field_outcomes
evidence: sources:S1,S2,S4,S6
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Telemetry（遙測）**：設備持續送出的溫度、流量、功率、漏液、狀態等資料；有數值不代表接收端知道它屬於哪個機櫃，也不代表系統會採取動作。
- **Metadata（中繼資料）**：描述數值是什麼、單位、設備身分與關係的上下文；同一個 `32.5` 可能是攝氏溫度、百分比或功率，必須靠 metadata 才能解讀。
- **Action contract（動作契約）**：不只定義誰送資料，也定義誰可以提出請求、誰有權決定、要回到哪個狀態，以及失聯或越界時的安全行為。
- **BMS／RMC**：BMS 是設施端建築管理系統；RMC 是機櫃管理控制器。兩者可能看到相似資料，但控制範圍與責任並不相同。
- **DSX**：NVIDIA 的 AI factory 基礎設施資料與控制契約；本篇引用的是其中 BMS Event Bus，不代表所有場域已部署。
- **OpenRMC**：OCP 的開放機櫃管理控制器專案，處理 rack manager 的硬體、軟體與介面邊界。
- **Redfish**：DMTF 定義的設備管理 API 標準，提供通用資源與動作模型；有 Redfish 介面不等於已實作 DSX 的隔離狀態機。

### 三句話抓重點

- NVIDIA DSX BMS Event Bus 1.0.0 把即時值與 metadata 分開，要求穩定的 rack identity，並為液冷與電力隔離定義 request／status point types。
- DSX 文件明示外部 IT integration 只能提出 request，BMS 仍是是否執行動作的最終權威，且應用 guardrail 與失聯 safe default；漏液 tray 訊息則被列為 informational，不要求 BMS 動作。
- 這足以建立「資料何時能進入營運決策」的檢驗框架，不能證明任何場域已成功隔離、跨平台完全互通、台灣公司取得訂單，或 telemetry 本身形成獨立獲利。

### 為什麼重要

把感測器數量或資料點數直接當成「智慧機櫃價值量」會漏掉最難的部分：同一個物理機櫃是否有
一致身分、數值是否帶時間與品質、接收端是否知道語意、誰能提出動作、誰負責安全裁決，以及
動作後能否看到隔離與復原狀態。任一段缺失，dashboard 可以很漂亮，卻不一定能支援故障隔離。

### 接下來怎麼追

- 追 DSX 的 isolation request／status 是否補上 acknowledgement、timeout、rejection reason、手動 override、復原與 service ticket 的完整狀態機。
- 追 OpenRMC／Redfish profile 或 conformance 工具能否把 rack identity、事件、action 與 telemetry 的最低共同集合跨供應商驗證。
- 追具名 production site 的注入測試、隔離延遲、成功／失敗結果與維修閉環；再由客戶和台灣公司申報雙向確認責任、部署量及財務分母。

### 想一想

- 若溫度與漏液都有數值，但 rack ID 在 IT 與 OT 兩邊不一致，系統該隔離哪一座機櫃？
- 告警、請求與命令是不是同一件事？誰對越界請求說「不」，失聯時又由誰回到安全狀態？
- 一個平台公開 schema，是否等於所有 OpenRMC／Redfish 裝置已能互通，或台灣 ODM 已因而取得收入？

## 主張與證據帳本

本文把平台資料契約、通用 rack-manager 管理介面、實際場域結果與公司財務曝險分開。
「證實」只到文件可定位的欄位、發布責任與介面範圍；deployment、跨廠 interoperability、
field outcome 與台灣供應商一律不由規格存在推導。

<!-- research_source
source_id: S1
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DSX Exchange BMS Event Bus 1.0.0 Overview
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://docs.nvidia.com/dsx-exchange/schema/bms-event-bus/overview
locator: BMS Event Bus 1.0.0 的 Value／Metadata、publisher rules、integration publishing contract、topic derivation 與 Rack point types；2026-08-07 擷取
limitation: 動態平台文件會更新；它定義 NVIDIA DSX 的 MQTT contract，不是跨平台標準、production deployment、field reliability、台灣供應商或財務證據
independence_group: nvidia-dsx
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DSX Exchange BMS Integration Companion Guide
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://docs.nvidia.com/dsx-exchange/bms-integration
locator: Value vs. Metadata、Publisher Rules、Integration-Published Points、Guardrails、Rack Identifier Fields 與 Point Types；2026-08-07 擷取
limitation: Companion guide 是 DSX implementation guidance；「應執行隔離」與 guardrail 建議不證明任何場域已 commissioned、動作成功、延遲達標或故障後完成維修
independence_group: nvidia-dsx
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: living_index
publisher: NVIDIA
title: Mission Control to BMS Data Catalog
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://docs.nvidia.com/datacenter/dsx/bms-datacatalog-interactive.html
locator: 頁面顯示 Last Updated 2026-07-31、29 records；Value／Metadata payload、rackName／rackID coordination、BMS／BCM read-write 欄位
limitation: 這是動態資料目錄且與新 Event Bus 文件的命名／架構可能演進；資料點與 R／W 欄不等於 production action sequence、跨平台 conformance 或商業價值
independence_group: nvidia-dsx
-->

<!-- research_source
source_id: S4
role: standard
source_kind: document
publisher: Open Compute Project
title: OpenRMC Design Specification v1.0.0
published_at: 2020-07-15
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://www.opencompute.org/documents/openrmc-design-specification-v1-0-1-pdf
locator: PDF 3 Overview 與 6 Rack Management Controller Northbound Interface；rack manager 管理 power／thermal／firmware，northbound 採 Redfish，列出 Power、Thermal、EventService、TaskService、TelemetryService 等 resources
limitation: 這是 2020 年 v1.0.0、引用舊 Redfish 1.6.0／2018.3 schema；可證明管理邊界與資源類型，不代表目前所有 OCP rack、DSX point types、跨廠 conformance 或 production deployment
independence_group: open-compute-project
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: Open Compute Project
title: OpenRMC-DM Sub-Project
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://www.opencompute.org/community/openrmc-dm
locator: 2026-08-07 的 project scope；northbound／southbound interface、rack-manager open-source implementation、asset query、fault isolation、preventive action 與 firmware management
limitation: 專案範圍與目標不是 conformance 結果；不證明 DSX 與 OpenRMC 已互通、任何設備已部署，或 fault isolation 在 field 中成功
independence_group: open-compute-project
-->

<!-- research_source
source_id: S6
role: standard
source_kind: living_index
publisher: DMTF
title: Redfish Standards Index
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://www.dmtf.org/standards/redfish
locator: 2026-08-07 的正式索引；Redfish Specification DSP0266 v1.24.0、Data Model 2026.1、Interop Profiles 1.10.0，發布日 2026-05-17
limitation: 索引只確認現行標準版本與文件集合；Redfish 的通用 resource／action／event 機制不自動包含 DSX 專屬 rack isolation point types，也不證明特定 profile 或產品 conformance
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-07
accepted_at: 2026-08-07
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-07 起追蹤 serverodm、powersupply、thermal 族群的法說、季報、重大訊息與產品／場域資料
limitation: 查詢入口本身不證明任何公司實作 DSX／OpenRMC／Redfish、承擔 action contract、完成場域驗收、取得訂單或形成財務貢獻
independence_group: twse-mops
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA DSX BMS Event Bus 1.0.0 將每個監測點拆成 Value 與 Metadata；Value 帶 value、毫秒 timestamp、quality，Metadata 提供 object／point type、單位、身分與關係，且 rackLocationId 必須在 IT 與 OT 上線前對齊
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-07
basis: S1／S2 可定位 Value／Metadata payload 與 rack identifier requirement，S3 的資料目錄另顯示 rackName／rackID coordination
boundary: 只證實 DSX 公開契約與欄位；不證明現場資料完整、timestamp 正確、quality 有效、兩邊 ID 已對齊或任何控制結果
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
claim: DSX 為 integration-owned values 定義獨立 publisher namespace；RackLiquidIsolationRequest 與 RackElectricalIsolationRequest 被列為 actionable、BMS 預期執行相應隔離，而 RackLeakDetectTray 被列為 informational only
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-07
basis: S1 的 integration publishing contract 與 S2 Point Types 直接區分兩種 isolation request 和 tray leak information 的動作責任
boundary: 「預期執行」是設計責任，不是場域證據；公開文件未證明 request 被接受、隔離完成時間、失敗原因、手動介入、復原或 service ticket
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
claim: DSX companion guide 把 BMS 定義為是否套用 integration request 的最終權威，建議先驗證安全 guardrails，並在 integration 失聯或數值越界時回到 safe default
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-08-07
basis: S2 Integration-Published Points 的 Guardrails 段落直接說明 request 與 BMS authority、範圍／變化率驗證及 safe default
boundary: 這是 implementation guidance，不指定每個 site 的限值、fail-safe topology、功能安全等級、測試結果或法律／合約責任
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: AI 機櫃 telemetry 只有在穩定身分、帶時間與品質的數值、可解讀 metadata、明確 request owner、BMS guardrail／safe default，以及可回查的 isolation state 被串成同一 action contract 時，才足以進入故障隔離與維修決策；資料點數本身不是閉環
supporting_source_ids: S1,S2,S4,S5,S6
contrary_source_ids:
as_of: 2026-08-07
basis: S1／S2 具體化 DSX identity、value／metadata、request、authority 與 status，S4／S5 獨立界定 rack manager 的 power／thermal／event／telemetry 與 fault-isolation 管理範圍，S6 固定現行 Redfish 標準邊界
boundary: 這是研究端的驗證階梯，不宣稱 DSX 是唯一設計、已跨平台互通、每個 action 都有完整 ack／service state，或更完整契約必然創造可辨識營收
verification_needed: 需 production sequence of operations、conformance profile、故障注入、request／accept／reject／isolate／recover 狀態、時間戳、field log 與維修工單驗證閉環
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: DSX、OpenRMC 與現行 Redfish 已能以共同 profile 跨供應商互通，且具名 production site 已公布 isolation request 的接受率、動作延遲、失敗／復原與維修結果
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-07
basis: 現有來源分別支持 DSX 平台契約、OpenRMC rack-manager scope 與 Redfish 標準索引，沒有共同 conformance report 或 production field outcome
boundary: 不把相容的管理概念、resource 名稱或開放標準目標改寫成已完成跨平台 interoperability 與可靠度驗證
verification_needed: 同一測試 profile 的多供應商 conformance，及具名 site 的故障注入、動作與復原紀錄
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 台灣 serverodm、powersupply 或 thermal 族群已有公司承擔可定位的 DSX／OpenRMC action-contract 實作與場域驗收，並形成可辨識訂單、收入、毛利或維護收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-07
basis: 平台與標準文件沒有 universe 公司、具名 site、合約責任、部署量與財務分母；MOPS 只作後續一手文件入口
boundary: 不由 ODM／電源／液冷的供應鏈鄰接、產品關鍵字、OCP 參與或營收成長推導 action-contract 曝險
verification_needed: 客戶與台灣公司雙向確認具名產品／軟體、責任範圍、conformance、commissioning、部署量、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## Action contract：從數值走到安全動作

| 契約層 | DSX 可定位證據 | 仍缺的 production 證據 |
|---|---|---|
| 物理身分 | `rackLocationId` 需在 BMS 與 IT 系統上線前協調，且建立後不應改變 | 資產異動、換櫃、重編號與錯配偵測／復原紀錄 |
| 值與品質 | Value payload 有 value、毫秒 timestamp、quality | 感測校正、遺失／延遲資料、時鐘同步與 quality code 的場域處置 |
| 語意與拓撲 | Metadata 提供 objectType、pointType、單位、身分及 serves／associate 關係 | 全 site mapping completeness、版本遷移與跨供應商語意一致性 |
| 請求與所有權 | Integration 依 metadata 的 owner 發布 request；BMS 是 metadata publisher | 權限配置、審計、request id、重送／去重與拒絕原因 |
| 安全裁決 | BMS 應套用上下限、變化率 guardrail，失聯或越界回 safe default | 每一場域的限值、fail-safe topology、測試涵蓋與責任簽核 |
| 動作與回報 | Liquid／electrical isolation request 與 isolation status 都有 point type | accept／reject／in-progress／complete／failed／recover 狀態機、延遲與 field outcome |
| 維修閉環 | DSX 可供 break-fix 系統訂閱；OpenRMC scope 包含 fault isolation／preventive action | 告警到工單、實體維修、復原驗證、誤報／漏報與維護成本 |

前五層讓資料具備被安全使用的條件，第六與第七層才回答「現場真的有沒有完成」。公開 DSX
文件已跨過單純 sensor list 的門檻，但仍沒有把每一個 request 的 acknowledgement、timeout、
失敗與 service outcome 封成可重現的 production evidence。因此本文升格的是**檢驗框架**，
不是 deployment 成功或供應商價值量。

## OpenRMC／Redfish 與 DSX 不是同一層

- **DSX** 提供 NVIDIA 平台內 BMS 與 IT integration 的 MQTT point／publisher contract，最具體到 rack isolation request 與 status。
- **OpenRMC** 定義 rack manager 的 northbound／southbound 管理範圍；v1.0.0 以 Redfish resources 描述 power、thermal、event、task、telemetry 與 update 等能力。
- **Redfish** 是較通用、持續演進的管理標準；現行正式索引已到 DSP0266 v1.24.0 與 2026.1 data model，但標準存在不代表某個產品支援 DSX 專屬 point types 或通過共同 profile。

三者可以互補，不能用名稱相近就寫成「已互通」。真正的交集要由 profile、schema mapping、
conformance result 與同一場域 sequence of operations 證明。

## 分析師如何使用這張圖

1. **先問事件會不會改變動作**：只有 sensor list 或 dashboard，不建立獨立商業主張。
2. **逐層找缺口**：identity、value quality、metadata、owner、guardrail、state feedback、service outcome 任一缺口都要保留。
3. **分開規格與場域**：platform schema、open standard、conformance、commissioning、field result 與財務認列是不同成熟度。
4. **最後才映射公司**：需要客戶與供應商雙向證據，並指出公司究竟負責 sensor、controller、BMS integration、rack integration、commissioning 或維護。

## 研究判定

- **可保留的結論**：DSX 已公開一份比 telemetry 欄位清單更完整的 action contract；身分、語意、publisher、兩種隔離 request、status 與 BMS guardrail 可逐項查核。
- **可信度為中而不是高**：DSX 是單一平台契約；OpenRMC／Redfish 支持通用管理邊界，但尚無共同 conformance 與 production field outcome。
- **不得發布的結論**：跨平台已互通、隔離一定成功、遙測點數／控制器價值量增加、台灣公司已供貨、訂單／收入／毛利或市場尚未反映。
- **升格條件**：同一具名 production site 公布 profile／mapping、故障注入、request 到 isolation／recovery 的時間與結果、維修閉環；台灣公司再以合約責任與財務分母交叉確認。

## 來源

- [NVIDIA：DSX BMS Event Bus 1.0.0](https://docs.nvidia.com/dsx-exchange/schema/bms-event-bus/overview)
- [NVIDIA：BMS Integration Companion Guide](https://docs.nvidia.com/dsx-exchange/bms-integration)
- [NVIDIA：Mission Control to BMS Data Catalog](https://docs.nvidia.com/datacenter/dsx/bms-datacatalog-interactive.html)
- [OCP：OpenRMC Design Specification v1.0.0](https://www.opencompute.org/documents/openrmc-design-specification-v1-0-1-pdf)
- [OCP：OpenRMC-DM project](https://www.opencompute.org/community/openrmc-dm)
- [DMTF：Redfish standards](https://www.dmtf.org/standards/redfish)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)

## 族群影響

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: ODM／rack integrator 位於 IT equipment、RMC、BMS mapping、commissioning 與 service handoff 的交界，適合作為責任查核路由
evidence_boundary: 沒有 universe 公司具名 DSX／OpenRMC implementation、場域驗收、部署量或財務分母，不建立受惠排行
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 電力 isolation request／status、power topology 與 safe default 需要電源控制和 BMS／IT 契約協同，形成相鄰搜尋路由
evidence_boundary: 資料契約不指定 800V／48V power topology、控制器、供應商、qualification、訂單或財務貢獻
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: Liquid isolation request、leak status、CDU／rack telemetry 與維修程序使散熱系統整合成為必要查核位置
evidence_boundary: 不由 DSX point types 推導冷板、CDU、閥、感測器或台灣供應商的 BOM、份額、部署與收入
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5
metric: DSX isolation contract 是否補齊 acknowledgement、timeout、reject／override、recover 與 service outcome，並公布具名場域結果
source_ids: S1,S2,S3
watch_source_ids: S1,S2,S3
frequency: monthly
next_check: 2026-08-31
trigger: 新版本或 production case 同時提供 request identity、guardrail decision、isolation status、動作時間、失敗／復原與維修結果
invalidation: DSX 移除可操作 isolation contract，或 field evidence 顯示 request／status 無法安全支援故障隔離且沒有替代契約
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C5
metric: OpenRMC／Redfish 是否發布可對齊 rack identity、telemetry、event、action 與 state feedback 的共同 profile、mapping 與多供應商 conformance
source_ids: S4
watch_source_ids: S5,S6
frequency: monthly
next_check: 2026-08-31
trigger: OCP／DMTF 公布正式 profile 或 test result，可把 DSX-like rack isolation sequence 跨至少兩個獨立 implementation 重現
invalidation: 最新 profile 明確排除這類 action／state 契約，或多供應商測試顯示語意無法對齊且沒有 mapping 層
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6
metric: 台灣 serverodm、powersupply、thermal 公司是否由客戶與自身申報雙向揭露具名 action-contract 責任、場域驗收、部署與財務分母
source_ids: S7
watch_source_ids: S7
frequency: quarterly
next_check: 2026-09-30
trigger: 客戶與台灣公司一手文件同時確認具名產品／軟體、contract scope、conformance／commissioning、部署量、收入及毛利
invalidation: 公司或客戶明示只供應一般硬體、不承擔控制契約或場域驗收，且相關收入無法辨識
-->

## 目前不能下的結論／待驗證

- 不能把 DSX 的平台 schema 稱為所有 AI data center 的共同標準，也不能把 Redfish resource 名稱當成 DSX point-level interoperability。
- 不能由 request／status 欄位存在推導隔離速度、成功率、可靠度或維修成本改善；這些都需要 production field denominator。
- 不能由族群位置、OCP 參與或產品關鍵字推導台灣公司訂單與獲利；公司映射在 C6 與三條 impact 中維持 unverified。
