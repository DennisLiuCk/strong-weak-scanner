# AI 機櫃如何從感測警報走到安全隔離：先找對設備，再決定動作

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
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave7_power_cooling_learning_no_conclusion_change
evidence: editorial:plain_language_wave7
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave84_sensor_to_isolation_no_conclusion_change
evidence: editorial:plain_language_wave84_sensor_to_isolation
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: backfilled_redfish_action_state_conformance_and_physical_verification_evidence
evidence: sources:S8,S9,S10,S11,S12
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_end_to_end_safe_state_deadline_budget_without_thesis_or_clock_refresh
evidence: sources:S1,S8,S11,S12,S13
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **感測資料**：溫度、流量、功率、漏液與設備狀態等讀數；看到數字不代表系統已知道是哪一座機櫃，也不代表可以立刻切電。
- **機櫃身分（rack ID）**：每一座實體機櫃在不同系統共用的固定編號。若監控畫面與設備控制系統使用不同編號，可能找錯甚至隔離錯設備。
- **IT 監控系統**：資訊設備端用來彙整資料、顯示告警及提出控制請求的系統；它不一定擁有最後的安全控制權。
- **設備控制系統（OT）**：直接管理建築、電力、冷卻與現場設備的控制系統；本文用這個白話名稱取代只寫 OT。
- **遙測（telemetry）**：設備持續送出的感測資料。它回答「目前量到什麼」，不會單獨回答「系統接下來該做什麼」。
- **時間戳記（timestamp）**：讀數產生的時間；沒有它，就難以分辨眼前數值是剛量到，還是延遲送達的舊資料。
- **資料品質（quality）**：標示讀數是否有效、可疑或不可用的欄位；系統不應把每一個數字都當成同樣可靠。
- **中繼資料（metadata）**：說明數值的意義、單位、設備身分與關係。相同的 `32.5` 可能代表溫度、百分比或功率，必須先知道上下文。
- **即時值封包（Value payload）**：DSX 傳送每筆讀數的格式，包含數值、時間戳記與資料品質；仍要搭配中繼資料才能知道它屬於哪個設備。
- **告警**：提醒人或系統注意異常的訊息；告警本身不等於已經要求切斷電力或冷卻。
- **請求（request）**：外部系統提出「希望執行某個動作」；接收端仍可依安全條件接受或拒絕。
- **命令**：經過權限與安全檢查後，真正交給設備執行的動作；它和告警、請求不是同一件事。
- **動作規則（action contract）**：把「誰提供資料、誰能提出請求、誰有權決定、如何回報結果」寫清楚的一套共同規則。
- **BMS／RMC**：BMS 是管理設施電力與冷卻的建築管理系統；RMC 是管理單座或一群機櫃的控制器。兩者範圍不同，不應混為同一個控制者。
- **安全限制（guardrail）**：控制系統執行動作前檢查的上下限、變化速度與其他保護條件，用來攔下危險或不合理的請求。
- **失聯安全預設（safe default）**：外部系統斷線或資料越界時，設備回到事先定義的安全狀態，而不是沿用最後一個未知是否仍安全的指令。
- **隔離**：把故障或有風險的電力、液冷或設備區段切開，避免問題擴大；隔離後仍要確認結果並規劃復原。
- **動作狀態**：告訴外部系統一項請求正在處理、已完成、失敗或已復原的回報。
- **確認回覆（acknowledgement）**：接收端明確表示已收到請求；收到不等於同意執行，更不等於動作完成。
- **逾時（timeout）**：超過預定時間仍未收到回覆或結果時的處理規則。
- **安全狀態期限（safe-state deadline）**：從指定事件起點算起，設備必須被獨立確認到達安全狀態的最晚時間；期限起點、終點與誰批准都要先寫清楚。
- **端到端時間預算（end-to-end time budget）**：把資料年齡、傳輸、裁決、排隊、致動與確認各自花掉的時間放進同一本帳，而不是只量 API 回應速度。
- **資料年齡（data age）**：系統開始判讀時，感測值距原始量測時間已經過多久；資料在網路與佇列裡等待的時間也會消耗安全期限。
- **致動時間（actuation time）**：控制命令交給實體 relay、breaker、valve、pump 或 cooling unit 後，到設備實際改變狀態所需的時間。
- **獨立確認時間（independent confirmation time）**：致動後用另一個狀態欄位或感測路徑確認目標物理狀態的時間；它不能只重讀命令回覆。
- **期限裕量（deadline margin）**：安全狀態期限減去端到端實際時間；正值代表尚有餘量，負值代表已逾時，但本文示例數字不是任何產品門檻。
- **請求關聯編號（correlation ID）**：把告警、請求、非同步任務、設備狀態與維修工單串成同一事件的穩定編號；本文沒有找到公開規格已替整條鏈固定共同欄位。
- **冪等（idempotency）**：同一請求因逾時而重送時，不會重複執行危險動作的特性。資源版本檢查可以擋舊資料覆寫，卻不自動保證每個 action 都能安全重送。
- **資源版本標籤（ETag）**：服務替一份資源狀態產生的版本標記；客戶端可用它說明「我是在這個版本上提出更新」。
- **條件式更新（If-Match）**：要求服務只在資源仍符合先前 ETag 時接受更新，避免舊畫面把較新的狀態蓋回去。
- **行動參數表（ActionInfo）**：Redfish 用來公開一項動作需要哪些參數與允許值的資源；參數格式正確不代表動作在現場情境下安全。
- **202 Accepted**：HTTP 表示服務已接受一項非同步工作；它不是「已完成」，也不是「實體設備已到位」。
- **非同步任務（asynchronous task）**：請求後不會立即完成的工作；服務先回覆一個可追蹤任務，客戶端之後再查狀態。
- **任務監看入口（Task Monitor）**：Redfish 讓客戶端查詢長時間工作進度與最後成功或失敗的網址；任務完成仍需另看設備實際狀態。
- **任務狀態（TaskState）**：Redfish Task 用來標示工作處於新建、執行中、完成、例外或被取消等階段的欄位；它仍是管理軟體所見狀態。
- **回查位置（Location）**：HTTP 回應告訴客戶端接下來到哪個網址查詢非同步工作；網址日後可能失效，不能拿它代替長期事件紀錄。
- **Retry-After**：HTTP 回應用來提示客戶端隔多久再查或再送請求的欄位；它不是工作完成時間，也不是安全狀態期限。
- **服務水準協議（SLA）**：供應方與使用方約定的可用率、延遲或處理期限；若沒有量測起點、終點、統計窗口與例外條件，就不能把一句「很快」當成可驗收的 SLA。
- **命令狀態（commanded state）**：控制系統認為自己已發出或完成的邏輯動作，例如要求關閉某個 outlet。
- **實際觀測狀態（observed physical state）**：由設備狀態與獨立感測確認電力、流量、泵浦或漏液狀態真的改變；它不能只沿用命令回覆。
- **互通 profile（interoperability profile）**：把必須支援的 Redfish 資源、欄位、訊息與 action 寫成機器可讀的最低要求，供採購與測試工具使用。
- **一致性檢查工具（validator）**：檢查通訊規則、資料格式或 profile 要求的工具；不同工具測的範圍不同，通過 API 檢查不等於通過故障注入或場域驗收。
- **通訊規則（protocol）**：規定 HTTP 方法、header、狀態碼與安全行為如何交換；protocol 正確不代表回傳內容或設備動作一定正確。
- **冷卻液分配單元（CDU）**：在設施水路與機櫃液冷迴路之間換熱、循環並監測流量與壓力的設備。
- **模式設定動作（SetMode）**：液冷設備模型用來要求冷卻單元或泵浦切換運轉模式的 action；動作回覆後仍要核對泵速、流量與設備狀態。
- **電力控制動作（PowerControl）**：Redfish 電力設備模型用來要求開、關或循環供電的 action 名稱；收到動作不等於實體回路已切換。
- **電力狀態（PowerState）**：電力設備模型回報目前供電狀態的唯讀欄位，應和轉換中狀態及獨立電氣讀值一起判讀。
- **漏液偵測狀態（DetectorState）**：液冷設備模型中漏液偵測器回報目前判定的欄位；仍要確認位置、設備健康與現場處置。
- **故障注入（fault injection）**：刻意製造感測失真、失聯、漏液或電力異常，確認系統能否依預期拒絕、隔離、回復並留下紀錄。
- **手動介入（override）**：現場人員在必要時暫停、拒絕或取代自動控制的機制，必須留下權限與稽核紀錄。
- **維修工單（service ticket）**：把告警、隔離結果、實體維修與復原確認串在一起的作業紀錄。
- **介面規格（schema）**：規定資料欄位、名稱與格式的文件；規格存在，不等於不同廠牌的產品已實際連線成功。
- **一致性驗證（conformance）**：用共同測試確認多個產品是否依同一套規格交換資料與執行動作。
- **量產場域（production site）**：真正承載日常營運的資料中心現場，不是實驗室示範或文件範例。
- **DSX**：NVIDIA 的 AI 基礎設施資料與控制規格；本篇引用其中的 BMS Event Bus，不代表所有資料中心都已部署。
- **OpenRMC**：OCP 的開放機櫃管理控制器專案，界定機櫃管理器的硬體、軟體與介面範圍。
- **Redfish**：DMTF 制定的通用設備管理介面標準；產品支援 Redfish，不等於已實作 DSX 的隔離流程。

