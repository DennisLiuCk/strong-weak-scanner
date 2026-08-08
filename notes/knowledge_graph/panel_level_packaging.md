# Panel-level packaging 知識圖譜

本圖把面積利用率、pilot／early qualification 與 HVM 經濟性拆開。公司節點只呈現設備商已公開的
研發或交易布局；台灣族群在具名客戶與 good-package yield 出現前維持待驗證。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: panel-level-packaging
root_node_id: concept:panel-level-packaging
label: Panel-level packaging
summary: 以面積利用率連接 uniformity、yield、throughput、panel standard 與 ECD，顯示 pilot readiness 為何尚不能直接推成 HVM 成本優勢。
article_ids: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS
status: active
-->

<!-- knowledge_edge
edge_id: KG-PLP-C01
view: company
from_id: company:lam-research
to_id: concept:panel-level-packaging
relation: has_capability
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C1
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Salzburg center 具 panel R&D、pilot、engineering test 與 early qualification 能力；不是具名客戶 HVM 或工具財務貢獻。
next_trigger: Lam 與具名客戶公開 panel tool qualification、HVM yield、throughput 與出貨。
-->

<!-- knowledge_edge
edge_id: KG-PLP-C02
view: company
from_id: company:applied-materials
to_id: concept:panel-level-packaging
relation: develops_packaging
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-03
review_due: 2026-08-23
status: active
boundary: Applied 已簽約收購 NEXX 以補 panel ECD，但公告日交易仍待完成；不證明整合、客戶採用、收入或份額。
next_trigger: 交易完成、NEXX 整合、具名客戶 qualification 與財務揭露。
-->

<!-- knowledge_edge
edge_id: KG-PLP-C03
view: company
from_id: company:5234
to_id: concept:panel-level-packaging
relation: develops_packaging
claim_refs:
note_refs: 5234#S1,5234#S4
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-12
review_due: 2026-08-21
status: active
boundary: 達興材料獨立核驗筆記支持其布局 WLP／PLP 的離型層與感光介電材料，且半導體產品組合已有量產與驗證項目；公開資料未把特定料號、量產項目或收入逐一對到 panel-level packaging 客戶與 HVM 線，因此此線維持推論。
next_trigger: 達興與客戶雙向公布 PLP 具名材料、panel form factor、qualification、量產項目、出貨量及產品收入／毛利。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I01
view: industry
from_id: concept:panel-level-packaging
to_id: component:panel-substrate
relation: uses_component
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: 方形或長方形 panel 是製程載體，不代表特定尺寸、材料或供應商已成標準或量產。
next_trigger: 客戶產品公開 panel 長寬、厚度、材料與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I02
view: industry
from_id: concept:panel-level-packaging
to_id: metric:area-utilization
relation: measured_by
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 面積利用率是幾何分子之一，不能單獨證明每個合格封裝成本較低。
next_trigger: 同一產品在 wafer／panel 路徑的可排數、good-package yield、cycle time 與成本。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I03
view: industry
from_id: concept:panel-level-packaging
to_id: capability:uniformity-control
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Lam 明列大面積 uniformity 為挑戰；沒有客戶線分布、規格與良率資料可判定問題已解決。
next_trigger: 具名 panel process 的 across-panel uniformity 與 yield correlation。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I04
view: industry
from_id: concept:panel-level-packaging
to_id: capability:yield-management
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 良率是單位成本必要分母，但本輪沒有具名產品 good-package yield 或報廢成本。
next_trigger: 客戶披露一致定義的 panel good-package yield、可靠度與成本。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I05
view: industry
from_id: concept:panel-level-packaging
to_id: metric:panel-throughput
relation: measured_by
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 大 panel 的理論輸出必須扣除 cycle time 與設備利用率；現有來源沒有可比 throughput 數字。
next_trigger: 具名工具在客戶線的 panels per hour、cycle time 與 uptime。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I06
view: industry
from_id: concept:panel-level-packaging
to_id: standard:panel-size
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Lam 明示 ecosystem 仍在決定 panel size，Applied 的 510x515mm or more 只是能力／路線敘述，不是統一標準。
next_trigger: OSAT、設備、材料與基板供應鏈採用可核對的共同 form factor。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I07
view: industry
from_id: concept:panel-level-packaging
to_id: process:panel-ecd
relation: includes
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-03
review_due: 2026-08-23
status: active
boundary: NEXX 具 large-area panel ECD 技術且交易簽約；交易完成、客戶 qualification 與量產收入仍未證。
next_trigger: Acquisition closing、產品整合、具名客戶出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I08
view: industry
from_id: concept:panel-level-packaging
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: OSAT 是 process integration 搜尋路由，沒有 universe 公司具名 panel HVM 與財務證據。
next_trigger: OSAT 與客戶雙向確認 panel form factor、qualification、量產與財務。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I09
view: industry
from_id: concept:panel-level-packaging
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: 多種 panel tool 形成設備搜尋路由，不證明台灣設備商能處理目標尺寸或已通過客戶量產資格。
next_trigger: 具名工具、panel size、客戶 qualification、量產出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I10
view: industry
from_id: concept:panel-level-packaging
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: 大型基板與 form factor 是 PCB／載板研究入口，沒有 universe 公司具名 PLP 客戶、qualification 或財務證據。
next_trigger: 基板商與客戶對同一 panel product、尺寸、量產與財務雙向核對。
-->
