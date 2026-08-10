# 曝光次數少了，晶片不一定更便宜：先看圖形怎麼印、哪些成本又冒出來

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

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:high_frequency_glossary
-->

<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave6_compute_interconnect_learning_no_conclusion_change
evidence: editorial:plain_language_wave6
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave100_high_na_five_positions_five_cost_lenses_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **晶圓**：用來製造許多晶片的圓形薄片；同一片上會重複進行曝光、顯影、蝕刻、沉積與量測。
- **微影**：把設計好的微小圖形複製到晶圓表面的製程，像替後續加工畫出位置與邊界。
- **曝光**：用光把光罩圖形投到晶圓表面的光阻上；曝光完成仍要顯影與後續加工才能留下實體結構。
- **光罩**：承載某一層晶片圖形的模板；圖形正確不等於曝光後的晶圓一定沒有缺陷。
- **光阻**：塗在晶圓上的感光材料；受光後的化學變化讓指定區域能在顯影時被留下或移除。
- **顯影**：依光阻受光結果洗出圖形；顯影完成仍要確認線寬、缺陷與圖形是否可轉移。
- **圖形轉移**：把光阻上的暫時圖形交給蝕刻或其他加工，變成晶圓上的實體結構。
- **蝕刻**：依圖形選擇性移除材料；曝光印得出來不等於蝕刻後仍能維持相同尺寸與良率。
- **量測**：量出線寬、位置、厚度與疊對等數值，用來判斷製程是否落在可接受範圍。
- **檢查**：尋找顆粒、刮傷、圖形破損與其他缺陷；量測與檢查常一起決定問題能否被及早發現。
- **缺陷**：可能讓圖形或晶片功能失敗的異常；缺陷數量要放回晶圓面積、層數與產品良率判讀。
- **線寬**：晶圓上某條線或間距的尺寸；能印得更細不等於整個產品都會使用相同尺寸。
- **解析度**：曝光系統分開細小圖形的能力；解析度提升只是製程成立的一項條件。
- **數值孔徑**：描述光學系統收集與聚焦光線能力的指標；提高它可改善解析度，也會改變光罩、光阻與製程整合要求。
- **EUV**：極紫外光微影，用很短波長的光印製先進晶片圖形；它只是完整製程中的一段。
- **High-NA**：把極紫外光系統的數值孔徑提高到 0.55 的方案；目標是一次印出更細圖形，但仍要驗證良率、產出與成本。
- **Low-NA**：目前較低數值孔徑的極紫外光平台；部分細圖形會搭配多重圖形化完成。
- **多重圖形化**：把原本難以一次印出的圖形拆成多次曝光與加工；步驟增加，也會增加對準與製程控制負擔。
- **對準**：讓本次加工對到晶圓上預定位置；偏差過大可能讓圖形或電路失效。
- **疊對**：量測不同製程層彼此位置是否重合；單層印得清楚仍不代表多層能正確接起來。
- **製程視窗**：曝光、焦距、材料與加工條件仍能產生合格結果的可接受範圍；視窗太窄會增加量產波動。
- **良率**：投入後得到合格晶片的比例；設備速度快或步驟少，都必須和良率一起看。
- **可用率**：設備在預定生產時間內可正常工作的比例，英文常寫 availability；它不等於每小時產出或良率。
- **每小時產出**：設備在一小時內可處理的晶圓或合格層數，英文常寫 throughput；要和停機、返工及良率一起判讀。
- **維護時間**：設備保養、校正或故障修復占用的時間；它會影響可用率、排程與實際產出。
- **測試圖形**：為了研究或校正而設計的簡化圖形；成功不等於實際產品的所有圖形都能量產。
- **產品晶圓**：使用實際產品設計而非只有測試圖形的晶圓，英文常寫 product wafer；仍可能停在驗證階段。
- **校準**：調整設備與量測基準，使結果落在預定範圍；校準完成不等於製程資格或量產完成。
- **資格驗證**：依指定條件確認設備、材料與製程能否被採用，英文常寫 qualification；範圍可能只涵蓋部分圖形或條件。
- **高量產導入**：把設備與製程放進持續生產的產品節點，英文常寫 HVM insertion；需要穩定良率、產出、成本與客戶產品共同成立。
- **EXE**：ASML 對高數值孔徑極紫外光曝光機使用的產品平台前綴，例如 EXE:5200；型號到廠不等於量產導入。
- **每顆合格晶片成本**：把設備、材料、加工、維護、返工與報廢分攤到最後合格晶片的成本；它比只算曝光次數更接近經濟結果。

### 三句話抓重點