### 三句話抓重點

- 機櫃收到溫度、功率或漏液資料後，不能立刻切電；系統要先確認資料屬於哪一座機櫃、何時量到，以及讀數是否可靠。
- 外部監控系統可以提出隔離請求，但建築管理系統仍要檢查安全限制，才決定是否執行；告警、請求與真正命令是三件不同的事。
- DSX 已把設備身分、感測資料、隔離請求與狀態寫進契約；Redfish 又把「接受非同步工作」與「工作完成」分開，但兩者都不能單獨證明設備真的隔離、服務已恢復或台灣供應商已有收入。

### 為什麼重要

**先找對設備。** 同一座機櫃必須在監控系統與設備控制系統使用一致編號，否則畫面上的警報
可能對不到現場設備，最嚴重時甚至會隔離錯機櫃。

**再確認資料可用。** 一筆讀數要帶時間、品質與設備關係，接收端才能知道它是不是最新資料、
是否可信，以及代表哪一個位置的溫度、功率或漏液狀態。

**最後才執行動作。** 系統還要分清楚誰能提出請求、誰負責安全判斷，以及隔離後如何回報完成、
失敗與復原。少了任何一段，監控畫面可以很完整，卻不一定能安全處理故障。

**接受不等於完成。** API 回覆 `202 Accepted` 時，只代表服務願意處理長時間工作；還要沿任務
監看入口查到成功或失敗，才能知道控制軟體走到哪一步。

**完成不等於恢復。** 邏輯命令顯示完成後，仍要用電力、流量、泵速、漏液與設備狀態確認物理
結果，再完成回復測試與維修簽核。這幾層若共用同一個「成功」字樣，最容易把半條鏈誤當閉環。

### 接下來怎麼追

- 先追一個隔離請求的共同關聯編號：是否收到、接受或拒絕，建立哪個 Task、多久完成，以及重送時有沒有重複動作。
- 再核對命令狀態與實際觀測狀態：電力是否真的斷開、泵浦或冷卻單元是否到達目標模式、獨立感測是否支持同一結果。
- 查看 OpenRMC／Redfish 是否有具名 profile 與版本化測試報告，並分清 protocol、schema 與 interoperability validator 各自測了什麼。
- 最後找具名量產場域的故障注入、跨電力／液冷 sequence、復原與維修紀錄，再由客戶和台灣公司一手申報交叉確認責任、部署量與財務貢獻。

