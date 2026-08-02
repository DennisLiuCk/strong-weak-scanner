# High-NA EUV 已有八台出貨與產品晶圓測試，但 HVM 插入仍在 2027–2028 階段

<!-- research_topic
topic_id: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-04-22
last_reviewed_at: 2026-08-02
review_due: 2026-10-01
source_type: mixed
publisher: ASML
publisher_domain: asml.com
canonical_url: https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf
source_chain_id: high-na-euv-insertion-20260802
stock_ids:
group_ids: semiequip,material
trigger_type: lithography_tool_process_and_hvm_insertion
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: ASML、imec 與 Intel 一手來源可交叉確認工具出貨、客戶端運轉、產品晶圓測試與資格／插入時程；但 2026 年底 HVM readiness、2027 至 2028 客戶節點插入、台灣供應商角色與財務貢獻仍待驗證
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_high_na_scan
evidence: source_chain:high-na-euv-insertion-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_tool_shipment_operation_process_qualification_product_wafer_and_hvm_insertion
evidence: sources:S1,S2,S3,S4
-->

<!-- research_source
source_id: S1
role: company_filing
source_kind: document
publisher: ASML
title: ASML 2026 Annual General Meeting Presentation
published_at: 2026-04-22
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf
locator: PDF p.15（檔案頁碼標示 Page 15）；截至 2025 年底八台 High-NA 出貨、六台運轉、首台 EXE:5200B 在客戶端，並以 2026 年底 HVM requirements、2027–2028 insertion 為目標
limitation: ASML 的出貨與時程證實工具及平台進度，不證明客戶製程已 qualification、量產良率、節點採用層數或供應商財務曝險
independence_group: asml
-->

<!-- research_source
source_id: S2
role: other_primary
source_kind: document
publisher: imec
title: Imec Receives the World Most Advanced High NA EUV System
published_at: 2026-03-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system
locator: 正文 tool arrival、ecosystem integration 與最後一段；imec 預期 EXE:5200 於 2026Q4 fully qualified
limitation: imec 是研發與 pilot 環境；工具到廠及其 qualification 目標不等於任何晶圓代工客戶的 HVM insertion
independence_group: imec
-->

<!-- research_source
source_id: S3
role: company_filing
source_kind: document
publisher: ASML
title: ASML Q1 2026 Investor Call Transcript
published_at: 2026-04-15
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ourbrand.asml.com/asset/8e1f7393-33dd-4737-a436-cfe1b68cc577/2026_04_15-ASML-Transcript-investor-call-Q1-2026.pdf
locator: PDF p.4（文件頁標示 Page 4 of 5）；High-NA 已處理逾 50 萬片 wafer、availability 逾 80%，客戶開始在 product wafers 測試，並提到 resist 進度
limitation: 數字由 ASML 揭露且沒有逐客戶、節點、層數、良率或成本分母；product-wafer testing 不等於 HVM
independence_group: asml
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: Intel
title: Press Kit High NA EUV at Intel
published_at: 2024-04-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.intel.com/press-kit/intel-high-na-euv
locator: press kit 首段與安裝說明；Intel 完成首台商用 High-NA 系統安裝並開始 calibration
limitation: 2024 安裝是早期導入基線，不證明 2026 製程資格、14A 量產插入、客戶產品或良率
independence_group: intel
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: ASML
title: ASML Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.asml.com/en/news/press-releases
locator: 2026-08-02 查得 ASML 系統、季度結果與 High-NA 後續公告入口
limitation: 動態索引只供發現新附件；不能自行證明 HVM requirements、客戶 insertion 或收入
independence_group: asml
-->

