# 800VDC 功率半導體鏈知識圖譜

本圖先用 topology 判斷哪些轉換、隔離、備援與保護級存在，再把 SiC、GaN 與 Si 放回同一
power stage 的六軸選材包絡線。公司節點只表示已公開的架構、reference design 或產品規劃；
沒有一條線代表台灣公司已取得訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: 800v-power-tree
root_node_id: concept:800v-power-tree
label: 800VDC 功率半導體鏈
summary: 先分開現行 48V、過渡 sidecar、設施級 800V 與靠近運算的直降 topology，再以工作電壓電流、切換、隔離、保護、熱封裝及 qualification 六軸拆解 SiC、GaN 與 Si，並分開 reference design、系統驗收與財務歸因。
article_ids: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION
status: active
-->

<!-- knowledge_edge
edge_id: KG-8VP-C01
view: company
from_id: company:nvidia
to_id: concept:800v-power-tree
relation: owns_platform
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA 公開的是 800VDC 架構與多家 silicon／power ecosystem；並非單一元件、材料或供應商的排他平台。
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Starting in 2027 是架構錨點，不證明 2026 full-scale deployment、固定 BOM 或個別供應商收入。
next_trigger: NVIDIA 公布 production-level power tree、qualification 與實際 rack deployment。
-->

<!-- knowledge_edge
edge_id: KG-8VP-C02
view: company
from_id: company:infineon
to_id: concept:800v-power-tree
relation: has_capability
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C2,MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Infineon 同時展示 GaN IBC 與 SiC BBU 路徑；這是多材料 portfolio，不是任何 stage 的獨家供應證據。
as_of: 2026-06-02
review_due: 2026-08-16
status: active
boundary: 具名 reference design 支持技術角色，不等於 hyperscaler qualification、量產、部署或財務貢獻。
next_trigger: 客戶把具名 Infineon design／device 導入 production rack 並揭露 qualification 與 shipment。
-->

<!-- knowledge_edge
edge_id: KG-8VP-C03
view: company
from_id: company:onsemi
to_id: concept:800v-power-tree
relation: has_capability
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C4
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: onsemi 公開 SST 高壓 SiC 路徑與產品定位；不等於具名 AI 資料中心採用、量產份額或收入。
next_trigger: 客戶或 onsemi 公布具名 SST／800V product qualification、shipment 與 deployment。
-->

