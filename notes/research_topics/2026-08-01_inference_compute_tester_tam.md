# 推論晶片變多，測試機一定變多嗎？從 tester TAM 拆出八個需求分母

<!-- research_topic
topic_id: MI-2026-08-01-INFERENCE-COMPUTE-TESTER-TAM
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-07-29
last_reviewed_at: 2026-08-14
review_due: 2026-08-15
source_type: mixed
publisher: Advantest
publisher_domain: advantest.com
canonical_url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf
source_chain_id: advantest-inference-tester-tam-20260729
stock_ids: 2449,3035,3264,3443,3661,6223,6257,6510,6515,6533
group_ids: ipdesign,packtest,semiequip
trigger_type: demand_validation_and_market_forecast_revision
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C6
base_confidence: medium
confidence_basis: IEEE、設備商與三家台灣公司正式資料已能把需求拆成八個分母，並分辨測試服務、介面產品及設備收入時鐘；但仍沒有同產品測試時間、利用率、增量機台與台灣公司專案財務歸因
cross_company_numbers: true
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: primary_source_hyperscaler_and_test_equipment_scan
evidence: source_chain:advantest-inference-tester-tam-20260729
-->
<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: validated_global_demand_but_withheld_taiwan_supplier_attribution
evidence: sources:S1,S2,S3,S4,S5
-->
<!-- transition
date: 2026-08-08
from: triaged
to: triaged
reason: editorial_glossary_for_repeated_terms_no_conclusion_change
evidence: editorial:readability
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave8_learning_no_conclusion_change
evidence: editorial:plain_language_wave8
-->

<!-- transition
date: 2026-08-11
from: triaged
to: triaged
reason: editorial_plain_language_wave113_inference_test_profit_bridge_no_conclusion_change
evidence: editorial:plain_language_wave113_test_demand_bridge
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: reframed_tester_tam_as_eight_denominator_test_cell_and_financial_conversion
evidence: sources:S7,S8,S9,S10,S11
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_test_responsibility_passport_and_change_triggered_regression_without_thesis_upgrade
evidence: sources:S12,S13,S14,S15
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: separated_test_service_interface_product_and_equipment_revenue_clocks_without_company_beneficiary_upgrade
evidence: sources:S16,S17,S18
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **推論算力**：AI 模型回答問題時使用的運算資源；它可以由 GPU、自研 ASIC 與 CPU 等不同晶片共同提供。
- **Tester TAM**：測試設備商估計某一期間整體測試機市場的金額，不等於任何一家台灣供應商已取得的訂單。
- **自動測試設備（ATE）**：用測試程式、儀器與介面對晶圓或封裝後晶片施加訊號，再判定是否符合規格的設備。
- **晶圓針測（wafer sort／probe）**：封裝前，用探針卡接觸晶圓上的晶粒，先篩出可繼續投入封裝的晶粒。
- **成品測試（final test）**：封裝完成後，以測試機、載板與測試座確認電性和功能。
- **系統級測試（SLT）**：把晶片放進較接近實際系統的環境，執行較長或較貼近應用的測試；它不等於成品測試的重複版。
- **燒機（burn-in）**：在受控電壓、溫度與時間下施加壓力，用來暴露部分早期失效。
- **測試插入點（test insertion）**：在晶粒、堆疊、封裝、模組或系統等不同階段安排的測試節點；標準能定義存取方法，卻不會替每項產品決定必測幾次。
- **可測試性設計（DFT／scan）**：晶片設計時預留測試控制與觀測路徑，讓內部邏輯或記憶體較容易被測到。
- **量產篩選（production screening）**：在製造流程中依既定測項判定哪些單位可繼續投入、放行、重測或報廢；它和抽樣式產品資格驗證不是同一個分母。
- **可靠度資格驗證（reliability qualification）**：以樣品、任務環境、加速壓力、時間與允收條件判斷產品或製程能否進入下一階段；通過不表示每一顆出貨品都跑過相同壓力。
- **測試責任護照（test responsibility passport）**：把受測物版本、測試目的、故障類別、插入點、設備組態、覆蓋、結果責任與重測條件綁在同一筆可回查紀錄。
- **變更觸發回歸重測（change-triggered regression）**：晶片、封裝、程式、介面、製程或場域條件改變後，先做影響分析，再重跑受影響的測項；不等於每次一律全套重測。
- **多站並行（multisite）**：一套測試系統同時測多顆待測元件；站數越多不代表效率必然等比例提高。
- **待測元件（DUT）**：正在接受測試的晶片、封裝或模組。
- **每小時產出（UPH）**：特定設定下每小時可完成的單位數；不同設備、測項與時間不能直接互比。
- **測試單元（test cell）**：測試機加上探針台或分類機、介面、溫控、自動化與軟體形成的生產單元。
- **漏測（test escape）**：未在前一測試階段被攔下、到後續製程或客戶端才暴露的缺陷。
- **退貨分析（RMA）**：產品在客戶或現場失效後，沿序號、批次與既有測試結果回查、重現並分析根因的流程；單一退貨不等於全體失效率。
- **已知良品晶粒（known-good die）**：在投入昂貴多晶粒封裝前，已按約定範圍完成篩選的晶粒；「已知良品」仍受測試覆蓋和條件限制。
- **年化營收規模**：把目前一季或當下速度換算成一年的概略規模，不等於已完成的全年會計收入。
- **營收時鐘**：同一波測試需求在服務商、介面商與設備商分別跨過可計費機時、產品交付、設備驗收等事件後，才可能進入收入；三者不是同一個時間點。
- **Trainium**：Amazon（AWS）自行設計的 AI 晶片系列。它是雲端業者自研晶片的代表之一，與外購 GPU 是不同採購路徑。
- **Maia**：Microsoft 自行設計的 AI 加速晶片系列，角色與 Trainium 類似。
- **DRAM**：主流的動態隨機存取記憶體。本文提到它，是因為記憶體測試需求也構成測試機市場的一部分，與推論晶片需求要分開看。
- **CY2026（2026 曆年）**：從 2026 年 1 月到 12 月；它與公司的財政年度可能不同，本文用它表示 Advantest 市場預估涵蓋的時間。
- **SoC（系統單晶片）**：把處理器、控制器與其他功能整合在同一顆晶片；本文的 SoC tester 市場不只包含 AI 加速器。

### 三句話抓重點

- Advantest 上修 2026 年 tester TAM，並把推論 ASIC、CPU 與 DRAM 的產量及複雜度列為原因之一。
- 多晶粒產品與更長測項可能增加測試內容，但多站並行、既有設備升級與程式／載板重用也可能減少新增測試單元；兩邊必須放在同一張表。
- 三份台灣公司正式資料顯示，同一測試鏈會開出測試服務、介面產品與設備三種不同發票；它們仍沒有證明具名 AI 專案的新增訂單與獲利。

### 為什麼重要

市場容易把「自研 ASIC 成長」解讀成 GPU 單向流失，也容易把全球 tester TAM 上修直接分配給台灣個股。這篇把晶片數量、測試插入點、每顆測試內容、並行效率、良率重測、既有設備重用與公司財務拆開；只要其中一個分母不同，「晶片多一顆就多一台測試機」便不成立。

### 從晶片變多到公司獲利，先問四個問題

1. **測的是哪一種產品？** GPU、自研 ASIC、CPU、記憶體與多晶粒封裝的測項、功率、接腳與價值風險不同，不能只數晶片顆數。
2. **在哪些階段測？** 晶粒、堆疊、封裝、模組與系統測試可能新增、合併或移動；測試存取標準不是強制插入點清單。
3. **一套單元能做多少工作？** 測試時間會增加需求，多站並行、利用率、升級與重用則可能吸收需求。
4. **誰真的收到錢？** 還要由買方與台灣公司對上具名產品、介面、數量、期間、收入、毛利與現金，全球市場預估不能代替公司證據。

### 接下來怎麼追

- 下一次 Advantest 展望先追 2026 年市場區間是否維持，再找同產品的顆數、測試插入點、時間、站數、利用率、既有設備餘裕與新增測試單元。
- 追 Amazon Trainium 與 Microsoft Maia 的實際部署，但不把平台部署直接換算成測試設備採購。
- 追台灣公司法說與財報是否同時揭露具名專案、介面、量產、稼動率、平均售價、收入及毛利，而不是只談產業市場規模。

### 想一想

- 如果每顆晶片測試時間變長，但一套系統可同時測更多顆，新增測試單元一定增加嗎？
- 已知良品晶粒可以降低昂貴封裝後才報廢的風險，但它一定代表測試設備商收入等比例增加嗎？
- Advantest 的全球市場估計要經過哪八個分母，才能合理連到某一家台灣供應商的獲利？