<!-- research_source
source_id: S6
role: other_primary
source_kind: living_index
publisher: imec
title: Imec Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.imec-int.com/en/press
locator: 2026-08-02 查得 High-NA qualification、patterning、resist、mask 與 metrology 更新入口
limitation: 新聞索引不等於 qualification 完成；每個新里程碑仍須區分 test vehicle、pilot 與 customer HVM
independence_group: imec
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: Intel Foundry
title: Intel Foundry Process Technologies
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.intel.com/content/www/us/en/foundry/process.html
locator: 2026-08-02 查得 Intel 14A、18A 與後續製程公開更新入口
limitation: 動態 process page 與 roadmap 不能替代 High-NA 實際使用層、qualification、量產良率或客戶產品文件
independence_group: intel
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: ASML 表示截至 2025 年底已向數個客戶出貨八台 High-NA 系統，其中六台已運轉，並包含首台第二代 EXE:5200B；公司目標是 2026 年底滿足 HVM requirements、2027 至 2028 年由客戶插入
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-04-22
basis: S1 p.15 直接列出出貨、運轉、機型與兩個目標時段
boundary: 出貨與運轉不是 process qualification；HVM requirement 目標與 customer insertion 也不是已完成事件
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: imec 於 2026-03-18 公告 EXE:5200 已抵達 Leuven cleanroom，並預期該系統在 2026Q4 fully qualified
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-18
basis: S2 的到廠與 qualification 時程段落直接支持
boundary: imec qualification 是研發環境里程碑，不等於晶圓代工客戶的產品節點或量產良率
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: ASML 在 2026Q1 投資人資料表示 High-NA 平台已處理超過 50 萬片 wafer、availability 超過 80%，且客戶開始在 product wafers 測試
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-04-15
basis: S3 p.4 直接列出累計 wafer、availability 與 product wafer testing
boundary: 聚合平台數字沒有逐客戶與量產分母，不能改寫成任何特定節點已 qualification 或達 HVM
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: Intel 在 2024-04-18 公開資料中表示已完成首台商用 High-NA EUV 系統安裝並開始 calibration
supporting_source_ids: S4
contrary_source_ids:
as_of: 2024-04-18
basis: S4 press kit 首段與圖片說明直接支持安裝及 calibration
boundary: 這是早期客戶導入基線，不證明 2026 製程資格、14A HVM 或外部 foundry 客戶採用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: inference
status: active
claim: High-NA EUV 已跨過只有單機 prototype 的階段，進入多台客戶端運轉、研發資格與 product-wafer testing；但在證據階梯上仍位於客戶 HVM insertion 之前，不能用八台出貨、50 萬片處理量或 imec 到廠替 2027–2028 量產節點提前畢業
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 提供 fleet 與 insertion 時程，S2 提供 imec qualification 目標，S3 提供平台與 product-wafer testing，S4 提供首個客戶安裝基線
boundary: 不推估 ASML 訂單、客戶節點份額、每片成本、台灣設備／材料用量、公司收入或市場是否已反映
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: ASML 已在 2026 年底達成全部 High-NA HVM requirements，或任一客戶已完成 2027–2028 量產節點 insertion
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 都把這些節點放在未來目標，S3 只到 product-wafer testing；本輪沒有完成文件
boundary: 未到目標日期與沒有完成證據不是反證，但成熟度只能停在 testing／qualification plan
verification_needed: ASML、imec 與客戶端發布 qualification、HVM readiness、實際節點／層數、良率及量產產品證據
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: universe 內半導體設備或材料公司已因 High-NA EUV 取得具名 qualification、訂單、收入、毛利或資本支出貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: ASML、imec 與 Intel 來源沒有具名 universe 公司，也沒有平台端與供應商端的財務雙向核對
boundary: 能服務先進製程、EUV、光阻、清洗、量測或耗材，只形成搜尋入口，不構成 High-NA 曝險
verification_needed: 客戶或平台端具名 qualification，加上台灣公司揭露產品、出貨與可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: inference
status: active
claim: High-NA 的量產準備度是 scanner、resist、mask、pattern transfer、metrology 與 process stability 的共同結果，而不是只由掃描機數量決定
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S2 明列 patterning、metrology、materials 與 resist／mask ecosystem，S3 把 resist 進度與 product-wafer testing 連到平台成熟
boundary: 這個依賴鏈不證明任一材料或設備供應商已取得客戶資格、份額、訂單或財務貢獻
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C5,C6,C8
metric: EXE:5200 qualification、availability、product wafer、HVM requirements 與 ecosystem readiness
source_ids: S1,S2,S3
watch_source_ids: S5,S6
frequency: monthly
frequency_detail: 每月檢查 ASML 與 imec；2026Q4 起提高為每次正式公告即重審
next_check: 2026-10-01
trigger: imec 公告 fully qualified、ASML 確認 HVM requirements 達成，或客戶披露產品晶圓層數、良率與 process window
invalidation: qualification 延後、availability／throughput 未達客戶要求、resist／mask／metrology 阻礙量產，或客戶維持 Low-NA multi-patterning
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C5,C6,C7
metric: 客戶節點 insertion、量產產品與台灣設備／材料財務映射
source_ids: S1,S4
watch_source_ids: S5,S7
frequency: quarterly
frequency_detail: 追蹤 ASML 季報與 Intel／其他客戶 process roadmap；公司線須等客戶與供應商雙向文件
next_check: 2026-10-15
trigger: 客戶確認 High-NA 實際節點、層數、產品與 HVM，且供應商揭露 qualification、出貨及收入
invalidation: 客戶 insertion 延至 2029 以後、只在 R&D 使用，或 Low-NA／多重圖形化在成本與良率上持續勝出
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **EUV**：用極短波長光把先進晶片圖形印到晶圓上的微影技術；它是製程中的一段，不是完整晶片工廠。
- **High-NA**：把 EUV 光學系統的數值孔徑提高到 0.55，以印更小圖形；解析度提高，同時也帶來光阻、掩模、量測與製程整合的新要求。
- **Availability**：設備在預定生產時間內可正常工作的比例；它重要，但不等於產能、良率或客戶已量產。
- **Product wafer**：用實際產品設計而非單純 test pattern 的晶圓做製程驗證；仍可能只在研發或 qualification 階段。
- **HVM insertion**：把設備與製程真正放進高量產節點；需要穩定 throughput、availability、良率、成本與客戶設計共同成立。

### 三句話抓重點

