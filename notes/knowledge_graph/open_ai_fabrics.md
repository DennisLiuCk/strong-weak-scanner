# AI 資料路徑與跨廠互通知識圖譜

本圖用兩條軸閱讀開放人工智慧網路：先分清加速器機架內、跨機架、服務／處理器、儲存、
帶內與帶外管理六種網路工作，再分開實體、端點、交換、軟體、管理、單件合規、跨廠互通、
系統與部署契約。共同使用 Ethernet 或同一設備不會合併責任，也不能相加成已部署收入。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: open-ai-fabrics
root_node_id: concept:open-ai-fabrics
label: AI 資料路徑與跨廠互通
summary: 先固定加速器機架內、跨機架、服務／處理器、儲存、帶內與帶外管理六種網路工作，再把實體、端點、交換、軟體、管理、單件合規、跨廠互通、系統壓力與客戶部署逐層驗收，並用十欄 collective 效能護照分開 line rate、payload、algbw、busbw 與訓練結果。
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

<!-- knowledge_edge
edge_id: KG-FAB-I15
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-network-plane-map
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C18
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 六種網路工作是 OCP 現行範圍與一套 OPG-M 參考架構支持的閱讀框架；不表示所有叢集都有六套獨立實體設備或相同拓撲。
next_trigger: 更多具名參考架構或客戶部署公開網路平面、是否匯聚、BOM、冗餘與驗收結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I16
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-front-end-network
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OCP 現行範圍列出 front-end，OPG-M 以 SO-C 與帶內管理分工；這不證明所有叢集用相同實體網路或設備。
next_trigger: 具名系統公開前端／SO-C 拓撲、流量、交換器、軟體、故障與驗收分母。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I17
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-storage-network
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OCP 範圍與 OPG-M 參考設計把 storage network 分開；不證明特定儲存平台、吞吐、部署或供應商收入。
next_trigger: 具名叢集公開儲存工作、拓撲、容量／吞吐、故障恢復、利用率與客戶驗收。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I18
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-in-band-management-network
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OPG-M 把 in-band management 列為獨立網路；管理可達不等於資料平面、故障救援或客戶部署已驗收。
next_trigger: 具名系統公開帶內管理的設備發現、設定、遙測、漂移、故障與恢復結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I19
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-out-of-band-management-network
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OPG-M 把 out-of-band management 列為獨立網路；救援通道存在不等於主資料網具冗餘或生產工作不會中斷。
next_trigger: 具名部署公開帶外管理拓撲、隔離、權限、失聯情境、重置與維修時間。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I20
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-fabric-stack-contract
relation: contains
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C16,MI-2026-08-02-OPEN-AI-FABRICS#C18
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 八層契約是把 UALink／UEC／OCP 的分工與驗收邊界投影成統一閱讀框架，不是官方共同認證等級或效能排名。
next_trigger: 各組織發布完整測試架構，或具名產品結果顯示需要合併、拆分或重排驗收層。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I21
view: industry
from_id: concept:open-ai-fabrics
to_id: stage:compliance-self-attestation
relation: passes_through
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C17
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: UEC 已公開自我聲明、checklist 與測試床工具入口；另頁會員聲明是必要專利權利登錄，沒有具名產品聲明／通過或第三方認證清單，且不能替代跨廠互通。
next_trigger: UEC 公開具名產品、版本、已填 checklist、測項與結果，並說明自我聲明或第三方驗證責任。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I22
view: industry
from_id: concept:open-ai-fabrics
to_id: stage:system-stress-validation
relation: passes_through
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C17,MI-2026-08-02-OPEN-AI-FABRICS#C19
note_refs:
evidence_state: unverified
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-19
status: active
boundary: UEC 測試床文件明示 system stress／scale 與 performance 不在範圍；本輪沒有具名產品或系統已通過的公開結果。
next_trigger: 公開端點與機架數、版本、拓撲、負載、期間、故障、效能、恢復與通過條件的具名系統報告。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I23
view: industry
from_id: concept:open-ai-fabrics
to_id: capability:fabric-lifecycle-management
relation: requires
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C16,MI-2026-08-02-OPEN-AI-FABRICS#C18
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OCP／UEC 將管理、遙測、除錯、生命週期與設定漂移列為責任範圍；這不證明特定工具已部署或產生收入。
next_trigger: 具名系統公開設備上線、設定、更新、漂移偵測、告警、替換與退役的版本化結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I24
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-storage-data-plane
relation: integrated_with
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C15
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: OCP 把 storage network 列為人工智慧叢集的一張網，只建立與資料讀取／儲存路徑的概念連接，不證明具名產品、容量或部署。
next_trigger: 具名叢集同時公開訓練資料、檢查點、模型搬運的網路拓撲、工作負載與驗收結果。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I25
view: industry
from_id: concept:open-ai-fabrics
to_id: concept:ai-rack-action-contract
relation: integrated_with
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C14,MI-2026-08-02-OPEN-AI-FABRICS#C18
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 管理網路與生命週期責任需要身分、資料語意、動作所有權及維修閉環；這是跨文章推論，不是已部署的共同標準。
next_trigger: OCP、UEC 或具名平台公開跨設備管理資料、控制動作、安全裁決、隔離與維修結果的共同契約。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I26
view: industry
from_id: concept:open-ai-fabrics
to_id: process:ai-collective-performance-passport
relation: requires
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C21,MI-2026-08-02-OPEN-AI-FABRICS#C22,MI-2026-08-02-OPEN-AI-FABRICS#C23
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-19
status: active
boundary: 十欄護照是研究中心整合 UEC compliance 邊界、NCCL collective microbenchmark 與 MLCommons training outcome 的比較框架，不是共同標準、產品 pass、跨廠互通或客戶部署。
next_trigger: 同一具名 AI workload 公開完整十欄、collective event 分布、wire counters、故障、wall-clock-to-quality、資源成本與設備版本。
-->

<!-- knowledge_edge
edge_id: KG-FAB-I27
view: industry
from_id: concept:open-ai-fabrics
to_id: metric:collective-algorithm-bus-bandwidth-contract
relation: measured_by
claim_refs: MI-2026-08-02-OPEN-AI-FABRICS#C20,MI-2026-08-02-OPEN-AI-FABRICS#C21,MI-2026-08-02-OPEN-AI-FABRICS#C22
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-19
status: active
boundary: algbw 是 S／t，busbw 是依 collective 與 ranks 衍生的正規化；兩者不是獨立 payload、不得相加，也不能在缺 algorithm／topology／offload 條件時冒充 wire bandwidth。
next_trigger: 具名系統同時公開 message／time、algbw／busbw 公式、實測 port／link counters、algorithm、topology、tail 與 end-to-end step 結果。
-->
