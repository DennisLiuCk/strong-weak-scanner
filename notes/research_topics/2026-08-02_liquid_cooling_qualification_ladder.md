# 液冷設備不能只比容量：平台列名、供應準備與收入是三種不同證據

<!-- research_topic
topic_id: MI-2026-08-02-LIQUID-COOLING-QUALIFICATION-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-27
last_reviewed_at: 2026-08-14
review_due: 2026-08-16
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
thesis_claim_id: C21
base_confidence: medium
confidence_basis: NVIDIA 動態清單在捕捉日以同一欄標示三個型號的額定容量與供應狀態，容量保留原始 MW／kW 後可正規化比較；另有 LG 與 Daikin 一手文件補充認證、合作及 PoC 階段。台達管理層已提供公司液冷產品族約占 2025 年合併營收 10% 的近似分子，但 Marketplace 沒有固定版本與完整跨廠測試協定，三家台廠的具名 CDU 客戶、出貨量、產品收入及毛利仍未證實
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
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: older_ocp_document_added_as_operating_envelope_and_reliability_decoder_no_thesis_clock_refresh
evidence: sources:S9
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_three_performance_scorecards_and_typed_telemetry_context_no_thesis_change
evidence: sources:S9,S10
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_fluid_specific_capacity_and_qualification_branch_without_thesis_clock_refresh
evidence: sources:S9,S11,S12,S13
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: q2_financial_denominator_evidence_reframed_thesis_from_platform_listing_to_named_model_bridge
evidence: sources:S14,S15,S16,S17,S18
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **液冷**：用液體把伺服器產生的熱帶走。它是一整套散熱方式，可能包含冷板、管路、泵浦、熱交換器、控制系統與機房冷卻設備，不等於只買一台 CDU。
- **CDU（Coolant Distribution Unit）**：冷卻液分配單元，透過泵浦、熱交換器與控制系統，把伺服器迴路的熱帶走。它不是 GPU 上的冷板，也不等於機房產生冷水的 chiller。
- **額定容量**：設備在指定測試條件下，設計上可帶走的熱量。它回答「能處理多少熱」，不回答效率、可靠度、客戶採用或公司收入。
- **MW／kW**：兆瓦／千瓦，都是功率單位；`1MW = 1000kW`。換成同一單位後只能比較數值大小，不能順便比較產品成熟度。
- **Cooling Capacity @ 4°C ATD**：NVIDIA 清單以這個欄名標示 CDU 的額定排熱能力。MW／kW 是絕對容量，不是效率或產品優劣；同欄數字可在單位換算後比較，但頁面沒有公布完整跨廠測試協定，實際水溫、流量、壓差與備援仍會改變可用能力。
- **ATD（Approach Temperature Difference）**：熱交換兩側在指定位置的溫差條件。本文只沿用 NVIDIA 欄名中的 `4°C ATD`，不自行補上頁面未公布的完整測試程序。
- **L-L CDU（Liquid-to-Liquid CDU）**：兩側都以液體循環換熱的 CDU；一側接機房設施水路，另一側接伺服器冷卻水路。這個名稱說明架構，不代表已通過哪一套驗證。
- **L-A／L2A（Liquid-to-Air）**：伺服器端以液體帶熱，再把熱排到空氣側的架構。它和 L-L／L2L 是不同產品分支；公司只說「液冷產品」時，不能自行判定收入來自哪一支。
- **FWS／TCS**：FWS 是設施水系統，負責把熱送往機房冷源；TCS 是技術冷卻系統，負責把熱從伺服器帶回 CDU。兩側各自的溫度、流量與壓力都會限制實際工作點。
- **操作包絡線（Operating envelope）**：設備可安全、穩定運作的一組條件範圍，例如冷卻液種類、進水溫度、流量、壓力與負載。單一 kW 額定值只是這個範圍中的一個截面。
- **熱性能曲線（Thermal performance curve）**：在指定流體、FWS／TCS 流量與進水溫度下，把 ATD 和可帶走熱負載畫成曲線。它回答「這組熱條件可支撐多少 kW」，不是供應商總分。
- **PQ 曲線（Pressure–flow curve，壓力－流量曲線）**：把流量與壓力或壓差畫在同一張圖。CDU 的 TCS 側用它看泵浦能否克服二次水路阻力；FWS 側用它看設備會對機房一次水路形成多少阻力。
- **TCS 壓頭（TCS pressure head）**：CDU 二次側泵浦在指定流量下能提供的壓力能力。壓頭要大到克服管路、接頭、分流器與冷板的壓降，但數字較大不自動代表效率、可靠度或產品較好。
- **FWS 流動阻抗（FWS flow impedance）**：設施水流過 CDU 一次側時遇到的阻力。機房必須能供應所需溫度、流量與壓力；若設備需求超過現場水力能力，名牌容量就不一定能落地。
- **量測身分證（Typed measurement context）**：讓一筆讀值帶著「哪台設備、哪一側／哪個位置、量的是什麼、使用什麼單位」的上下文。只看數字而沒有這些欄位，可能把一次側入口和二次側回水混在一起。
- **時間戳與品質旗標（Timestamp／quality）**：時間戳說明讀值何時產生；品質旗標說明系統當下是否把讀值視為健康可用。`quality=1` 不是儀表已完成校正或產品通過資格驗證，只是資料契約中的讀值健康狀態。
- **感測值／設定值／動作請求**：感測值描述設備實際量到什麼；設定值是控制目標；動作請求則要求 BMS 執行某個控制。NVIDIA 文件要求外部請求先經安全限制判斷，不能把「收到命令」當成「設備已安全執行」。
- **DSX Exchange**：NVIDIA 用來讓建築管理系統與 IT 軟體交換設施資料、狀態與控制請求的資料契約。它規定訊息怎麼被辨識與傳遞，不取代 BMS、感測器校正、CDU 性能測試或場域驗收。
- **processArea（量測位置上下文）**：DSX metadata 用來區分同一設備內不同位置或功能的欄位；例如同一台 CDU 的一次側入口、一次側出口、二次側供水與二次側回水。它是位置標籤，不是量測結果。
- **資格驗證包（Qualification evidence packet）**：把測試對象、版本、條件、原始資料、通過／失敗結果與限制一起保存的證據集合。只有測試名稱而沒有這些內容，不能重現結果。
- **水壓與環境可靠度測試**：水壓測試檢查承壓時是否洩漏或變形；運輸衝擊、振動、溫濕度與熱循環則檢查搬運及環境變化下的耐受性。通過其中一項不等於完整系統已通過所有驗證。
- **Revision（修訂版）**：文件更新後的版本名稱。本文引用 Revision 1.0，只代表這份 OCP 方法文件的版本，不等於產品認證等級。
- **流量**：冷卻液在一定時間內通過管路的體積；常見單位是每分鐘公升。流量會影響帶熱能力，但不能單獨代表整套系統效能。
- **壓差**：冷卻液流過管路與元件前後的壓力差。壓差過大可能提高泵浦負擔，因此容量相同的設備仍可能有不同整合條件。
- **備援**：主要泵浦、電源或控制元件失效時，由另一組元件接手。額定容量沒有說明設備在故障情境下還能維持多少能力。
- **材料相容性**：冷卻液、金屬、密封件與管路長期接觸時是否會腐蝕、膨潤或產生污染。它是部署條件之一，不會由 kW 數字直接回答。
- **水基冷卻液（Water-based heat transfer fluid）**：以經處理的水為主要傳熱介質，並依指定材料、化學處理與監測條件使用。它不是「任何自來水都可直接灌入」，也不能把同一組水質門檻套到丙二醇配方。
- **PG25／PG55**：OCP 2022 丙二醇指引中的兩個配方範圍；PG 是 propylene glycol，數字約指丙二醇體積百分比等級。本文保留文件的合格範圍，不把 `25` 或 `55` 當成所有產品都恰好等於的單點濃度。
- **體積百分比（vol %）**：某成分體積占混合液總體積的比例。它和重量百分比不是同一單位，不能不經密度與定義核對就互換。
- **凝固點（Freeze point）**：流體開始結凍的溫度條件。它是配方選擇的一項邊界，不等於冷卻能力、泵浦功耗、腐蝕壽命或設備容量總分。
- **折射計（Refractometer）**：以折射特性估算丙二醇濃度的現場工具；要使用適合該流體與濃度範圍的量測設定。讀到濃度仍不代表全部抑制劑、污染與材料相容性都合格。
- **緩蝕劑／儲備鹼度（Corrosion inhibitor／reserve alkalinity）**：緩蝕劑用來降低接液金屬腐蝕；儲備鹼度描述流體抵抗酸化的緩衝能力之一。兩者都要依配方、材料與供應商程序判讀，不能看到單一數字就自行加藥。
- **抑菌狀態（Biostatic）**：流體條件能抑制微生物增長，不等於無菌。OCP 丙二醇文件只在濃度維持於指定條件時給出這項判讀，不能擴寫成所有 PG 迴路永遠不需微生物監測。
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
- **分子／分母**：分子是要衡量的那一塊，例如液冷產品收入；分母是比較基準，例如同期間合併營收。只有分子、分母、期間與合併範圍都對齊，占比才有可查核意義。
- **產品族（Product family）**：一組相關產品的合計範圍，可能同時含冷板、風扇、泵浦、CDU 或不同 L2A／L2L 架構。產品族占比不能直接分配給其中一個型號。
- **部門代理（Segment proxy）**：公司只公布大部門數字時，用來框住題材可能落在哪個上限範圍。部門通常還包含許多非液冷產品，因此不是液冷收入分子。
- **Infrastructure（基礎設施事業）**：台達正式部門之一，範圍包含資通訊基礎設施、能源基礎設施與顯示器等多種業務。法說表示其中含液冷，但不能把整個部門都算成液冷收入。
- **DDP（Delivered Duty Paid，完稅後交貨）**：ICC Incoterms 規則下，賣方負責把貨物送到約定目的地、辦妥進口清關並承擔到該地點的成本與風險。它是交貨責任，不是產品毛利率；管理層若說 DDP 改變報表毛利呈現，仍要和產品售價、成本及淨利分開讀。
- **PoC（Proof of Concept，概念驗證）**：在真實或接近真實的環境做小規模試行，用來確認方案可行。**PoC 進行中不等於已交付節電、成本或可靠度數字**，本文多處出現的 PoC 都停在這個階段。
- **MOU（合作備忘錄）**：合作方對預計合作範圍的書面表達。它不是已完成產品、採購合約、出貨或收入證據。
- **Portfolio（產品組合）**：一家公司或合作案規劃涵蓋的一組產品。範圍可大於單一型號，不能拿整組規劃覆蓋某台設備的額定數字。
- **AVC／奇鋐（3017）**：AVC 是 Asia Vital Components 的縮寫；本文用公司官網的 `TSE: 3017` 完成名稱映射。這只確認公司身分，不證明具名客戶或收入。
- **Delta／台達電（2308）與 LITEON／光寶科（2301）**：本文以英文公司名出現的兩家台灣電源與散熱供應商，都是本 universe 成員。台達另有公司液冷產品族的近似營收占比；這仍不等於 NVIDIA 清單中的具名 CDU 已取得客戶訂單、出貨量或產品毛利，光寶目前也只有平台列名與廣泛部門範圍。
- **LGE／LG Electronics**：LG 電子的英文縮寫。2026-08-09 的 NVIDIA 清單可定位其 600kW 列項，但供應狀態欄空白，因此不能替它補成任何階段。
- **CDU1000-LTL-RW／RDF106CDT5192／LC-LL-WCDU-6011(S)**：分別是 AVC、Delta 與 LITEON 在 NVIDIA 清單中的 CDU 型號。型號只是辨識產品的名字；容量、供應狀態與量產證據仍要分欄閱讀。
- **TSE（Taiwan Stock Exchange，臺灣證券交易所）**：本文只用公司官網的 `TSE: 3017` 把 AVC 對應到臺灣上市公司奇鋐；這個代號本身不證明該 CDU 的客戶或收入。
- **FY2027（2027 財政年度）**：公司的 2027 會計年度，起訖日不一定等於 2027 曆年。本文引用的是 Daikin 的商用目標時間，不是目前已完成部署。