### 想一想

- 溫度與漏液警報都出現時，若監控畫面和設備控制系統使用不同的機櫃編號，系統要怎麼確定該隔離哪一座？
- 告警只是提醒、請求可以被拒絕、命令才會驅動設備；誰負責攔下危險請求，失聯時又由誰讓設備回到安全狀態？
- 一項非同步任務顯示完成後，要再看哪些獨立讀值，才能證明電力或冷卻設備真的到達安全狀態？
- 一份公開介面規格，能不能直接證明不同廠牌已互通，或台灣機櫃供應商已因此取得收入？

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

<!-- research_source
source_id: S8
role: standard
source_kind: document
publisher: DMTF
title: Redfish Specification 1.24.0
published_at: 2026-04-02
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.24.0.html
locator: sections 6.5 ETags、9.9.6 Action info annotation、12.1 Eventing 與 12.2 Asynchronous operations
limitation: 規格定義 HTTP、action、Task Monitor、事件與版本前置條件；不指定 DSX 專屬隔離語意、場域 guardrail、物理動作、跨供應商產品通過或 production outcome
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: DMTF
title: Redfish Interoperability Profiles 1.10.0
published_at: 2026-04-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP0272_1.10.0.html
locator: sections 1–2 profile purpose、8.3 protocol requirements、8.4 resource／property／action requirements
limitation: Profile 可固定最低 API 能力並供工具驗證，但不替產品證明電力或液冷的安全 sequence、故障注入、物理狀態、場域驗收或維修結果
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: DMTF
title: Redfish Conformance and Test Tools White Paper 1.0.0
published_at: 2024-01-25
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP2068_1.0.0_0.pdf
locator: pp.5–15；Protocol Validator、Service Validator 與 Interop Validator 的不同測試範圍
limitation: 這是工具用途與執行方式說明；validator pass 不等於多供應商互通、實體 relay／pump／valve 動作、故障注入、production reliability 或功能安全簽核
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S11
role: standard
source_kind: document
publisher: DMTF
title: Redfish for Power Distribution Equipment 1.1.0
published_at: 2025-02-05
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP2056_1.1.0.pdf
locator: pp.30–38 Circuit；pp.50–56 Outlet；PowerControlLocked、delay、PowerRestorePolicy、PowerStateInTransition、PowerState 與 PowerControl action
limitation: 白皮書界定資料模型與動作欄位，不證明任何 PDU／busway／outlet 已實作、跨廠 profile 通過、切電時間達標，或與冷卻隔離完成安全協同
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: DMTF
title: Redfish for Liquid Cooling Equipment 1.1.0
published_at: 2025-02-05
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.dmtf.org/sites/default/files/standards/documents/DSP2064_1.1.0.pdf
locator: pp.36–39 CoolingUnit 與 SetMode；pp.58–64 LeakDetection／LeakDetector；pp.70–72 Pump 與 SetMode
limitation: 白皮書界定 cooling resource、leak state 與 enable／disable action；沒有規定 DSX request mapping、跨電力協同、場域 guardrail、故障注入、復原或維修閉環
independence_group: dmtf-redfish
-->

