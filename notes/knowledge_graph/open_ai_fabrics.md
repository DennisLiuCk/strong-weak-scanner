# AI 資料路徑與跨廠互通知識圖譜

本圖先把運算端點、連接傳輸、交換器、控制軟體與目的端點放回同一條資料路徑，再分開
機架內 UALink、ESUN／SUE-T 與跨機架 UEC、UALoE、晶粒及部署成熟度。規格、產品與雲端
規劃可以相連，但不能相加成已互通或已部署收入；台灣族群仍只保留為待驗證搜尋路由。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: open-ai-fabrics
root_node_id: concept:open-ai-fabrics
label: AI 資料路徑與跨廠互通
summary: 先展開端點、連接傳輸、交換器、控制軟體與目的端點，再把 UALink、ESUN／SUE-T 機架內路徑與 UEC 跨機架路徑分開，依序追蹤規格、實體晶片、合規、跨廠互通、系統與雲端部署。
article_ids: MI-2026-08-02-OPEN-AI-FABRICS
status: active
-->

<!-- knowledge_edge
edge_id: KG-FAB-C01
view: company
from_id: company:amd
to_id: concept:open-ai-fabrics
relation: uses_standard
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Helios 同時使用 UALink／UALoE scale-up 與 UEC-ready Ethernet scale-out，且為 reference design，不是單一互連或單一 OEM 的排他產品。
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: AMD Helios 產品頁證實架構整合，不等於 OEM 量產、multi-vendor interoperability、客戶驗收或財務貢獻。
next_trigger: AMD／OEM 公布具名 Helios 量產、互通測試與客戶部署。
-->

<!-- knowledge_edge
edge_id: KG-FAB-C02
view: company
from_id: company:oracle
to_id: concept:open-ai-fabrics
relation: planned_customer
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-14
review_due: 2026-08-17
status: active
boundary: Oracle／AMD 證實的是 Q3 2026 起的 MI450／Helios 與 UALink-over-Ethernet 規劃，不是截至 2026-08-02 已部署、GA 或收入。
next_trigger: Oracle 或 AMD 公布 shipment、preview、GA、實際部署與利用率。
-->

