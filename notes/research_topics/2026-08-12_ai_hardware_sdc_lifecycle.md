# AI 硬體沒有報錯，答案仍可能算錯：從出廠測試到機群隔離的 SDC 責任鏈

<!-- research_topic
topic_id: MI-2026-08-12-AI-HARDWARE-SDC-LIFECYCLE
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-12
source_published_at: 2025-12-16
last_reviewed_at: 2026-08-12
review_due: 2026-08-31
source_type: mixed
publisher: Open Compute Project Foundation
publisher_domain: opencompute.org
canonical_url: https://www.opencompute.org/documents/sdc-in-ai-ocp-whitepaper-ver-1-1-final-pdf
source_chain_id: ai-hardware-sdc-lifecycle-primary-scan-20260812
stock_ids:
group_ids: packtest,semiequip,serverodm
trigger_type: silent_data_corruption_lifecycle_test_contract
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C7
base_confidence: medium
confidence_basis: OCP SDC 白皮書與 Server Component Resilience v1.0 已對齊錯誤分類、測試輸入輸出、part history、coverage、repeatability、time-to-fail 與 quarantine pool；Meta、NVIDIA DCGM、Google Research 及 Google Cloud 又分別提供機群偵測、主動診斷、應用層防護與主機隔離案例。公開證據仍缺跨框架一致交換格式、誤報漏報、共通隔離與 RMA 門檻，以及本 universe 的具名資格與財務曝險
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-12
from: initial
to: inbox
reason: captured_cross_lifecycle_sdc_detection_and_isolation_sources
evidence: source_chain:ai-hardware-sdc-lifecycle-primary-scan-20260812
-->
<!-- transition
date: 2026-08-12
from: inbox
to: triaged
reason: aligned_taxonomy_and_test_handoffs_while_preserving_threshold_and_commercial_boundaries
evidence: sources:S1,S2,S3,S4,S5,S6,S7,S8,S9
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_zero_event_exposure_confidence_and_isolation_evidence_passport_without_thesis_clock_refresh
evidence: sources:S1,S2,S11,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **無聲資料損壞（Silent Data Corruption，SDC）**：硬體已把資料或運算結果算錯，內建偵錯機制卻沒有發出警報，程式因此把錯誤答案當成正確答案繼續使用。
- **良性錯誤（benign fault）**：硬體內部發生擾動，但最後輸出沒有被改變；有故障不一定就有可見錯誤。
- **已修正錯誤（corrected error）**：系統發現錯誤並在影響輸出前修好，例如記憶體的錯誤修正碼修回一個位元。
- **偵測到但無法修正的錯誤（DUE）**：系統知道答案可能不可靠，卻無法自行修好，通常會停止、重試或重新啟動；它和「完全沒有警報」的 SDC 不同。
- **靜態錯誤**：設備無法開機、無法被系統辨識等容易重現的明顯故障。
- **暫態錯誤**：只在特定負載、溫度、電壓或時間出現的故障；重跑時可能消失。
- **測試逃逸（test escape）**：有缺陷的零件通過原本的製造測試，到了整機或實際使用階段才被另一種工作負載觸發。
- **結構測試**：用特定故障模型與測試向量檢查晶片內部電路，例如卡住或延遲類型的缺陷。
- **功能測試**：讓晶片執行實際或類似實際的程式，檢查輸出是否符合預期；較接近使用情境，但不可能窮舉所有資料與狀態。
- **燒機（burn-in）**：在較長時間、較高負載或指定溫度與電壓下運作設備，提早暴露不穩定或早期失效。
- **系統層測試（SLT）**：晶片已放進板卡或伺服器後，以完整系統環境執行測試，確認問題是否只在電源、散熱、韌體或整機交互作用下出現。
- **機內診斷（in-system diagnostics）**：設備裝在實際主機內時執行的主動測試；它可以檢查特定資料路徑，但不等於能證明所有工作負載都不會出錯。
- **已知答案測試**：先算好正確結果，再讓待測設備運算同一題並比較；若結果不同，才能建立可重現的錯誤證據。
- **測試覆蓋（coverage）**：一項測試能抓到多少已知缺陷；它不是「未來所有未知缺陷都抓得到」的保證。
- **可重複性（repeatability）**：同一台機器重跑時，能否再次製造相近條件；**可重現性（reproducibility）**則更進一步要求結果也一致。
- **誤報／漏報**：誤報是把健康設備判成故障，漏報是有問題卻沒有抓到；兩者都需要有好、壞樣本與完整分母才能量化。
- **隔離池（quarantine pool）**：把已知或疑似有問題的主機移出正式工作，保留給重測、比較與根因分析的受控設備池。
- **可現場更換零件（FRU）**：維修人員可直接更換的模組，例如板卡或電源；找出故障晶片不一定就等於知道該換哪個 FRU。
- **管理控制器（BMC）**：即使主機作業系統異常，仍可從機外收集紀錄、管理電源、重啟與維修資料的控制器。
- **退回分析（RMA）**：把疑似故障的零件退回供應商重測、分析或更換；診斷工具報錯不會自動決定是否符合 RMA 條件。
- **DCGM**：NVIDIA Data Center GPU Manager，提供 GPU 監測與主動診斷；本文引用它的公開測試能力與限制，不把它視為所有加速器的共同標準。
- **OpenDCDiag**：OCP 規格列出的開源資料中心診斷框架之一；被規格列名不等於已遵循共同 SDC 輸入輸出格式。
- **Server Component Resilience v1.0**：OCP 的伺服器元件韌性規格版本；它定義測試交換與品質欄位，不代表現有工具都已實作。
- **OCP**：Open Compute Project，開放資料中心硬體規格社群；本文引用其跨公司共同規格，不代表所有成員產品已完成相同實作。
- **Q-pool**：quarantine pool 的縮寫；OCP 規格用它指含已知壞與疑似壞設備的隔離池，不代表池內每台都已確診或符合 RMA。
- **v1.1**：本文引用的 OCP Silent Data Corruption in AI 白皮書版本；版本號只固定本次證據內容，不表示它是產品符合性認證。
- **NIST**：美國國家標準與技術研究院；本文只引用其工程統計方法，不把通用公式當成任何加速器的實測結果。
- **獨立試驗機會**：每一次都能清楚判定有無指定事件，且不受其他次結果影響的觀測單位；同一台設備重跑通常不能直接假設彼此獨立。
- **二項試驗**：把每個固定機會只分成事件發生或未發生，並假設共同機率與獨立性的模型；現實分層不符合時要先拆開。
- **單側 95% 上限**：在明示模型下，只對未知事件率的上邊界作 95% 信心水準推論；它不是點估計，也不是「真值有 95% 機率在裡面」的產品保證。
- **裝置時數（device-hour）**：一台裝置運作一小時的暴露量；一千台各一小時與一台一千小時雖同為一千裝置時數，老化、批次與工作負載結構可能不同。
- **固定發生率模型（HPP／exponential）**：假設事件在時間中以不變速率發生的模型；若磨耗、資料或環境會改變風險，就不能無條件套用。
- **平均故障間隔（MTBF）**：固定發生率模型下，兩次合格事件之間的平均時間；零事件只能產生單側下限，不能證明 MTBF 無限大。
- **FIT**：每十億裝置時數一個合格事件的速率單位；事件定義不同的 FIT 不能互相比較。
- **混淆矩陣**：把真實好壞與測試 pass／fail 交叉成四格，讓抓到、漏掉、誤殺與正確放行各自有分母。
- **靈敏度（sensitivity）**：已知壞樣本中被測試抓到的比例；只看它會漏掉健康設備被誤判的成本。
- **誤報率（false-positive rate）**：已知好樣本中被錯判為 fail 的比例；它和所有 fail 裡有多少真的壞不是同一個分母。
- **陽性預測值（precision）**：所有被標成 fail 的設備中，實際已知壞的比例；它會隨測試池的好壞組成改變。
- **基準發生率（base rate）**：在被評估母體中，事件原本占多少；沒有真實母體分母時，不能把刻意挑選的測試池比例當成機群盛行率。

