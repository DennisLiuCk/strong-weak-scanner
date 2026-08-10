# 液冷設備不能只比容量：平台列名、供應準備與收入是三種不同證據

<!-- research_topic
topic_id: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-27
last_reviewed_at: 2026-08-09
review_due: 2026-08-14
source_type: mixed
publisher: NVIDIA
publisher_domain: marketplace.nvidia.com
canonical_url: https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/
source_chain_id: nvidia-liquid-cooling-marketplace-capture-20260802
stock_ids: 3017,2308,2301
group_ids: thermal,powersupply
trigger_type: qualification_and_supply_stage
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C9
base_confidence: medium
confidence_basis: NVIDIA 動態清單在捕捉日以同一欄標示三個型號的額定容量與供應狀態，容量保留原始 MW／kW 後可正規化比較；另有 LG 與 Daikin 一手文件補充認證、合作及 PoC 階段，但 Marketplace 沒有固定版本與完整跨廠測試協定，台廠訂單、收入與獲利也尚未證實
cross_company_numbers: true
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: captured_same_column_cdu_capacity_and_supply_status
evidence: source_chain:nvidia-liquid-cooling-marketplace-capture-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_comparable_capacity_from_qualification_supply_and_financial_maturity
evidence: sources:S1,S2,S3,S4
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
reason: weekly_monitor_trigger_lge_added_to_marketplace_without_supply_status
evidence: sources:S8
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave7_power_cooling_learning_no_conclusion_change
evidence: editorial:plain_language_wave7
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave87_capacity_maturity_evidence_ladder_no_conclusion_change
evidence: editorial:plain_language_wave87_capacity_maturity_evidence_ladder
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **液冷**：用液體把伺服器產生的熱帶走。它是一整套散熱方式，可能包含冷板、管路、泵浦、熱交換器、控制系統與機房冷卻設備，不等於只買一台 CDU。
- **CDU（Coolant Distribution Unit）**：冷卻液分配單元，透過泵浦、熱交換器與控制系統，把伺服器迴路的熱帶走。它不是 GPU 上的冷板，也不等於機房產生冷水的 chiller。
- **額定容量**：設備在指定測試條件下，設計上可帶走的熱量。它回答「能處理多少熱」，不回答效率、可靠度、客戶採用或公司收入。
- **MW／kW**：兆瓦／千瓦，都是功率單位；`1MW = 1000kW`。換成同一單位後只能比較數值大小，不能順便比較產品成熟度。
- **Cooling Capacity @ 4°C ATD**：NVIDIA 清單以這個欄名標示 CDU 的額定排熱能力。MW／kW 是絕對容量，不是效率或產品優劣；同欄數字可在單位換算後比較，但頁面沒有公布完整跨廠測試協定，實際水溫、流量、壓差與備援仍會改變可用能力。
- **ATD（Approach Temperature Difference）**：熱交換兩側在指定位置的溫差條件。本文只沿用 NVIDIA 欄名中的 `4°C ATD`，不自行補上頁面未公布的完整測試程序。
- **流量**：冷卻液在一定時間內通過管路的體積；常見單位是每分鐘公升。流量會影響帶熱能力，但不能單獨代表整套系統效能。
- **壓差**：冷卻液流過管路與元件前後的壓力差。壓差過大可能提高泵浦負擔，因此容量相同的設備仍可能有不同整合條件。
- **備援**：主要泵浦、電源或控制元件失效時，由另一組元件接手。額定容量沒有說明設備在故障情境下還能維持多少能力。
- **材料相容性**：冷卻液、金屬、密封件與管路長期接觸時是否會腐蝕、膨潤或產生污染。它是部署條件之一，不會由 kW 數字直接回答。
- **冷板**：貼近 GPU、CPU 或其他發熱元件，把熱傳給冷卻液的金屬元件。冷板位於伺服器端，和負責分配、換熱與控制的 CDU 不同。
- **Chiller（冰水主機）**：在設施端製造冷水或移走熱量的設備。它和 CDU 可能一起工作，但容量、控制責任與收入來源不能混成同一項產品。
- **HVAC**：建築或資料中心的暖通空調系統，涵蓋加熱、通風與空調。本文提到的是機房整體冷卻整合，不等於單一 CDU 的表現。
- **平台列名**：產品被平台清單列出，表示至少能在指定日期找到該產品資料；它不等於客戶已驗收、已下單或公司已認列收入。
- **Sample Ready／MP Ready**：NVIDIA Marketplace 的供應狀態標籤。本文保留原文，不自行把 `MP Ready` 解釋成已有大量客戶訂單，也不把 `Sample Ready` 解釋成產品不成熟。
- **平台驗證**：產品通過平台商指定測試或被列進合格清單；它降低部分技術採購風險，仍不等於客戶已下單、完成部署或供應商已認列收入。
- **Validation type**：平台列出的驗證類別。它能說明產品接受哪一類平台測試，不能代替完整測試分數、客戶現場驗收或量產訂單。
- **Supply Chain Status**：NVIDIA 清單中的供應狀態欄。本文只保存來源原文；平台沒有公布足以換算成產能、良率、交期或收入的共同尺度。
- **客戶部署**：設備進入客戶場域，完成安裝、整合並開始運作。平台列名與送樣都不能自動證明已完成部署。
- **客戶驗收**：客戶依約定條件確認設備或系統可接受。驗收比平台列名更接近商業結果，但仍須看是否產生訂單、交付與收入。
- **量產**：產品以可重複方式持續製造與交付。本文沒有各型號的產量、良率、庫存或交期資料，因此不能替公司判定量產規模。
- **財務認列**：公司依會計規則把交易記入收入、成本或獲利。產品列名、合作備忘錄與概念驗證都不能直接代替財務認列。
- **毛利**：收入扣除直接銷售成本後的金額或比率。即使已有收入，仍需產品別或可合理拆分的資料，才能判斷液冷產品的獲利貢獻。
- **PoC（Proof of Concept，概念驗證）**：在真實或接近真實的環境做小規模試行，用來確認方案可行。**PoC 進行中不等於已交付節電、成本或可靠度數字**，本文多處出現的 PoC 都停在這個階段。
- **MOU（合作備忘錄）**：合作方對預計合作範圍的書面表達。它不是已完成產品、採購合約、出貨或收入證據。
- **Portfolio（產品組合）**：一家公司或合作案規劃涵蓋的一組產品。範圍可大於單一型號，不能拿整組規劃覆蓋某台設備的額定數字。
- **AVC／奇鋐（3017）**：AVC 是 Asia Vital Components 的縮寫；本文用公司官網的 `TSE: 3017` 完成名稱映射。這只確認公司身分，不證明具名客戶或收入。
- **Delta／台達電（2308）與 LITEON／光寶科（2301）**：本文以英文公司名出現的兩家台灣電源與散熱供應商，都是本 universe 成員。文中提到它們時只涉及產品被列出或通過平台驗證，不含訂單、出貨量或毛利證據。
- **LGE／LG Electronics**：LG 電子的英文縮寫。2026-08-09 的 NVIDIA 清單可定位其 600kW 列項，但供應狀態欄空白，因此不能替它補成任何階段。
- **CDU1000-LTL-RW／RDF106CDT5192／LC-LL-WCDU-6011(S)**：分別是 AVC、Delta 與 LITEON 在 NVIDIA 清單中的 CDU 型號。型號只是辨識產品的名字；容量、供應狀態與量產證據仍要分欄閱讀。
- **TSE（Taiwan Stock Exchange，臺灣證券交易所）**：本文只用公司官網的 `TSE: 3017` 把 AVC 對應到臺灣上市公司奇鋐；這個代號本身不證明該 CDU 的客戶或收入。
- **FY2027（2027 財政年度）**：公司的 2027 會計年度，起訖日不一定等於 2027 曆年。本文引用的是 Daikin 的商用目標時間，不是目前已完成部署。

