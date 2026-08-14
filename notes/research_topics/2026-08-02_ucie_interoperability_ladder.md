# UCIe 讓小晶片共用語言，但一次互通不代表生態系成熟：先分清設計、實體測試與客戶產品

<!-- research_topic
topic_id: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-03-05
last_reviewed_at: 2026-08-12
review_due: 2026-08-17
source_type: mixed
publisher: UCIe Consortium
publisher_domain: uciexpress.org
canonical_url: https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem
source_chain_id: ucie-spec-silicon-interop-20260802
stock_ids: 3443
group_ids: ipdesign,packtest,pcb
trigger_type: standard_to_silicon_interoperability
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C9
base_confidence: medium
confidence_basis: UCIe Consortium 的 16G 跨廠展示、創意 32G 實體晶片與 64G 驗證時程，以及創意／Cadence／Synopsys 各自的 64G tape-out 可建立具名一手證據鏈；但這些證據分屬不同速度、設計與測試包絡，尚不能證明同一組 64G UCIe 3.0 晶片已完成跨廠 compliance、客戶量產或台灣公司財務貢獻
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

<!-- research_source
source_id: S7
role: company_release
source_kind: document
publisher: Global Unichip Corp.
title: GUC Announces Successful Launch of Industry's First 32G UCIe Silicon on TSMC 3nm and CoWoS Technology
published_at: 2025-03-13
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.guc-asic.com/en/news/PressRelease/PR_ENG_20240313
locator: 32G UCIe 2.0 PHY silicon、N3P／CoWoS、several dies、silicon measurements 與 full-corner qualification 段落
limitation: 創意自述可證實其 test chip 已有 32Gbps 實體量測，但沒有列出獨立供應商 chiplet、共同 compliance 判定、完整 full-corner 報告、客戶產品或 UCIe 專屬收入
independence_group: guc
-->

<!-- research_source
source_id: S8
role: company_release
source_kind: document
publisher: Global Unichip Corp.
title: GUC Announces Tape-out of UCIe 64G IP on TSMC N3P Technology
published_at: 2026-02-26
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.guc-asic.com/en/news/all/PR_20260226
locator: 64 Gbps per lane、UCIe 3.0、TSMC N3P／CoWoS 與 AXI／CXS／CHI bridge 段落
limitation: 新聞稿證實的是設計送廠與宣稱功能，不是 64G 回片量測、第三方 compliance、跨廠 chiplet 互通、客戶 qualification 或收入
independence_group: guc
-->

<!-- research_source
source_id: S9
role: company_filing
source_kind: document
publisher: Global Unichip Corp.
title: Global Unichip Corp. 2025 Annual Report
published_at: 2026-04-16
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.guc-asic.com/upload/2026_04_16/8_202604161551145dnuwxrHk5.pdf
locator: PDF page 3 lines 171–178；page 61 lines 6129–6158 的 UCIe test-chip tape-out 與 silicon verification schedule
limitation: 年報列的是不同版本、製程與測試晶片的公司時程；不能把 3nm UCIe 1.0、5nm UCIe LP 32G 與 3nm／2nm UCIe 64G 合併成同一產品，也沒有 UCIe 專屬收入分母或跨廠結果
independence_group: guc
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: document
publisher: Cadence
title: Cadence Tapes Out UCIe IP Solution at 64G Speeds on TSMC N3P Technology
published_at: 2025-12-17
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/cadence-tapes-out-ucie-ip-solution-at-64g-speeds-on-tsmc-n3p-technology
locator: 64Gbps UCIe IP subsystem、TSMC N3P、supported protocols 與 third-generation tapeout 段落
limitation: Cadence 自述的 tape-out、compliant 與 designed for interoperability 不等於該 64G test chip 已回片、由共同測試機構通過或和另一供應商的實體 chiplet 互通
independence_group: cadence
-->

<!-- research_source
source_id: S11
role: company_release
source_kind: living_index
publisher: Global Unichip Corp.
title: GUC Press Release
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.guc-asic.com/en/news/PressRelease
locator: 2026-08-12 查得創意新聞稿清單與最新 UCIe／高速介面更新入口
limitation: 活頁索引只用來偵測公司後續回片與驗證公告；沒有新公告不能單獨證明里程碑延後或失敗
independence_group: guc
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: UCIe Consortium
title: Introduction to UCIe Webinar: Q&A Recap
published_at: 2023-05-03
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.uciexpress.org/post/introduction-to-ucie-webinar-q-a-recap
locator: Physical Questions 的 x16／direction 單位更正、module-width overhead、spare／clock／track／valid／sideband；Compliance Testing 與 Miscellaneous 的 CRC／retry／retrain、latency、link-parameter negotiation 與 68B／256B flit 說明
limitation: 這是 2023 年針對 UCIe 1.0 的聯盟問答，可用來固定單位、方向與 overhead 邊界；不是 UCIe 3.0 64G 產品測試，也沒有具名 device、run、payload goodput、功耗、長時間錯誤或客戶結果
independence_group: ucie-consortium
-->

