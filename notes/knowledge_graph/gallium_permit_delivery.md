# 砷化鎵基板的許可與交付

以AXT申報為公司案例，先核對砷化鎵的材料，再分開出口目的地、許可與交付。
磷化銦在文章中作產品邊界的對照，沒有接成鎵需求或台廠收入的關係線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: gallium-permit-delivery
root_node_id: product:gaas-substrate
label: 砷化鎵許可與交付
summary: 機構模型提示上游精煉依賴，公司申報顯示不同目的地許可差異；逐層追到同產品交付，再判斷業務影響。
article_ids: MI-2026-09-10-GALLIUM-PERMIT-DELIVERY
status: active
-->

<!-- knowledge_edge
edge_id: KG-GPD-C01
view: company
from_id: company:axt
to_id: product:gaas-substrate
relation: produces
claim_refs: MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C2
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-13
review_due: 2026-10-01
status: active
boundary: 公司申報自身生產砷化鎵基板，並不證明所有出口目的地可交貨或資料中心收入占比。
next_trigger: 新申報分列同產品的許可及實際交付。
-->

<!-- knowledge_edge
edge_id: KG-GPD-I01
view: industry
from_id: product:gaas-substrate
to_id: capability:gallium-refining-recovery
relation: requires
claim_refs: MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C1,MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C2
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-01
status: active
boundary: 從機構上游依賴分析及公司材料披露形成查核方向，未量出鎵短缺、替代能力或可交付產量。
next_trigger: 可辨認原料、回收提純能力與合格材料供應文件。
-->

<!-- knowledge_edge
edge_id: KG-GPD-I02
view: industry
from_id: product:gaas-substrate
to_id: metric:destination-export-permit
relation: measured_by
claim_refs: MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C3,MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C7
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-01
status: active
boundary: 以AXT自身不同目的地狀態建立分列方法，未把8/13公司說法變成9/10全球法令或全面斷供結論。
next_trigger: 同產品的新許可、出口目的地與後續出貨說明。
-->

<!-- knowledge_edge
edge_id: KG-GPD-I03
view: industry
from_id: product:gaas-substrate
to_id: stage:substrate-delivery-verification
relation: passes_through
claim_refs: MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C6,MI-2026-09-10-GALLIUM-PERMIT-DELIVERY#C7
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-09-10
review_due: 2026-10-01
status: active
boundary: 這是待查節點，尚缺同產品交付與收入對照；磷化銦需求不能證明砷化鎵交付，未引用待驗證主張冒充已發生收入遞延。
next_trigger: 砷化鎵產品出貨、客戶收貨或可核對的收入解釋。
-->
