# 資料先是電、再變成光：轉換器放哪裡，決定可插拔與共同封裝的取捨

<!-- research_topic
topic_id: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-05-31
last_reviewed_at: 2026-08-01
review_due: 2026-08-15
source_type: mixed
publisher_domain: nvidia.com
canonical_url: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory
source_chain_id: nvidia-cpo-production-marvell-1p6t-20260312-20260721
stock_ids: 3711
group_ids: packtest
trigger_type: product_ramp
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C2
base_confidence: medium
confidence_basis: 多家一手來源證實兩種架構同時商品化，但尚無可比出貨占比
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: official_cpo_production_and_pluggable_volume_sources_captured
evidence: source_chain:nvidia-cpo-production-marvell-1p6t-20260312-20260721
-->

<!-- research_source
source_id: S1
role: company_release
publisher: NVIDIA
title: Vera Rubin 與 Spectrum-X Ethernet Photonics full production 公告
published_at: 2026-05-31
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory
locator: Spectrum-X Ethernet Photonics 與 full production 段落
limitation: 只能證實 NVIDIA 的產品階段，未揭露 CPO 出貨占比或客戶部署數
-->

<!-- research_source
source_id: S2
role: company_release
publisher: NVIDIA
title: GTC Taipei 製造生態系與 SPIL 角色
published_at: 2026-06-01
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/
locator: manufacturing ecosystem 與 co-packaged optics 段落
limitation: 生態系列名不等於供應商新增訂單、份額或獲利
-->

<!-- research_source
source_id: S3
role: company_release
publisher: NVIDIA
title: Spectrum-6 同時支援 pluggable 與 co-packaged optics
published_at: 2026-07-21
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/
locator: Spectrum-6 form factors 段落
limitation: 未提供兩種形式的出貨量、收入或長期占比
-->

<!-- research_source
source_id: S4
role: competitor_primary
publisher: Marvell
title: Ara 1.6T 可插拔光 DSP 大量出貨
published_at: 2026-03-12
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html
locator: mass volume production 與 pluggable modules 段落
limitation: 供應商公告未揭露終端客戶、實際模組數量或市場份額
-->

<!-- research_source
source_id: S5
role: other_primary
publisher: ASE Technology
title: SPIL 新廠與 NVIDIA 合作關係
published_at: 2025-01-16
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.aseglobal.com/press-room/spil-hosts-nvidia-founder-and-ceo-at-new-factory-site/
locator: SPIL subsidiary 與 packaging relationship 段落
limitation: 只能確認公司關係與合作脈絡，未量化 CPO 訂單或收入
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
locator: 2026-08-01 以 3711 與相關台灣供應商代號重查法說、重大訊息與季度財報的入口
limitation: 查詢入口會持續更新；入口本身不證明 CPO 客戶、料號、量產或收入
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: document
publisher: Lumentum
title: Lumentum selected as NVIDIA silicon photonics ecosystem partner
published_at: 2025-03-18
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investor.lumentum.com/financial-news-releases/news-details/2025/Lumentum-Selected-as-an-NVIDIA-Silicon-Photonics-Ecosystem-Partner-to-Advance-AI-Networking-at-Scale/default.aspx
locator: key contributor、high-power high-efficiency lasers 與 Spectrum-X Photonics role 段落
limitation: 具名技術角色不等於 Spectrum-X 量產出貨量、供應份額、sole source、收入或毛利貢獻
independence_group: lumentum
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: NVIDIA 已將 Spectrum-X Ethernet Photonics 描述為進入 full production
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-05-31
basis: 指定來源直接使用 full production 描述產品階段
boundary: 證實的是 NVIDIA 的公開產品階段，不代表已知出貨占比、市占或供應商損益
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: active
claim: 現有證據較支持 CPO 與 1.6T 可插拔在本階段共存，而非可插拔立即被全面取代
supporting_source_ids: S3,S4
contrary_source_ids:
as_of: 2026-07-21
basis: Spectrum-6 公開支援兩種形式，且 Marvell 同期宣告 1.6T 可插拔 DSP 大量出貨
boundary: 這是由產品組合與供應商階段推導的市場結構判讀，沒有全市場出貨占比可直接驗證
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: NVIDIA 公開資料列出 SPIL 的 CPO 封裝、組裝與測試角色，ASE 資料確認 SPIL 的集團關係
supporting_source_ids: S2,S5
contrary_source_ids:
as_of: 2026-06-01
basis: 兩份公司一手資料分別支持製造角色與公司歸屬
boundary: 只能證實列名與角色，不能外推新增訂單、份額、收入或毛利
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: unverified
status: active
claim: SPIL 已因 Spectrum-X CPO 取得可量化且具財務重大性的新增訂單
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 目前來源只有生態系列名與合作脈絡，沒有公司層級財務證據
boundary: 未確認料號、訂單、出貨量、收入占比、毛利或客戶合約
verification_needed: 日月光投控法說、財報或客戶文件需直接揭露 CPO 量產貢獻
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: Lumentum 公告其高功率高效率 InP laser 是 NVIDIA Spectrum-X Photonics networking switches 的具名矽光子生態系角色
supporting_source_ids: S7
contrary_source_ids:
as_of: 2025-03-18
basis: S7 直接使用 selected as a key contributor，並明列 Lumentum laser 在 Spectrum-X Photonics 的角色
boundary: 只能證實具名角色，不能外推量產數量、供應份額、sole source、收入或毛利
verification_needed:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2
metric: Spectrum-X 後續世代的 CPO 與可插拔產品組合、部署量或占比
source_ids: S1,S3,S4
watch_source_ids: S6
frequency: event_driven
frequency_detail: 每季與重大產品發布
next_check: 2026-08-15
trigger: NVIDIA 或光通訊供應商首次量化任一形式的系統數、埠數或收入占比
invalidation: 若後續兩個產品世代仍未擴大 CPO 部署且可插拔持續主導，快速替代論失效
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C4
metric: SPIL CPO 客戶、料號、量產與財務貢獻
source_ids: S2,S5
watch_source_ids: S6
frequency: quarterly
frequency_detail: 每季法說與財報
next_check: 2026-10-31
trigger: 日月光投控首次直接揭露 CPO 量產、客戶或收入貢獻
invalidation: 若公司持續只被生態系列名而沒有量產或財務證據，個股受惠映射維持未證
-->

