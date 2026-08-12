# 面板級封裝（PLP）知識圖譜

本圖先把扇出架構、晶片先放／線路先做與方形面板載體拆開，再把面積利用率、planned line、
客戶資格與穩定量產經濟性接回同一張圖。ASE 的 310×310 mm 線是具名規劃，不是已完成 HVM。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: panel-level-packaging
root_node_id: concept:panel-level-packaging
label: 面板級封裝（PLP）
summary: 把 fan-out、chip-first／chip-last、重構面板與 SEMI 3D20 載體條件分開，再連接面積利用率、良率、產出及 ASE 310x310mm planned line，顯示製程能力為何尚不能直接推成 HVM 成本優勢。
article_ids: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS
status: active
-->

<!-- knowledge_edge
edge_id: KG-PLP-C01
view: company
from_id: company:lam-research
to_id: concept:panel-level-packaging
relation: has_capability
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C1
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Salzburg center 具 panel R&D、pilot、engineering test 與 early qualification 能力；不是具名客戶 HVM 或工具財務貢獻。
next_trigger: Lam 與具名客戶公開 panel tool qualification、HVM yield、throughput 與出貨。
-->

<!-- knowledge_edge
edge_id: KG-PLP-C02
view: company
from_id: company:applied-materials
to_id: concept:panel-level-packaging
relation: develops_packaging
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-03
review_due: 2026-08-23
status: active
boundary: Applied 已簽約收購 NEXX 以補 panel ECD，但公告日交易仍待完成；不證明整合、客戶採用、收入或份額。
next_trigger: 交易完成、NEXX 整合、具名客戶 qualification 與財務揭露。
-->

<!-- knowledge_edge
edge_id: KG-PLP-C03
view: company
from_id: company:5234
to_id: concept:panel-level-packaging
relation: develops_packaging
claim_refs:
note_refs: 5234#S1,5234#S4
evidence_state: inference
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-12
review_due: 2026-08-21
status: active
boundary: 達興材料獨立核驗筆記支持其布局 WLP／PLP 的離型層與感光介電材料，且半導體產品組合已有量產與驗證項目；公開資料未把特定料號、量產項目或收入逐一對到 panel-level packaging 客戶與 HVM 線，因此此線維持推論。
next_trigger: 達興與客戶雙向公布 PLP 具名材料、panel form factor、qualification、量產項目、出貨量及產品收入／毛利。
-->