### 三句話抓重點

- SDC 最危險的地方不是設備停機，而是設備繼續運作，卻把錯誤答案交給訓練、推論或資料系統。
- 工廠、燒機、整機驗收、上線前診斷、運行中監測與隔離返修各自只能看到部分故障；任何一次通過都不是終身健康證明。
- OCP 已把共同分類、測試資料與品質指標寫進規格，但公開工具尚未遵循同一交換格式，也沒有共通的誤報、漏報、隔離與 RMA 門檻，所以不能直接換算成測試時間、設備需求或台灣公司收入。

### 為什麼重要

**這像一個沒有冒煙的火災。** 一般故障會停機或亮紅燈，SDC 卻可能讓程式繼續跑。畫面看似
正常，最後保存的資料、模型參數或判斷結果已經偏離正確答案。

**每一站都要交接同一張病歷。** 工廠說「通過」、整機廠說「重測失敗」、資料中心說「某個
工作負載偶爾算錯」，如果沒有測試版本、輸入、環境、正確答案、失敗零件與處置紀錄，三方
其實無法確認是不是同一個問題。

**通過一項測試，只代表那一項沒有抓到錯。** NVIDIA 的公開文件也明確提醒，診斷通過只適用
已執行的檢查；測試跳過、環境錯誤與硬體缺陷更不能混成同一種結果。研究時因此要先問「測了
什麼、沒測什麼」，最後才問誰可能增加收入。

### 接下來怎麼追

- 先追 OCP 的交換格式是否被 DCGM、OpenDCDiag 或其他框架真正採用，並能輸出同一組測試、環境、裝置與處置欄位。
- 再追至少兩個平台用好、壞與疑似設備公布 coverage、repeatability、誤報、漏報、測試成本與隔離條件。
- 接著找工廠、系統整合商、資料中心與晶片供應商共同揭露的 part history：同一零件如何從首次失敗、重測、隔離、根因分析走到修復或報廢。
- 最後才查本 universe 公司是否有具名 tester、socket、板卡、BMC、整機驗收或維修責任，並由客戶資格與財務分母交叉確認。

### 想一想

- 一張 GPU 通過三分鐘矩陣運算，能證明它在不同資料、溫度與電壓下運作兩年都不會算錯嗎？
- 一個測試找到錯誤答案，若無法定位到主機、板卡或晶片，營運團隊該隔離什麼，供應商又該分析什麼？
- 工廠測試時間增加，卻沒有公開抓到多少額外缺陷、減少多少漏報或由誰付費時，能直接推成設備商收入嗎？

## 主張與證據帳本

本文只把一手文件直接支持的分類、流程、工具能力與限制列為「證實」。跨平台共同門檻、完整
RMA 閉環及台灣公司價值線仍是未證實主張；平台內的測試頻率也不拿來做跨公司比較。

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: Open Compute Project
title: Silent Data Corruption in AI Whitepaper Version 1.1
published_at: 2025-12-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/sdc-in-ai-ocp-whitepaper-ver-1-1-final-pdf
locator: PDF pp.7–8 的 benign／corrected／DUE／SDC taxonomy，pp.14–21 的生命週期測試、機群偵測、隔離、結構與功能測試，pp.23–27 的硬體指標與 AI correctness、非決定性及標準化 benchmark 缺口
limitation: 白皮書彙整跨公司研究與最佳實務，不是產品符合性清單、共同誤報漏報資料、隔離門檻、RMA 規則或台灣供應商證據
independence_group: ocp-sdc-whitepaper
-->

<!-- research_source
source_id: S2
role: standard
source_kind: document
publisher: Open Compute Project
title: Server Component Resilience Revision 1.0
published_at: 2024-09-27
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/external-ver-1-0-open-compute-specification-server-component-resilience-sdc-workstream-docx-1-pdf-1
locator: PDF pp.7–16 的 CPU／GPU／accelerator scope、test input、test output、manufacturing／post-manufacturing、part history、Q-pool、coverage、repeatability、reproducibility、cost 與 time-to-fail；pp.19–23 的 test flow 與 framework 現況
limitation: 規格定義交換欄位與評估方法；它明示現有 DCGM、OpenDCDiag、Open Field Health Check 尚未符合該輸入輸出格式，且不提供公開跨平台誤報漏報、共同隔離或 RMA 門檻
independence_group: ocp-server-component-resilience
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Meta
title: How Meta keeps its AI hardware reliable
published_at: 2025-07-22
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://engineering.fb.com/2025/07/22/data-infrastructure/how-meta-keeps-its-ai-hardware-reliable/
locator: Types of hardware faults、Key challenges、Novel SDC detection mechanisms、training／inference impact 與 mitigation；包含 Fleetscanner、Ripple、Hardware Sentinel、reductive triage、quarantine 及 factory-to-fleet 建議
limitation: Meta 的自有機群方法、頻率與結果只代表其公開場域；文章沒有共同產品 qualification、跨平台誤報漏報、RMA 門檻或 universe 公司財務資料
independence_group: meta-sdc-fleet
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DCGM Diagnostics
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/dcgm-diagnostics.html
locator: 2026-08-12 的 active diagnostics 使用時點、run levels、structured results、configuration 與 Beyond Scope；明示不修復故障、不取代 offline field diagnostics、不判定 RMA eligibility
limitation: 動態文件會隨 DCGM 版本更新；測試失敗可能來自主機、權限、函式庫、拓撲、散熱、電力或工作負載干擾，不自動證明 GPU 晶片缺陷
independence_group: nvidia-dcgm
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DCGM Diagnostic Plugin
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/datacenter/dcgm/latest/reference/diagnostics/plugins/diagnostic.html
locator: 2026-08-12 的 sustained matrix、framebuffer correctness、operating-condition monitoring、parameters 及 pass／fail codes；錯誤計算會回報 faulty memory data-path result
limitation: 只驗證指定 GPU、資料路徑、測試時間與參數；pass 不涵蓋未執行 plugin、所有資料狀態、長期磨耗、其他供應商平台或 RMA 結論
independence_group: nvidia-dcgm
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Google Cloud
title: Report faulty host - AI Hypercomputer
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host
locator: 2026-08-12 的 faulty host process、SILENT_DATA_CORRUPTION reason、主機停止、修復與 managed／all-capacity 路徑
limitation: 這是客戶回報與雲端主機處置介面；疑似 SDC 可含 vCPU、軟體或核心問題，且文件要求先調查並以 best effort 處理，不是自動根因、共同隔離門檻或零件 RMA 判定
independence_group: google-cloud-host-repair
-->