## 主張與證據帳本

`證實` 只表示指定來源直接支持精確措辭；發行人的市場估計、年化數字與效能比較仍受各自定義限制，不代表台灣供應商訂單已被證實。

<!-- research_source
source_id: S1
role: market_estimate
publisher: Advantest
title: FY2026 Q1 Business Briefing
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf
locator: p.12 tester market outlook
limitation: tester TAM 是 Advantest 的市場估計，沒有拆分 GPU、CPU、ASIC 貢獻或台灣供應商份額
-->

<!-- research_source
source_id: S2
role: company_release
publisher: Amazon
title: Amazon 2026 Q2 Results
published_at: 2026-07-30
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
locator: AWS chips business 與 Trainium 客戶承諾段落
limitation: chips business 包含 Graviton、Trainium 與 Nitro，年化規模不是 Trainium 單一產品收入或採購金額
-->

<!-- research_source
source_id: S3
role: management_commentary
publisher: Microsoft
title: Microsoft FY2026 Q4 Earnings Call
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
locator: Maia 200、OpenAI／MAI models 與異質運算段落
limitation: 效能比較以 Microsoft 自有 fleet 為基準，沒有提供晶片數量、外部售價或台灣供應商映射
-->

<!-- research_source
source_id: S4
role: management_commentary
publisher: Advantest
title: FY2026 Q1 Business Briefing Notes
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf
locator: p.12 tester market trends、130–145 億美元區間與推論 ASIC／CPU／DRAM 需求段落
limitation: 管理層簡報附註仍是 Advantest 的市場預估，沒有拆出各運算架構或台灣供應商的實際貢獻
-->

<!-- research_source
source_id: S5
role: management_commentary
publisher: Advantest
title: Q1 FY2026 Financial Briefing Q&A Summary
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf
locator: pp.1–2 GPU、custom ASIC 與 CPU tester demand 問答
limitation: 管理層明示難以切分 GPU、CPU 與 custom ASIC 對 TAM 增量的相對貢獻，前瞻說法也不是已實現收入
-->

<!-- research_source
source_id: S6
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 台灣設計服務、封測與測試介面公司季報、法說及重大訊息查找入口
limitation: 雲端自研晶片與 tester TAM 只構成查找 trigger；入口本身不支持任何台灣公司訂單
-->

<!-- research_source
source_id: S7
role: standard
source_kind: living_index
publisher: IEEE Standards Association
title: IEEE 1838-2019 - IEEE Standard for Test Access Architecture for Three-Dimensional Stacked Integrated Circuits
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://standards.ieee.org/ieee/1838/5073/
locator: Active Standard summary 的 die-level test access、pre-stacking／post-stacking、partial／complete stack、pre-packaging／post-packaging／board-level scope
limitation: 公開摘要證明測試存取架構涵蓋哪些情境，不提供付費標準全文、產品實際插入點數、測試時間、良率、設備需求或公司訂單
independence_group: ieee-test-standards
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: living_index
publisher: Advantest
title: V93000 EXA Scale SoC Test System
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.advantest.com/en/products/semiconductor-test-system/soc/v93000/
locator: AI／HPC applications、scan-data volume、power、yield learning、high pin count、multisite、compatibility and reuse 段落
limitation: 這是設備供應商現行產品頁；沒有第三方驗證客戶實際測試時間、站數效率、利用率、設備重用率、增量機台或收入
independence_group: advantest-product
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: living_index
publisher: Advantest
title: 7038 SLT and Burn-In Test System
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.advantest.com/en/products/component-test-system/system-level-test-systems/7038/
locator: high-volume／high-test-time、up to 720 DUTs simultaneously、up to 5,000 UPH around 10-minute tests、structural test correlation 段落
limitation: up to 與 around 都是產品商條件式能力說明；沒有客戶產品組合、實際上線率、良率、利用率、收入，也不能與其他平台數字直接比較
independence_group: advantest-product
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: living_index
publisher: Teradyne
title: UltraFLEXplus Semiconductor Test System
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.teradyne.com/products/ultraflexplus/
locator: site count／parallel test efficiency、claimed 15%–50% test-cell reduction、redeployment、upgrade and reuse 段落
limitation: 這是產品供應商的效益宣稱，沒有共同產品、測試程式、客戶分母或生產實績，不能當成全市場實現值或與 Advantest 產品數字互比
independence_group: teradyne-product
-->

<!-- research_source
source_id: S11
role: management_commentary
source_kind: document
publisher: Teradyne
title: The Test Cell Ecosystem: From Tester Performance to Production Outcomes
published_at: 2026-06-15
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.teradyne.com/2026/06/15/the-test-cell-ecosystem-from-tester-performance-to-production-outcomes/
locator: heterogeneous integration、intermediate test stages、wafer／panel／subassembly／module insertions、test-cell throughput and yield 段落
limitation: 這是設備商產品管理觀點與生態系行銷，不是獨立產業普查，也沒有已實現客戶經濟效益；舊發布日只補框架，不單獨刷新需求時鐘
independence_group: teradyne-product
-->

<!-- research_source
source_id: S12
role: management_commentary
source_kind: document
publisher: Teradyne
title: AI Chiplet Architectures Redefining Test Insertions
published_at: 2026-07-27
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.teradyne.com/2026/07/27/ai-chiplet-architectures-redefining-test-insertions/
locator: Known-Good Everything、Module-Level Probe 與 Integration Density Drives Insertion Density 段落
limitation: 這是設備商主管的技術與市場觀點；只支持供應商描述的 wafer、singulated die、CoW module、final assembly 及 metrology／ATE／SLT 分工，不能把 insertion 數量、第三方 GPU 價格或產品能力改寫成全產業流程、設備台數或客戶收入
independence_group: teradyne-product
-->

<!-- research_source
source_id: S13
role: competitor_primary
source_kind: living_index
publisher: Amkor Technology
title: IC Semiconductor Test Services
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://amkor.com/test-services/
locator: Test Equipment、Burn-in Tester、System Level Tester 與 High Performance Compute 的 distributed test 段落
limitation: 這是封測服務商現行能力頁；wafer probe、in-situ、final ATE／SLT、qualification 與 100% burn-in 是可提供能力，不代表同一產品全部採用、各站測試時間、實際利用率、良率改善或新增收入
independence_group: amkor-test-services
-->

<!-- research_source
source_id: S14
role: company_release
source_kind: living_index
publisher: AMD
title: Design and Development
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.amd.com/en/corporate/quality/design-development.html
locator: Phase Gate Process、Product Validation、Design for Test 與 Design for Manufacturability 段落
limitation: 這是 AMD 的通用品質方法頁；只支持 pre-silicon verification、post-silicon validation、production exit、DFT 生命週期與 customer-return PPM 回饋的公司自述，不提供具名推論晶片的測試流程、覆蓋、時間、插入點或供應商採購
independence_group: amd-quality
-->

<!-- research_source
source_id: S15
role: competitor_primary
source_kind: living_index
publisher: NXP Semiconductors
title: Product Qualification
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nxp.com/products/nxp-product-information/quality/product-qualification%3AQUALITY__QUALIF
locator: Principles、bathtub curve、Knowledge-Based Qualification Methodology 與 Reliability Qualification Tests 段落
limitation: 這是 NXP 的通用產品資格方法，不是 AI 加速器或特定客戶規格；它只支持 mission profile、burn-in early-failure screening 與 accelerated qualification 的目的差異，不能外推到每顆產品皆採相同壓力、相同抽樣或相同設備需求
independence_group: nxp-quality
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: document
publisher: 京元電子
title: 2026 年第一季營運報告
published_at: 2026-05-08
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.kyec.com.tw/Common/Download?faname=CE9C12F9789DF09DB07AD813BD5475688BEAD13771DE3682E1557C949D18AADCBC1CA2FE6409102AE04ABAA1E80DB9551E6AE8CB84DA42B60CA4CFCBFBE8C3C1975FCB01637C8125A0F6E112F17D377B7B9D286F3E2741BDAAEFB35D0B5248527223686E9D7CE1A7
locator: pp.3–9 的製程收入、營運現金流、公司定義自由現金流與資本支出
limitation: 這是 Q1 而非 Q2 文件；製程與資料處理分類沒有 AI 專案、測試時間、稼動率、客戶、單價或毛利分子，且公司定義自由現金流不是營運現金流減資本支出
independence_group: kyec-2026q1-operating-report
-->

