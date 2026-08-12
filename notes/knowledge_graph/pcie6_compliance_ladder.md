# PCIe 6 高速連線的測試與部署階梯

<!-- knowledge_graph_meta
schema_version: 1
graph_id: pcie6-compliance-ladder
root_node_id: concept:pcie6-deployment-readiness
label: PCIe 6 高速連線的測試與部署階梯
summary: 先把 PAM4 Flit 錯誤控制與四類正式測試放在鏈路正確性軸，再綁定受測物件 角色 CEM connector 邊界與列名程序，最後把互通 列名 量產 完整平台與財務歸因放在商品化軸；不能由任一節點推導整體成熟或台灣公司收入。
article_ids: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER
status: active
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I01
view: industry
from_id: organization:pci-sig
to_id: concept:pcie6-deployment-readiness
relation: owns_platform
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C13,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C14,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C16
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: PCI-SIG 維護測試角色 必要項 互通門檻與 Integrators List；公開清單捕捉未見 64 GT/s 列不表示測試失敗或產品不具能力。
next_trigger: 具名 64 GT/s 結果把受測物件 邊界 必要測項 listing form 與列表更新接起來。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I02
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: standard:pcie6
relation: uses_standard
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C14
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: PCIe 6.x 測試角色與部分必要項已由工作坊政策界定；制度存在不等於特定產品通過或部署。
next_trigger: 可定位的產品 角色 connector 邊界 pass revision rate 與 lane 結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I03
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:official-compliance
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C14,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C16
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: Workshop 提供 64 GT/s official testing，且制度要求互通門檻與必要測項；尚未由公開資料得知哪些具名產品完成全套程序。
next_trigger: PCI-SIG 公開具名 64 GT/s official result 與必要測項範圍。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I04
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:integrators-listing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C13,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C16
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 2026-08-12 清單捕捉仍支援部分 Gen6 功能產品在 PCIe 5.0 32 GT/s 的列項；未見最高速列不表示能力不足或測試失敗，listing form 也可能稍後提交。
next_trigger: 同一或新產品新增 PCIe 6.x 64 GT/s listing 並可核對測試日 送表日與列名日。
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

<!-- knowledge_edge
edge_id: KG-PCIE6-I13
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: process:pcie-pam4-signaling
relation: includes
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C8,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: PAM4 是 64 GT/s 實體層機制；規格採用不等於具名產品已通過電氣與協定測試。
next_trigger: 具名產品在公開測試中揭露 PAM4 通道條件 BER 與通過狀態。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I14
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: concept:pcie-flit-mode
relation: includes
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 固定 256 Byte Flit 是錯誤控制的共同資料單元；支援 Flit 不等於應用層工作負載正確。
next_trigger: 具名主機 終端與交換元件公開 Flit negotiation 及錯誤恢復結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I15
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: capability:pcie-error-control
relation: requires
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: FEC CRC 與 replay 共同管理錯誤；具備機制不表示連線零錯誤或無重送延遲。
next_trigger: 公開 FBER FEC 可修正範圍 CRC 未修正錯誤與 replay 統計。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I16
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: metric:pcie-first-bit-error-rate
relation: measured_by
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: FBER 是規格錯誤模型的一個量測；本文沒有具名產品的實測樣本 分布或誤差。
next_trigger: 具名裝置在可重現通道條件下公布 FBER 與錯誤聚集結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I17
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-electrical-testing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C9,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C10
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 電氣測試是相容性計畫的一個正式區域；區域存在不表示具名產品已通過目標速率。
next_trigger: PCI-SIG 或供應商公開具名 64 GT/s electrical pass 與測試條件。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I18
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-configuration-testing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C9,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C10
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 設定空間測試檢查能力宣告與存取行為；不能由電氣結果替代，也不代表具名產品已通過。
next_trigger: 具名產品公開 configuration test 模組版本與通過狀態。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I19
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-link-protocol-testing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C9,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C10
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 鏈路協定測試是獨立成績單；不能由能連線或支援 Flit 推成完整通過。
next_trigger: 具名產品公開 link protocol 模組版本 速率與通過結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I20
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-transaction-protocol-testing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C9,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C10
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 交易協定測試檢查讀寫 回覆與排序；不能由實體層眼圖或單次互通替代。
next_trigger: 具名產品公開 transaction protocol 模組版本與通過結果。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I21
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie6-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C7,MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C10
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 技術驗證與列名不能直接推成台灣供應商收入 毛利或現金流；本輪沒有公司雙向財務證據。
next_trigger: 平台端具名產品與供應商端同期間出貨 份額 價格 收入及毛利雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I22
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: concept:pcie-test-object-contract
relation: requires
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C15
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 測試物件合約是研究中心整理由制度欄位推出的證據框架，不是 PCI-SIG 新增的認證名稱或產品成熟度分數。
next_trigger: 第一項 64 GT/s 公開列名能重建物件 角色 邊界 必要測項 互通與列名日期。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I23
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-component-specific-testing
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C14
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 板卡或系統在 CEM connector 邊界通過不能替邊界後方 redriver 或 retimer 取得元件列名；本文沒有具名元件通過結果。
next_trigger: 具名訊號元件以 component 角色另行完成必要電氣與功能測試。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I24
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-lane-margining
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C14
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 工作坊政策把 lane margining 列為 5.0 與 6.x AIC System 必要測項；必要性不表示任何具名產品已通過或長期部署穩定。
next_trigger: 具名 64 GT/s AIC 與 System 公開 lane margining 方法 結果與可重現條件。
-->

<!-- knowledge_edge
edge_id: KG-PCIE6-I25
view: industry
from_id: concept:pcie6-deployment-readiness
to_id: stage:pcie-integrators-eligibility
relation: passes_through
claim_refs: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER#C16
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: 80% interoperability 所有必要 compliance tests 與 listing form 共同構成公開列名程序；未立即列名不是測試失敗的直接證據。
next_trigger: 具名產品公開測試日 送表日與 Integrators List date added 並完成 eligibility chain。
-->
