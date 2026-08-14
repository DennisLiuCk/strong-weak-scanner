# 新記憶體層不能只靠大容量：HBF 還要通過讀寫、耐久、系統整合與量產

<!-- research_topic
topic_id: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-02-25
last_reviewed_at: 2026-08-12
review_due: 2026-08-26
source_type: mixed
publisher: Sandisk and SK hynix
publisher_domain: sandisk.com
canonical_url: https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf
source_chain_id: hbf-standardization-sampling-20260802
stock_ids:
group_ids: memory,packtest
trigger_type: memory_standardization_and_sampling_ladder
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C9
base_confidence: medium
confidence_basis: Sandisk 與 SK hynix 的聯合規格公告及 SK hynix 技術摘要可確認第一版 HBF 技術規格已對外發布，並列出介面、堆疊容量、頻寬等級、封裝可靠度與軟體讀寫範圍；但本輪未獨立取得可定位版本的 OCP 規範原文，實體樣品、合規互通、客戶資格、裝置整合、量產及財務貢獻也尚未被證實
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_hbf_scan
evidence: source_chain:hbf-standardization-sampling-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_standardization_memory_sample_device_sample_qualification_and_production
evidence: sources:S1,S2,S3,S4
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Sandisk and SK hynix
title: Sandisk and SK hynix Begin Global Standardization of Next-Generation Memory Solution High Bandwidth Flash
published_at: 2026-02-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf
locator: 標題下方 workstream 摘要與正文第 1 至 5 段；兩家公司將在 OCP 建立 HBF 專屬 workstream
limitation: 聯合公告證實合作與設計方向，不證明規格已完成、樣品已交付、客戶採用或量產
independence_group: sandisk-sk-hynix-joint
-->

<!-- research_source
source_id: S2
role: standard
source_kind: living_index
publisher: Open Compute Project
title: OCP Semi-Private Workstreams
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.opencompute.org/community/semi-private-workstreams
locator: 2026-08-02 的 Storage 分類列出 High Bandwidth Flash workstream
limitation: 動態工作組索引只能確認 OCP 目前列有 HBF；不提供公開規格內容、版本、合規結果或產品成熟度
independence_group: open-compute-project
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SK hynix Presents Vision at TSMC Symposium 2026
published_at: 2026-04-23
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://news.skhynix.com/en/tsmc-technology-symposium-2026/
locator: The Way Forward in the AI Era 段落；HBF 註解將其定義為 NAND solution、KV cache 應用並使用 logic process base die
limitation: 技術願景與展示不等於最終產品規格、實測結果、客戶樣品、qualification 或出貨
independence_group: sk-hynix
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Sandisk
title: Memory-Centric AI Sandisk High Bandwidth Flash Will Redefine AI Infrastructure
published_at: 2025-08-11
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom/blogs/2025/memory-centric-ai
locator: NAND reimagined、Finding allies 與 Looking forward；目標於 2026 下半年交付首批 HBF memory samples、2027 年初送出首批 HBF inference device samples
limitation: 時程與效能敘述是公司目標及內部模擬；截至本輪不是已完成的樣品、獨立 benchmark、客戶資格或商業出貨
independence_group: sandisk
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Sandisk
title: Sandisk Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.sandisk.com/company/newsroom
locator: 2026-08-02 查得 Sandisk 新聞、部落格與 HBF 後續附件入口
limitation: 新聞索引只供未來重查；新標題不能替代文件內容、樣品交付或客戶證據
independence_group: sandisk
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: SK hynix
title: SK hynix Press Center
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://news.skhynix.com/press-center/press-release/
locator: 2026-08-02 查得 SK hynix HBF、AI NAND、樣品與量產更新入口
limitation: 動態新聞索引不能證明 HBF 有新規格、客戶樣品、量產或收入；須另登錄實際附件
independence_group: sk-hynix
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: document
publisher: Sandisk and SK hynix
title: Sandisk and SK hynix Advance Global Standardization of High Bandwidth Flash Technology
published_at: 2026-08-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://investor.sandisk.com/news-releases/news-release-details/sandisk-and-sk-hynix-advance-global-standardization-high
locator: 第一版 HBF technical specification 發布、xPU-HBF host interface、electrical、performance、reliability／packaging、software read／write，以及 Google／Tenstorrent consortium membership 段落
limitation: 聯合公告摘要不是本輪可逐條核對的 OCP 規範原文；Google 與 Tenstorrent 參與 consortium 也不等於獨立採用、產品 qualification、互通通過或部署
independence_group: sandisk-sk-hynix-joint-spec
-->

<!-- research_source
source_id: S8
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SK hynix Unveils HBF Standard Specification and AI Memory Vision at FMS 2026
published_at: 2026-08-04
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://news.skhynix.com/en/hbf-at-fms-2026/
locator: 第一版 standard specification、8-high／16-high、最高 512GB、約 0.4 至 3.0 TB/s 三個 bandwidth grades、UCIe、reliability／packaging 與 software I/O 段落
limitation: 這是 SK hynix 對同一共同規格的公司摘要，不是獨立產品實測或直接 OCP normative document；容量與頻寬是規格包絡，不是已交付樣品的量測結果
independence_group: sandisk-sk-hynix-joint-spec
-->

<!-- research_source
source_id: S9
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SK hynix Showcases Full-Stack AI Memory Portfolio at FMS 2026
published_at: 2026-08-07
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://news.skhynix.com/en/fms-2026/
locator: Tiered Memory Architecture 段落；將 HBM、DRAM、NAND-based HBF 與 SSD 分層，並強調減少資料搬移及 hardware／software co-design
limitation: 展會回顧提供供應商架構敘事，不是具名部署、共同 benchmark、客戶資格、樣品交付或收入證據
independence_group: sk-hynix
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: document
publisher: Sandisk
title: Q4 FY26 Earnings Presentation
published_at: 2026-08-05
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://investor.sandisk.com/static-files/c75d1bee-c5c9-4e5a-8605-302c1aeac59b
locator: 第 2 頁 portfolio overview 的 advanced HBF；其後財務頁按公司與 end market 揭露，未提供 HBF 獨立分子
limitation: 簡報在組合層級提到 HBF，沒有揭露 HBF sample、qualification、shipment、revenue 或 margin；公司與終端市場數字不能倒推為 HBF 貢獻
independence_group: sandisk
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: document
publisher: Sandisk
title: HBF Fact Sheet
published_at: 2025-07-29
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf
locator: PDF 第 1 至 3 頁；第 2 頁列 Gen 1 讀取頻寬 1.6 TB／s、256Gb per die 與 16-die stack 512GB，第 3 頁腳註把 2.2% 主張限定為內部測試／模擬、讀取 Llama 3.1 405B 的 8-bit pretrained weights、一次一個 kernel、HBM 容量假設無限，並明示 HBF 較高 latency、較大 page size、actual user capacity less；本地檔案 SHA-256 349f05372fb528702d2fe95ec8f3a9cb9b4dd976c7d115a3db49f26031b10111，3／3 頁已逐頁渲染核對
limitation: 供應商 fact sheet 的 Gen 1 數字、2.2% 與未來 roadmap 是產品目標及內部模擬，不是實體 HBF sample、公開 raw logs、共同 benchmark、延遲／寫入／耐久結果、客戶 qualification 或量產；文件也明示規格可能變更
independence_group: sandisk
-->

