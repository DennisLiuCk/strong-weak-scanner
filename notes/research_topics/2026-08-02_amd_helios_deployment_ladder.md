# AMD Helios：從參考設計走向具名部署，但七個里程碑不能混為訂單

<!-- research_topic
topic_id: MI-2026-08-02-AMD-HELIOS-DEPLOYMENT-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-23
last_reviewed_at: 2026-08-02
review_due: 2026-08-09
source_type: mixed
publisher: AMD / Microsoft
publisher_domain: amd.com
canonical_url: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
source_chain_id: amd-microsoft-helios-20260720-0723
stock_ids: 2356,3037,3189,3231,3693,3711,6239,6669,8046
group_ids: packtest,pcb,serverodm
trigger_type: product_ramp_and_named_deployment
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C1
base_confidence: medium
confidence_basis: Microsoft 與 AMD 對 2026-07-20 同一合作事件做雙方一手確認，另有 AMD 主導的 Anthropic、AAI 與台灣生態系文件支持不同里程碑；但這些不是彼此完全獨立的客戶自有揭露，除 AMD 所稱 in production 外，其餘多為前瞻時程或驗證中，且台灣合作名單沒有訂單與財務證據
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: recent_primary_source_market_scan
evidence: source_chain:amd-microsoft-helios-20260720-0723
-->

<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: named_deployment_ladder_separated_from_taiwan_order_mapping
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
reason: editorial_plain_language_wave6_compute_interconnect_learning_no_conclusion_change
evidence: editorial:plain_language_wave6
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **機架級系統（rack-scale）**：把 GPU、CPU、網路、電力、散熱與軟體整合成一整櫃交付；它比單顆晶片更接近可用設備，但不代表客戶已正式上線。
- **production**：AMD 表示 Helios 已進入生產階段；這是製造里程碑，不等於每個具名客戶都已收到、驗收或認列收入。
- **shipment／online／validation**：shipment 是開始出貨，online 在本來源只表示接通並投入運行，validation 是仍在測試與確認；online 不等於已對外商用、Azure GA、已有利用率或收入，三者不能互換。
- **GW（gigawatt）**：十億瓦，這裡描述大型 AI 基礎設施的電力規模；「最高可達」是合作上限，不是目前已啟用容量。
- **生態系夥伴**：公開參與設計、製造或封裝的公司；被列名只能證明合作角色，不能自動推成新增訂單、收入或毛利。
- **Helios**：AMD 的機架級 AI 系統平台名稱，也就是本文追蹤的那一整櫃系統。
- **MI455X**：AMD 的 Instinct 加速器（GPU）型號，是 Helios 裡的運算主角。
- **ND MI455X v7**：微軟 Azure 雲端虛擬機器的規格名稱。ND 是 Azure 給 GPU 加速機型的系列代號，MI455X 指所用的 AMD 加速器，v7 是該系列的版本。**它是一個雲端產品型號，不是硬體出貨數量**；微軟目前把它列為 upcoming，尚未給上線日期。
- **EFB（Elevated Fanout Bridge）**：AMD 生態系文件列出的一種先進封裝技術路徑，用橋接結構連接同一封裝內的多顆晶片。它出現在封裝夥伴的合作敘述裡，不代表任何一家封測廠已取得可辨識的訂單。
- **ASIC（特定用途集成電路）**：為特定客戶或任務設計的晶片。Helios 的支出成長可能是新增，也可能排擠客製 ASIC 或其他 GPU 平台。
- **SKU（可銷售規格項目）**：客戶可以選購或使用的具體產品配置。Azure 預告型號，不等於該 SKU 已普遍開放使用。
- **ASE／SPIL／PTI**：分別指日月光、矽品與力成的英文簡稱。AMD 文件列名合作角色，仍不等於已有 Helios 訂單或財務貢獻。
- **Helios-based／Helios-specific**：前者是「以 Helios 為基礎」，後者是「明確專屬 Helios」。一般 AMD 封裝合作不能自動改寫成 Helios 專屬出貨。

### 三句話抓重點

- AMD 已把 Helios 描述為 in production，Microsoft、OpenAI、Meta 與 Anthropic 也各有具名但不同階段的節點，因此研究問題已不再只是「有沒有參考設計」。
- 真正要追的是生產、2026 下半年出貨、廣義 multi-GW 部署目標、Azure 即將推出、OpenAI 第四季投入運行、Meta 驗證與 Anthropic 2027 上半年首個 GW 是否逐級兌現。
- AMD 列名 ODM、機構、封裝與載板夥伴只能建立搜尋路由；現有來源沒有證明台灣公司的新訂單或獲利。