<!-- research_source
source_id: S17
role: company_release
source_kind: document
publisher: 中華精測
title: 2026 年第二季營運報告
published_at: 2026-07-29
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.cht-pt.com.tw/files/file_pool/1/0Q209650487702138855/26Q2%20%E6%B3%95%E8%AA%AA%E6%9C%83_CN.pdf
locator: pp.3、11–19 的產品收入結構、季度損益、營運現金流、資本支出與自由現金流公式
limitation: 這是公司法說簡報而非含完整附註的 Q2 會計師核閱財報；產品分類沒有數量、平均售價、客戶、具名產品、插入點、test-cell 利用率或產品別毛利
independence_group: chpt-2026q2-operating-report
-->

<!-- research_source
source_id: S18
role: company_release
source_kind: document
publisher: 旺矽
title: 2026 First Quarter Results
published_at: 2026-05-15
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.mpi-corporation.com/wp-content/uploads/2026/05/2026-Q1-Quarter-Result_0515%E5%AF%8C%E9%82%A6_2-page_EN.pdf
locator: 第 1–3 頁的探針卡、設備與其他收入占比，以及合併營收與損益摘要
limitation: 這是四頁 Q1 摘要且不是 Q2 文件；沒有兩條產品線各自金額、毛利、訂單、出貨量、平均售價、客戶、稼動率、資本支出或現金流
independence_group: mpi-2026q1-results
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Advantest 將 CY2026 SoC 與 memory tester TAM 更新為 130–145 億美元，並把推論 ASIC、CPU 與 DRAM 的產量及複雜度列為需求因素
supporting_source_ids: S1,S4
contrary_source_ids:
as_of: 2026-08-01
basis: S1 p.12 可直接定位市場預估區間與需求說明
boundary: 這是設備商的市場估計，不是已實現市場收入，也不證明任何台灣公司訂單、市占或獲利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: superseded
claim: 推論工作負載正擴大 ASIC、CPU、DRAM 與 GPU 並行的異質算力組合，晶片數量與複雜度可能共同增加測試需求
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-01
basis: S1 的 tester TAM 驅動因素與 S2、S3 的自研晶片擴大揭露共同支持此基準情境
boundary: 這是跨來源研究推論，不代表各架構的測試貢獻相同，也不自動成立於每一家台灣同族群公司
verification_needed: 後續 tester 訂單出貨、實際測試時間與台灣公司量產收入及毛利
corrected_by_claim_id: C6
resolution:
-->

<!-- research_claim
claim_id: C3
label: unverified
status: active
claim: 2449、3035、3264、3443、3661、6223、6257、6510、6515、6533 已因這波推論算力擴張取得可量化新增訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 三份來源都沒有點名上述台灣公司，也沒有提供其專案份額、收入、稼動率、ASP 或毛利
boundary: 只能作為公司級搜尋與複核清單，不得寫入正式筆記事實或當成既成受惠
verification_needed: 台灣公司正式法說、季報或公告須揭露專案階段並出現可辨識收入、毛利與現金流證據
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: IEEE 1838 的現行官方摘要把三維堆疊晶片測試存取涵蓋到堆疊前後、部分與完整堆疊、封裝前後及板級情境，證明測試可跨越多個製造與整合階段
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-08-12
basis: S7 Active Standard summary 直接列出 die-level test access 與各測試情境
boundary: 標準只定義存取架構及適用情境，不表示每項產品必須採用相同插入點數，也不提供測試時間、良率、設備台數或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: Advantest 與 Teradyne 的現行官方產品資料一方面列出 scan data、功率、接腳、測試時間與良率學習等工作壓力，另一方面也列出多站並行、升級及既有硬體或程式重用等容量抵銷手段
supporting_source_ids: S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: S8–S11 的產品與 test-cell 說明直接列出複雜度、吞吐、並行與重用，但各自適用條件不同
boundary: 這只證實設備商如何描述產品能力與需求機制；不是第三方驗證的客戶產能、實際節省幅度、市場平均或財務結果
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C6
label: inference
status: active
claim: 推論晶片需求不能按晶片顆數線性換算成 tester 需求；研究上應依序拆成產品組合與數量、測試插入點、內容與覆蓋、單顆時間／功率／接腳／熱、多站與並行效率、良率／重測／漏測、既有設備重用與資本支出時點，最後才做公司財務歸因
supporting_source_ids: S1,S2,S3,S4,S5,S7,S8,S9,S10,S11,S16,S17,S18
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C2；S1–S5 支持異質算力與市場方向，S7 補多階段測試存取，S8–S11 同時提供內容量壓力與並行／重用抵銷因素，因此縮窄原先把數量和複雜度直接連到需求的粗框架
boundary: 八層框架沒有替各分母設定權重，不預測市場規模、設備採購、台灣公司份額、收入、毛利、估值或股價方向
verification_needed:
correction_kind: supersedes
corrects_claim_id: C2
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: 公開資料已能把 Advantest 2026 tester TAM 的變動拆成產品數量、插入點、測試內容與時間、並行與重用、良率重測及增量測試單元，並據此量化歸因到台灣公司的收入與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 現有來源只有市場區間、平台方向、標準範圍與設備商產品能力，沒有同產品的完整 test-cell 與公司財務分母
boundary: 未取得完整分母前，不能以 tester TAM、產品頁最高能力、雲端晶片營收或平台效能代替訂單與獲利歸因
verification_needed: 同一產品與期間的晶片數、插入點、測項與時間、站數與並行效率、良率與重測、利用率、既有設備餘裕、增量設備採購，以及台灣公司介面、出貨、收入與毛利
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Teradyne 的 2026-07-27 官方文章把 wafer、singulated die、CoW module on interposer wafer、singulated CoW module 與 final assembly 列為不同測試層級；Amkor 現行官方能力頁另把 wafer probe、關鍵組裝步驟間 in-situ test、final ATE、SLT 與 burn-in 分開列示
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2026-08-12
basis: S12 的 Integration Density Drives Insertion Density 段落逐項列出多晶粒封裝測試層級，S13 的 HPC distributed-test 與 equipment 段落逐項列出封測服務位置及設備類別
boundary: 只證實兩家供應商如何描述能力與插入位置；不表示所有產品採同一流程、每站皆為 100% 測試、插入點增加、測試時間增加或新增設備與收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: 要把多階段測試換算成工作量，必須先用同一份測試責任護照固定受測物與版本、決策目的、故障類別、生命週期與參考平面、存取與 test-cell 組態、刺激與環境、抽樣／覆蓋／誤判／漏測、結果責任與放行、變更觸發重測及零件結果沿革；否則設計驗證、量產篩選、可靠度資格、SLT 與現場診斷不能共用一個 test-time 分母
supporting_source_ids: S7,S12,S13,S14,S15
contrary_source_ids:
as_of: 2026-08-12
basis: IEEE 1838 與 S12、S13 顯示受測物、存取位置及設備類別會隨封裝階段改變；S14 把 pre-silicon verification、post-silicon validation、production exit 與 customer-return feedback 分開；S15 又把 early-failure screening、mission profile 與 qualification 分開，因此本文將它們整理成可重算的責任與變更契約
boundary: 這是跨來源研究框架，不是任何標準規定的固定欄位、全產業共同流程、測試覆蓋權重、合格門檻、設備採購公式或台灣公司財務歸因
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: 本輪可定位的三家台灣公司正式營運資料使用不同收入分母：京元電子 2026Q1 按產品／成品測試、晶圓測試及預燒等服務製程分類，中華精測 2026Q2 按晶圓測試卡、IC 測試板及技術服務與其他分類，旺矽 2026Q1 則同時列探針卡、設備及其他
supporting_source_ids: S16,S17,S18
contrary_source_ids:
as_of: 2026-08-14
basis: S16 第 5 頁、S17 第 11 頁與 S18 第 1–2 頁直接列示各自季度收入分類；三份原檔已固定 SHA-256，並以全文擷取及引用頁影像交叉核對
boundary: 三家公司、兩個季度與三套分類只證明收入角色不同，不能比較占比高低、推估市場份額、AI 收入、產品毛利、tester 台數、測試機時或任何公司題材受惠
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: 將 AI 測試需求連到台灣公司財務時，至少要分開建立測試服務的可計費 test-cell 時數、介面產品的合格組態與交付／維修量、設備產品的交機／驗收與升級量三張單位經濟卡；兼營多條產品線的公司還要先拆線，不能把 tester TAM、服務時數與介面銷售額放入同一分母
supporting_source_ids: S8,S10,S11,S13,S16,S17,S18
contrary_source_ids:
as_of: 2026-08-14
basis: S8、S10、S11、S13 界定 test cell、設備、介面與測試服務角色；S16–S18 又以公司實際揭露顯示服務、介面及設備收入分類不同，本文據此建立三卡轉換框架
boundary: 三卡是研究中心的量綱與證據契約，不是會計準則、產業固定報價公式、收入認列政策、需求預測、估值模型或公司排序；各卡仍缺具名產品的數量、價格、利用率、毛利與現金回收
verification_needed:
resolution:
-->

