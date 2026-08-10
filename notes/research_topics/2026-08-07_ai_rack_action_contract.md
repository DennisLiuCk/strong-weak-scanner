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
- 公開文件證明 DSX 已把設備身分、感測資料、隔離請求與結果狀態寫進規格，卻不能證明現場已成功部署、不同廠牌已互通，或台灣供應商已取得收入。

### 為什麼重要

**先找對設備。** 同一座機櫃必須在監控系統與設備控制系統使用一致編號，否則畫面上的警報
可能對不到現場設備，最嚴重時甚至會隔離錯機櫃。

**再確認資料可用。** 一筆讀數要帶時間、品質與設備關係，接收端才能知道它是不是最新資料、
是否可信，以及代表哪一個位置的溫度、功率或漏液狀態。

**最後才執行動作。** 系統還要分清楚誰能提出請求、誰負責安全判斷，以及隔離後如何回報完成、
失敗與復原。少了任何一段，監控畫面可以很完整，卻不一定能安全處理故障。

### 接下來怎麼追

- 先追一個隔離請求的完整履歷：是否收到、接受或拒絕，多久完成，失敗時原因為何，以及何時復原並開立維修工單。
- 再看 OpenRMC 或 Redfish 是否提出共同測試，能跨廠牌核對機櫃身分、事件、控制動作與結果狀態。
- 最後找具名量產場域的故障注入與隔離紀錄，再由客戶和台灣公司的一手申報交叉確認責任、部署量與財務貢獻。

### 想一想

- 溫度與漏液警報都出現時，若監控畫面和設備控制系統使用不同的機櫃編號，系統要怎麼確定該隔離哪一座？
- 告警只是提醒、請求可以被拒絕、命令才會驅動設備；誰負責攔下危險請求，失聯時又由誰讓設備回到安全狀態？
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

## 三套規格各管一層：DSX、OpenRMC 與 Redfish

- **DSX 管平台內的資料與動作規則**：它具體說明建築管理系統與 IT 監控系統如何交換資料，並定義液冷與電力隔離的請求和狀態。
- **OpenRMC 管機櫃管理器的範圍**：它描述管理器如何連接上游與下游設備，以及如何處理電力、散熱、事件、任務、遙測與更新。
- **Redfish 提供通用設備管理介面**：它持續更新設備資源與動作模型，但產品支援 Redfish，不代表已支援 DSX 專用的隔離欄位或通過共同測試。

三者可以互補，名稱或功能相近卻不能直接寫成「已互通」。仍要看到欄位對照、共同測試結果，
以及同一場域從警報到隔離與復原的實際操作紀錄。

## 怎麼用這張表判讀公司新聞

1. **先問新功能會不會改變動作**：如果只有更多感測器或更漂亮的監控畫面，還不能單獨建立商業價值主張。
2. **沿七個步驟找缺口**：設備身分、資料可信度、含義、控制權、安全限制、結果回報與維修紀錄，任何一項缺失都要保留疑問。
3. **分開文件與現場成熟度**：公開介面、開放標準、共同測試、現場驗收、實際結果與財務認列，是六個不同階段。
4. **最後才連到公司**：要由客戶與供應商雙向證明，並說清楚公司負責感測器、控制器、系統整合、整櫃驗收，還是後續維護。

## 這篇目前能說到哪裡

- **已知道的事**：DSX 已公開比感測欄位清單更完整的控制規則，可以逐項查到設備身分、資料含義、發布責任、液冷與電力隔離請求、結果狀態及安全限制。
- **為何可信度是中等**：DSX 仍是單一平台規格；OpenRMC 與 Redfish 支持通用管理邊界，但還沒有共同的一致性測試與量產場域結果。
- **還不能說的事**：不能說跨平台已互通、隔離一定成功、設備價值量增加、台灣公司已供貨，或訂單、收入、毛利已可辨識。
- **何時可以升級判定**：同一個具名量產場域要公開欄位對照、故障注入、從請求到隔離與復原的時間和結果，以及維修閉環；台灣公司還要以合約責任與財務分母交叉確認。

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

## 還缺哪些證據

- DSX 是單一平台的介面規格，不能直接稱為所有 AI 資料中心的共同標準；Redfish 使用相似資源名稱，也不能證明它和 DSX 已在欄位層互通。
- 隔離請求與狀態欄位存在，不代表隔離速度、成功率、可靠度或維護成本已改善；這些判定都需要量產現場的請求總數與成功、失敗結果。
- 族群位置、參與 OCP 或產品名稱出現相關關鍵字，都不能直接證明台灣公司取得訂單或增加獲利；目前仍缺具名公司、責任、場域與財務證據。