<!-- research_source
source_id: S13
role: standard
source_kind: document
publisher: UCIe Consortium
title: UCIe 1.1 Provides Streaming Protocol Solution for Error Detection and Replay
published_at: 2023-08-28
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.uciexpress.org/post/ucie-1-1-provides-streaming-protocol-solution-for-error-detection-and-replay
locator: Raw Mode、streaming flit negotiation、236／250-byte CHI payload，以及 D2D adapter 插入 flit header／CRC 並執行 CRC detection／replay 的段落
limitation: 文件說明 UCIe 1.1 streaming reliability 與特定 CHI packed-flit payload，不提供 UCIe 3.0 64G 實測 goodput、所有 protocol 的共同效率、延遲分布、錯誤事件分母或客戶 interoperability
independence_group: ucie-consortium
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

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: 創意於 2025-03-13 公開 32G UCIe 2.0 test chip 的 N3P／CoWoS 實體量測，多顆 die 經 interposer 連接並量到 32Gbps；該頁同時說 full-corner qualification 仍在進行
supporting_source_ids: S7
contrary_source_ids:
as_of: 2025-03-13
basis: S7 直接列出版本、製程／封裝、多顆 die、silicon measurement 與尚待完成的 full-corner qualification
boundary: 這是創意自身 test vehicle 的實體晶片證據；來源沒有說晶粒由不同供應商獨立設計，也沒有共同 compliance、客戶 qualification、量產良率或收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: 創意 2025 年報把不同 UCIe IP 的 tape-out 與 silicon verification 分列；其中 3nm UCIe 64G 已於 2025 年第 4 季送廠，實體晶片驗證排在 2027 年第 1 季
supporting_source_ids: S8,S9
contrary_source_ids:
as_of: 2026-04-16
basis: S8 確認 N3P／CoWoS 64G UCIe 3.0 tape-out，S9 page 3 與 page 61 重複列出 3nm 64G tape-out 和 2027Q1 silicon verification schedule
boundary: 時程是公司前瞻且可能改變；截至該年報不能把 64G 寫成 silicon-proven。年報另列 3nm UCIe 1.0 與 5nm LP 32G，不得和 S7 的 N3P UCIe 2.0 自動視為同一 test chip
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
claim: 創意、Cadence 與 Synopsys 都已各自公開 64G UCIe IP tape-out，但三份公告屬三個分開的供應商 test vehicle，不能合併成一次 multi-vendor interoperability result
supporting_source_ids: S3,S8,S10
contrary_source_ids:
as_of: 2026-06-30
basis: S3、S8、S10 各自直接宣告其 64G IP tape-out；沒有任一來源說三顆晶片曾放進同一封裝或依共同測試計畫互通
boundary: 多家各自送廠提高可追蹤的實作者數量，但不證明回片、共同 compliance、跨廠互換、客戶產品或台灣公司財務貢獻
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
claim: UCIe 成熟度不能只畫一條速度階梯；至少要同時對齊「證據物件階段」「測試包絡」「供應商獨立性」三軸，因為 16G 跨廠展示、32G 單一供應商實體晶片與 64G 多家各自 tape-out 分別只跨過不同軸
supporting_source_ids: S1,S2,S3,S7,S8,S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S2 提供 16G multi-vendor live demo，S7 提供 32G single-vendor silicon measurement，S3／S8／S10 提供三家分開的 64G tape-out，S9 又把 64G 回片驗證列為未來節點
boundary: 三軸框架用來防止把不同 test vehicle 斜著拼接；不據此預測 UCIe 市占、chiplet marketplace、客戶採用速度、公司營收或估值
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: 64G UCIe 3.0 已讓兩家以上獨立供應商 chiplet 在同一實體封裝完成公開 compliance 與錯誤測試，並進入具名客戶量產或形成創意可辨識的 UCIe 收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 本輪能定位 64G 規格與三家各自 tape-out，也能定位 16G 跨廠及 32G 單一供應商實體證據，但沒有同版、同速、同封裝、多廠、共同測項與客戶／財務橋接
boundary: 本輪核對的是指定官方來源，不是所有聯盟會員、客戶或未公開專案的完整普查；「沒有在已查來源找到」不等於證明市場上不存在
verification_needed: 需公開 64G chiplet 身分、版本、封裝、protocol／manageability、錯誤與長時間測試、通過／失敗結果、客戶 qualification，以及 UCIe 專屬財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: UCIe Consortium 的官方問答明確更正 Gb/s 與 GB/s，並把 x16@4G 寫成 64 Gb/s／direction＝8 GB/s／direction、把 x16@32G 列為 64 GB/s／direction 的一種配置；同頁也說 module width 必須和 clocking、valid、track、sideband overhead 及 lane-to-lane skew 一起讀
supporting_source_ids: S12
contrary_source_ids:
as_of: 2023-05-03
basis: S12 Physical Questions 直接列單位更正、兩個 x16 方向性算例，以及 width／overhead／skew 的取捨
boundary: 這些是聯盟對資料通道單位與模組配置的說明，不是 payload goodput、雙向可互換容量、具名產品量測、64G silicon、延遲、功耗、錯誤率或 compliance result
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
claim: UCIe 1.1 的 streaming flit 會在初始化時協商，CHI packed flit 可提供 236 或 250 bytes payload，D2D adapter 另插入 flit header 與 CRC 並支援 detection／replay；UCIe 問答也把 sideband、spare lane、clock／track／valid、replay、retrain 與 protocol path 分開
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2023-08-28
basis: S13 直接列 payload bytes、header、CRC 與 replay，S12 直接列 physical auxiliary signals、spares、replay／retrain 與 transaction path 邊界
boundary: 只證實不同層存在不同 overhead 與恢復責任，不代表所有模式都固定損失同一百分比，也不能由 236／250 bytes 外推 UCIe 3.0 所有 protocol、實際 traffic mix、payload goodput 或服務效能
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 在「每個資料 lane 每次 transfer 承載一個 data bit、x16 指 16 條 data lanes、只算單一方向且尚未扣除任何協定與運作損失」的教材條件下，x16@64 GT/s 的資料通道算術是 64×16÷8＝128 GB/s／direction；兩方向同時相加可寫成 256 GB/s aggregate，但不能把 256 GB/s 當成單向 payload
supporting_source_ids: S1,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S1 確認 64 GT/s 規格率，S12 的 x16@4G＝8 GB/s／direction 與 x16@32G＝64 GB/s／direction 提供同一換算路徑；Python Fraction 與獨立 awk 均重算得 128 與 256
boundary: 這是 N=1 個假想 x16@64G link configuration 的確定性單位展開，沒有 device、module、run 或抽樣，故沒有 sampling SE／t；未扣 flit／protocol／CRC／replay／idle／throttle／retrain，也沒有 latency、energy、BER、corner、interoperability 或 application result
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
claim: UCIe 效能與互通不能由最高 GT/s 單欄驗收；至少要把版本／封裝路徑、lane／module／direction、raw 算式、flit／protocol／payload、error／replay／retrain、workload／traffic、latency／energy／corner、兩端晶片與測試機構、客戶 qualification 及財務分母綁成同一份 link-performance passport
supporting_source_ids: S1,S2,S7,S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: S1 只定義最高規格與 package options，S12／S13 把 direction、auxiliary signals、payload、CRC、replay 與 latency 拆層，S2／S7 又顯示跨廠 demo 與單一供應商 silicon measurement 是不同證據物件
boundary: 護照是研究中心整合標準、官方問答與既有 silicon／demo 證據的查核框架，不是 Consortium compliance template；欄位完整仍不保證 pass、量產、多廠可互換、低成本、低功耗、台灣公司收入或投資報酬
verification_needed: 同一具名 64G UCIe 3.0 multi-vendor package 的版本、module／lane／direction、protocol／flit、payload workload、error／replay／retrain、latency／energy／corner／duration、通過與失敗結果、客戶 qualification 與供應商財務共同鍵
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6,C7,C9,C10
metric: 創意各 UCIe 版本／製程／test chip 身分、32G full-corner 結果與 64G silicon verification 進度
source_ids: S7,S8,S9
watch_source_ids: S11
frequency: quarterly
frequency_detail: 每季查創意新聞稿、年報與法說，逐一核對版本、製程、封裝、tape-out、silicon-proven 與客戶／財務節點
next_check: 2026-10-15
trigger: 創意公布具名 64G 回片與 full-corner／protocol 測試結果，或把同一 IP 接到客戶 qualification 與可歸因財務分母
invalidation: 公司正式延後 64G 2027Q1 驗證時程、只公布另一顆不同版本 test chip，或結果缺少版本、測試條件與失敗邊界
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

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_taiwan_32g_silicon_and_64g_tapeout_schedule_without_promoting_64g_interoperability
evidence: sources:S7,S8,S9,S10
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_ucie_transfer_raw_direction_payload_and_interoperability_performance_contract_without_thesis_or_clock_refresh
evidence: sources:S1,S12,S13
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **小晶片（chiplet）**：把原本一大顆晶片拆成多顆各司其職的小晶粒，再放進同一封裝共同運作。
- **晶粒（die）**：從一片晶圓切下、尚未封裝的單顆半導體；一個封裝裡可以放入一顆或多顆晶粒。
- **封裝（package）**：把晶粒、接點、布線、供電與散熱結合成可裝進系統的元件，不只是外面的保護殼。
- **三奈米加強版製程（N3P）**：台積電三奈米製程家族中的一個版本；製程名稱只說明製造路徑，不代表介面已通過目標速度。
- **晶圓上晶片封裝（CoWoS）**：用中介層或其他高密度路徑把多顆晶片整合在同一先進封裝；使用此封裝不等於多家晶片已互通。
- **晶粒對晶粒連線（die-to-die）**：讓同一封裝內的晶粒直接交換資料與管理訊息的短距離連線。
- **通用小晶片互連（UCIe）**：為封裝內小晶片定義電氣、協定、管理與測試共同規則的開放介面。
- **介面控制器（controller）**：整理要傳送的資料、命令、流量與錯誤處理，再交給實體傳輸電路。
- **實體傳輸電路（PHY）**：把數位資料轉成晶粒間可傳送與接收的電氣訊號；有實體電路不等於完整協定已互通。
- **傳輸通道（lane）**：實體介面中並行傳送資料的一條路；速度、通道數與封裝布線要一起核對。
- **標準／先進封裝路徑（UCIe-S／UCIe-A）**：分別面向較傳統與更高密度封裝的實體連接方式，兩者不能共用同一筆測試結論。
- **每秒十億次傳輸（GT/s）**：介面每秒可完成的傳輸次數；它是傳輸率，不是單顆產品的產量、收入或成熟度。
- **十六條資料通道（x16）**：在指定 module 定義下並行使用 16 條 data lanes；它不是 16 GB，也不是 16 顆晶片，仍要另寫每 lane 速率與方向。
- **原始資料通道算術（raw data-lane arithmetic）**：依傳輸率、資料通道數與方向換算的條件式理論 bytes／s，尚未扣除 framing、協定、錯誤恢復、閒置或應用等待。
- **循環冗餘檢查（CRC）**：接收端用來偵測資料傳送錯誤的檢查碼；偵測到錯誤後是否重送、重訓或失敗，要由另一組 counter 與規則判讀。
- **16、32 與 64 的差別**：本文的 16 是跨廠展示速度，32 是單一供應商實體晶片量測速度，64 是第三代最高傳輸率與各家送廠目標；三筆證據不是同一組產品。
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
- **實體晶片驗證（silicon-proven）**：回片後在公司定義的範圍完成量測；要判斷證據強弱，仍須知道版本、速度、封裝、測項與失敗結果。
- **完整工況驗證（full-corner qualification）**：在不同製程、電壓與溫度等邊界條件下檢查晶片；宣布正在驗證不等於已公開完整通過報告。
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
- 現在有三種錯開的進展：十六有跨廠展示、三十二有單一供應商實體驗證、六十四有多家各自送廠；它們還不能拼成同一項最高速度成果。

