# 800VDC 保護責任層知識圖譜

本圖從故障與安全責任出發，分開 interlock、接地／絕緣、overcurrent／ground fault、hot-swap／
inrush 與 ride-through；hot-swap 再把預充與故障清除的時間欄位分開，維修安全則把機械隔離、
殘餘電壓與可安全接近狀態接回同一條證據鏈。公司線只到公開 requirement、reference-design 或
experimental stage，不表示量產訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: 800vdc-protection-layers
root_node_id: concept:800v-protection-layers
label: 800VDC 保護責任層
summary: 以 fault model 拆分人身維修、絕緣接地、故障電流、帶電連接與備援能量，再分開預充 故障清除 機械隔離 殘餘電壓與安全接近狀態，避免把所有保護需求合成一顆元件或台廠受惠結論。
article_ids: MI-2026-08-03-800VDC-PROTECTION-LAYERS
status: active
-->

<!-- knowledge_edge
edge_id: KG-8PL-C01
view: company
from_id: company:texas-instruments
to_id: concept:800v-protection-layers
relation: has_capability
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TI 展示 800V hot-swap input protection；Infineon 另有獨立 400／800V hot-swap reference design。
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: Reference architecture 支持 input-protection 角色，不證明完整 safety coverage、客戶 qualification、production BOM、份額或收入。
next_trigger: 具名 production platform 採用 TI design 並公布 qualification、fault tests、field operation 與出貨。
-->

