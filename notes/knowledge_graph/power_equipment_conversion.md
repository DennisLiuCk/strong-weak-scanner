# 燃氣設備預約、轉單與交付

以GE Vernova季度披露為案例，分開看預約、正式訂單、預付款與設備交付。
產業視圖列出後續查核欄位；公司視圖只記錄已披露的設備出貨，未連接台廠收入。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: power-equipment-conversion
root_node_id: product:gas-power-equipment
label: 燃氣設備預約與交付
summary: 預約與訂單分列後，再看管線施工準備、預付款義務及現場投運；公司季度出貨提供案例，後續計畫仍待驗證。
article_ids: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION
status: active
-->

<!-- knowledge_edge
edge_id: KG-PEC-C01
view: company
from_id: company:ge-vernova
to_id: product:gas-power-equipment
relation: produces
claim_refs: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-22
review_due: 2026-10-31
status: active
boundary: 只證實GE Vernova披露2026Q2燃氣設備出貨；全球合計未辨認資料中心客戶或台灣供應商。
next_trigger: 下一季度同口徑出貨與具名客戶文件。
-->

<!-- knowledge_edge
edge_id: KG-PEC-I01
view: industry
from_id: product:gas-power-equipment
to_id: metric:gas-backlog-and-reservations
relation: measured_by
claim_refs: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C1,MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C2
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-31
status: active
boundary: 以公司分列欄位形成追蹤框架，含預約合計不能視為全部正式訂單，未計算產業轉換率。
next_trigger: 同定義的新增預約、既有預約轉單、出貨及季末存量。
-->

<!-- knowledge_edge
edge_id: KG-PEC-I02
view: industry
from_id: product:gas-power-equipment
to_id: capability:gas-project-construction-readiness
relation: requires
claim_refs: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C1,MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-31
status: active
boundary: 從GE Vernova所述轉單流程提出施工查核問題，未證實每個客戶專案已完成準備。
next_trigger: 公司或客戶提供管線、工程總包及設備時程的配對。
-->

<!-- knowledge_edge
edge_id: KG-PEC-I03
view: industry
from_id: product:gas-power-equipment
to_id: metric:equipment-prepayments-and-obligations
relation: measured_by
claim_refs: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C3,MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C5
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-31
status: active
boundary: 現金與履約分時的判讀框架；美元剩餘履約義務含設備服務，不能換算為燃氣設備GW或把全部現金流歸於預約。
next_trigger: 新季度合約負債、付款節奏及設備服務履約說明。
-->

<!-- knowledge_edge
edge_id: KG-PEC-I04
view: industry
from_id: product:gas-power-equipment
to_id: stage:gas-equipment-commissioning
relation: passes_through
claim_refs: MI-2026-09-10-POWER-EQUIPMENT-CONVERSION#C6
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-31
status: active
boundary: 出貨後仍須現場安裝及測試；管理層產出與投運展望尚待驗證，沒有統一專案交期。
next_trigger: 實際季度產出及具名專案的安裝、測試與投運文件。
-->