### 為什麼重要

小晶片讓設計者有機會把運算、記憶體與輸入輸出等功能分開製造，再放回同一封裝。真正的
商業價值不只在介面速度，而在不同設計能否被製造、挑出良品、封裝、測試、修正錯誤，最後
由客戶長期使用。若把「最高速度的共同規則」、「某家介面設計送廠」與「較低速度的一次跨廠
展示」合成一句，就會太早把技術進展寫成可互換供應、量產訂單或公司收入。

### 接下來怎麼追

- 每次看到互通展示，先記錄版本、傳輸率、製程、實體路徑、協定功能、封裝、參與廠商、測試時間，以及是模擬、送廠還是實體晶片。
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
| 1. 傳輸率 | 每條通道在哪個速度運作，是否為目標版本最高速度 | 跨廠實體展示是 16，創意實體量測是 32，第三代規格與三家送廠設計談到 64 | 同一組實體晶片在 64 完成可重現量測 | 16 或 32 的進度自動替 64 畢業 |
| 2. 實體路徑 | 使用標準或先進封裝路徑、接點、布線與封裝型態 | 16 跨廠展示屬標準封裝路徑；創意 32 與 64 來源列出 CoWoS，但不是同一 test vehicle | 公開封裝、接點與兩端實體條件的 64 測試 | 一種封裝或另一顆晶片的結果適用所有封裝 |
| 3. 協定與管理功能 | 資料傳輸、旁帶管理、錯誤回報、重新校準與所承載協定 | 本輪能確認具名連接與成功測試，沒有完整功能覆蓋矩陣 | 第三方公布逐項功能、錯誤與恢復結果 | 能送資料等於所有管理功能通過 |
| 4. 廠商獨立性與晶片狀態 | 是否由不同團隊獨立設計，以及是模擬、送廠、回片或實體展示 | 16 有兩家獨立 test chip；32 有創意自身實體晶片；64 有三家各自送廠 | 兩家以上獨立設計的 64 回片晶片互通 | 多顆同公司 die 或多家各自 tape-out 等於跨廠互通 |
| 5. 封裝、時間與故障條件 | 封裝拓撲、運作時間、溫度、錯誤注入、恢復與失敗樣本 | 創意 32 公告明說 full-corner 尚在進行；其餘來源也沒有足以重算的長時間與失敗分母 | 公開測試計畫、樣本、環境、失敗與重測結果 | 一次量測或現場展示等於可靠度或量產良率 |