- 先在晶圓表面塗上光阻，再用光罩控制光線落在哪裡；這一步像替下一道加工留下底稿。
- 新設備可能一次印出更細的底稿，因而少做重複對準與加工；但停機、材料缺陷和做壞的比例也會改變。
- 因此不能只看機器送到或累計處理多少片；要看到實際產品通過驗證、穩定生產，以及每顆合格晶片的總成本。

### 為什麼重要

曝光設備的新聞很容易把「機器送到」誤讀成「新製程已經大量生產」。真正的問題不是圖形能否
在一次展示中印得更細，而是光罩、材料、後續加工、量測與產品設計能否一起穩定運作。少做幾個
步驟可能省時間，也可能因設備昂貴、停機、缺陷或做壞更多而失去節省；最後要看的是每顆合格
晶片，而不是單一設備的最高紀錄。

### 接下來怎麼追

- 先看研發機構是否完成資格驗證，並說清楚測了哪些圖形、材料與製程條件。
- 再看設備商是否宣布量產準備條件達成，而不是只更新累計處理片數或單機最高紀錄。
- 客戶端要揭露實際產品、使用層數、缺陷、良率、每小時產出與量產日期。
- 材料與設備公司只有在客戶具名驗證、公司出貨及財務貢獻能相互核對時才升級。

### 想一想

- 如果新設備少做兩次加工，卻更常停機或做壞更多晶片，最後每顆合格晶片會更便宜嗎？
- 八台機器送到不同場所，只回答了設備商哪一段進度，還缺哪些客戶產品與穩定生產證據？
- 如果客戶只在少數最難的圖形使用新設備，材料、量測與後續加工需求會全部一起增加嗎？

## 先用五個位置看圖形怎麼印到晶圓

| 本文五個位置 | 眼前發生什麼 | 主要接力角色 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 設計圖形與光罩 | 把某一層電路圖形做成曝光時使用的模板 | 晶片設計、光罩製作、資料準備與檢查 | 光罩缺陷、圖形修正與實際產品相容性 | 光罩完成不等於晶圓已印成功或產品能量產 |
| 2. 晶圓表面與光阻 | 清潔晶圓、塗上感光材料並控制厚度與均勻性 | 晶圓廠、材料、塗佈顯影設備與製程整合 | 光阻反應、均勻度、顆粒與後續顯影結果 | 有高數值孔徑用光阻不等於已通過客戶資格 |
| 3. 曝光機與光學 | 用光學系統把光罩圖形縮小並投到晶圓光阻上 | 曝光設備、光源、光學、校準與設備維護 | 解析度、焦距、可用率、每小時產出與長期穩定度 | 機器出貨或印出測試圖形不等於產品節點量產 |
| 4. 顯影與圖形轉移 | 洗出光阻圖形，再用蝕刻等加工把圖形留下來 | 顯影、蝕刻、材料、清洗與製程控制 | 線寬、側壁、缺陷、對準與轉移後的圖形完整性 | 曝光成功不等於後續加工仍能保住相同圖形 |
| 5. 量測、檢查與下一層 | 找出尺寸、位置與缺陷，再決定是否進入下一層 | 量測、檢查、缺陷分析、良率與產品工程 | 多層疊對、實際產品良率、返工與報廢 | 單層或單次測試合格不等於整顆晶片合格 |

五個位置是最短閱讀路徑，不是完整晶片配方。高數值孔徑方案主要改變第三個位置的光學能力，
但它能不能降低總成本，仍取決於第一、二、四、五個位置能否一起通過產品與量產驗收。

## 再用五把尺比較少做步驟是否真的省錢

| 本文五把尺 | 較高數值孔徑方案 | 現行多步驟方案 | 下一個要量的結果 | 不能直接推成 |
|---|---|---|---|---|
| 1. 曝光與加工次數 | 目標是一次印出更細圖形，讓部分層少做重複曝光與圖形轉移 | 可能把困難圖形拆開，多做曝光、對準與加工 | 同一產品層實際少了哪些步驟、時間與材料 | 理論少一步不等於整片晶圓或整顆晶片成本較低 |
| 2. 機器可用時間與每小時產出 | 新平台要證明長時間運轉、維護與每小時產出符合生產需求 | 既有平台已有較長的運轉經驗，但多步驟會占用更多機台時間 | 同一期間的可用率、停機原因、維護時間與合格產出 | 累計處理片數不能直接換成每台穩定產能 |
| 3. 光罩、光阻與缺陷 | 更細圖形會改變光罩、感光材料與缺陷控制要求 | 多次加工增加光罩、材料與每一步產生缺陷的機會 | 光罩數、材料用量、缺陷密度、返工與報廢 | 材料要求變高不等於任何材料商已取得份額 |
| 4. 對準、製程視窗與良率 | 少做部分重複對準可能有利，但新光學與材料仍要建立穩定視窗 | 每多一次圖形拆分與轉移，都要控制層間位置與誤差累積 | 實際產品的疊對、視窗、缺陷與最終良率 | 單一測試圖形更清楚不等於完整產品良率更高 |
| 5. 每顆合格晶片總成本 | 要把昂貴設備、材料、維護、停機與良率一起分攤 | 要把較多曝光、加工、光罩、排程與誤差成本一起分攤 | 同一產品、產量與期間的設備折舊、材料、返工、良率與合格品 | 不能只靠曝光次數或設備價格宣告哪一條路更便宜 |