## 先把 tester TAM 拆成八個分母

「市場規模上修」是研究起點，不是設備台數答案。以下八層要使用同一產品、同一期間和同一測試
參考平面才可能相乘；現有 18 份來源只覆蓋部分欄位，空白處不能用產業故事補上。

| 分母 | 先問什麼 | 現有公開證據 | 還缺什麼才可換算 |
|---|---|---|---|
| 1. 產品組合與數量 | 增加的是 GPU、ASIC、CPU、記憶體、裸晶或完整封裝？是淨增還是替代？ | Amazon、Microsoft 證實自研晶片路徑擴大；Advantest 把推論 ASIC、CPU、DRAM 列入市場驅動 | 同產品、同期間的合格出貨顆數，並扣除被替代產品 |
| 2. 測試插入點 | 晶粒、堆疊、封裝、模組與系統各測幾次？哪一站新增、移動或合併？ | IEEE 1838 證實三維堆疊存在封裝前後、部分與完整堆疊等存取情境 | 具名產品的實際測試流程、必測與抽測比例 |
| 3. 內容與覆蓋 | 測哪些故障、功能、介面與記憶體？覆蓋多少風險？ | 設備商頁面列出 scan data、結構測試與良率學習等需求 | 固定測試程式、故障模型、圖樣數、覆蓋、誤判與漏測 |
| 4. 單顆時間與負載 | 每個插入點要測多久？功率、接腳與溫控是否限制站數？ | Advantest 產品頁列出高功率、高接腳與長測試時間情境 | 同產品的實際秒數、功率、溫度、停機與換線時間 |
| 5. 多站與吞吐 | 一套設備同時測幾顆？並行效率和每小時產出是多少？ | 兩家設備商都把多站或並行效率列為產能手段 | 客戶實際站數、效率、可用率、良率及瓶頸設備 |
| 6. 良率、重測與漏測 | 低良率會增加重測，還是提早篩除後節省昂貴封裝？ | 來源只說明良率學習與已知良品篩選的重要性 | 各站良率、重測率、報廢成本、漏測率與改善前後結果 |
| 7. 既有設備與資本時點 | 新工作能否用原設備、載板和程式升級或重用？何時才需買新單元？ | Advantest、Teradyne 都主張平台升級或資產重用 | 已裝機量、剩餘時數、相容性、改機成本、交期與實際採購 |
| 8. 公司財務歸因 | 最後由誰提供設計、設備、介面或測試服務，收到多少錢？ | 公開資訊觀測站只提供後續查找入口 | 買方與供應商對上產品、數量、期間、售價、收入、毛利與現金 |

## 一顆複雜晶片會在哪些地方被測

測試不是一條固定流水線。IEEE 1838 的公開摘要把三維堆疊測試存取放在多個情境，說明工程上
需要跨階段設計；它沒有規定所有產品都必須使用下表每一站。

| 可能站點 | 主要問題 | 通過後仍不知道什麼 |
|---|---|---|
| 堆疊前晶粒測試 | 這顆裸晶是否值得投入後續封裝？ | 封裝後互連、熱與整合環境是否正常 |
| 部分或完整堆疊測試 | 新增鍵結與晶粒間連線後，是否出現組裝缺陷？ | 成品封裝與系統負載下的行為 |
| 封裝前後測試 | 封裝流程是否改變電性、功能或可靠度？ | 長時間應用、散熱與整機互動 |
| 成品測試 | 封裝晶片是否符合出貨規格？ | 實際軟體與系統工作負載下的邊緣問題 |
| 系統級測試與燒機 | 較長、較接近應用或壓力環境下是否失效？ | 全生命週期不會老化，也不保證沒有漏測 |
| 板級、機群與現場診斷 | 整機與運行階段能否偵測、隔離與重現錯誤？ | 根因一定在晶片，也不代表供應商已承擔維修責任 |

重點不是把站點數得越多越樂觀，而是問：新增哪一站、刪掉哪一站、每站測什麼、花多久、攔下
多少原本會流到下一站的缺陷。

## 同樣叫「測試」，七種決策不能相加

初學者最容易把 verification、wafer probe、final test、SLT、burn-in、qualification 與現場診斷
都看成同一種「測試」。它們可能共用部分程式、設備或故障知識，卻在回答不同問題；沒有先固定
受測物、目的與放行決定，測試次數和測試時間都不能相加。

| 本文七種決策 | 受測物與主要問題 | 結果交給誰、用來做什麼 | 不能直接併入哪個分母 |
|---|---|---|---|
| 1. 設計驗證與可測試性設計 | 在實體晶片完成前，功能、介面、時序與內部節點是否能被控制和觀察？ | 設計、驗證與測試工程據此修改 RTL、DFT、scan、記憶體自測或測試存取 | 模擬、形式驗證與 DFT 開發工時不是量產 tester cell-hours |
| 2. 製程量測與實體檢查 | 晶粒、凸塊、TSV、中介層、鍵結、翹曲與對位是否按製程做對？ | 製造與封裝工程用來調參、圍堵、重工或停止投入更多價值 | 看見結構完整不等於電性功能、長時間壽命或系統工作已通過 |
| 3. 晶圓與組裝中篩選 | 在切割、堆疊、接基板或完成封裝前，哪些晶粒或部分模組值得繼續投入？ | 晶圓圖、分 bin、已知良品與組裝決定交給封裝、測試及良率團隊 | 某一站通過不保證後續新增互連、封裝熱環境與軟體負載正常 |
| 4. 封裝後 final ATE | 封裝元件的結構、電性、功能、速度、功率與介面是否符合出貨規格？ | 量產測試依 bin、重測、報廢或放行規則處置每個受測單位 | 高結構覆蓋不等於所有複雜介面、稀有指令序列與實際工作負載都被激發 |
| 5. 系統級測試（SLT） | 元件放入較接近真實板卡或系統後，複雜介面、韌體與 mission-mode 工作是否正確？ | 產品、系統與量產工程處置 ATE 難以重現的功能或邊緣失效 | SLT 時間不能直接當 final ATE 時間，也不等於客戶場站已完成驗收 |
| 6. 燒機與可靠度資格 | 電壓、溫度、濕度、循環與時間壓力要篩早期失效，還是用樣品證明任務壽命與製程資格？ | 量產品質、可靠度、客戶與放行委員會依目的決定 100% 篩選、抽樣資格或設計改善 | 同樣叫 burn-in，若樣本比例、壓力、時間與決策不同，就不是同一個工作量 |
| 7. 現場診斷與退貨回饋 | 已部署產品在特定資料、負載、環境或老化後為何出錯，能否重現並隔離？ | 機群、RMA、失效分析、設計與製造把零件病歷轉成新測項、圍堵與修正 | 現場事件不一定是製造缺陷；也不能把 RMA 診斷時數倒算成原量產 tester 需求 |

Teradyne 的 S12 把 metrology、ATE、SLT 與多個封裝 insertion 分開；Amkor 的 S13 又把 wafer
probe、組裝中測試、final ATE、SLT 與 burn-in 分列。AMD 的 S14 則從另一端把 pre-silicon
verification、post-silicon validation、production exit 與客戶退貨 PPM 回饋分開；NXP 的 S15
明示 burn-in 可用來篩早期失效，而可靠度資格另要綁定 mission profile、加速條件與 read point。
這四份都是機構或公司的方法自述，不是所有 AI 晶片都必須照抄的固定流程。

## 一份測試責任護照至少有十欄

只寫「做過 wafer test」或「通過 SLT」像只保存考試名稱，卻沒有考生、版本、題目、考場與
及格線。要讓不同站點的結果可以交接、比較與回歸，研究時至少要把下列十欄綁在同一產品版本；
欄位未知可以留空，但不能用另一產品、另一站或設備最高規格補值。