五把尺必須落在同一組實體產品上。若速度來自規格、晶片狀態來自送廠聲明、跨廠互通來自
另一組較低速度測試，就只能得到三筆各自有邊界的證據，不能拼成一項最高速度成果。

## 先把 64 GT/s、128 GB/s、256 GB/s 與 payload 分開

看到「64」時，第一個問題不該是「比上一代快幾倍」，而是「這個 64 的量、寬度、方向與
資料層是什麼」。GT/s 是每秒傳輸次數的速率口徑；GB/s 是每秒 bytes；payload goodput 則是
工作真正收到、可用的有效資料。三者之間必須先補 lane 數與方向，後面還有 framing、CRC、
重送、閒置和上層協定，不能把同一個數字換單位後就宣稱應用程式已經拿到。

| 數字層 | 它回答什麼 | 必須一起保存 | 最常見的誤讀 |
|---|---|---|---|
| 每 lane 傳輸率 | 一條資料 lane 每秒有多少次 transfer | 規格版本、UCIe-S／UCIe-A、lane 定義 | 把 GT/s 直接寫成 GB/s |
| 單向資料通道算術 | 指定 data-lane width 在一個方向的理論 bytes／s | rate、data lanes、每次 transfer 的 data bits、direction | 沒寫 x16 還是 x64，就比較「頻寬」 |
| 雙向 aggregate | 兩個方向同時各自運作時的數字加總 | 每一方向各自的分母與 traffic | 把兩向相加值當成任一方向都能使用 |
| payload goodput | 工作在指定時間內真正完成的有效 bytes | protocol／flit、payload 定義、workload、時間、error／replay／idle | 把 raw 算術當成應用吞吐量 |

聯盟問答先提供兩個很好的單位錨：x16@4G 是 64 Gb/s／direction，也就是 8 GB/s／direction；
x16@32G 則是 64 GB/s／direction 的一種配置。沿用相同的條件式資料通道算式：

> 單向資料通道算術＝每 lane GT/s × data-lane 數 × 每次 transfer 的 data bits ÷ 8。

若教材假設每條 data lane 每次 transfer 承載 1 bit，x16@64 GT/s 就是
64×16÷8＝128 GB/s／direction；只有在兩個方向同時各跑到該算術值時，才可把兩向相加成
256 GB/s aggregate。256 不能回頭冒充 256 GB/s 單向，更不能直接冒充 256 GB/s payload。

| 教材配置 | 算式 | 可以說 | 不能說 |
|---|---:|---|---|
| x16@4 GT/s | 4×16÷8＝8 GB/s／direction | 與聯盟問答的單向單位例相符 | 某產品已交付 8 GB/s payload |
| x16@32 GT/s | 32×16÷8＝64 GB/s／direction | 與聯盟問答列出的 x16 配置相符 | 所有封裝、協定與工作都得到 64 GB/s |
| 假想 x16@64 GT/s | 64×16÷8＝128 GB/s／direction | 在明列假設下的 raw data-lane 算術 | 64G silicon、compliance 或有效吞吐已通過 |
| 假想 x16@64 GT/s 兩向相加 | 128×2＝256 GB/s aggregate | 兩個方向的會計加總 | 單向工作能讀或寫 256 GB/s |

