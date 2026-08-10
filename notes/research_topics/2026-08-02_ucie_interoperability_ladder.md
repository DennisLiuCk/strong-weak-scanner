# UCIe 讓小晶片共用語言，但一次互通不代表生態系成熟：先分清設計、實體測試與客戶產品

<!-- research_topic
topic_id: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-03-05
last_reviewed_at: 2026-08-02
review_due: 2026-08-17
source_type: mixed
publisher: UCIe Consortium
publisher_domain: uciexpress.org
canonical_url: https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem
source_chain_id: ucie-spec-silicon-interop-20260802
stock_ids:
group_ids: ipdesign,packtest,pcb
trigger_type: standard_to_silicon_interoperability
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: UCIe Consortium、Intel／Cadence 實體展示與 Synopsys 64G IP tape-out 可建立三條一手證據鏈；但已展示的跨廠互通是 16G UCIe-S，尚不能證明 64G UCIe 3.0、完整協定組合、不同封裝與量產產品皆可互換
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_chiplet_interoperability_scan
evidence: source_chain:ucie-spec-silicon-interop-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_spec_ip_tapeout_live_interop_and_customer_product_stages
evidence: sources:S1,S2,S3
-->

<!-- research_source
source_id: S1
role: standard
source_kind: document
publisher: UCIe Consortium
title: UCIe Consortium Introduces 3.0 Specification With 64 GT/s Performance and Enhanced Manageability
published_at: 2025-08-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.uciexpress.org/_files/ugd/8dc731_ae67289d0ec646cdba5c1aee245538b3.pdf
locator: PDF page 1 lines 10–25；page 2 specification highlights 與 backward compatibility
limitation: 規格發布只證實介面與測試要求存在，不證明任何 64G 晶片已回片、跨廠互通、封裝量產或客戶採用
independence_group: ucie-consortium
-->