### 三句話抓重點

- 2026 年 8 月 2 日保存的 NVIDIA 清單，在同一欄列出三個供應商型號的容量：1.2MW、1MW 與 380kW。把單位都換成 kW 後，這三個數字可以比較。
- 容量只回答設備在指定條件下設計可帶走多少熱；平台列名與供應標籤只能說明部分資格與準備進度，兩者都不等於客戶已部署。
- 要判斷誰更接近收入，還要看到客戶驗收、量產數量與公司財務揭露。目前這些證據都缺，因此不能用容量大小替公司排行。

### 為什麼重要

液冷題材最容易把不同關卡混成一張排行榜。讀這篇時先拆成五問：設備能帶走多少熱？是否已被平台列出或完成部分測試？供應準備到哪一步？客戶是否真的部署並驗收？公司是否已把交易認列為收入？容量只能回答第一問，平台欄位只回答中間兩問的一部分；最後兩問仍要靠客戶與公司資料。把五關分開，才不會看到 1MW 就推論某家公司一定比 380kW 的供應商更成熟或賺得更多。

### 接下來怎麼追

- 每週保存 NVIDIA 清單的型號、額定容量、驗證類別與原始供應標籤；只記錄欄位怎麼變，不自行替空白欄位補答案。
- 查 3017、2308、2301 的重大訊息、法說與季報，等到公司首次把具名型號連到客戶驗收、量產數量、收入占比與毛利，才把證據往商業結果推進。
- 追蹤 Daikin／NTT DATA 的概念驗證是否在 2027 年 3 月前公布可重算的節電、成本或自動化結果，以及 Daikin 對 2027 財政年度的商用目標是否維持。

### 想一想