### 三句話抓重點

- 2026 年 8 月 2 日保存的 NVIDIA 清單，在同一欄列出三個供應商型號的容量：1.2MW、1MW 與 380kW。把單位都換成 kW 後，這三個數字可以比較。
- 容量只回答設備在指定條件下設計可帶走多少熱；還要把熱性能曲線、TCS 壓頭、FWS 阻抗，以及每筆讀值的設備、位置、單位、時間與品質接起來，才知道這個數字落在什麼操作包絡線。平台列名與供應標籤也都不等於客戶已部署。
- 台達管理層已把「液冷產品」連到 2025 年約占合併營收 10% 的公司層級分子，但沒有拆成 L2A／L2L、具名 CDU、客戶、數量或產品毛利；其餘兩家季報的部門範圍也更廣。因此仍不能用容量大小替公司排行。

### 為什麼重要

液冷題材最容易把不同關卡混成一張排行榜。讀這篇時先拆成五問：額定值是在什麼冷卻液、
溫度、流量與壓力下量到？產品與整機通過哪些可靠度測試？供應準備到哪一步？客戶是否真的
部署並驗收？公司是否已把交易認列為收入？

容量只回答第一問的一個截面，平台欄位只回答中間幾問的一部分；最後兩問仍要靠客戶與公司
資料。把五關分開，才不會看到 1MW 就推論某家公司一定比 380kW 的供應商更成熟或賺得更多。

### 接下來怎麼追

- 每週保存 NVIDIA 清單的型號、額定容量、驗證類別與原始供應標籤；只記錄欄位怎麼變，不自行替空白欄位補答案。
- 查 3017、2308、2301 的重大訊息、法說與季報；對台達先追「液冷產品族」如何拆成 L2A／L2L 與具名 CDU，等公司把型號連到客戶驗收、量產數量、實際收入及毛利，才把證據推進到產品層。
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

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: Open Compute Project
title: Liquid to Liquid CDU Test Methodology and Performance Rating, Revision 1.0
published_at: 2024-11-01
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.opencompute.org/documents/ocp-wp-l-lcdu-test-methodology-performance-rating-r1-pdf
locator: PDF pp. 15–19 的 ingredient-level／system-level qualification、性能參數與建議 rating；pp. 20–22 的材料相容性、水壓、衝擊／振動、熱循環及法規文件要求
limitation: 這是 OCP 提出的通用測試與性能溝通方法，不是所有平台或客戶強制採用的共同認證；封面標示 August 2024，版本表另記錄 2024-11-01 initial release，本文保留版本表日期並揭露差異。文件不證明 NVIDIA 清單中的任何型號依這套方法通過，也不提供客戶、訂單、出貨、收入、市占或毛利
independence_group: opencompute-cdu
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: living_index
publisher: NVIDIA
title: DSX Exchange BMS Integration Companion Guide
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://docs.nvidia.com/dsx-exchange/bms-integration
locator: 2026-08-12 Object Types and Point Types、processArea、Metadata／Value Publication、Integration-Published Points 與 FAQ；CDU 可發布 LiquidTemperature、LiquidDifferentialPressure、LiquidFlow、LiquidPressure 等點位，primary／secondary 位置以 processArea 區分，value 帶 timestamp 與 quality，外部 setpoint／action request 由 BMS 套用 guardrails
limitation: 動態技術頁定義資料與控制交換契約，不要求每個場域發布所有點位，也不證明感測器校正精度、熱平衡、具名 CDU 的性能曲線、site commissioning、field reliability、客戶驗收或財務貢獻
independence_group: nvidia-dsx-docs
-->

<!-- research_source
source_id: S11
role: standard
source_kind: document
publisher: Open Compute Project
title: Guidelines for Using Propylene Glycol-Based Heat Transfer Fluids in Single-Phase Cold Plate-Based Liquid Cooled Racks
published_at: 2022-10-03
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/guidelines-for-using-propylene-glycol-based-heat-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf
locator: PDF pp. 6–10 的 TCS scope、PG25／PG55 配方與腐蝕測試；pp. 13–21 的過濾、啟動、濃度／凝固點監測、調整與 records
limitation: 這是 2022 年丙二醇基單相冷板 TCS 指引；published_at 採共同作者公開 publication listing 的日期，PDF 正文沒有獨立批准日。文件的 PG25／PG55 範圍、測試與維護條件不是水基、介電液、FWS 或所有客戶的通用門檻，也沒有比較熱傳、泵功、成本、產品 qualification 或具名場域結果
independence_group: open-compute-project
-->