<!-- research_source
source_id: S7
role: other_primary
source_kind: document
publisher: Google Research
title: Detection and Prevention of Silent Data Corruption in an Exabyte-scale Database System
published_at: 2022-01-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://research.google/pubs/detection-and-prevention-of-silent-data-corruption-in-an-exabyte-scale-database-system/
locator: 2022 IEEE Workshop publication abstract；Spanner 的應用層偵測／預防、手動與自動移除故障機器，以及定量分析仍困難的邊界
limitation: 摘要是資料庫應用案例，不是 AI accelerator 工廠測試、完整方法資料、跨平台門檻或本 universe 曝險
independence_group: google-research-spanner-sdc
-->

<!-- research_source
source_id: S8
role: other_primary
source_kind: document
publisher: Google Research
title: Silent Data Corruption by 10× Test Escapes Threatens Reliable Computing
published_at: 2025-01-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://research.google/pubs/silent-data-corruption-by-10-test-escapes-threatens-reliable-computing-4/
locator: IEEE Design & Test 42(6) publication page與 abstract；將 manufacturing test escapes、system-behavior diagnosis、in-field detection 與新測試實驗連成三條改善路徑
limitation: 公開頁面只提供論文摘要；標題的 10× 是作者研究結論，不作跨所有晶片、平台與供應商的普遍倍數，也不換算設備需求或收入
independence_group: google-research-test-escapes
-->

<!-- research_source
source_id: S9
role: standard
source_kind: living_index
publisher: Open Compute Project
title: OCP GPU and Accelerator RAS Requirements Version 1.0
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/ocp-gpu-and-accelerators-ras-requirements-1-0-final-pdf
locator: PDF pp.13–18 的 metrics、CE／DUE／SDC、containment、FRU 與 recovery；pp.29–41 的 error report、error injection、debug dump 與 compliance tool；appendix 中多項 schema 與 targets 留待後續版本
limitation: RAS 規格同時涵蓋可偵測錯誤與服務流程，不能把 error reporting／poison／reset 能力等同於已偵測所有 SDC；部分目標、discovery 與 schema 仍為協商或未來工作
independence_group: ocp-gpu-ras
-->

<!-- research_source
source_id: S10
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-12 起追蹤 packtest、semiequip、serverodm 族群的法說、季報、重大訊息、具名平台資格、測試責任與財務資料
limitation: 查詢入口本身不證明任何公司提供 SDC 測試、隔離、BMC、整機驗收、RMA 服務或取得相關收入
independence_group: twse-mops
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: Exact Binomial Confidence Limits
published_at: 2010-10-05
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbici.htm
locator: Description 與 one-sided limits；當 failure 或 sample size 很小時，對稱常態近似可能不夠準確，頁面提供以 binomial CDF 求 exact limits 並明示可計算單側界線
limitation: 這是通用二項比例方法，不是 SDC、加速器、診斷工具或機群結果；套用前必須固定事件、N、共同機率及獨立試驗假設，重複相關測試不能直接累加成獨立 N
independence_group: nist-engineering-statistics
-->

