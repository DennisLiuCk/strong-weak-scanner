# AI 機櫃控制契約知識圖譜

本圖把 rack identity、Value／Metadata、publisher ownership、guardrail、isolation state 與
service outcome 分開。DSX 提供平台內具體契約；OpenRMC／Redfish 只作獨立管理邊界，
沒有共同 conformance 與場域結果前不畫成已互通，也不建立台灣公司供貨線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ai-rack-action-contract
root_node_id: concept:ai-rack-action-contract
label: AI 機櫃控制契約
summary: 從穩定身分與具語意 telemetry 走到 request owner、安全裁決、隔離狀態及維修結果，拆開資料點存在與營運閉環的差距。
article_ids: MI-2026-08-07-AI-RACK-ACTION-CONTRACT
status: active
-->

<!-- knowledge_edge
edge_id: KG-RAC-C01
view: company
from_id: company:nvidia
to_id: concept:ai-rack-action-contract
relation: owns_platform
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C1,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C2,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: NVIDIA 公開 DSX BMS Event Bus 與 integration guidance，只證明平台契約；不證明 production site、跨平台互通、field outcome、排他供應或台灣公司財務曝險。
next_trigger: 具名 production site 公布 DSX commissioning、故障注入、隔離與復原結果。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I01
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:rack-identity-coordination
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C1
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: DSX 要求 IT／OT 共用穩定 rackLocationId，不證明任何場域已正確映射或能處理資產異動與錯配。
next_trigger: 具名 site 公布 rack identity onboarding、變更、錯配偵測與復原測試。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I02
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:typed-event-context
relation: measured_by
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C1
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: Value 的 timestamp／quality 與 Metadata 的語意只建立資料契約，不證明感測校正、時鐘同步、完整率或下游使用正確。
next_trigger: Production site 公布資料完整率、延遲、時鐘與 quality-code 處置結果。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I03
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:action-ownership
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C2,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: DSX 分開 integration publisher 與 BMS authority，不證明場域 ACL、稽核、去重、拒絕理由或合約責任完整。
next_trigger: 具名 integration 公布權限、request identity、accept／reject 與 audit trail。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I04
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:guardrailed-isolation
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C3,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: 文件建議 guardrail 與 safe default；把它視為完整 action-contract 必要層是研究推論，不指定限值、拓撲、功能安全或 field performance。
next_trigger: Site sequence of operations 與故障注入公開 guardrail、safe state、動作時間及測試結果。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I05
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:action-state-feedback
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C5
note_refs:
evidence_state: unverified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: DSX 有 request 與 isolation status vocabulary，但完整 accept／reject／failed／recover／service state 及跨平台 conformance 尚未驗證。
next_trigger: 公開 schema 與 field log 能逐一重建 request 到維修完成的狀態與時間。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I06
view: industry
from_id: concept:ai-rack-action-contract
to_id: standard:openrmc-northbound
relation: integrated_with
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C5
note_refs:
evidence_state: unverified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: OpenRMC 的 power／thermal／event／telemetry 管理範圍可與本框架對照，但沒有證據證明 DSX point contract 已映射或跨廠互通。
next_trigger: OCP 公布 current profile、DSX mapping 與多供應商 conformance result。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I07
view: industry
from_id: concept:ai-rack-action-contract
to_id: standard:redfish-management
relation: integrated_with
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C5
note_refs:
evidence_state: unverified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: Redfish 提供通用管理文件集合；標準存在不等於產品支援 DSX isolation point types、相同 sequence 或通過 profile。
next_trigger: 正式 Redfish profile 與測試把 rack identity、event、action、state feedback 對齊並公布結果。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I08
view: industry
from_id: concept:ai-rack-action-contract
to_id: concept:liquid-cooling-loop-boundary
relation: integrated_with
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: Liquid isolation 與 leak telemetry 是 action-contract 的應用之一；本圖不取代 FWS／TCS／ITE、元件與場域責任研究。
next_trigger: 同一場域公布 leak detect、liquid isolation、復原與維修的完整 sequence。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I09
view: industry
from_id: concept:ai-rack-action-contract
to_id: concept:800v-protection-layers
relation: integrated_with
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-08-31
status: active
boundary: Electrical isolation request 可連到保護 fault model，但 DSX 文件不指定 800V／48V topology、fault clearing、元件或供應商。
next_trigger: 同一 production rack 公布 electrical isolation request、保護動作、timing、復原與 fault log。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I10
view: industry
from_id: concept:ai-rack-action-contract
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-09-30
status: active
boundary: ODM 位於 rack、RMC、BMS mapping 與 commissioning 交界，只形成搜尋路由；沒有具名合約責任、部署或財務證據。
next_trigger: 客戶與 ODM 雙向確認 implementation、conformance、site acceptance、部署量及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I11
view: industry
from_id: concept:ai-rack-action-contract
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-09-30
status: active
boundary: 電力隔離與 power telemetry 只形成電源族群搜尋路由；不證明 topology、控制器、qualification、訂單或財務。
next_trigger: 具名 power implementation 與公司申報對齊 action role、site acceptance、出貨及毛利。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I12
view: industry
from_id: concept:ai-rack-action-contract
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-07
review_due: 2026-09-30
status: active
boundary: Liquid isolation、leak 與 CDU telemetry 只形成散熱族群搜尋路由；不支持元件 BOM、供應商份額、部署或收入。
next_trigger: 客戶與公司雙向確認具名液冷 action contract、commissioning、field result 及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I13
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:async-action-tracking
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C7
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Redfish 證實 202、Task Monitor、TaskState 與最後結果可分開；不證明 DSX 已採同一 Task 或物理設備已到位。
next_trigger: 具名整合保存 request、Task、錯誤與完成時間，並可和設備讀值及工單按同一事件追查。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I14
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:stale-write-protection
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C8
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: ETag 與條件式更新可攔版本衝突；不提供 action 去重、冪等、跨域仲裁、guardrail 或物理結果驗證。
next_trigger: 具名 isolation 實作公開資源版本、衝突處理、重送去重與跨控制器競爭測試。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I15
view: industry
from_id: concept:ai-rack-action-contract
to_id: standard:redfish-interop-profile
relation: integrated_with
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C10
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: Profile 與三類 validator 可固定並查核最低 API 能力；不等於多供應商 action sequence、故障注入、場域可靠度或驗收。
next_trigger: 正式 rack action profile 公開逐項要求、工具版本、結果與至少兩個獨立實作的互通矩陣。
-->

<!-- knowledge_edge
edge_id: KG-RAC-I16
view: industry
from_id: concept:ai-rack-action-contract
to_id: capability:physical-state-verification
relation: requires
claim_refs: MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C13,MI-2026-08-07-AI-RACK-ACTION-CONTRACT#C15
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 把 Task 完成後的設備狀態、獨立感測、復原與維修另列為必要驗收層是跨文件推論；公開資料沒有共同 production record。
next_trigger: 同一場域公布 request／Task、commanded／observed power／cooling state、fault injection、rollback、repair 與 service sign-off。
-->