<!-- research_source
source_id: S12
role: standard
source_kind: document
publisher: Open Compute Project
title: Guidelines for Using Water-Based Transfer Fluids in Single-Phase Cold Plate-Based Liquid-Cooled Racks
published_at: 2022-10-03
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/guidelines-for-using-water-based-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf
locator: PDF pp. 5–9 的 water-based TCS scope、典型水質與微生物欄位；pp. 12–20 的過濾、啟動、監測、調整與 records
limitation: 這是 2022 年水基、非 PG 單相冷板 TCS 指引；數值需依專案風險與 treatment plan 客製，不能套用到 PG、介電液、FWS 或所有平台。文件沒有比較兩種流體的熱傳效率、泵功、成本、產品 qualification 或具名場域結果
independence_group: open-compute-project
-->

<!-- research_source
source_id: S13
role: standard
source_kind: living_index
publisher: Open Compute Project
title: Cold Plate Sub-Project — Coolant Fluids workstream and accepted contributions
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate
locator: 2026-08-14 capture 的 Active Workstreams 與 Accepted Contributions；Coolant Fluids 分列單相 glycol-based、單相 water-based 與 two-phase，頁面另列 July 2024 water draft、November 2025 updated PG draft，以及兩份 2022 accepted contributions
limitation: 動態工作頁只支持捕捉日的工作流與版本地圖；draft 標題不等於正式發布或已採用，本文沒有讀取 Google Drive 草案內容，也不把工作流存在改寫成產品通過、跨流體等效、場域採用或財務證據
independence_group: open-compute-project
-->

<!-- research_source
source_id: S14
role: management_commentary
source_kind: document
publisher: Delta Electronics
title: Delta Electronics 2Q 2026 Results Meeting Transcript
published_at: 2026-07-30
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://filecenter.deltaww.com/IR/download/calendar/2Q26_Transcript.pdf
locator: PDF pp. 2、4、12；03:06 的事業成長說明、09:48 的 DDP 毛利呈現說明，以及 55:45–56:19 的 liquid-cooling products 約占 2025 年營收 10%／2026 年預期超過 12% 與 L2A／L2L 回答；下載檔 SHA-256 1d3cf7fb34d23713300c694b86e0af732115eb937b24996b649591aad107916b
limitation: 公司製作的英文逐字稿明示僅供參考、中文原音為準；10% 是管理層對 2025 年液冷產品族的近似說法，超過 12% 是 2026 年預期而非已實現結果，兩者都未拆出 L2A、L2L、具名 CDU、客戶、出貨量、金額或產品毛利。DDP 說明涉及報表呈現且管理層稱不影響淨利，不能改寫成產品毛利改善
independence_group: delta-electronics
-->

<!-- research_source
source_id: S15
role: company_filing
source_kind: document
publisher: Delta Electronics
title: 115 年第二季合併財務報告
published_at: 2026-07-29
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=2308&filename=202602_2308_AI1.pdf
locator: PDF pp. 89–90 的部門資訊與產品範圍；MOPS 索引檔名 202602_2308_AI1.pdf、115/07/29 16:26:39、1,808,979 bytes；下載檔 SHA-256 838b88e3b21639a122a4cdd88d87fe1bb3b185592d603184d65e5a955402ed08
limitation: 申報附件把電源及零組件、基礎設施等廣泛部門分開，但沒有單列液冷、L2A、L2L 或 RDF106CDT5192 的收入、數量與毛利；MOPS 索引 N=3 全數命中只證明指定三家公司附件可取得，不代表全部公司、全部 IR 文件或產品歸因皆完整
independence_group: delta-electronics
-->

<!-- research_source
source_id: S16
role: company_filing
source_kind: document
publisher: LITE-ON Technology
title: 115 年第二季合併財務報告
published_at: 2026-07-31
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=2301&filename=202602_2301_AI1.pdf
locator: PDF pp. 67–68 的雲端及物聯網部門範圍；MOPS 索引檔名 202602_2301_AI1.pdf、115/07/31 19:27:54、1,868,258 bytes；下載檔 SHA-256 ea26c644fb6e0f5ecc5029fca228c37dd878bf41982d043287ccf5b05f10213e
limitation: 雲端及物聯網部門同時包含資料中心、伺服器、網通、AI、物聯網、智慧裝置與影像等多種業務，沒有單列 LC-LL-WCDU-6011(S)、液冷收入、出貨量或產品毛利；部門數字不能直接當成液冷分子
independence_group: liteon-technology
-->

<!-- research_source
source_id: S17
role: company_filing
source_kind: document
publisher: Asia Vital Components
title: 115 年第二季合併財務報告
published_at: 2026-08-12
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=3017&filename=202602_3017_AI1.pdf
locator: PDF pp. 50–51 的部門資訊；MOPS 索引檔名 202602_3017_AI1.pdf、115/08/12 16:00:26、893,656 bytes；下載檔 SHA-256 418df6e7296a62f0e324fa71ba4325923dc7eba9b08b78250d8f98903f639746
limitation: 申報附件依海外與綜合管理等營運／地域性質呈現部門，沒有單列 CDU1000-LTL-RW、液冷收入、出貨量或產品毛利；部門分類不能直接當成液冷分子
independence_group: asia-vital-components
-->