<!-- research_source
source_id: S2
role: standard
source_kind: document
publisher: UCIe Consortium
title: Chiplet Summit 2026: UCIe Momentum Across a Growing Ecosystem
published_at: 2026-03-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem
locator: first live UCIe-S interoperability demonstration 段落；Intel／Cadence independently designed chiplets、16G PHY 與 Cameron Creek
limitation: 展示由 Consortium 彙整，且只明確證實 16G UCIe-S 的特定 test chip 組合；沒有 48／64G、UCIe-A、長期可靠度、良率或量產客戶資料
independence_group: intel-cadence-demo
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Synopsys
title: How 64G UCIe IP Tape-Out Enables High-Speed Die-to-Die Connectivity
published_at: 2026-06-30
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.synopsys.com/blogs/chip-design/64g-ucie-ip-high-speed-die-to-die-connectivity.html
locator: Introduction 的 64Gbps UCIe IP on 2-nm tape-out；Key Features 與 Why It Matters 段落
limitation: IP 供應商自述的 tape-out／production-ready 不等於 silicon 回片驗證、第三方 compliance、跨廠 chiplet 互通、客戶產品 tape-out 或收入
independence_group: synopsys
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Synopsys
title: UCIe 3.0: Next-Gen Chiplet Connectivity and IP Solutions
published_at: 2026-07-27
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.synopsys.com/blogs/chip-design/ucie-3-0-chiplet-ip-solutions.html
locator: What’s new in UCIe 3.0；Enabling fast UCIe 3.0 adoption；Early momentum and what’s next
limitation: 公司頁可證實其 IP／EDA 支援聲明，不能代表其他供應商相容、實際客戶產品或全生態系成熟度
independence_group: synopsys
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: UCIe Consortium
title: UCIe Specifications
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.uciexpress.org/specifications
locator: 2026-08-02 查得 UCIe 1.0–3.0 規格、compliance testing 與版本入口
limitation: 規格索引只用來偵測版本與合規更新；頁面存在不構成 silicon、互通或部署證據
independence_group: ucie-consortium
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Synopsys
title: Synopsys UCIe IP Solution
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.synopsys.com/designware-ip/interface-ip/die-to-die/ucie.html
locator: 2026-08-02 查得 64G UCIe IP、interoperability 與 silicon success 更新入口
limitation: 產品頁是供應商自述；新增速度或 tape-out 仍需另找回片、compliance、客戶與跨廠證據
independence_group: synopsys
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: UCIe Consortium 於 2025-08-05 發布 UCIe 3.0，新增 48／64 GT/s、runtime recalibration、延伸 sideband 與 manageability，並維持向下相容
supporting_source_ids: S1
contrary_source_ids:
as_of: 2025-08-05
basis: S1 page 1–2 直接列出版本、資料率與功能
boundary: 這是標準能力，不是 64G 實體產品、跨廠互通、量產封裝或客戶採用
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
claim: 2026 Chiplet Summit 的 Cameron Creek 展示已把獨立設計的 Intel 與 Cadence chiplet 以 16G UCIe-S PHY 連接，形成可定位的跨廠實體互通證據
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-03-05
basis: S2 直接寫明 first live demo、independently designed chiplets、16G UCIe-S 與 successful interoperability testing
boundary: 只適用於該 test chip、PHY 與速度；不能外推為 64G UCIe 3.0、所有協定、封裝或供應商已互換
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
claim: Synopsys 於 2026-06-30 公開表示已完成 64Gbps UCIe IP 在 2nm 製程的 tape-out，並在 7 月說明其 UCIe 3.0 PHY／controller／verification flow
supporting_source_ids: S3,S4
contrary_source_ids:
as_of: 2026-07-27
basis: S3 Introduction 與 S4 Enabling fast UCIe 3.0 adoption 直接列示 tape-out 與工具鏈
boundary: Tape-out 是送製造節點，不等於回片成功、實測 64G、第三方 compliance、跨廠互通或客戶量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: UCIe 生態系已從紙上規格跨到部分實體互通，但成熟度仍不連續：已證實的跨廠展示是 16G，64G UCIe 3.0 則停在規格與供應商 IP tape-out，因此研究上必須分開追「速度」與「互通範圍」
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 定義 64G 標準，S2 鎖定 16G live cross-vendor demo，S3／S4 鎖定 64G IP tape-out；三種證據位於不同成熟度
boundary: 不據此預測 UCIe 市占、chiplet marketplace 時程、台灣公司 design win、先進封裝需求量或估值
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 64G UCIe 3.0 已完成至少兩家獨立 chiplet 的實體 compliance、在客戶封裝中長期穩定運作，或已讓台灣供應鏈取得可辨識收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 本輪只有 64G 規格、單一 IP 供應商 tape-out 與 16G 跨廠展示，沒有把三者連成同一個 64G 客戶產品的證據
boundary: 會員資格、IP 支援、simulation、tape-out、demo 與量產收入是六個不同節點
verification_needed: 需 64G test silicon 回片、第三方 compliance、至少兩家獨立 chiplet 的實體互通、具名封裝／客戶 qualification 與公司財務揭露
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5
metric: 64G UCIe 3.0 回片、compliance 與跨廠實體互通的速度及協定覆蓋
source_ids: S1,S2,S3,S4
watch_source_ids: S5,S6
frequency: weekly
frequency_detail: 每週檢查 Consortium 與 IP 供應商；出現 64G silicon、plugfest 或 compliance result 即重審
next_check: 2026-08-17
trigger: 至少兩家獨立 chiplet 在 64G 完成可重現的實體 interoperability，並公開封裝、協定與測試範圍
invalidation: 64G 回片或 compliance 延後、只剩 simulation／單一供應商 loopback，或不同封裝與協定無法互通
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C5
metric: UCIe 客戶產品 qualification、量產封裝與台灣公司財務足跡
source_ids: S2,S3
watch_source_ids: S5,S6
frequency: monthly
frequency_detail: 每月檢查具名 SoC／chiplet、foundry／OSAT qualification 與供應商法說
next_check: 2026-09-02
trigger: 客戶公布含多廠 UCIe chiplet 的量產產品，且供應商能以具名 IP、封裝或基板完成雙向核對
invalidation: 客戶仍採 captive chiplet、專有 die-to-die，或 UCIe 僅作內部同廠介面而沒有可交易生態系
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
reason: editorial_plain_language_wave103_ucie_package_positions_test_dimensions_evidence_objects_roles_and_six_gate_ecosystem_ladder
evidence: editorial:reader_only_wave103
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **小晶片（chiplet）**：把原本一大顆晶片拆成多顆各司其職的小晶粒，再放進同一封裝共同運作。
- **晶粒（die）**：從一片晶圓切下、尚未封裝的單顆半導體；一個封裝裡可以放入一顆或多顆晶粒。
- **封裝（package）**：把晶粒、接點、布線、供電與散熱結合成可裝進系統的元件，不只是外面的保護殼。
- **晶粒對晶粒連線（die-to-die）**：讓同一封裝內的晶粒直接交換資料與管理訊息的短距離連線。
- **通用小晶片互連（UCIe）**：為封裝內小晶片定義電氣、協定、管理與測試共同規則的開放介面。
- **介面控制器（controller）**：整理要傳送的資料、命令、流量與錯誤處理，再交給實體傳輸電路。
- **實體傳輸電路（PHY）**：把數位資料轉成晶粒間可傳送與接收的電氣訊號；有實體電路不等於完整協定已互通。
- **傳輸通道（lane）**：實體介面中並行傳送資料的一條路；速度、通道數與封裝布線要一起核對。
- **標準／先進封裝路徑（UCIe-S／UCIe-A）**：分別面向較傳統與更高密度封裝的實體連接方式，兩者不能共用同一筆測試結論。
- **每秒十億次傳輸（GT/s）**：介面每秒可完成的傳輸次數；它是傳輸率，不是單顆產品的產量、收入或成熟度。
- **16 與 64 的差別**：本文的 16 代表已展示的較低傳輸率，64 代表第三代規格的最高傳輸率；兩筆證據不是同一組產品。
- **旁帶與管理訊息（sideband／manageability）**：資料之外，用來啟動、監控、回報狀態與處理錯誤的控制訊息。
- **重新校準（recalibration）**：系統運作時重新調整連線參數，以因應溫度、電壓或訊號狀態改變。
- **傳輸協定（protocol）**：兩端如何包裝、解讀、排序與確認資料的共同約定；接通電氣訊號不等於所有協定功能都通過。
- **封裝內布線（package routing）**：在晶粒與載板之間安排訊號、電源與接地路徑，會影響損耗、干擾與可製造性。
- **微凸塊或接點（bump）**：晶粒與封裝布線之間的細小電氣接點；接點間距與品質會限制連線密度和良率。
- **時鐘、供電、散熱與測試共同設計**：小晶片不只要傳資料，還要共用穩定時序、電力、溫度管理與故障檢查。
- **介面智財（IP）**：可被晶片設計者整合進產品的控制器、實體傳輸電路或驗證設計；可用不等於已做成量產晶片。
- **電子設計自動化（EDA）**：協助設計、模擬、佈局與驗證晶片的軟體工具流程。
- **送廠製造（tape-out）**：設計完成並交給晶圓廠製造；它早於回片、實測、客戶驗證與量產。
- **回片（returned silicon）**：送廠後取得實體晶片並開始量測；回片本身仍不代表所有功能或速度通過。
- **測試晶片（test chip）**：為驗證介面、製程或封裝而設計的實體晶片，不等同完整客戶產品。
- **模擬（simulation）**：在軟體或模型環境預測設計行為；它能提早找錯，但不能取代實體晶片測試。
- **單晶片自我迴路測試（loopback）**：讓訊號在同一顆晶片或同一供應商設計內送出再收回，不能證明不同廠商互通。
- **跨廠互通（interoperability）**：不同廠商獨立設計的元件在公開條件下接在一起並完成指定功能。
- **符合規格測試（compliance）**：依共同測試計畫檢查產品是否符合指定版本、速度與功能要求，不等同客戶已採用。
- **客戶資格驗證（qualification）**：客戶把元件放進實際產品條件，檢查功能、可靠度、良率與供應穩定性。
- **單一公司內部設計與多廠供應**：同一家公司設計所有小晶片可以使用開放介面，但不能單獨證明零件可向不同供應商互換。
- **已知良品晶粒（known-good die）**：封裝前已通過指定測試的晶粒；多顆晶粒一起封裝時，可降低壞品拖累整包良率的風險。
- **封裝測試服務與載板（OSAT／substrate）**：把晶粒組裝、布線、測試並連到系統的製造角色與承載結構。
- **量產產品（production product）**：通過設計、製造、測試與客戶驗證後，能持續交付的具名產品，不只是展示樣品。
- **生態系成熟度**：多家供應商、設計工具、製造、封裝、測試與客戶能在可重現規則下持續合作的程度。