<!-- research_source
source_id: S12
role: other_primary
source_kind: living_index
publisher: National Institute of Standards and Technology
title: Constant repair rate HPP exponential model
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm
locator: Confidence Interval Equation and Zero Fails Case；零故障時只有單側 MTBF 下限 T／−ln(alpha)，並列明 fixed-time repairable systems 或失效後替換的新單位才屬 exact 情境
limitation: HPP／exponential 假設固定事件率；SDC 可能依資料、電壓、頻率、溫度、壽命、批次與偵測能力改變，故裝置時數換算只是一階上限模型，不是產品壽命、零風險或 RMA 保證
independence_group: nist-engineering-statistics
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: OCP SDC in AI v1.1 將硬體故障結果分成 benign fault、fault corrected、DUE 與 SDC；只有錯誤輸出未觸發硬體內建偵測者才屬 SDC，已被偵測或修正的錯誤不應混稱 SDC
supporting_source_ids: S1
contrary_source_ids:
as_of: 2025-12-16
basis: S1 PDF pp.7–8 直接定義四種結果及 false／true DUE 邊界
boundary: 分類對齊不代表各平台已用同一 error code、測試向量、嚴重度、隔離或 RMA 門檻
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
claim: SDC 的觸發可能依資料、電壓、頻率、溫度與設備壽命而變，製造缺陷、製程邊緣與磨耗也可能只在特定條件顯現；因此單次工廠或驗收通過不能替整個生命週期背書
supporting_source_ids: S1,S3,S8
contrary_source_ids:
as_of: 2026-08-12
basis: S1 pp.8、14、20–21 說明 small-delay defect、operating-condition dependence、life-cycle testing 與 structural／functional trade-off；S3 提供 Meta 同方向場域說明；S8 將 test escapes 與 in-field detection 串起來
boundary: 來源支持「需要多層測試」，不支持每顆晶片都會磨耗成 SDC、固定增加多少測試時間，或特定設備訂單必然成長
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
claim: OCP Server Component Resilience v1.0 已為 CPU、GPU 與 accelerator 定義 test input、test output、manufacturing／post-manufacturing test、part history、Q-pool、coverage、repeatability、reproducibility、test cost 與 time-to-fail；但同一規格明示列出的三套框架當時尚未符合其輸入輸出格式
supporting_source_ids: S2
contrary_source_ids:
as_of: 2024-09-27
basis: S2 PDF pp.7–16 逐欄定義交換資料與 metrics，pp.19–23 描述 framework 並在 p.20 明示 not compliant with this specification's input and output format
boundary: 有共同規格不等於已有共同資料庫、工具實作、公開測試池、跨平台結果或量產採用率
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
claim: Meta 公開的自有機群做法同時使用維護窗口的定向測試、與工作負載共存的短測試及分析式異常偵測，並在訓練錯誤時縮小範圍、隔離可疑節點後從 checkpoint 重啟
supporting_source_ids: S3
contrary_source_ids:
as_of: 2025-07-22
basis: S3 Novel SDC detection mechanisms、SDCs in training workloads 與 mitigation 段落直接描述 Fleetscanner、Ripple、Hardware Sentinel、reductive triage、quarantine 與 checkpoint restore
boundary: 這證實 Meta 的部署方法，不建立業界共同頻率、coverage、誤報漏報、隔離門檻或任何供應商營收；Meta 揭露的 45–60 天 cadence 只屬其方法背景，不作跨公司 benchmark
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: NVIDIA DCGM 可在主機內執行已知答案的運算與 framebuffer 測試，錯誤計算可回報 data-path failure；但 DCGM 文件明示診斷不修復故障、不取代 offline field diagnostics、也不決定 RMA eligibility，且執行環境問題也可能造成 fail
supporting_source_ids: S4,S5
contrary_source_ids:
as_of: 2026-08-12
basis: S5 列出 matrix／framebuffer correctness 與 DCGM_FR_FAULTY_MEMORY；S4 Beyond Scope、results、configuration 段落界定維修、RMA 與 environment failure 邊界
boundary: DCGM pass／fail 只適用已執行 plugin、SKU、參數、時間與環境，不能替其他平台、未執行路徑或長期可靠度背書
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 公開 operator 流程已把「發現可疑錯誤」與「移出正式工作」分開：Google Research 描述應用層偵測及手動／自動移除故障機器，Google Cloud 也提供 SILENT_DATA_CORRUPTION fault reason 與主機修復流程，但要求先調查且不把原因限定為硬體
supporting_source_ids: S6,S7
contrary_source_ids:
as_of: 2026-08-12
basis: S7 abstract 直接描述 Spanner detection／prevention 與 faulty-machine removal；S6 列出 SDC reason、report、stop／repair 流程與調查提醒
boundary: 主機被回報或移除不證明已定位 GPU、CPU、軟體或核心根因，也不等於供應商接受 RMA、永久修復或跨平台門檻一致
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: 一條可稽核的 SDC 生命週期責任鏈至少要把測試版本與環境、輸入與正確答案、結果與失敗時間、裝置與 FRU 定位、隔離／修復決策、part history 及供應商回饋串在一起；任何單站的 pass、fail 或警報都不能替其他站背書
supporting_source_ids: S1,S2,S3,S4,S5,S6,S7,S9
contrary_source_ids:
as_of: 2026-08-12
basis: S2 提供共同交換欄位與 part history，S1／S3 建立跨生命週期偵測與隔離，S4／S5 界定工具 verdict，S6／S7 建立 operator removal，S9 補上 FRU、error report、debug dump、error injection 與 service action
boundary: 這是研究端綜合出的驗證契約，不主張只有一種實作、已形成法定責任、所有場域都能追到晶片根因，或契約完整必然增加硬體支出
verification_needed: 具名平台公布固定 test／firmware version、input、expected result、environment、device identity、repeat count、coverage、false positive／negative、quarantine、repair、root cause 與 part-history feedback
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: DCGM、OpenDCDiag、Open Field Health Check 或其他主要平台已遵循同一 OCP SDC 輸入輸出格式，並以同一好壞樣本公布可比較的 coverage、誤報、漏報、測試成本與隔離門檻
supporting_source_ids:
contrary_source_ids: S1,S2,S4
as_of: 2026-08-12
basis: S2 明示三套 framework 尚未符合共同格式；S1 把 repeatable scalable representative resilience benchmark 列為待建方向；S4 的 threshold 與 plugin availability 仍依 SKU、configuration 與環境
boundary: 各平台有測試工具、共同作者或相似結果欄位，不等於已完成同一資料契約與可比較統計
verification_needed: 固定版本共同 schema、同一 hardware pool snapshot、known-good／known-bad／suspect 分母、測試矩陣及公開 confusion matrix 與 quarantine decision
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: 工廠、整機整合、機群營運與晶片供應商已用同一 part history 完成從 test escape、重現、隔離、根因分析、RMA 到製造測試改善的跨公司閉環
supporting_source_ids:
contrary_source_ids: S2,S4,S6,S9
as_of: 2026-08-12
basis: S2 規格要求 part history 但 Q-pool 管理與部分供應商資料仍待後續或可能受 NDA 限制；S4 不決定 RMA；S6 只到 host repair；S9 的部分 discovery、targets 與 schema 留待後續版本
boundary: 單一 operator 內部 quarantine、供應商 diagnostic log 或一次故障分析都不能代替跨公司的可回查 closed loop
verification_needed: 同一 serial／part identity 的 factory test、SLT、fleet incident、quarantine、vendor FA、RMA disposition、corrective action 與新 test coverage 紀錄
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: 本 universe 的封測、半導體設備或伺服器 ODM 公司已承擔可定位的 SDC 測試、裝置隔離、BMC／診斷整合或 RMA 閉環，並形成具名 qualification、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: OCP、Meta、NVIDIA 與 Google 來源沒有把 universe 公司、具名產品、買方資格、測試分母、合約責任與財務科目連在一起；S10 只作後續一手申報入口
boundary: 封測能力、tester／socket 產品、伺服器出貨、BMC 能力、OCP 會員或 AI 關鍵字都不能單獨證明 SDC 曝險
verification_needed: 客戶與公司雙向文件確認具名 tester／socket／board／BMC／system、SDC test item、acceptance responsibility、deployment、unit／time denominator、收入及毛利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: NIST 的 exact binomial 方法指出，當 failure 或 sample size 很小時，對稱常態近似可能不夠準確，應以 binomial CDF 求 exact confidence limits，且可計算單側界線
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-08-14
basis: S11 Description、equation 與 one-sided limits 段落直接說明比例、sample size、exact method 及單側計算
boundary: 方法只在事件、N、共同機率與獨立二項機會固定時成立；它沒有提供任何 SDC detector 的實際零事件樣本、coverage、裝置分層或產品門檻
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: NIST 的固定修復率模型指出，總暴露時間 T 內零次合格失效時，只能得到單側 MTBF 下限 T／−ln(alpha) 與相對應事件率上限，不能得到 MTBF 上限或宣稱零風險
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-14
basis: S12 zero fails case 直接列公式、解釋及 fixed-time exact 適用情境
boundary: HPP／exponential 假設固定事件率；若裝置不替換、磨耗率改變、測試覆蓋不同、批次相關或 SDC 依資料與環境觸發，公式可能只近似或不適用
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: OCP SDC in AI v1.1 把維護窗口的分鐘級週期篩檢與工作負載共存的毫秒至秒級短測試分開，並指出兩類方法存在約 70% 重疊 coverage 與各自獨有部分，因此不同測試的 coverage 不能直接相加
supporting_source_ids: S1
contrary_source_ids:
as_of: 2025-12-16
basis: S1 PDF p.14 的 Novel Detection Mechanisms 段落直接列 cadence、時間尺度、fleet sweep 與 overlapping／unique coverage
boundary: 70% 是白皮書引用特定方法的場域觀察，不是所有 SDC 測試、架構、裝置或客戶的共同 coverage，也沒有公開同一 hardware pool 的完整 confusion matrix
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C14
label: inference
status: active
claim: 判讀一份 SDC 零事件或隔離成效主張，至少應把事件定義、暴露單位、獨立性與分層、detector 版本、ground truth、混淆矩陣、信賴上限、隔離與放行、part history／RMA 及可用性與財務綁成同一份十欄證據護照
supporting_source_ids: S1,S2,S11,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S1 固定資料、環境、壽命與多機制 coverage 邊界，S2 固定 hardware pool、Q-pool、coverage、repeatability、cost、time-to-fail 與 part history，S11／S12 分別固定零二項事件與零時間事件的單側界線
boundary: 十欄護照是本文研究工具，不是 OCP、NIST、NVIDIA、Meta 或 Google 的共同 SDC 標準；現有公開資料沒有同一具名產品把完整 raw verdict、獨立暴露、ground truth、隔離、RMA、成本及財務共同鍵公開
verification_needed: 至少兩套 framework 對同一具名 hardware pool 公開事件定義、device／test／time denominators、版本、分層、pass／fail／skip、ground truth、confusion matrix、confidence bound、quarantine／release、RMA 與成本
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 先分清四種結果：沒有錯、已修正、停下來與悄悄算錯