這五把尺把「解析度更高」和「經濟性更好」分開。高數值孔徑方案可能先用在最難、最值得少做
步驟的少數層；現行方案也可能在其他層繼續使用。沒有同一產品、層數、產出、良率與成本分母，
就不能把技術優勢改寫成全面替代或更低總成本。

## 把五類角色放回同一段曝光接力

| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 曝光設備與平台 | 提供高數值孔徑曝光機、安裝、運轉與平台改進 | ASML 的 EXE 平台 | 截至 2025 年底八台出貨、六台運轉；平台累計處理逾 50 萬片 | 出貨、運轉與累計片數不等於客戶完成量產導入 |
| 2. 研發與資格整合 | 把設備、光罩、光阻、量測與圖形轉移放進共同測試環境 | imec 的 EXE:5200 | 設備已到研發環境，公開目標是在 2026 年第四季完成資格驗證 | 研發機構資格不等於晶圓製造客戶的產品節點量產 |
| 3. 晶圓製造客戶 | 安裝設備、校準並用實際產品圖形驗證製程 | Intel 的早期安裝；其他客戶產品晶圓測試 | Intel 公開完成安裝並開始校準；ASML 表示客戶已開始產品晶圓測試 | 沒有客戶、節點、層數、良率與量產日期，不能宣告導入完成 |
| 4. 光罩、材料與圖形轉移 | 讓曝光圖形能被顯影、蝕刻並保留在晶圓上 | 本輪只確認這些是共同成熟條件 | ASML 與 imec 文件支持光阻、光罩與圖形化依賴 | 沒有具名供應商資格、出貨、份額或台灣公司財務證據 |
| 5. 量測、檢查與生產經濟 | 找缺陷、量尺寸、追良率，並把結果接回產出與成本 | 本輪沒有具名台灣供應商 | 量測、檢查與製程穩定度是成熟條件；公司映射仍未證實 | 一般先進製程能力不能改寫成高數值孔徑訂單或獲利 |

角色表回答「誰負責哪一段」，不是完整供應商名單。ASML、imec 與 Intel 的公開資料分屬
設備商、研發整合與早期客戶時鐘；它們能共同支持產業路徑，卻不能替任何台灣設備或材料公司
補上具名資格、出貨與財務結果。

## 把五個里程碑排成同一條導入階梯

| 本文五個里程碑 | 白話意思 | 本輪可確認 | 下一份證據 | 不能合併成 |
|---|---|---|---|---|
| 1. 機器送達 | 設備商完成出貨，客戶或研發場所收到設備 | 截至 2025 年底累計八台高數值孔徑系統出貨 | 後續安裝、客戶驗收與逐台配置 | 八台出貨不是八條量產線，也不是八個客戶量產 |
| 2. 開始運轉與校準 | 設備安裝後能啟動、調整並處理晶圓 | 六台運轉；Intel 早期系統完成安裝並開始校準 | 長期可用率、每小時產出、維護與客戶驗收 | 能運轉不等於製程資格、產品良率或量產 |
| 3. 研發資格與共同整合 | 光罩、材料、圖形轉移與量測在指定範圍通過測試 | imec 設備到廠，目標在 2026 年第四季完成資格驗證 | 完成文件、測試範圍、限制與未成熟項目 | 目標日期不是已完成結果；研發資格也不是客戶量產 |
| 4. 實際產品晶圓測試 | 用真實產品圖形而非只有測試圖形驗證 | ASML 表示客戶已開始測試；平台累計處理逾 50 萬片、可用率逾 80% | 客戶、產品、層數、視窗、缺陷與良率分母 | 聚合片數與可用率不能指定到某個客戶節點 |
| 5. 穩定量產導入 | 客戶把具名層放進持續生產，產出、良率與成本可重算 | ASML 把量產準備條件與客戶導入放在未來目標 | 2026 年底準備結果與 2027–2028 客戶產品量產文件 | 未來目標不能提前寫成已量產或已形成供應鏈收入 |

