# 小晶片設計資料交接與合規鏈知識圖譜

本圖把封裝內連線、系統角色、機器可讀設計資料與端到端符合性流程分開。公開證據目前只到
正式架構、部分可執行 schema 與單工具自述，不把它畫成跨工具、封測量產或公司訂單。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: chiplet-design-handoff-contracts
root_node_id: concept:chiplet-design-handoff
label: 小晶片設計資料交接與合規鏈
summary: 從介面 系統角色 CDXML 與 3DK 資料包追到 schema 執行 跨工具重現及 foundry OSAT 簽核 避免把規格發布當成端到端隨插即用。
article_ids: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS
status: active
-->

<!-- knowledge_edge
edge_id: KG-CDH-C01
view: company
from_id: company:arm
to_id: concept:chiplet-design-handoff
relation: develops_ip
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C1,MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C4
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: FCSA 1.0.0 文件由 Arm Ltd. 撰寫且 OCP implementation 清單目前只列 Arm CSA；清單明示列名不構成 endorsement。
as_of: 2026-08-12
review_due: 2026-08-24
status: active
boundary: Arm 的 CSA FCSA 架構工作與公開平台案例不證明 CDXML 3DK 跨工具結果 foundry OSAT 簽核 客戶量產或財務貢獻。
next_trigger: Arm 與獨立工具 製造 封測及買方共同公布固定 FCSA 3DK 版本 測試結果與產品資格。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I01
view: industry
from_id: concept:chiplet-design-handoff
to_id: standard:ucie3
relation: integrated_with
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C7
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: UCIe 代表連線介面層的例子；本圖不主張 FCSA CDXML 或 3DK 只能搭配 UCIe，也不以介面互通替代資料交接。
next_trigger: 同一具名多供應商產品公開介面版本 FCSA profile 3DK bundle 與各層測試結果。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I02
view: industry
from_id: concept:chiplet-design-handoff
to_id: standard:fcsa
relation: includes
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-02-12
review_due: 2026-08-24
status: active
boundary: FCSA 1.0.0 定義 system topology chiplet type interface requirement 與 compliance level；不背書 CDXML 3DK tool import 或製造資格。
next_trigger: 非 Arm 實作公開固定 FCSA version level test suite 與可重現通過結果。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I03
view: industry
from_id: concept:chiplet-design-handoff
to_id: standard:cdxml
relation: includes
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C2,MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C5
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: OCP 已公開 CDXML 與相關 XSD；固定 commit 的四份 XSD 中只有 MDK TDK 可編譯，不能描述為完整可執行 conformance pack。
next_trigger: 正式 tag 下 CDXML ADK MDK TDK 全數可解析編譯 並附正反範例與預期結果。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I04
view: industry
from_id: concept:chiplet-design-handoff
to_id: concept:3d-ic-design-kits
relation: contains
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C2,MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2025-01-21
review_due: 2026-08-31
status: active
boundary: 3DK 教程分出 CDK ADK MDK TDK DRM 與 SI PI design kit；工作分解不等於六種套件已形成同版交付包。
next_trigger: OCP 或標準組織發布固定版本 3DK manifest dependency version 與 validator。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I05
view: industry
from_id: concept:chiplet-design-handoff
to_id: stage:executable-schema
relation: reaches_stage
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C5
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 固定 commit 只有四份 XSD 中兩份可編譯 因此只到部分 executable schema 而非整套通過。
next_trigger: 四份 XSD 在 CI 以固定 parser 完整編譯 並對正反 XML 範例符合預期。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I06
view: industry
from_id: concept:chiplet-design-handoff
to_id: stage:single-tool-import
relation: reaches_stage
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: limited_source
exclusivity_scope: 本輪只找到 OCP Marketplace 上 Thrace DankaChiplet 的 CDXML 產品自述 沒有第二套工具共同結果。
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 單工具產品頁沒有 schema version input bundle diagnostics 或客戶結果 不代表跨工具互通。
next_trigger: Thrace 公布固定 CDXML 版本 import coverage sample input validator output 與可重現操作。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I07
view: industry
from_id: concept:chiplet-design-handoff
to_id: stage:cross-tool-conformance
relation: passes_through
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C8
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: 尚未找到兩套獨立 EDA 工具對固定版本共同正反資料輸出一致 pass fail 的公開報告。
next_trigger: 兩家工具商公布 tool version schema SHA test vector expected error units 與一致結果。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I08
view: industry
from_id: concept:chiplet-design-handoff
to_id: stage:foundry-osat-conformance
relation: passes_through
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C9
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: 多供應商平台與介面互通沒有揭露同一 3DK bundle 的製造 封裝 測試 sign-off 與買方資格。
next_trigger: Foundry OSAT 與買方共同公布 bundle version tool checks waiver qualification 與量產節點。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I09
view: industry
from_id: concept:chiplet-design-handoff
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-31
status: active
boundary: CDK authoring interface alignment 與 tool validation 只形成矽智財研究入口 沒有 universe 公司 design win 訂單或財務證據。
next_trigger: 買方與公司雙向確認具名 IP data bundle qualification deployment 收入與毛利。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I10
view: industry
from_id: concept:chiplet-design-handoff
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: ADK TDK sign-off 與 qualification 只形成封測搜尋路由 沒有 universe OSAT 具名流程 客戶 量產或財務證據。
next_trigger: OSAT 與買方共同公布固定 3DK bundle 封裝測試資格 量產數量 價格與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CDH-I11
view: industry
from_id: concept:chiplet-design-handoff
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-12-CHIPLET-DESIGN-HANDOFF-CONTRACTS#C10
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-30
status: active
boundary: TDK 與共同合規若落地才可能改變量測測試需求 目前沒有設備型號 測項 產能 訂單或收入。
next_trigger: 公開 test plan 將新測項與具名設備 工時 產能 客戶資格及出貨分母對齊。
-->