<!-- research_source
source_id: S13
role: standard
source_kind: document
publisher: Internet Engineering Task Force
title: RFC 9110 HTTP Semantics
published_at: 2022-06-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.rfc-editor.org/rfc/rfc9110.html
locator: §§10.2.3、15.3.3；202 Accepted 只表示請求已接受但處理尚未完成、日後可能執行也可能不執行，HTTP 不會由非同步操作重新送一次狀態碼；response 應描述目前狀態並指向 status monitor；Retry-After 表示後續請求前建議等待時間。RFC header 只標 June 2022，帳本日期以 2022-06-01 正規化且不主張日精度
limitation: RFC 9110 是通用 HTTP 語意，不定義 Redfish Task、DSX isolation、rack safe-state deadline、實體致動、獨立感測、功能安全或場域驗收；它只界定 202 與 follow-up timing 的協定邊界，不證明任何設備、平台、客戶或 production outcome
independence_group: ietf-http
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
supporting_source_ids: S1,S2,S4,S5,S6,S8,S9,S10,S11,S12
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

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Redfish 1.24.0 對長時間動作把 HTTP 202 Accepted、Location 指向的 Task Monitor、持續中的 TaskState 與最終成功或失敗分開；收到 202 只表示服務接受非同步處理，不表示設備動作已完成
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 section 12.2 逐一規定 202 response、Location／Retry-After、Task Monitor 查詢、TaskState 與完成或失敗回應
boundary: 只證實 Redfish API 的非同步狀態模型；不證明 DSX isolation request 採用同一 Task、實體接觸器或泵浦已動作、感測結果正確或服務已恢復
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Redfish 1.24.0 允許客戶端以 ETag 與 If-Match／If-None-Match 帶入先前讀到的資源版本，服務可用 412 或 428 擋下版本衝突或缺少前置條件的更新
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 section 6.5 說明 ETag、conditional update、412 Precondition Failed 與 428 Precondition Required
boundary: ETag 只處理資源版本碰撞；不自動提供 request correlation、重送去重、跨電力與冷卻仲裁、場域安全限值或實體結果驗證
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: Redfish 的 ActionInfo 可公開一項 action 的參數需求與允許值，但參數可被機器讀取不等於該 action 在特定機櫃、負載與故障情境下安全
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-12
basis: S8 section 9.9.6 直接把 ActionInfo 定義為 action parameter requirements 與 allowable values 的資源
boundary: ActionInfo 不提供 DSX request owner、BMS guardrail、設備互鎖、fault injection、物理確認、維修責任或公司財務證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: Redfish interoperability profile 可把 schema、property、registry 與 action 的最低要求寫成機器可讀文件；DMTF 又把 protocol、schema payload 與 profile conformance 分成三類 validator
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S9 sections 1–2 與 8.4 定義 profile 內容及可供 conformance tool 使用，S10 pp.6–15 分列 Protocol、Service 與 Interop Validator 的測試範圍
boundary: 三類 validator 只證明各自測到的 API 契約；不等於多供應商完整互通、實體動作、跨域安全 sequence、production reliability 或場域驗收
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: DMTF 電力設備模型把控制鎖定、開關延遲、復電政策、轉換中狀態、最終電力狀態與 PowerControl action 分成不同欄位或動作
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-12
basis: S11 的 Circuit／Outlet 章節直接列出 PowerControlLocked、PowerOff／On／Cycle Delay、PowerRestorePolicy、PowerStateInTransition、PowerState 與 PowerControl
boundary: 資料模型不證明實體 breaker／contactor 動作、切換時間、故障電流清除、跨廠實作、DSX mapping 或 field outcome
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: DMTF 液冷設備模型把冷卻單元與泵浦的 SetMode、設備狀態、泵速，以及 leak detector 的位置與 DetectorState 分成不同資源與欄位
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的 CoolingUnit、Pump、LeakDetection 與 LeakDetector 章節直接列出 SetMode、Status、PumpSpeedPercent、Location／PhysicalContext 與 DetectorState
boundary: 資源與欄位存在不證明漏液後的閥件／泵浦／電力 sequence、安全時序、故障注入、復原、維修或具名場域結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 機櫃控制閉環至少要分開五個結果：請求被收到、API 接受並建立任務、邏輯命令完成、設備被觀測到達目標物理狀態，以及服務在復原與維修後恢復；任一前段成功都不能代替後段
supporting_source_ids: S1,S2,S8,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S1／S2 分開 request、BMS authority 與 isolation status，S8 分開 202／Task Monitor／TaskState，S11／S12 又分開 action、transition／mode 與 read-only equipment state，因而可建立五層結果階梯
boundary: 這是跨文件的研究框架，不主張所有平台使用相同五個欄位、同一傳輸協定或相同故障處置；沒有 production log 前不報成功率、延遲或可靠度
verification_needed: 同一事件的 request ID、Task／command、設備狀態、獨立感測、復原驗證與 service ticket 時序紀錄
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: unverified
status: active
claim: 現有公開資料尚未提供一份共同 production record，可把 DSX request、Redfish Task Monitor、電力與液冷設備狀態、獨立物理感測、故障注入、跨域仲裁、復原驗證與維修工單串成同一事件
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S1–S3 是 DSX 平台契約，S8–S10 是通用 API／profile／validator，S11／S12 是各自設備模型；來源沒有共同 site、事件 ID、完整時序與 outcome
boundary: 缺少公開共同紀錄不是 DSX、Redfish、PDU 或 CDU 無法實作的反證，也不表示私有場域沒有完成；只限制本文不能宣稱閉環已證實
verification_needed: 具名多供應商場域的 fault-injection report 與去識別化事件紀錄，逐欄對齊 request、Task、commanded／observed state、跨域 sequence、rollback、repair 及 sign-off
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 驗收 action contract 時應把 schema 支援、profile 要求、protocol／service／interop validator、跨供應商互通、故障注入、場域 commissioning 與 production outcome 分成七級；API validator 通過不能替最後四級背書
supporting_source_ids: S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S9 定義可測的最低 profile，S10 明列三種 validator 的 API 測試邊界，S11／S12 顯示電力與液冷仍有不同物理資源、action 與 state，因而需要額外互通、故障與場域驗證
boundary: 七級是研究與採購查核順序，不是 DMTF 認證等級、產品排名、功能安全標準或已公布的單一 certification program
verification_needed: 同一設備組合逐級保存 profile、工具版本、pass／fail、互通矩陣、fault case、commissioning 與 production incident outcome
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: IETF RFC 9110 將 202 Accepted 定義為請求已被接受處理但尚未完成，後續可能被執行也可能在真正處理時被拒絕，且 HTTP 沒有由非同步操作再次送出狀態碼的機制；回應應描述目前狀態並指向 status monitor。DMTF Redfish 1.24.0 另用 Location、Retry-After、Task Monitor 與 TaskState 補上輪詢路徑，但這些欄位仍只到管理服務狀態
supporting_source_ids: S8,S13
contrary_source_ids:
as_of: 2026-08-14
basis: S13 §15.3.3 直接說明 202 的 intentionally noncommittal 邊界與 status monitor，§10.2.3 定義 Retry-After；S8 §12.2 直接規定 Redfish 202 response、Location／Retry-After、Task Monitor 與 TaskState
boundary: 只證實 HTTP 與 Redfish 的非同步狀態語意，不證明 DSX isolation 採同一 Task、Retry-After 是完成承諾、設備已動作、物理狀態已確認、safe-state deadline 已達成或服務已復原；S8 與 S13 是兩條標準鏈，不是兩個產品或場域樣本
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: AI 機櫃隔離的時間驗收應把資料年齡、身分／關聯對齊、guardrail 裁決、API 接受與排隊、實體致動、獨立物理確認及 safe-default／復原分開，並以安全狀態期限減去各段總和得到 deadline margin；本文固定 8.0 秒教材中，A 在 2.7 秒收到 202、7.2 秒完成獨立確認而餘 0.8 秒，B 同樣在 2.7 秒收到 202、卻因致動較慢到 8.5 秒才確認而逾時 0.5 秒，因此 API acceptance latency 不能替代 end-to-end safe-state time
supporting_source_ids: S1,S8,S11,S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: S1 分開 timestamp／quality、request 與 isolation status，S8／S13 分開 202 與非同步結果，S11／S12 分開 action、transition、設備 state 與感測欄位；把六段時間放進同一期限帳與兩個固定案例，是研究中心依這些責任邊界建立的可重算教材
boundary: 8.0 秒期限、1.2／0.3／0.8／0.4／3.5或4.8／1.0 秒各段、A／B、90.0%／106.25%預算使用率與 pass／fail 都是假想，不是 DSX、Redfish、電力、液冷、功能安全或 AI rack 的規定與實測；N=2 是固定案例數，沒有 sampling SE／t、故障率、SLA、部署或財務效果
verification_needed: 具名場域以共同時鐘公開同一事件的原始 sensor timestamp、ingest／correlation、guardrail decision、202／Task、commanded state、observed physical state、independent confirmation、deadline owner、timeout／safe default、recovery 與 service sign-off
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 從警報到復原：七個步驟不能少

