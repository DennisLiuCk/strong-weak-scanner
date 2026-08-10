# AI 機櫃做出來，不等於客戶已上線：用六個關卡讀懂 AMD Helios

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

<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave97_helios_six_stage_five_customer_timeline_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **機架級系統（Rack-scale）**：把運算晶片、網路、電力、散熱與軟體整合成一整櫃交付；它比單顆晶片更接近可用設備，但不代表客戶已正式上線。
- **開始生產（Production）**：製造端已進入生產階段；這比只有設計圖更前進，但不等於產品已送到客戶手上。
- **實際出貨（Shipment）**：產品真正離開供應端並交付客戶；預告未來會出貨，不等於已發生出貨。
- **客戶測試與驗證（Validation）**：客戶仍在確認系統能否穩定執行自己的工作；開始測試不等於已通過、採購或部署。
- **正式上線（Online）**：系統已接通並投入運行；本文來源中的預計上線，不等於截至資料日已上線，也不自動代表已對外商用或已有收入。
- **部署（Deployment）**：把設備放進實際環境、接好並開始使用的過程；可以是一小批，也可以是後續擴張，必須看日期、範圍與容量。
- **雲端產品規格（SKU）**：雲端客戶可以選購或使用的具體產品配置；被預告的規格不等於已普遍開放使用。
- **即將推出（Upcoming）**：產品已被預告，但尚未證明進入測試開放或正式推出。
- **測試開放（Preview）**：產品開放給部分使用者測試；仍可能限制區域、名額、功能與服務承諾。
- **正式推出（Launched／GA）**：產品已進入正式供應狀態；仍要另外看可用區域、使用量與收入。
- **可用區域**：雲端產品實際在哪些資料中心區域可選用；公布型號但沒有區域，仍不能證明客戶可以立即使用。
- **利用率**：設備真正被工作負載使用的程度；設備已安裝，不等於一直在有效運轉。
- **吉瓦（GW）**：十億瓦，本文用來描述大型人工智慧基礎設施的電力規模；它是容量尺度，不是設備台數或採購金額。
- **最高可達（Up to）**：合作或容量的上限，不是目前已啟用、已採購或最後一定會達到的數量。
- **具名客戶**：公開文件直接點名的客戶；被點名比匿名市場傳聞更具體，但仍要分清預告、測試與實際使用。
- **生態系夥伴**：公開參與設計、製造、封裝或材料供應的公司；被列名只能證明合作角色，不能自動推成新增訂單、收入或毛利。
- **Helios**：AMD 的機架級人工智慧系統平台名稱，也就是本文追蹤的整櫃系統。
- **MI455X**：AMD 的 Instinct 加速器型號，是 Helios 裡執行人工智慧運算的核心晶片。
- **ND MI455X v7**：微軟 Azure 雲端虛擬機器的規格名稱；它是一個雲端產品型號，不是硬體出貨數量。
- **高架扇出橋接（EFB）**：用橋接結構連接同一封裝內多顆晶片的先進封裝路徑；合作文件出現此技術，不代表封裝商已有可辨識訂單。
- **2.5D 封裝**：把多顆晶片放在中介層或橋接結構上互連的封裝方式；具備技術能力不等於已進入具名產品量產。
- **客製晶片（ASIC）**：為特定客戶或任務設計的晶片；雲端客戶可能同時採用客製晶片與外部加速平台。
- **多架構共存**：同一客戶同時使用不同供應商或自研晶片；單一平台上線不等於其他架構被完全取代。
- **整機代工（ODM）**：把伺服器或機架系統設計、組裝並交付客戶的製造角色；合作列名不等於已取得新增份額。
- **機構件**：承載並固定機架、運算托盤與其他零件的結構；參與設計不等於量產數量或收入已確定。
- **載板**：承接晶片封裝內部電性連接與支撐的基礎材料；廣泛 AMD 合作不等於 Helios 專屬訂單。
- **資格認證（Qualification）**：客戶或平台確認產品符合規格與可靠度要求的過程；參與認證不等於已通過或已量產。
- **以 Helios 為基礎（Helios-based）**：系統以 Helios 架構為基礎，但不必然代表每個零件都只供 Helios 使用。
- **Helios 專屬（Helios-specific）**：文件明確把產品或出貨限定到 Helios；一般 AMD 合作不能自動改寫成專屬供應。
- **可辨識收入**：公司財報或說明能把收入與具名產品、客戶或業務分部合理連結，而不是只看產業總需求。
- **日月光／矽品／力成（ASE／SPIL／PTI）**：三家台灣封裝測試業者的中英文名稱；被 AMD 文件列為合作角色，仍不等於已有 Helios 訂單或財務貢獻。
- **現金流足跡**：訂單與收入最後是否轉成現金，並能在存貨、應收帳款或營業現金流看到合理變化。

### 三句話抓重點

