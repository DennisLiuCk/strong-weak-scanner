# 混合接合（Hybrid bonding）知識圖譜

本圖把成熟度拆成應用、W2W／D2W 接法、介面世代與具名產品階段：Sony 影像感測器、TSMC SoIC
與 AMD 3D V-Cache 提供已應用或 production 格；200nm 試驗結構與 pathfinding PDK 則保留在各自
早期格。台灣族群只保留研究路由，沒有公司量產線。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: hybrid-bonding
root_node_id: concept:hybrid-bonding
label: 混合接合（Hybrid bonding）
summary: 連接 Sony 影像感測器、TSMC SoIC 與 AMD 3D V-Cache 的既有應用／production 證據，再分開逐顆接晶圓、晶圓接晶圓、探索型設計規則、200nm 試驗結構、對準控制與平坦化；任何成熟格都不能替其他應用、接法或介面世代繼承資格。
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
edge_id: KG-HYB-C03
view: company
from_id: company:sony-semiconductor
to_id: concept:hybrid-bonding
relation: uses_packaging
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2024-04-22
review_due: 2026-08-19
status: active
boundary: Sony 官方技術回顧把 Cu-Cu hybrid bonding 放入 2015 stacked BI-CIS 與後續產品功能演進；未公開各代流程、良率、throughput、成本或供應商份額。
next_trigger: Sony 對具名產品世代補充 W2W／D2W、pitch、合格產出、可靠度與量產分母。
-->

<!-- knowledge_edge
edge_id: KG-HYB-C04
view: company
from_id: company:tsmc
to_id: concept:hybrid-bonding
relation: owns_platform
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2022-06-17
review_due: 2026-08-19
status: active
boundary: TSMC 表示 N7 SoIC CoW／WoW chips 已在 production 並列出 CPU＋SRAM 與 IPU＋DTC 應用；沒有逐產品良率、throughput、成本、利用率或財務分子。
next_trigger: TSMC 固定產品、接法與節點後披露 qualification、合格產出、產能利用或可定位財務分母。
-->

<!-- knowledge_edge
edge_id: KG-HYB-C05
view: company
from_id: company:amd
to_id: concept:hybrid-bonding
relation: uses_packaging
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2022-03-21
review_due: 2026-08-19
status: active
boundary: AMD 把 EPYC 7003 3D V-Cache 商用處理器描述為 copper-to-copper hybrid bonding bumpless design；不採用公司效能倍數，也未取得接合良率、成本或供應商分子。
next_trigger: AMD 對具名世代補充製造資格、接合介面、出貨分母或供應鏈雙向核對。
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
boundary: 本邊只描述 NanoIC／Kinex 這組新 D2W 格已有 pathfinding PDK 與整合設備客戶使用；AMD／N7 CoW 的既有 production 格不能替它完成 tape-out 或 HVM。
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
boundary: 本邊只描述 imec 200nm W2W 試驗車；TSMC N7 WoW production 格不能讓不同 pitch 與產品的試驗車自動取得客戶 HVM electrical yield。
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

<!-- knowledge_edge
edge_id: KG-HYB-I10
view: industry
from_id: concept:hybrid-bonding
to_id: product:stacked-cmos-image-sensor
relation: names_application
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: deployment
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2024-04-22
review_due: 2026-08-19
status: active
boundary: Sony 技術回顧證明 stacked CIS 是較早混合接合應用家族；不同感測器世代、材料與多層流程仍須逐格判定。
next_trigger: 具名感測器世代對上接法、pitch、qualification、良率與出貨分母。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I11
view: industry
from_id: concept:hybrid-bonding
to_id: product:tsmc-soic
relation: names_application
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2022-06-17
review_due: 2026-08-19
status: active
boundary: N7 SoIC CoW／WoW 有 production 聲明；SoIC 平台內其他節點、接法與 bond pitch 不沿用同一成熟度。
next_trigger: 各 SoIC 世代固定產品、接法與介面後公開 qualification、良率、throughput 或成本。
-->

<!-- knowledge_edge
edge_id: KG-HYB-I12
view: industry
from_id: concept:hybrid-bonding
to_id: product:amd-3d-v-cache
relation: names_application
claim_refs: MI-2026-08-02-HYBRID-BONDING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2022-03-21
review_due: 2026-08-19
status: active
boundary: EPYC 7003 3D V-Cache 是具名商用 hybrid-bond product family；不代表其他 CPU、GPU、HBM 或細間距試驗格相同成熟。
next_trigger: AMD 或製造端對同一產品世代補充接合資格、產量、良率或財務分母。
-->