| 控制步驟 | 這一步要回答什麼 | 公開文件目前支持什麼 | 還缺哪些現場證據 |
|---|---|---|---|
| 1. 找到正確設備 | 警報究竟來自哪一座實體機櫃？ | DSX 要求建築管理與 IT 系統上線前先對齊 `rackLocationId`，建立後不應任意更改 | 換櫃、重編號時如何更新，以及系統如何發現並修正編號錯配 |
| 2. 確認讀數可用 | 這筆數值是何時量到，現在還可信嗎？ | 即時值封包包含數值、毫秒時間戳記與資料品質 | 感測器校正、資料延遲或遺失、時鐘不同步及可疑讀數的現場處理 |
| 3. 看懂資料含義 | 數字代表什麼單位、設備與上下游關係？ | 中繼資料描述資料類型、單位、身分及設備關係 | 整座資料中心的對照表是否完整、版本更新後是否一致，以及不同廠牌能否使用同一含義 |
| 4. 分清誰能請求、誰能決定 | 外部系統能直接控制設備，還是只能提出請求？ | 外部整合系統可發布自己負責的請求，建築管理系統保有最後決定權 | 權限與稽核紀錄、請求編號、重送或重複請求處理，以及拒絕原因 |
| 5. 套用安全限制 | 哪些請求必須被攔下，失聯時要回到哪個狀態？ | 建築管理系統應檢查上下限與變化速度，失聯或越界時回到安全預設 | 每個場域實際採用的限值、故障時的安全路徑、測試範圍與責任簽核 |
| 6. 回報動作結果 | 隔離正在處理、完成、失敗，還是已經復原？ | DSX 為液冷與電力隔離定義請求與狀態欄位 | 接受、拒絕、處理中、完成、失敗與復原的完整流程、所需時間及現場結果 |
| 7. 完成維修閉環 | 隔離後是否派修、修復並確認恢復正常？ | DSX 資料可供故障維修系統訂閱，OpenRMC 的範圍也包含故障隔離與預防動作 | 從告警到工單、實體維修、復原驗證、誤報漏報及維護成本的完整紀錄 |

前五步決定資料能不能安全地驅動控制，第六與第七步才回答「現場真的有沒有完成」。公開 DSX
文件已不只是列出感測器，但仍未公開每一個請求是否收到、何時逾時、為何失敗，以及維修後是否
恢復正常。因此本文建立的是**檢驗流程**，不是在宣稱部署成功或供應商價值已經增加。

## 同一個「成功」其實有五層：API 接受後還有四次核對

控制系統最危險的語意捷徑，是把每一層都顯示成綠色的「成功」。Redfish 1.24.0 明確把長時間
工作拆成 `202 Accepted`、Task Monitor、持續中的 TaskState 與最後成功或失敗。DMTF 電力與液冷
模型又另外保留設備狀態與感測欄位。把兩類文件接起來，可得到下面五層；它是查核框架，不是新的
共同標準。

| 結果層 | 至少要留下什麼 | 這一層能證明什麼 | 還不能代替什麼 |
|---|---|---|---|
| 1. 請求已收到 | 關聯編號、目標設備、請求者、時間、動作與參數 | 控制系統知道要處理哪一件事 | 安全判斷、接受、執行或設備結果 |
| 2. API 已接受 | HTTP 回應、Task Monitor、Task ID 與重查時間 | 服務已建立或接受非同步工作 | 任務成功、命令下達或實體設備已動 |
| 3. 邏輯任務已完成 | TaskState、完成時間、錯誤訊息與命令結果 | 管理服務認為工作已成功或失敗 | relay／breaker／pump／cooling unit 真的到位 |
| 4. 物理狀態已確認 | 電力狀態、轉換中旗標、流量、泵速、漏液、壓力或獨立感測 | 設備與環境讀值支持目標狀態 | 工作負載可恢復、根因修復或維修已簽收 |
| 5. 服務已復原 | 復原測試、維修工單、變更紀錄、人工簽核與重開條件 | 故障處理走完營運閉環 | 長期可靠度、所有場域都可重現或供應商財務受惠 |

Task Monitor 可能在工作結束後被刪除，Redfish 允許較晚查詢回覆 `404 Not Found` 或 `410 Gone`。
所以場域若要稽核，不能只保存一個之後會失效的網址；仍要把 Task、設備讀值、事件訊息與工單按同一
關聯編號封存。公開資料尚未證明 DSX 已提供這份跨系統共同紀錄。

## 202 Accepted 很快，為什麼安全隔離仍可能逾時

前一節回答「五層成功各代表什麼」，這一節改問「每一層何時發生」。兩者不能互相替代：狀態語意
完整，仍可能超過安全期限；API 很快，仍可能卡在排隊、致動或物理確認。真正要量的是從指定事件
起點到**獨立確認安全狀態**的端到端時間，而不是只看 HTTP round trip。