### 三句話抓重點

- 把一顆大晶片拆成多顆小晶片後，它們仍要在同一封裝裡交換資料、時鐘、管理訊息與錯誤狀態。
- 共同規則、送廠製造、測試晶片互通和客戶產品量產，是四種不同證據；其中一項成立不能替其他項畢業。
- 本輪已確認兩家獨立設計的測試晶片能在較低速度互通，也確認最高速度已有規格與介面設計送廠；還沒有同一組實體產品把最高速度、跨廠互通與客戶量產串起來。

### 為什麼重要

小晶片讓設計者有機會把運算、記憶體與輸入輸出等功能分開製造，再放回同一封裝。真正的
商業價值不只在介面速度，而在不同設計能否被製造、挑出良品、封裝、測試、修正錯誤，最後
由客戶長期使用。若把「最高速度的共同規則」、「某家介面設計送廠」與「較低速度的一次跨廠
展示」合成一句，就會太早把技術進展寫成可互換供應、量產訂單或公司收入。

### 接下來怎麼追

- 每次看到互通展示，先記錄傳輸率、實體路徑、協定功能、封裝、參與廠商、測試時間，以及是模擬還是實體晶片。
- 分開追最高速度回片、符合規格測試、跨廠實體互通、客戶資格驗證、量產產品與財務認列，不把不同產品的進度拼在一起。
- 對台灣公司只接受具名介面、封裝、載板或測試服務與客戶雙向核對，不用聯盟會員名單或一般先進封裝能力代替。

