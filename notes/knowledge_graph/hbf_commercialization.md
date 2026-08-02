# HBF 商用化知識圖譜

本圖把 HBF 的公司研發角色與標準、樣品、裝置整合及客戶資格拆開。工作組與未來樣品
可以畫線，但不能跨級變成量產、財務曝險或 HBM 的已證實替代品。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hbf-commercialization
root_node_id: concept:hbf-commercialization
label: HBF 商用化
summary: 追蹤 HBF 從 NAND／logic base die 架構、OCP 標準化到 memory sample、device sample、客戶資格與量產的證據階梯。
article_ids: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-HBF-C01
view: company
from_id: company:sandisk
to_id: concept:hbf-commercialization
relation: develops_ip
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Sandisk 與 SK hynix 共同推進 HBF 標準化；產品與樣品時程由 Sandisk 揭露，不構成排他供應或量產。
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: Sandisk 是具名發起者並公布樣品目標，不等於 memory sample 已交付、客戶資格、量產或財務貢獻。
next_trigger: Sandisk 公布實體 HBF sample、規格、測試條件、接收方與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-HBF-C02
view: company
from_id: company:sk-hynix
to_id: concept:hbf-commercialization
relation: develops_ip
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1,MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: SK hynix 與 Sandisk 共同標準化，並公開 NAND／logic base die／KV cache 技術方向；未證明唯一供應或量產角色。
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 技術願景與標準合作不等於 SK hynix 已有 HBF 樣品、客戶、出貨或收入。
next_trigger: SK hynix 公布具名 sample、介面、測試、客戶資格與量產節點。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I01
view: industry
from_id: concept:hbf-commercialization
to_id: standard:hbf-workstream
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: OCP 列有 HBF workstream；工作組不等於 specification、compliance 或 multi-vendor product。
next_trigger: OCP 公開可定位的規格版本、介面與 compliance 計畫。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I02
view: industry
from_id: concept:hbf-commercialization
to_id: component:nand-flash
relation: uses_component
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: SK hynix 將 HBF 定義為 NAND solution；不證明標準 SSD NAND 可直接替代或所有 NAND 供應商都能生產 HBF。
next_trigger: 公開 HBF die、cell、stack、controller 與量產製程規格。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I03
view: industry
from_id: concept:hbf-commercialization
to_id: component:logic-base-die
relation: uses_component
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: HBF 技術方向使用 logic base die；沒有最終 node、foundry、介面、良率或供應商證據。
next_trigger: 樣品或規格公開 base die 功能、製程與製造路徑。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I04
view: industry
from_id: concept:hbf-commercialization
to_id: concept:kv-cache
relation: names_application
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-23
review_due: 2026-10-15
status: active
boundary: SK hynix 將 KV cache 列為目標資料；不證明所有 KV cache 工作負載、寫入模式與耐久條件都適用。
next_trigger: 具名裝置提供 KV cache 讀寫、延遲、耐久、容量與端到端效能結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I05
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-memory-sample
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-11
review_due: 2026-08-17
status: active
boundary: Sandisk 公布的是 2026 下半年目標，不是 sample 已交付；verified 只指時程原文。
next_trigger: 公告實際交付日、規格、測試條件、接收方與結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I06
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-device-sample
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-11
review_due: 2026-10-15
status: active
boundary: 2027 年初 device sample 是公司預期；不等於具名裝置已整合、能運行或完成客戶資格。
next_trigger: 裝置端與記憶體端雙方公布樣品、記憶體拓撲、工作負載與測試結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I07
view: industry
from_id: concept:hbf-commercialization
to_id: concept:ai-memory-hierarchy
relation: integrated_with
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C4
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: HBF 可能形成 NAND 型中間層，但尚未有實體系統證明它與 HBM、DRAM、CXL memory 或 SSD 如何分工。
next_trigger: 具名 AI 系統公布 HBF memory map、軟體調度、工作負載與端到端結果。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I08
view: industry
from_id: concept:hbf-commercialization
to_id: stage:hbf-customer-qualification
relation: passes_through
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 客戶 qualification 是必要的未來節點；本輪沒有具名客戶、測試條件或完成結果。
next_trigger: 客戶與供應商雙方確認 qualification 範圍、結果與下一步量產。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I09
view: industry
from_id: concept:hbf-commercialization
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: HBF 形成記憶體與 controller 搜尋路由，沒有 universe 公司具名產品、qualification、訂單或財務證據。
next_trigger: 平台端與公司端雙向核對 HBF 產品、客戶資格、出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HBF-I10
view: industry
from_id: concept:hbf-commercialization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 堆疊與 base die 形成封裝測試搜尋路由，不證明 universe 公司參與 HBF 或取得收入。
next_trigger: HBF 平台端具名 OSAT／設備／測試路徑，且公司端揭露 qualification、出貨與財務貢獻。
-->