<!-- research_source
source_id: S12
role: standard
source_kind: living_index
publisher: MLCommons Association
title: MLPerf Inference Rules
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc
locator: 2026-08-14 查得 Definitions、Scenarios、Benchmarks 與 LoadGen Operation；system under test 綁硬體與軟體，run 包含 queries、pre／post-processing、scenario latency 與 quality，現行 LLM 規則另分 TTFT／TPOT，並列 Llama3.1-405B 的資料集、品質與 scenario-specific latency 契約
limitation: MLPerf 是推論系統 benchmark contract，不是 HBF 規格或 HBF 實測；它不能證明 Sandisk 模擬符合 MLPerf、隔離單一記憶體因果、代表 production workload，或建立樣品、客戶與財務證據
independence_group: mlcommons-inference
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Sandisk 與 SK hynix 於 2026-02-25 公告共同推進 HBF 標準化，並表示會在 Open Compute Project 建立專屬 workstream；OCP 的工作組索引截至 2026-08-02 也列有 High Bandwidth Flash
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-02
basis: S1 的聯合公告直接說明合作與 OCP workstream，S2 由 OCP 自身索引交叉確認工作組存在
boundary: 工作組成立不等於規格 ratified、介面穩定、合規計畫完成或多廠產品已互通
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
claim: SK hynix 將 HBF 描述為面向 KV cache 等大量運算資料的下一代 NAND solution，並表示其像 HBM 一樣在 base die 使用 logic process 以提高資料傳輸能力
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-04-23
basis: S3 的 HBF 註解直接定義 NAND、KV cache 與 logic base die
boundary: 技術定位不證明所有推論工作負載都適用，也不證明延遲、寫入、耐久、熱與軟體調度已達客戶要求
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
claim: Sandisk 的公開目標是於 2026 年下半年交付首批 HBF memory samples，並預期首批整合 HBF 的 AI inference device samples 在 2027 年初出現
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-08-11
basis: S4 Looking forward 直接列出兩個目標時點
boundary: 這是前瞻目標，不是截至 2026-08-02 已交付樣品、已通過客戶測試或已量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: superseded
claim: HBF 目前最合理的成熟度定位，是一個已由單一公司概念前進到跨公司與 OCP 標準化、但仍位於實體 memory sample 之前的 NAND 型 AI 記憶體候選層；能否進入正式 AI memory hierarchy，要依序通過介面公開、樣品、裝置整合、客戶 qualification 與量產
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 與 S2 證實標準化工作組，S3 補上 NAND／base die／KV cache 的技術位置，S4 明示樣品仍是未來目標
boundary: 不把標準化、公司模擬或樣品目標改寫成產品效能勝過 HBM、客戶採用、市占、收入或台灣供應商訂單
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C9
resolution: S7／S8 公告第一版 HBF 技術規格已發布，使規格時鐘越過「只有工作組」；原成熟度把規格與實體產品放在同一條線，改由 C9 的雙時鐘框架取代
-->