<!-- knowledge_edge
edge_id: KG-8PL-C02
view: company
from_id: company:infineon
to_id: concept:800v-protection-layers
relation: samples
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Infineon REF_XDP701_4800 是 sampling reference design；TI 與其他路徑顯示 800V protection 並非單一排他供應。
as_of: 2025-10-09
review_due: 2026-09-01
status: active
boundary: 12kW、SOA-controlled inrush 與 sampling 只支持產品階段，不等於 customer qualification、production deployment、份額或財務貢獻。
next_trigger: REF_XDP701_4800 由具名客戶完成 qualification、量產部署、field fault validation 與出貨。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I01
view: industry
from_id: concept:800v-protection-layers
to_id: capability:safety-interlock
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: OCP requirement 支持 live-access de-energization／interlock 責任，不指定唯一機構、控制器、供應商或 production implementation。
next_trigger: Production rack 公布 interlock circuit、service sequence、fail-safe test 與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I02
view: industry
from_id: concept:800v-protection-layers
to_id: capability:protective-earthing
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: OCP requirement 支持 dedicated protective grounding／bonding，不指定 connector、cable、supplier、deployment 或財務價值。
next_trigger: Production rack 公布 bonding topology、fault-current test、connector／cable qualification 與 field inspection。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I03
view: industry
from_id: concept:800v-protection-layers
to_id: capability:overcurrent-protection
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: OCP 要求 outputs 具 overcurrent protection，不指定 fuse、breaker、eFuse、clearing time、selectivity 或供應商。
next_trigger: Production fault matrix 公布 current threshold、clearing time、selectivity、qualified parts 與 field results。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I04
view: industry
from_id: concept:800v-protection-layers
to_id: capability:ground-fault-detection
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: OCP 要求 ground-fault detection，不指定 sensing method、threshold、reaction、controller、supplier 或 deployment。
next_trigger: Production platform 公布 insulation／ground-fault sensing、threshold、action、test coverage 與 field log。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I05
view: industry
from_id: concept:800v-protection-layers
to_id: component:hot-swap-protection
relation: contains
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C2,MI-2026-08-03-800VDC-PROTECTION-LAYERS#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TI 與 Infineon 提供兩條獨立 800V hot-swap／input-protection 路徑，沒有排他供應證據。
as_of: 2026-03-16
review_due: 2026-09-01
status: active
boundary: Hot-swap 支持帶電連接、inrush 與 power-path protection，不取代 interlock、earthing、完整 ground-fault coverage 或 backup energy。
next_trigger: 具名 production tray／rack 公布 hot-swap topology、fault timing、qualification、field data 與 BOM。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I06
view: industry
from_id: concept:800v-protection-layers
to_id: capability:controlled-inrush
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C3
note_refs:
evidence_state: verified
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-09
review_due: 2026-09-01
status: active
boundary: Infineon sampling board 支持依 SOA 控制 inrush 的實作，不證明共同 trajectory、所有負載、production reliability 或供應份額。
next_trigger: Customer qualification 公布 bulk capacitance、pre-charge trajectory、SOA margin、fault test 與量產結果。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I07
view: industry
from_id: concept:800v-protection-layers
to_id: concept:ai-power-buffering
relation: integrated_with
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-01
status: active
boundary: CBU／BBU 與 protection layers 必須協同，但 ride-through energy 不能取代 fault isolation、interlock 或 earthing。
next_trigger: 同一 production rack 公布 protection 與 CBU／BBU 的完整 sequence、fault interaction、qualification 與 field log。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I08
view: industry
from_id: concept:800v-protection-layers
to_id: group:power
relation: routes_to
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 主動開關、控制與感測只形成 power 族群搜尋路由；沒有 universe 公司具名 BOM、qualification、訂單或財務證據。
next_trigger: 買方與台灣公司雙向確認 device、fault role、qualification、production、收入及毛利。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I09
view: industry
from_id: concept:800v-protection-layers
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: 系統整合責任只形成 powersupply 搜尋路由，不證明台灣電源廠採用特定 topology、量產、訂單或獲利。
next_trigger: 具名模組／rack 公布 protection topology、customer qualification、shipment 與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I10
view: industry
from_id: concept:800v-protection-layers
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-30
status: active
boundary: Bulk capacitance、temperature／overcurrent protection 與 filtering 只形成相鄰查核，不支持元件顆數、台灣供應商、ASP、份額或收入。
next_trigger: Production BOM 與公司申報雙向確認具名 passive part、fault role、qualification、出貨及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I11
view: industry
from_id: concept:800v-protection-layers
to_id: metric:hot-swap-startup-time
relation: measured_by
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: TI 的 440ms 只屬 800V、100µF、200mA startup target 等指定實驗設計條件，不是所有平台、電容量、溫度或元件的共同預充時間。
next_trigger: 具名 production tray 公布 pre-charge trajectory、bus sag、bulk capacitance、SOA margin、qualification 與 field log。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I12
view: industry
from_id: concept:800v-protection-layers
to_id: metric:hot-swap-fault-clearing-time
relation: measured_by
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: TI 的 10µs 與數微秒結果只屬指定 gradual-overcurrent／output-short 實驗，不是所有 fault type、配線、元件、隔離層或量產平台的共同清除時間。
next_trigger: 具名 production platform 公布各 fault type 的 threshold、clearing time、selectivity、fail-safe state、qualification 與 field result。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I13
view: industry
from_id: concept:800v-protection-layers
to_id: concept:service-safe-state
relation: contains
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C10
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-13
review_due: 2026-09-01
status: active
boundary: 可安全維修狀態是研究中心整合 IEC OCP 與 TI 文件的四道狀態與六欄護照，不是共同標準、完整 LOTO 程序、通用殘壓門檻或 production qualification。
next_trigger: 具名 production rack 公布切斷 隔離 放電 安全確認 維修放行與復歸的固定版本 state machine 及 field results。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I14
view: industry
from_id: concept:800v-protection-layers
to_id: capability:mechanical-isolation-contact
relation: requires
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C8
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: IEC 60947-10 公開摘要只固定 SCCB 與 hybrid breaker 的 series mechanical isolation contact；其他 service-isolation topology 仍須按平台文件驗證。
as_of: 2026-05-12
review_due: 2026-09-01
status: active
boundary: 公開摘要支持 interruption 與 mechanical isolation 分工，不提供付費完整條文、特定 rack 接點架構、位置回饋、測試結果、量產採用或供應商財務。
next_trigger: Production platform 公布隔離接點位置 回饋 fail-safe 測試 service sequence 與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I15
view: industry
from_id: concept:800v-protection-layers
to_id: metric:residual-voltage-after-disconnection
relation: measured_by
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-01
review_due: 2026-09-01
status: active
boundary: TI 的 2kΩ 10W 100µF 與 1.5 秒只是一組 output-discharge 設計例，不是 IEC OCP 或所有 800V platform 的共同殘餘電壓與等待時間。
next_trigger: 具名 production rack 公布各儲能位置 初始條件 放電路徑 殘壓量測位置 時間門檻 pass-fail 與 field record。
-->

<!-- knowledge_edge
edge_id: KG-8PL-I16
view: industry
from_id: concept:800v-protection-layers
to_id: metric:dc-stored-energy-discharge-pulse
relation: measured_by
claim_refs: MI-2026-08-03-800VDC-PROTECTION-LAYERS#C12,MI-2026-08-03-800VDC-PROTECTION-LAYERS#C13
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope: TI STDA029 固定一組 800V 100µF 2kΩ 10W 與 1.5 秒 reference design；32J 與 RC pulse 護照是研究中心的理想換算與查核方法，不是平台共同標準或供應商比較。
as_of: 2026-08-14
review_due: 2026-09-01
status: active
boundary: 理想模型只分開儲能 時間常數 殘壓 瞬時功率與 pulse 能量，不建立通用安全門檻、元件 pass-fail、production BOM、需求、ASP 或公司財務效果。
next_trigger: 具名 production platform 公布固定 topology reference plane 全部儲能位置 元件 pulse derating 原始電壓電流溫度軌跡 殘壓門檻量測不確定度 fault test qualification 與 field record。
-->
