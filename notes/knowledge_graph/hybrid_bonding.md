# 混合接合（Hybrid bonding）知識圖譜

本圖用設計規則、試驗結構、整合設備與穩定大量生產缺口呈現成熟度，不以最小接點間距取代
良率、每小時產能與客戶資格認證。台灣族群只保留研究路由，沒有公司量產線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hybrid-bonding
root_node_id: concept:hybrid-bonding
label: 混合接合（Hybrid bonding）
summary: 連接逐顆接晶圓與晶圓接晶圓、探索型設計規則、200nm 試驗結構、對準控制、平坦化與具名設備，同時把穩定大量生產與台灣財務映射留在待驗證層。
article_ids: MI-2026-08-02-HYBRID-BONDING-READINESS
status: active
-->

<!-- knowledge_edge
edge_id: KG-HYB-C01
view: company
from_id: company:ev-group
to_id: concept:hybrid-bonding
relation: provides_tooling
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-28
review_due: 2026-08-16
status: active
boundary: EVG GEMINI FB 參與 imec 200nm W2W 試驗車與 overlay 結果；不證明具名量產客戶、設備份額、出貨或財務貢獻。
next_trigger: EVG 與客戶公開具名 HVM qualification、throughput、量產出貨與可靠度。
-->

<!-- knowledge_edge
edge_id: KG-HYB-C02
view: company
from_id: company:applied-materials
to_id: concept:hybrid-bonding
relation: provides_tooling
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2025-10-07
review_due: 2026-08-16
status: active
boundary: Kinex 是具名整合 D2W 工具且公司稱多類客戶使用；未揭露客戶、qualification、HVM yield、出貨量或收入。
next_trigger: Applied／Besi 與具名客戶雙向確認 HVM qualification、出貨及財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I01
view: industry
from_id: concept:hybrid-bonding
to_id: process:die-to-wafer-hybrid-bonding
relation: includes
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C1,MI-2026-08-02-HYBRID-BONDING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-02
review_due: 2026-08-16
status: active
boundary: D2W 路徑已有 pathfinding PDK 與整合設備客戶使用，仍不等於 fabrication-ready tape-out 或具名產品 HVM。
next_trigger: 完整 tape-out、客戶 qualification、good-die yield 與 throughput。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I02
view: industry
from_id: concept:hybrid-bonding
to_id: process:wafer-to-wafer-hybrid-bonding
relation: includes
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-28
review_due: 2026-08-16
status: active
boundary: W2W 已在 imec 200nm 試驗車展示，不可把試驗車 overlay 結果寫成客戶 HVM electrical yield。
next_trigger: 具名 logic-to-logic 或 memory-to-logic 產品 qualification 與 HVM 資料。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I03
view: industry
from_id: concept:hybrid-bonding
to_id: stage:pathfinding-pdk
relation: passes_through
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C1
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-03-02
review_due: 2026-08-16
status: active
boundary: NanoIC 第一版明確是 exploratory／pathfinding；不能視為完整製造套件或量產設計生態。
next_trigger: PDK 進入 fabrication-ready tape-out 並產出實體 silicon。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I04
view: industry
from_id: concept:hybrid-bonding
to_id: stage:test-vehicle
relation: passes_through
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-28
review_due: 2026-08-16
status: active
boundary: 200nm 結果出自 routable test vehicle；不是客戶最終商品、產能或成本資料。
next_trigger: 從 test vehicle 進入具名 product qualification 的一手證據。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I05
view: industry
from_id: concept:hybrid-bonding
to_id: capability:overlay-control
relation: requires
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-28
review_due: 2026-08-16
status: active
boundary: Sub-40nm overlay 是指定試驗車結果與關鍵能力，不證明量產設備長期分布、良率或同業工具性能。
next_trigger: 客戶線 overlay distribution、drift control 與 HVM yield correlation。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I06
view: industry
from_id: concept:hybrid-bonding
to_id: process:cmp-planarization
relation: requires
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-28
review_due: 2026-08-16
status: active
boundary: imec 試驗流程需要 CMP 控制平坦度與 Cu recess；技術需要不等於台灣 CMP 工具或耗材公司已供貨。
next_trigger: 客戶與供應商對同一量產 CMP step、qualification 與財務貢獻雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I07
view: industry
from_id: concept:hybrid-bonding
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: 封裝、known-good-die 與接合後檢查形成研究入口，沒有 universe OSAT 具名量產與財務證據。
next_trigger: OSAT 與客戶雙向確認具名 hybrid bonding 產品、qualification、出貨與財務。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I08
view: industry
from_id: concept:hybrid-bonding
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: Bonding、CMP、clean、overlay 與 inspection 是設備搜尋路由，不代表 universe 設備商已進客戶量產線。
next_trigger: 具名工具、客戶 qualification、量產出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I09
view: industry
from_id: concept:hybrid-bonding
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: SiCN、Cu、清洗化學品與 CMP 耗材是材料入口；沒有台灣公司具名料號、qualification、份額或財務證據。
next_trigger: 材料商與客戶對同一量產製程完成雙向核對。
-->