<!-- research_claim
claim_id: C5
label: unverified
status: superseded
claim: 截至 2026-08-02，HBF 最終公開介面規格已完成、首批 memory samples 已實際交付、整合裝置已送樣，或已有具名客戶完成 qualification
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源只有工作組、技術定位與未來時程，沒有規格版本、shipment 文件、客戶名稱、測試條件或 qualification 結果
boundary: 找不到完成證據不是反證；但在新文件出現前，圖譜成熟度不能越過 planned sample
verification_needed: OCP 公開規格或合規文件、Sandisk／SK hynix 樣品交付公告，以及客戶或裝置端可交叉核對的 qualification 結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C11
resolution: S7／S8 已證明第一版技術規格公告發布，原句把已驗證的規格節點與仍未驗證的樣品、裝置及客戶資格混在同一主張；改由 C7／C8 記錄規格、C11 續追產品節點
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: universe 內記憶體或封測公司已因 HBF 取得可辨識訂單、收入、毛利或資本支出貢獻
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: Sandisk、SK hynix 與 OCP 文件沒有具名台灣供應商，也沒有雙向核對的產品、客戶與財務資料
boundary: NAND、controller、bonding、TSV 或封測能力只形成搜尋路由，不構成公司受惠事實
verification_needed: HBF 平台端與台灣公司端同時揭露具名產品、qualification、出貨及可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Sandisk 與 SK hynix 於 2026-08-03 公告透過 OCP 發布第一版 HBF 技術規格；公告摘要涵蓋基本效能期望、xPU-HBF 主機介面、電氣連接、可靠度與封裝，以及軟體讀寫指引，並把 Google 與 Tenstorrent 列為參與技術驗證及標準工作的 consortium members
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-08-03
basis: S7 直接列出第一版 technical specification 的發布、規格範圍與新增成員角色
boundary: S7 是 Sandisk／SK hynix 聯合公告；本輪未獨立取得可逐條核對的 OCP 規範原文，Google／Tenstorrent membership 也不證明其產品採用、qualification、跨廠互通或部署
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: SK hynix 對第一版共同規格的摘要列出 8-high 與 16-high NAND die 配置、最高 512GB，以及約 0.4 至 3.0 TB/s 的三個頻寬等級，並描述以 UCIe 連接、可靠度與封裝規範及軟體 I/O 指引
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-04
basis: S8 直接列出 stack configuration、capacity、bandwidth grades、UCIe、reliability／packaging 與 software I/O
boundary: 這些是供應商公布的規格包絡，不是已交付樣品的量測結果；文件未提供延遲、寫入、耐久、功耗、熱條件、測試方法或與 HBM 的共同基準
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: HBF 的成熟度現在必須用兩個時鐘閱讀：共同介面與規則的「規格時鐘」已從工作組前進到第一版技術規格公告發布；可測硬體與客戶導入的「產品時鐘」仍停在公開可驗證的實體 memory sample 之前
supporting_source_ids: S2,S4,S7,S8
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C4；S2 確認 OCP 工作組、S7／S8 更新第一版規格公告與範圍，S4 的 memory／device sample 仍是未來目標；S9 的分層架構另由 C12 處理，不重複算入主命題來源鏈
boundary: 規格發布不能外推為規範全文已被本輪獨立核對、silicon 存在、產品符合規格、多廠互通、客戶資格、量產、收入或 HBM 替代
verification_needed:
correction_kind: supersedes
corrects_claim_id: C4
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: 本輪核對的 2026-08-03／08-04 規格公告與 Sandisk 2026-08-05 財報簡報，沒有揭露具名且已交付的 HBF memory sample、device sample、客戶 qualification、量產出貨或 HBF 獨立財務分子；財報簡報只在產品組合層級列出 advanced HBF
supporting_source_ids: S7,S8,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S7／S8 的公開內容停在共同規格與技術包絡，S10 的 HBF 字樣停在 portfolio overview，財務表只到公司與 end-market 層級
boundary: 這是對三份指定公開文件的揭露範圍判讀，不證明公司內部不存在 prototype、未公開測試或客戶接觸；也不能用公司營收反推 HBF 收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: unverified
status: active
claim: HBF 實體 memory sample 已具名交付並附規格與測試條件、整合 device sample 已運行目標工作負載、客戶 qualification 已完成，或已形成量產出貨與可辨識收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C5；S7／S8 已把第一版技術規格從原複合主張中移出，但 S7、S8、S10 仍沒有交付、裝置、客戶資格或財務分子的完成證據
boundary: 找不到公開完成證據不是反證；在新文件出現前，產品時鐘不能越過 planned memory sample
verification_needed: 供應商與接收方可交叉核對的 sample 文件、規格與測試條件；具名裝置工作負載；客戶 qualification；量產出貨及同產品財務分子
correction_kind: supersedes
corrects_claim_id: C5
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: SK hynix 的 FMS 2026 回顧把 HBM、DRAM、NAND 型 HBF 與 SSD 放在同一個 tiered memory architecture 中，並把減少資料搬移與硬體／軟體共同設計列為系統目標
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-07
basis: S9 的 Tiered Memory Architecture 段落直接列出四層位置與 data movement、hardware／software co-design
boundary: 這是供應商的系統架構敘事，不是已部署系統、共同 benchmark、資料放置策略成效、客戶採用或 HBF 優於其他層的證據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: unverified
status: active
claim: 本輪可直接取得帶版本與定位條款的 OCP HBF normative specification、公開 compliance 測試方法、具名產品 pass result，或跨廠互通矩陣
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S2 仍只提供 workstream 索引，S7／S8 是廠商對第一版規格的摘要；本輪未在 OCP 公開入口取得可逐條核對的版本化規範或合規結果
boundary: 未定位到公開文件不代表 OCP 貢獻者空間內沒有規格，也不否定廠商的發布公告；只限制本文不能自行補出規範版本、normative requirement、合規或互通結論
verification_needed: OCP 公開且可定位版本的 HBF 規範原文、規範條款對應表、合規測試計畫、具名 pass list 或多供應商互通結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: Sandisk 2025 年 7 月 HBF fact sheet 把 Gen 1 描述為 256Gb per die、16-die stack 512GB 與 1.6 TB／s read bandwidth；同一文件把「與無限容量 HBM 的系統效能差在 2.2% 內」限定為讀取 Llama 3.1 405B 之 8-bit pretrained weights、一次執行一個 kernel 的內部測試／模擬，並明示 HBM 容量在模型中假設無限、HBF latency 較高、page size 較大、actual user capacity less
supporting_source_ids: S11
contrary_source_ids:
as_of: 2025-07-29
basis: S11 PDF 第 2 頁直接列 Gen 1 容量與讀取頻寬，第 3 頁腳註逐一限定 2.2% 的模型、精度、kernel concurrency、HBM baseline、latency／page-size 差異與容量口徑；本地 SHA-256 及 3／3 頁渲染已核對
boundary: verified 只指 fact sheet 原文及腳註條件，不證明 512GB 是可用容量、1.6 TB／s 是具名樣品實測、2.2% 可重現、HBF 與 HBM 等速、所有模型都適用，或已完成 sample、qualification、部署與財務轉換
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 若只依 S11 的教材條件，把 405,000,000,000 個參數各記為 8 bits，並以文件定義的 decimal GB 計算，純權重 payload 是 405GB；相對 512GB 名目 stack 是 405／512＝79.1015625%，名目差額 107GB，但這不能證明整個模型或推論工作集實際放得下
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-14
basis: Python Fraction 與獨立 awk 路徑均由 parameters×bits／8 得 405,000,000,000 bytes，並得到 occupancy 405／512、79.1015625% 與 107GB nominal remainder
boundary: 這是 N=1 個假想 weights-only payload 的確定性單位展開，沒有裝置、模型檔、run 或抽樣，故沒有 sampling SE／t；未計 actual user capacity、量化 scale／metadata、KV cache、activation、runtime、workspace、冗餘、錯誤管理、分片、壓縮、page alignment 或其他系統記憶體
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: MLPerf Inference 現行規則把 system under test 定義為會影響效能的完整硬體與軟體，run 必須在指定 scenario 下完成 queries、相關 pre／post-processing、latency 與 quality 要求；LLM 又分開 TTFT 與 TPOT，且 Llama3.1-405B 有指定資料集、品質與 scenario-specific latency 契約
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-14
basis: S12 的 Definitions、Scenarios、Benchmarks、LoadGen Operation 與 LLM 註腳直接列 SUT、run、scenario、quality、latency、TTFT／TPOT 與 Llama3.1-405B 契約
boundary: 這只證明一套可重現推論結果要綁哪些系統與工作負載條件，不證明 Sandisk 內部模擬是 MLPerf submission、HBF 已存在，或 MLPerf 能隔離單一 memory tier 的因果效果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: inference
status: active
claim: HBF 的容量、頻寬與推論效益必須用三張成績單橋接：先保存 stack／die／名目與可用容量／讀寫／page／latency／耐久／功耗等裝置包絡，再保存模型權重／KV cache／activation／precision／placement／kernel／concurrency 等資料路徑，最後才以固定 scenario、資料、品質、TTFT／TPOT／throughput／tail／失敗／功耗／成本報告服務結果
supporting_source_ids: S8,S11,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S8 只給規格包絡，S11 同時揭露 nominal capacity、read bandwidth、internal simulation 與較高 latency／較大 page／usable-capacity 邊界，S12 則要求完整 SUT、scenario、quality 與 latency result；三者共同顯示裝置、資料路徑與服務結果不能互相替代
boundary: 三張成績單是研究中心整合供應商文件與 MLCommons 規則的檢查框架，不是 HBF 或 MLPerf 共同標準；欄位完整仍不證明產品存在、多廠互通、單一記憶體因果、production deployment、成本優勢或台灣公司收入
verification_needed: 同一具名 HBF sample 與 HBM／其他 baseline 公開裝置 raw、完整工作集 placement、相同模型／資料／品質／scenario 的 run-level TTFT／TPOT／throughput／tail／failures／power／cost，以及接收方 qualification
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C3,C4,C5
metric: HBF 規格版本、memory sample、device sample 與客戶 qualification
source_ids: S1,S2,S3,S4
watch_source_ids: S2,S5,S6
frequency: event_driven
frequency_detail: 週一三五自動研究循環檢查 OCP、Sandisk 與 SK hynix；出現規格、樣品或客戶文件即重審
next_check: 2026-08-17
trigger: OCP 發布可定位的 HBF 規格／合規資料，或 Sandisk、SK hynix、客戶公告實體樣品、測試條件與 qualification
invalidation: 2026 下半年沒有 sample evidence、工作組不再列示、時程延後，或實測顯示延遲、寫入、耐久與熱邊界無法支援目標工作負載
retired_at: 2026-08-12
retirement_reason: S7／S8 命中第一版技術規格發布 trigger，但沒有命中實體樣品、合規互通或客戶資格；規格與產品時鐘已拆開，由 T3／T4 接續
-->