- 如果一個型號容量較大，另一個型號的供應標籤看起來更往前，只靠這兩欄能判斷誰更接近客戶訂單與收入嗎？
- 客戶選擇冷卻設備時，除了容量，是否還會同時檢查流量、壓差、故障備援、材料相容性、維修網路與整套控制整合？
- 如果後續收入來自冰水主機、冷板或控制軟體，而不是冷卻液分配單元，研究中心應如何重新判斷價值落在哪一層？

## 主張與證據帳本

`證實` 只代表指定來源支持精確措辭；平台列名、認證或 MOU 都不自動證明客戶訂單、量產收入或獲利。

<!-- research_source
source_id: S1
role: other_primary
source_kind: living_index
publisher: NVIDIA Marketplace
title: DSX Infrastructure for AI Factory validated CDU list
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/
locator: 2026-08-02 捕捉的 CDU 表；欄名 Cooling Capacity @ 4°C ATD 與 Supply Chain Status；AVC CDU1000-LTL-RW、Delta RDF106CDT5192、LITEON LC-LL-WCDU-6011(S) 三列
limitation: 頁面會持續改動、沒有固定發布日或不可變版本；清單只支持捕捉日看到的列名、欄位標示值與原始狀態，不提供完整跨廠測試協定、客戶、訂單、出貨量、收入、市占或毛利，頁面改版後舊值可能無法由外部重現
independence_group: nvidia-marketplace
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: LG Electronics
title: LG Electronics Earns NVIDIA AI Data Center Validation for Its 600kW Coolant Distribution Unit
published_at: 2026-07-27
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.lg.com/global/newsroom/news/eco-solution/lg-electronics-earns-nvidia-ai-factory-validation-for-its-600kw-coolant-distribution-unit/
locator: News Summary 與 Reliable Partner for Global Hyperscalers 段落；600kW CDU、超過 100 項 technical evaluation criteria；Expanding AI Infrastructure Capabilities 段落
limitation: LG 的公司公告沒有附完整測試資料、Marketplace 同欄口徑、供應狀態、實際部署數、訂單或財務貢獻；因此 600kW 不納入 M1 跨公司比較
independence_group: lg-electronics
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Daikin Industries
title: Daikin Holdings Singapore and Delta Electronics Sign MOU to Advance Next Generation Data Centre Cooling Solutions in Asia-Oceania Market
published_at: 2026-05-11
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.daikin.com/press/2026/20260511
locator: 正文合作範圍段落；100kW 至 3000kW rack power density、Delta In-Rack／In-Row CDU portfolio 與 Daikin grey-space 至 chip-level 整合
limitation: MOU 與 100 至 3000kW 是合作組合涵蓋範圍，不是單一 RDF106CDT5192 型號的額定容量、客戶訂單、量產數量或收入預測
independence_group: daikin
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: document
publisher: Daikin Industries
title: Daikin and NTT DATA Launch Joint Proof of Concept for AI-Driven Data Center Cooling Optimization
published_at: 2026-07-06
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.daikin.com/press/2026/20260706
locator: Overview 與 Next steps；2026-07 至 2027-03 在 NTT DATA 日本資料中心驗證，目標 FY2027 commercial deployment
limitation: PoC 仍在進行，公告未提供節電、成本、可靠度實測結果，也不能用 FY2027 目標證明目前已商用或台灣供應商已取得收入
independence_group: daikin
-->

<!-- research_source
source_id: S5
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-02 以 3017、2308、2301 重查重大訊息、法說會資料與季度財報的持續更新入口
limitation: 索引頁本身不證明 CDU 客戶、驗收、訂單、量產、收入或毛利；後續出現文件時須另建 document source
independence_group: twse-mops
-->

<!-- research_source
source_id: S6
role: other_primary
source_kind: living_index
publisher: Asia Vital Components
title: Asia Vital Components official homepage
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.avc.co/en-us/
locator: 2026-08-02 首頁 General Information；Asia Vital Components Co., Ltd、Taiwan listed company、TSE: 3017，並自稱 AVC
limitation: 只用於把 NVIDIA Marketplace 的 AVC 法律實體映射到 3017；公司首頁不證明指定 CDU 型號的客戶、訂單、出貨、收入或毛利
independence_group: avc
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: living_index
publisher: Daikin Industries
title: Daikin Global Press Releases 2026
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://www.daikin.com/press/2026
locator: 2026-08-02 的 2026 press-release 索引可定位 2026-07-06 Daikin／NTT DATA PoC 與 2026-05-11 Daikin／Delta MOU
limitation: 動態索引只供追蹤新文件；索引本身不證明 PoC 結果、商用部署或財務貢獻，命中後須另建 document source
independence_group: daikin
-->

