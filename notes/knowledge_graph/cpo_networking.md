# 光電轉換位置與兩種光學路徑知識圖譜

本圖先把交換晶片、電光轉換與光纖路徑串起來，再把平台產品生產、具名生態系角色、可插拔
共存與公司財務貢獻拆開。線條較粗只能代表已公開的角色或成熟度；沒有部署、出貨、份額與
損益證據前，不代表供應商已取得重大經濟利益。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: cpo-networking
root_node_id: concept:cpo-networking
label: 光電轉換位置與兩種光學路徑
summary: 以交換晶片到光纖的五個位置，連接 Spectrum-X 共同封裝產品、可插拔光模組、NVIDIA、SPIL 與 Lumentum，再用部署分母與財務證據阻止具名角色被誤寫成公司受惠。
article_ids: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
status: active
-->

<!-- knowledge_edge
edge_id: KG-CPO-C01
view: company
from_id: company:nvidia
to_id: concept:cpo-networking
relation: owns_platform
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-15
status: active
boundary: NVIDIA 將 Spectrum-X Ethernet Photonics 定義為進入生產；未揭露 CPO 交換器數、埠數、收入、客戶驗收或全網路占比。
next_trigger: NVIDIA 或首批採用者披露 production shipment、部署交換器數、埠數與實際可靠度／功耗結果。
-->

<!-- knowledge_edge
edge_id: KG-CPO-C02
view: company
from_id: company:3711
to_id: concept:cpo-networking
relation: platform_lists
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C3
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-01
review_due: 2026-10-31
status: active
boundary: NVIDIA 直接列名 SPIL 的 CPO chip-level packaging、assembly、testing 角色；沒有日月光公司級出貨量、收入、毛利或供應份額。
next_trigger: 日月光投控正式文件揭露 Spectrum-X／CPO 客戶、量產、產能利用與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-CPO-C03
view: company
from_id: company:lumentum
to_id: concept:cpo-networking
relation: platform_lists
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C5
note_refs:
evidence_state: verified
commercial_stage: ecosystem
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-03-18
review_due: 2026-10-31
status: active
boundary: Lumentum 自身公告 InP laser 的具名 Spectrum-X Photonics 角色；未證明 sole source、量產出貨量、份額、收入或毛利。
next_trigger: NVIDIA 與 Lumentum 對同一產品完成量產出貨雙向核對，並出現可辨識財務資料。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I01
view: industry
from_id: product:spectrum-x-ethernet-photonics
to_id: concept:cpo-networking
relation: generation_of
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-15
status: active
boundary: 產品名稱與 NVIDIA production 敘述已確認；不代表所有 Spectrum-6 form factor 都是 CPO，也不表示客戶已大規模部署。
next_trigger: 公開型號、shipment、客戶 deployment 與 CPO／pluggable 產品組合。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I02
view: industry
from_id: concept:cpo-networking
to_id: component:co-packaged-optics
relation: includes
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-15
status: active
boundary: Spectrum-X Ethernet Photonics 是具名 CPO 產品路徑；本線不推定其他交換器、連線距離或客戶也採 CPO。
next_trigger: 更多具名量產型號與實際部署位置。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I03
view: industry
from_id: concept:cpo-networking
to_id: component:pluggable-optics
relation: competes_with
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C2
note_refs:
evidence_state: inference
commercial_stage: production
materiality: named_product
exclusivity: multi_source
exclusivity_scope: NVIDIA Spectrum-6 同代 form factor 與 1.6T pluggable product path
as_of: 2026-07-21
review_due: 2026-08-15
status: active
boundary: 同代產品與可插拔量產證據支持共存推論，沒有全市場埠數或收入分母可判斷長期替代速度。
next_trigger: 平台商量化 CPO／pluggable 的型號、埠數、部署位置與資本支出占比。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I04
view: industry
from_id: concept:cpo-networking
to_id: stage:product-production
relation: reaches_stage
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C1
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-31
review_due: 2026-08-15
status: active
boundary: 生產是平台產品階段，不等於 production shipment 已量化、客戶驗收或供應商財務認列。
next_trigger: shipment、deployment 與 supplier financial evidence。
-->

<!-- knowledge_edge
edge_id: KG-CPO-I05
view: industry
from_id: concept:cpo-networking
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: SPIL 的平台列名形成封裝測試研究入口，但 C4 明確保留公司級新增訂單與財務重大性為未驗證。
next_trigger: 日月光正式文件揭露具名 CPO 量產、收入、毛利或資本回報。
-->
