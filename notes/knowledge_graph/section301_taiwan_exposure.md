# Section 301 台灣商品七關與四制度分流知識圖譜

本圖把國家層級政策、商品與交易判定、經濟轉嫁及公司財務歸因分開。正式 notice 已支持
前段稅率公式與部分 code-level 豁免；另把關稅、EAR 出口管制、OFAC 制裁與技術合格評定
分成四份底稿。四個台灣族群只建立搜尋入口，沒有公司受損線或法律合規結論。

<!-- knowledge_graph_meta
schema_version: 1
graph_id: section301-taiwan-exposure
root_node_id: concept:section301-taiwan-exposure
label: Section 301 台灣商品七關與四制度分流
summary: 從 policy scope HTS classification Annex exemption customs origin shipment importer Incoterms demand pass-through 追到 company financial attribution 並把 tariff EAR export control OFAC sanctions 與 technical conformity 分開 避免把單一通行證或國家 headline rate 直接寫成公司合規與毛利結論。
article_ids: MI-2026-07-23-US-SECTION301-TAIWAN
status: active
-->

<!-- knowledge_edge
edge_id: KG-S301-C01
view: company
from_id: company:2308
to_id: concept:section301-taiwan-exposure
relation: produces
claim_refs:
note_refs: 2308#S1
evidence_state: verified
commercial_stage: production
materiality: named_product
exclusivity: unknown
exclusivity_scope:
as_of: 2026-07-17
review_due: 2026-08-31
status: active
boundary: 台達年報只支持電源供應器 功率元件 風扇 熱管理與資料中心產品入口 不支持任何產品 HTS 原產 豁免 進口責任 關稅轉嫁或 Section 301 財務影響。
next_trigger: 台達與可追溯 entry 或客戶資料對上同一產品 HTS 原產 importer Incoterms 價格數量與公司財務分母。
-->

<!-- knowledge_edge
edge_id: KG-S301-I01
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:policy-action-scope
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C5
note_refs:
evidence_state: verified
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 正式 notice 支持台灣稅率公式 生效與 entry 框架 不等於任一商品實際分類 豁免 原產或公司稅負。
next_trigger: USTR docket 或 Federal Register 發布 amendment correction updated Annex 或執行文件。
-->

<!-- knowledge_edge
edge_id: KG-S301-I02
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:hts-product-classification
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Annex 按 HTS 執行只證明必須分類 不替任何公司 SKU 組態或 entry 指定 code。
next_trigger: 公司或可追溯報關資料公布同一料號 規格 進口形態與 HTS classification rationale。
-->

<!-- knowledge_edge
edge_id: KG-S301-I03
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:annex-exemption-test
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C2,MI-2026-07-23-US-SECTION301-TAIWAN#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 多類電腦 設備 傳輸與半導體 code 列入一般豁免 不表示每個裸零件 模組或公司產品都豁免。
next_trigger: 同一具名產品先固定 HTS 再逐條核對 Annex 一般豁免 Section 232 與其他條件。
-->

<!-- knowledge_edge
edge_id: KG-S301-I04
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:customs-origin-test
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 供應商總部 出貨港或最後組裝地不能替代海關原產地判定 本文不提供法律或報關意見。
next_trigger: 同一產品公開製程 工廠 實質轉型依據與 ruling 或可追溯 entry origin。
-->

<!-- knowledge_edge
edge_id: KG-S301-I05
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:shipment-contract-incidence
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: Importer of record 的先繳義務不等於最後經濟承擔 且美國營收占比不能替代直出與交易條款。
next_trigger: 公司或客戶揭露直出占比 importer Incoterms 報價幣別與 tariff price adjustment clause。
-->

<!-- knowledge_edge
edge_id: KG-S301-I06
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:demand-pass-through-response
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C6
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 政策與合約只能列出傳導路徑 沒有實際價格 數量 替代與議價資料就不能指定最後承擔方。
next_trigger: 同一產品在政策前後公開成交價格 數量 客戶協商 替代路徑與供應鏈配置變化。
-->

<!-- knowledge_edge
edge_id: KG-S301-I07
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:section301-company-financial-attribution
relation: reaches_stage
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C4
note_refs:
evidence_state: unverified
commercial_stage: financial
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 現有來源沒有同一產品 entry 原產 條款 價格 數量 成本與公司總額橋接 因此沒有毛利或現金流結論。
next_trigger: 公司與可追溯交易資料對上同一期間產品分子 收入成本毛利現金流與公司分母。
-->

<!-- knowledge_edge
edge_id: KG-S301-I08
view: industry
from_id: concept:section301-taiwan-exposure
to_id: group:passive
relation: routes_to
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 被動元件只是一個分類查找入口 沒有公司料號 HTS 原產 出貨 轉嫁或財務曝險證據。
next_trigger: 具名被動元件產品完成七關映射並由公司與客戶或 entry 資料雙向核對。
-->

<!-- knowledge_edge
edge_id: KG-S301-I09
view: industry
from_id: concept:section301-taiwan-exposure
to_id: group:pcb
relation: routes_to
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 裸板 組裝板 零件與整機可能不同分類 PCB 族群只建立查找路由 不建立受損或受惠線。
next_trigger: 具名 board identity 進口形態 HTS 原產 客戶條款 出貨與公司財務完成七關重建。
-->