128 與 256 已用 Python `Fraction` 及獨立 `awk` 兩條路徑重算一致。這是 N=1 個假想
x16@64G link configuration 的確定性單位展開，不是裝置、模組、測試 run 或抽樣，因此沒有
sampling SE／t，也不是一筆效能比較。4G 與 32G 是官方問答的參照例，不是新增產品樣本。

### Raw 之後還有五層，不能只套一個固定效率

| 從 raw 到工作結果的層 | 會加入什麼責任 | 本輪官方證據 | 讀者應該索取 |
|---|---|---|---|
| 1. 實體 module | data lanes 之外還有 clock、valid、track、sideband 與 spare；寬度越大也增加 clock distribution 與 lane-to-lane skew 挑戰 | 聯盟問答列出 x16 的 overhead 取捨，advanced package 每 32 data lanes 有 2 spare lanes，clock／track／valid 另有 spare | bump map、module 數、data／auxiliary／spare lane mapping、封裝路徑 |
| 2. Link framing 與可靠度 | header、Ack／Nak、CRC、偵測、重送與重新訓練都不是使用者資料 | 聯盟文件列出 D2D adapter 插入 header／CRC、執行 detection／replay；問答也說 replay／retrain 會擾動延遲 | flit type、header／CRC 定義、error counters、replay bytes／events、retrain 與降速紀錄 |
| 3. Protocol 與 payload | Raw Mode、streaming、PCIe、CXL 或其他映射的資料單元與有效內容不同 | UCIe 1.1 streaming flit 在初始化協商；特定 CHI packed flit 提供 236 或 250 bytes payload | protocol、flit format、message mix、payload numerator 與 wire／raw denominator |
| 4. 運作狀態 | 閒置、流量不對稱、throttle、校準、backpressure、錯誤恢復與溫度會改變完成量 | UCIe 3.0 提供 runtime recalibration、power-state 與 manageability 能力，但發布稿沒有具名產品 raw counters | busy／idle 時間、單向／雙向 traffic、duration、temperature／voltage corners、power／energy |
| 5. 應用服務 | 一筆 memory／coherency transaction 還會走出介面，等待 endpoint、software 與資料 | 聯盟問答明說 transaction latency 超出單一 interconnect 規格範圍，且 replay／retrain 會影響可重複性 | workload、完整 path、latency distribution、tail、完成／失敗與使用者結果 |

所以不能看到「236 bytes」就替所有 UCIe traffic 套 236／某個固定分母，也不能看到 CRC／replay
就自訂一個全產品通用折扣。不同 protocol、flit、錯誤情境與 traffic mix 的 payload 分子都不同；
真正可比較的是同一個護照下的原始 counter、公式與工作結果。

### 十欄 link-performance passport

| 護照欄位 | 最低要寫什麼 | 缺欄時最多能說什麼 |
|---|---|---|
| 1. 物件與版本 | 兩端 chiplet／revision、UCIe version、test vehicle 或 customer product | 只能說規格或設計存在 |
| 2. 實體路徑 | UCIe-S／UCIe-A、package、bump／channel、process／voltage／temperature | 不能把結果外推到另一封裝 |
| 3. Lane 與方向 | data／auxiliary／spare lanes、module 數、rate、單向或雙向 | 不能重算 GB/s，也不能比較 aggregate |
| 4. Raw 參考平面 | bits／transfer、公式、量測或理論、counter 所在層 | 只能保留 GT/s 規格值 |
| 5. Protocol 與 payload | protocol、flit／header／CRC、payload 定義、message／read-write mix | 不能把 raw 寫成 goodput |
| 6. 錯誤與恢復 | exposed bits／flits／time、raw／detected／residual errors、replay、retrain、降速、失敗 | 「零錯誤」沒有事件與暴露分母就不可比較 |
| 7. Workload 與流量 | message size、concurrency、directionality、busy／idle、backpressure、duration | 只能說特定 link 曾運作 |
| 8. 服務與資源 | throughput、latency distribution／tail、power／energy、thermal／corner、repeat runs | 不能宣稱系統效能或效率 |
| 9. 互通與判定 | 兩端是否獨立供應商、test authority、plan／version、pass／fail／retest matrix | 單一 loopback 或展示不等於多廠 compliance |
| 10. 客戶與財務 | qualification、production quantity／period、shipment、可歸因收入／成本分母與兩端核對 | 不能把技術必要性寫成公司受惠 |

這張護照把「快」和「能一起工作」放進同一份紀錄：只有速度而沒有兩端身分，是介面能力；
只有兩端互通而沒有 payload、錯誤、延遲與條件，是受限展示；只有客戶名稱而沒有 qualification
與財務共同鍵，仍不是可歸因營收。

### 多空小作文：兩邊都必須交同一份成績單

| 敘事 | 可以成立的產業機制 | 會證成它的下一份資料 | 會使它失效或降級的資料 |
|---|---|---|---|
| 偏多 | 每 lane 速率提高後，同樣封裝 shoreline 可承載更多資料，或以較少 module 完成既定目標；開放介面也可能增加 PHY／controller／verification、封裝共同設計與 system-level test 內容 | 同一 64G multi-vendor package 在固定 workload 下，比 32G baseline 提高單向 payload／area，同時守住 latency tail、energy、error／replay、corner 與長時間結果；再接上客戶 qualification、量產與可歸因財務 | 只有規格、simulation 或各家分開 tape-out；payload、功耗、錯誤、良率或 qualification 沒有共同分母 |
| 偏空 | 更高資料率可能把難度轉成 clock／skew、signal integrity、power、thermal、replay、known-good-die 與封裝測試；客戶也可能只在自有 captive chiplet 內使用共同介面，沒有可交易多廠市場 | 同一具名 64G product 顯示 raw 增幅被 idle／replay／throttle／latency／energy／yield 吃掉，multi-vendor matrix 長期空白，或客戶退回較低速／專有介面 | 多家獨立晶片在共同測試與客戶工作中持續通過，失敗／重測也公開，且 production 與財務共同鍵可核對 |
| 共同裁決 | 最高 GT/s 不是裁判，固定的 link-performance passport 才是 | 同版本、同 package、同 lanes／direction、同 protocol／payload、同 workload、同 error／latency／energy／corner、同跨廠與客戶分母 | 任何一邊只換標題、換分母、把雙向加總冒充單向，或把 raw 冒充 payload |