<!-- research_source
source_id: S18
role: standard
source_kind: living_index
publisher: International Chamber of Commerce
title: Incoterms DDP — Delivered Duty Paid
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://library.iccwbo.org/clp/clp-incoterms.htm
locator: 2026-08-14 capture 的 DDP 條目；賣方在貨物已辦妥進口清關、於約定目的地到達運輸工具上待卸時交付，並承擔送達該地的成本、風險、進出口清關與關稅責任
limitation: ICC 條目只定義買賣雙方的交貨、成本與風險責任，不解釋台達特定合約的收入總額／淨額判斷、售價、成本、產品毛利或淨利；台達的報表影響仍以 S14 管理層原話為準
independence_group: international-chamber-of-commerce
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

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: OCP 的 L-L CDU 方法把性能測試分為元件層與完整系統層，建議以冷卻液、FWS 溫度與流量、TCS／FWS 壓力及 ATD 一起報告容量；可靠度章節另列材料相容性、水壓、衝擊／振動、熱循環與法規文件
supporting_source_ids: S9
contrary_source_ids:
as_of: 2024-11-01
basis: S9 PDF pp. 15–19 直接列出 qualification 層級與建議性能參數，pp. 20–22 分列材料、水壓、運輸／環境及 regulatory 文件類別
boundary: 只證實 OCP Revision 1.0 的建議方法與欄位，不宣稱它是所有客戶的共同強制標準，也不證明 NVIDIA 列名型號依此方法通過、產品彼此優劣、客戶採購或財務貢獻
verification_needed: 後續若平台或供應商公開具名型號的固定版本、測試條件、原始資料與 pass／fail，才能把通用方法連到特定產品結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: CDU 的 kW 額定值是固定熱與水力條件下的容量主張，不是整體資格分數；跨廠判讀至少還要分開看操作包絡線、元件與整機可靠度、平台列名與供應狀態、場域驗收及公司財務證據
supporting_source_ids: S8,S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 顯示容量必須連同冷卻液、溫度、流量、壓力與 ATD 閱讀，並把可靠度另列成多組測試；S8 又把容量、validation type 與 Supply Chain Status 分成不同欄位，因此不能把單一 kW 欄擴寫成總分
boundary: 這是研究中心用來避免跨層誤讀的判讀框架，不替各平台定義一致門檻，也不建立供應商排名、客戶、訂單、收入、市占、毛利或市場是否反映的結論
verification_needed: 需平台或客戶公布可重現的共同測試條件與具名型號結果，並由部署、採購與同期間公司財務資料分別驗證商業階段
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: OCP 的 L-L CDU 方法把性能報告分成熱性能、TCS 壓頭與 FWS 流動阻抗三張圖；其建議 rating 另把流體類型、FWS 溫度或水溫等級、流量、TCS／FWS 壓力條件與 ATD 綁在同一個 X kW 主張
supporting_source_ids: S9
contrary_source_ids:
as_of: 2024-11-01
basis: S9 PDF pp.16–20 分別定義 ATD 對熱負載曲線、TCS pressure-head 對 flow 曲線、FWS impedance 對 flow 曲線，並列出 fluid、FWS temperature、flowrate、dP 與 ATD 的 performance-reporting 建議
boundary: 只證實 OCP Revision 1.0 的建議報告格式與示例條件；不把示例數值當成所有客戶的強制門檻，也不證明 NVIDIA Marketplace 任一型號已依這三張圖測試、通過或可在具名場域達標
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
claim: NVIDIA DSX Exchange 的 BMS 契約為 CDU 支援液體溫度、流量、壓力與壓差等點位，以同一設備 ID 配合 processArea 區分一次側與二次側位置，並要求 value 帶 timestamp 與 quality；外部設定值或動作請求仍由 BMS 依安全 guardrails 決定是否執行
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 的 Object Types and Point Types、processArea、Value Publication 與 Integration-Published Points 直接列出 CDU 點位、位置上下文、timestamp／quality payload 及 BMS guardrail 權責
boundary: 資料契約支持的是欄位語意與交換責任，不表示所有點位都已安裝、讀值已校正、quality 等於量測不確定度合格、控制已 commissioned，或具名產品已完成平台／客戶驗收
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
claim: 一個可核對的 CDU 容量主張至少要同時保留熱性能、TCS 壓頭、FWS 阻抗三張性能圖，以及能辨識設備、迴路位置、單位、時間與讀值品質的量測上下文；名牌 kW、單一即時數字或資料流存在都不能替代完整 qualification 與 site acceptance
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2026-08-12
basis: S9 把同一 X kW 拆成熱與兩側水力條件，S10 則顯示即時值仍需設備／位置、工程單位、timestamp 與 quality 才能被正確解讀，且控制請求另受 guardrails 裁決；兩份文件共同形成性能與量測的雙層證據契約
boundary: 這是研究中心的證據檢查框架，不宣稱 OCP 與 NVIDIA 已發布單一共同認證、所有場域採同一點位／頻率／門檻，亦不建立供應商排名、客戶、訂單、收入、毛利或市場是否反映的結論
verification_needed: 需平台或客戶對具名型號公開版本化三張性能曲線、感測器位置／校正與品質規則、穩態測試原始資料、pass／fail、site commissioning 及驗收結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: OCP 的丙二醇 TCS 指引把 PG25 定義為 24.5–29.5 vol%、凝固點 9–15°F（−13 至 −9°C），PG55 定義為 53.0–57.5 vol%、凝固點 −37 至 −51°F（−38 至 −46°C）；配方還要有針對迴路金屬的緩蝕劑，並以濃度、凝固點、pH、儲備鹼度及溶解金屬等欄位持續核對
supporting_source_ids: S11
contrary_source_ids:
as_of: 2022-10-03
basis: S11 PDF pp. 7–9 與 pp. 17–20 直接列出 PG25／PG55 體積濃度、凝固點、緩蝕劑、現場濃度檢查及年度分析欄位
boundary: 這些是 OCP 2022 PG 指引的配方與維護範圍，不是所有商品配方的保證值，也不提供熱傳效率、黏度、泵功、CDU 容量、跨廠產品優劣、客戶部署或財務結果
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
claim: OCP 的水基與丙二醇基指引都要求流體、接液材料、接頭、操作條件、啟動與長期紀錄彼此相容，但兩份文件使用不同的流體身分與品質欄位：水基路徑追蹤 TSS／TDS、導電度、硬度與微生物等，PG 路徑另追蹤丙二醇濃度、凝固點、儲備鹼度與配方相關分析
supporting_source_ids: S11,S12
contrary_source_ids:
as_of: 2022-10-03
basis: S11 與 S12 的 General Overview、Typical Properties、Startup、Monitoring and Maintenance、Submittals 分別列出共同生命週期責任與 fluid-specific 欄位
boundary: 只證實兩份 OCP 方法的欄位分流；相同欄名也不代表門檻、測法或化學機制相同，更不能由此判定哪種流體熱效率、成本、可靠度或商業價值較高
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: 2026-08-14 的 OCP Cold Plate 工作頁仍把單相 glycol-based、單相 water-based 與 two-phase coolant 分成不同流體工作範圍，並同時列出 2022 accepted contributions 與後續 water／PG drafts
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-14
basis: S13 Active Workstreams 直接列出三類 coolant scope 與 July 2024 water、November 2025 updated PG draft，Accepted Contributions 另列兩份既有單相指引
boundary: 動態頁面的 draft 名稱與工作流只代表方法仍在演進，不證明草案已發布、任一產品已採用、不同流體可互換，或市場已形成共同 qualification 與財務結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: 同一個 CDU kW 主張若跨水基、PG25 或 PG55 比較，證據包必須固定實際流體與配方版本，並在該流體條件下重新核對熱性能、TCS 壓頭與 FWS 阻抗；水基水質表或 PG 凝固點／濃度表都不能單獨替另一條流體分支背書
supporting_source_ids: S9,S11,S12
contrary_source_ids:
as_of: 2026-08-14
basis: S9 要求容量連同 fluid、溫度、流量、壓力與三張性能圖閱讀；S11／S12 又顯示兩條流體路徑有不同配方、品質與維護契約，因此只換 kW 或 ATD 欄名不足以證明跨流體工作點等效
boundary: 這是研究中心的跨流體可比性閘門，不宣稱水基或 PG 必然較優，也未計算熱物性、泵功、能耗、成本、壽命或供應商排名；文件閾值是規格條件，不是抽樣績效，沒有 sampling SE／t
verification_needed: 需具名 CDU 對同一硬體版本、相同邊界條件與各流體配方公開校正後原始資料、三張性能曲線、重複測試、量測不確定度與 pass／fail
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: unverified
status: active
claim: NVIDIA Marketplace 的具名 CDU 型號已有可重現、版本化且涵蓋 water-based、PG25 與 PG55 的同條件三張性能曲線、流體分析、材料變更與 site acceptance 證據
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-14
basis: S1／S8 只提供動態容量、validation type、wetted materials 與供應狀態欄；S9／S11／S12 是通用方法，S13 是工作流索引，不能替具名產品補上跨流體測試結果
boundary: 不因公開欄位缺少就推論供應商內部沒有測試；只表示目前列出的公開來源不足以建立跨流體等效、qualification、場域驗收或公司財務事實
verification_needed: 平台、供應商與客戶需對同型號／同版本公開各流體配方、操作包絡、原始性能曲線、材料清單、變更控制、commissioning 與 acceptance 結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: 台達在 2026Q2 法說逐字稿中表示，液冷產品約占 2025 年合併營收 10%，並預期 2026 年占比將超過 12%；同場也把部分液冷零組件列為電源及零組件事業成長動能，並表示基礎設施事業所含液冷業務在 2026 上半年快速成長
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-07-30
basis: S14 的事業說明與 Q&A 可直接定位 liquid-cooling components、Infrastructure 所含 liquid cooling，以及管理層對 2025 約 10% 與 2026 預期超過 12% 的回答
boundary: `verified` 只證實管理層做出這些陳述；10% 是公司產品族的近似歷史占比，沒有底層金額與四捨五入規則，超過 12% 是預期而非已實現結果。兩者都沒有拆成 L2A／L2L、RDF106CDT5192、具名客戶、數量或產品毛利；單一發行人揭露不是統計樣本，沒有 sampling SE／t
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: inference
status: active
claim: 液冷財務證據至少要分成「公司液冷產品族占合併營收」、「含液冷的廣泛部門代理」與「具名 CDU 的客戶、數量、收入及毛利」三層；台達的 2025 年約 10% 只讓第一層成立，三家公司 2026Q2 申報附件的部門範圍仍不足以完成第三層型號橋接
supporting_source_ids: S14,S15,S16,S17
contrary_source_ids:
as_of: 2026-08-14
basis: S14 提供台達 aggregate liquid-cooling products 的公司占比；S15 把台達揭露在電源及零組件與基礎設施等廣泛部門，S16 的光寶雲端及物聯網涵蓋多類資料中心與裝置業務，S17 的奇鋐部門則依營運／地域性質呈現，三份申報附件都沒有把平台具名 CDU 接到客戶、數量、收入與毛利
boundary: 三層是研究中心的歸因檢查框架，不是會計準則、公司間成熟度排名或估值模型；它不否定公司可能在內部掌握更細資料，也不把未單列解釋成零收入。台達 10% 不能分配給單一型號，光寶與奇鋐的廣泛部門也不能當成液冷收入上限以外的精確分子
verification_needed: 三家公司以同期間、同合併範圍把具名 CDU 或可辨識產品族連到客戶驗收、出貨量、實際收入及產品毛利；台達另需把 aggregate liquid-cooling products 拆成 L2A／L2L 或具名型號
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: verified
status: active
claim: ICC 的 DDP 規則要求賣方把貨物辦妥進口清關並送到約定目的地、在到達運輸工具上待卸時完成交付，且賣方承擔送達該地的成本與風險
supporting_source_ids: S18
contrary_source_ids:
as_of: 2026-08-14
basis: S18 的 DDP 條目直接列出交貨地點、進口清關，以及賣方承擔成本與風險的責任
boundary: 交貨條件不等於產品毛利率，也不能單獨決定特定公司應採收入總額或淨額表達；台達本輪只表示部分液冷產品的 DDP 銷售提高報表毛利呈現但不影響淨利，不能據此推論液冷產品經濟性改善
verification_needed:
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