### 為什麼重要

市場很容易把「平台已生產」與「客戶已部署」合併成一個完成式，再把合作名單直接映射成
台廠營收。這篇把每個動詞拆開，讓讀者能在相同時間軸上判斷：技術與製造風險是否下降、
客戶採用是否真的前進，以及價值最後有沒有落到台灣公司的收入、毛利與現金流。

### 接下來怎麼追

- 2026-08-09 重查 AMD 與 Azure 更新入口：是否出現 Helios 實際出貨，或 ND MI455X v7 由 upcoming 進入 preview／launched 並公布區域。
- 2026 年第四季追 OpenAI 是否確認 Helios 已 online；同時區分 Meta 是否仍停在 lab validation。
- 2027 年上半年以前追 Anthropic 首個 GW 是否開始部署，且不要把最高 2 GW 當成已上線容量。
- 追台灣被列名公司的季報、法說與重大訊息，是否同時出現產品階段、出貨及可辨識財務足跡。

### 想一想

- 如果 AMD 如期出貨，但 Azure 沒有推出可用 SKU，能否說 Helios 已完成雲端部署？
- Meta 的 validation 與 OpenAI 的 online，哪一個更接近客戶收入，還缺哪一步？
- 一家公司被列為製造夥伴後，至少要看到哪兩項公司級資料，才能把「合作」升級成「受惠」？
- Helios 是新增 AI 支出，還是從其他 GPU、客製 ASIC 與既有供應鏈重新分配的份額？

## 為何值得現在研究

2026-05-21 至 07-23 的官方文件形成一條可檢驗的部署階梯。AMD 先表示 Helios on track for
multi-gigawatt deployments beginning 2H 2026；這是未分配到具名客戶的廣義平台目標。
Microsoft 隨後將 Helios 驅動的
ND MI455X v7 列為三項 upcoming Azure offerings 之一；AMD 同日表示會在 2026 下半年開始
向包括 Microsoft 在內的客戶出貨。其後 AMD／Anthropic 公布最高 2 GW、首個 GW 預計
2027 年上半年開始部署；AMD 07-23 又稱 Helios 已 in production，並把 OpenAI 的第四季
online 與 Meta 的 validation 分開描述。廣義 multi-GW 目標與 Anthropic 具名首個 GW 的
客戶範圍及期限不同，不能視為矛盾，也不能把前者當成已部署容量。這些節點比單純路線圖
更具體，但仍不是同一完成度。

## 主張與證據帳本

<!-- research_source
source_id: S1
role: other_primary
source_kind: document
publisher: Microsoft
title: Microsoft expands Azure AI and HPC infrastructure with AMD
published_at: 2026-07-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/
locator: 開頭 infrastructure strategy、three upcoming Azure offerings 與 Production-scale AI inference — ND MI455X v7 段落
limitation: Microsoft 把 ND MI455X v7 稱為 upcoming offering，未提供 GA 日期、可用區域、部署數量或台灣供應商；同文並稱 Azure 同時採用自研 purpose-built silicon
independence_group: amd-microsoft-20260720
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: AMD
title: Microsoft to Deploy Next-Gen AMD Instinct and AMD EPYC Processors as the Companies Expand Their Long-Term Strategic Partnership
published_at: 2026-07-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership
locator: News Highlights、Microsoft will deploy Helios 與 AMD will begin shipping Helios to customers including Microsoft in 2H 2026 段落；Cautionary Statement
limitation: 2026 下半年出貨與產品時程是 AMD 的前瞻性陳述，不是已完成出貨、Azure GA、收入或毛利
independence_group: amd-microsoft-20260720
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: AMD
title: AMD and Anthropic Announce Strategic Partnership to Deploy Up to 2 Gigawatts of AMD Instinct MI450 Series GPUs
published_at: 2026-07-22
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus
locator: News Highlights 與首段的 up to 2 GW、first gigawatt beginning in 1H 2027；另見最高 50 億美元股權投資段落
limitation: up to 2 GW 是合作上限且首個 GW 尚待未來部署；最高 50 億美元是 AMD 對 Anthropic 的股權投資承諾，不能與設備採購額混為一談
independence_group: amd
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: AMD
title: AAI 2026: AMD Delivers Full-Stack Compute for the Agentic AI Era
published_at: 2026-07-23
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era
locator: Helios now in production 段落；AMD Helios 與 partner deployment bullets，特別是 OpenAI Q4 online、Meta testing and validating
limitation: in production 是 AMD 對平台製造階段的敘述；客戶節點仍包含預期上線與驗證，且 AMD 的效能／經濟性數字屬自家測試，本文不據此做跨公司排名
independence_group: amd
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: AMD
title: AMD Announces More Than $10 Billion in Taiwan Ecosystem Investments to Accelerate AI Infrastructure
published_at: 2026-05-21
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure
locator: News Summary 的 multi-gigawatt deployments beginning 2H 2026、EFB ecosystem development、Panel-based innovation with PTI、Ecosystem Accelerates AMD Helios Deployment，以及 Unimicron／AIC／Nan Ya PCB／Kinsus 引言
limitation: 2H26 multi-GW 是 AMD 未分配到具名客戶的前瞻平台目標；超過 100 億美元是廣泛台灣生態系總投資敘述，未分配到個別公司；所有列名都沒有訂單、數量、ASP、收入或毛利，且載板三家公司未被寫成 Helios-specific
independence_group: amd
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: AMD
title: AMD Investor Relations Press Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.amd.com/news-events/press-releases
locator: 截至 2026-08-02，首頁可見 07-20 Microsoft、07-22 Anthropic 與 07-23 AAI 2026 公告，供後續查找新的 Helios 出貨、客戶或財務附件
limitation: 索引會持續變動且沒有單一發布日；只能作為未來重查入口，新公告必須另建 document source 才能更新 claim
independence_group: amd
-->