因此，64 GT/s 對矽智財、先進封裝與測試可能是需求起點，卻不是受惠結論。讀者真正要追的是
128 的單向 raw 算式能否在同一顆實體產品上，依序轉成可重建 payload、可靠度、服務表現、
跨廠 qualification 與財務；其中任何一層換了晶片、封裝、方向或 workload，就要重新開始對齊。

## 先不要只畫一條階梯：三條軸要同時對齊

| 三條判讀軸 | 要回答的問題 | 可前進的證據 | 常見誤讀 |
|---|---|---|---|
| 1. 證據物件階段 | 這筆資料是規格、模擬、送廠、回片量測、符合規格測試、客戶資格，還是財務認列？ | 同一顆具名晶片沿時間留下可核對的前後節點 | 把「設計可製造」寫成「實體已通過」 |
| 2. 測試包絡 | 版本、速度、實體路徑、製程、封裝、協定、管理功能、運作時間與錯誤情境是否相同？ | 公開測試計畫、環境、通過與失敗項目 | 只看到最高速度，就假定所有功能與封裝都通過 |
| 3. 供應商獨立性 | 是同一公司自我測試、多顆同源 die、兩家獨立 chiplet、共同測試機構，還是客戶與供應商雙向核對？ | 至少兩家獨立設計在共同條件留下可重現結果 | 把「三家公司各自送廠」加總成「三家互通」 |

成熟度只能在三軸交會處前進。例如一顆 32G 實體晶片在「物件階段」領先 64G tape-out，
卻沒有因此跨過「供應商獨立性」；16G 兩家互通在獨立性上更強，也不能借來替 64G 的速度與
測試包絡畢業。這就是本文所說的「不能斜著拼證據」。

## 把 16、32、64 放進同一張證據矩陣

| 具名證據 | 物件階段 | 測試包絡已知範圍 | 供應商獨立性 | 現在能說 | 還不能說 |
|---|---|---|---|---|---|
| Intel／Cadence Cameron Creek 16G | 跨廠 live test-chip demo | 16G、UCIe-S；完整 protocol、長時間與故障矩陣未公開 | 兩家獨立設計 | 特定 16G 實體組合已互通 | 64G 或所有功能、封裝與供應商可互換 |
| 創意 N3P／CoWoS 32G | 實體 test-chip measurement | UCIe 2.0、32Gbps、多顆 die；公告時 full-corner 仍在進行 | 來源只證實創意自身 test vehicle | 32G 已跨過純規格與送廠節點 | 多廠 compliance、客戶產品或完整可靠度已通過 |
| 創意 N3P／CoWoS 64G | test-chip tape-out | UCIe 3.0、64Gbps、AXI／CXS／CHI bridge；年報排定 2027Q1 silicon verification | 單一供應商 | 具名 64G 設計已送廠且有可追時程 | 截至年報已 silicon-proven、跨廠或量產 |
| Cadence N3P 64G | IP subsystem tape-out | 64Gbps 與多種 protocol 支援聲明 | 單一供應商 | 另一個獨立 64G 實作者已送廠 | 與創意、Intel 或其他 chiplet 完成實體互通 |
| Synopsys 2nm 64G | IP tape-out | 64Gbps 與 UCIe 3.0 工具鏈聲明 | 單一供應商 | 第三個可定位的 64G 送廠路徑 | 三家公告能組成一份共同測試結果 |

創意年報還分列「3nm UCIe 1.0 已於 2025 年第 3 季完成 silicon validation」與「5nm UCIe
LP 32G 原排 2026 年第 2 季 silicon verification」。本文刻意不把它們和 2025 年新聞稿的
N3P UCIe 2.0 32G 自動合併，因為版本、製程名稱與 test-chip 身分沒有在同一段落完全對齊。
這不是挑字眼，而是避免用 A 產品的回片替 B 產品補完里程碑。

## 創意（3443）應該怎麼讀

| 公司一手證據 | 可以放進研究結論 | 必須留白的橋 |
|---|---|---|
| 2025 年 32G UCIe 2.0 test-chip 實體量測 | 創意在 universe 內已有具名 UCIe 實體晶片證據，研究節點高於只宣布支援或只送廠 | 沒有跨廠對手、共同測試結果、完整 full-corner 報告與客戶產品 |
| 2026 年 64G UCIe 3.0 tape-out，加上年報的 2027Q1 silicon verification schedule | 可以建立可否證的公司里程碑，後續逐季檢查是否如期回片與公布測試包絡 | 不能在回片前寫成 64G silicon-proven，也不能把公司前瞻時程當保證 |
| 年報列出多代 UCIe／GLink／HBM IP 與公司整體營運 | 可以辨認創意的介面智財與先進封裝設計角色 | 沒有 UCIe 專屬授權、NRE、量產收入或毛利分母，不能把公司總營收歸因給 UCIe |

因此創意是這篇第一個可定位的台灣公司研究路由，但不是「64G 量產受惠已確認」的結論。
真正的升級條件是同一顆 64G IP 的回片、測試範圍、客戶 qualification 與財務分母依序接上。