### 想一想

- 兩家測試晶片在一次展示中能交換資料，還要故意測哪些錯誤與長時間情境，才能證明它們真的能一起工作？
- 最高速度只有共同規則與送廠設計，較低速度已有實體互通時，研究者應如何避免把兩筆證據拼成同一項成果？
- 如果封裝裡所有小晶片都由同一家公司設計，即使使用開放介面，能否證明不同公司產品可以互換？

## 先用五個位置看小晶片如何在同一封裝裡接力

| 本文五個位置 | 它做什麼 | 代表元件或工作 | 下一個要驗收 | 不能直接推成 |
|---|---|---|---|---|
| 1. 執行功能的小晶片 | 分別負責運算、記憶體或輸入輸出，再產生要交換的資料 | 運算晶粒、記憶體晶粒、輸入輸出晶粒 | 每顆晶粒的功能、功耗與資料需求能對上 | 已能和任何公司的晶粒互換 |
| 2. 介面控制與傳輸協定 | 把資料、命令、流量、狀態與錯誤整理成兩端都能理解的格式 | 介面控制器、傳輸協定、旁帶與管理訊息 | 兩端在指定功能與錯誤情境使用同一套規則 | 實體訊號、封裝與長時間運作已通過 |
| 3. 實體傳輸電路與通道 | 把數位資料變成能跨越晶粒間距的電氣訊號，再在另一端收回 | 實體傳輸電路、傳輸通道、時鐘恢復 | 目標傳輸率、錯誤率與重新校準結果 | 完整協定或客戶產品已互通 |
| 4. 接點與封裝內布線 | 讓訊號、供電與接地真正跨過兩顆晶粒之間的實體路徑 | 微凸塊、接點、封裝布線、載板 | 損耗、干擾、對準、良率與可製造性 | 同一設計能直接換到另一種封裝 |
| 5. 封裝整體協調與測試 | 同時管理時鐘、供電、散熱、故障、測試與已知良品晶粒 | 封裝共同設計、溫度管理、系統級測試 | 長時間負載、錯誤注入、恢復與整包良率 | 已通過客戶資格驗證或穩定量產 |