<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: architecture_coexistence_and_taiwan_mapping_reviewed
evidence: sources:S1,S2,S3,S4,S5
-->
<!-- transition
date: 2026-08-02
from: triaged
to: triaged
reason: added_named_external_laser_role_without_financial_promotion
evidence: sources:S7
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
reason: editorial_plain_language_wave3_no_conclusion_change
evidence: editorial:plain_language_wave3
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave99_cpo_five_positions_five_tradeoffs_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **交換晶片**：接收多台設備的資料並決定下一站要從哪個連接埠送出；光學方案改變的是資料離開晶片後的轉換位置。
- **電訊號**：以電壓或電流變化承載資料的訊號；它在晶片與電路板上傳送，距離愈長、速度愈高，耗電與訊號損失愈難控制。
- **光訊號**：以光的變化承載資料的訊號；適合沿光纖送到下一台設備，但必須先完成電光轉換。
- **光纖**：以光傳送資料的纖維；光纖存在不代表轉換器一定放在可插拔模組或交換晶片旁邊。
- **電光轉換**：把交換晶片送出的電訊號轉成光訊號，接收端再把光還原成電的過程。
- **共同封裝光學（CPO）**：把光引擎放到交換晶片旁邊，縮短高速電訊號在電路板上行走的距離。
- **可插拔光模組**：裝在交換器前面板、能從外部拔換的光通訊模組；它把轉換器與交換晶片分開。
- **光引擎**：負責電光轉換、驅動與光學介面的模組；放在交換晶片旁邊時，維修方式會和前面板模組不同。
- **前面板**：交換器機箱面向維修人員、安裝光模組與光纖接頭的位置。
- **連接埠**：交換器對外收送一條連線的介面；產品開始生產不等於已知部署了多少個連接埠。
- **高速序列介面（SerDes）**：把資料轉成高速序列電訊號並在另一端還原的電路；速度愈高，傳輸距離、耗電與訊號完整性愈難兼顧。
- **光訊號處理晶片（DSP）**：在光模組中處理高速訊號補償與轉換的晶片；晶片大量出貨不等於整體模組市場只剩一種架構。
- **1.6T**：每秒 1.6 兆位元的連線容量；它描述速度，不是固定的封裝形式、產品數量或營收。
- **雷射光源**：提供穩定光能給光引擎調變與傳輸的元件；光源位置與維修方式會影響整體設計。
- **磷化銦雷射（InP laser）**：以磷化銦材料製作的雷射元件；具名角色不等於獨家供應、已知份額或已揭露收入。
- **矽光子**：在矽基製程上整合光學元件的技術；有製程能力不等於已進入特定平台量產。
- **光纖耦合**：把光準確送進或送出光纖與光學元件的連接步驟；對準、損耗與封裝一致性都要驗收。
- **Spectrum-X Ethernet Photonics**：NVIDIA 的具名共同封裝光學交換器產品線；公司把它描述為進入產品生產。
- **Spectrum-6**：NVIDIA 的交換器世代名稱；官方資料顯示同代可支援可插拔與共同封裝兩種形式。
- **Ara**：Marvell 對 1.6T 可插拔光模組 DSP 使用的產品名稱；本文只用它確認可插拔路徑仍在出貨。
- **SPIL（矽品）**：日月光投控旗下封測公司；NVIDIA 直接列名其晶片級封裝、組裝與測試角色。
- **Lumentum**：公告自己是 NVIDIA 矽光子生態系的具名雷射角色；公司自述仍不能替出貨量、份額或毛利背書。
- **封裝、組裝與測試**：把光學、電路與晶片整合、接起來並確認功能與品質的製造接力；列名角色不等於可量化訂單。
- **產品生產（Production／full production）**：平台商表示具名產品已進入持續製造的階段；各公司門檻不同，仍要另查實際出貨與部署。
- **產品組合**：同一世代同時提供哪些形式、型號與速度；支援兩種形式不代表兩者出貨比例相同。
- **可維修性**：設備故障後能否快速定位、拆換與恢復服務；能拔換通常較直接，共同封裝則要看平台的實際維修設計。
- **故障範圍**：單一元件故障時會影響一個模組、一個連接埠、整個交換器或更大區域的範圍。
- **生命週期成本**：從購買、耗電、維修、備品、停機到升級的總成本；不能只用單一元件價格比較。
- **客戶驗收**：營運者依功能、可靠度、維修與系統條件確認產品是否可正式使用。
- **部署分母**：判斷需求規模的共同基準，例如交換器數、連接埠數、光連線數與兩種形式的使用比例。
- **雙向核對**：平台端與供應商端文件能對上同一產品、角色、期間與量產狀態。
- **財務足跡**：能在出貨、收入、毛利或現金流中辨識的結果；生態系列名與技術合作還不算。