<!-- research_source
source_id: S8
role: other_primary
source_kind: living_index
publisher: NVIDIA Marketplace
title: DSX Infrastructure for AI Factory validated CDU list — 2026-08-09 capture
published_at:
captured_at: 2026-08-09
accepted_at: 2026-08-09
status: active
url: https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/?category=liquid_to_liquid&page=1&limit=15
locator: 2026-08-09 捕捉的 Liquid to Liquid CDU 表；LGE／LGE 列為 600kW、850LPM，validation type 列出 Hydraulic Test-Constant DP／Constant Flow、Flow Sensor Accuracy、Cold Start、Thermal Test-Low Load／Nominal Capacity、Pump Failover、Pumping Capacity，Supply Chain Status 欄空白；AVC、Delta、LITEON 三列容量與狀態同 2026-08-02 capture
limitation: 動態頁沒有不可變版本與變更日誌；本 source 只支持 2026-08-09 當下可定位欄位，不把空白供應狀態解釋為 Sample Ready、MP Ready、撤銷或量產，也不提供客戶、訂單、出貨、收入、毛利或完整跨廠測試協定
independence_group: nvidia-marketplace
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: 2026-08-02 捕捉的 NVIDIA Marketplace 同一 Cooling Capacity @ 4°C ATD 欄位列出 AVC CDU1000-LTL-RW 1.2MW、Delta RDF106CDT5192 1MW 與 LITEON LC-LL-WCDU-6011(S) 380kW；Supply Chain Status 依序為 Sample Ready、MP Ready 與 Sample Ready
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-08-02
basis: S1 在捕捉日的同一張 CDU 表可直接定位三個 vendor、model、capacity 與原始供應狀態
boundary: 只證實捕捉日動態清單內容；沒有不可變外部版本，頁面改動後舊值可能無法重現，且狀態標籤不能自行轉換為客戶量產、訂單、收入、市占或獲利
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
claim: LG Electronics 表示其 600kW CDU 已通過 NVIDIA 超過 100 項技術評估標準
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-07-27
basis: S2 的 News Summary 與 Reliable Partner 段落直接提供 600kW 與超過 100 項 criteria
boundary: 公司公告沒有附完整測試結果，也不證明供應狀態、實際客戶部署、訂單、收入或獲利
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
claim: Daikin 與 Delta 的 MOU 把合作解決方案範圍描述為支援 100kW 至 3000kW rack power density，並涵蓋 Delta In-Rack 與 In-Row CDU portfolio
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-05-11
basis: S3 合作範圍段落直接列出 100kW 至 3000kW 與產品組合
boundary: 這是合作 portfolio scope，不是單一型號容量、產品完成度、訂單承諾、出貨量或財務預測
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
claim: Daikin 與 NTT DATA 的冷卻最佳化 PoC 規劃自 2026-07 執行至 2027-03，並以 FY2027 commercial deployment 為目標
supporting_source_ids: S4
contrary_source_ids:
as_of: 2026-07-06
basis: S4 的 Overview 與 Next steps 直接提供 PoC 期間及商用目標
boundary: 尚無完成結果、節電量、成本效益、正式採購或台灣供應商收入可供驗證
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
claim: 三個 NVIDIA Marketplace 容量標示因捕捉日期與欄位一致，保留原始 MW／kW 後可正規化為 kW 比較；但頁面沒有完整跨廠測試協定，額定容量也不能作為效率、產品優劣、供應商量產成熟度、訂單或財務表現排名
supporting_source_ids: S1,S2,S3,S4
contrary_source_ids:
as_of: 2026-08-02
basis: S1 提供同欄容量標示與不同供應狀態，M1 保留來源原始單位並以固定算術正規化；S2 是另一份 LG 認證公告而不混入 M1，S3 與 S4 又分別停在 MOU scope 與 PoC 時鐘
boundary: 可比 verdict 只涵蓋 NVIDIA 欄位標示的絕對額定容量，不聲稱完整測試條件相同，也不評估效率、產品優劣、市占、價格、訂單、收入、毛利或市場是否已反映；工況、備援、服務及整合能力另須驗證
verification_needed: 需平台商公布狀態定義與更新紀錄，並以客戶部署及各公司財報核對量產和經濟結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 3017、2308、2301 已因 NVIDIA CDU 列名取得具財務重大性的新增量產訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源只到 NVIDIA 平台列名、LG 認證、合作 MOU 與 PoC；未提供三家台廠客戶、數量、價格及財務貢獻
boundary: 不建立訂單金額、出貨量、市占、收入占比、毛利或客戶名的公司事實
verification_needed: 需客戶部署或驗收文件，並與三家公司法說、季報或重大訊息交叉核對具名產品、數量、收入與獲利
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Asia Vital Components 官方首頁自稱 AVC，並明列該公司為臺灣上市公司 TSE 3017
supporting_source_ids: S6
contrary_source_ids:
as_of: 2026-08-02
basis: S6 General Information 同時列出完整英文公司名、AVC 自稱與 TSE: 3017
boundary: 只完成 NVIDIA vendor 名稱到法律實體／股票代號的映射，不證明 CDU1000-LTL-RW 的客戶、訂單、出貨、收入或毛利
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
claim: 2026-08-09 捕捉的 NVIDIA Marketplace 已以可定位同表列項顯示 LGE／LGE 600kW、850LPM 與八類 validation test，Supply Chain Status 欄空白；同日 AVC 1.2MW／Sample Ready、Delta 1MW／MP Ready、LITEON 380kW／Sample Ready 的型號、容量與供應狀態未較 2026-08-02 capture 改變
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-09
basis: S8 在同一張 Liquid to Liquid CDU 表可直接定位四個 vendor、model、Cooling Capacity @ 4°C ATD、validation type 與原始 Supply Chain Status 欄
boundary: 只證實 2026-08-09 動態清單內容；空白狀態不自行補值，列名與 validation test 也不證明客戶驗收、量產訂單、收入、市占、毛利或跨廠測試結果可完全等同
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
claim: LGE 從 2026-08-02 只有公司公告的 NVIDIA validation，前進到 2026-08-09 可在 NVIDIA Marketplace 同欄定位的 600kW 列項；但平台沒有給 LGE Supply Chain Status，因此證據階梯只升到「平台列名／validation」，不能升為 MP Ready、客戶部署、訂單或財務認列
supporting_source_ids: S2,S8
contrary_source_ids:
as_of: 2026-08-09
basis: S2 是 LG 對 600kW CDU validation 的公司公告，S8 是不同發行人的 NVIDIA 平台 capture；兩條來源鏈共同支持產品與平台列名，S8 的供應狀態欄仍為空白
boundary: 兩條來源鏈降低單一公司自述風險，但不等於獨立客戶驗收；不推算 supply stage、訂單、出貨量、市占、收入、毛利或現金流
verification_needed: 持續保存 NVIDIA 欄位變化，並以具名客戶部署與 LG 財務揭露驗證量產及經濟結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 容量可以換算，商業成熟度不能跟著換算