| 硬體故障後的結果 | 程式拿到的答案 | 系統有沒有警報 | 營運上通常先做什麼 | 為何不能混稱 SDC |
|---|---|---|---|---|
| 良性錯誤 | 仍正確 | 不一定 | 通常無需處置 | 故障沒有改變程式輸出 |
| 已修正錯誤 | 修正後正確 | 有紀錄或計數器 | 觀察是否累積、是否接近失效 | 內建機制已抓到並修好 |
| DUE | 不交付不可信答案 | 有警報 | 停止、重試、reset 或回到 checkpoint | 問題已被偵測，只是無法修正 |
| SDC | 錯誤 | 沒有硬體警報 | 要靠額外測試、重算、比較或應用異常才可能發現 | 錯誤結果被當成正確答案繼續使用 |

這個分類先回答「系統看見什麼」，不是根因。相同的錯誤答案可能來自晶片缺陷、板卡電源、
散熱、韌體、驅動程式或軟體；所以看到 SDC 現象後，仍要重現、縮小範圍並留下環境資料。

## 一次通過不等於一生可靠：六個生命週期站點

| 生命週期站點 | 主要目的 | 它可能抓到什麼 | 它不能替誰背書 |
|---|---|---|---|
| 1. 晶片與封裝製造測試 | 出廠前攔下結構、時序與組裝缺陷 | 可被既有故障模型、電壓、溫度與向量觸發的缺陷 | 沒跑到的資料狀態、整機交互作用與日後磨耗 |
| 2. 燒機與壓力測試 | 用時間、溫度或負載提早暴露邊緣設備 | 早期失效、熱或電力敏感、較易重現的間歇問題 | 所有實際工作負載與多年使用情境 |
| 3. 整機整合與客戶驗收 | 在板卡、電源、散熱、韌體與網路都裝好後測試 | 只有完整系統才會出現的相容性或資料路徑問題 | 上線後的新軟體、資料分布與大規模同步效應 |
| 4. 工作前與維修後主動診斷 | 節點空閒時用已知答案確認是否適合接工作 | 指定運算、記憶體、互連、功率或效能路徑 | 未執行的 plugin、被 skip 的測試與未覆蓋狀態 |
| 5. 運行中偵測 | 在正式工作期間用短測試、分析或應用層檢查找異常 | 隨時間、資料或負載才顯現的錯誤 | 尚未出現、沒有比較基準或被模型雜訊掩蓋的錯誤 |
| 6. 隔離、重測與供應商回饋 | 移出工作、定位 FRU／晶片並把根因送回測試設計 | 可重現的壞設備、環境問題、維修與測試逃逸 | 沒有 serial／part history、無法重現或供應商未接受的 RMA |

真正的閉環不是「每站都多測一次」，而是後一站發現的新缺陷能不能回到前一站，形成新的測試
內容或製造改善。如果資料中心只把節點換掉，卻沒有把失敗條件、零件身分與分析結果帶回供應商，
下一批設備仍可能讓同類缺陷再次逃逸。

## 每一站要交接的不是「好／壞」，而是六欄測試契約

| 交接欄位 | 最少要留下什麼 | 少了會發生什麼 |
|---|---|---|
| 1. 測試身分 | 工具、版本、參數、編譯方式與執行命令 | 同名測試其實不是同一內容，無法比較 |
| 2. 題目與答案 | 輸入資料、正確輸出、比較方法與超時條件 | 只能說「看起來異常」，無法證明算錯 |
| 3. 執行環境 | 裝置、韌體、驅動、作業系統、電壓、頻率、溫度、裸機或容器 | 重跑失敗時，不知道是環境改變還是缺陷消失 |
| 4. 結果品質 | pass／fail／skip、第一次失敗時間、重跑次數、coverage 與成本 | 把沒跑成當通過，或拿一次偶發結果當確診 |
| 5. 定位與處置 | 主機、板卡、晶片或 FRU 身分，隔離、reset、換件與復原結果 | 知道有錯，卻不知道該移除什麼、誰負責 |
| 6. 零件病歷 | 製造測試、燒機、整機測試、首次失敗年齡、供應商分析與改善動作 | 工廠、整機與機群各有一段故事，無法形成根因閉環 |

OCP Server Component Resilience v1.0 的價值正在這裡：它不只是說「要做 SDC test」，而是把
輸入、輸出、環境、失敗時間、重現率與 part history 拆成可交換欄位。不過規格也坦白記錄，
列出的現成框架當時還沒有遵循同一格式；因此目前是**共同病歷表已畫好，醫院還未全面用同一張表**。

## 三套公開做法，各自只看到責任鏈的一個切面