RFC 9110 對 `202 Accepted` 的邊界比「排隊成功」更窄：處理尚未完成，之後可能執行，也可能在
真正處理時被拒絕；HTTP 不會由非同步操作再主動送一次新的狀態碼，回應因此應指向 status monitor。
[S13] Redfish 再用 `Location`、`Retry-After`、Task Monitor 與 TaskState 讓客戶端輪詢。[S8]
但 `Retry-After` 只告訴客戶端何時再查，並不是設備將在該時點前完成的承諾；Task completed 也還要
接到電力或液冷的 observed state。[S11][S12]

### 同樣在 2.7 秒收到 202，兩個結局卻不同

以下是純教材，不是 AI 機櫃、DSX、Redfish、電力或液冷規格。假設某一事件從原始感測 timestamp
算起，必須在 `D_safe=8.0 秒` 內完成獨立物理確認；A、B 共用相同資料年齡、關聯、裁決、API
接受與確認時間，只讓實體致動時間由 `3.5 秒` 變成 `4.8 秒`。所有系統時鐘在本例假設已對齊，
沒有另加 clock uncertainty；真實驗收必須把同步方法與不確定度寫回帳本。

| 時間段 | 本例花費 | A 累計 | B 累計 | 這一段回答什麼 |
|---|---:|---:|---:|---|
| 1. 資料年齡 | 1.2 秒 | 1.2 秒 | 1.2 秒 | 系統開始處理前，感測值已經多舊 |
| 2. 身分／關聯與傳輸 | 0.3 秒 | 1.5 秒 | 1.5 秒 | 找到正確機櫃並把事件接到同一 request |
| 3. Guardrail 裁決 | 0.8 秒 | 2.3 秒 | 2.3 秒 | 權限、限值、互鎖與 safe-default policy 是否允許動作 |
| 4. API 接受／Task 建立 | 0.4 秒 | 2.7 秒 | 2.7 秒 | 服務回覆 `202` 並提供可追蹤工作 |
| 5. 實體致動 | A 3.5 秒／B 4.8 秒 | 6.2 秒 | 7.5 秒 | relay、breaker、valve、pump 或 cooling unit 是否真的改變 |
| 6. 獨立物理確認 | 1.0 秒 | 7.2 秒 | 8.5 秒 | 另一狀態或感測路徑是否支持已到安全狀態 |

本例公式把 `T_safe` 定義為 data age、correlation、decision、task acceptance、actuation 與
independent confirmation 的總和；`deadline margin = D_safe − T_safe`。兩案都在累計 `2.7 秒`
收到 `202`，此時已用掉
`33.75%` 的 8 秒預算、還剩 `5.3 秒`。A 在 `7.2 秒` 完成確認，使用 `90.0%` 預算並留下
`+0.8 秒` 裕量；B 在 `8.5 秒` 才完成，使用 `106.25%` 預算並以 `−0.5 秒` 逾時。相同的 API
acceptance latency，不能替兩案得到相同的 safe-state 結論。

Python `Fraction` 精確有理數與獨立 `awk` 浮點路徑均得到：acceptance 累計 2.70、剩餘 5.30、
A 的 7.20／+0.80／90.00%／pass，以及 B 的 8.50／−0.50／106.25%／fail。這是 `N=2` 個固定
假想案例的確定性加總，不是抽樣、故障注入、設備測試或 production log，沒有 sampling SE／t、
分位數、SLA、失效率、部署、收入或公司效果。

**逾時後要做什麼也是契約的一部分。** B 的 `−0.5 秒` 不能只在 dashboard 變紅；場域必須事前
指定是否拒絕後續請求、改走本地保護、切到另一致動路徑、人工介入或保留控制電力。本文沒有取得
這類具名場域規則，因此示例只判定 deadline miss，不替任何平台選 safe default。

### 多空小作文要共用八欄安全狀態期限護照

| 八欄期限護照 | 至少保存什麼 | 缺少時最容易被誤讀成 |
|---|---|---|
| 1. 事件與受控版本 | rack／PDU／CDU／BMC、韌體、設定、負載與 correlation ID | 同系列設備都具有相同時序 |
| 2. 期限定義與責任人 | hazard、起點、終點、`D_safe`、批准者與適用模式 | 任意 timeout 都等於安全期限 |
| 3. 時鐘與量測邊界 | timestamp 來源、同步方法、clock uncertainty、解析度與缺值 | 不同系統時間可直接相減 |
| 4. 資料年齡與關聯 | measurement time、ingest、quality、身分 mapping、傳輸與 queue | API 收到時資料仍是即時狀態 |
| 5. 裁決時間 | guardrail／權限／互鎖 policy 版本、輸入、accept／reject 與耗時 | 快速決策一定是正確決策 |
| 6. API 與 Task 時間 | request、`202`、Location、Retry-After、TaskState、錯誤與重查節奏 | `202` 或短 round trip 等於動作快 |
| 7. 致動與獨立確認 | commanded state、設備 transition、observed state、獨立感測與每段 timeout | Task completed 等於物理安全狀態 |
| 8. 裕量、失敗與復原 | margin、deadline miss、safe default、rollback、人工介入、recovery、service sign-off | 一次 pass 就代表長期可靠與可量產 |

偏多小作文會說，端到端時間預算讓控制系統在故障擴大前自動隔離，降低人工確認與影響範圍；偏空
小作文則會說，跨 IT／OT 關聯、非同步 Task、輪詢與多個致動器讓延遲和故障面增加，過短期限還可能
造成誤隔離。兩邊都必須交同一張八欄護照、完整事件分母、各段原始 timestamp、pass／miss／reject／
override／rollback 結果、連續運行區段與統計不確定度。只有平均 API latency 或一個成功 demo，既
不能證明偏多的可靠自動化，也不能證明偏空的架構失效，更不能直接推導台灣公司的訂單與損益。

## 四種錯誤要用四種機制：版本、重送、仲裁與結果不能混用