## 額定容量只是操作包絡線的一個截面

OCP 的 2024 年 L-L CDU 方法補上 NVIDIA 動態清單沒有展開的「讀規格說明書」。它先提醒：
不同供應商因客製化與缺乏共同格式，可能用不同條件描述性能；因此建議把容量連同冷卻液、
FWS 進水溫度與流量、TCS／FWS 壓力及 ATD 一起報告。換句話說，`600kW` 不是一張總成績單，
而是設備在一組熱與水力條件下的工作點。

這也解釋了為什麼兩台都標 `600kW` 的 CDU，現場整合仍可能不同：一台可能需要較高流量或
設施壓力，另一台可能只支援特定冷卻液；若沒有相同條件與原始資料，就不能只看 kW 說兩者
完全等效。本文的 `M1`／`M2` 仍只比較 NVIDIA 同日同欄的**標示值**，不把 OCP 方法倒填成
那些產品已實際採用的測試程序。

| 證據包要固定什麼 | 新手可以問的白話問題 | OCP 方法能支持到哪裡 | 還不能因此判定 |
|---|---|---|---|
| 熱條件 | 這個容量是在多大的兩側溫差與熱負載下量到？ | ATD、熱負載與流量要一起說明 | 效率、產品優劣或現場一定可達 |
| 水力條件 | 設施端與伺服器端各要多少流量與壓力？ | FWS／TCS 流量、壓力與壓頭是性能邊界 | 客戶機房一定有足夠泵送能力 |
| 冷卻液與材料 | 用哪一種液體，金屬、密封件與濾材能否長期共存？ | 冷卻液種類、材料相容性、腐蝕與流體分析要分開記錄 | 已完成多年現場壽命驗證 |
| 測試對象 | 測的是單一零件，還是整台 CDU 組裝完成後的系統？ | 元件層與完整系統層 qualification 是兩個層級 | 平台列名產品已走完同一套流程 |
| 機械與環境可靠度 | 承壓、運輸、振動、溫濕度變化時會不會漏或變形？ | 水壓、衝擊／振動、熱循環等測試應分列 | 通過單項就等於整機與場域驗收 |
| 文件與法規 | 測試版本、原始資料、限制及安全文件是否可回查？ | 方法要求一般測試報告與 safety／EMC／材料文件 | 已取得訂單、部署或收入 |

這張表是**判讀框架，不是認證名單**。S9 是 OCP 提出的通用方法；沒有任何一頁證明 AVC、
Delta、LITEON 或 LGE 依這份 Revision 1.0 完成全部測試。因此研究中心只把 C10／C12 的方法
事實、C13 的資料契約與 C11／C14 的分層推論接在容量欄後面，不刷新 C9 的公司／平台證據時鐘，
也不改變「財務證據仍缺」的結論。

## 一個 kW 要同時讀三張性能圖與一張量測身分證

**先看熱能不能搬走。** OCP 的熱性能圖不是只放一個最大 kW，而是在指定 FWS／TCS 流量與
設施進水溫度下，把 ATD 對應到可支撐的熱負載。讀者可以把它想成「熱交換器在這組溫差與
流量下，能把多少熱從伺服器側交給設施側」。換一種流體、進水溫度或流量，工作點就可能移動；
所以不同型號若只報最大容量、沒有同一組曲線，仍不能說現場表現完全等效。

**再看二次側推不推得動。** TCS 壓頭曲線回答 CDU 泵浦在不同流量下還能提供多少壓力能力；
現場的管路、快速接頭、分流器與冷板則會形成壓降。只有泵浦能力和整條二次水路阻力在目標流量
相交到可接受的工作點，冷卻液才真的能送到各支路。名牌 kW 不會自動告訴讀者這個交點在哪裡，
也不會說明一台泵浦失效後的備援工作點。

**最後看設施端供不供得上。** FWS 阻抗曲線回答設施水流過 CDU 一次側需要付出多少壓差；
機房則必須供應相符的水溫、流量與壓力。這一關和 TCS 壓頭方向不同：前者在檢查設備向設施
要求多少水力條件，後者在檢查 CDU 能向伺服器迴路提供多少泵送能力。把兩張 PQ 曲線混成一張，
就會看不出瓶頸是在機房一次側、CDU 泵浦，還是伺服器二次側。

| 要看的成績單 | 橫軸與縱軸在回答什麼 | 能支持的問題 | 還不能因此判定 |
|---|---|---|---|
| 熱性能曲線 | 在指定 FWS／TCS 流量與進水溫度下，ATD 對應多少熱負載 | 這組熱條件下可支撐的容量工作點 | 兩台不同條件的 CDU 完全等效、效率較高或已通過客戶驗收 |
| TCS 壓頭 PQ 曲線 | CDU 二次側在不同流量下可提供多少壓頭 | 泵浦能否克服伺服器側管路、接頭、分流器與冷板阻力 | 備援切換一定成功、每個支路都有足夠流量或長期可靠 |
| FWS 阻抗 PQ 曲線 | 設施水通過 CDU 一次側在不同流量下形成多少壓差 | 機房是否可能供應設備要求的溫度、流量與壓力 | 具名場域已完成改造、調試或可在所有季節達到名牌容量 |
| 量測身分證 | 哪台設備、哪一側／位置、量測類型、單位、時間與讀值品質 | 即時資料是否能對到正確物件、位置與時間，並排除明示的不健康讀值 | 感測器已校正、量測不確定度合格、曲線已重現或產品已通過資格驗證 |

三張曲線說明**性能條件**，量測身分證說明**現場數字如何被解讀**。NVIDIA DSX 契約讓同一台
CDU 的一次側入口、一次側出口、二次側供水與二次側回水可以用相同設備 ID、不同 `processArea`
區分；數值另帶工程單位、時間戳與品質旗標。這避免把 `27` 誤當成不同位置、不同單位或過期的
讀值，卻不會自動證明感測器校正、穩態條件或熱平衡正確。

控制資料還要再分成三類：感測值描述現況，設定值描述目標，動作請求要求系統改變狀態。
NVIDIA 明示外部設定值與隔離請求要先經 BMS 的最小／最大值、變化速率與失聯回退等安全限制；
因此「資料已送到」和「設備已安全執行」是兩個證據節點。研究中心把完整階梯依序讀成：

1. 名牌容量與平台欄位先形成待核對主張。
2. 三張性能圖固定熱與水力工作點。
3. 量測身分證讓場域讀值能對到正確設備、位置與時間。
4. 校正、穩態、故障切換與整體試運轉再驗證系統可重現。
5. 客戶驗收、部署分母與公司財務最後才回答商業結果。

這個順序是證據階梯，不是供應鏈或重要性排序。S9 沒有證明 NVIDIA 型號採用同一套 OCP
曲線，S10 也沒有證明每個場域都發布全部點位；兩份資料只能共同說明，容量與即時資料要怎麼
被問對問題，不能替任何供應商補上產品通過、客戶部署、訂單或收入。

## 同樣寫 kW，水基、PG25 與 PG55 仍是三條證據分支

**先辨識名牌數字使用哪一種流體。** 冷卻液不是規格表最後一行的耗材備註，而是熱性能、
水力條件、材料與維護共同使用的測試版本。OCP 2022 年把 treated water 與 propylene glycol
分成兩份指引；丙二醇文件又分 PG25 與 PG55。三者都可用在單相冷板 TCS 的研究問題，卻不是
三個可直接互換的名稱。若兩台設備都寫 `600kW @ 4°C ATD`，但沒有說明實際流體與配方，讀者
還不能確定兩個工作點是否使用同一把尺。