這五個位置是本文的閱讀地圖，不是完整介面分層、固定接線順序或封裝配方。一次展示只有在
說清楚用了哪些晶粒、介面功能、實體路徑與測試條件後，才能知道它實際跨過哪幾個位置。

## 再用五把尺讀懂一次互通展示證明什麼

| 本文五把尺 | 每筆展示要記錄 | 本輪可看到的例子 | 下一份證據 | 不能直接推成 |
|---|---|---|---|---|
| 1. 傳輸率 | 每條通道在哪個速度運作，是否為目標版本最高速度 | 跨廠實體展示是 16，第三代規格與介面送廠設計談到 64 | 同一組實體晶片在 64 完成可重現量測 | 16 的互通自動替 64 畢業 |
| 2. 實體路徑 | 使用標準或先進封裝路徑、接點、布線與封裝型態 | 本輪跨廠展示明確屬標準封裝路徑 | 公開封裝、接點與兩端實體條件的 64 測試 | 一種封裝結果適用所有封裝 |
| 3. 協定與管理功能 | 資料傳輸、旁帶管理、錯誤回報、重新校準與所承載協定 | 本輪能確認具名連接與成功測試，沒有完整功能覆蓋矩陣 | 第三方公布逐項功能、錯誤與恢復結果 | 能送資料等於所有管理功能通過 |
| 4. 廠商獨立性與晶片狀態 | 是否由不同團隊獨立設計，以及是模擬、送廠、回片或實體展示 | 兩家獨立設計的測試晶片已有實體互通；64 只有規格與介面送廠 | 兩家以上獨立設計的 64 回片晶片互通 | 單一供應商自我測試等於跨廠互通 |
| 5. 封裝、時間與故障條件 | 封裝拓撲、運作時間、溫度、錯誤注入、恢復與失敗樣本 | 本輪來源沒有足以重算的長時間與故障測試分母 | 公開測試計畫、樣本、環境、失敗與重測結果 | 一次現場展示等於可靠度或量產良率 |

五把尺必須落在同一組實體產品上。若速度來自規格、晶片狀態來自送廠聲明、跨廠互通來自
另一組較低速度測試，就只能得到三筆各自有邊界的證據，不能拼成一項最高速度成果。

## 把五種證據物件分開，不讓它們斜著畢業

| 本文五種證據物件 | 白話意思 | 本輪可確認 | 下一份證據 | 不能借用 |
|---|---|---|---|---|
| 1. 共同規格 | 多家參與者先約定介面、速度、管理與測試要求 | 第三代規格已定義 48／64 與管理功能 | 正式測試計畫與具名 64 結果 | 不能借用任何產品名稱當成實體通過 |
| 2. 介面智財與設計工具 | 設計者可以取得控制器、實體電路與驗證流程 | 有供應商公開 64 介面與工具鏈 | 另一獨立實作與共同測試條件 | 不能借用規格存在當成每家設計都相容 |
| 3. 送廠設計與回片 | 送廠表示設計交付製造，回片才有實體晶片可量測；兩者仍是不同節點 | 本輪可確認 64 介面設計送廠，未確認同一設計回片實測 | 具名回片、實測速度、錯誤率與失敗紀錄 | 不能借用送廠聲明當成實體測試成功 |
| 4. 測試晶片互通展示 | 兩家獨立晶片在特定封裝與條件完成指定工作 | 16 標準封裝路徑已有具名跨廠實體展示 | 同一產品組合的完整功能、故障與長時間結果 | 不能借用較低速度展示替最高速度通過 |
| 5. 客戶量產產品 | 客戶把多顆晶片做成具名產品，通過資格驗證並持續交付 | 本輪沒有可核對的 64 多廠客戶產品 | 客戶、晶片、封裝、資格與量產的雙向揭露 | 不能借用展示、會員資格或一般封裝能力當成訂單 |