<!-- knowledge_edge
edge_id: KG-8VP-C04
view: company
from_id: company:rohm
to_id: concept:800v-power-tree
relation: plans_production
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: ROHM 規劃在特定 AC-DC PSU 同時採用 Si 與 SiC MOSFET；不是單一材料或供應商排他設計。
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: Management planned adoption 不等於截至本輪已量產、客戶驗收、800V full-scale rack 或財務貢獻。
next_trigger: ROHM／客戶確認 production start、具名 PSU、出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-8VP-C05
view: company
from_id: company:2481
to_id: concept:800v-power-tree
relation: has_capability
claim_refs:
note_refs: 2481#S1,2481#S4
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-12
review_due: 2026-08-20
status: active
boundary: 強茂獨立核驗筆記支持 650V／1200V SiC SBD 已發佈、伺服器主板導入及 AI／運算應用曝險；把這些具名產品能力連到 800VDC 功率鏈仍是相鄰推論，不證明 800V rack qualification、production BOM、訂單、收入或毛利。
next_trigger: 強茂與平台／客戶雙向公布 800V BBU、PSU 或保護節點的具名料號、failure criteria、qualification、量產出貨與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I01
view: industry
from_id: concept:800v-power-tree
to_id: component:sic-power
relation: uses_component
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: SiC 在本輪分布於 SST、BBU、hot-swap 與 PSU 等多種 stage，且各 stage 仍可能有其他材料／topology。
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: 功能分區來自多份供應商設計，不是固定 BOM、材料份額或 winner-takes-all 結論。
next_trigger: 同一 production rack 公布各 stage 的 SiC device、qualification 與 volume。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I02
view: industry
from_id: concept:800v-power-tree
to_id: component:gan-power
relation: uses_component
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: GaN 在 Infineon design 用於高頻 HV IBC，仍與低壓 Si device、driver、controller 共同工作且不是唯一可行 topology。
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: Reference design 支持應用位置，不代表全產業採用、量產份額或公司財務貢獻。
next_trigger: 具名客戶完成 GaN HV IBC qualification、production 與 deployment。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I03
view: industry
from_id: concept:800v-power-tree
to_id: component:silicon-power
relation: uses_component
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Si 與 WBG 元件可在同一 PSU／IBC 共存；位置取決於 voltage、control、cost 與 topology。
as_of: 2026-08-02
review_due: 2026-08-16
status: active
boundary: Silicon 保留部分環節不代表內容量固定，也不表示 SiC／GaN 無法往相鄰 stage 延伸。
next_trigger: Production BOM 揭露 Si、SiC、GaN 的 stage 與 device count。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I04
view: industry
from_id: concept:800v-power-tree
to_id: component:solid-state-transformer
relation: contains
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C4
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-14
review_due: 2026-08-16
status: active
boundary: SST 是 onsemi 描述的 early-commercialization 高壓路徑；不代表具名 AI 資料中心已量產採用。
next_trigger: 具名 hyperscaler SST qualification、deployment 與 operating data。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I05
view: industry
from_id: concept:800v-power-tree
to_id: component:high-voltage-bbu
relation: contains
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-08-16
status: active
boundary: Infineon 24 kW SiC BBU 是 reference design，不是具名客戶 production module 或 deployed rack。
next_trigger: 客戶 qualification、production shipment 與 field reliability。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I06
view: industry
from_id: concept:800v-power-tree
to_id: component:hv-ibc
relation: contains
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-17
review_due: 2026-08-16
status: active
boundary: 800V／±400V 至 50V／12V GaN design 已具體；不等於所有 rack 採同一路徑或已量產。
next_trigger: 具名 platform／customer 導入 production HV IBC。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I07
view: industry
from_id: concept:800v-power-tree
to_id: component:hot-swap-protection
relation: contains
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-08-16
status: active
boundary: SiC JFET 在指定 BBU reference design 提供 ORing／hot-swap；不代表所有保護節點或客戶 BOM。
next_trigger: 800V production rack 的 fault protection、qualification 與 serviceability 規格。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I08
view: industry
from_id: concept:800v-power-tree
to_id: stage:reference-design
relation: reaches_stage
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C2,MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-02
review_due: 2026-08-16
status: active
boundary: GaN IBC 與 SiC BBU 已到 reference design；這一階不能改寫成 customer qualification 或 production。
next_trigger: Reference design 被具名客戶採用並完成 qualification。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I09
view: industry
from_id: concept:800v-power-tree
to_id: component:point-of-load
relation: contains
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C5
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Grid-to-core 功能框架保留 processor-level silicon；本輪沒有同一 rack 的完整 POL production BOM。
next_trigger: Platform 公布 800V 到 GPU core 的完整轉換鏈與量產元件。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I10
view: industry
from_id: concept:800v-power-tree
to_id: group:power
relation: routes_to
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: 功率元件是研究路由；本輪沒有 universe 公司具名 800V qualification、訂單或財務證據。
next_trigger: 客戶與公司雙向核對具名 device、stage、量產與收入。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I11
view: industry
from_id: concept:800v-power-tree
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: PSU、BBU 與 IBC 形成電源族群搜尋路由；外部 reference design 不證明台灣廠採相同 BOM 或已認列收入。
next_trigger: 具名 800V power product、客戶 qualification、shipment、收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I12
view: industry
from_id: concept:800v-power-tree
to_id: concept:800v-topology-device-selection
relation: includes
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C7
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: NVIDIA、TI、ST、OCP 與既有供應商來源展示不同 topology／stage；它們是獨立架構鏈，不是同一 production system 的多數決。
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 兩層框架用來固定研究順序與比較條件，不是唯一最佳架構、材料份額、device count、供應商排名或財務預測。
next_trigger: 平台或客戶固定 production topology／revision，逐級公開責任、具名 device 與 pass-fail。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I13
view: industry
from_id: concept:800v-power-tree
to_id: metric:power-stage-selection-envelope
relation: measured_by
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C7
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 六軸來自多條轉換、保護與過渡架構的共同設計邊界；各公司仍使用不同 input／output、topology 與 reference plane。
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 六軸是條件清單，不合成分數；未固定輸入輸出、負載、冷卻、隔離與測法時不得跨設計排名。
next_trigger: 同一 power stage 公開兩個以上方案的對齊條件、原始結果、不確定度與 failure boundary。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I14
view: industry
from_id: concept:800v-power-tree
to_id: component:direct-hv-bus-converter
relation: includes
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C8,MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C9
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: TI 與 ST 各自公開 800V-to-6V／12V 路徑，ST 另有 800V-to-50V prototype；不同供應商與 topology 不構成單一客戶 BOM。
as_of: 2026-03-17
review_due: 2026-08-19
status: active
boundary: Reference architecture／prototype 支持可行路徑，不證明 NVIDIA production topology、客戶 qualification、量產份額或收入。
next_trigger: 具名平台固定 direct-conversion revision、converter raw test、rack integration、customer pass 與 production BOM。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I15
view: industry
from_id: concept:800v-power-tree
to_id: component:48v-power-shelf
relation: includes
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C10
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: limited_source
exclusivity_scope: 本邊只依 OCP HPR V2 1.0.0 規格固定一套 48V contract；不代表所有 rack、會員實作或 alternate architecture。
as_of: 2026-06-12
review_due: 2026-08-19
status: active
boundary: 規格支持 72kW、6×12kW、60kW N+1 與 48V 系統要求，不證明共同 qualification、部署量、供應商或財務。
next_trigger: 具名產品依相同 revision 公開 qualification、production shipment、deployment denominator 與 transition plan。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I17
view: industry
from_id: concept:800v-power-tree
to_id: stage:800v-subsystem-qualification
relation: reaches_stage
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C11
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 本輪沒有同一 800V converter／BBU／protection revision 的完整原始 test matrix、pass-fail、change control 與 customer acceptance。
next_trigger: 具名 subsystem 固定 topology、device、firmware、cooling 與 fault boundary，公開可重算 qualification pack。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I18
view: industry
from_id: concept:800v-power-tree
to_id: stage:800v-site-acceptance
relation: reaches_stage
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C11
note_refs:
evidence_state: unverified
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: Platform path、reference design 與 48V specification 都不證明具名 800V rack／site 已完成 as-built fault、safety、serviceability、load 與 operating-hours acceptance。
next_trigger: 具名客戶場站公開 revision、commissioning、fault injection、acceptance、deployment denominator 與 field reliability。
-->

<!-- knowledge_edge
edge_id: KG-8VP-I19
view: industry
from_id: concept:800v-power-tree
to_id: stage:800v-commercial-attribution
relation: reaches_stage
claim_refs: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION#C11
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 本輪沒有買方與供應商對上同一 800V product／site／period 的 production BOM、shipment、revenue、cost、margin 與 cash。
next_trigger: 雙方揭露可核對的 product revision、deployed volume、shipment、收入成本毛利與分母，且排除 48V／54V 過渡產品混入。
-->