**再把共同責任與流體專屬欄位分開。** 兩份 OCP 指引都要求流體、接液材料、接頭、溫度、
壓力、過濾、啟動樣本與後續紀錄彼此相容；這是共同骨架。專屬欄位則不能混用：水基路徑要
管理 TSS、TDS、導電度、硬度與微生物等水處理狀態，PG 路徑要另固定丙二醇濃度、凝固點、
儲備鹼度與配方相關分析。共同骨架回答「每條迴路都要管理什麼責任」，專屬欄位回答「這條
流體實際要量什麼」。

| 查核位置 | 水基路徑要保留什麼 | PG25／PG55 路徑要保留什麼 | 最容易出現的錯讀 |
|---|---|---|---|
| 流體身分 | 水源、處理方案、初始水質與添加物 | 商品／配方版本、丙二醇體積濃度、抑制劑與稀釋水 | 只寫「water」或「glycol」，沒有版本與濃度 |
| 防凍邊界 | S12 沒有提供 PG 濃度－凝固點表，不能借用 | PG25 為 24.5–29.5 vol%、凝固點 9–15°F（−13 至 −9°C）；PG55 為 53.0–57.5 vol%、−37 至 −51°F（−38 至 −46°C） | 把 `25`／`55` 當成設備容量或所有商品的固定單點 |
| 微生物控制 | 以填充／運轉微生物量、處理方案與趨勢管理 | S11 只在 glycol 濃度維持高於 25 vol% 時稱流體具抑菌性 | 把「biostatic」誤寫成無菌，或推成永遠不需監測 |
| 腐蝕與材料 | 水化學、金屬離子、完整接液材料與變更重審 | 針對迴路金屬的緩蝕配方、修訂後 ASTM D8040 腐蝕試驗、溶解金屬與材料變更重審 | 看到一種金屬合格，就外推所有密封、接頭與塗層 |
| 啟動與換液 | 清潔、沖洗、合格填充、代表樣本與 treatment plan | 新迴路先以選定 PG 流體循環帶出殘留後排放，再正式填充、留樣；既有迴路換液另核對相容性 | 把一次壓測／漏測當成流體 commissioning 完成 |
| 容量與水力 | 用實際水基配方重建熱性能與兩側 PQ 工作點 | 用實際 PG 配方與濃度重建同一組曲線 | 把另一種流體的 kW、流量或壓差直接貼到本配方 |

表中的 PG 濃度與凝固點是 S11 的**規格範圍**，不是供應商績效樣本；因此沒有抽樣 `n`、
sampling SE 或 t 值，也不能據此排列熱效率、泵功、成本與壽命。S11 沒有提供黏度、比熱或
跨流體容量比較，S12 也沒有宣稱 treated water 必然優於 PG。研究中心只量到「兩套文件的
證據欄位不同」，沒有量到「哪一種流體在所有場域更好」。

**最後才問 kW 能不能搬過去。** S9 的三張性能圖提供一個簡單閘門：先在熱性能圖固定流體、
兩側流量、進水溫度與 ATD，再用 TCS 壓頭圖確認二次側推得動，用 FWS 阻抗圖確認設施端供得上。
只要流體或配方版本改變，就要以該版本重新核對這三張圖；不能拿水基的化學合格表替 PG 熱性能
背書，也不能拿 PG 凝固點合格替水基場域的材料、污染與泵送條件背書。

給初學者的最短讀法是依序問四句：**流體是什麼版本？容量曲線是否真的使用這個版本？所有
接液材料與啟動程序是否對應同一版本？換件、補液與長期監測後，這個版本是否仍成立？** 四句
都能由具名資料回答，容量才從名牌值前進到可重現的工作點；再往後仍要另看場域驗收、部署分母
與公司收入。OCP 現行工作頁還列著 2024 water draft 與 2025 updated PG draft，表示版本地圖
仍在演進；草案名稱只能成為監測入口，不能回頭改寫 2022 accepted documents 或替產品補證。

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
| 1. 容量規格 | 設備在指定熱與水力條件下設計可帶走多少熱 | NVIDIA 同日同欄的三筆容量，對應 M1；OCP 方法把容量拆成熱性能、TCS 壓頭與 FWS 阻抗三張曲線，NVIDIA DSX 再示範讀值需要設備／位置、單位、時間與品質上下文 | 各型號實際採用的共同測試程序、完整操作包絡線、感測器校正／不確定度、穩態原始資料與 pass／fail |
| 2. 元件、整機與平台測試 | 零件與完整 CDU 是否通過性能、承壓、材料及環境可靠度測試，產品是否被平台列出 | OCP 提出元件層／系統層及多類可靠度方法；NVIDIA 列出 AVC、Delta、LITEON；LG 另稱 600kW 設備通過超過 100 項條件 | 哪些具名型號依哪一版方法通過、完整門檻與 pass／fail，以及各產品是否走相同流程 |
| 3. 供應準備 | 平台在捕捉日給產品哪一個原始供應標籤 | Delta 為 MP Ready；AVC、LITEON 為 Sample Ready | 標籤對應的產能、良率、庫存、交期與客戶承諾；LG 當時沒有可重現狀態 |
| 4. 場域整合與客戶部署 | 系統是否在接近真實或真實場域運作，並走向驗收 | Daikin／Delta 規劃 100 至 3000kW 產品範圍；Daikin／NTT DATA 概念驗證預計至 2027 年 3 月 | 節電、成本、可用率、商用接受度，以及具名客戶是否完成驗收 |
| 5. 公司收入 | 產品是否帶來訂單、收入、毛利與現金流 | 台達管理層表示 2025 年液冷產品約占合併營收 10%，但只到公司產品族分子 | 三家公司把具名 CDU 接到客戶驗收、數量、實際收入、產品毛利與現金流；台達另需拆開 L2A／L2L 與型號 |

只有第一關的 `M1` 容量完成「換成相同單位後可比」判定。平台的兩種供應標籤沒有公開的共同
量產率或財務定義，因此本文不把它們換算成成熟度分數。第五關現在多了一筆台達公司的產品族
占比，卻仍沒有三家公司同產品、同期間、同會計定義的數字，所以不能比較誰更接近收入。

## 財務分母階梯：10% 已經比部門代理更近，但還不是那台 CDU

讀液冷財務揭露，最重要的不是先問「數字大不大」，而是先問**這個分子究竟裝了什麼**。
本輪把三種常被混在一起的數字拆開：

| 財務層級 | 分子與分母 | 本輪證據到哪裡 | 不能跨過的界線 |
|---|---|---|---|
| 1. 公司液冷產品族 | 所有 liquid-cooling products ÷ 同期間合併營收 | 台達管理層表示 2025 年約 10%，並預期 2026 年超過 12% | `約 10%` 沒有底層金額與四捨五入規則；`超過 12%` 是預期，不是已實現結果；兩者都沒有拆成 L2A、L2L 或 CDU |
| 2. 廣泛部門代理 | 含有液冷的整個事業部 ÷ 合併營收 | 台達申報附件仍以電源及零組件、基礎設施等部門呈現；光寶雲端及物聯網與奇鋐營運／地域部門範圍也都比液冷大 | 不能把整個部門都算成液冷，也不能拿三種不同部門定義互排 |
| 3. 具名型號橋接 | 某一 CDU 的客戶驗收、數量、收入與毛利 ÷ 對齊的公司分母 | 尚未完成 | 台達的 10% 不能分配給 RDF106CDT5192；AVC 與 LITEON 的平台型號也沒有公司財務分子 |

這裡的 10% 是**單一發行人對公司全集合的近似陳述**，不是從樣本估計母體；來源沒有提供底層
產品收入、四捨五入規則或跨期重述，因此沒有可計算的 sampling SE／t，也不宜反推一個看似
精確的金額。2026 年「超過 12%」更只能放在管理層預期欄，不能先寫進實績。

### 為什麼同一句「液冷」仍可能裝了不同產品

法說提問先談 L2A，管理層回答時使用較廣的 `liquid-cooling products`，並表示 L2A 的生命週期
可能比市場預期長、公司同時觀察 L2L。這個回答說明產品族可能跨越架構與零組件，卻沒有給出
各分支占比。研究中心因此保留原詞，不把 10% 偷換成「L2L CDU 占比」，也不把 NVIDIA 上的
1MW 型號當成這個分子的全部。

### DDP 改變報表呈現，不等於產品毛利變好

台達在同場說明，第一季部分液冷產品採 DDP 銷售，使報表毛利率看起來較高，但對淨利沒有影響。
ICC 對 DDP 的定義重點是賣方負責送達約定目的地、進口清關並承擔相關成本與風險；它描述的是
交貨責任，不是產品經濟性。若只看到「毛利率較高」就推論液冷售價、成本結構或產品毛利改善，
會把交易條件造成的報表呈現和真正的單位經濟混在一起。下一份有用的證據應直接給出同產品、
同期間的收入、成本或毛利，而不是再次只給公司整體毛利率。