| 公開做法 | 已證實能力 | 適合放在哪一站 | 不能從它推出什麼 |
|---|---|---|---|
| Meta Fleetscanner／Ripple／Hardware Sentinel | 維修窗口定向測試、運行中短測試與分析式異常偵測可疊加使用 | 工作前、運行中、隔離與縮小範圍 | 其他 operator 採相同頻率、工具有共同誤報漏報，或台廠因此受惠 |
| NVIDIA DCGM Diagnostics | 能對指定 GPU 執行運算與 framebuffer 已知答案測試，輸出細分結果與錯誤碼 | 整機、工作前、失敗後重測 | 診斷會自動修復、一定定位到晶片、決定 RMA，或 pass 等於長期健康 |
| Google 應用與主機處置 | 應用層可偵測／避免部分資料損壞並移除可疑機器；雲端介面可回報 SDC 後停止與修復主機 | 運行中、主機隔離與服務復原 | 回報原因必然是硬體、已找到 FRU、供應商已接受 RMA 或共同門檻已成立 |

三者不是互相替代。已知答案測試擅長重現指定資料路徑；應用層檢查能看到最終資料或模型是否
偏離；機群分析能從大量工作找出異常設備。可用的責任鏈要把它們的結果串起來，而不是選一套
工具後宣稱問題已全部解決。

## 為什麼「多跑測試」仍可能抓不到

1. **題目空間太大**：硬體可能只在少數資料組合與指令順序算錯，測試無法窮舉所有輸入。
2. **環境會改變答案**：電壓下降、溫度上升、頻率、供電雜訊與高切換負載可能讓邊緣缺陷才出現。
3. **缺陷會隨時間變化**：同一內容今天通過，磨耗後可能失敗；只測出廠時點會漏掉生命週期問題。
4. **coverage 的分母只含已知缺陷**：一項測試能抓到所有已收錄壞機，也不能保證抓到尚未見過的新缺陷。
5. **AI 工作本身不完全決定性**：相同模型重跑仍可能因排程與數值順序略有差異，使硬體錯誤和正常波動難分。
6. **測試也會失敗在環境**：權限、函式庫、散熱、電力或工作負載干擾都可能造成 fail；沒有錯誤碼與環境紀錄就會誤換健康零件。

所以一份可信報告不能只寫「測試通過率」。它至少要分出實際執行、跳過、環境失敗、抓到已知
缺陷、抓到新缺陷，以及健康設備被誤判的數量；現有公開資料尚不足以做跨平台統計比較。

## 零次命中不是零風險：先鎖試驗機會、裝置時數與錯判矩陣

「跑了一百次都沒錯」只是一筆觀察，不是錯誤率等於零。先要問每一次是不是同一個事件定義、
是不是可視為獨立機會，以及 detector 沒有命中是否真的代表底層沒有 SDC。NIST 的 exact binomial
方法特別提醒，事件數或樣本小時不宜用對稱常態近似；零事件只能報單側上限。

### 零次錯誤也有上限，而且上限由 N 決定

在每次機會彼此獨立、事件機率相同、事件一定能被觀察的匿名二項教材裡，若 N 次都零事件，
事件機率的一側 95% exact 上限為：

事件率上限＝1−0.05 的 1／N 次方。

| 匿名零事件情境 | 獨立試驗機會 N | 觀察事件 | 一側 95% 上限 | 換成 ppm |
|---|---:|---:|---:|---:|
| 小型驗證 | 100 | 0 | 2.951304961% | 29,513.049607 ppm |
| 擴大驗證 | 1,000 | 0 | 0.299124955% | 2,991.249545 ppm |
| 大型匿名母體 | 1,000,000 | 0 | 0.000299573% | 2.995728 ppm |

一百次零命中仍只把上限壓到約 2.95%，一百萬次才壓到約 3 ppm。可是同一 GPU 用相同向量連跑
一百次，很可能共享資料、溫度、電壓、磨耗與缺陷狀態，不能自動算成一百個獨立機會。若 detector
本身會漏報，這張表限制的也只是「被該 detector 看見的事件」，不是底層真實 SDC 機率。

### 裝置時數相同，也要先確認事件率是否真的固定

對固定時間、固定事件率的 HPP／exponential 模型，NIST 對零故障給出的 95% 單側界線可改寫為：

MTBF 下限＝總裝置時數 T ÷〔−ln(0.05)〕；
事件率上限＝−ln(0.05) ÷ T。

| 匿名零事件暴露 | 總裝置時數 T | 觀察事件 | 95% 單側 MTBF 下限 | 95% 單側事件率上限 |
|---|---:|---:|---:|---:|
| 百萬裝置時數 | 1,000,000 | 0 | 333,808.200695 小時 | 2,995.732274 FIT |
| 十億裝置時數 | 1,000,000,000 | 0 | 333,808,200.695334 小時 | 2.995732 FIT |

這說明為何「累積很多小時都沒出事」仍要附總暴露量：百萬與十億裝置時數的零事件，速率上限差
一千倍。但 SDC 可能依資料、電壓、頻率、溫度與壽命改變；不同批次、軟韌體與工作負載也可能
共因失效。若事件率不固定、失效設備未按模型替換，或 detector coverage 隨版本改變，這個換算
只能當一階邊界，不能冒充產品 MTBF 或 RMA 門檻。

### 抓得到壞機與不誤殺好機，是兩個不同分母

再看一個刻意組成的匿名測試池：100 台已知壞設備與 10,000 台已知好設備，不代表真實機群盛行率。
假設測試抓到 90 台壞設備、漏掉 10 台，又誤把 50 台好設備標成 fail：

| ground truth | 測試 fail | 測試 pass | 小計 |
|---|---:|---:|---:|
| 已知壞 | 90 | 10 | 100 |
| 已知好 | 50 | 9,950 | 10,000 |
| 小計 | 140 | 9,960 | 10,100 |

| 指標 | 算式 | 固定結果 | 它回答什麼 |
|---|---|---:|---|
| 靈敏度 | 90 ÷ 100 | 90.000000% | 已知壞設備抓到多少 |
| 漏報率 | 10 ÷ 100 | 10.000000% | 已知壞設備放走多少 |
| 誤報率 | 50 ÷ 10,000 | 0.500000% | 已知好設備誤殺多少 |
| 陽性預測值 | 90 ÷ 140 | 64.285714% | 所有 fail 裡多少真的已知壞 |
| 隔離占比 | 140 ÷ 10,100 | 1.386139% | 這個刻意測試池有多少設備會先被移出工作 |

即使靈敏度有 90%，140 台被隔離的設備裡仍有 50 台是已知好設備。若真實機群的壞設備更少，
陽性預測值還會改變；所以不能拿刻意平衡或富集壞樣本的 validation pool 直接預測機群隔離量。
OCP 白皮書另外指出週期篩檢與工作中短測試存在重疊及各自獨有 coverage，也提醒研究者不能把兩套
工具的百分比直接相加成總 coverage。

### 多空小作文共用的 SDC 零事件—隔離十欄護照

