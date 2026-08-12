# Vera Rubin 七關交付與整櫃責任知識圖譜

本圖把 NVIDIA 平台、營運商驗證、雲端供應語言與三家台灣系統廠的公開角色接回同一張圖，
再把平台生產、系統就緒、工廠生產、整櫃驗證、站點驗收、工作負載與財務歸因逐關分開。
圖中的族群線是下一份證據的搜尋入口；除具名系統廠角色外，不代表台灣供應商已取得訂單或獲利。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: vera-rubin-delivery-contract
root_node_id: product:nvidia-vera-rubin-nvl72
label: Vera Rubin 七關交付與整櫃責任
summary: 用五欄證據表辨認發布者 物件 成熟度動詞 範圍日期與下一份裁決證據，再把 NVIDIA Vera Rubin 從平台生產追到整櫃責任 站點交付 工作負載與供應商財務歸因。
article_ids: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP
status: active
-->

<!-- knowledge_edge
edge_id: KG-VRD-C01
view: company
from_id: company:nvidia
to_id: product:nvidia-vera-rubin-nvl72
relation: owns_platform
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C1,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: NVIDIA 的量產與平台組成敘述只證明自身產品階段，不證明每家系統廠已生產 客戶已驗收或台灣供應商已有財務貢獻。
next_trigger: NVIDIA 公布有版本的 configuration matrix 實際出貨 客戶站點驗收與可對時部署量。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C02
view: company
from_id: company:coreweave
to_id: product:nvidia-vera-rubin-nvl72
relation: tests
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C6
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-01
review_due: 2026-08-15
status: active
boundary: CoreWeave 自述完成單一整櫃 bring-up 與 system-level validation，沒有測試母體 長時間 workload 跨站點複製或客戶 acceptance。
next_trigger: CoreWeave 公布固定組態 測項 測試時間 機架數 站點與 production workload 結果。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C03
view: company
from_id: company:google
to_id: product:nvidia-vera-rubin-nvl72
relation: integrates
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C7
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-22
review_due: 2026-08-15
status: active
boundary: Google CEO remarks 只證明 Google Cloud 的 offer 語言，沒有 SKU 地區 preview或GA 容量 利用率 工作負載或系統供應商。
next_trigger: Google Cloud 發布可取得的 Vera Rubin SKU 區域 配額 上線日期與 workload 邊界。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C04
view: company
from_id: company:2376
to_id: product:nvidia-vera-rubin-nvl72
relation: integrates
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C4,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 技嘉被 NVIDIA 列名且型錄列出 NVL72 240 kW power shelf 與 in-row CDU，不等於可下單 實際生產 出貨 客戶驗收或收入。
next_trigger: 技嘉以具名 SKU 交期 生產出貨 客戶驗收與財務分母推進型錄角色。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C05
view: company
from_id: company:2382
to_id: product:nvidia-vera-rubin-nvl72
relation: platform_lists
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C4
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-15
status: active
boundary: QCT 被平台商列為系統夥伴只證明公開角色，不等於廣達取得新訂單 量產份額 收入 毛利或現金回收。
next_trigger: 廣達或客戶文件以同一 Rubin 產品與期間確認資格 生產 出貨 驗收及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C06
view: company
from_id: company:3231
to_id: product:nvidia-vera-rubin-nvl72
relation: plans_production
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C8
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-21
review_due: 2026-08-15
status: active
boundary: 緯創文件說 Texas D1 當時生產 GB300 且未來接 Rubin，不能把未來式改寫成 Rubin 已在該廠量產或形成收入。
next_trigger: 緯創確認 Rubin 在具名工廠開始實際生產並提供出貨 驗收與財務期間。
-->