證據可以並行出現，卻不能沿著不同產品「斜著畢業」。研究結論必須跟著同一個版本、同一組
晶片、同一種封裝與同一份測試條件前進；其中任何一項換了對象，就要重新標示邊界。

## 把六類角色放回同一個小晶片產品

| 本文六類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 規格聯盟與測試規則 | 共同介面版本、速度、管理功能與符合規格測試入口 | UCIe Consortium | 第三代共同規格與既有互通展示紀錄可查 | 聯盟發布規格不等於所有會員已有產品 |
| 2. 介面智財與設計工具 | 控制器、實體傳輸電路、模擬與驗證流程 | Synopsys | 公開 64 介面送廠與工具鏈聲明 | 供應商自述不等於回片、第三方測試或客戶收入 |
| 3. 小晶片設計者 | 各自設計能執行功能並接上共同介面的實體晶片 | Intel、Cadence | 兩家獨立測試晶片完成指定 16 跨廠展示 | 一組測試晶片不代表所有協定、速度與供應商可互換 |
| 4. 晶圓製造 | 把送廠設計製造成實體晶片，建立製程與良率條件 | 本輪只看到介面供應商揭露製程節點 | 可確認送廠聲明，沒有可重算的回片與良率結果 | 製程節點不等於介面在目標速度通過 |
| 5. 封裝、載板與測試服務 | 組裝晶粒、安排接點與布線、挑出良品並驗證整包 | 本輪未具名封裝測試服務商 | 技術角色可辨認，尚無具名 64 客戶服務 | 技術必要性不等於特定公司取得訂單或毛利 |
| 6. 客戶產品與台灣財務查證 | 定義實際工作、資格驗證、量產分母，再與供應商揭露互相核對 | 本輪沒有具名 64 多廠客戶產品 | 仍是待驗證路由 | 客戶規劃、會員名單或公司能力不等於可辨識收入 |

六類角色是責任分工，不是固定供應商名單，也不是受惠排序。只有客戶與供應商能對同一個
介面版本、晶片、封裝、測試服務與量產期間雙向核對，才適合把產業關係接到公司財務。

## 最後用六關判斷「能互通」到「生態系成熟」

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 共同規格與測試合約可查 | 版本、速度、實體路徑、功能與測試方法有共同文件 | 已有第三代規格與測試入口 | 具名 64 測試計畫、條件與判定方式 | 有共同語言不等於已有實體產品 |
| 2. 介面實作完成並送廠 | 控制器、實體電路與驗證流程已整合成可製造設計 | 有供應商公開 64 介面送廠 | 回片日期、晶片狀態與首輪實測 | 送廠不等於回片或測試通過 |
| 3. 實體晶片在目標速度運作 | 回片晶片在同一速度、封裝與功能條件穩定收發 | 本輪 16 有實體測試晶片，64 尚未由同一證據確認 | 64 回片、錯誤率、溫度與長時間結果 | 較低速度結果不等於最高速度通過 |
| 4. 跨廠互通與正式測試對齊 | 兩家以上獨立晶片在相同條件互通，並有共同或第三方判定 | 特定 16 組合已有跨廠展示，64 正式結果未確認 | 64 多廠測試矩陣、符合規格結果與失敗樣本 | 一次展示不等於整個供應生態可互換 |
| 5. 客戶產品通過資格並量產 | 具名產品完成可靠度、良率、供應與實際工作驗收 | 本輪沒有可核對的 64 多廠客戶產品 | 客戶產品、封裝、資格、產量與持續交付 | 測試晶片或參考設計不等於量產產品 |
| 6. 台灣公司財務足跡可雙向核對 | 同一產品的服務、出貨、收入、毛利或現金流能由兩端確認 | 本輪只有矽智財、封測與載板搜尋路由 | 客戶與供應商對具名產品及財務期間共同揭露 | 產業必要性不等於公司已受惠 |