先只做一件事：把同一天、同一張表、同一欄的容量換成相同單位。2026 年 8 月 2 日保存的
NVIDIA 清單共有三筆可比較資料；來源原值是 1.2MW、1MW、380kW，換算後是 1,200kW、
1,000kW、380kW。這個比較在查核帳本中記為 `M1`。

`M1` 只能回答「清單在那一天標示的額定容量誰大誰小」。頁面沒有公布完整跨廠測試程序，
所以它不能回答效率、產品優劣、驗證種類、供應準備、客戶訂單或財務表現。LG 的 600kW
當時只出現在另一份公司公告，來源欄位不同，因此不放進這張表硬比。

| 2026-08-02 清單中的供應商 | 產品型號 | 來源原始容量 | 換算成 kW | 平台原始供應標籤 | 這一列只能證明 |
|---|---|---:|---:|---|---|
| AVC／奇鋐（3017；S6 映射） | CDU1000-LTL-RW | 1.2MW | 1,200kW | Sample Ready | 同欄容量與平台列名 |
| Delta／台達電（2308） | RDF106CDT5192 | 1MW | 1,000kW | MP Ready | 同欄容量與平台列名 |
| LITEON／光寶科（2301） | LC-LL-WCDU-6011(S) | 380kW | 380kW | Sample Ready | 同欄容量與平台列名 |

<!-- metric_comparison
comparison_id: M1
comparison_kind: aligned_metric
observation_id: M1-O1
claim_id: C1
entity: AVC
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 1.2
value_kind: point
period_start: 2026-08-02
period_end: 2026-08-02
period_basis: point_in_time_nvidia_marketplace_capture
unit: MW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的來源顯示值；只表示頁面在捕捉日標示的額定容量，不代表完整跨廠測試協定相同
evidence_ids: S1
comparability: normalized_comparable
comparability_reason: 三筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: reported_MW_multiply_by_1000_using_1MW_equals_1000kW
normalized_value: 1200
normalized_unit: kW
normalized_period_start: 2026-08-02
normalized_period_end: 2026-08-02
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

2026 年 8 月 9 日的新快照另建 `M2`，不覆寫 `M1`。`M2` 加入新出現的 LGE 同欄列項，
並重新保存當日四筆來源值；它仍只表示同日同欄的容量可以換算，不是商業成熟度排名。