<!-- research_source
source_id: S7
role: other_primary
source_kind: living_index
publisher: Microsoft Azure
title: Azure Updates
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://azure.microsoft.com/en-us/updates/
locator: 截至 2026-08-02，頁面提供 In development、In preview、Launched 狀態定義；當日未取得可定位的 ND MI455X v7 獨立更新項目
limitation: 此頁由動態篩選產生且會持續改變；當日沒看到項目不是不存在的證明，未來命中須另存正式更新頁
independence_group: microsoft-azure
-->

<!-- research_source
source_id: S8
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 截至 2026-08-02，作為 2356、3037、3189、3231、3693、3711、6239、6669、8046 季報、法說及重大訊息的後續查找入口
limitation: 入口會持續更新且沒有單一發布日；產業公告不能替代各公司自己的產品、訂單與財務附件
independence_group: twse-mops
-->

<!-- research_source
source_id: S9
role: other_primary
source_kind: living_index
publisher: OpenAI
title: OpenAI News
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://openai.com/news/
locator: 截至 2026-08-02 的官方 News 索引，作為 OpenAI 自有 Helios 上線、基礎設施或時程更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 OpenAI 已確認 Helios online；命中後須另建可定位 document source
independence_group: openai
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: living_index
publisher: Meta
title: Meta Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://about.fb.com/news/
locator: 截至 2026-08-02 的官方 Newsroom 索引，作為 Meta 自有 Helios validation、部署或取消更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 Meta 已完成 Helios validation 或部署；命中後須另建可定位 document source
independence_group: meta
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: living_index
publisher: Anthropic
title: Anthropic Newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.anthropic.com/news
locator: 截至 2026-08-02 的官方 Newsroom 索引，作為 Anthropic 自有 Helios 首個 GW、時程、縮量或取消更新的後續查找入口
limitation: 動態索引沒有單一發布日且目前不等於 Anthropic 已開始部署；命中後須另建可定位 document source
independence_group: anthropic
-->