### 三句話抓重點

- 資料先以電訊號進入交換晶片，再轉成光訊號送往下一台設備；兩種做法真正不同的地方，是轉換位置離交換晶片多遠、能不能從面板拔換。
- 轉換留在前面板比較容易維修與升級；把它移到交換晶片旁邊則縮短高速電路，卻把封裝、散熱、雷射、測試與故障處理綁得更緊。
- 所以一種方案開始生產，不代表另一種立刻消失；還要看到它用在哪些連線、多少交換器與連接埠、誰通過驗收，以及收入與毛利，才能判斷公司真正受惠。

### 為什麼重要

**先找「電在哪裡變成光」。** 可插拔光模組把轉換器留在前面板，壞掉時可以從外部更換；
共同封裝光學把光引擎移到交換晶片旁邊，讓高速電訊號少走一段電路板。兩者不是單純的新舊
版本，而是把功耗、密度、維修、封裝與測試壓力放在不同位置。

**再看誰承接每一段工作。** 平台與交換晶片團隊決定架構，光引擎與雷射提供電光轉換，封裝
測試把光學和電路整合，模組與系統團隊負責連接、維修與部署。任何一個角色被列名，都只證明
它在接力中有位置，還沒有回答數量、份額與獲利。

**最後分開產品生產與公司受惠。** 同一世代可以同時提供可插拔與共同封裝，兩條路也可能
同步出貨。真正要量的是各自部署在哪裡、占多少連接埠、故障與維修結果如何，以及供應商的
出貨、收入、毛利和現金流。

### 接下來怎麼追

- 先追平台端是否公布兩種形式用在哪些交換器與連線，並提供交換器數、連接埠數、故障率、維修時間與耗電結果。
- 再追具名雷射、封裝測試與可插拔晶片角色，能否由平台端和供應商端對上同一產品、期間、驗收與出貨。
- 最後追日月光投控是否拆出矽品相關產能、收入、毛利與現金流；其他台灣公司沒有具名文件前，維持研究候選。