<!-- metric_comparison
comparison_id: M2
comparison_kind: aligned_metric
observation_id: M2-O1
claim_id: C8
entity: AVC
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 1.2
value_kind: point
period_start: 2026-08-09
period_end: 2026-08-09
period_basis: point_in_time_nvidia_marketplace_capture
unit: MW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的 2026-08-09 來源顯示值；只表示捕捉日額定容量，不代表完整跨廠測試協定相同
evidence_ids: S8
comparability: normalized_comparable
comparability_reason: 四筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: reported_MW_multiply_by_1000_using_1MW_equals_1000kW
normalized_value: 1200
normalized_unit: kW
normalized_period_start: 2026-08-09
normalized_period_end: 2026-08-09
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: aligned_metric
observation_id: M2-O2
claim_id: C8
entity: Delta
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 1
value_kind: point
period_start: 2026-08-09
period_end: 2026-08-09
period_basis: point_in_time_nvidia_marketplace_capture
unit: MW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的 2026-08-09 來源顯示值；只表示捕捉日額定容量，不代表完整跨廠測試協定相同
evidence_ids: S8
comparability: normalized_comparable
comparability_reason: 四筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: reported_MW_multiply_by_1000_using_1MW_equals_1000kW
normalized_value: 1000
normalized_unit: kW
normalized_period_start: 2026-08-09
normalized_period_end: 2026-08-09
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: aligned_metric
observation_id: M2-O3
claim_id: C8
entity: LITEON
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 380
value_kind: point
period_start: 2026-08-09
period_end: 2026-08-09
period_basis: point_in_time_nvidia_marketplace_capture
unit: kW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的 2026-08-09 來源顯示值；只表示捕捉日額定容量，不代表完整跨廠測試協定相同
evidence_ids: S8
comparability: normalized_comparable
comparability_reason: 四筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: identity_conversion_reported_kW_equals_normalized_kW
normalized_value: 380
normalized_unit: kW
normalized_period_start: 2026-08-09
normalized_period_end: 2026-08-09
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: aligned_metric
observation_id: M2-O4
claim_id: C8
entity: LGE
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 600
value_kind: point
period_start: 2026-08-09
period_end: 2026-08-09
period_basis: point_in_time_nvidia_marketplace_capture
unit: kW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的 2026-08-09 來源顯示值；只表示捕捉日額定容量，不代表完整跨廠測試協定相同
evidence_ids: S8
comparability: normalized_comparable
comparability_reason: 四筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: identity_conversion_reported_kW_equals_normalized_kW
normalized_value: 600
normalized_unit: kW
normalized_period_start: 2026-08-09
normalized_period_end: 2026-08-09
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: aligned_metric
observation_id: M1-O2
claim_id: C1
entity: Delta
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 1
value_kind: point
period_start: 2026-08-02
period_end: 2026-08-02
period_basis: point_in_time_nvidia_marketplace_capture
unit: MW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的來源顯示值；只表示頁面在捕捉日標示的額定容量，不代表完整跨廠測試協定相同
evidence_ids: S1
comparability: normalized_comparable
comparability_reason: 三筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: reported_MW_multiply_by_1000_using_1MW_equals_1000kW
normalized_value: 1000
normalized_unit: kW
normalized_period_start: 2026-08-02
normalized_period_end: 2026-08-02
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: aligned_metric
observation_id: M1-O3
claim_id: C1
entity: LITEON
metric: NVIDIA Marketplace Cooling Capacity at 4C ATD
reported_value: 380
value_kind: point
period_start: 2026-08-02
period_end: 2026-08-02
period_basis: point_in_time_nvidia_marketplace_capture
unit: kW
definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd
definition: NVIDIA Marketplace 同一欄 Cooling Capacity @ 4°C ATD 的來源顯示值；只表示頁面在捕捉日標示的額定容量，不代表完整跨廠測試協定相同
evidence_ids: S1
comparability: normalized_comparable
comparability_reason: 三筆資料來自同日同表同欄，但原始單位含 MW 與 kW；只在固定單位換算後比較欄位標示容量，不比較效率、完整工況、供應狀態或財務
normalization_method: identity_conversion_reported_kW_equals_normalized_kW
normalized_value: 380
normalized_unit: kW
normalized_period_start: 2026-08-02
normalized_period_end: 2026-08-02
normalized_definition_key: nvidia_marketplace_cooling_capacity_at_4c_atd_normalized_kw
-->

## 為什麼值得持續追蹤

市場現在不只問「有沒有液冷產品」，還問產品走到哪一關。NVIDIA 清單讓不同供應商的容量與
原始供應標籤出現在同一個查核框架；LG 的驗證公告、Daikin／Delta 的合作範圍，以及
Daikin／NTT DATA 的概念驗證，則提醒讀者：產業價值不只在一台設備的 kW，還包括設施端冷卻、
伺服器端冷卻、控制整合與長期運作。研究中心因此沿著五關追蹤，不做單純的容量排行榜。

## 從規格到收入要過五關

先判斷眼前資料在回答哪一問，再看它還缺什麼。容量、準備進度與商業結果是不同的尺，不能
把前一關的數字直接帶到下一關。