## 什麼情況會讓容量排行榜失真

- **相同 kW 可能落在不同操作包絡線**：客戶必須確認現場 FWS／TCS 的溫度、流量、壓力與冷卻液能否落入設備條件；只知道額定容量，還不知道泵浦負擔、材料相容性或故障時可用能力。
- **客戶可能要的是模組化與維修能力**：客戶可能依機櫃或整排配置採多台設備，而不是選單台最大容量；泵浦備援、占地、隔離、維修時間與服務網路都可能更重要。
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
- [S9：OCP《Liquid to Liquid CDU Test Methodology and Performance Rating》Revision 1.0](https://www.opencompute.org/documents/ocp-wp-l-lcdu-test-methodology-performance-rating-r1-pdf)（元件／整機 qualification、性能條件與可靠度測試的建議方法；不是產品認證名單）。
- [S10：NVIDIA DSX Exchange BMS Integration Companion Guide](https://docs.nvidia.com/dsx-exchange/bms-integration)（2026-08-12 capture；CDU 點位、位置／單位／時間／品質上下文與 BMS guardrails 的資料契約；不是產品性能或場域驗收結果）。
- [S11：OCP《Guidelines for Using Propylene Glycol-Based Heat Transfer Fluids》](https://www.opencompute.org/documents/guidelines-for-using-propylene-glycol-based-heat-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf)（2022-10-03；PG25／PG55 配方、腐蝕、啟動與維護指引；不是跨流體性能排名）。
- [S12：OCP《Guidelines for Using Water-Based Transfer Fluids》](https://www.opencompute.org/documents/guidelines-for-using-water-based-transfer-fluids-in-single-phase-cold-plate-based-liquid-cooled-racks-final-pdf)（2022-10-03；水基 TCS 的水質、啟動與維護指引；門檻不能套到 PG）。
- [S13：OCP Cold Plate Sub-Project 工作頁](https://www.opencompute.org/wiki/Cooling_Environments/Cold_Plate)（2026-08-14 capture；現行 coolant workstream、draft 與 accepted contribution 版本地圖；不是草案已發布證明）。
- [S14：台達 2026Q2 法說逐字稿](https://filecenter.deltaww.com/IR/download/calendar/2Q26_Transcript.pdf)（2026-07-30；公司液冷產品族占比、事業成長與 DDP 回答；英文稿僅供參考、中文原音為準）。
- [S15：台達 115 年第二季合併財務報告](https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=2308&filename=202602_2308_AI1.pdf)（部門仍大於液冷產品族，沒有具名 CDU 分子）。
- [S16：光寶科 115 年第二季合併財務報告](https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=2301&filename=202602_2301_AI1.pdf)（雲端及物聯網涵蓋多種業務，不能直接當液冷收入）。
- [S17：奇鋐 115 年第二季合併財務報告](https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=3017&filename=202602_3017_AI1.pdf)（部門按營運／地域性質呈現，沒有具名 CDU 分子）。
- [S18：ICC Incoterms DDP 定義](https://library.iccwbo.org/clp/clp-incoterms.htm)（2026-08-14 capture；說明交貨、清關、成本與風險責任，不是產品毛利定義）。

**可證實：** 同日同欄的容量、平台原始供應標籤、LG 自述驗證、合作備忘錄範圍與概念驗證時程；OCP 文件另可證實其建議的性能報告欄位與可靠度測試類別。台達管理層也確實做出「2025 年液冷產品約占合併營收 10%、2026 年預期超過 12%」的陳述，但前者是近似產品族占比，後者是預期。

**待驗證：** 平台狀態的精確判準、具名客戶、部署數、訂單、具名 CDU 收入、產品毛利、
現金流與實際節能結果。台達產品族占比不能分配給單一 L2A／L2L 或 RDF106CDT5192；OCP
方法也不能證明某一具名產品已完成相同測試。合作名單、平台列名、額定 kW 或廣泛部門數字
都不得替代這些產品與公司層級證據。

## 8 月 9 日複核：LG 進入清單，但供應階段仍空白

- `T1` 預先登錄的觸發條件已命中：LGE 從公司公告中的驗證資訊，前進到 NVIDIA 清單可定位的
  600kW／850LPM 列項；但原始供應狀態欄仍空白，不能代填成 `Sample Ready` 或 `MP Ready`。
- AVC、Delta、LITEON 的原列型號、容量與供應狀態未變；`M1` 保留 2026 年 8 月 2 日三筆歷史
  快照，`M2` 另存 8 月 9 日四筆同欄觀測。
- 新證據只把 LGE 推到「平台列名／validation」；客戶部署、訂單、量產、收入與獲利仍沒有
  可重算證據。下一輪改由 `T4` 追蹤原始欄位變化。

## 8 月 12 日方法補強：三張性能圖與量測身分證補上 kW 背後的問題

- 本輪後來找到的 S9 發布於 2024 年；它把容量拆成熱性能、TCS 壓頭與 FWS 阻抗三張圖，
  也把元件、整機、水壓、材料、運輸與環境可靠度分開。這補的是讀法，不是 2026 年產品新進展。
- S10 是 8 月 12 日捕捉的現行 NVIDIA 資料契約：它要求 CDU 讀值帶設備／位置、工程單位、
  timestamp 與 quality，並把感測、設定值、動作請求及 BMS guardrails 分開。資料可以被正確
  交換，仍不表示感測器已校正、三張性能圖已重現或場域已通過驗收。
- S9 早於現有公司與平台證據；S10 雖是本日捕捉的現行頁面，卻只定義資料交換，沒有指向
  任何 NVIDIA 列名產品的 pass／fail。本輪新增內容也沒有追加到 C9 主命題；因此保留 `last_reviewed_at: 2026-08-09`、
  `review_due: 2026-08-14` 與 C9，不用周邊方法或資料契約假刷新證據時鐘。
- 後續若平台公開同型號、同版本、同測試條件的原始資料與結果，才可把 C10 的通用方法推進
  到特定產品；在那之前，C11／C14 只是避免把 kW 或即時資料當總分的分層框架。

## 8 月 14 日方法補強：先固定流體分支，再談容量可比

- 本輪以 2022 年同日發布的 S11／S12 拆開丙二醇基與水基 TCS；兩份文件有共同的材料、啟動、
  監測與變更責任，卻使用不同流體身分、化學與維護欄位。PG25／PG55 的濃度與凝固點是規格
  範圍，不是抽樣績效，也沒有跨流體熱效率、泵功、成本或壽命比較可供外推。
- S9 已要求容量帶著冷卻液與三張熱／水力曲線；S11／S12 進一步證明「冷卻液」不能只留一個
  泛稱。C18 因此新增流體版本閘門，但仍是方法推論；S1／S8 沒有具名產品的跨流體曲線與場域
  驗收，C19 保持待驗證。
- S13 是 2026-08-14 的現行工作頁，支持的是 workstream 與 draft／accepted 版本地圖；本文未
  讀取 Google Drive 草案內容，也不把 draft 名稱改寫成正式規格或產品採用。
- S11／S12 發布於 C9 主命題之前，S13 雖是本日 living capture，卻只支持新 C17 並作 T7 的
  版本監測入口；三者都沒有追加到 C9。故這次方法補強當時不刷新 `last_reviewed_at`、
  `base_confidence` 與公司／平台結論；後續的 Q2 財務監測再另行留下新期限。

## 8 月 14 日監測複核：先有公司液冷分子，仍沒有具名 CDU 橋接

- 本輪依 `T2` 預先登錄範圍，用同一 MOPS 索引查 2301、2308、3017 的 115 年 Q2 中文合併
  財報；明示母體 N=3、命中 3、缺件 0，並逐頁核對各自部門資訊。這是指定公司母體的精確
  census，不是抽樣估計，因此沒有 sampling SE／t；它也不代表全 121 檔、所有 IR 附件或
  液冷相關公司都已掃完。
- 新支持來自 S14：台達管理層把 aggregate liquid-cooling products 連到 2025 年約 10% 的
  公司營收分子，並給出 2026 年超過 12% 的預期。這讓「公司液冷產品族」前進到直接財務
  歸因，但 10% 沒有底層金額與產品拆分，12% 以上也尚未成為實績。
- S15–S17 的正式財報仍停在廣泛部門：台達同一液冷敘事可能跨電源及零組件與基礎設施，
  光寶雲端及物聯網涵蓋多類產品，奇鋐則依營運／地域性質呈現。三份附件都沒有把 NVIDIA
  平台上的具名 CDU 接到客戶驗收、數量、收入與毛利。
- `T2` 因出現新支持而退役，但原 trigger 沒有完整命中；`T8` 接續追公司產品族到具名型號的
  最後一段橋。這批新證據把文章核心從 C9 的單次平台列名進展，推進為 C21 的「產品族分子、
  廣泛部門代理、具名型號橋接」三層主命題；C9 仍保留為歷史有效 claim，不被覆寫。因此
  `last_reviewed_at` 更新為 2026-08-14、`review_due` 取所有 active monitor 最早的 T4
  2026-08-16，`base_confidence` 維持 medium；這次時鐘刷新由 S14–S17 的新主命題證據承擔，
  不是用 DDP 名詞或周邊方法假刷新。

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
evidence_boundary: 台達另有 aggregate liquid-cooling products 約占 2025 年合併營收 10% 的管理層陳述，但平台列名、狀態、MOU 與公司產品族占比都不證明 RDF106CDT5192 或光寶 LC-LL-WCDU-6011(S) 的具名客戶、量產出貨、產品收入、市占、毛利或現金流
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
status: retired
claim_ids: C6
metric: 台廠 CDU 客戶驗收、量產出貨與財務認列
source_ids: S1,S3,S6
watch_source_ids: S5
frequency: quarterly
frequency_detail: 每季法說、財報與重大訊息發布後逐公司核對
next_check: 2026-08-14
trigger: 3017、2308 或 2301 首次把具名 CDU 型號連到客戶驗收、量產數量、收入及毛利
invalidation: 公司明確表示指定 CDU 專案取消、沒有相關訂單／收入或退出該產品；到期只有平台列名、MOU 或整體液冷敘事時維持 C6 待驗證，不視為反證
retired_at: 2026-08-14
retirement_reason: 三家公司 2026Q2 正式財報已完成指定母體複核，台達另出現公司液冷產品族約占 2025 年營收 10% 的新支持；但具名 CDU 客戶、數量、收入與產品毛利 trigger 未完整命中，後續由 T8 追產品族到型號的橋接
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

<!-- monitoring_item
monitor_id: T5
status: active
claim_ids: C10,C11
metric: NVIDIA CDU 列項是否公開可重現的操作包絡線、元件／整機範圍、可靠度結果與版本化證據包
source_ids: S8,S9
watch_source_ids: S8
frequency: monthly
frequency_detail: 每月在 Marketplace 週捕捉之外，另核對 validation type、測試條件與可下載文件；出現完整 protocol 或具名產品結果時提前
next_check: 2026-08-31
trigger: 平台對具名型號公開冷卻液、ATD、FWS／TCS 流量與壓力、測試版本、原始資料及 pass／fail，或明示採用與 OCP Revision 1.0 可對照的方法
invalidation: 平台明示各型號使用不可互比的定義、撤回測試結果，或新文件顯示 C11 所列條件仍不足以描述性能；屆時縮窄判讀框架，不覆寫 S9 的歷史方法內容
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C12,C13,C14
metric: 具名 CDU 是否把熱性能曲線、TCS 壓頭、FWS 阻抗與可辨識設備／位置／單位／時間／品質的 telemetry 接成可重現場域證據
source_ids: S9,S10
watch_source_ids: S8,S10
frequency: monthly
frequency_detail: 每月核對 Marketplace 產品附件與 DSX BMS 文件版本；具名型號新增曲線、校正、穩態或 commissioning evidence 時提前
next_check: 2026-08-31
trigger: 平台或客戶對同一型號公開版本化三張性能曲線、感測器位置與校正／不確定度、timestamp／quality 規則、穩態原始資料、故障切換及 site pass／fail
invalidation: 新版共同方法證明單一 kW 與既有 Marketplace 欄位已完整固定三張性能圖、量測品質及所有場域驗收條件；屆時縮窄 C14，不把資料契約存在當成公司財務證據
-->

<!-- monitoring_item
monitor_id: T7
status: active
claim_ids: C15,C16,C17,C18,C19
metric: 具名 CDU 與 OCP 方法是否把 water-based、PG25、PG55 的配方版本、三張性能曲線、材料變更與場域驗收接成可重現的跨流體證據
source_ids: S9,S11,S12
watch_source_ids: S13,S8
frequency: monthly
frequency_detail: 每月核對 OCP Coolant Fluids workstream、accepted／draft 版本地圖與 Marketplace 附件；正式新版或具名跨流體結果出現時提前
next_check: 2026-08-31
trigger: OCP 正式發布新版 water／PG 文件，或平台、供應商與客戶對同一 CDU 版本公開各流體配方、熱性能、TCS 壓頭、FWS 阻抗、量測不確定度、材料變更、commissioning 與 pass／fail
invalidation: 具名重複測試證明流體或配方版本在本文列出的完整熱、水力、材料與場域條件下不影響工作點，或正式新版方法合併分支並提供等效規則；屆時依新證據修正 C18，不以 draft 標題或單一 kW 欄代替結果
-->

<!-- monitoring_item
monitor_id: T8
status: active
claim_ids: C6,C20,C21
metric: 公司液冷產品族占比到具名 CDU 客戶、數量、實際收入與產品毛利的橋接
source_ids: S14,S15,S16,S17
watch_source_ids: S5
frequency: quarterly
frequency_detail: 每季法說、財報與重大訊息發布後逐公司核對；具名型號、客戶驗收或產品財務出現時提前
next_check: 2026-11-14
trigger: 3017、2308 或 2301 把平台具名 CDU 連到客戶驗收、量產數量、實際收入及產品毛利，或台達把 aggregate liquid-cooling products 的實際占比拆成 L2A／L2L／CDU 與具名型號
invalidation: 公司明確取消或退出具名 CDU、表示沒有相關訂單／收入，或後續正式揭露修正台達 2025 約 10% 的產品族口徑；只有廣泛部門、總體液冷敘事、DDP 報表呈現或年度預期時，C6 仍維持待驗證
-->

## 接下來看到什麼，判定才會改變

- **平台欄位改變**：若 NVIDIA 改寫 AVC、LITEON 或 LGE 的原始供應狀態，就追加新快照、來源與觀測；不得修改 `M1` 的 2026 年 8 月 2 日歷史紀錄。
- **公司補上商業證據**：台達已有公司液冷產品族的近似歷史占比，但仍須把它拆成 L2A／L2L、CDU 與具名型號；3017、2308、2301 若在法說或財報同時揭露具名設備的客戶驗收、量產數量、實際收入與產品毛利，才可完成產品層商業橋接。
- **概念驗證交付結果**：Daikin／NTT DATA 若公布結果，需有可重算的節電、成本或可靠度基線；官方宣告失敗、取消或延後超過 2027 年 3 月才構成反證，沒有公開結果只維持待驗證。
- **容量與收入走出相反順序**：若較高容量型號長期停留送樣，而較低容量型號先取得部署與收入，就會直接否定「容量可代表商業成熟度」的市場捷徑。
- **容量欄位定義改變**：若 NVIDIA 改變 `Cooling Capacity @ 4°C ATD` 定義，或顯示不同型號不能共用同一欄位，`M1` 的可比結論只保留在 2026 年 8 月 2 日快照，不外推到新版清單。
- **公開可重現的資格驗證包**：只有平台或客戶把具名型號、版本、冷卻液、溫度、流量、壓力、測試矩陣、原始資料與 pass／fail 接起來，才把「列出測試名稱」升為可對照的產品結果；OCP 通用方法本身不能代替這份證據。
- **三張曲線與量測品質接到同一型號**：只有熱性能、TCS 壓頭與 FWS 阻抗曲線能對回同一設備版本，且現場資料另揭露感測位置、單位、時間、quality、校正／不確定度與穩態條件，才可判斷名牌工作點是否可在具名場域重現；資料流存在本身仍不是驗收或收入。
- **流體分支能否對回同一設備版本**：平台若只寫 `water`、`glycol` 或 wetted materials，仍不足以證明跨流體等效；要看到實際配方、濃度、三張性能曲線、材料與換液／變更紀錄、commissioning 及客戶 pass／fail，才可把 water-based、PG25 或 PG55 的結果放進同一比較。
