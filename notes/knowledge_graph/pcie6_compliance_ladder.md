# PCIe 6 高速連線的測試與部署階梯

<!-- knowledge_graph_meta
schema_version: 1
graph_id: pcie6-compliance-ladder
root_node_id: concept:pcie6-deployment-readiness
label: PCIe 6 高速連線的測試與部署階梯
summary: 把具名裝置 實際連線條件 跨廠元件互通 PCI-SIG 官方測試 公開列名 元件量產與客戶完整平台部署分開；不能由任一節點推導整體成熟或台灣公司收入。
article_ids: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I01
view: industry
from_id: organization:pci-sig
to_id: concept:pcie6-deployment-readiness
relation: owns_platform
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C1,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: PCI-SIG 維護測試活動與 Integrators List；這不表示所有 Gen6 產品已有 64 GT/s 公開結果。
next_trigger: Workshop 140 後具名 64 GT/s pass 與列表更新。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I02
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: standard:pcie6
relation: uses_standard
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: 規格與 official test option 存在不等於特定產品通過或部署。
next_trigger: 可定位的產品 pass revision rate 與 lane 結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I03
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:official-compliance
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C1
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: Workshop 提供 64 GT/s official testing；尚未由活動頁得知哪些產品通過。
next_trigger: PCI-SIG 公開具名 64 GT/s official result。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I04
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:integrators-listing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C2
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: 現行列表支援部分 Gen6 功能產品在 PCIe 5.0 32 GT/s 的列項；不表示最高能力或 64 GT/s 失敗。
next_trigger: 同一或新產品新增 PCIe 6.x 64 GT/s listing。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-C01
view: company
from_id: company:astera-labs
to_id: concept:pcie6-deployment-readiness
relation: produces
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-05-01
review_due: 2026-09-15
status: active
boundary: 公司宣稱 portfolio ramp production 與客戶 qualification；不等於 PCI-SIG 64 GT/s pass 或具名 fleet 部署。
next_trigger: Official listing 與客戶端 production deployment 的雙向證據。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-C02
view: company
from_id: company:micron
to_id: concept:pcie6-deployment-readiness
relation: produces
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-09-15
status: active
boundary: Micron 宣稱 9650 SSD high-volume production；不等於 official listing 或具名客戶 fleet 分母。
next_trigger: PCI-SIG 結果與客戶平台實際部署 利用率或數量。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I05
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: component:pcie-retimer
relation: includes
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-05-01
review_due: 2026-09-15
status: active
boundary: Astera portfolio 包含 retimer；不表示所有 retimer 已通過 64 GT/s official testing。
next_trigger: Retimer 具名 64 GT/s listing 與 multi-vendor production topology。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I06
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: component:pcie-fabric-switch
relation: includes
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-05-01
review_due: 2026-09-15
status: active
boundary: Astera portfolio 包含 fabric switch；不證明完整 host endpoint 組合已部署。
next_trigger: Switch 與獨立 host endpoint retimer 的 64 GT/s 測試及客戶部署。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I07
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: product:micron-9650
relation: includes
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C4
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-16
review_due: 2026-09-15
status: active
boundary: 9650 是量產 endpoint 證據；不代表完整 PCIe 6 生態系或客戶部署完成。
next_trigger: 9650 的 official listing 與具名 production host switch retimer 組合。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I08
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:vendor-interoperability
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C3
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-05-01
review_due: 2026-09-15
status: active
boundary: 公司 lab 與客戶 qualification 是 vendor interop 證據；測試矩陣與客戶未完整公開。
next_trigger: 至少兩家獨立元件供應商公開拓撲 速率 firmware 與可重現結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I09
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie6-platform-deployment
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C6
note_refs:
evidence_state: unverified
commercial_stage: deployment
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-09-15
status: active
boundary: 完整 production fleet 是尚未由現有來源證實的未來節點。
next_trigger: 具名客戶揭露完整平台 元件組合 部署量與實際運行結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I10
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: 只建立高速介面 IC 搜尋路由；沒有 universe 公司具名 compliance design win 或財務曝險。
next_trigger: 平台端與公司端雙向確認產品 64 GT/s qualification 出貨與財務。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I11
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: 只建立 server platform 搜尋路由；不證明具名 PCIe 6 fleet 訂單或收入。
next_trigger: 客戶與 ODM 雙向公布完整平台 qualification 部署與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I12
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C7
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-03
review_due: 2026-08-10
status: active
boundary: 只建立 64 GT/s 板材與訊號路由；不證明具名 stack-up qualification 份額或財務。
next_trigger: 平台與 PCB CCL 公司雙向確認材料 stack-up qualification 出貨與財務貢獻。
-->