| 護照欄位 | 必須固定什麼 | 少了這欄會怎麼誤讀 |
|---|---|---|
| 1. 受測物身分與版本 | lot、wafer、die、stack、package、module、board 或 system，以及設計、stepping、封裝與韌體版本 | 把不同世代或不同組裝狀態的結果當成同一顆產品趨勢 |
| 2. 生命週期與參考平面 | pre-silicon、wafer、pre-bond、mid-assembly、post-package、SLT、qualification 或 field，量測邊界到哪裡 | 用一站結果替尚未存在的互連、封裝、板卡或系統背書 |
| 3. 決策目的與責任人 | 除錯、製程調整、已知良品、分 bin、出貨放行、可靠度資格、客戶驗收或 RMA；誰有權簽核 | 看見 test 名稱卻不知道通過後允許哪個動作 |
| 4. 故障類別與失效機制 | 結構短開路、時序、記憶體、die-to-die、功率、熱、老化、軟錯或特定工作負載錯誤 | 把多測到一項功能誤寫成所有漏測風險都下降 |
| 5. 存取、DFT 與可觀察性 | scan、BIST、boundary scan、IEEE 1838 wrapper、probe pad、C4、socket 或系統介面如何控制與讀回內部狀態 | 標準允許存取就誤以為所有故障都可被同樣激發與定位 |
| 6. 刺激、負載與環境 | pattern、指令、資料、電壓、頻率、溫度、濕度、時間、功率與冷卻條件 | 在不同壓力和工作負載下比較 pass rate 或 test time |
| 7. Test-cell 組態與版本 | tester、prober／handler、probe card／load board／socket、溫控、校正、程式、韌體與軟體版本 | 把設備名稱相同當成測試能力、接觸品質與吞吐都相同 |
| 8. 抽樣、覆蓋與誤判 | 100% 或抽樣、site／pattern／fault coverage、false fail、escape、guardband 與重測規則 | 把樣品資格當成逐顆篩選，或把高覆蓋寫成零漏測 |
| 9. 結果、放行與沿革 | 原始結果、bin、fail signature、重測、報廢、wafer map、序號、簽核、fallback 與前後站關聯 | 只剩一個 pass badge，無法知道缺陷在哪站生成或被攔下 |
| 10. 變更與回歸條件 | 哪些設計、材料、製程、設備、程式、供應商、場站或現場失效會觸發哪些重測 | 把舊版本通過結果永久沿用到已改變的產品與流程 |

這份護照不是新的產業標準，也不是要求所有公司公開機密 recipe。它是研究中心的最小可比性
契約：只有受測物、目的、條件、結果與版本邊界相同，兩筆 test time、coverage、yield 或 UPH
才可能放進同一個分母；若公司只披露其中一欄，研究結論就只能停在那一欄。

## 哪些變更要觸發回歸重測

「已通過」只對當時護照有效。變更後也不必無差別重跑全部測項；正確做法是先把變更連到可能
受影響的故障類別、存取路徑、test cell 與放行決定，再保存重測範圍及理由。

| 變更類型 | 舊結果可能失效的原因 | 最少要留下的重測動作 | 對設備需求仍不能直接推論 |
|---|---|---|---|
| 晶片設計、stepping、DFT 或測試程式 | 內部邏輯、scan chain、記憶體、pattern、guardband 或故障模型改變 | 固定新舊版本、受影響 coverage、相關性與 bin migration，再重跑對應結構及功能測試 | 程式變長可能被 pattern 最佳化、並行或既有 tester 餘裕吸收 |
| 晶粒組合、堆疊、鍵結、封裝或材料 | 新互連、翹曲、熱阻、應力與裝配缺陷在舊參考平面不存在 | 重查 pre／post-assembly access、互連、熱、功率、機械與可靠度項目 | 新增 insertion 仍不表示每顆全測或必須買新 tester |
| Probe card、load board、socket、prober、handler 或溫控 | 接觸、寄生、電流、平坦度、對位、溫度與站數效率改變 | 重新校正、做 tester-to-tester／interface correlation，核對 false fail、UPH 與可用率 | 換介面可能改善吞吐，也可能只是維修或替代，不等於市場增量 |
| 製程 recipe、設備、工廠、封測站點或供應商 | 缺陷分布、材料、量測系統與可重現性可能改變 | 依 change control 做 qualification、lot correlation、良率與失效模式比較 | qualification 樣品與時間不能當成長期量產負載 |
| Mission profile、客戶規格、韌體或實際工作負載 | 原本沒有激發的功率、溫度、介面、指令與長時間條件可能出現 | 更新 validation／SLT／reliability matrix，保留新舊條件、exit criteria 與客戶簽核 | 客戶測試增加不等於已驗收、已部署或供應商收入增加 |
| 現場 escape、RMA 或新失效簽名 | 舊測項可能沒有覆蓋特定資料、環境、老化或稀有組合 | 將序號、lot、測試沿革、現場條件、根因與新增 pattern／screen 接回同一修正鏈 | 一個 RMA 不足以估算全體 defect rate、全線重測或 tester 台數 |

回歸矩陣的輸出應是「哪個版本、哪個風險、重跑哪些測項、由誰簽核、結果如何回到前後站」，
而不是一個沒有範圍的 `retest: yes`。只有重測後的新增工作超過並行、利用率、程式最佳化與既有
裝機餘裕，才可能繼續推到增量 test cell；再往公司收入走，仍要通過本文第八個財務分母。

## 為什麼測試時間增加，設備台數仍可能不線性增加

以下是研究用的量綱檢查，不是市場預測公式：

```text
需求的測試單元時數
≈ 出貨顆數 × 每顆插入點數 × 每插入點平均測試時數 × 重測係數
  ÷（同時站數 × 並行效率 × 可用率）
```

- 顆數、插入點與測試時間增加，分子上升。
- 同時站數提高，只有在電源、溫控、介面與資料傳輸都不成為瓶頸時，才可能降低單位所需時數。
- 並行效率不是站數本身；若不同待測元件互相等待、測項不能同步，八站不會自動得到八倍吞吐。
- 可用率要扣除換線、校正、維修、待料與程式除錯，產品頁最高能力不能直接當全年產出。
- 得到測試單元時數後，還要先扣既有設備的剩餘產能、升級與重用，才可能推到增量採購。

因此「測試時間變長」與「新增 tester 台數」中間至少隔著並行、利用與裝機餘裕三個分母；
反過來，「多站並行」也不能證明需求下降，因為產品量、插入點和覆蓋可能同時增加。

## 五組數字不能直接排高低

### 先保留原本的三份需求觀測

| 公司資料 | 這份資料直接說了什麼 | 讀完仍不能下什麼結論 |
|---|---|---|
| Advantest 2026-07-29 | Advantest 預估 CY2026 測試機市場為 130–145 億美元（SoC 105–115 億、memory 25–30 億），較 4 月中值約增 19%。公司把 AI 晶片產量與複雜度，尤其推論 ASIC、CPU、DRAM，列為需求因素。 | 這只是 Advantest 的市場預估。公司在 Q&A 明說無法拆分 GPU、CPU、ASIC 各自貢獻，而且 GPU 目前仍是最大市場。 |
| Amazon 2026-07-30 | Amazon 表示 AWS 晶片業務年化營收超過 250 億美元、年增三位數；Trainium 已取得 Anthropic、OpenAI 的多年、多 GW 承諾。 | 250 億美元包含 Graviton、Trainium 與 Nitro，不能全部算成 Trainium。容量承諾也不是晶片採購金額，Amazon 同時仍大量採用 NVIDIA。 |
| Microsoft 2026-07-29 | Microsoft 表示 Maia 200 已支援 OpenAI 與 MAI models，且仍在擴大。相較自有機隊最新硬體，每美元效能高 30%，MAI models 的每瓦效能高 40%。 | 比較只限 Microsoft 自有機隊，沒有點名擊敗特定 GPU。同一段也明說自研晶片與 NVIDIA、AMD 並行。 |

**三組數字的時間、單位與定義不同。** 它們分別是設備市場預估、晶片業務年化營收規模與相對
效能比，不能橫向排名或加總。下方 `M1` 保留在被 C6 取代的早期 C2 框架中，作為研究版本沿革；
數字本身沒有被改寫。