<!-- monitoring_item
monitor_id: T2
status: retired
claim_ids: C2,C5,C6
metric: HBF 在 AI memory hierarchy 的實際工作負載與台灣供應鏈財務足跡
source_ids: S2,S3,S4
watch_source_ids: S5,S6
frequency: quarterly
frequency_detail: 每季檢查 HBF inference device、軟體調度、量產與供應商法說；只有雙向證據才升級公司線
next_check: 2026-10-15
trigger: 具名裝置公布 HBF／HBM／DRAM 分層、工作負載與測試結果，且供應商揭露產品、出貨、收入或毛利
invalidation: HBF 長期只停留在模擬與標準化，或實際系統仍以 HBM、DRAM、CXL memory、SSD／context storage 完成需求
retired_at: 2026-08-12
retirement_reason: C5 已拆成規格文件／合規缺口 C13 與產品節點 C11，原 T2 混合工作負載、產品及財務三種時鐘；由 T3／T4／T5 分層接續
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C7,C8,C9,C13
metric: HBF 直接規範原文、規範層級對應、合規計畫與跨廠互通
source_ids: S2,S7,S8
watch_source_ids: S2,S5,S6
frequency: event_driven
frequency_detail: 週一三五自動研究循環檢查 OCP、Sandisk 與 SK hynix；只在取得可定位版本原文、compliance artifact 或具名互通結果時升級
next_check: 2026-08-26
trigger: OCP 公開帶版本與條款定位的 HBF normative specification、xPU-HBF／UCIe 層級對應、合規測試方法、具名 pass list 或 multi-vendor interoperability result
invalidation: 第一版規格撤回、範圍重大改寫，或後續公開測試顯示介面、封裝可靠度與軟體 I/O 無法共同成立
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C3,C9,C10,C11
metric: HBF memory sample、device sample、測試包絡與客戶 qualification
source_ids: S4,S7,S8,S10
watch_source_ids: S5,S6
frequency: weekly
frequency_detail: 每週重查 Sandisk／SK hynix 的 sample、FMS 後續附件與客戶端公告；供應商目標日期本身不算交付
next_check: 2026-08-26
trigger: 具名 HBF memory sample 實際交付，且提供堆疊、容量、頻寬、延遲、寫入、耐久、功耗、熱或接收方測試中的可定位資訊；或裝置端確認工作負載及 qualification
invalidation: 2026 下半年沒有可核對的 memory sample、時程明確延後、接收方未確認，或測試結果無法支持目標工作負載
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C2,C6,C11,C12
metric: HBF 在具名 AI 系統的資料分層、軟體調度、部署與供應鏈財務足跡
source_ids: S3,S9,S10
watch_source_ids: S5,S6
frequency: quarterly
frequency_detail: 每季檢查具名 inference device、資料放置、部署分母與供應商法說；只有平台與公司兩端同產品、同期間證據才升級公司線
next_check: 2026-10-15
trigger: 具名裝置公布 HBF／HBM／DRAM／SSD 分層與工作負載結果，或平台端及台灣公司端同時揭露 qualification、出貨、收入或毛利
invalidation: HBF 長期只停留在規格與 roadmap，未出現可測硬體、軟體支援與部署；或財務揭露無法隔離 HBF 分子
-->

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave92_hbf_system_conditions_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: split_specification_and_product_clocks_after_first_hbf_technical_specification
evidence: sources:S7,S8,S9,S10
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_hbf_nominal_usable_working_set_and_simulation_to_service_evidence_bridge_without_thesis_or_clock_refresh
evidence: sources:S8,S11,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **新記憶體層**：在既有高速工作記憶體與長期儲存之間增加一個資料位置；只有容量還不夠，系統還要知道哪些資料適合放進去。
- **高頻寬快閃記憶體（HBF）**：嘗試把大量快閃記憶體平行化，再配上底部邏輯晶片，提高容量與讀取能力；第一版共同技術規格已公告發布，但本輪仍沒有可核對的實體樣品交付。
- **高頻寬記憶體（HBM）**：把多層動態記憶體疊在一起並放在運算晶片附近；速度高，但容量、成本與封裝空間都有取捨。
- **快閃記憶體（NAND）**：固態硬碟常用、斷電後仍可保留資料的記憶體；密度高，但讀寫等待、更新與耐久特性不同於工作記憶體。
- **動態隨機存取記憶體（DRAM）**：需要持續供電、適合快速讀寫的工作記憶體；它與快閃記憶體的速度、成本與資料保留方式不同。
- **固態硬碟（SSD）**：以快閃記憶體保存大量資料的儲存裝置；容量大不代表能直接承擔工作記憶體的即時讀寫任務。
- **鍵值快取（KV cache）**：大型模型推論時保存先前上下文計算結果的資料；容量不足會增加搬移或重算，但實際讀寫模式仍依工作負載而異。
- **容量**：裝置能保存多少資料；容量變大不代表讀取、寫入、耐久、功耗與成本會同時達標。
- **名目容量**：依晶粒數與每顆宣告容量加總的理論 bytes；尚未扣除保留空間、錯誤管理、對齊與其他系統用途。
- **可用容量**：軟體真正能配置給資料的容量；通常小於名目容量，必須由具名產品與介面實際揭露。
- **模型權重**：模型訓練後保存的參數數值；即使權重本身放得下，推論仍可能需要額外快取、暫存與執行空間。
- **工作集**：某段運算期間真正需要同時駐留或快速取用的全部資料；可能包含權重、鍵值快取、啟用值、程式與暫存區。
- **數值精度**：每個參數或運算值使用多少 bits 及何種表示法；寫 8-bit 不等於整個模型檔案剛好每參數只占 1 byte。
- **頻寬**：一段時間內可搬移多少資料；總量高不代表每次取用的等待時間都短。
- **延遲**：從提出讀寫要求到取得結果所需的等待時間；平均值不能取代最慢情況與不同存取模式。
- **頁面大小（page size）**：記憶體一次讀寫或管理的資料粒度；頁面較大時，小而分散的要求可能搬移額外資料。
- **首詞元延遲（TTFT）**：使用者送出要求後，到收到第一個輸出詞元的時間；它不等於後續每個詞元的生成速度。
- **每輸出詞元時間（TPOT）**：第一個詞元之後，相鄰輸出詞元的平均時間間隔；它和同時服務多少請求仍是不同問題。
- **推論情境（scenario）**：請求如何抵達、併行與計時的共同規則，例如單一請求、互動式服務或離線批次；不同情境不能直接排同一名次。
- **受測系統（SUT）**：實際被計時的完整硬體與軟體範圍；只換記憶體以外的軟體、加速器或互連，也可能改變結果。
- **品質門檻**：輸出正確性或任務品質至少要達到的標準；更快但品質不相等的結果不能算同一比較。
- **內部模擬**：公司在自建模型與假設下推演的結果；必須保存模型、工作負載、baseline 與限制，不能冒充實體樣品或第三方 benchmark。
- **隨機讀取**：從分散位置取資料；它與連續搬移大區塊資料的難度不同，不能只用順序讀取數字代替。
- **順序讀取**：連續讀出相鄰資料；表現好不代表頻繁跳點、寫入或更新同樣適合。
- **寫入與更新**：新增資料或改寫既有內容；工作負載若頻繁更新，只有讀取速度不足以證明可用。
- **耐久**：記憶體可承受多少次寫入、溫度與使用時間；單次展示不能證明長期服務壽命。
- **功耗**：裝置運作所需電力；每次搬移資料的耗能與整體系統功率都會影響是否可部署。
- **熱管理**：把晶片與封裝產生的熱帶走；堆疊密度提高後，熱點可能限制速度、壽命與穩定度。
- **底部邏輯晶片（logic base die）**：位在記憶體堆疊底部、處理資料傳輸與控制功能的邏輯晶片；有此設計方向不等於產品已完成。
- **控制器**：安排資料讀寫、錯誤處理與裝置溝通的元件或邏輯；能控制一般固態硬碟不代表已支援 HBF。
- **堆疊**：把多層晶粒垂直整合，以增加容量或縮短連線；層數增加也會提高接合、測試與散熱難度。
- **記憶體分層**：依資料的速度、容量、持久性與成本需求，安排不同記憶體或儲存位置；不是越靠近運算晶片就一定越好。
- **軟體調度**：由系統軟體決定哪些資料何時搬移、放在哪一層；硬體存在不代表應用會自動使用。
- **標準化**：多方討論共同名稱、介面與測試規則；開始標準化不等於規格完成或產品互通。
- **工作組（workstream）**：由參與者共同推進特定議題的組織；工作組成立只證明有人開始協作。
- **公開規格（specification）**：可定位版本與內容的共同技術文件；廠商已公告第一版 HBF 規格發布，但本文仍把公告摘要與可逐條核對的規範原文分開。
- **規格時鐘**：追蹤工作組、共同文件、規範條款、合規方法與互通結果；它回答「大家是否用同一套規則」。
- **產品時鐘**：追蹤實體樣品、裝置整合、客戶資格、量產與收入；它回答「規則是否已變成可交付產品」。
- **頻寬等級**：規格把可提供的資料搬移量分成數個級別；公布等級包絡不等於某顆樣品已在指定條件下量到同樣結果。
- **UCIe 介面**：用來連接封裝內不同晶粒的共同互連方法；文件寫出介面名稱，仍要再確認版本、層級、封裝與合規結果。
- **xPU-HBF 主機介面**：運算處理器與 HBF 系統交換資料、指令及狀態的主機端規則；名稱存在不等於任一處理器已完成整合。
- **硬軟共同設計**：硬體資料路徑與軟體放置規則一起設計；只有硬體容量或頻寬，不能證明工作負載會自動受益。
- **未來記憶體與儲存大會（FMS）**：Future of Memory and Storage 的縮寫，是記憶體與儲存技術活動；廠商在活動發表願景或規格摘要，仍不等於產品已完成。
- **Gen（世代）**：Generation 的縮寫，用來區分產品或技術路線的第幾代；Gen 1 的目標不能自動外推到 Gen 2／3，也不代表已量產。
- **大型語言模型（LLM）**：以大量文字資料訓練、能處理或產生語言的模型；參數量相同也可能因架構、精度與工作負載而有不同記憶體需求。
- **推論（inference）**：使用已訓練模型處理新輸入並產生結果；它和訓練的資料流、寫入模式與品質目標不同。
- **Llama3.1-405B（Llama 3.1 405B）**：Sandisk 模擬與現行 MLPerf 規則都提到的 4050 億參數語言模型；同名模型仍須固定 precision、資料、quality 與 scenario 才能比較。
- **MLPerf Inference**：MLCommons 維護的推論 benchmark 規則與套件；它要求完整受測系統、情境、品質與延遲口徑，但不是 HBF 規格或 HBF 已通過的測試。
- **介面**：裝置與系統交換資料、指令與狀態的規則；介面名稱存在不等於多家產品已互通。
- **合規計畫（compliance）**：用一致方法檢查產品是否符合規格；規劃測試不等於已有通過結果。
- **記憶體樣品（memory sample）**：可被量測的實體記憶體產品；公布目標日期不等於樣品已交付。
- **裝置樣品（device sample）**：把記憶體整合進可運作裝置或系統的樣品；單一展示板不等於客戶產品完成。
- **客戶資格認證（qualification）**：客戶依指定產品、工作負載與條件判定能否採用；開始測試不等於已通過。
- **製造良率**：投入製造後能成為合格產品的比例；少量成功樣品不能證明大量製造可穩定維持。
- **量產**：產品進入持續製造與交付；只有樣品、可量產聲明或設備就位仍不是實際量產。
- **重複訂單與收入**：客戶持續採購，且財務金額能對應同一產品與期間；公司總營收不能直接證明 HBF 貢獻。