<!-- knowledge_edge
edge_id: KG-S301-I10
view: industry
from_id: concept:section301-taiwan-exposure
to_id: group:powersupply
relation: routes_to
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: PSU 模組 零件與整機可能由不同主體進口 現有來源沒有 universe 公司 pass-through 或財務證據。
next_trigger: 具名 PSU 或電源模組完成 HTS 原產 importer Incoterms 價格數量與財務橋接。
-->

<!-- knowledge_edge
edge_id: KG-S301-I11
view: industry
from_id: concept:section301-taiwan-exposure
to_id: group:thermal
relation: routes_to
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C4
note_refs:
evidence_state: unverified
commercial_stage: application_opportunity
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-15
status: active
boundary: 風扇 散熱器 冷板 模組與整機內含件可能不同分類 產品俗稱不能支持公司稅負或毛利方向。
next_trigger: 具名 thermal 產品完成 entry HTS 原產 交易責任 轉嫁與財務分母的七關映射。
-->

<!-- knowledge_edge
edge_id: KG-S301-I12
view: industry
from_id: concept:section301-taiwan-exposure
to_id: concept:trade-regime-separation
relation: includes
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C10
note_refs:
evidence_state: inference
commercial_stage: concept
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 四制度分流只防止關稅 出口管制 制裁與技術資格互相背書 不替任何產品完成法律 技術或財務判定。
next_trigger: 同一具名產品與交易公開四份底稿並由合格法律 技術與財務責任人各自簽核。
-->

<!-- knowledge_edge
edge_id: KG-S301-I13
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:tariff-import-entry
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C5
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: HTS entry 原產與關稅結果不回答 ECCN 出口許可 制裁交易或客戶 qualification。
next_trigger: 具名產品公開可追溯 entry HTS origin exemption importer 與 duty result 並接回同產品其他三份底稿。
-->

<!-- knowledge_edge
edge_id: KG-S301-I14
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:ear-export-license-screen
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C7
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: BIS 通用指引只證明要分開 item scope ECCN destination parties 與 end use 不替任何具名產品或交易判定許可。
next_trigger: 合格責任人對同一具名產品固定 EAR scope classification destination transaction parties end use license exception 與最終結果。
-->

<!-- knowledge_edge
edge_id: KG-S301-I15
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:ofac-sanctions-transaction-screen
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C8
note_refs:
evidence_state: verified
commercial_stage: validation
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: OFAC 與 BIS 名單目的不同不表示個案只受一套規則 也不替任何交易判定封鎖 拒絕 授權或可進行。
next_trigger: 同一交易公開適用 sanctions program party ownership jurisdiction activity authorization 與處理結果。
-->

<!-- knowledge_edge
edge_id: KG-S301-I16
view: industry
from_id: concept:section301-taiwan-exposure
to_id: stage:technical-conformity-assessment
relation: passes_through
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C9
note_refs:
evidence_state: verified
commercial_stage: qualification
materiality: adjacent
exclusivity: unknown
exclusivity_scope:
as_of: 2026-08-12
review_due: 2026-08-26
status: active
boundary: 通用合格評定角色與活動存在不表示具名 AI 產品已通過第三方認證 平台 qualification 客戶簽收或量產變更重驗。
next_trigger: 同一產品版本公開 requirement sample test condition executor raw result pass criteria change control 與 customer sign-off。
-->

<!-- knowledge_edge
edge_id: KG-S301-I17
view: industry
from_id: concept:section301-taiwan-exposure
to_id: process:tariff-to-financial-passport
relation: requires
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C14
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: multi_source
exclusivity_scope: 十欄護照是研究中心綜合USTR CBP與USITC邊界的稽核框架 不是報關表 法律意見 會計政策或政府正式標準。
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 護照只分開政策 entry 經濟歸宿與公司財務證據 不判定具名產品適用性 duty pass-through或公司效果。
next_trigger: 同一具名SKU與entry由報關法律責任人 公司及客戶共同公布十欄資料和價格數量成本財務橋接。
-->

<!-- knowledge_edge
edge_id: KG-S301-I18
view: industry
from_id: concept:section301-taiwan-exposure
to_id: metric:customs-value-duty-incidence-boundary
relation: measured_by
claim_refs: MI-2026-07-23-US-SECTION301-TAIWAN#C11,MI-2026-07-23-US-SECTION301-TAIWAN#C12,MI-2026-07-23-US-SECTION301-TAIWAN#C13,MI-2026-07-23-US-SECTION301-TAIWAN#C14
note_refs:
evidence_state: inference
commercial_stage: validation
materiality: unknown
exclusivity: multi_source
exclusivity_scope: CBP固定通用customs-value入口 USITC固定歷史border incidence與限制 教學算式不是產品entry公司或未來預測樣本。
as_of: 2026-08-14
review_due: 2026-08-26
status: active
boundary: 固定稅率與毛利情境只防止分母混用 不提供HTS原產豁免appraised value其他duty法律判定或公司估值。
next_trigger: 具名entry公開customs value稅率逐項duty importer合約價格數量及公司毛利共同鍵並與海關結果核對。
-->