## 把五種證據物件分開，不讓它們斜著畢業

| 本文五種證據物件 | 白話意思 | 本輪可確認 | 下一份證據 | 不能借用 |
|---|---|---|---|---|
| 1. 共同規格 | 多家參與者先約定介面、速度、管理與測試要求 | 第三代規格已定義 48／64 與管理功能 | 正式測試計畫與具名 64 結果 | 不能借用任何產品名稱當成實體通過 |
| 2. 介面智財與設計工具 | 設計者可以取得控制器、實體電路與驗證流程 | 有供應商公開 64 介面與工具鏈 | 另一獨立實作與共同測試條件 | 不能借用規格存在當成每家設計都相容 |
| 3. 送廠設計與回片 | 送廠表示設計交付製造，回片才有實體晶片可量測；兩者仍是不同節點 | 32 有創意實體量測；64 有三家各自送廠，創意年報把 64 驗證排在 2027Q1 | 同一 64 test chip 的回片、實測速度、錯誤率與失敗紀錄 | 不能借用 32 回片或 64 送廠聲明當成 64 實體測試成功 |
| 4. 測試晶片互通展示 | 兩家獨立晶片在特定封裝與條件完成指定工作 | 16 標準封裝路徑已有具名跨廠實體展示 | 同一產品組合的完整功能、故障與長時間結果 | 不能借用較低速度展示替最高速度通過 |
| 5. 客戶量產產品 | 客戶把多顆晶片做成具名產品，通過資格驗證並持續交付 | 本輪沒有可核對的 64 多廠客戶產品 | 客戶、晶片、封裝、資格與量產的雙向揭露 | 不能借用展示、會員資格或一般封裝能力當成訂單 |

證據可以並行出現，卻不能沿著不同產品「斜著畢業」。研究結論必須跟著同一個版本、同一組
晶片、同一種封裝與同一份測試條件前進；其中任何一項換了對象，就要重新標示邊界。

## 把六類角色放回同一個小晶片產品

| 本文六類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 規格聯盟與測試規則 | 共同介面版本、速度、管理功能與符合規格測試入口 | UCIe Consortium | 第三代共同規格與既有互通展示紀錄可查 | 聯盟發布規格不等於所有會員已有產品 |
| 2. 介面智財與設計工具 | 控制器、實體傳輸電路、模擬與驗證流程 | 創意、Cadence、Synopsys | 三家各自公開 64 介面送廠；創意另有 32 實體量測 | 多家各自實作不等於彼此互通、第三方測試或客戶收入 |
| 3. 小晶片設計者 | 各自設計能執行功能並接上共同介面的實體晶片 | Intel、Cadence | 兩家獨立測試晶片完成指定 16 跨廠展示 | 一組測試晶片不代表所有協定、速度與供應商可互換 |
| 4. 晶圓製造 | 把送廠設計製造成實體晶片，建立製程與良率條件 | 供應商來源列出 TSMC N3P／2nm | 可確認製程路徑與 32 實體量測；沒有 64 回片與可重算良率結果 | 製程節點不等於介面在目標速度通過 |
| 5. 封裝、載板與測試服務 | 組裝晶粒、安排接點與布線、挑出良品並驗證整包 | 創意來源列出 CoWoS test vehicle；未具名外部封裝測試服務商 | 可辨認 32／64 封裝路徑，尚無具名 64 客戶服務 | 使用某封裝技術不等於服務商取得訂單或毛利 |
| 6. 客戶產品與台灣財務查證 | 定義實際工作、資格驗證、量產分母，再與供應商揭露互相核對 | 本輪沒有具名 64 多廠客戶產品 | 仍是待驗證路由 | 客戶規劃、會員名單或公司能力不等於可辨識收入 |

六類角色是責任分工，不是固定供應商名單，也不是受惠排序。只有客戶與供應商能對同一個
介面版本、晶片、封裝、測試服務與量產期間雙向核對，才適合把產業關係接到公司財務。

## 最後用六關判斷「能互通」到「生態系成熟」

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 共同規格與測試合約可查 | 版本、速度、實體路徑、功能與測試方法有共同文件 | 已有第三代規格與測試入口 | 具名 64 測試計畫、條件與判定方式 | 有共同語言不等於已有實體產品 |
| 2. 介面實作完成並送廠 | 控制器、實體電路與驗證流程已整合成可製造設計 | 創意、Cadence、Synopsys 各有 64 介面送廠 | 各自的回片日期、晶片身分與首輪實測 | 三家送廠不等於三家互通或測試通過 |
| 3. 實體晶片在目標速度運作 | 回片晶片在同一速度、封裝與功能條件穩定收發 | 32 有創意實體量測；64 尚未由同一證據確認，創意年報排定 2027Q1 | 64 回片、錯誤率、溫度、full-corner 與長時間結果 | 32 的實體結果不等於 64 通過 |
| 4. 跨廠互通與正式測試對齊 | 兩家以上獨立晶片在相同條件互通，並有共同或第三方判定 | 特定 16 組合已有跨廠展示，64 正式結果未確認 | 64 多廠測試矩陣、符合規格結果與失敗樣本 | 一次展示不等於整個供應生態可互換 |
| 5. 客戶產品通過資格並量產 | 具名產品完成可靠度、良率、供應與實際工作驗收 | 本輪沒有可核對的 64 多廠客戶產品 | 客戶產品、封裝、資格、產量與持續交付 | 測試晶片或參考設計不等於量產產品 |
| 6. 台灣公司財務足跡可雙向核對 | 同一產品的服務、出貨、收入、毛利或現金流能由兩端確認 | 本輪只有矽智財、封測與載板搜尋路由 | 客戶與供應商對具名產品及財務期間共同揭露 | 產業必要性不等於公司已受惠 |