ETag 與 `If-Match` 處理的是「我看到的資源版本是否仍是最新版」。ActionInfo 處理的是「這項 action
允許哪些參數」。兩者都很重要，但都不是危險動作的完整保護。研究或驗收時至少要把四種故障分開：

| 風險 | 典型情境 | 需要的契約 | 現有公開證據邊界 |
|---|---|---|---|
| 舊狀態覆寫 | 操作員在舊畫面改值，另一個控制器已先更新 | ETag、條件式更新與衝突回覆 | Redfish 已定義；未證明 DSX 每個隔離 action 都採用 |
| 逾時重送 | 回覆遺失後重送切電或停泵請求 | 關聯編號、去重範圍、冪等規則與重送窗口 | 本輪沒有找到整條 action 的共同公開欄位 |
| 跨域衝突 | 液冷要求隔離，電力系統同時要保留泵浦或控制器供電 | 優先序、互鎖、最終裁決者、手動介入與 safe state | DSX 說 BMS 有最後權威，但未公開跨域 sequence |
| 結果遺失或誤判 | Task 顯示完成，實體設備沒有到位或讀值延遲 | Task 狀態、commanded state、independent observed state 與逾時升級 | DMTF 分開 action 與設備狀態；沒有具名場域共同紀錄 |

因此「支援 Redfish action」不能直接改寫成「動作可安全自動化」。要先知道它解決的是哪一種錯誤，
再檢查其他三種是否有明確 owner、時間與失效處置。

## 從介面支援到量產閉環：七級驗收不能跳級

DMTF 已把三種 validator 分開：Protocol Validator 看 HTTP 與安全等通訊規則；Service Validator
看回應是否符合 schema；Interop Validator 再按指定 profile 檢查最低能力。三者都很實用，但它們
仍在 API 與資料模型層。要證明隔離閉環，還要往物理世界走四步。

| 驗收級別 | 核心問題 | 最低產物 | 不能因此宣稱 |
|---|---|---|---|
| 1. Schema 支援 | 有沒有對應資源、欄位與 action？ | 版本化 schema 與實作清單 | 採購需要的欄位都存在 |
| 2. Profile 要求 | 哪些能力對這類設備是必須？ | 具名 profile、版本與適用設備 | 產品真的符合 profile |
| 3. Protocol Validator | HTTP、狀態碼、header 與安全行為是否合規？ | 工具版本、測試目標與完整報告 | payload 與設備語意正確 |
| 4. Service Validator | 回應欄位、型別、URI 與 schema 是否相符？ | pass／fail／skip 明細 | 採購 profile 或跨廠行為一致 |
| 5. Interop Validator | 產品是否符合指定最低 profile？ | profile、工具版本與逐項結果 | 多供應商在同一 action sequence 已互通 |
| 6. 互通與故障注入 | 兩個以上實作在失聯、重送、拒絕與設備故障時能否一致處理？ | 互通矩陣、fault case、時間線、rollback 與 physical state | 量產場域的故障率與維護成本 |
| 7. 場域與營運結果 | 真實負載下是否正確隔離、復原並完成維修？ | commissioning、incident log、工單、SLA 與變更後重驗 | 所有客戶可複製、台灣公司已有收入或獲利 |

如果新聞只說「支援 Redfish」，它只回答第一級的一部分；即使附上 validator pass，也要看是哪一種
工具、用哪份 profile、測到哪些設備與情境。七級順序只安排證據，不代表產品優劣或公司受惠。

## 同樣叫隔離，電力與液冷是兩套物理動作

DMTF 的電力白皮書把 `PowerControlLocked`、開關延遲、復電政策、轉換中狀態與最終 PowerState
分開；液冷白皮書則把 CoolingUnit／Pump 的 SetMode、泵速、漏液位置與 DetectorState 分開。這說明
同一句「隔離機櫃」至少跨兩套設備模型，不能只發一個共通命令就假設完成。

| 物理域 | 公開模型目前能描述什麼 | 動作後應另看什麼 | 仍缺的跨域問題 |
|---|---|---|---|
| 電力 | outlet／circuit 的控制鎖定、延遲、PowerControl、轉換中與最終電力狀態 | 目標回路、電壓電流、PowerState、轉換時間及復電政策 | 哪些控制器、泵浦或安全設備必須保留供電 |
| 液冷 | cooling unit／pump 的 enable／disable、泵速、漏液位置與 detector state | 流量、壓力、溫度、泵速、漏液與設備健康 | 先關閥、停泵、降載還是切電，以及每一步的逾時 |
| 跨域接力 | DSX 可提出液冷或電力隔離 request，BMS 保有最後裁決 | 同一關聯編號下的兩域 commanded／observed state | 互鎖、優先序、失敗回退、人工介入與安全簽核 |
| 復原 | 各域都有可讀狀態與可設定模式 | 故障排除、重新加壓／上電、負載驗證與維修工單 | 誰批准重開、哪些測試必須重跑及責任如何交接 |

這些文件支持的是「可以把責任拆細」，不是「某套跨域 sequence 已被證實」。真正的升級證據要在
同一具名場域公開事件時序、設備版本、故障注入、物理結果與簽核，而且不能只由供應商示範代替客戶
驗收。

## 三套規格各管一層：DSX、OpenRMC 與 Redfish

- **DSX 管平台內的資料與動作規則**：它具體說明建築管理系統與 IT 監控系統如何交換資料，並定義液冷與電力隔離的請求和狀態。
- **OpenRMC 管機櫃管理器的範圍**：它描述管理器如何連接上游與下游設備，以及如何處理電力、散熱、事件、任務、遙測與更新。
- **Redfish 提供通用設備管理介面**：它持續更新設備資源、動作、事件與非同步任務模型；profile 可固定最低要求，三類 validator 可分開測 protocol、schema 與 profile，但產品支援 Redfish 仍不代表已支援 DSX 專用隔離欄位或通過場域故障測試。