<!-- knowledge_edge
edge_id: KG-VRD-C07
view: company
from_id: company:6669
to_id: product:nvidia-vera-rubin-nvl72
relation: has_capability
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C10
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 緯穎自述 production-ready rack 與 L12 驗證能力，不披露實際 Rubin 機架出貨 客戶 acceptance 數量 收入或毛利。
next_trigger: 緯穎以固定組態與具名客戶揭露 Rubin 資格 出貨 驗收及可重算財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I01
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-platform-production
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-27
review_due: 2026-08-15
status: active
boundary: 平台商的 production 或 ramp 不提供各 ODM 工廠數量 良率 出貨與收入。
next_trigger: 平台與系統廠以同一配置及期間公布實際生產和出貨分母。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I02
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-system-ready
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C10
note_refs:
evidence_state: verified
commercial_stage: platform_listing
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 型錄配置與 production-ready 能力回答公開設計狀態，不回答 orderability 交期 實際產量或客戶驗收。
next_trigger: 系統廠發布有版本 SKU configuration lock 訂購條件與 factory build 狀態。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I03
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-factory-production
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C8
note_refs:
evidence_state: unverified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現有緯創文件明確把當前 GB300 生產與未來 Rubin 分開，尚無台灣系統廠可核對的 Rubin factory build。
next_trigger: 具名工廠確認固定 Rubin 組態已開始製造並提供日期與可驗證產量邊界。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I04
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-rack-validation
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C6
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-01
review_due: 2026-08-15
status: active
boundary: CoreWeave 的單一營運商整櫃驗證不等於跨廠組態資格 長時間可靠度 站點 commissioning 或客戶簽收。
next_trigger: 公開固定組態 測試計畫 通過門檻 機架母體 長時間結果與異常處置。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I05
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-site-acceptance
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C11
note_refs:
evidence_state: unverified
commercial_stage: deployment
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現有來源沒有台灣系統廠具名站點的電力 冷卻 網路 commissioning acceptance 日期或簽收母體。
next_trigger: 客戶與系統廠共同留下同一站點 組態 測項 通過條件 驗收日期與機架數。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I06
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-cloud-workload
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C7,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C11
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Google 的 offer 語言接近服務端但沒有 SKU 地區 GA 容量 利用率 SLO 或持續 workload，不能直接寫成全面可用。
next_trigger: 雲端商公布具名 SKU 區域 可取得日期 配額 工作負載與服務結果。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I07
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: stage:vera-rubin-financial-attribution
relation: reaches_stage
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C11
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 沒有資料把 Rubin 專屬數量 單價 成本 驗收期間連到台灣公司收入 毛利 存貨或現金流。
next_trigger: 買方與供應商用同一平台 產品 期間 數量 驗收及財務分母完成雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I08
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: concept:ai-memory-hierarchy
relation: requires
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 平台頁證明整櫃運算責任存在，但沒有把 HBM CPU memory context 與持久儲存的同一 workload 容量 頻寬 延遲及資料放置合約完整公開。
next_trigger: 版本化系統文件以同一 workload 固定各記憶體與儲存層的資料 容量 頻寬 延遲及錯誤處理。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I09
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: concept:open-ai-fabrics
relation: requires
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: NVIDIA 列出 NVLink 與 Spectrum-X或Quantum-X 只證明 scale-up 與 scale-out 路徑，不證明開放標準合規 跨廠互通或部署壓力測試。
next_trigger: 有版本的拓樸與測試矩陣把實體 端點 交換 軟體 管理 互通及系統壓力逐層驗收。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I10
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: concept:liquid-cooling-loop-boundary
relation: requires
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 液冷 CPU 與型錄 in-row CDU 不等於 FWS TCS ITE 的水質 流量 壓差 漏液 控制 維護及場站交接已閉合。
next_trigger: 同一站點公開 CDU 設施水路 二次水路 ITE 控制責任 commissioning 與 acceptance 結果。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I11
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: concept:ai-storage-data-plane
relation: requires
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: inference
commercial_stage: integration
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: BlueField storage 角色只證明儲存是平台責任之一，沒有公開 dataset fetch checkpoint persistence 與 model distribution 的同負載 throughput tail latency recovery 結果。
next_trigger: 客戶以同一組態與工作負載公布三條資料路徑的流量 延遲 重啟復原及瓶頸。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I12
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: capability:rack-lifecycle-control
relation: requires
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C6,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C10
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: rack control 與 L12 能力敘述未提供跨硬體 韌體 驅動 軟體版本 更新回退 故障隔離及維修復原的完整契約。
next_trigger: 營運商公開版本基線 遙測 動作所有權 更新回退 故障注入 更換與恢復測試。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I13
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: group:memory
relation: routes_to
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C12
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 記憶體只是系統責任與後續搜尋路由；韓國 HBM 合作不能替台灣 memory 公司證明 Rubin qualification 訂單或獲利。
next_trigger: 平台與台灣公司對上同一記憶體料號 客戶資格 出貨期間 收入 毛利與現金。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I14
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 高速互連只形成 PCB 研究入口；沒有具名板件 stackup 材料 qualification 份額 數量 單價或財務證據。
next_trigger: 平台與 PCB 公司共同確認同一板件 材料 測項 資格 出貨與財務分母。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I15
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 240 kW 與 power shelf 是系統配置，不是任何台灣電源公司具名 BOM qualification 出貨 收入或毛利。
next_trigger: 平台與電源公司用同一 PSU或power shelf 型號 規格 資格 數量 期間及財務分母雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I16
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: group:serverodm
relation: routes_to
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C4,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C10
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 具名夥伴 型錄與能力使 server ODM 成為可證實研究路由，但仍不表示四家公司都已量產 出貨 驗收或取得財務利益。
next_trigger: 各公司分別用具名 Rubin 產品 期間 數量 驗收 收入 毛利 存貨與現金完成歸因。
-->

<!-- knowledge_edge
edge_id: KG-VRD-I17
view: industry
from_id: product:nvidia-vera-rubin-nvl72
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C5,MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP#C9
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 液冷與 in-row CDU 只形成散熱研究入口；沒有 universe 公司具名冷板 CDU QD 水路資格 出貨或財務分母。
next_trigger: 平台 客戶與散熱公司用同一冷卻組態 資格 驗收 數量 期間 收入及毛利雙向核對。
-->