**本文只把它們放進同一個研究問題。** 比較帳本 `M1` 將它們判定為不可直接比較
（`not_comparable`）；用途只是交叉觀察推論算力需求。

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O1
claim_id: C2
entity: Advantest
metric: SoC and memory tester TAM forecast
value_kind: range
reported_value: 13.0..14.5
period_start: 2026-07-29
period_end: 2026-07-29
period_basis: management_forecast_observed_on_2026-07-29_for_CY2026_horizon
unit: USD_billion
definition_key: soc_memory_tester_tam_forecast
definition: 2026-07-29 發布、預測涵蓋 CY2026 的 SoC 與 memory tester 整體可服務市場區間
evidence_ids: S1,S4,S5
comparability: not_comparable
comparability_reason: 這是設備市場全年預估，不是雲端晶片收入或單一晶片效能指標
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O2
claim_id: C2
entity: Amazon
metric: AWS chips business annualized revenue run rate
value_kind: lower_bound
reported_value: 25
period_start: 2026-06-30
period_end: 2026-06-30
period_basis: annualized_run_rate_as_of_quarter_end
unit: USD_billion_per_year
definition_key: aws_chips_business_annualized_revenue_run_rate
definition: Graviton、Trainium 與 Nitro 合計 chips business 的年化營收規模
evidence_ids: S2
comparability: not_comparable
comparability_reason: 這是多項 AWS 晶片業務的年化收入速度，不是 tester TAM、採購金額或 Trainium 單項收入
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: heterogeneous_evidence
observation_id: M1-O3
claim_id: C2
entity: Microsoft
metric: Maia 200 performance per dollar improvement
value_kind: point
reported_value: 30
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal_quarter_management_comparison
unit: percent
definition_key: maia_200_performance_per_dollar_vs_latest_fleet_hardware
definition: Maia 200 相對 Microsoft fleet 最新硬體的 performance per dollar 改善幅度
evidence_ids: S3
comparability: not_comparable
comparability_reason: 這是公司自有硬體基準的相對效能比，不是收入、TAM、晶片出貨量或跨公司 benchmark
-->

### 再看兩個不能互比的產能數字

| 產品頁觀測 | 直接說了什麼 | 為什麼不能拿來算市場台數 |
|---|---|---|
| Advantest 7038 | 產品頁寫「最多」可同時容納 720 個待測元件，並另列特定長測試情境下的每小時產出能力 | 這是系統級測試／燒機平台的條件式上限，沒有客戶產品、實際站數效率、可用率與良率 |
| Teradyne UltraFLEXplus | 產品頁宣稱較高站數與並行效率可讓所需測試單元減少 15%–50% | 這是相對效益區間，沒有公開比較基準、產品、測試程式、原始單元數與生產實績 |

這兩筆 `M2` 觀測一筆是待測元件容量上限，一筆是供應商宣稱的相對測試單元降幅。即使都談
吞吐，也沒有共同分子、分母與測試階段，所以裁決仍是 `not_comparable`。

<!-- metric_comparison
comparison_id: M2
comparison_kind: heterogeneous_evidence
observation_id: M2-O1
claim_id: C5
entity: Advantest
metric: 7038 simultaneous DUT capacity
value_kind: upper_bound
reported_value: 720
period_start: 2026-08-12
period_end: 2026-08-12
period_basis: current_product_page_captured_on_2026-08-12
unit: DUT_count
definition_key: advantest_7038_simultaneous_dut_capacity_upper_bound
definition: Advantest 7038 現行產品頁所列可同時容納待測元件數的 up to 上限
evidence_ids: S9
comparability: not_comparable
comparability_reason: 這是特定 SLT／burn-in 平台的條件式 DUT 容量上限，不是實際有效站數、全年吞吐、tester 台數或相對節省率
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: heterogeneous_evidence
observation_id: M2-O2
claim_id: C5
entity: Teradyne
metric: claimed reduction in required test cells
value_kind: range
reported_value: 15..50
period_start: 2026-08-12
period_end: 2026-08-12
period_basis: current_product_page_captured_on_2026-08-12
unit: percent
definition_key: teradyne_ultraflexplus_claimed_test_cell_reduction
definition: Teradyne UltraFLEXplus 現行產品頁把較高 site count 與 parallel test efficiency 連到所需 test cell 的宣稱降幅區間
evidence_ids: S10
comparability: not_comparable
comparability_reason: 這是沒有公開共同基準、產品、程式與客戶生產結果的相對宣稱，不能與 DUT 容量、UPH 或市場設備需求互換
-->

## 產業角色不要混在一起

| 角色 | 解決什麼問題 | 本研究中心怎麼查 | 不能替誰背書 |
|---|---|---|---|
| 雲端與平台買方 | 決定工作負載、晶片組合、部署節奏與驗收條件 | Amazon、Microsoft 等一手部署文件 | 不能證明指定測試設備、介面或台灣供應商訂單 |
| 晶片設計、矽智財與可測試性設計 | 把 scan、記憶體自測、測試存取與產品規格放進設計 | `ipdesign` 族群追具名專案、設計交付、tape-out 與量產 | 不能用平台晶片存在就推定設計服務收入 |
| 自動測試設備商 | 提供量測儀器、時序、電源、資料處理與測試平台 | Advantest、Teradyne 用來建立全球工具與產能分母 | 產品最高能力不能替客戶實際利用率與採購背書 |
| 測試介面、探針卡、載板與測試座 | 把設備訊號可靠地送到晶圓或封裝晶片 | `semiequip` 族群追具名介面、接腳、功率、資格與出貨 | tester 市場規模不能直接當介面市場或個股市占 |
| 探針台、分類機、溫控與自動化 | 搬運、定位、接觸、控溫並維持單元可用率 | 追同一測試單元配置與瓶頸，不只看 tester | 任一設備規格不能代表整個 test cell 的吞吐 |
| 封裝測試服務商 | 執行晶圓針測、成品測試、系統級測試或燒機並承擔良率與交期 | `packtest` 族群追測項、插入點、產能、稼動率、報價與毛利 | 有封測能力不等於已取得特定 AI 專案 |

## 同一個 test cell，會開出三種不同的發票

一個 test cell 在工程上可能同時包含 tester、prober／handler、探針卡／測試板／測試座、溫控與
自動化；商業上卻不會由一家公司只開一張總發票。三份台灣公司正式資料把差異顯示得很清楚：
測試服務商按製程呈現收入，介面商按產品呈現收入，兼營探針卡與設備的公司又同時帶著兩個時鐘。

| 證據個案（不是同儕排名） | 正式資料直接揭露什麼 | 研究上要追哪個收入與成本時鐘 | 這份資料仍不能回答什麼 |
|---|---|---|---|
| 京元電子：測試服務 | 2026Q1 製程收入為產品／成品測試 58.9%、晶圓測試 32.1%、預燒 7.3%、封裝 1.4%、其他 0.3%；同季營運現金流 37.42 億元、資本支出 67.86 億元，公司自定義自由現金流為負 21.49 億元 | 先重建可計費 test-cell 時數、費率、利用率、折舊、人力、電力與良率；設備先買而需求或認證延後時，現金與折舊可能早於收入 | 「資料處理」或「產品測試」有多少來自 AI、哪個專案用了多少秒、多少站、何種設備、稼動率、單價與產品毛利 |
| 中華精測：介面產品 | 2026Q2 收入 16.40 億元；晶圓測試卡占 76%、IC 測試板 18%、技術服務與其他 6%；公司定義自由現金流為營運現金流 2.57 億元減資本支出 0.89 億元，得到 1.68 億元 | 先追合格組態數、交付量、平均售價、探針／板／零件自製、良率、維修與更換週期；客戶 tester 忙碌不等於介面商同季等比例認列收入 | 具名晶片、插入點、介面數量與 ASP、客戶、產品別毛利、測試機時；這份法說也不是含完整附註的 Q2 核閱財報 |
| 旺矽：介面與設備混合 | 2026Q1 合併營收 39.33 億元，探針卡占 71.1%、設備 26.9%、其他 2.0% | 探針卡要走資格、交付、維修與汰換時鐘；設備要另走訂單、製造、交機、安裝、驗收、升級與服務時鐘，先拆線才能談組合 | 兩條產品線各自金額、訂單、數量、ASP、毛利、現金流與客戶，也不能把 26.9% 設備全部視為 ATE tester |

### 先做三張單位經濟卡，再談誰受惠

1. **測試服務卡：** `可計費 test-cell 時數 ≈ 合格測試量 × 實際插入點 × 每站秒數 × 重測係數 ÷（同時站數 × 並行效率）`。再加上計價方式、利用率、停機、折舊、人力與電力，才可能連到服務收入和毛利；公司若按顆、按秒、按專案或混合計價，還要另留契約欄。
2. **介面產品卡：** `介面收入 ≈ 合格組態的交付量 × 平均售價 + 維修／更換／服務`。針數、功率、間距與散熱可提高難度，卻仍要通過客戶資格、量產良率、交期與壽命；tester 多跑一小時不會自動多賣一張探針卡。
3. **設備產品卡：** `設備收入 ≈ 新機與升級交付量 × 各自平均售價`。訂單、出貨、安裝、驗收、收入與收款可能在不同季度；已裝機平台也可能用升級及重用吸收新工作，所以 tester TAM 不能直接當設備收入。