本輪不是「完全沒有進展」：共同規格、64 介面送廠與 16 跨廠實體展示都各自成立。真正的
邊界是三者尚未落在同一組 64 實體產品，因此不能把第四關以前的分散證據寫成第五或第六關。

## 這篇對公司判斷的用處與界線

| 看到公開訊息 | 可以先做 | 還不能做 |
|---|---|---|
| 公司加入聯盟或宣布支援共同介面 | 放入規格、介面智財或製造角色的候選清單 | 直接寫成具名訂單、跨廠互通或收入 |
| 介面設計完成送廠 | 追蹤回片、目標速度與第三方測試日期 | 把送廠當成實體晶片成功或客戶量產 |
| 兩家測試晶片完成展示 | 記錄速度、封裝、協定、測試時間與故障條件 | 外推到最高速度、所有廠商或長期可靠度 |
| 客戶開始資格驗證或量產 | 對齊具名晶片、封裝、測試服務、數量與期間 | 只憑單方宣稱估算供應商收入或毛利 |
| 台灣公司法說提到小晶片或先進封裝 | 查找同一具名產品、客戶與可歸因財務分母 | 用題材關鍵字、會員名單或一般能力做投資排序 |

因此，本文把矽智財、封測與載板保留為研究入口，而不是受惠名單。下一次更新若仍只有新規格、
單一供應商自我測試或未具名客戶規劃，就只能更新相應節點，不能把整條生態系一起升級。

## 來源與證據邊界

- [UCIe 3.0 規格發布](https://www.uciexpress.org/_files/ugd/8dc731_ae67289d0ec646cdba5c1aee245538b3.pdf)（第三代最高傳輸率與管理功能）。
- [2026 小晶片高峰會互通展示](https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem)（Intel／Cadence 的 16 跨廠實體互通）。
- [Synopsys 64 介面智財送廠說明](https://www.synopsys.com/blogs/chip-design/64g-ucie-ip-high-speed-die-to-die-connectivity.html)（送廠製造節點）。
- [Synopsys 第三代介面方案更新](https://www.synopsys.com/blogs/chip-design/ucie-3-0-chiplet-ip-solutions.html)（實體傳輸電路、控制器與驗證流程）。
- [UCIe 規格持續更新入口](https://www.uciexpress.org/specifications)（後續版本與符合規格測試入口）。
- [Synopsys UCIe 介面持續更新入口](https://www.synopsys.com/designware-ip/interface-ip/die-to-die/ucie.html)（後續回片與互通消息入口）。

本文不把不同速度、封裝或測試型態當成同一指標，也不使用會員數、宣稱市場規模或公司效能
數字做跨公司比較。規格聯盟對展示的敘述與介面供應商對自身產品的敘述都屬參與者一手資料，
仍需要未來符合規格測試與客戶產品形成獨立驗證。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: UCIe 會形成 PHY、controller、verification、retimer 與 chiplet 管理 IP 的搜尋入口，但本輪只有外部 IP 供應商證據
evidence_boundary: universe 公司具高速介面能力或加入生態系，不等於已有 UCIe 3.0 64G silicon、design win 或收入
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: Multi-vendor chiplet 需要 known-good-die、封裝整合、compliance 與系統級測試，形成封測研究路由
evidence_boundary: 技術必要性不證明任何 OSAT 已承接具名 64G UCIe 產品、量產或取得財務貢獻
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: 標準封裝、先進封裝與更高資料率會改變 substrate routing、signal integrity 與材料要求
evidence_boundary: UCIe 介面與封裝需求不自動對應任一台灣載板／PCB 公司訂單、份額、良率或毛利
-->

## 下一個可證明／否定的節點

- 64G test silicon 回片後，由第三方公布 electrical compliance 與長時間運作結果。
- 兩家以上獨立 chiplet 在同一實體 package 以 64G 完成可重現互通，並公開 protocol 與封裝範圍。
- 具名客戶把 UCIe multi-vendor chiplet 放進 qualification／production，而不只是 internal captive design。
- 台灣公司與客戶對同一具名 IP、封裝、substrate 或測試服務完成雙向核對；否則只保留族群搜尋線。