| 先問哪一關 | 這一關能回答什麼 | 本輪已有的公開證據 | 仍然缺什麼 |
|---|---|---|---|
| 1. 容量規格 | 設備在指定條件下設計可帶走多少熱 | NVIDIA 同日同欄的三筆容量，對應 M1 | 完整跨廠測試程序、實際資料中心工況、全生命週期效率與可靠度 |
| 2. 平台列名與測試 | 產品是否出現在清單，以及完成哪一類平台測試 | NVIDIA 清單列出 AVC、Delta、LITEON；LG 另稱 600kW 設備通過超過 100 項條件 | LG 當時是否採同欄定義、完整門檻、各項分數，以及產品是否都走相同流程 |
| 3. 供應準備 | 平台在捕捉日給產品哪一個原始供應標籤 | Delta 為 MP Ready；AVC、LITEON 為 Sample Ready | 標籤對應的產能、良率、庫存、交期與客戶承諾；LG 當時沒有可重現狀態 |
| 4. 場域整合與客戶部署 | 系統是否在接近真實或真實場域運作，並走向驗收 | Daikin／Delta 規劃 100 至 3000kW 產品範圍；Daikin／NTT DATA 概念驗證預計至 2027 年 3 月 | 節電、成本、可用率、商用接受度，以及具名客戶是否完成驗收 |
| 5. 公司收入 | 產品是否帶來訂單、收入、毛利與現金流 | 尚無可重算證據 | 3017、2308、2301 的具名設備訂單、收入占比、毛利、現金流與投資回收 |

只有第一關的 `M1` 容量完成「換成相同單位後可比」判定。平台的兩種供應標籤沒有公開的共同
量產率或財務定義，因此本文不把它們換算成成熟度分數；公司端也沒有同產品、同期間、同會計
定義的數字，所以不能比較誰更接近收入。

## 什麼情況會讓容量排行榜失真

- **客戶可能要的是模組化與維修能力**：客戶可能依機櫃或整排配置採多台設備，而不是選單台最大容量；流量、壓差、泵浦備援、材料相容性、占地與維修時間都可能更重要。
- **平台通過測試不保證快速轉單**：LG 已公告超過 100 項驗證，但公告沒有同欄容量定義、平台供應狀態、客戶或訂單；這不是否定驗證，而是說不同來源的欄位不能互相代填。
- **價值可能落在整套控制與設施端**：Daikin／NTT DATA 正驗證空調、冰水主機與液冷的整合控制。若節能與可靠度主要來自控制軟體或設施端設備，只看 CDU 容量會錯估價值分配。
- **合作範圍不等於已完成產品**：Daikin／Delta 規劃的 100 至 3000kW 是合作備忘錄中的產品範圍，不能拿來覆蓋 NVIDIA 對 Delta 單一型號的 1MW 額定值，也不能當成未來收入預測。

## 來源與證據邊界