<!-- knowledge_edge
edge_id: KG-PLP-C04
view: company
from_id: company:3711
to_id: concept:panel-level-packaging
relation: develops_packaging
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: ASE 公開 310x310mm automated line、FOCoS／FOCoS-Bridge compatibility 與 2027 expected production；不證明截至 2026-08-12 已 production release、客戶 qualification、HVM yield、出貨或財務貢獻。
next_trigger: ASE 公布同一 310x310mm platform 的實際 production release、具名客戶產品、qualification、連續良率／throughput 與可辨識財務結果。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I01
view: industry
from_id: concept:panel-level-packaging
to_id: component:panel-substrate
relation: uses_component
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: 方形或長方形 panel 是製程載體，不代表特定尺寸、材料或供應商已成標準或量產。
next_trigger: 客戶產品公開 panel 長寬、厚度、材料與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I02
view: industry
from_id: concept:panel-level-packaging
to_id: metric:area-utilization
relation: measured_by
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 面積利用率是幾何分子之一，不能單獨證明每個合格封裝成本較低。
next_trigger: 同一產品在 wafer／panel 路徑的可排數、good-package yield、cycle time 與成本。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I03
view: industry
from_id: concept:panel-level-packaging
to_id: capability:uniformity-control
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Lam 明列大面積 uniformity 為挑戰；沒有客戶線分布、規格與良率資料可判定問題已解決。
next_trigger: 具名 panel process 的 across-panel uniformity 與 yield correlation。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I04
view: industry
from_id: concept:panel-level-packaging
to_id: capability:yield-management
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 良率是單位成本必要分母，但本輪沒有具名產品 good-package yield 或報廢成本。
next_trigger: 客戶披露一致定義的 panel good-package yield、可靠度與成本。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I05
view: industry
from_id: concept:panel-level-packaging
to_id: metric:panel-throughput
relation: measured_by
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C4
note_refs:
evidence_state: inference
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-08-23
status: active
boundary: 大 panel 的理論輸出必須扣除 cycle time 與設備利用率；現有來源沒有可比 throughput 數字。
next_trigger: 具名工具在客戶線的 panels per hour、cycle time 與 uptime。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I06
view: industry
from_id: concept:panel-level-packaging
to_id: standard:panel-size
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C2,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-06-25
review_due: 2026-08-23
status: active
boundary: Lam 明示 ecosystem 仍在決定 panel size，Applied 的 510x515mm or more 只是能力／路線敘述，不是統一標準。
next_trigger: OSAT、設備、材料與基板供應鏈採用可核對的共同 form factor。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I07
view: industry
from_id: concept:panel-level-packaging
to_id: process:panel-ecd
relation: includes
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C3
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-05-03
review_due: 2026-08-23
status: active
boundary: NEXX 具 large-area panel ECD 技術且交易簽約；交易完成、客戶 qualification 與量產收入仍未證。
next_trigger: Acquisition closing、產品整合、具名客戶出貨與財務貢獻。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I08
view: industry
from_id: concept:panel-level-packaging
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: OSAT 是 process integration 搜尋路由，沒有 universe 公司具名 panel HVM 與財務證據。
next_trigger: OSAT 與客戶雙向確認 panel form factor、qualification、量產與財務。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I09
view: industry
from_id: concept:panel-level-packaging
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: 多種 panel tool 形成設備搜尋路由，不證明台灣設備商能處理目標尺寸或已通過客戶量產資格。
next_trigger: 具名工具、panel size、客戶 qualification、量產出貨與收入。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I10
view: industry
from_id: concept:panel-level-packaging
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C5
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-02
review_due: 2026-10-31
status: active
boundary: 大型基板與 form factor 是 PCB／載板研究入口，沒有 universe 公司具名 PLP 客戶、qualification 或財務證據。
next_trigger: 基板商與客戶對同一 panel product、尺寸、量產與財務雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I11
view: industry
from_id: concept:panel-level-packaging
to_id: concept:fan-out-packaging
relation: includes
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Fan-out 是 PLP 常見封裝架構，但 SEMI 只說 many applications include fan-out；不能把所有 PLP 都定義成 fan-out，也不能把 fan-out 自動等同 panel form factor。
next_trigger: 具名產品同時公開 fan-out architecture、carrier format、process flow 與 qualification。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I12
view: industry
from_id: concept:panel-level-packaging
to_id: process:chip-first-fan-out
relation: includes
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Chip-first 指先放置／包封晶粒再形成 RDL 的先後順序；它不指定唯一 panel size，也不證明 die shift、warpage、yield 或 cost 已達量產要求。
next_trigger: 同一 chip-first panel product 公布 die-shift distribution、RDL alignment、good-package yield 與 customer release。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I13
view: industry
from_id: concept:panel-level-packaging
to_id: process:chip-last-fan-out
relation: includes
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Chip-last／RDL-first 指先形成 RDL 再接合晶粒；降低 RDL 製作期間的 die-shift 問題不等於接合、封裝後良率、可靠度或成本已通過。
next_trigger: 同一 chip-last panel product 公布 RDL yield、die attach／mold result、customer qualification 與 HVM output。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I14
view: industry
from_id: concept:panel-level-packaging
to_id: component:reconstituted-panel
relation: uses_component
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: 重構面板是把 singulated dies 重新排列並固定後供批次加工的中間載體；它不一定留在最終 package，也不能替 package substrate 或 customer product 身分。
next_trigger: 具名產品公開 carrier／mold stack、release、RDL、singulation 與 final package cross-section。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I15
view: industry
from_id: concept:panel-level-packaging
to_id: component:fine-pitch-rdl
relation: uses_component
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6,MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C7
note_refs:
evidence_state: verified
commercial_stage: capability
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: Fraunhofer 與 ASE 都把 RDL 放在 fan-out 核心，ASE 並列出自家 platform line-space；單一 L/S 數字不證明跨面板 uniformity、yield、reliability 或 production release。
next_trigger: 同一 panel product 公布 RDL stack、across-panel distribution、defect／yield correlation 與 customer qualification。
-->

<!-- knowledge_edge
edge_id: KG-PLP-I16
view: industry
from_id: concept:panel-level-packaging
to_id: standard:semi-3d20-panel-characteristics
relation: requires
claim_refs: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS#C6
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-09-12
status: active
boundary: SEMI 3D20 公開摘要界定外形、厚度、翹曲、重量與有無 process carrier；標準存在不代表單一尺寸已統一、設備互通已驗證或產品已量產。
next_trigger: OSAT、設備與材料鏈對同一 panel format 公開 carrier spec、FOUP／loadport compatibility 與 production qualification。
-->