### 三句話抓重點

- 新的記憶體層不能只提供更大容量；它還要在目標工作負載下證明讀取速度、寫入與更新、耐久、功耗和熱管理都能成立。
- 兩家記憶體公司已公告第一版共同技術框架，涵蓋容量、傳輸級別、主機連接、封裝可靠度與軟體讀寫，規格工作已比只有工作組時更前進一步。
- 但規則前進不等於產品同步前進；本輪仍不能說實體樣品已交付、裝置已整合、客戶已通過或產品已量產。

### 為什麼重要

人工智慧系統裡，有些資料正在被運算，有些要快速重複取用，有些則適合長期保存。新增一層記憶體
只有在容量、等待時間、讀寫模式、耐久、功耗與成本共同成立，而且系統軟體知道何時搬移資料時，
才可能真正分擔既有記憶體與儲存裝置的工作。

因此第一版共同規則值得升級，但它只回答「預計如何連接與描述產品」，還沒有回答「哪一顆樣品
在什麼條件下做到了」。把規格時鐘、產品時鐘、系統條件、角色交接與商用關卡分開，才能避免
把新名詞或規格包絡直接寫成量產市場與台灣供應商訂單。

### 接下來怎麼追

- 先找開放運算計畫可直接定位的規格版本與條款，確認主機介面、晶粒互連、封裝可靠度及軟體讀寫各在哪一層，再追合規與互通方法。
- 再找 2026 年下半年實體記憶體樣品的交付日、規格、測試條件與接收方。
- 2027 年初若出現裝置樣品，要確認它真的完成裝置整合、軟體調度與目標工作負載測試，而非單一展示板。
- 公司層級必須同時看到平台端具名、客戶資格認證、穩定製造、出貨、重複訂單與可辨識財務資料。

### 想一想

- 如果一種裝置容量很大、連續讀取很快，卻無法承受應用所需的頻繁寫入與更新，它應被當成新的工作記憶體層，還是特殊儲存裝置？
- 公司宣布加入工作組、公開規格完成、中立測試通過與多家產品互通，分別代表哪些不同證據？
- 即使裝置樣品能運作，還要看到哪些客戶與製造證據，才能稱為量產市場？