- ASML 表示截至 2025 年底已出貨八台 High-NA、六台運轉，平台也已處理逾 50 萬片 wafer，客戶開始做 product-wafer testing。
- imec 的 EXE:5200 目標在 2026Q4 fully qualified，而 ASML 將 HVM requirements 與客戶 insertion 分別放在 2026 年底及 2027–2028。
- 所以 High-NA 已不只是實驗室單機，但仍不能把工具出貨直接當成客戶量產；下一步要看資格、產品晶圓、良率、層數與實際節點。

### 為什麼重要

微影設備新聞最容易把「機器送到」誤讀成「新製程已量產」。High-NA 的真正價值來自能否用較少
曝光與製程步驟穩定印出客戶需要的圖形，這同時依賴 scanner、光阻、掩模、蝕刻、量測與缺陷控制。
把階梯拆開後，讀者才能分辨設備商收入、研發進度與晶圓代工節點是三個不同時鐘，也不會把所有
先進製程供應商一口氣畫成直接受惠。

### 接下來怎麼追

- 2026Q4 先看 imec 是否如期 fully qualified，以及 qualification 的測試範圍與限制。
- 看 ASML 是否明確宣布 HVM requirements 已達成，而不是只更新累計 wafer 或單機最高數字。
- 客戶端要找到實際節點、產品、High-NA 層數、良率、throughput 與量產日期。
- 材料與設備公司只有在客戶具名 qualification、公司出貨及財務貢獻同時出現時才升級。

### 想一想

- 如果 High-NA 能少做曝光步驟，但 availability、光阻缺陷或良率不足，總成本一定會比 Low-NA multi-patterning 更低嗎？
- 八台出貨是 ASML 的商業里程碑；對晶圓廠而言，還要多哪些製程與產品證據才算 HVM？
- 若客戶只在少數 critical layers 使用 High-NA，設備、材料與量測價值會如何分配，而不是全製程同步上升？

## 導入階梯：五個數字不能合併成一個「已量產」

| 階段 | 已有證據 | 仍需驗證 |
|---|---|---|
| 工具出貨 | 2025 年底累計八台 | 後續 shipment、安裝、acceptance 與各客戶配置 |
| 客戶端運轉 | 六台運轉，含首台 EXE:5200B | 長期 availability、throughput、maintenance 與成本 |
| 研發／資格 | imec EXE:5200 到廠；目標 2026Q4 fully qualified | qualification 完成、測試範圍、resist／mask／metrology readiness |
| Product wafer | ASML 表示客戶已開始測試 | 實際節點、層數、process window、缺陷與良率 |
| HVM insertion | ASML 目標 2027–2028 客戶插入 | 客戶量產產品、穩定良率、產出與經濟性 |

累計 wafer 與 availability 是平台成熟度線索，但缺少每台設備、每個客戶與量產層的分母。研究中心
因此保存原數字，卻不把它們正規化成一個假精確的「HVM 完成率」。

## 來源與證據邊界

- [ASML 2026 AGM presentation](https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf)（工具出貨、運轉與 insertion 時程）。
- [Imec EXE:5200 arrival](https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system)（研發環境與 2026Q4 qualification 目標）。
- [ASML Q1 2026 transcript](https://ourbrand.asml.com/asset/8e1f7393-33dd-4737-a436-cfe1b68cc577/2026_04_15-ASML-Transcript-investor-call-Q1-2026.pdf)（累計 wafer、availability、product wafer 與 resist）。
- [Intel High-NA press kit](https://newsroom.intel.com/press-kit/intel-high-na-euv)（早期客戶安裝／calibration 基線）。

本篇沒有拿 ASML、imec 與 Intel 的數字互相比較：一個是工具 fleet、一個是研發機構資格、一個是
早期安裝事件，期間、單位與定義不同。也不使用設備出貨數推估台灣公司訂單、晶圓廠良率或市場定價。

## 影響路由

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-01
rationale: High-NA 需要曝光之外的塗佈 顯影 蝕刻 清洗 量測與缺陷控制，但本輪未取得 universe 公司被客戶具名 qualification 的雙向證據
evidence_boundary: 服務先進製程或 EUV 不等於直接參與 High-NA、取得訂單或形成收入毛利
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-01
rationale: ASML 與 imec 明示 resist、mask、patterning 與材料生態系是成熟條件，但沒有具名台灣材料、規格、資格或財務貢獻
evidence_boundary: 光阻 化學品 晶圓或耗材能力是搜尋路由，不是 High-NA 客戶採用或業績事實
-->

## 下一個可證明／否定的節點

- Imec 在 2026Q4 公開 EXE:5200 fully qualified 結果、範圍與仍未達成項目。
- ASML 確認 HVM requirements 是否如期達成，並提供可區分 testing 與 production 的指標。
- Intel 或其他客戶揭露實際節點、High-NA 層數、產品晶圓、qualification、良率與量產日期。
- 若 2027–2028 insertion 延後、只停在 R&D，或 Low-NA multi-patterning 在成本／良率仍優，C5 必須下修。
- 台灣設備與材料公司只有在客戶具名 qualification 與公司財務揭露相互吻合後，才從 unverified 路由升級。