兩家公司都寫「自由現金流」，公式卻已不同：中華精測明列營運現金流減資本支出，京元電子則從
營業利益、折舊攤銷、利息、稅、非控制權益與股利等項目建構公司口徑。負 21.49 億元與正 1.68
億元因此不能直接排序，更不能拿來推論哪種商業模式較好。三份文件是為辨認角色而定向選取的
`N=3` 個案，不是台灣測試產業的統計樣本，沒有抽樣標準誤或 t 值。比較帳本 `M3` 因此把三筆
占比明確裁為 `not_comparable`；它保存公司原始口徑，不建立跨公司排名。

<!-- metric_comparison
comparison_id: M3
comparison_kind: heterogeneous_evidence
observation_id: M3-O1
claim_id: C10
entity: 京元電子
metric: product and final test revenue share
value_kind: point
reported_value: 58.9
period_start: 2026-01-01
period_end: 2026-03-31
period_basis: company_reported_2026Q1_process_revenue_mix
unit: percent_of_company_revenue
definition_key: kyec_product_final_test_share_of_company_revenue
definition: 京元電子 2026Q1 營運報告的產品／成品測試製程收入占合併營收比例
evidence_ids: S16
comparability: not_comparable
comparability_reason: 這是測試服務商的製程收入占比，不是介面產品占比、設備占比、AI 收入、test-cell 時數或市場份額
-->

<!-- metric_comparison
comparison_id: M3
comparison_kind: heterogeneous_evidence
observation_id: M3-O2
claim_id: C10
entity: 中華精測
metric: wafer test card revenue share
value_kind: point
reported_value: 76
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: company_reported_2026Q2_product_revenue_mix
unit: percent_of_company_revenue
definition_key: chpt_wafer_test_card_share_of_company_revenue
definition: 中華精測 2026Q2 營運報告的晶圓測試卡收入占合併營收比例
evidence_ids: S17
comparability: not_comparable
comparability_reason: 這是介面產品收入占比且期間為 Q2，不是測試服務製程、設備收入、測試機時或市場份額
-->

<!-- metric_comparison
comparison_id: M3
comparison_kind: heterogeneous_evidence
observation_id: M3-O3
claim_id: C10
entity: 旺矽
metric: probe card revenue share
value_kind: point
reported_value: 71.1
period_start: 2026-01-01
period_end: 2026-03-31
period_basis: company_reported_2026Q1_product_revenue_mix
unit: percent_of_company_revenue
definition_key: mpi_probe_card_share_of_company_revenue
definition: 旺矽 2026Q1 業績摘要的探針卡收入占合併營收比例
evidence_ids: S18
comparability: not_comparable
comparability_reason: 旺矽同時包含探針卡與設備兩條產品線；該占比不是測試服務、純介面同儕比較、AI 收入或市場份額
-->

## 新手最常混淆的八件事

1. **市場規模不等於公司收入。** tester TAM 是全球工具市場估計，台灣設計、封測與介面公司的商業模式和分母都不同。
2. **晶片顆數不等於設備台數。** 產品組合、插入點、每顆時間、同時站數與既有設備餘裕會改變換算。
3. **標準涵蓋不等於每站必測。** IEEE 1838 提供存取架構；產品團隊仍要依風險、成本與良率決定插入點。
4. **測試時間變長不等於線性增機。** 多站、並行效率、可用率與升級重用可能吸收一部分工作量。
5. **產品頁最高值不能互相比。** 待測元件上限、每小時產出、相對單元降幅與市場金額不是同一量綱。
6. **平台部署不等於台灣公司受惠。** 必須由買方與供應商對上同產品、期間、數量、收入、毛利與現金。
7. **資格驗證不等於 100% 量產篩選。** 同樣使用 burn-in 或壓力測試，樣品、逐顆、時間、目的與放行權限不同，工作量就不能相加。
8. **舊版本通過不等於變更後仍通過。** 晶片、封裝、介面、程式、製程或工作負載改變，要先做影響分析並重跑受影響測項。

## 在研究中心接著怎麼學

1. **先讀「小晶片設計資料交接與合規鏈」。** 理解介面能連線後，設計資料、測試存取與製造封測仍要共同簽核。
2. **再讀 High-NA EUV 與混合鍵結。** 把製程能力、鍵結與多晶粒封裝的資格階段放回實體製造。
3. **回到本文。** 用八個分母判斷產品複雜度如何變成實際量產測試工作，而不是直接乘上市場故事。
4. **最後讀「AI 硬體 SDC 生命週期」。** 量產測試通過不是終點；運行中仍要偵測、隔離、重測並把零件病歷回饋製造端。

這條順序只服務學習：設計交接、製程封裝、量產測試與運行回饋不是單一公司的上下游受惠鏈，
也不表示任何一站已完成商業歸因。

## 來源與證據邊界