| 本文十欄 | 至少要固定什麼 | 最常見的跳級 |
|---|---|---|
| 1. 事件定義 | wrong answer、DUE、diagnostic fail、application mismatch 或 supplier-confirmed defect | 把所有警報、錯誤答案與 RMA 混成一種 event |
| 2. 暴露單位 | device、test invocation、operation、device-hour、workload-hour 與觀察窗口 | 只報「跑很久」或「很多台」而沒有共同分母 |
| 3. 獨立性與分層 | product、lot、age、voltage、temperature、firmware、workload、data state 與相關結構 | 同一裝置重跑就把 N 無限放大 |
| 4. Detector 身分 | tool、plugin、version、參數、expected result、skip／environment error 與 coverage scope | 零 fail 等於零 defect |
| 5. Ground truth | known-good、known-bad、suspect、故障注入、supplier FA 與 label 時點 | 用未確認的 suspect 同時訓練又驗證 |
| 6. 混淆矩陣 | true／false positive、true／false negative、分母及信賴界線 | 只報 accuracy 或 pass rate |
| 7. 零事件上限 | binomial 或 time-rate model、信心水準、N／T、假設及 sensitivity correction | 零次命中直接寫零風險 |
| 8. 隔離與放行 | quarantine threshold、重測、release、repair、scrap、availability 與 repeat failure | 工具 fail 等於永久移除或 RMA 成立 |
| 9. Part history 與 RMA | serial、factory／SLT／fleet history、root cause、vendor disposition 與 corrective action | 換掉主機就宣稱根因閉環 |
| 10. 成本與財務 | test time、compute／energy、downtime、spares、false quarantine、合約責任、收入與毛利 | 技術風險直接映射設備需求或供應商獲利 |

較強的多方版本不是「零次錯誤所以平台可靠」，而是同一事件定義在預先分層的獨立暴露中，把
95% 上限壓到 acceptance threshold 以下，同時維持可接受的漏報、誤報與隔離成本，並沿 part
history 證明新增測試減少 field escape。較強的空方版本也不是「仍有上限所以測試無效」，而是
N／T 被相關重跑灌大、detector 有盲區、false quarantine 吃掉可用性，或工廠與機群沒有同一
serial／RMA 回饋。兩邊都必須交同一張護照。

### 分母、誤差與限制

第一張表是 N＝3 個匿名零事件情境，使用獨立同分布二項假設，報一側 95% exact upper confidence
bound；第二張表是 N＝2 個匿名總暴露情境，使用 fixed-time constant-rate HPP／exponential 假設，
報一側 95% rate upper bound 與 MTBF lower bound。第三組混淆矩陣是 N＝10,100 筆刻意組成的匿名
labelled records，其中已知壞 N＝100、已知好 N＝10,000；它是固定教材，不是真實機群抽樣。

Python math／Fraction 與獨立 awk 在顯示精度內完全一致。前兩組的誤差表達是模型條件下的單側
95% confidence bound，不再另報 sampling SE／t；混淆矩陣只是固定整數比例，也沒有 sampling
SE／t。真實 device、test、device-hour、workload、lot、product、customer 或 production run 的
物理樣本 N＝0，因此本文不估 SDC 盛行率、detector 效果、MTBF、隔離成本、設備需求、收入、毛利
或公司效果。NIST 與 OCP 是統計方法及產業標準兩條來源鏈，不是兩個產品、客戶或獨立實驗。

## 用七關判斷 SDC 需求是否真的形成

| 關卡 | 可觀察證據 | 通過後能說什麼 | 還不能說什麼 |
|---|---|---|---|
| 1. 分類對齊 | benign、corrected、DUE、SDC 與錯誤碼映射 | 大家描述的是同一類結果 | 測試或隔離門檻一致 |
| 2. 可執行測試 | 固定版本、輸入、正確答案、參數與結果碼 | 指定問題可以被重跑 | 所有 SDC 都能抓到 |
| 3. 品質可量化 | known-good／bad／suspect 分母、coverage、repeatability、誤報、漏報、成本 | 可以比較測試價值與代價 | 不同平台已採用相同門檻 |
| 4. 裝置可隔離 | 主機、板卡、晶片／FRU 身分與 quarantine 規則 | 錯誤能從正式工作移出 | 根因、RMA 與永久修復已完成 |
| 5. 病歷可回傳 | part history、供應商重現、failure analysis 與 corrective action | test escape 能回饋到前段測試 | 新測試已量產導入且有效 |
| 6. 跨平台重現 | 至少兩套獨立框架遵循共同格式，對同一設備池得到可比較結果 | 責任與測試資料可跨公司交接 | 台灣公司已有產品資格或收入 |
| 7. 客戶與財務 | 具名平台 qualification、部署／測試分母、合約責任、收入與毛利 | 才能建立公司材料性 | 估值、價格已反映程度與投資報酬 |

截至本輪，第一關已有 OCP 共同 taxonomy，第二關有多套可執行工具，第三至第五關已有規格欄位
但缺完整公開分母，第六關還被 OCP 自身的「框架尚未符合共同格式」卡住，第七關則沒有 universe
公司的雙向證據。這就是為什麼文章可以升格，受惠線仍不能升格。

## 誰負責，誰不能替別人背書

| 角色 | 主要責任 | 需要交出去的證據 | 不能替誰背書 |
|---|---|---|---|
| 晶片與封裝供應商 | 結構／功能測試、故障模型、製造條件、failure analysis | 製造測試、coverage、part identity、根因與改善 | 整機電力散熱、客戶軟體與機群門檻 |
| 封測與測試設備鏈 | 執行量產測項、溫度電壓條件、治具與判定 | tester／socket／handler、test time、重測與逃逸分母 | 該測項以外的工作負載與多年磨耗 |
| ODM／整機整合商 | 板卡、電源、散熱、韌體、BMC 與整機驗收 | 系統版本、SLT、節點身分、維修與換件紀錄 | 晶片根因、operator 的模型正確性與財務價值 |
| 平台診斷軟體 | 執行已知答案、收集 telemetry、輸出細分 verdict | plugin、參數、pass／fail／skip、logs 與 error codes | 自動修復、供應商 RMA 接受與完整生命週期健康 |
| 資料中心與工作負載團隊 | 運行中比較、異常偵測、縮小範圍、quarantine 與服務復原 | incident、checkpoint、host／device mapping、隔離與復原結果 | 工廠一定漏測、哪家設備商會增加收入 |
| 供應商維修與品質團隊 | 重現、根因、RMA disposition、corrective action 與新測試導入 | 同一零件的完整 part history 與改善前後 coverage | 改善已普遍部署、客戶已付費或財務材料性 |

## 這篇對個股判斷的用處與界線

