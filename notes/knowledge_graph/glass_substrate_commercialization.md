# 玻璃基板商業化知識圖譜

本圖把玻璃材料能力、pilot、proof sample、客戶可靠度與 production yield 分開。公司有工廠、
合作或樣品並不等於量產；財務內圈目前刻意保持空白。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: glass-substrate-commercialization
root_node_id: concept:glass-substrate-commercialization
label: 玻璃基板商業化
summary: 從 glass core 與 TGV 技術追到 pilot、proof sample、reliability、yield 與量產，並保存 2025 HVM 預期被 2026 證據修正的歷史。
article_ids: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION
status: active
-->

<!-- knowledge_edge
edge_id: KG-GLS-C01
view: company
from_id: company:absolics
to_id: concept:glass-substrate-commercialization
relation: tests
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-12
review_due: 2026-08-14
status: active
boundary: Absolics 已有 production-ready proof samples 與未具名客戶 reliability evaluation；這會修正 2025 HVM 預期，但不是量產失敗或完成。
next_trigger: 客戶 reliability 通過，並公布 production start、yield／throughput、shipment 或 repeat order。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C02
view: company
from_id: company:intel
to_id: concept:glass-substrate-commercialization
relation: develops_packaging
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Intel 與 Lens 公告探索互補能力，且只證實合作；沒有排他、供應份額或固定量產路徑。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: Explore／potential cooperation 不等於產品、sample、qualification、mass production 或財務貢獻。
next_trigger: Intel 公布具名 glass substrate package、sample、customer qualification 與 production plan。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C03
view: company
from_id: company:lens-technology
to_id: concept:glass-substrate-commercialization
relation: supports_substrate
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Lens 提供精密玻璃加工與大規模製造能力，但合作仍在 explore 階段且未宣稱獨家。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: 一般精密玻璃量產能力不等於半導體 glass core 已完成 TGV、metallization、reliability 與 HVM。
next_trigger: Lens／Intel 公布具名 package、pilot sample、qualification 與 production。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C04
view: company
from_id: company:samsung-electro-mechanics
to_id: concept:glass-substrate-commercialization
relation: plans_production
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C5
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-01-09
review_due: 2026-09-02
status: active
boundary: Samsung Electro-Mechanics 已建立 pilot line 並目標 2027 mass production；roadmap 不等於 qualification、yield 或時程達成。
next_trigger: Customer sample result、production equipment、qualification 與 2027 timeline update。
-->

<!-- knowledge_edge
edge_id: KG-GLS-C05
view: company
from_id: company:corning
to_id: concept:glass-substrate-commercialization
relation: has_capability
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C6
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Corning Glass Core program 證實材料、TGV 與 composition 開發能力；不等於下游客戶 HVM、份額或收入。
next_trigger: 具名 semiconductor customer、qualification、production shipment 與 financial contribution。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I01
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:glass-core
relation: includes
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C6
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: 多家公司開發 glass core 支持技術路徑存在，不代表共同規格、可互換供應或量產成熟。
next_trigger: 客戶產品公開 glass core 規格、supplier、qualification 與 production。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I02
view: industry
from_id: concept:glass-substrate-commercialization
to_id: process:through-glass-via
relation: requires
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C6
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: TGV 是 glass core 互連路徑之一；技術必要性不證明特定設備、材料商或台灣公司已供貨。
next_trigger: 量產 TGV pitch、metallization、defect、throughput 與 supplier qualification。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I03
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:pilot-line
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C5
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-01-09
review_due: 2026-09-02
status: active
boundary: Samsung 已揭露 pilot line；小規模試產線不等於客戶 HVM 或穩定良率。
next_trigger: Pilot sample 通過客戶 qualification 並轉 production equipment。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I04
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:proof-sample
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C4
note_refs:
evidence_state: inference
commercial_stage: sample
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-12
review_due: 2026-08-14
status: active
boundary: SKC 的 production-ready proof sample 支持工程樣品階段；production-ready 不等於 production。
next_trigger: 具名 customer qualification、production start 與 repeat order。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I05
view: industry
from_id: concept:glass-substrate-commercialization
to_id: stage:reliability-evaluation
relation: reaches_stage
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C4
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-12
review_due: 2026-08-14
status: active
boundary: 未具名美國通訊晶片客戶正在 reliability evaluation；尚未證實通過、量產或出貨。
next_trigger: 客戶結果、qualification completion 與 production preparation start。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I06
view: industry
from_id: concept:glass-substrate-commercialization
to_id: capability:production-yield
relation: requires
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C6
note_refs:
evidence_state: inference
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-14
status: active
boundary: 公司文件把 yield improvement 列為待完成工作；本輪沒有 production yield 數值或分布。
next_trigger: 供應商公布 production yield、throughput、scrap／rework 與客戶 acceptance。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I07
view: industry
from_id: concept:glass-substrate-commercialization
to_id: component:organic-substrate
relation: competes_with
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: multi_source
exclusivity_scope: 玻璃是有機核心的潛在替代路徑；不同 package、成本與成熟度可能讓兩者長期共存。
as_of: 2026-07-24
review_due: 2026-09-02
status: active
boundary: Intel 的材料比較支持技術差異，不證明全面替代、時間、成本或客戶份額。
next_trigger: 同一 customer package 比較 glass／organic 的 qualification、yield、cost 與 production volume。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I08
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Glass composition、metallization、film 與 chemicals 是搜尋入口；沒有 universe 公司具名供貨與財務證據。
next_trigger: 客戶與材料商雙向核對料號、qualification、volume、share 與收入。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I09
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Package substrate 製造能力是搜尋路由；ABF／PCB 能力不等於 glass core qualification 或訂單。
next_trigger: 具名 glass substrate、customer qualification、production shipment 與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-GLS-I10
view: industry
from_id: concept:glass-substrate-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Handling、assembly、inspection 與 reliability 形成 OSAT 搜尋入口；沒有具名量產服務與收入。
next_trigger: OSAT 與客戶共同確認 glass substrate package、qualification、yield、shipment 與財務。
-->