- [S1：NVIDIA Marketplace DSX Infrastructure 動態清單](https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/)（2026-08-02 capture；頁面沒有不可變版本，後續須另留新 capture）。
- [S2：LG 600kW CDU NVIDIA validation 公告](https://www.lg.com/global/newsroom/news/eco-solution/lg-electronics-earns-nvidia-ai-factory-validation-for-its-600kw-coolant-distribution-unit/)（官網日期 2026-07-27）。
- [S3：Daikin／Delta 下一代資料中心冷卻 MOU](https://www.daikin.com/press/2026/20260511)（2026-05-11）。
- [S4：Daikin／NTT DATA 冷卻最佳化 PoC](https://www.daikin.com/press/2026/20260706)（2026-07-06）。
- [S5：公開資訊觀測站持續更新入口](https://mops.twse.com.tw/mops/web/index)。
- [S6：AVC 官方首頁的 Asia Vital Components／TSE 3017 映射](https://www.avc.co/en-us/)。
- [S7：Daikin 2026 新聞稿索引](https://www.daikin.com/press/2026)。
- [S8：NVIDIA Marketplace DSX Infrastructure 動態清單](https://marketplace.nvidia.com/en-us/enterprise/dsx-infrastructure/)（2026-08-09 capture；LGE 已有可定位 600kW 列項，供應狀態欄空白）。

**可證實：** 同日同欄的容量、平台原始供應標籤、LG 自述驗證、合作備忘錄範圍與概念驗證時程。

**待驗證：** 平台狀態的精確判準、具名客戶、部署數、訂單、收入、毛利、現金流與實際
節能結果。合作名單、平台列名或額定 kW 不得替代這些公司層級證據。

## 8 月 9 日複核：LG 進入清單，但供應階段仍空白

- `T1` 預先登錄的觸發條件已命中：LGE 從公司公告中的驗證資訊，前進到 NVIDIA 清單可定位的
  600kW／850LPM 列項；但原始供應狀態欄仍空白，不能代填成 `Sample Ready` 或 `MP Ready`。
- AVC、Delta、LITEON 的原列型號、容量與供應狀態未變；`M1` 保留 2026 年 8 月 2 日三筆歷史
  快照，`M2` 另存 8 月 9 日四筆同欄觀測。
- 新證據只把 LGE 推到「平台列名／validation」；客戶部署、訂單、量產、收入與獲利仍沒有
  可重算證據。下一輪改由 `T4` 追蹤原始欄位變化。

## 影響路由

<!-- impact
group_id: thermal
stock_ids: 3017
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-09
rationale: NVIDIA 2026-08-02 capture 直接列出 AVC CDU1000-LTL-RW、1.2MW 與 Sample Ready，S6 把 AVC 映射到 TSE 3017，可作平台資格與狀態監測起點
evidence_boundary: 法律實體映射與平台列名只到捕捉日原始狀態；不證明奇鋐具名客戶、量產數量、訂單、收入占比、市占或毛利
-->

<!-- impact
group_id: powersupply
stock_ids: 2308,2301
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-09
rationale: NVIDIA capture 分別列出 Delta RDF106CDT5192 1MW／MP Ready 與 LITEON LC-LL-WCDU-6011(S) 380kW／Sample Ready，Daikin MOU另提供台達整合範圍
evidence_boundary: 平台列名、狀態與 MOU 都不證明台達電或光寶科具名客戶、量產出貨、訂單、收入、市占、毛利或現金流
-->

## 持續驗證清單

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C1,C5
metric: NVIDIA CDU 型號、同欄額定容量、validation type 與 Supply Chain Status 變化
source_ids: S1
watch_source_ids: S1
frequency: weekly
frequency_detail: 每週保存一次 Marketplace 表格 capture；重大產品或資格更新時提前
next_check: 2026-08-09
trigger: AVC、Delta、LITEON 的型號、容量、validation type 或供應狀態改變，Sample Ready 轉階段，或 LGE 以可定位欄位正式出現
invalidation: NVIDIA 移除型號、撤回資格、重新定義 4°C ATD 欄位，或同一型號容量被重編；屆時保留舊 observation 並追加新比較，不覆寫 M1
retired_at: 2026-08-09
retirement_reason: 預先登錄的 LGE 可定位列項 trigger 已命中；新增 S8、C8、C9 與 M2 保存 2026-08-09 capture，後續欄位變化改由 T4 接續
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C6
metric: 台廠 CDU 客戶驗收、量產出貨與財務認列
source_ids: S1,S3,S6
watch_source_ids: S5
frequency: quarterly
frequency_detail: 每季法說、財報與重大訊息發布後逐公司核對
next_check: 2026-08-14
trigger: 3017、2308 或 2301 首次把具名 CDU 型號連到客戶驗收、量產數量、收入及毛利
invalidation: 公司明確表示指定 CDU 專案取消、沒有相關訂單／收入或退出該產品；到期只有平台列名、MOU 或整體液冷敘事時維持 C6 待驗證，不視為反證
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C3,C4,C5
metric: Daikin／Delta 系統整合與 Daikin／NTT DATA PoC 的節電、成本、可靠度及商用階段
source_ids: S3,S4
watch_source_ids: S7
frequency: event_driven
frequency_detail: Daikin 新聞稿、PoC 里程碑或 FY2027 商用更新出現時重查
next_check: 2026-09-30
trigger: PoC 公布可重算的基線、節電、成本或可靠度結果，或正式商用部署、客戶採購與部署範圍
invalidation: Daikin／NTT DATA 官方宣告 PoC 失敗、取消或延後超過 2027-03，或結果顯示整合控制沒有改善預先定義指標；沒有公開結果只維持待驗證並觸發 freshness downgrade
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C8,C9
metric: NVIDIA CDU 型號、同欄額定容量、validation type 與 Supply Chain Status 的後續變化
source_ids: S8
watch_source_ids: S8
frequency: weekly
frequency_detail: 每週保存一次 Marketplace 表格 capture；重大產品、資格或供應狀態更新時提前
next_check: 2026-08-16
trigger: AVC、Delta、LITEON、LGE 的型號、容量、validation type 或原始供應狀態改變，空白狀態取得平台明示值，或新增 universe 供應商的可定位列項
invalidation: NVIDIA 移除型號、撤回資格、重新定義 4°C ATD 欄位，或同一型號容量被重編；屆時保留 M1／M2，另建新 comparison，不回寫歷史 capture
-->

## 接下來看到什麼，判定才會改變

- **平台欄位改變**：若 NVIDIA 改寫 AVC、LITEON 或 LGE 的原始供應狀態，就追加新快照、來源與觀測；不得修改 `M1` 的 2026 年 8 月 2 日歷史紀錄。
- **公司補上商業證據**：3017、2308、2301 若在法說或財報同時揭露具名設備的客戶驗收、量產數量、收入占比與毛利，才可從平台列名前進到公司級商業證據。
- **概念驗證交付結果**：Daikin／NTT DATA 若公布結果，需有可重算的節電、成本或可靠度基線；官方宣告失敗、取消或延後超過 2027 年 3 月才構成反證，沒有公開結果只維持待驗證。
- **容量與收入走出相反順序**：若較高容量型號長期停留送樣，而較低容量型號先取得部署與收入，就會直接否定「容量可代表商業成熟度」的市場捷徑。
- **容量欄位定義改變**：若 NVIDIA 改變 `Cooling Capacity @ 4°C ATD` 定義，或顯示不同型號不能共用同一欄位，`M1` 的可比結論只保留在 2026 年 8 月 2 日快照，不外推到新版清單。
