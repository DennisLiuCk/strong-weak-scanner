# 資料中心分期交付

同一園區已有租客時，按工程期別分開查看融資、初次通電及資料廳交付。本圖以Beacon Point
作具名案例；公司公布的未來目標保留為規劃階段，沒有台灣供應商收入歸因。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: dc-phase-delivery
root_node_id: concept:dc-phase-delivery
label: 資料中心分期交付
summary: Beacon Point兩期租約對應不同融資與交付進度；按期別查看資金、通電和資料廳，不把園區全數簽租寫成已上線算力。
article_ids: MI-2026-09-10-DC-PHASE-DELIVERY
status: active
-->

<!-- knowledge_edge
edge_id: KG-DCP-C01
view: company
from_id: company:hut8
to_id: concept:dc-phase-delivery
relation: plans_deployment
claim_refs: MI-2026-09-10-DC-PHASE-DELIVERY#C2,MI-2026-09-10-DC-PHASE-DELIVERY#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-10
status: active
boundary: 只證實Hut 8公布兩期租約與交付目標；未證實如期上線、起租或台灣公司訂單。
next_trigger: 官方文件披露各期實際交付與驗收，或調整原時程。
-->

<!-- knowledge_edge
edge_id: KG-DCP-I01
view: industry
from_id: concept:dc-phase-delivery
to_id: stage:dc-phase-financing
relation: passes_through
claim_refs: MI-2026-09-10-DC-PHASE-DELIVERY#C1,MI-2026-09-10-DC-PHASE-DELIVERY#C3
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-10
status: active
boundary: 此為逐期查證框架，第一期已融資不能證明第二期同樣完成；不作全產業信用結論。
next_trigger: 第二期融資完成公告及明確資金用途。
-->

<!-- knowledge_edge
edge_id: KG-DCP-I02
view: industry
from_id: concept:dc-phase-delivery
to_id: stage:dc-initial-energization
relation: passes_through
claim_refs: MI-2026-09-10-DC-PHASE-DELIVERY#C1,MI-2026-09-10-DC-PHASE-DELIVERY#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-10
status: active
boundary: 初次通電是獨立工程節點，原文件是未來目標，並未代表IT設備已安裝或可用。
next_trigger: 實際送電文件及涵蓋工程範圍。
-->

<!-- knowledge_edge
edge_id: KG-DCP-I03
view: industry
from_id: concept:dc-phase-delivery
to_id: stage:dc-data-hall-delivery
relation: passes_through
claim_refs: MI-2026-09-10-DC-PHASE-DELIVERY#C1,MI-2026-09-10-DC-PHASE-DELIVERY#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-10
status: active
boundary: 各期初次資料廳交付目標不等於全期容量交付或租金已開始收取。
next_trigger: 客戶驗收、實際交付規模與起租條件。
-->