<!-- research_claim
claim_id: C1
label: inference
status: active
claim: Helios 已跨過只有參考設計的研究階段，進入具名生產與部署階梯；但 production、2026 下半年 shipment、未具名客戶的 multi-GW deployment 目標、Azure upcoming SKU、OpenAI 第四季 online、Meta validation 與 Anthropic 2027 上半年首個 GW 是七個不同完成度，不能合併成已全面部署
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-02
basis: S4 直接稱 Helios now in production；S1／S2 是同一 Microsoft 合作事件的雙方一手確認，S3 至 S5 是 AMD 主導的其他客戶、平台與生態系文件，合計足以把研究問題從是否存在移到各階段是否兌現，但不構成完全獨立的客戶交叉驗證
boundary: 這是產品與客戶里程碑的階段推論；S5 的 multi-GW 是未分配到具名客戶的廣義前瞻目標，不證明目前容量、每個客戶已驗收、AMD 已認列收入、Helios 取得排他份額或台灣夥伴已有新訂單
verification_needed: AMD 實際出貨公告、Azure SKU 狀態與區域、客戶上線確認及公司財務揭露
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: AMD 在 2026-07-23 正式將 Helios 描述為 now in production
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-02
basis: S4 新聞稿首段直接使用 now in production 描述 Helios
boundary: 只證實 AMD 做出平台生產階段的正式敘述，不等於客戶已收到、驗收、上線或帶來可辨識收入
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
claim: AMD 表示將於 2026 下半年開始向包括 Microsoft 在內的客戶出貨 Helios；Microsoft 則把 Helios 驅動的 ND MI455X v7 列為 upcoming Azure offering
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-08-02
basis: S2 直接給出 begin shipping in the second half of 2026，S1 直接把 ND MI455X v7 放在 three upcoming Azure offerings
boundary: 這證實兩家公司當時公布的未來時程與產品定位，不證明已出貨、已 GA、可用區域或利用率
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
claim: AMD 表示 OpenAI 預期自 2026 年第四季開始讓 Helios online；Meta 當時則仍在實驗室測試與驗證 Helios workloads
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-08-02
basis: S4 的 partner deployment bullets 分別使用 expects to bring Helios online beginning in Q4 2026 與 begun testing and validating workloads
boundary: OpenAI 是未來預期、Meta 是驗證狀態；兩者都不能寫成截至 2026-08-02 已完成大規模部署
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
claim: AMD 與 Anthropic 公布最高 2 GW 的 Helios 合作，首個 GW 預計在 2027 年上半年開始部署；AMD 另承諾未來最高 50 億美元股權投資
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-08-02
basis: S3 的 News Highlights、首段與投資段落直接分開揭露部署上限、首批時程及股權投資
boundary: up to 是上限而非已部署容量；股權投資不是 Anthropic 向 AMD 採購設備的金額，也不證明收入認列
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
claim: AMD 的台灣生態系公告列名 ASE／SPIL／PTI 參與 EFB／2.5D 封裝，Wiwynn／Wistron／Inventec 協助打造 Helios-based systems，AIC 參與 Helios 機架與 compute-tray 機構設計，並列名 Unimicron／Nan Ya PCB／Kinsus 支援載板或先進封裝
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-02
basis: S5 的 EFB、PTI、Helios deployment 段落及四家公司引言直接列出上述公司與合作角色
boundary: 列名只證實合作角色；三家載板公司的文字是廣泛 AMD packaging 支援，不是 Helios-specific，所有列名都不證實新訂單、分配份額、出貨量、ASP、收入、毛利或現金流
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
claim: Microsoft 明確表示 Azure AI 基礎設施同時使用 AMD 等外部創新者與自家 purpose-built silicon and systems
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-02
basis: S1 開頭直接描述 Azure 以異質平台同時採用產業夥伴與自研晶片／系統
boundary: 這支持多架構共存的反方路徑，但沒有披露 Helios、自研晶片或其他 GPU 的份額，因此不能判斷誰將取代誰
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: unverified
status: active
claim: 緯穎、緯創、英業達、營邦、日月光／矽品、力成、欣興、南電與景碩已因 Helios 取得可量化新增訂單、收入或獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S5 只有生態系投資、技術與合作角色，且載板列名不是 Helios-specific；S1 至 S4 也沒有提供台灣公司的訂單及財務資料
boundary: 此主張不得放入正式公司筆記、估值或 H# 終態，也不能用產業總投資或 GW 上限補洞
verification_needed: 各公司一手季報、法說或重大訊息須把具名產品與客戶階段連到出貨、收入、毛利、存貨或營業現金流
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: AMD 在 2026-05-21 表示 Helios on track for multi-gigawatt deployments beginning 2026 下半年，並稱生態系夥伴支援同期部署
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-05-21
basis: S5 News Summary 直接使用 multi-gigawatt deployments beginning 2H 2026，正文另稱生態系支援 Helios 在 2026 下半年部署
boundary: 這只證實 AMD 當時提出廣義平台目標；沒有具名客戶容量、已部署證據或台灣公司分配，不能與 Anthropic 2027 上半年首個 GW 合併或視為矛盾
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 部署階梯：七個節點不能互換