## 先判斷它能不能成為新的記憶體層

以下五項只是本文整理本輪公開資料的閱讀問題，不是完整產品規格，也不是對任何記憶體技術的
效能排名。只有把目標工作負載與共同測試條件說清楚，才能判斷新裝置究竟是工作記憶體、快取，
還是特殊儲存設備。

| 本文五項系統條件 | 讀者先問 | 沒通過會怎樣 | 主要接力角色 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 容量與資料保留 | 能否保存目標資料量，斷電後是否要保留 | 容量不足會頻繁搬移；保留方式不符則放錯資料層 | 快閃記憶體、堆疊與控制器 | 規格摘要列出 8 層／16 層與最高 512GB 包絡；尚非實體產品量測 |
| 2. 讀取與等待時間 | 連續與分散讀取能否在工作負載要求內完成 | 總頻寬看似很高，單次取用仍可能等太久 | 底部邏輯晶片、控制器與介面 | 規格摘要列約 0.4 至 3.0 TB/s 三級；沒有延遲、存取型態、測試條件或第三方結果 |
| 3. 寫入、更新與耐久 | 能否承受應用需要的改寫頻率與服務壽命 | 只能大量讀取時，可能仍較像特殊儲存裝置 | 記憶體元件、控制器與韌體 | 規格公告涵蓋軟體讀寫與可靠度指引；尚無寫入、更新與耐久測試結果 |
| 4. 功耗、熱與封裝 | 堆疊與底部邏輯晶片能否在系統功率與溫度範圍內穩定運作 | 熱點、功耗或接合問題可能限制速度、壽命與良率 | 封裝、測試、供電與散熱角色 | 規格公告涵蓋封裝與可靠度；尚無實體樣品的功耗、熱、接合或良率結果 |
| 5. 系統整合與軟體調度 | 裝置、控制器與軟體是否知道哪些資料何時搬移 | 硬體即使可用，也可能沒有應用願意或能夠使用 | 裝置商、系統軟體、應用與客戶 | 公告列 UCIe、主機介面與軟體讀寫；2027 年初裝置樣品仍是目標，尚無具名系統運行結果 |

## 第一版技術規格先對齊哪四份合約

下表是依 Sandisk／SK hynix 的聯合公告與 SK hynix 技術摘要整理的閱讀地圖，不是本文自行補寫
的規範條款。本輪沒有從 OCP 公開入口取得可逐條定位的版本化規範原文，所以只能確認「公告說
規格涵蓋什麼」，不能宣稱每一條 normative requirement、版本號或合規方法已被獨立核對。

| 四份共同合約 | 公告摘要對齊什麼 | 初學者要避免的誤讀 | 下一份可升級證據 |
|---|---|---|---|
| 1. 產品包絡 | 8 層／16 層、最高 512GB、約 0.4 至 3.0 TB/s 三個頻寬等級 | 規格上限等於已交付產品實測，或總頻寬等於低延遲 | 可定位規範條款、樣品型號、測試方法與完整操作條件 |
| 2. 主機與電氣介面 | xPU-HBF 主機介面、電氣連接與 UCIe 路徑 | 寫出介面名稱等於任一運算晶片已接通，或多廠產品已互通 | 版本與層級對應、compliance checklist、具名 silicon 與跨廠結果 |
| 3. 堆疊、封裝與可靠度 | 堆疊配置、可靠度與封裝設計指引 | 設計指引等於接合、熱、良率及長期壽命已通過 | 樣品結構、熱／機械條件、可靠度方法、結果與接收方 |
| 4. 軟體讀寫 | 軟體 read／write user guide 與硬軟共同設計方向 | 有讀寫指引等於驅動、資料放置與目標工作負載已完成 | 公開軟體介面、資料放置策略、具名裝置與端到端工作負載 |

## 512GB、1.6TB/s 與「只差 2.2%」是三種不同證據

Sandisk 的 HBF fact sheet 把三個很容易被接成一句話的數字放在一起：Gen 1 的 `512GB`
名目 stack、`1.6 TB/s` read bandwidth，以及內部模擬中「相對無限容量 HBM 的系統效能差在
2.2% 內」。它們分別是容量包絡、資料搬移率與特定模型下的系統推演，不能互相代替。[S11]

| 看到的數字 | 證據層 | 分子與分母至少還要綁定 | 目前不能說 |
|---|---|---|---|
| `512GB per 16-die stack` | 廠商描述的 Gen 1 名目容量 | 每 die 容量、die 數、GB 定義、保留空間與 software-visible capacity | 實體 sample 已有 512GB 可用空間，或整個模型一定放得下 |
| `1.6 TB/s read bandwidth` | 廠商描述的 Gen 1 讀取頻寬 | 連續／隨機、page、request size、concurrency、方向、時間窗、latency、功耗與溫度 | 寫入同速、每次存取很快、所有容量都能持續滿速，或量到的是 production workload |
| `within 2.2% of unlimited-capacity HBM` | 供應商內部測試／模擬敘事 | baseline 指標、模型、precision、kernel、batch／concurrency、資料放置、quality、run 與分布 | HBF 與 HBM 等速、2.2% 可重現、容量優勢已納入，或任何具名 sample 已完成 benchmark |
| TTFT／TPOT／throughput／quality | 完整推論服務結果 | 同一受測系統、scenario、模型／資料、品質、請求分布、失敗、功耗、成本與重複 run | 單一記憶體就是因果，或結果自動變成採用、訂單與公司財務 |

關鍵不在主標題，而在 fact sheet 第 3 頁腳註：比較只模擬讀取 `Llama 3.1 405B` 的
`8-bit pretrained weights`，一次在 xPU performance model 上執行一個 kernel；HBM 容量為建模
目的被假設成無限，所以比較刻意沒有計入 HBF 的容量優勢。文件還直接承認 HBF 相對 HBM 有
較高 latency 與較大 page size，並註明實際 user capacity 會小於名目容量。[S11] 因此 2.2%
不是錯誤數字，但只能在這個被明示的模擬盒子裡閱讀。

### 405B×8-bit 只得到純權重 payload，不是整個工作集

沿用文件自己的 decimal 單位，並把 model name 裡的 `405B` 條件式解讀成
`405,000,000,000 parameters`，可以做一次量綱核對；這不是把模擬補成實測，也不是主張實際
模型檔恰有這個精確參數數或 byte 數：

| 步驟 | 確定性計算 | 結果 | 仍未計入 |
|---|---|---:|---|
| 1. 純權重 payload | `405,000,000,000 parameters × 8 bits ÷ 8` | `405GB` | 量化 scale／metadata、對齊、壓縮與模型檔格式 |
| 2. 占 512GB 名目 stack 比例 | `405 ÷ 512` | `79.1015625%` | actual user capacity 與保留空間 |
| 3. 名目差額 | `512 − 405` | `107GB` | KV cache、activation、runtime、workspace、冗餘與錯誤管理 |
| 4. 整個服務能否放下 | 需要具名軟硬體的 software-visible memory map | 未量測 | 分片、其他 memory tier、並行請求、page alignment 與失敗恢復 |

