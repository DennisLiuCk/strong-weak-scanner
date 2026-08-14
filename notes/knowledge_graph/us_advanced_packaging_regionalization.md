# 美國先進封裝區域化九關橋接知識圖譜

本圖把 CHIPS 獎勵、補助撥付、客戶預付款、公司資本投入、廠房與工具、製程與客戶資格、
量產利用及財務歸因分開。線條只表示下一個應驗證的責任節點；未走完後半段前，不把美國
擴產寫成台灣訂單流失，也不把政府、客戶與公司的不同金流相加。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: us-advanced-packaging-regionalization
root_node_id: concept:us-advanced-packaging-regionalization
label: 美國先進封裝區域化九關橋接
summary: 從 CHIPS award scope 與里程碑撥付，經專案資本結構 建築 工具 製程與客戶資格，到量產利用 損平 滿載 財務歸因及台美替代驗證，保留 project phase facility 版本與 reference plane。
article_ids: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION
status: active
-->

<!-- knowledge_edge
edge_id: KG-UAP-C01
view: company
from_id: company:amkor
to_id: concept:us-advanced-packaging-regionalization
relation: plans_production
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C16,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C12,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C13
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: Amkor 的兩期 campus 與 2025 至 2030 invest ramp break-even full-utilization 時鐘是管理規劃；Phase 1 full-scale 指標不等於現況，NIST award-project 又屬另一 scope，均不是完成工具 資格 量產或獲利的證據。
next_trigger: Amkor 以 project phase facility ID 調節 award scope 擴大 campus 建設 工具 資格 實際產出 利用率 損平 滿載與財務。
-->

<!-- knowledge_edge
edge_id: KG-UAP-C02
view: company
from_id: company:nvidia
to_id: concept:us-advanced-packaging-regionalization
relation: planned_customer
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C1
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 約 15 億美元多年期協議與 2027 年客戶預付款預期不等於已付款 已履約 保底量 客戶產品資格或 Amkor 已認列收入。
next_trigger: NVIDIA 與 Amkor 對上同一產品 facility qualification release 預付款收取與服務收入期間。
-->