本輪不是「完全沒有進展」：共同規格、三家 64 介面送廠、創意 32 實體量測與 16 跨廠展示
都各自成立。真正的邊界是它們沒有落在同一組 64 實體產品，因此不能把第四關以前的分散證據
寫成第五或第六關。

## 這篇對公司判斷的用處與界線

| 看到公開訊息 | 可以先做 | 還不能做 |
|---|---|---|
| 公司加入聯盟或宣布支援共同介面 | 放入規格、介面智財或製造角色的候選清單 | 直接寫成具名訂單、跨廠互通或收入 |
| 介面設計完成送廠 | 追蹤回片、目標速度與第三方測試日期 | 把送廠當成實體晶片成功或客戶量產 |
| 兩家測試晶片完成展示 | 記錄速度、封裝、協定、測試時間與故障條件 | 外推到最高速度、所有廠商或長期可靠度 |
| 客戶開始資格驗證或量產 | 對齊具名晶片、封裝、測試服務、數量與期間 | 只憑單方宣稱估算供應商收入或毛利 |
| 台灣公司法說提到小晶片或先進封裝 | 查找同一具名產品、客戶與可歸因財務分母 | 用題材關鍵字、會員名單或一般能力做投資排序 |
| 公司年報列出下一次實體驗證時程 | 把版本、製程、test chip 與預定季度做成可否證監測 | 在預定季度以前先寫成完成，或用另一版本的回片代替 |

因此，本文把矽智財、封測與載板保留為研究入口，而不是受惠名單。下一次更新若仍只有新規格、
單一供應商自我測試或未具名客戶規劃，就只能更新相應節點，不能把整條生態系一起升級。

## 來源與證據邊界

- [UCIe 3.0 規格發布](https://www.uciexpress.org/_files/ugd/8dc731_ae67289d0ec646cdba5c1aee245538b3.pdf)（第三代最高傳輸率與管理功能）。
- [2026 小晶片高峰會互通展示](https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem)（Intel／Cadence 的 16 跨廠實體互通）。
- [Synopsys 64 介面智財送廠說明](https://www.synopsys.com/blogs/chip-design/64g-ucie-ip-high-speed-die-to-die-connectivity.html)（送廠製造節點）。
- [Synopsys 第三代介面方案更新](https://www.synopsys.com/blogs/chip-design/ucie-3-0-chiplet-ip-solutions.html)（實體傳輸電路、控制器與驗證流程）。
- [UCIe 規格持續更新入口](https://www.uciexpress.org/specifications)（後續版本與符合規格測試入口）。
- [Synopsys UCIe 介面持續更新入口](https://www.synopsys.com/designware-ip/interface-ip/die-to-die/ucie.html)（後續回片與互通消息入口）。
- [創意 32G UCIe 2.0 實體晶片公告](https://www.guc-asic.com/en/news/PressRelease/PR_ENG_20240313)（N3P／CoWoS test chip、32Gbps 量測與當時尚待 full-corner 的邊界）。
- [創意 64G UCIe 3.0 送廠公告](https://www.guc-asic.com/en/news/all/PR_20260226)（N3P／CoWoS 64G tape-out，不是回片結果）。
- [創意 2025 年報](https://www.guc-asic.com/upload/2026_04_16/8_202604161551145dnuwxrHk5.pdf)（第 3、61 頁的版本、製程、送廠與實體晶片驗證時程）。
- [Cadence N3P 64G UCIe 送廠公告](https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/cadence-tapes-out-ucie-ip-solution-at-64g-speeds-on-tsmc-n3p-technology)（另一家 64G test vehicle，仍不是共同互通結果）。
- [創意新聞稿持續更新入口](https://www.guc-asic.com/en/news/PressRelease)（後續 32G／64G 回片與驗證公告監測）。
- [UCIe 入門 webinar 問答](https://www.uciexpress.org/post/introduction-to-ucie-webinar-q-a-recap)（Gb/s／GB/s、x16 單向算例、module overhead、spare／sideband、CRC／retry／retrain 與 latency 邊界）。
- [UCIe 1.1 streaming error detection／replay](https://www.uciexpress.org/post/ucie-1-1-provides-streaming-protocol-solution-for-error-detection-and-replay)（特定 CHI packed-flit payload、header、CRC 與 replay；不是 64G 實測 goodput）。

本文不把不同速度、封裝或測試型態當成同一指標，也不使用會員數、宣稱市場規模或公司效能
數字做跨公司比較。規格聯盟對展示的敘述與介面供應商對自身產品的敘述都屬參與者一手資料，
仍需要未來符合規格測試與客戶產品形成獨立驗證。

## 影響路由

<!-- impact
group_id: ipdesign
stock_ids: 3443
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-02
rationale: 創意已用官方新聞稿與年報揭露 32G 實體晶片量測、64G tape-out 與預定 silicon verification，形成可定位的 universe 公司 UCIe IP 路由
evidence_boundary: 創意的 32G test chip 與 64G 送廠不等於 64G silicon-proven、跨廠 compliance、客戶 design win、UCIe 專屬收入或毛利
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
- 創意依 2025 年報時程，在 2027 年第 1 季前後公布同一顆 3nm 64G test chip 的回片、版本與測試包絡；若改期或換成另一版本，監測不視為原節點完成。
- 兩家以上獨立 chiplet 在同一實體 package 以 64G 完成可重現互通，並公開 protocol 與封裝範圍。
- 具名客戶把 UCIe multi-vendor chiplet 放進 qualification／production，而不只是 internal captive design。
- 台灣公司與客戶對同一具名 IP、封裝、substrate 或測試服務完成雙向核對；否則只保留族群搜尋線。
