# Custom HBM 客製範圍與商用階梯

<!-- knowledge_graph_meta
schema_version: 1
graph_id: custom-hbm-scope-ladder
root_node_id: concept:custom-hbm-commercialization
label: Custom HBM 客製範圍與商用階梯
summary: 顯示 Samsung SK hynix 與 Micron 各自揭露的客製入口及 sample qualification production 門檻；不能用來比較領先 市占或台灣公司收入。
article_ids: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C01
view: company
from_id: company:samsung-electronics
to_id: concept:custom-hbm-commercialization
relation: samples
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-02-12
review_due: 2026-09-15
status: active
boundary: Samsung 公開的是 2027 客戶樣品 roadmap；不是樣品已交付 客戶已 qualification 或產品已量產。
next_trigger: Samsung 與客戶雙方公布實體 custom HBM sample 產品世代 客製欄位及測試條件。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C02
view: company
from_id: company:sk-hynix
to_id: concept:custom-hbm-commercialization
relation: has_capability
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: GTC 展示支持 Stream DQ 位於 base die 與 preprocessing 搬移；不證明客戶資格 量產或跨廠效能領先。
next_trigger: 具名客戶與 SK hynix 公布可重現 workload qualification 及量產結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-C03
view: company
from_id: company:micron
to_id: concept:custom-hbm-commercialization
relation: develops_ip
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-09-23
review_due: 2026-09-23
status: active
boundary: Micron 揭露 HBM4E 客製 base logic die 選項與 TSMC 分工；較高毛利仍是預期而非已實現結果。
next_trigger: Micron 公布具名客戶 qualification 量產與可核對的 NRE 售價 良率或毛利。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I01
view: industry
from_id: concept:custom-hbm-commercialization
to_id: product:custom-hbm
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C5
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Custom HBM 是多種客製對象的集合；本線不建立共同規格或供應商排名。
next_trigger: 產業形成可共同核對的產品世代 客製欄位與 qualification 定義。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I02
view: industry
from_id: concept:custom-hbm-commercialization
to_id: component:logic-base-die
relation: uses_component
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: SK hynix 與 Micron 資料把 base die 放入各自客製路徑；不表示架構 定義或功能完全相同。
next_trigger: 公開 die function 介面 PPA 熱與客戶 qualification 的共同測試邊界。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I03
view: industry
from_id: concept:custom-hbm-commercialization
to_id: capability:workload-offload
relation: includes
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-27
review_due: 2026-09-15
status: active
boundary: 只支持 SK hynix 展示的 preprocessing 搬移方向；不是所有 custom HBM 的必要功能。
next_trigger: 客戶端可重現 workload 與端到端 latency power thermal 結果。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I04
view: industry
from_id: concept:custom-hbm-commercialization
to_id: process:customer-codesign
relation: requires
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C2,MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 客戶別規格與客製 base logic die 推導共同設計需求；不證明任何具名客戶 NRE 或獨家關係。
next_trigger: 供應商與客戶雙向揭露設計範圍 tape-out qualification 與責任分工。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I05
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-sample
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-02-12
review_due: 2026-09-15
status: active
boundary: 2027 是 Samsung roadmap；不能套用到所有公司或視為已完成節點。
next_trigger: 實體 sample shipment 與接收方 測試條件及產品世代。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I06
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-qualification
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Qualification 是尚未被三家公司以共同口徑證實的未來節點。
next_trigger: 客戶與供應商雙方公布 qualification 範圍 結果與後續量產決策。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I07
view: industry
from_id: concept:custom-hbm-commercialization
to_id: stage:custom-hbm-production
relation: passes_through
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: production
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-23
status: active
boundary: 標準 HBM4 或 HBM4E 的量產不可替代 custom HBM 量產證據。
next_trigger: 具名 custom product 進入穩定量產並揭露數量 良率或財務分母。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I08
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 只建立記憶體族群搜尋路由；沒有 universe 公司具名產品 qualification 或財務曝險。
next_trigger: 平台端與公司端完成產品 客戶資格 出貨與財務雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I09
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: Base die 與堆疊只形成封測搜尋路由；不證明任何公司參與或收入。
next_trigger: 具名封裝測試供應商 qualification 出貨與可辨識財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CHBM-I10
view: industry
from_id: concept:custom-hbm-commercialization
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 客製 base-die 邏輯只形成 IC 設計搜尋路由；不證明 design win NRE 或收入。
next_trigger: 客戶與公司雙向確認具名 IP tape-out qualification 與財務貢獻。
-->