- [Advantest FY2026 Q1 簡報](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_slide.pdf)（p.12，2026-07-29）。
- [Advantest 簡報附註](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf)（tester market 段落，2026-07-29）。
- [Advantest Q&A](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)（pp.1–2，2026-07-29）。
- [Amazon 2026Q2 結果](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)（2026-07-30）。
- [Microsoft FY2026Q4 法說逐字稿](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)（2026-07-29）。
- [IEEE 1838 現行標準摘要](https://standards.ieee.org/ieee/1838/5073/)（2026-08-12 捕捉）。
- [Advantest V93000 EXA Scale](https://www.advantest.com/en/products/semiconductor-test-system/soc/v93000/)（2026-08-12 捕捉）。
- [Advantest 7038 SLT／Burn-In](https://www.advantest.com/en/products/component-test-system/system-level-test-systems/7038/)（2026-08-12 捕捉）。
- [Teradyne UltraFLEXplus](https://www.teradyne.com/products/ultraflexplus/)（2026-08-12 捕捉）。
- [Teradyne test-cell ecosystem](https://www.teradyne.com/2026/06/15/the-test-cell-ecosystem-from-tester-performance-to-production-outcomes/)（2026-06-15）。
- [Teradyne chiplet test insertions](https://www.teradyne.com/2026/07/27/ai-chiplet-architectures-redefining-test-insertions/)（2026-07-27）。
- [Amkor IC test services](https://amkor.com/test-services/)（2026-08-12 捕捉）。
- [AMD design and development](https://www.amd.com/en/corporate/quality/design-development.html)（2026-08-12 捕捉）。
- [NXP product qualification](https://www.nxp.com/products/nxp-product-information/quality/product-qualification%3AQUALITY__QUALIF)（2026-08-12 捕捉）。
- [京元電子 2026Q1 營運報告](https://www.kyec.com.tw/Common/Download?faname=CE9C12F9789DF09DB07AD813BD5475688BEAD13771DE3682E1557C949D18AADCBC1CA2FE6409102AE04ABAA1E80DB9551E6AE8CB84DA42B60CA4CFCBFBE8C3C1975FCB01637C8125A0F6E112F17D377B7B9D286F3E2741BDAAEFB35D0B5248527223686E9D7CE1A7)（pp.3–9，2026-05-08）。
- [中華精測 2026Q2 營運報告](https://www.cht-pt.com.tw/files/file_pool/1/0Q209650487702138855/26Q2%20%E6%B3%95%E8%AA%AA%E6%9C%83_CN.pdf)（pp.3、11–19，2026-07-29）。
- [旺矽 2026Q1 業績摘要](https://www.mpi-corporation.com/wp-content/uploads/2026/05/2026-Q1-Quarter-Result_0515%E5%AF%8C%E9%82%A6_2-page_EN.pdf)（第 1–3 頁，2026-05-15）。

18 份來源是定向證據集合，不是產業抽樣，所以本文不計算標準誤；它們只覆蓋市場方向、平台部署、
測試存取範圍、供應商自述產品能力、設計／量產／資格責任邊界，以及三家公司不同季度的收入分類。
來源沒有共同產品的晶片數、插入點、實際時間、站數效率、利用率、良率、既有裝機餘裕或增量採購，
也沒有點名 3035、3443、3661、6533 的新 NRE／
tape-out／量產案，或 2449、3264、6257、6223、6510、6515 的訂單、稼動率、平均售價與市占。

IEEE、設備商、封測服務商與晶片公司的方法頁不是十八條完全獨立證據鏈：S8、S9 同屬 Advantest，
S10–S12 同屬 Teradyne；S13、S14、S15 分別提供封測、設計生命週期與可靠度資格的另一個角色，
S16–S18 則分屬京元電子、中華精測與旺矽，但期間、格式與收入分類不同，也沒有同一具名產品的共同
結果。這些來源可用來界定「要量什麼、誰做哪個決定、由哪種收入時鐘收錢」，不能當成已實現的
市場平均。由於本輪也沒有一致預期、估值與即時持倉資料，不宣稱這些公司「尚未反映」或市場上修
必然造成倍數擴張。

## 傳導與投資判讀

```text
推論工作負載擴張
  → 產品組合與合格出貨量
  → 測試插入點 × 內容覆蓋 × 單顆時間／功率／接腳／熱
  → 再除以同時站數 × 並行效率 × 可用率，並納入良率與重測
  → 扣除既有設備餘裕、升級與重用後，才可能形成增量 test cell
  → 買方與供應商以同產品、期間和分母對帳，才可能形成台股公司財務證據
```

- **工作量分子**：同產品的合格出貨顆數、插入點、測試內容與時間、重測率。
- **產能分母**：同時站數、並行效率、可用率、既有設備餘裕、升級與重用比例。
- **公司轉換**：具名介面或測試服務、客戶資格、出貨期間、稼動率、平均售價、收入、毛利與現金。
- **常見假訊號**：把雲端資本支出、AWS 晶片年化營收、產品頁最高能力或 Advantest TAM 全數映射到單一台灣供應商。
- **最關鍵分歧**：新增內容量是否超過並行與既有產能吸收量，並真的跨過增量採購與公司財務兩關。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids: 3035,3443,3661,6533
direction: mixed
hypothesis_refs: 3035:H1,3035:H2,3443:H1,3443:H2,3661:H1,3661:H2,6533:H1
note_action: review_due
action_due: 2026-08-15
rationale: 先固定具名產品與合格出貨量，再核對可測試性設計、測試插入點、NRE、tape-out、量產與收入；不能由雲端晶片部署跳過測試內容及公司財務分母
evidence_boundary: Amazon、Microsoft、IEEE 與設備商均未指認這四家公司，也未證實專案、設計交付、測試內容、收入或毛利
-->

<!-- impact
group_id: packtest
stock_ids: 2449,3264,6257
direction: mixed
hypothesis_refs: 2449:H1,2449:H2,3264:H1,6257:H1,6257:H2
note_action: review_due
action_due: 2026-08-15
rationale: 依產品組合、插入點、時間、站數、並行效率、良率重測與既有設備餘裕，核對 AI 測試專案是否真的形成新增產能、稼動率與報價
evidence_boundary: tester TAM、IEEE 存取情境與設備商產品能力都不等於台灣測試廠的具名專案、實際 test cell、稼動率、報價或客戶歸屬
-->

<!-- impact
group_id: semiequip
stock_ids: 6223,6510,6515
direction: mixed
hypothesis_refs: 6223:H1,6223:H2,6510:H1,6510:H2,6515:H1,6515:H2
note_action: review_due
action_due: 2026-08-15
rationale: 先對上具名插入點、接腳與功率、探針卡／載板／測試座、站數與重用，再追公司接單、產能、平均售價與毛利
evidence_boundary: 兩家全球設備商均未點名本 universe 測試介面廠，不能由 tester TAM、最高 DUT 容量或宣稱 test-cell 降幅推導個股市占與獲利
-->

## 持續驗證清單

T1 的 2026-08-08 `not_yet_testable` 回查仍保存在 append-only review ledger；它沒有刷新 evidence
clock。新主命題改由 T3、T4 接續，責任護照與變更重測由 T5 追蹤；`review_due` 2026-08-15 等於 active monitor 最早的
`next_check`。

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C2
metric: Advantest tester TAM、訂單與實際出貨
source_ids: S1,S4,S5
watch_source_ids: S6
frequency: event_driven
next_check: 2026-08-08
trigger: Advantest 更新 2026 tester TAM，或揭露 AI 相關 tester 的訂單與實際出貨
invalidation: TAM 區間下修、推論專案延後，或估計未轉成設備訂單與出貨
retired_at: 2026-08-12
retirement_reason: T1 的 2026-08-08 到期回查已記為 not_yet_testable 並把觀測窗對齊 2026-10-30；C2 又由八分母 C6 取代，後續由 T3 接續市場、test-cell 與抵銷因素
-->

<!-- monitoring_item
monitor_id: T2
status: retired
claim_ids: C2,C3
metric: 自研晶片部署與台灣供應商可辨識財務貢獻
source_ids: S2,S3,S6
watch_source_ids: S6
frequency: quarterly
next_check: 2026-08-15
trigger: Amazon 或 Microsoft 揭露實際部署，且台灣公司文件出現 NRE、量產、稼動率、收入與毛利證據
invalidation: 自研晶片時程延後，或台灣公司只有題材與擴產而沒有量產及獲利交叉證據
retired_at: 2026-08-12
retirement_reason: C2 的晶片數量與複雜度粗框架已由 C6 取代；原 2026-08-15 台灣公司檢查期限不延後，改由 T4 以產品、測試單元與財務分母接續
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C4,C5,C6,C7
metric: Advantest tester TAM 與同產品的數量、插入點、測試內容／時間、站數效率、利用率、既有設備餘裕及增量 test cell
source_ids: S1,S4,S5,S7,S8,S9,S10,S11
watch_source_ids: S8,S9,S10
frequency: event_driven
frequency_detail: 下一次 Advantest 展望，或任一來源首次提供可對帳的同產品 test-cell 分母時重審
next_check: 2026-10-30
trigger: 新展望更新 TAM，或來源同時披露具名產品的顆數、插入點、時間、站數、效率、利用率、既有裝機與新增設備／訂單
invalidation: 市場區間下修，或更高並行、利用與重用足以吸收內容量，使增量測試單元與設備訂單未形成
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C3,C6,C7,C10,C11
metric: 台灣設計、封測、測試介面與設備公司的具名產品、收入單位、test-cell 角色、資格、利用率及可辨識財務貢獻
source_ids: S2,S3,S6,S8,S11,S16,S17,S18
watch_source_ids: S6
frequency: quarterly
frequency_detail: 公司季報、法說或重大訊息發布時，以八分母與買賣雙向文件逐項核對
next_check: 2026-08-15
trigger: 台灣公司與客戶對上同產品、插入點、設備／介面、出貨期間、數量、利用率、平均售價、收入與毛利
invalidation: 公司只談 AI、測試需求或擴產，沒有具名測試角色、量產分母與可辨識財務結果
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C8,C9
metric: 具名產品的測試責任護照、前後站結果沿革與變更觸發回歸重測
source_ids: S7,S12,S13,S14,S15
watch_source_ids: S13,S14,S15
frequency: event_driven
frequency_detail: 封裝、晶片或客戶首次公布同一產品的完整 insertion、test configuration、exit criteria、change control 或 RMA feedback 時重審
next_check: 2026-09-15
trigger: 同一具名產品與版本公開受測物、插入點、故障類別、DFT／介面、刺激環境、抽樣覆蓋、設備程式、pass／fail、責任人、變更與重測結果
invalidation: 供應商通用流程無法對到實際產品，或新增 insertion／重測被程式最佳化、並行、重用及既有產能吸收，未形成增量 test-cell 工作量
-->

## 下一個可證明／否定的節點

- Advantest 下一次展望是否維持 130–145 億美元 CY2026 tester TAM；若維持，能否首次把變動拆到同產品的顆數、插入點、測試時間、站數效率、利用率與增量設備。
- Amazon、Microsoft 的實際部署能否對到測試參考平面；多年容量承諾、年化營收與效能比仍不能替設備採購背書。
- 矽智財公司是否揭露具名設計、可測試性工作、NRE、tape-out、量產與收入；未點名客戶時不得自行補上 AWS、Meta 或 Microsoft。
- 封測與測試介面公司是否對上同一產品、插入點、設備／介面、稼動率、平均售價、收入與毛利；若只有擴產或全球市場上修，證據不足。
- 任一具名產品能否第一次公開同一份測試責任護照與變更重測結果；只有 test 名稱、設備能力或 qualification 宣稱，仍不能把不同目的的時數加總。
- 若市場下修、平台延期，或並行與重用吸收新增內容量，應下修增量設備假說；不得只用股價反應續留。