Python Fraction 與獨立 awk 路徑都得到 `405GB`、`405／512`、`79.1015625%` 與 `107GB`。
這是 **N=1 個假想 weights-only payload** 的確定性單位展開，沒有裝置、模型檔、run 或抽樣，
所以沒有 sampling SE／t。即使名目差額是正的，也不能寫成「Llama 3.1 405B 完整工作集已放進
一顆 HBF」；fact sheet 自己已提醒 actual user capacity less。

### 同一顆記憶體要過三張成績單

| 成績單 | 最少保存什麼 | 這一層回答 | 少了會怎麼誤讀 |
|---|---|---|---|
| 1. 裝置與規格 | sample ID、die／stack、名目／可用容量、read／write、page、latency distribution、endurance／retention、error、power、temperature 與測試方法 | 這顆實體記憶體在什麼操作包絡下能做什麼 | 規格上限或 roadmap 被當成產品實測 |
| 2. 模型與資料路徑 | weights／KV cache／activation／workspace bytes、precision、placement、sharding、搬移量、kernel、batch、concurrency、軟體與 baseline | 哪些資料真的放在哪一層，瓶頸是否落在 HBF | 純權重或單一 kernel 被當成完整推論服務 |
| 3. 服務與商業結果 | scenario、資料、quality、TTFT、TPOT、throughput、tail、失敗、run-level distribution、功耗、成本、部署量、價格、收入與毛利 | 使用者是否得到相同品質的可持續改善，以及是否形成可辨識財務 | 內部模擬直接變成客戶採用、TAM 或台灣公司訂單 |

MLPerf Inference 的方法邊界能說明第三張表為何不能省：現行規則把受測系統定義成會影響效能的
完整硬體與軟體，run 要在指定 scenario 下完成 queries、相關前後處理、latency 與 quality；LLM
另分 TTFT 與 TPOT，Llama3.1-405B 也有自己的資料集、品質與 scenario-specific latency 契約。
[S12] 這不表示 HBF 要或已通過 MLPerf，而是提供一個獨立檢查：單一 memory bandwidth 與一次
內部 kernel 模擬，還不是可比較的推論服務結果。

### 多空小作文必須共用同一個推論情境

| 敘事 | 合理假說 | 必須再看到的共同證據 | 什麼會讓敘事失效 |
|---|---|---|---|
| 偏多：更大近端非揮發容量減少資料搬移 | 更多權重或快取留在加速器附近，可能降低跨層搬移、提高可服務模型大小，並增加 NAND、logic base die、堆疊、測試與封裝內容 | 同一模型／precision／quality／scenario 的三張成績單，含 software-visible capacity、placement、bytes moved、TTFT／TPOT／throughput／tail、功耗、成本、qualification、部署與財務分母 | 只有名目 GB、read TB/s、內部模擬或 consortium 名單，沒有實體 sample、完整工作集與接收方結果 |
| 偏空：較高延遲、較大 page 與寫入邊界抵銷容量 | 小而分散的讀取、KV 更新、尾端等待、耐久或軟體搬移可能讓部分工作仍需 HBM／DRAM，降低 HBF 可承擔的有效比例 | 固定資料放置與並行請求，公開 read／write mix、request／page、latency distribution、stall、endurance、retention、功耗、失敗與服務品質 | 只拿 HBM 名目容量不足或 NAND 一般特性推論，沒有具名 HBF 裝置與相同 workload 比較 |
| 共同底線 | 大容量、讀取頻寬與端到端推論效益是三個不同分母 | 固定 sample、可用容量、完整工作集、baseline、scenario、quality、run 分布與成本，再由供應商和接收方雙向核對 | 把 `512GB`、`1.6 TB/s` 與 `2.2%` 串成已量產、已採用或已形成台灣公司收入的單一路徑 |

本輪新增 N=2 份一手方法文件：Sandisk fact sheet 是供應商產品／模擬鏈，MLCommons rules 是
獨立 benchmark-contract 鏈，不是兩顆 HBF、兩個 sample、兩個客戶或兩次 run。PDF 共 3 頁，
本地 SHA-256 為 `349f05372fb528702d2fe95ec8f3a9cb9b4dd976c7d115a3db49f26031b10111`，
3／3 頁已逐頁渲染核對；PDF／PNG 只留在 `tmp/`，不進版控。除了 N=1 教材換算，沒有新的
effect size、sampling SE／t、價格、估值、共識、部位或投資判斷。

## 用兩個時鐘避免把規格當產品

規格與產品會互相影響，卻不一定同步。把它們拆成兩個時鐘，讀者就能理解「這次真的有進展」
與「仍不能稱為商用產品」為何可以同時成立。

| 證據時鐘 | 依序要經過 | 截至本輪的位置 | 還不能說 |
|---|---|---|---|
| 規格時鐘 | 工作組 → 第一版共同文件 → 可定位規範條款 → 合規方法 → 具名通過 → 跨廠互通 | 廠商公告第一版技術規格發布，並摘要四份合約；OCP 仍列工作組 | 本輪已逐條核對規範原文、產品已合規或多廠已互通 |
| 產品時鐘 | 架構 → 實體記憶體樣品 → 裝置樣品 → 客戶資格 → 穩定量產 → 可辨識收入 | 架構與未來樣品時程已公開；本輪未見具名交付的實體樣品 | 裝置已完成、客戶已採用、量產出貨或供應鏈已有財務貢獻 |

## 再把商用化拆成六關

後一關需要新的證據，不能因為公司合作、目標日期接近或產品名稱含有「高頻寬」，就把後面的
樣品、客戶結果與量產一起補滿。這是本文的閱讀順序，不是產業共同標準或公司快慢排名。

| 本文六關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 技術位置與工作負載說清楚 | 想處理哪類資料，為何不能由既有記憶體或儲存裝置完成 | SK hynix 描述快閃記憶體、底部邏輯晶片與鍵值快取位置 | 共同工作負載、延遲、寫入、耐久、熱與功耗結果 | 效能已勝過高頻寬記憶體，或所有推論工作負載都適用 |
| 2. 共同規則公開 | 多家產品要如何交換資料、測試與互通 | 兩家公司已公告第一版技術規格發布，摘要主機／電氣介面、產品包絡、封裝可靠度與軟體讀寫 | OCP 可定位的版本化規範原文、條款對應、合規方法與跨廠結果 | 公告摘要已等同全文核對、多家產品已互通或已有合規結果 |
| 3. 交出可測記憶體樣品 | 實體記憶體是否按規格做出並交給接收方測試 | Sandisk 以 2026 年下半年為首批樣品目標 | 實際交付日、規格、測試條件與接收方 | 樣品已交付、測試已通過或已有客戶訂單 |
| 4. 完成裝置整合 | 記憶體是否被放入具名裝置，並由軟體安排目標工作負載 | Sandisk 以 2027 年初為首批裝置樣品目標 | 具名裝置、軟體調度、工作負載與運行結果 | 裝置樣品已完成、可大規模部署或已被客戶採用 |
| 5. 通過客戶資格認證 | 客戶是否依指定產品與條件完成驗證 | 本輪沒有完成證據 | 客戶名稱、測試條件、通過結果與採購節點 | 開始測試就等於通過，或單一客戶可代表整個市場 |
| 6. 穩定量產與形成收入 | 能否維持良率、出貨與重複採購，並在財務上辨認同一產品 | 本輪沒有完成證據 | 穩定良率、量產出貨、重複訂單及可辨識收入 | 台灣供應商已受惠、已有毛利貢獻或整個族群同步成長 |