三者可以互補，名稱或功能相近卻不能直接寫成「已互通」。仍要看到欄位對照、共同測試結果，
以及同一場域從警報到隔離與復原的實際操作紀錄。尤其要把 API 的 Task 完成與設備的物理狀態分開，
再把電力與液冷各自的 action 接成有優先序、逾時、回退與人工介入的跨域 sequence。

## 怎麼用這張表判讀公司新聞

1. **先問新功能會不會改變動作**：如果只有更多感測器或更漂亮的監控畫面，還不能單獨建立商業價值主張。
2. **沿七個步驟找缺口**：設備身分、資料可信度、含義、控制權、安全限制、結果回報與維修紀錄，任何一項缺失都要保留疑問。
3. **再拆五層結果**：請求收到、API 接受、Task 完成、物理狀態確認與服務復原不能共用一個「成功」標籤。
4. **分開文件與現場成熟度**：schema、profile、三類 validator、跨廠互通、故障注入、場域驗收、實際結果與財務認列都要逐級留下證據。
5. **最後才連到公司**：要由客戶與供應商雙向證明，並說清楚公司負責感測器、控制器、系統整合、整櫃驗收，還是後續維護。

## 這篇目前能說到哪裡

- **已知道的事**：DSX 已公開設備身分、資料含義、發布責任、液冷與電力隔離請求、結果狀態及安全限制；Redfish 另提供非同步 Task、版本前置條件、action 參數、profile 與分層 validator，電力／液冷模型也能把命令與設備狀態拆開。
- **為何可信度是中等**：NVIDIA 與 OCP／DMTF 是獨立文件鏈，能共同界定資料與 API 責任；但仍沒有同一個 profile、跨廠實作、故障注入與量產場域結果把五層狀態接完。
- **還不能說的事**：不能說 API 接受等於物理隔離、跨平台已互通、電力與液冷 sequence 已安全、設備價值量增加、台灣公司已供貨，或訂單、收入、毛利已可辨識。
- **何時可以升級判定**：同一具名量產場域要公開 profile 與工具版本、欄位對照、故障注入、request／Task／commanded／observed state、跨域 sequence、復原與維修時間線；台灣公司還要以合約責任與財務分母交叉確認。

## 來源

- [NVIDIA：DSX BMS Event Bus 1.0.0](https://docs.nvidia.com/dsx-exchange/schema/bms-event-bus/overview)
- [NVIDIA：BMS Integration Companion Guide](https://docs.nvidia.com/dsx-exchange/bms-integration)
- [NVIDIA：Mission Control to BMS Data Catalog](https://docs.nvidia.com/datacenter/dsx/bms-datacatalog-interactive.html)
- [OCP：OpenRMC Design Specification v1.0.0](https://www.opencompute.org/documents/openrmc-design-specification-v1-0-1-pdf)
- [OCP：OpenRMC-DM project](https://www.opencompute.org/community/openrmc-dm)
- [DMTF：Redfish standards](https://www.dmtf.org/standards/redfish)
- [DMTF：Redfish Specification 1.24.0](https://www.dmtf.org/sites/default/files/standards/documents/DSP0266_1.24.0.html)
- [DMTF：Redfish Interoperability Profiles 1.10.0](https://www.dmtf.org/sites/default/files/standards/documents/DSP0272_1.10.0.html)
- [DMTF：Redfish Conformance and Test Tools](https://www.dmtf.org/sites/default/files/standards/documents/DSP2068_1.0.0_0.pdf)
- [DMTF：Redfish for Power Distribution Equipment](https://www.dmtf.org/sites/default/files/standards/documents/DSP2056_1.1.0.pdf)
- [DMTF：Redfish for Liquid Cooling Equipment](https://www.dmtf.org/sites/default/files/standards/documents/DSP2064_1.1.0.pdf)
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

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C7,C8,C9,C10,C11,C12,C13,C14,C15
metric: 同一 incident 的 request correlation、resource version、action parameters、Task state、commanded／observed power／cooling state、fault injection、recovery 與 service sign-off
source_ids: S8,S9,S10,S11,S12
watch_source_ids: S1,S2,S6
frequency: monthly
next_check: 2026-08-31
trigger: 具名 profile 或多供應商場域公開同一事件的 profile／validator 版本、request／Task／physical state、fault case、rollback、repair 與 sign-off
invalidation: 公開測試顯示 API accepted／Task state 無法可靠對應 physical state，或跨域 sequence 缺共同 owner／rollback，則閉環成熟度下修
-->

## 還缺哪些證據

- DSX 是單一平台的介面規格，不能直接稱為所有 AI 資料中心的共同標準；Redfish 使用相似資源名稱，也不能證明它和 DSX 已在欄位層互通。
- `202 Accepted` 與 Task 完成都只到管理軟體層；仍缺同一事件把命令結果、電力／液冷設備狀態、獨立感測、復原測試與維修簽核接起來的量產紀錄。
- 安全期限必須固定 hazard、起點、終點、共同時鐘、各段時間與 deadline margin；只報 API 平均延遲或 `Retry-After`，不能證明設備在期限內到達並被獨立確認為安全狀態。
- ETag 可攔下舊資源版本覆寫，卻不等於 action 可安全重送；仍要公開共同關聯編號、去重範圍、跨電力／液冷仲裁、逾時與回退規則。
- Validator 通過必須附工具、版本、profile、測試目標與 pass／fail／skip 明細；它不能替多供應商故障注入、實體動作或場域驗收背書。
- 隔離請求與狀態欄位存在，不代表隔離速度、成功率、可靠度或維護成本已改善；這些判定都需要量產現場的請求總數與成功、失敗結果。
- 族群位置、參與 OCP 或產品名稱出現相關關鍵字，都不能直接證明台灣公司取得訂單或增加獲利；目前仍缺具名公司、責任、場域與財務證據。