1. **先找責任，不先找概念股**：公司究竟執行哪一站、哪一個測項、交付哪一份紀錄？只說「AI 測試需求增加」不夠。
2. **把測試時間拆成分母**：新增多少 test item、每台／每顆多多久、重測率、設備利用率與產能瓶頸是不同問題。
3. **把 BMC 與 ODM 能力拆成資格**：能收 log 或支援 Redfish，不等於已完成 SDC isolation workflow、客戶驗收與維修閉環。
4. **要求客戶與供應商雙向確認**：供應商產品頁、OCP 會員或一般 AI server 出貨不能單獨建立 design win。
5. **不做價格判斷**：本文沒有估值、預期差、部位、催化日期與市場價格資料，因此不是投資建議，也不判斷市場是否已反映。

## 這篇目前能說到哪裡

- **已知道的事**：跨公司共同分類已存在；測試輸入、輸出、part history 與品質指標也已有公開規格；Meta、NVIDIA 與 Google 分別證明機群偵測、主動診斷及主機／應用處置不是抽象概念。
- **為何可信度是中等**：證據來自多條獨立一手鏈，但 OCP 也直接揭露現有框架尚未使用共同交換格式，公開資料無法比較誤報、漏報、coverage 與隔離門檻。
- **還不能說的事**：不能說工廠已與機群形成完整 RMA 回饋、所有平台使用同一標準、測試時間必然增加、設備供不應求，或本 universe 公司已有相關收入。
- **何時可以升級判定**：共同 schema 被至少兩套框架採用，同一設備池公布完整分母與隔離結果，且具名客戶、製造／整機方與供應商能沿同一 part identity 重建 factory-to-fleet-to-RMA 病歷。

## 來源

- [OCP：Silent Data Corruption in AI Whitepaper v1.1](https://www.opencompute.org/documents/sdc-in-ai-ocp-whitepaper-ver-1-1-final-pdf)
- [OCP：Server Component Resilience Revision 1.0](https://www.opencompute.org/documents/external-ver-1-0-open-compute-specification-server-component-resilience-sdc-workstream-docx-1-pdf-1)
- [Meta：How Meta keeps its AI hardware reliable](https://engineering.fb.com/2025/07/22/data-infrastructure/how-meta-keeps-its-ai-hardware-reliable/)
- [NVIDIA：DCGM Diagnostics](https://docs.nvidia.com/datacenter/dcgm/latest/learn/modules/dcgm-diagnostics.html)
- [NVIDIA：DCGM Diagnostic Plugin](https://docs.nvidia.com/datacenter/dcgm/latest/reference/diagnostics/plugins/diagnostic.html)
- [Google Cloud：Report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host)
- [Google Research：Detection and Prevention of SDC in an Exabyte-scale Database](https://research.google/pubs/detection-and-prevention-of-silent-data-corruption-in-an-exabyte-scale-database-system/)
- [Google Research：Silent Data Corruption by 10× Test Escapes](https://research.google/pubs/silent-data-corruption-by-10-test-escapes-threatens-reliable-computing-4/)
- [OCP：GPU and Accelerator RAS Requirements v1.0](https://www.opencompute.org/documents/ocp-gpu-and-accelerators-ras-requirements-1-0-final-pdf)
- [公開資訊觀測站](https://mops.twse.com.tw/mops/web/index)
- [NIST：Exact Binomial Confidence Limits](https://itl.nist.gov/div898/software/dataplot/refman2/auxillar/exacbici.htm)
- [NIST：Constant repair rate HPP／exponential model](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm)

## 族群影響

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 製造測試、burn-in、SLT、重測與 part history 使封裝測試成為 SDC 生命週期前段的必要查核位置
evidence_boundary: 沒有 universe 封測公司具名 SDC test item、tester／socket、測試時間、escape／coverage 分母、客戶 qualification 或財務貢獻，不建立受惠排行
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: 新 fault model、voltage／temperature condition、diagnosis 與 failure analysis 可能改變測試及分析設備需求，形成後續搜尋路由
evidence_boundary: OCP 的 test metric 與 framework 不指定 universe 設備型號、測項、產能瓶頸、訂單或收入；不能由 test escape 論文直接外推設備需求
-->

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-30
rationale: ODM 位於系統層驗收、BMC／diagnostic integration、node identity、隔離、換件與供應商回饋的責任交界
evidence_boundary: 沒有 universe ODM 具名平台 SDC acceptance、quarantine workflow、RMA responsibility、deployment 分母或財務資料，不把一般 AI server 出貨視為證據
-->

## 監測器

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C7,C8,C9
metric: OCP SDC taxonomy、test exchange、hardware pool、coverage 與 part-history 規格是否形成可執行共同格式及公開 benchmark
source_ids: S1,S2
watch_source_ids: S4,S9
frequency: monthly
next_check: 2026-08-31
trigger: 新版本提供固定 schema、reference implementation、known-good／bad／suspect pool snapshot、coverage、repeatability、false positive／negative、quarantine 與 part-history output
invalidation: OCP 撤回共同交換方向，或公開跨框架試驗顯示欄位與 verdict 無法對齊且沒有替代 mapping
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C5,C6,C7,C8,C9
metric: Meta、NVIDIA 與 Google 是否公開跨工具 isolation threshold、field outcome、repair／RMA handoff 與 factory feedback
source_ids: S3,S4,S5,S6,S7
watch_source_ids: S3,S4,S5,S6
frequency: monthly
next_check: 2026-08-31
trigger: 至少兩個平台用固定版本與完整分母公布 test verdict、coverage、false positive／negative、host／FRU isolation、repair、root cause 及供應商 corrective action
invalidation: 平台文件明示 diagnostics 只供一般健康檢查且無法支援 SDC 證據或隔離，或場域資料顯示偵測成本高於效益且沒有替代方法
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C10
metric: 台灣 packtest、semiequip、serverodm 公司是否由客戶與自身申報雙向揭露具名 SDC 測項、責任、qualification、部署及財務分母
source_ids: S10
watch_source_ids: S10
frequency: quarterly
next_check: 2026-09-30
trigger: 客戶與公司一手文件同時確認具名平台／產品、factory／SLT／diagnostic／BMC／RMA scope、測試或部署數量、收入及毛利
invalidation: 公司或客戶明示只提供一般測試／伺服器功能、不承擔 SDC 驗收與閉環，且相關財務無法辨識
-->

## 還缺哪些證據

- 尚未找到至少兩套主要框架遵循同一 OCP SDC 輸入輸出 schema，對相同 hardware pool 公布可比較結果。
- 尚未找到跨平台完整 confusion matrix；沒有 known-good、known-bad、suspect、pass、fail、skip 與環境失敗分母，就不能量化誤報或漏報。
- 尚未找到共同 quarantine 與 RMA 門檻；主機移出工作、工具 fail、FRU 更換與供應商接受 RMA 是四個不同決策。
- 尚未找到同一零件從製造、燒機、SLT、機群 incident、供應商根因到 corrective action 的公開完整病歷。
- 尚未找到本 universe 公司與具名平台、測項、設備、責任、客戶資格、部署／測試分母及財務結果的雙向證據。