| 節點 | 截至 2026-08-02 的證據 | 還不能證明 |
| --- | --- | --- |
| production | AMD 稱 Helios now in production [S4] | 客戶已驗收、上線或 AMD 已認列收入 |
| 2H26 shipment | AMD 預計下半年開始向包括 Microsoft 的客戶出貨 [S2] | 已出貨數量、時間點與收入 |
| 2H26 broad multi-GW target | AMD 稱 Helios on track for multi-GW deployments beginning 2H26 [S5] | 具名客戶容量、已開始部署或台廠分配；與 Anthropic 首個 GW 的客戶範圍及期限不同 |
| Azure upcoming SKU | Microsoft 列出 upcoming ND MI455X v7 [S1] | preview、GA、區域與利用率 |
| OpenAI Q4 online | AMD 轉述 OpenAI 預期第四季開始 online [S4] | 已上線或 2027 年部署速度 |
| Meta validation | AMD 稱 Meta 已開始測試與驗證 workloads [S4] | 通過驗證、採購量或部署日期 |
| Anthropic first GW | 首個 GW 預計 2027 上半年開始部署 [S3] | 最高 2 GW 全數落地或已認列收入 |

本文沒有用上述數字做跨公司排名；2 GW、第一個 GW 與最高 50 億美元分別是容量上限、
首批部署節點與股權投資，定義不同，不能相加或互相比較。

## 反方路徑與失效條件

- **多架構共存**：Microsoft 自己說 Azure 同時採用外部方案與 purpose-built silicon；
  Helios 成為可部署選項，不等於排他標準，也可能只是既有 AI 支出的供應份額重分配。
- **軟硬體執行風險**：S2 的前瞻性警語列出時程、第三方製造、記憶體／基板供應、良率、
  軟體相容與客戶訂單不確定性；production 仍可能與大規模可靠部署有距離。
- **客戶階段停滯**：Azure／OpenAI／Anthropic 若錯過各自明示期限，或 Meta 官方撤回
  validation／選擇替代方案，都會削弱「部署階梯持續上行」的推論；Meta 單純沒有新公告
  只會觸發可信度降級，不當成反證。
- **台灣財務沒有轉換**：若台廠後續仍只談合作名單，沒有產品、出貨、毛利或現金流足跡，
  就應維持公司映射為待驗證，而不是用 AMD 平台進度替代公司證據。

## 來源與證據邊界