五個里程碑使用不同單位、期間與責任人。研究中心保留八台、六台、五十萬片、逾八成可用率
與未來時程，卻不把它們相加或正規化成一個假精確的「完成率」。

## 最後用六關分開設備進度、客戶量產與公司受惠

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 目標圖形可以印出 | 高數值孔徑設備能處理指定圖形與晶圓 | 多台設備已出貨與運轉，平台有累計處理量 | 第二個獨立環境重現實際產品圖形與限制 | 技術可行不等於量產穩定或成本較低 |
| 2. 多台設備能持續運轉 | 客戶端設備有可重算的可用率、產出與維護結果 | 六台運轉；平台聚合可用率逾 80% | 逐台、逐客戶、同期間的停機、維護與合格產出 | 聚合平均不能代替每台設備與客戶驗收 |
| 3. 共同製程通過資格 | 光罩、光阻、圖形轉移、量測與檢查在指定範圍完成驗證 | imec 公開的是 2026 年第四季目標，尚非完成結果 | 資格文件、測試範圍、材料、缺陷與未達項目 | 設備到廠或目標日期不能改寫成共同製程已成熟 |
| 4. 實際產品達成視窗與良率 | 客戶以具名產品與層數證明圖形、缺陷與良率 | 已開始產品晶圓測試，但沒有客戶與結果分母 | 產品、節點、層數、製程視窗、缺陷與良率 | 開始測試不等於完成驗證或進入大量生產 |
| 5. 量產層數、產出與成本可重算 | 客戶持續生產，能比較少做步驟後的每顆合格晶片成本 | 客戶導入仍是 2027–2028 目標 | 量產日期、層數、台數、產出、良率、設備與材料成本 | 未來導入目標不能換算市場規模、材料用量或公司營收 |
| 6. 供應商財務足跡出現 | 具名設備或材料通過客戶資格並留下出貨、收入、毛利與現金流 | 沒有任何 universe 公司完成雙向核對 | 客戶具名資格加上公司產品、出貨、份額與財務分母 | 服務先進製程或極紫外光不等於已取得高數值孔徑訂單 |

本輪設備與平台可走到第二關，第三關仍是待完成目標，第四關只有「開始測試」而沒有產品結果，
第五、六關尚未通過。六關是證據排序，不是技術分數、供應商名單、營收預測或投資排名。

## 這篇對公司判斷的用處與界線

半導體設備研究可以沿曝光、塗佈顯影、蝕刻、清洗、量測與缺陷控制尋找具名資格；材料研究
可以追光阻、光罩相關材料、化學品與耗材。但這些只是「去哪裡找下一份證據」，不是「公司
已經受惠」。同一台曝光機開始運轉，也不表示所有前後段設備與材料用量會等比例上升。

真正能升級公司信心的資料，必須把同一客戶、具名產品、使用層、資格驗證、量產出貨與財務
結果串在一起。現有來源沒有列名 universe 公司，也沒有訂單、收入、毛利、資本支出回收或
市場定價分母；因此本文不支持個股排序、營收推估或投資動作。

## 來源與證據邊界

- [ASML 2026 年股東會簡報](https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf)（工具出貨、運轉與客戶導入時程）。
- [Imec EXE:5200 到達研發環境](https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system)（研發整合與 2026 年第四季資格目標）。
- [ASML 2026 年第一季投資人電話會議](https://ourbrand.asml.com/asset/8e1f7393-33dd-4737-a436-cfe1b68cc577/2026_04_15-ASML-Transcript-investor-call-Q1-2026.pdf)（累計晶圓、可用率、產品晶圓與光阻進度）。
- [Intel 高數值孔徑極紫外光資料](https://newsroom.intel.com/press-kit/intel-high-na-euv)（早期客戶安裝與校準基線）。

本篇沒有拿 ASML、imec 與 Intel 的數字互相比較：一組是設備商平台、一組是研發機構資格，
一組是早期客戶安裝事件，期間、單位與定義不同。也不使用設備出貨數推估台灣公司訂單、
晶圓廠良率、每顆合格晶片成本或市場定價。

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

- Imec 在 2026 年第四季公開 EXE:5200 資格驗證結果、測試範圍與仍未達成項目。
- ASML 確認量產準備條件是否如期達成，並提供能分開產品測試與持續生產的指標。
- Intel 或其他客戶揭露實際節點、使用層數、產品晶圓、製程視窗、缺陷、良率與量產日期。
- 若 2027–2028 客戶導入延後、只停在研發，或現行多重圖形化在成本與良率持續更有利，C5 必須下修。
- 台灣設備與材料公司只有在客戶具名資格與公司產品、出貨及財務揭露相互吻合後，才從未驗證路由升級。