<!-- knowledge_edge
edge_id: KG-UAP-C03
view: company
from_id: company:tsmc
to_id: concept:us-advanced-packaging-regionalization
relation: planned_customer
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C16
note_refs:
evidence_state: inference
commercial_stage: planned
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 十年採購框架只證明規劃合作，沒有最低量 價格 排他性 產品資格 利用率或毛利；也不能用框架替 NIST 與 Amkor 的 project-version 差異背書。
next_trigger: TSMC 與 Amkor 公布具名封裝技術 產品資格 最低量 facility release 及可核對量產服務。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I01
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:chips-award-scope
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C5
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: NIST 現行頁與 final award 固定最高 4.07 億美元及當時 project 口徑；不等於擴大後 70 億美元兩期 campus 全部符合 award 或已撥款。
next_trigger: NIST 公布 versioned award amendment 並對上 Amkor 的 project phase facility。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I02
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:milestone-disbursement
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C5
note_refs:
evidence_state: verified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 已驗證的是 construction technology production commercial 四類里程碑撥付機制，不是任何一類已完成 請領 核准或收到現金。
next_trigger: NIST 或 Amkor 公布各里程碑日期 達成條件 核准額與 cash receipt。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I03
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-project-capital-stack
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C16
note_refs:
evidence_state: inference
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 4.07 億美元補助上限 15 億美元預付款 25 至 30 億美元公司級年度 CapEx 與 70 億美元 campus 計畫分屬不同 payer recipient period scope 及會計欄位，不能加總或互相代替。
next_trigger: Amkor 發布同一 project phase period 的 grant prepayment own funds debt tax credit CapEx 與 contract-liability reconciliation。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I04
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-site-construction
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C16
note_refs:
evidence_state: inference
commercial_stage: deployment
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 動土與 2027 年中第一座設施完成規劃不等於建築 水電 無塵室已驗收，也不等於工具已可安裝或製程已啟用。
next_trigger: 公司或政府固定 facility ID 公布 construction completion utilities cleanroom ready 與正式驗收日期。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I05
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-tool-process-enablement
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: deployment
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現有來源沒有同一 facility 的具名工具 move-in hook-up 工程批次或封裝流程整合，不能從 CapEx 或建築時程推定設備商 設備數或產線可用。
next_trigger: Amkor 或供應商雙向揭露具名工具 facility installation 工程批次與 process enablement 結果。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I06
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-process-qualification
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: qualification
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: NIST 的 technology milestone 是撥付類別，不是已完成製程資格；沒有固定產品 樣本 良率 可靠度 失效與放行門檻。
next_trigger: 具名製程在同一 facility 公布 qualification protocol sample yield reliability failure criteria 與 release。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I07
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-customer-product-qualification
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C7
note_refs:
evidence_state: unverified
commercial_stage: validation
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: NVIDIA 協議與 TSMC 採購框架都沒有證明具名產品已完成 customer qualification change approval 或量產 release。
next_trigger: 客戶與 Amkor 雙向確認產品 封裝 facility qualification completion 與 production release。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I08
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-capacity-ramp-utilization
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C7,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C12
note_refs:
evidence_state: unverified
commercial_stage: production
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: 每月 14,500 片晶圓與 370 萬顆 units 是 award-project 預期產出且 reference plane 不同；2028 至 2029 ramp 與 2030 estimated full utilization 也是公司目標，沒有 actual start product mix utilization yield qualified output 或持續交付。
next_trigger: 同一 facility 與期間公布名目產能 實際 start 產品組合 投入 合格產出 利用率 良率 客戶放行與相對 2030 目標的差異。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I09
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: stage:regional-packaging-financial-attribution
relation: passes_through
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C7,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C12,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C13
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: unknown
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: 補助 預付款 CapEx 框架 Phase 1 full-scale 約 10 億美元收入與超過 30% 毛利目標都不是 Arizona 當期封裝服務收入 毛利或現金，也沒有台美同產品 客戶 期間的替代或互補調節。
next_trigger: Amkor 與台灣公司以同一 facility 產品 客戶 期間揭露收入 成本 毛利 現金 訂單 利用率 損平與滿載實績。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I10
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: group:packtest
relation: routes_to
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C3,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C14,MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C15
note_refs:
evidence_state: unverified
commercial_stage: planned
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-14
review_due: 2026-08-15
status: active
boundary: Amkor Arizona 與 3711 高雄 FOCoS FC BGA 文件支持兩地同時規劃新增能力；兩份公司規劃不是同產品 qualification 訂單 利用率或毛利，也不證明 3711 已取得 失去或保留訂單。
next_trigger: Amkor 客戶與 3711 文件對上同一產品 qualification 客戶 期間 合格產出 訂單 利用率 毛利與可重算財務影響。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I11
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: group:semiequip
relation: routes_to
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C3
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 公司級 CapEx 與建廠只形成設備搜尋路由，沒有具名 universe 工具 facility move-in 採購額 驗收 收入或毛利。
next_trigger: Amkor 與設備商雙向對上同一工具 facility installation acceptance shipment revenue 與毛利期間。
-->

<!-- knowledge_edge
edge_id: KG-UAP-I12
view: industry
from_id: concept:us-advanced-packaging-regionalization
to_id: group:material
relation: routes_to
claim_refs: MI-2026-08-01-US-ADVANCED-PACKAGING-REGIONALIZATION#C3
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-01
review_due: 2026-08-15
status: active
boundary: 美國在地量產可能需要材料資格與雙區變更管理，但現有來源沒有 universe 材料 料號 facility qualification 份額 收入或毛利。
next_trigger: Amkor／客戶與材料商雙向對上同一料號 facility process qualification 用量 出貨 收入及毛利。
-->
