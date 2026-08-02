# 800VDC 保護責任層知識圖譜

本圖從故障與安全責任出發，分開 interlock、接地／絕緣、overcurrent／ground fault、hot-swap／
inrush 與 ride-through。公司線只到公開 requirement 或 reference-design stage，不表示量產訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: 800vdc-protection-layers
root_node_id: concept:800v-protection-layers
label: 800VDC 保護責任層
summary: 以 fault model 拆分人身維修、絕緣接地、故障電流、帶電連接與備援能量，避免把所有保護需求合成一顆元件或台廠受惠結論。
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