- 機架級系統從「開始生產」走到客戶「正式上線」，中間還要經過出貨、測試與產品開放；每個動詞回答不同問題。
- 四個具名客戶目前分別停在產品預告、預計上線、仍在測試與未來容量規劃；它們不能相加成已部署。
- 台灣公司被列為生態系夥伴，只能證明合作角色；還要看到具名產品、量產出貨、可辨識收入與現金流足跡，才能談公司受惠。

### 為什麼重要

把人工智慧機櫃想成一棟要交付的建築：開始生產像開工，出貨像把建物交到現場，測試像
驗屋，正式上線才像住戶真的入住；合作名單則只是參與工程，還不是每家公司已經收款。
這篇把製造、客戶採用與公司財務分成三層，避免把前一層的進度直接當成下一層已完成。

### 接下來怎麼追

- 先看製造端是否從「預計出貨」變成有日期、有客戶邊界的實際交付。
- 再看各客戶是否由產品預告或測試，前進到可用區域、正式上線與可描述的部署範圍。
- 最後查台灣公司自己的季報、法說與重大訊息，是否同時出現具名產品、量產出貨及財務足跡。

### 想一想

- 如果工廠已能生產，但客戶仍在測試，哪一個部署關卡尚未完成？
- 產品頁只寫「即將推出」，和「已可使用」之間還差哪些證據？
- 一家公司被列為合作夥伴後，還要看到哪些公司級資料，才能把「參與」升級成「受惠」？
- 當客戶同時使用不同運算架構時，單一平台上線是否一定代表整體支出增加？

## 先把六個部署關卡排成順序

一套機架級系統可以「已經做得出來」，卻還沒有真正送到客戶、通過測試或投入使用。先把
六個關卡排好，後面看到任何公司或客戶動詞時，才知道它回答的是哪一題。

| 本文六個關卡 | 白話意思 | 可接受的證據 | 本篇目前到哪裡 | 不能直接推成 |
| --- | --- | --- | --- | --- |
| 1. 方案成形 | 整櫃架構、主要元件與合作角色已被公開 | 具名平台、規格與合作文件 | Helios 與台灣生態系角色已被公開 [S5] | 已能穩定量產或客戶已採用 |
| 2. 開始生產 | 製造端已進入生產，不再只有設計圖 | 製造商明確說明生產狀態與日期 | AMD 稱平台已進入生產 [S4] | 已出貨、已驗收或已有收入 |
| 3. 實際出貨 | 產品真的離開供應端並交到客戶 | 已發生的出貨日期、客戶與範圍 | 目前只有 2026 下半年開始出貨的規劃 [S2] | 規劃已如期完成或數量已確定 |
| 4. 客戶測試與產品開放 | 客戶測試自己的工作，或雲端規格開始可用 | 驗證完成、測試開放、正式推出與可用區域 | Meta 仍在測試；Azure 規格仍是預告 [S1][S4] | 已通過驗證、已普遍可用或已有利用率 |
| 5. 正式上線 | 客戶把系統接通並投入實際運行 | 客戶或供應商確認上線日期與部署範圍 | OpenAI 只有 2026 年第四季預計上線 [S4] | 截至資料日已上線、已對外商用或已有收入 |
| 6. 規模部署與財務轉換 | 小批上線持續擴張，並落到供應商財務 | 已部署容量、重複出貨、收入、毛利與現金流 | 只有廣義容量目標與未來首批規劃 [S3][S5] | 容量上限已落地或台灣公司已受惠 |

這六關是本文整理資訊的閱讀順序，不是所有平台都會依同一節奏前進，也不是公司排名、
訂單推估或投資建議。

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

## 再把五組公開節點放回自己的時間線

原始文件出現七個動詞、時程與容量數字，但它們來自平台方及四個不同客戶。正確讀法不是
把所有節點排成一條直線，而是先問「這是誰的時間線」，再檢查下一個可驗收結果。

| 本文五條時間線 | 已公開到哪一步 | 時間或上限 | 下一個可驗收節點 | 不能混成 |
| --- | --- | --- | --- | --- |
| 1. AMD 整體平台 | 已開始生產，並提出廣義大規模部署目標 [S4][S5] | 預計 2026 下半年開始推進 | 已發生的出貨、具名客戶與部署容量 | 所有客戶都已部署或台灣公司已有分配 |
| 2. Microsoft／Azure | AMD 規劃向 Microsoft 出貨；Azure 預告 ND MI455X v7 [S1][S2] | 出貨規劃在 2026 下半年，雲端規格未給上線日 | 實際出貨、測試開放或正式推出，以及可用區域 | 雲端規格已可使用、已有利用率或收入 |
| 3. OpenAI | AMD 表示客戶預計讓系統上線 [S4] | 預計自 2026 年第四季開始 | 客戶或 AMD 確認實際上線日期與部署範圍 | 截至資料日已上線或已對外商用 |
| 4. Meta | 已開始測試與驗證自己的工作 [S4] | 沒有公開完成日期 | 驗證完成、開始部署或改採其他平台 | 已通過驗證、已有採購量或部署日期 |
| 5. Anthropic | 公布未來合作上限與首批部署規劃 [S3] | 最高 2 GW；首個 GW 預計 2027 上半年開始 | 首批實際部署日期、容量與後續擴張 | 2 GW 已全部啟用或 AMD 已認列收入 |