<!-- knowledge_edge
edge_id: KG-FAB-C03
view: company
from_id: company:marvell
to_id: concept:open-ai-fabrics
relation: develops_ip
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C8
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-06-11
review_due: 2026-08-10
status: active
boundary: Marvell 已公告 custom UALink solution 與 IP 組合；不等於第三方 compliance、客戶 design win、量產出貨或收入。
next_trigger: Marvell 或客戶公布 UALink silicon、樣品、qualification、量產與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I01
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:ualink
relation: includes
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-07
review_due: 2026-08-10
status: active
boundary: UALink 2.0 規格已 ratify；規格不等於 silicon、switch、compliance、互通或部署。
next_trigger: UALink 公布 compliance／plugfest 結果與至少兩家可核對的 multi-vendor products。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I02
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:uec
relation: includes
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C2
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: UEC 現行公開版本為 1.0.3；版本發布不證明 NIC、switch、optics、cable 已互通或部署。
next_trigger: UEC 公布 compliance、互通結果與商用產品清單。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I03
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:scale-up
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C1,MI-2026-08-02-OPEN-AI-FABRICS#C3,MI-2026-08-02-OPEN-AI-FABRICS#C10,MI-2026-08-02-OPEN-AI-FABRICS#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: UALink／Helios 與 ESUN／Arista 文件都證實 scale-up 路徑存在；不代表各路徑已 compliance、互通、部署或能用共同口徑比較。
next_trigger: UALink 與 Ethernet scale-up 各自有商用 accelerator endpoint、switch 與軟體完成可重現的 multi-vendor interoperability。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I04
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:scale-out
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C2,MI-2026-08-02-OPEN-AI-FABRICS#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: UEC 與 Helios 文件證實 Ethernet scale-out 層；不代表 UEC 1.0.3 產品已在 Helios 部署。
next_trigger: UEC-ready NIC／switch／optics 進入具名 Helios 或其他 AI 叢集並完成互通。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I05
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:ualoe
relation: includes
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C4
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-14
review_due: 2026-08-17
status: active
boundary: Oracle／AMD 公告規劃使用 UALink protocol over UALoE；不等於目前已部署或所有 UALink 系統都走相同傳輸。
next_trigger: Oracle／AMD 公布實際 UALoE silicon、shipment、preview／GA 與部署結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I06
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:ucie3
relation: integrated_with
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C7
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-07
review_due: 2026-08-10
status: active
boundary: UALink chiplet specification 明列與 UCIe 3.0 相容；規格相容不等於實體 chiplet、package 或 PHY 完成互通。
next_trigger: UALink／UCIe 公布 chiplet compliance、test vehicle 與 multi-vendor silicon。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I07
view: industry
from_id: concept:open-ai-fabrics
to_id: product:amd-helios
relation: integrated_with
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C3
note_refs:
evidence_state: verified
commercial_stage: integration
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Helios 是同時整合 UALink／UALoE 與 UEC-ready Ethernet 的開放 reference design，不是單一標準或供應商的排他系統。
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: Reference design 證實系統架構，不等於 OEM 量產、客戶驗收、部署或供應商收入。
next_trigger: AMD、OEM 或客戶公布 Helios 實際交付、互通與部署。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I08
view: industry
from_id: concept:open-ai-fabrics
to_id: stage:interoperability
relation: passes_through
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-04-07
review_due: 2026-08-10
status: active
boundary: UALink 表示 interoperability／compliance programs 將在後續導入，證實的是待完成節點而非已通過結果。
next_trigger: UALink 正式啟動 program 並發布可核對的 compliance／plugfest 結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I09
view: industry
from_id: concept:open-ai-fabrics
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 開放機架與互連形成 ODM 搜尋路由，但沒有 universe 公司具名 UALink／UEC 量產、訂單或財務證據。
next_trigger: OEM／ODM 與平台端雙向核對具名系統、互通、量產出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I10
view: industry
from_id: concept:open-ai-fabrics
to_id: group:ipdesign
relation: routes_to
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: Controller、PHY、retimer、switch 與 chiplet IP 是研究路由，不證明 universe 公司有 compliance、design win 或收入。
next_trigger: 公司揭露具名 UALink／UEC／UCIe IP、silicon、客戶 qualification 與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I11
view: industry
from_id: concept:open-ai-fabrics
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C6
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-17
status: active
boundary: 高速訊號與連接形成 PCB／CCL 搜尋路由，沒有具名板材、載板、連接器或光模組財務證據。
next_trigger: 平台與台灣公司雙向核對具名 UALink／UEC 系統材料、qualification、出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-FAB-C04
view: company
from_id: company:arista
to_id: concept:open-ai-fabrics
relation: owns_platform
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: 7060XE7 被定位為同時服務 scale-up 與 scale-out 的 Ethernet 平台，不是單一標準、單一 accelerator 或排他客戶架構。
as_of: 2026-06-09
review_due: 2026-08-10
status: active
boundary: Arista 公告具名平台與用途，不等於 ESUN／SUE-T compliance、shipment、部署數或市占。
next_trigger: Arista 或客戶公布 7060XE7 對應標準、出貨、互通、部署層級與分母。
-->

<!-- knowledge_edge
edge_id: KG-FAB-C05
view: company
from_id: company:broadcom
to_id: concept:open-ai-fabrics
relation: develops_ip
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C12
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: Broadcom 提出 SUE 並貢獻 OCP；SUE-T 與 ESUN 是開放工作組的一部分，不代表 Broadcom 獨家或唯一實作。
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: SUE 架構與 OCP contribution 不等於 SUE-T 規格完成、multi-vendor compliance、客戶部署或收入。
next_trigger: OCP 與獨立廠商公布 SUE-T endpoint silicon、合規、互通與具名系統部署。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I12
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:esun
relation: includes
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C10
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-10
review_due: 2026-08-10
status: active
boundary: ESUN 1.0 已定義 Ethernet scale-up network requirements；規格不等於 endpoint／switch silicon、compliance、互通或部署。
next_trigger: OCP 公布 ESUN compliance／plugfest 與至少兩家 endpoint、switch 實體互通。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I13
view: industry
from_id: concept:open-ai-fabrics
to_id: standard:sue-t
relation: includes
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C12
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-10
status: active
boundary: OCP 現行 workstream 將 SUE-T 放在 endpoint／transport；不等於 specification、產品與互通已成熟。
next_trigger: OCP 發布 SUE-T 正式規格、測試計畫與 multi-vendor endpoint 實作。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I14
view: industry
from_id: concept:open-ai-fabrics
to_id: product:arista-7060xe7
relation: integrated_with
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C11
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: multi_source
exclusivity_scope: 7060XE7 同時定位 scale-up／scale-out，且支援多樣 accelerator；產品公告未宣稱排他標準或唯一客戶。
as_of: 2026-06-09
review_due: 2026-08-10
status: active
boundary: 產品用途不等於 ESUN／SUE-T 實作、shipment、客戶部署或 scale-up／scale-out 收入分拆。
next_trigger: Arista 或客戶公布正式標準對應、出貨與實際部署拓撲。
-->