### 想一想

- 如果交換器最常壞的是可拔換模組，把轉換器移進晶片旁邊後，維修時間與受影響範圍會怎麼改變？
- 同一世代同時提供兩種形式時，要看到哪些交換器數與連接埠比例，才能判斷誰正在取代誰？
- 平台公布產品開始生產，但供應商沒有揭露出貨、收入或毛利時，技術信心與公司受惠信心應該一起上調嗎？

## 先用五個位置看資料怎麼從電變成光

| 本文五個位置 | 資料現在是什麼 | 這裡負責什麼 | 主要接力角色 | 不能直接推成 |
|---|---|---|---|---|
| 1. 交換晶片內部 | 電訊號 | 決定資料要從哪個連接埠送出 | 平台、交換晶片與系統軟體 | 晶片速度更快，不等於光學架構或供應商已確定 |
| 2. 晶片到轉換器的高速電路 | 電訊號 | 把資料送到電光轉換位置 | SerDes、電路板、封裝與訊號設計 | 電路較短通常是目標，不等於已知整機節能多少 |
| 3. 電光轉換位置 | 電轉成光 | 由可插拔模組或晶片旁光引擎完成轉換 | 光引擎、DSP、驅動與矽光子 | 能完成轉換，不等於通過客戶驗收或穩定量產 |
| 4. 雷射與光纖耦合 | 光訊號 | 提供光源並把光準確送進光纖 | 雷射、光學元件、耦合、封裝與測試 | 具名雷射角色不等於獨家供應、份額或財務貢獻 |
| 5. 光纖與下一台設備 | 光訊號 | 把資料送到另一台交換器或運算設備，再轉回電 | 光纖、連接器、交換器、營運與維修團隊 | 一條連線可用，不等於整個網路都採相同形式 |

五個位置是閱讀資料流的最短路徑，不是完整交換器設計圖。兩種方案都要把電轉成光；差別在
第三個位置靠近前面板還是交換晶片，以及這個選擇如何改變第二、四、五個位置的功耗、密度、
封裝、維修與故障責任。

## 再用五把尺比較兩種轉換位置

| 本文五把尺 | 可插拔光模組 | 共同封裝光學 | 下一個要量的結果 | 不能直接推成 |
|---|---|---|---|---|
| 1. 高速電路長度與功耗 | 轉換器在前面板，電訊號要走較長的板上路徑 | 光引擎靠近交換晶片，目標是縮短高速電路 | 同一速度與流量下的系統耗電、訊號損失與冷卻負擔 | 平台商倍數比較不能直接套到所有交換器 |
| 2. 前面板空間與頻寬密度 | 每個模組占用面板位置，形式與尺寸受面板限制 | 光學移近晶片，面板可改用光纖連接方式 | 每台交換器的有效連接埠、纖芯、空間與散熱配置 | 密度較高不等於每埠成本或總成本較低 |
| 3. 維修與故障範圍 | 模組可從外部替換，較容易隔離單一故障 | 光引擎與交換器整合更深，要看實際備援與維修設計 | 平均修復時間、備品、停機範圍與故障率 | 不能只憑位置斷言哪一種一定更可靠 |
| 4. 升級與多供應商彈性 | 模組可依相容規格替換或升級 | 光學、封裝與交換晶片需更早共同設計 | 相容名單、升級週期、第二來源與客戶驗收 | 支援多家供應商不等於所有產品可任意互換 |
| 5. 封裝、測試與生命週期成本 | 模組獨立製造與測試，系統端再插接 | 光學與晶片共同整合，封裝、測試、散熱與良率更緊密 | 合格品良率、測試時間、維修成本、耗電與資本支出 | 製程內容增加不等於封測商毛利一定提高 |

這五把尺不是宣告誰勝出，而是把「省電」和「好維修」放回同一張成本表。共同封裝較可能先
出現在電路長度、功耗或密度壓力最大的連線；可插拔則可能因維修、升級與多供應商彈性繼續
保留。沒有同一部署環境的連接埠比例、耗電、故障與成本資料，就不能做全面替代結論。

## 把五類角色放回同一條光電接力

| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 平台與交換器產品 | 決定交換晶片、連接埠、光學形式與產品時鐘 | NVIDIA 的 Spectrum-X Ethernet Photonics 與 Spectrum-6 | 前者被公司描述為進入生產，後者同代支援兩種形式 | 產品生產不等於已知客戶部署數與全市場占比 |
| 2. 可插拔訊號處理 | 在前面板模組內處理高速訊號與電光轉換 | Marvell Ara 1.6T DSP | 供應商表示已大量出貨給全球客戶 | 「大量」沒有模組數、終端客戶與市場份額分母 |
| 3. 雷射與光源 | 為共同封裝光引擎提供光源 | Lumentum 的磷化銦雷射角色 | 公司公告自己是具名生態系角色 | 自身公告不證明獨家、實際出貨量、收入或毛利 |
| 4. 封裝、組裝與測試 | 把晶片、光學與電路整合並完成製造測試 | NVIDIA 列名 SPIL；ASE 文件確認集團關係 | 平台端列名與公司歸屬可雙向確認 | 列名不等於日月光新增訂單、份額或財務重大性 |
| 5. 客戶部署與營運 | 決定連線位置、驗收、備援、維修與實際使用比例 | 本輪來源沒有可重算的部署分母 | 尚未確認交換器數、連接埠比例與營運結果 | 首批採用名單或展示不能改寫成規模部署 |

角色表說明「誰負責哪一段」，不是完整供應商名單。只有 SPIL 的封裝、組裝與測試角色由
NVIDIA 直接列名並可由 ASE 文件確認公司歸屬；Lumentum 是自身公告的外部雷射角色；Marvell
用來證明可插拔 DSP 路徑仍在出貨。其他台灣公司不得借用這三組證據升級。

## 把兩條產品時鐘放回同一代共存

NVIDIA 把 Spectrum-X Ethernet Photonics 描述為進入產品生產，又說 Spectrum-6 同代支援
可插拔與共同封裝兩種形式；Marvell 同期表示 Ara 1.6T 可插拔 DSP 已大量出貨。這三份一手
資料支持「本階段兩條路並存」的推論，卻沒有告訴我們兩種形式各占多少交換器、連接埠、收入
或網路資本支出。

因此可比較的是各自產品時鐘：共同封裝已有具名產品生產，可插拔也有具名晶片大量出貨。
不能比較的是長期勝負、全市場份額與每埠經濟性；更不能把平台生產直接改寫成台灣供應商財務
貢獻。

## 最後用六關分開產品生產、部署與公司受惠

| 本文六關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 兩種產品路徑已具名 | 平台與供應商公開可插拔、共同封裝的具名產品 | Spectrum-X Ethernet Photonics、Spectrum-6 與 Ara 都有一手產品文件 | 第二個平台用可比較方式公開兩種路徑 | 有產品名稱不等於規模部署或市場成熟 |
| 2. 產品進入持續生產 | 具名產品已從路線圖走到持續製造或大量出貨 | NVIDIA 描述共同封裝產品進入生產；Marvell 描述可插拔 DSP 大量出貨 | 實際出貨數、客戶驗收、期間與退貨／故障資料 | 各公司生產用語不能當成共同量尺 |
| 3. 供應商角色能雙向核對 | 平台端與供應商端對上同一產品、角色與公司 | SPIL 角色與集團關係可核對；Lumentum 有自身具名雷射公告 | 平台與供應商共同確認料號、期間與量產角色 | 生態系列名不能改寫成份額、獨家或訂單金額 |
| 4. 客戶驗收與部署分母出現 | 知道產品用在哪些連線、多少交換器與連接埠 | 尚無可重算的部署位置、交換器數與兩種形式比例 | 客戶驗收、連接埠配置、故障率、修復時間與耗電 | 首批採用者或展示不等於規模部署 |
| 5. 供應商出貨、份額與價格可辨識 | 具名供應商有出貨量、單價、份額、產能利用與重複訂單 | 現有來源沒有 SPIL 或 Lumentum 的產品分母 | 公司文件與客戶文件對上同期間量產出貨 | 平台產品生產不能直接換算供應商營收 |
| 6. 收入、毛利與現金流留下來 | 新增製造內容能接回公司收入、成本、毛利與現金流 | 日月光尚未拆出 Spectrum-X／CPO 的財務貢獻 | 具名產品收入、成本、毛利、資本支出與收款 | 營收成長不等於扣除良率、設備與維修成本後仍受惠 |