本文沒有用上述數字做跨公司排名；2 GW、第一個 GW 與最高 50 億美元分別是容量上限、
首批部署節點與股權投資，定義不同，不能相加或互相比較。

## 反方路徑與失效條件

- **不同架構同時存在**：Microsoft 表示 Azure 同時採用外部方案與自研晶片；Helios 成為
  可部署選項，不等於排他標準，也可能只是既有人工智慧支出的份額重新分配。
- **製造與軟體仍可能卡住**：時程、第三方製造、記憶體與載板供應、良率、軟體相容及客戶
  訂單都有不確定性；開始生產仍可能與大規模、可靠部署有距離。
- **客戶節點可能停滯**：如果客戶錯過自己公布的期限，官方撤回測試，或改採其他平台，
  都會削弱「部署持續前進」的推論；單純沒有新公告只代表證據變舊，不直接視為失敗。
- **公司財務不一定轉換**：若台灣公司後續仍只談合作名單，沒有產品、出貨、毛利或現金流
  足跡，就應維持公司映射為待驗證，不能用平台進度替代公司證據。

## 來源與證據邊界

- [Microsoft：Azure 與 AMD 基礎設施擴展](https://blogs.microsoft.com/blog/2026/07/20/microsoft-expands-azure-ai-and-hpc-infrastructure-with-amd/)（S1）。
- [AMD／Microsoft：Helios 2026 下半年出貨規劃](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership)（S2）。
- [AMD／Anthropic：最高 2 GW 與首個 GW 時程](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)（S3）。
- [AMD AAI 2026：production、OpenAI 與 Meta 階段](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)（S4）。
- [AMD 台灣生態系：封裝與 ODM 合作名單](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)（S5）。
- 未來重查使用 [AMD IR](https://ir.amd.com/news-events/press-releases)（S6）、[Azure Updates](https://azure.microsoft.com/en-us/updates/)（S7）、[MOPS](https://mops.twse.com.tw/mops/web/index)（S8），以及 [OpenAI](https://openai.com/news/)（S9）、[Meta](https://about.fb.com/news/)（S10）、[Anthropic](https://www.anthropic.com/news)（S11）官方索引；新附件出現時必須另建 document source。

## 最後用六關把平台進度接回台灣公司

平台前進與公司受惠是兩條不同的證據鏈。先從公開列名開始，逐關確認角色、專屬產品、
量產出貨、財務與現金流；中間任何一關缺資料，就停在那一關。

| 本文六關 | 要回答的問題 | 現有資料能確認 | 下一份公司證據 | 不能外推 |
| --- | --- | --- | --- | --- |
| 1. 公開列名 | 公司是否被平台方直接點名 | AMD 列名整機、機構、封裝與載板夥伴 [S5] | 可重查的官方合作文件 | 被列名就有新增訂單 |
| 2. 具體角色 | 公司負責整機、機構、封裝還是載板 | 各家公司角色可分到三個族群 | 公司自己的產品與責任說明 | 同族群所有公司都參與 |
| 3. 平台專屬產品 | 產品是否明確只用在 Helios 或 MI450 系列 | 整機與機構文字較直接；封裝與載板多為較廣的 AMD 合作 | 具名料號、平台資格與雙方可核對文件 | 一般 AMD 合作都是 Helios 專屬 |
| 4. 驗證與量產出貨 | 具名產品是否通過驗證並持續出貨 | 本輪來源沒有台灣公司完成量產的公司級證據 | 驗證完成、出貨數量、產能與交付時程 | 技術合作等於量產或高利用率 |
| 5. 可辨識財務結果 | 出貨是否落到收入與毛利 | 本輪來源沒有可歸因的公司財務數字 | 季報、法說中的產品收入、毛利或分部資料 | 產業容量上限等於公司營收 |
| 6. 現金流與重複訂單 | 收入是否收得到現金並持續發生 | 本輪來源沒有訂單、存貨或現金流轉換證據 | 應收帳款、存貨、營業現金流與後續訂單 | 一次列名等於長期獲利 |

- **整機與機構**：6669 緯穎、3231 緯創、2356 英業達被列名協助打造以 Helios 為基礎的
  系統；3693 營邦被列名參與機架與運算托盤機構設計，目前先停在第 2～3 關。
- **封裝測試**：3711 日月光投控所含日月光／矽品與 6239 力成被列名參與高架扇出橋接與
  2.5D 技術合作，目前先停在第 2 關，仍要追具名產品資格與量產。
- **載板**：3037 欣興、8046 南電、3189 景碩被列名支援載板或先進封裝成長，但原文沒有
  寫成 Helios 專屬，也沒有訂單，目前只建立較寬的 AMD 載板追蹤路由。
- 散熱、電源與其他族群在這批來源沒有具名公司；本文不因機架級系統需要相關零組件，就
  自動推成受惠。

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