- [Microsoft：Azure 與 AMD 基礎設施擴展](https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/)（S1）。
- [AMD／Microsoft：Helios 2026 下半年出貨規劃](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership)（S2）。
- [AMD／Anthropic：最高 2 GW 與首個 GW 時程](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)（S3）。
- [AMD AAI 2026：production、OpenAI 與 Meta 階段](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)（S4）。
- [AMD 台灣生態系：封裝與 ODM 合作名單](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)（S5）。
- 未來重查使用 [AMD IR](https://ir.amd.com/news-events/press-releases)（S6）、[Azure Updates](https://azure.microsoft.com/en-us/updates/)（S7）、[MOPS](https://mops.twse.com.tw/mops/web/index)（S8），以及 [OpenAI](https://openai.com/news/)（S9）、[Meta](https://about.fb.com/news/)（S10）、[Anthropic](https://www.anthropic.com/news)（S11）官方索引；新附件出現時必須另建 document source。

## 台灣映射與證據邊界

- **serverodm**：6669 緯穎、3231 緯創、2356 英業達由 AMD 直接列名協助打造
  Helios-based systems；3693 營邦則被列名參與 Helios 機架與 compute-tray 機構設計，
  都只能先追量產、驗收、出貨與營運資金。
- **packtest**：3711 日月光投控所含 ASE／SPIL 與 6239 力成由 AMD 列名於 EFB／2.5D
  技術合作，只能先追資格認證、產能與公司財務轉換。
- **pcb**：3037 欣興、8046 南電、3189 景碩被列名支援載板或 advanced-packaging growth，
  但原文沒有把三者寫成 Helios-specific，也沒有訂單；只能建立較寬的 AMD 載板追蹤路由。
- 散熱、電源與其他族群在這批來源沒有具名公司；本文不因 rack-scale 系統需要相關零組件
  就自動推成受惠。

<!-- impact
group_id: serverodm
stock_ids: 2356,3231,3693,6669
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 Inventec、Wistron、Wiwynn 協助打造 Helios-based systems，並列名 AIC 參與 Helios 機架與 compute-tray 機構設計，值得在公司文件追驗證、量產、出貨與營運資金
evidence_boundary: 生態系與製造夥伴列名不等於新增訂單、分配份額、收入、毛利或現金流
-->

<!-- impact
group_id: packtest
stock_ids: 3711,6239
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 ASE／SPIL 與 PTI 的 EFB／2.5D 技術開發或資格認證角色，值得追量產與財務轉換
evidence_boundary: 技術合作與資格認證不等於 Helios 專屬訂單、產能利用、收入或獲利
-->

<!-- impact
group_id: pcb
stock_ids: 3037,3189,8046
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AMD 直接列名 Unimicron、Nan Ya PCB 與 Kinsus 支援載板或 advanced-packaging growth，值得追產品資格、出貨與財務轉換
evidence_boundary: 三家公司列名不是 Helios-specific；廣泛 AMD 載板合作不等於 Helios 新訂單、分配份額、收入、毛利或現金流
-->

## 持續驗證帳本

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C3,C9
metric: Helios 由 production 進入實際出貨、廣義 multi-GW deployment，以及 Azure ND MI455X v7 的產品狀態與可用區域
source_ids: S1,S2,S4,S5
watch_source_ids: S6,S7
frequency: weekly
next_check: 2026-08-09
trigger: AMD 以新文件確認已開始出貨或 multi-GW deployment 並提供客戶／容量邊界，或 Azure 將 ND MI455X v7 列為 preview／launched 並公布區域
invalidation: AMD 或 Microsoft 官方延後／取消 2026 下半年出貨或部署，Azure 撤回產品；若截至 2026-12-31 仍無實際出貨／部署確認且 Azure 維持 upcoming，也判定原 2H26 時程未兌現
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C1,C4
metric: OpenAI 是否在 2026 年第四季把 Helios 接通並投入運行
source_ids: S4
watch_source_ids: S6,S9
frequency: monthly
next_check: 2026-09-01
trigger: OpenAI 自有文件或 AMD 新文件確認 Helios 已 online，並提供投入運行日期或部署範圍
invalidation: OpenAI 或 AMD 官方延後／取消原時程；若截至 2026-12-31 仍無 online 確認，也判定原第四季時程未兌現
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C4
metric: Meta Helios workloads 由 testing／validation 進入通過驗證或實際部署
source_ids: S4
watch_source_ids: S6,S10
frequency: monthly
next_check: 2026-09-01
trigger: Meta 自有文件或 AMD 新文件確認 validation 完成、開始部署，並提供產品或部署範圍
invalidation: Meta 或 AMD 官方表示 Helios validation 失敗、取消、改採其他平台或不再推進；單純沒有新公告只觸發 freshness downgrade，不視為反證
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C1,C5
metric: Anthropic 首個 GW 是否在 2027 年上半年開始部署，以及最高 2 GW 是否縮減
source_ids: S3
watch_source_ids: S6,S11
frequency: monthly
next_check: 2026-09-01
trigger: Anthropic 自有文件或 AMD 新文件確認首批部署開始，並提供日期、容量或後續擴張
invalidation: Anthropic 或 AMD 官方延後至 2027 下半年以後、取消或縮減原合作；若截至 2027-06-30 仍未開始首個 GW，也判定原時程未兌現
-->

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C6,C8
metric: 台灣 ODM、機構、封裝與載板夥伴的具名產品、出貨、收入、毛利、存貨與營業現金流
source_ids: S5
watch_source_ids: S8
frequency: quarterly
next_check: 2026-08-15
trigger: 台灣公司一手文件把 Helios／MI450 系列、EFB、機構或載板角色連到量產、可辨識收入與獲利或現金流
invalidation: 公司明示合作／資格取消、沒有相關訂單或不再參與，或具名產品的可定位分部資料直接顯示零收入／無重大財務貢獻；只有未見新揭露時維持 C8 待驗證
-->

## 下一個可證明／否定的節點

最先到期的是 2026-08-09 的 AMD／Azure 產品狀態重查。沒有新文件時，只在 append-only
scan log 記錄「未見新證據」，不能把 review due 往後移，也不能刷新主命題的 evidence
clock。只有新增且被 active claim 引用的正式文件，才可更新里程碑與可信度；台灣公司映射
仍須依各公司一手文件重做，不能從本篇直接升格為正式公司事實。