## 再把五組角色接力放回正確位置

HBF 若真的成為新記憶體層，不會只由一顆記憶體晶片完成。下表只說明各角色要交付什麼，以及
本輪證據停在哪裡；「形成搜尋路由」不等於已具名供應商、訂單或收入。

| 接力角色 | 要交付什麼 | 要和下一角色說清楚 | 本輪證據 | 不能外推 |
|---|---|---|---|---|
| 快閃記憶體與堆疊 | 提供容量、資料保留與可製造的記憶體結構 | 晶粒、堆疊、讀寫、耐久與測試規格 | 共同規格摘要列出 8／16 層與容量包絡；尚無具名實體樣品、晶粒細節或量測 | 一般固態硬碟用快閃記憶體可直接替代，或所有記憶體廠都能生產 HBF |
| 底部邏輯晶片與控制器 | 安排平行資料傳輸、命令與錯誤處理 | 介面、控制協定、製程、功耗與熱邊界 | 技術方向有底部邏輯晶片，規格摘要列主機／電氣介面與 UCIe；沒有具名 silicon 或實測 | 已完成設計、已選定晶圓代工或控制器供應商 |
| 封裝、測試與熱管理 | 把堆疊與邏輯晶片整合成可測、可散熱的產品 | 接合、互連、測試覆蓋、良率與散熱條件 | 規格公告涵蓋可靠度與封裝指引；沒有具名產品、測試結果或供應商 | 服務高頻寬記憶體的公司必然取得 HBF 訂單 |
| 裝置、系統與軟體 | 把記憶體放進具名裝置，安排資料搬移與工作負載 | 裝置介面、驅動、軟體調度與端到端結果 | 規格公告涵蓋軟體讀寫；裝置樣品仍是未來目標，沒有具名運行結果 | 加入規格 consortium 或單一展示板等於可部署產品 |
| 客戶、製造與財務 | 完成資格認證、穩定製造、持續採購與財務揭露 | 通過條件、良率、出貨、重複訂單與同期間收入 | Google／Tenstorrent 只由聯合公告列為 consortium members；沒有產品通過、量產、訂單或 HBF 財務分子 | 參與技術驗證、規格發布或公司總營收等於 HBF 商業化成功 |

## 來源與證據邊界

- [Sandisk／SK hynix HBF 標準化公告](https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf)（合作與 OCP workstream）。
- [OCP Semi-Private Workstreams](https://www.opencompute.org/community/semi-private-workstreams)（HBF 工作組的獨立索引）。
- [SK hynix TSMC Symposium 2026](https://news.skhynix.com/en/tsmc-technology-symposium-2026/)（NAND、KV cache 與 logic base die 技術位置）。
- [Sandisk Memory-Centric AI](https://www.sandisk.com/company/newsroom/blogs/2025/memory-centric-ai)（樣品目標與公司模擬邊界）。
- [Sandisk／SK hynix 第一版 HBF 技術規格公告](https://investor.sandisk.com/news-releases/news-release-details/sandisk-and-sk-hynix-advance-global-standardization-high)（規格發布、主機／電氣介面、封裝可靠度、軟體讀寫與 consortium members）。
- [SK hynix FMS 2026 HBF 規格摘要](https://news.skhynix.com/en/hbf-at-fms-2026/)（8／16 層、最高 512GB、三個頻寬等級、UCIe 與軟體 I/O）。
- [SK hynix FMS 2026 回顧](https://news.skhynix.com/en/fms-2026/)（分層記憶體與硬軟共同設計敘事）。
- [Sandisk Q4 FY26 Earnings Presentation](https://investor.sandisk.com/static-files/c75d1bee-c5c9-4e5a-8605-302c1aeac59b)（HBF 只在產品組合層級出現，沒有 HBF 獨立財務分子）。
- [Sandisk HBF Fact Sheet](https://documents.sandisk.com/content/dam/asset-library/en_us/assets/public/sandisk/collateral/company/Sandisk-HBF-Fact-Sheet.pdf)（Gen 1 名目容量／讀取頻寬，以及 2.2% 內部模擬的模型、精度、kernel、baseline、latency、page size 與可用容量腳註邊界）。
- [MLPerf Inference Rules](https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc)（完整受測系統、scenario、quality、TTFT／TPOT 與 Llama3.1-405B 的推論結果契約）。

8 月 3 日與 8 月 4 日兩篇是同一 Sandisk／SK hynix 共同規格消息鏈，不能當成兩份獨立採用證據；
Google 與 Tenstorrent 也只由這條聯合消息鏈列為 consortium members。本篇只把 512GB 與約 0.4
至 3.0 TB/s 寫成公告的規格包絡，只使用 Sandisk 模擬已明示的條件與腳註來教讀者辨認證據層，
不採用它宣稱 HBF 與 HBM 效能相等，也不拿沒有共同測試條件的容量、頻寬、成本或良率做跨產品
勝負與公司估值。

## 影響路由

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-26
rationale: 第一版共同規格讓 NAND、controller、logic base die、主機介面與軟體讀寫搜尋路由更具體；但本輪沒有 universe 公司被平台端具名，也沒有樣品、資格與財務雙向核對
evidence_boundary: 外部共同規格或一般記憶體／控制器能力，不等於 universe 公司已有 HBF sample、qualification、訂單或收入
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-26
rationale: HBF 規格摘要已涵蓋 8／16 層堆疊、UCIe、封裝與可靠度指引，形成 bonding、TSV、測試與熱管理搜尋入口；但沒有具名封裝產品、樣品結果或 universe 供應商
evidence_boundary: 規格指引、先進封裝能力或服務 HBM 客戶，不等於取得 HBF 客戶 qualification、量產或財務貢獻
-->

## 下一個可證明／否定的節點

- OCP 公開可直接定位的 HBF 規範版本與條款，並說清楚 xPU-HBF、UCIe、封裝可靠度及軟體 I/O 的層級與 compliance 路線。
- Sandisk 或 SK hynix 公告實際 memory sample，並提供可核對的規格、測試條件與接收方。
- 客戶或裝置端獨立確認 HBF device sample、工作負載、軟體調度與 qualification 結果。
- 若 2026 下半年沒有樣品證據、時程延後或規格沒有合規／互通路線，C9 的雙時鐘成熟度與信心必須下修。
- 台灣公司只有在平台端與公司端完成具名產品、資格、出貨與財務雙向核對後，才能從搜尋路由升級為公司曝險線。
