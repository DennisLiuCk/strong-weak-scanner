# UCIe 互通成熟度知識圖譜

本圖把規格速度、IP tape-out、實體跨廠 demo、compliance 與客戶產品分開。16G demo 是重要
進展，但不能替尚未公開的 64G multi-vendor product 提前畢業。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: ucie-interoperability
root_node_id: concept:ucie-interoperability
label: UCIe 互通成熟度
summary: 從 64G 規格、IP tape-out、16G 跨廠 demo 追到 compliance 與客戶量產，避免速度與成熟度錯配。
article_ids: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-UCI-C01
view: company
from_id: company:intel
to_id: concept:ucie-interoperability
relation: tests
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Cameron Creek demo 由 Intel 與 Cadence 獨立設計 chiplet 共同完成，不是單一供應商 loopback。
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: Intel 的具名 test chip 支持 16G UCIe-S live interoperability；不等於 64G、所有協定、量產封裝或客戶收入。
next_trigger: Intel 與另一供應商公布 64G UCIe 3.0 實體 compliance 與 multi-vendor demo。
-->

<!-- knowledge_edge
edge_id: KG-UCI-C02
view: company
from_id: company:cadence
to_id: concept:ucie-interoperability
relation: tests
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Cadence chiplet 與 Intel chiplet 在 Cameron Creek 形成指定 16G UCIe-S 跨廠組合；未證實其他廠商或速度。
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: Demo 證實特定實體互通，不代表 Cadence 64G IP 已完成相同測試、客戶量產或財務貢獻。
next_trigger: Cadence 公布 64G silicon、第三方 compliance、客戶 qualification 與量產節點。
-->

<!-- knowledge_edge
edge_id: KG-UCI-C03
view: company
from_id: company:synopsys
to_id: concept:ucie-interoperability
relation: develops_ip
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-17
status: active
boundary: Synopsys 已公開 64G UCIe IP tape-out 與工具鏈；不等於回片實測、跨廠 compliance、客戶產品或收入。
next_trigger: 64G test silicon 回片並與另一家獨立 chiplet 完成實體 interoperability。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I01
view: industry
from_id: concept:ucie-interoperability
to_id: standard:ucie3
relation: includes
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-05
review_due: 2026-08-17
status: active
boundary: UCIe 3.0 規格定義 48／64 GT/s 與管理功能；標準本身不證明產品、互通或部署。
next_trigger: 64G silicon 與正式 compliance result 對齊規格。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I02
view: industry
from_id: concept:ucie-interoperability
to_id: stage:specification
relation: passes_through
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-08-05
review_due: 2026-08-17
status: active
boundary: 規格發布是成熟度第一階，不可跨過 IP、silicon、互通與客戶產品。
next_trigger: 新規格有實體 test vehicle 與 compliance plan。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I03
view: industry
from_id: concept:ucie-interoperability
to_id: stage:ip-tapeout
relation: reaches_stage
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-30
review_due: 2026-08-17
status: active
boundary: Synopsys 64G IP 已 tape-out；送製造不等於回片、第三方 compliance 或量產客戶。
next_trigger: 回片實測 64G electrical／protocol behavior。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I04
view: industry
from_id: concept:ucie-interoperability
to_id: stage:cross-vendor-demo
relation: reaches_stage
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Intel／Cadence 16G UCIe-S demo 具兩家獨立 chiplet；範圍不延伸到 64G 或其他廠商。
as_of: 2026-03-05
review_due: 2026-08-17
status: active
boundary: 已跨過紙上規格，但速度、封裝與協定覆蓋仍有限。
next_trigger: 64G UCIe 3.0 multi-vendor live demo 與公開測試條件。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I05
view: industry
from_id: concept:ucie-interoperability
to_id: stage:compliance
relation: passes_through
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 64G 正式 compliance 與跨廠結果尚未由本輪證據證實。
next_trigger: Consortium 或第三方發布 64G compliance program、測試範圍與通過產品。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I06
view: industry
from_id: concept:ucie-interoperability
to_id: stage:customer-qualification
relation: passes_through
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: 尚未找到具名客戶 64G multi-vendor UCIe product qualification、量產或收入。
next_trigger: 客戶公布具名 chiplet、封裝、qualification 與 production。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I07
view: industry
from_id: concept:ucie-interoperability
to_id: process:advanced-packaging
relation: uses_packaging
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: UCIe 是封裝內介面且需 package co-design；不代表任何特定先進封裝路徑或供應商已勝出。
next_trigger: 客戶揭露 UCIe speed、package type、yield 與量產服務商。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I08
view: industry
from_id: concept:ucie-interoperability
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: PHY、controller 與 verification 是搜尋路由；沒有 universe 公司 64G UCIe design win 或財務證據。
next_trigger: 具名 IP、silicon、客戶 qualification 與收入雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I09
view: industry
from_id: concept:ucie-interoperability
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: 封裝與 compliance 測試形成 OSAT 搜尋路由；沒有具名量產客戶、服務或收入。
next_trigger: OSAT 與客戶共同確認 UCIe package、測試、量產與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-UCI-I10
view: industry
from_id: concept:ucie-interoperability
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-09-02
status: active
boundary: Package substrate 與高速 routing 是搜尋入口，不代表任一載板／PCB 公司已獲得 UCIe 訂單。
next_trigger: 客戶與供應商雙向確認具名 substrate、qualification、出貨與收入。
-->