本輪兩條架構都能通過第一關，產品端各自走到第二關；SPIL 與 Lumentum 最多提供第三關的
具名角色線索，尚未通過第四到第六關。六關是證據排序，不是技術排名、供應商名單、營收預測
或投資建議。

## 這篇對公司判斷的用處與界線

日月光投控是目前可追的台灣公司入口，因為 NVIDIA 直接列名旗下 SPIL 負責 CPO 晶片級封裝、
組裝與測試；這能確認角色，卻沒有回答產品出貨量、產能利用、收入占比、毛利與資本回報。
頎邦與訊芯等既有研究候選沒有被本輪平台或可插拔文件列名，仍要依自己的正式文件補齊客戶、
料號、驗收與財務證據。

因此研究下一步不是把所有光通訊或矽光子公司排成受惠名單，而是沿六關尋找部署分母、雙向
核對與公司財務足跡。在第四到第六關出現前，本文不支持個股排序、營收推估或投資動作。

## 來源與證據邊界

- [NVIDIA：Vera Rubin 與 Spectrum-X Ethernet Photonics 進入生產，2026-05-31](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)
- [NVIDIA GTC Taipei：列名 TSMC、SPIL、TFC、Foxconn 的製造角色，2026-06-01 更新](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)
- [NVIDIA：Spectrum-6 同時支援可插拔與 CPO，2026-07-21](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)
- [Marvell：Ara 1.6T 可插拔 DSP 大量出貨，2026-03-12](https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html)
- [ASE：SPIL 為日月光投控子公司，2025-01-16](https://www.aseglobal.com/press-room/spil-hosts-nvidia-founder-and-ceo-at-new-factory-site/)
- [Lumentum：Spectrum-X Photonics 的具名 InP laser 生態系角色，2025-03-18](https://investor.lumentum.com/financial-news-releases/news-details/2025/Lumentum-Selected-as-an-NVIDIA-Silicon-Photonics-Ecosystem-Partner-to-Advance-AI-Networking-at-Scale/default.aspx)

**已知：** NVIDIA 將具名共同封裝產品描述為進入生產並直接列名 SPIL；Spectrum-6 與
Marvell 的資料也證明可插拔路徑仍在同代產品與量產生態中。

**還不知道：** 兩種形式的實際出貨配比、部署位置、每埠成本、故障率、台灣供應商收入與
毛利，以及 6147、6451 是否參與上述具名平台。

**不可外推：** NVIDIA、Marvell 與 Lumentum 的效能、角色或成本敘述仍有各自的發行人邊界；
沒有共同部署、價格、估值、共識與部位資料，本題不判斷市場是否已反映。

## 影響路由

對 `packtest` 的方向定為 `mixed`：CPO 增加光電共同封裝與測試內容量，但可插拔持續放量，也表示價值不會一次全部移轉。公司級處理分成「直接列名」與「待自身文件證明」兩層。

<!-- impact
group_id: packtest
stock_ids: 3711
direction: mixed
hypothesis_refs:
note_action: review_due
action_due: 2026-08-15
rationale: SPIL 被 NVIDIA 直接列為 CPO 封裝組裝測試夥伴，需由日月光投控正式文件裁決量產收入與獲利。
evidence_boundary: 平台量產與生態系列名不等於 3711 已有可量化新增訂單；不建立收入、市占或毛利事實，6147與6451僅保留在正文的既有 H# 複核清單。
-->

## 下一個可證明／否定的節點

- **平台層**：首批雲端採用者是否公布 CPO 交換器數量、部署位置、可靠度或節能的實際值；若只停在展示或少量部署，量產解讀要降級。
- **架構層**：Spectrum-6 後續產品組合是否仍維持雙形式；若可插拔占比長期居高且 CPO 未擴到更多場景，「快速替代」假說被否定。
- **公司層**：3711 是否拆出光電共同封裝的收入／毛利；6147、6451 是否由送樣或小量生產轉為正式量產收入。沒有公司文件，就不把平台證據寫進正式筆記事實。
- **經濟層**：新增封裝與測試內容量是否高於所需資本支出、良率爬坡與維修成本；若收入增加但毛利、現金流未改善，受惠只停在營收表面。
