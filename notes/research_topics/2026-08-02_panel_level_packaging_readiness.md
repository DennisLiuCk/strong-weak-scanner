# 面板排得更滿，成品不一定更便宜：要一起看面積、良率、速度與報廢

<!-- research_topic
topic_id: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-06-25
last_reviewed_at: 2026-08-02
review_due: 2026-08-23
source_type: mixed
publisher: Lam Research
publisher_domain: lamresearch.com
canonical_url: https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing
source_chain_id: panel-level-packaging-pilot-readiness-20260802
stock_ids:
group_ids: packtest,semiequip,pcb
trigger_type: advanced_packaging_manufacturing_readiness
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C4
base_confidence: medium
confidence_basis: Lam 的研發中心與製造說明可確認 pilot／early qualification 階段及均勻度、良率、throughput、標準化難題，Applied Materials 的 NEXX 交易提供第二個設備商布局證據；但交易仍待完成，且沒有具名客戶 HVM、good-package yield 或台灣公司財務貢獻
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: official_panel_processing_readiness_sources_captured
evidence: source_chain:panel-level-packaging-pilot-readiness-20260802
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_area_efficiency_pilot_qualification_hvm_and_financial_stages
evidence: sources:S1,S2,S3
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Lam Research
title: Lam Research establishes Panel-Level Packaging Center of Excellence
published_at: 2026-05-20
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE
locator: Salzburg facility、panel-focused wet processing R&D、development／pilot stages、early qualification 與 customer co-development 段落
limitation: 研發中心與 pilot／early qualification 能力不證明具名客戶 HVM、良率、產能、工具訂單或財務貢獻
independence_group: lam-research
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Lam Research
title: From Wafer to Panel: Scaling Advanced Packaging with Panel-Level Processing
published_at: 2026-06-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing
locator: key takeaways；roughly 100x100mm package discussion；uniformity、yield、throughput、automation 與 panel-size standards 段落
limitation: 面積效率與 HVM readiness 是設備商的技術與前瞻敘事；未提供客戶線 good-package yield、cycle time、成本、採用量或收入
independence_group: lam-research
-->

<!-- research_source
source_id: S3
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials broadens advanced packaging portfolio with acquisition of NEXX
published_at: 2026-05-03
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-broadens-advanced-packaging-portfolio
locator: pending acquisition、large-area ECD、panel form factors as large as 510x515mm or more 與 closing conditions 段落
limitation: 交易當時仍待完成；公司對 panel transition、served market 與 customer roadmap 的描述不等於 HVM adoption、交易綜效或財務實現
independence_group: applied-materials
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: Lam Research
title: Lam Research newsroom
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://newsroom.lamresearch.com/
locator: 2026-08-02 建立的 panel qualification、tool release、customer adoption 與 HVM 結果重查入口
limitation: 新聞索引只用來找到後續文件；HVM readiness 或 customer co-development 不能代替實際 qualification 與量產資料
independence_group: lam-research
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: living_index
publisher: Applied Materials
title: Applied Materials investor news releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases
locator: 2026-08-02 建立的 NEXX closing、panel ECD、customer qualification 與財務揭露重查入口
limitation: 新聞索引不證明交易完成、技術整合、客戶採用或收入；每一節點需回到新文件核對
independence_group: applied-materials
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Lam 在 2026-05-20 開設的 Salzburg panel center 是 panel-focused wet processing R&D site，公開定位包含 development、pilot、engineering testing 與 early qualification
supporting_source_ids: S1,S2
contrary_source_ids:
as_of: 2026-06-25
basis: S1 與 S2 直接說明 facility scope、pilot lines、customer co-development 與 early qualification
boundary: R&D／pilot／early qualification 不等於客戶 HVM、量產良率、工具訂單或收入
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: verified
status: active
claim: Lam 將 panel-level processing 的優點描述為大型封裝的面積利用率與擴展性，同時明列 uniformity、yield、throughput、automation 與 panel-size standards 為轉換難題
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-25
basis: S2 key takeaways、wafer-to-panel challenge 與 FAQ 段落逐項列出優點和限制
boundary: 這證實設備商的問題定義，不證明 panel 在客戶線已比 wafer 有較低 good-package cost 或較高經濟良率
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Applied Materials 於 2026-05-03 公告簽約收購 NEXX 以增加 large-area panel-level ECD 能力，並明示交易仍受一般 closing conditions 約束
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-05-03
basis: S3 的 transaction、technology、form factor 與 expected closing 段落
boundary: 簽約不等於交易已完成或整合成功；510x515mm or more 是公司路線描述，不是全產業已採用的單一標準
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: inference
status: active
claim: Panel-level packaging 是否具有商業優勢，應以每個合格大型封裝的總成本判斷，而不能只用方形面板比圓形晶圓的幾何利用率判斷
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-08-02
basis: S2 同時揭示 area efficiency 與 uniformity／yield／throughput／standards 約束，S1 顯示技術仍在 pilot／early qualification，S3 顯示設備布局但交易和採用未完成
boundary: 不量化 wafer 與 panel 的成本差、TAM、市占或台灣公司份額；缺少一致的 panel size、good-package yield、cycle time、設備折舊與材料成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: Panel-level packaging 已在具名 AI accelerator 客戶進入 HVM，或 universe 內封測、設備與 PCB 公司已取得可辨識量產收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源是設備商 R&D／readiness、pilot 與交易布局，沒有具名 end product、HVM yield 或台灣公司財務雙向核對
boundary: 不以大型 AI package 趨勢、panel 工具能力、先進封裝身分或方形載板供應能力直接建立訂單關係
verification_needed: 具名客戶產品、panel form factor、qualification、good-package yield、量產節拍，搭配台灣公司料號、出貨與財務貢獻
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4
metric: Panel-level packaging 的交易完成、form-factor 標準、客戶 qualification、good-package yield、throughput 與 HVM 狀態
source_ids: S1,S2,S3
watch_source_ids: S4,S5
frequency: event_driven
frequency_detail: 設備商、OSAT、基板商或 AI 平台公布 panel qualification／HVM／standard 時重審
next_check: 2026-08-23
trigger: 具名客戶產品披露 panel size、qualification 與可定位的 good-package yield／throughput，或 NEXX 交易完成並出現整合與出貨證據
invalidation: 量產仍受 panel 標準、翹曲、均勻度、良率或節拍阻擋，pilot 長期無法轉入 HVM，則商業急迫性下修
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: 台灣封測、設備與 PCB 公司在 panel-level packaging 的具名客戶、料號、量產與財務貢獻
source_ids: S1,S3
watch_source_ids: S4,S5
frequency: quarterly
frequency_detail: 每季法說與財報檢查客戶 qualification、panel 工具／基板出貨、收入占比與毛利
next_check: 2026-10-31
trigger: 台灣公司與客戶對同一 panel 產品或流程完成雙向核對，並揭露量產出貨或財務資訊
invalidation: 公司只描述先進封裝或大尺寸基板機會，未披露 form factor、客戶、qualification 與財務足跡
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
reason: editorial_plain_language_wave4_packaging_learning_no_conclusion_change
evidence: editorial:plain_language_wave4
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave95_panel_cost_four_measures_production_chain_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **面板級封裝（Panel-level packaging，PLP）**：用方形或長方形大面板處理多顆封裝，而不是只在圓形晶圓上排版；載體形狀改變不會自動解決良率與成本。
- **圓形晶圓（Wafer）**：半導體製程常用的圓形基板；排入大型方形封裝時，圓周邊緣可能留下較多無法使用的面積。
- **方形面板（Panel）**：面板級製程使用的方形或長方形大載體；可排版面積較完整，但尺寸越大也越難維持平整與均勻。
- **面板載體**：承接重佈線、金屬與封裝結構的大面積基板；材料、厚度與搬運方式都會影響製程結果。
- **面板尺寸標準**：設備、材料、載具與自動化共同採用的長寬與厚度規格；單一公司的可處理尺寸不等於全產業共同標準。
- **面積利用率**：可用來排入產品的面積占載體可用面積的比例；它回答幾何效率，不等於最後合格品比例。
- **理論可排數**：依產品尺寸與版圖估算一片載體最多能放多少顆；尚未扣除製程缺陷、測試失敗與報廢。
- **投入數**：進入指定製程或良率計算的面板、封裝或產品數；比較良率前必須先確認分母定義相同。
- **合格品**：通過指定電性、尺寸與可靠度要求、可以交付的產品；「做出來」與「合格可交付」是兩個不同節點。
- **合格封裝良率（Good-package yield）**：最終合格封裝數占投入封裝數的比例；必須說明測試條件、分母與產品規格才能比較。
- **大面積均勻度（Uniformity）**：面板中央與邊緣的厚度、線寬、清洗、沉積或蝕刻結果是否一致。
- **翹曲**：面板受材料、溫度或應力影響而彎曲；翹曲會干擾曝光、搬運、對準與接合。
- **邊緣控制**：管理面板邊緣的厚度、圖形與缺陷；平均值達標不代表中央與邊緣都合格。
- **缺陷分布**：缺陷在整片面板上的位置與密度；同樣缺陷數若集中在關鍵區域，可能造成不同報廢結果。
- **良率管理**：追蹤缺陷來源、製程漂移、測試失敗與返工，讓合格比例能在連續批次維持穩定。
- **製程週期（Cycle time）**：一片面板從進站到完成指定流程所需的時間；面板較大不代表處理時間一定相同。
- **單位時間產出（Throughput）**：設備或產線每小時真正完成的面板或合格品數；要連同良率、停機與返工一起看。
- **設備利用率**：設備可生產時間中實際投入製造的比例；等待、換線、保養與故障都會壓低有效產出。
- **停機時間**：設備因故障、清潔、保養、調整或等待材料而不能生產的時間。
- **自動搬運**：用機械與控制系統移動、定位及追蹤大面板；尺寸與翹曲變化會增加破損、卡料與定位風險。
- **返工**：產品未一次達標後，仍能重新處理或修復的流程；返工會增加時間、材料與再次失敗的風險。
- **報廢**：產品或整片面板無法再使用而必須丟棄；一片面板排得越多，整片失敗時可能損失越多產品。
- **可靠度**：產品經過溫度、濕度、機械與長時間使用後仍能維持功能；短期測試通過不能替代長期驗證。
- **每顆合格品總成本**：把面板、材料、設備折舊、製程時間、返工與報廢等成本，除以最後可交付的合格品數。
- **電鍍沉積（ECD）**：用電化學方式形成銅等金屬層；大面積處理時要同時控制厚度與跨面板均勻度。
- **薄膜沉積（PVD／CVD）**：用物理或化學方式形成薄膜的製程；設備能處理大面板，不等於厚度與缺陷已達量產要求。
- **蝕刻（Etch）**：選擇性移除材料以形成線路或結構；大面積線寬與深度的一致性會影響後續良率。
- **微影（Lithography）**：把電路圖形轉印到材料表面的製程；大面板曝光、對準與翹曲控制需一起驗證。
- **試產線（Pilot line）**：用來調整製程與做工程測試的小量產線；能試做不等於已具備穩定大量生產能力。
- **客戶資格認證（Qualification）**：客戶依功能、可靠度與製造條件確認產品是否可採用；早期共同開發還不能替代具名產品認證。
- **穩定大量生產（HVM）**：連續生產時同時守住良率、產出速度、可靠度與成本，而不是只完成一次樣品或工程批次。
- **NEXX**：Applied Materials 宣布簽約收購、用來補強大型面板電鍍能力的設備公司；簽約不等於交易完成、整合成功或客戶量產。

### 三句話抓重點

- 方形面板能利用更多邊角、一次排進更多大型封裝；這只回答「排得下多少」，還沒回答最後能做出多少合格品。
- 本輪公開資料只確認研發場域、試產與早期認證能力，也指出大面積均勻度、良率、產出速度、自動搬運與尺寸標準仍是量產難題。
- 目前沒有具名產品的合格品良率、穩定產能、可靠度與財務貢獻，因此不能把「排得更多」直接讀成「每顆更便宜」或台灣公司已受惠。

### 為什麼重要

大型人工智慧封裝要把運算晶片、記憶體與輸入輸出晶片放在同一載體上，產品變大後，圓形晶圓
邊緣的排版損失會更明顯。方形面板可能減少幾何浪費，卻也把難題放大到整片平整度、中央與邊緣
一致性、搬運、返工與整片報廢。真正的成本問題不是「一片能排幾顆」，而是「一小時能穩定交付
幾顆合格品，以及為此花了多少材料、設備與失敗成本」。

### 接下來怎麼追

- 先標記新資料位於研發場域、試產與工程測試、早期認證、具名產品認證、穩定量產或財務貢獻哪一關。
- 比較同一產品時，同時核對面板尺寸、理論可排數、投入數、合格品良率、每小時產出、停機、返工、報廢與可靠度。
- 公司映射要讓客戶端的具名產品與供應商端的設備、材料、量產出貨及財務資料互相對上，缺一邊就維持待驗證。

### 想一想

- 面板一次排得下更多封裝，若報廢增加、製程變慢，每顆合格品還會更便宜嗎？
- 大面板的平均厚度達標時，中央與邊緣仍可能有哪些翹曲、線寬、清洗與搬運問題？
- 一座試產線能做工程批次後，還要看到哪些具名產品、連續良率、產出、可靠度與財務資料才算量產成熟？

## 先用四把尺拆開「更便宜」

| 本文四把尺 | 它先回答什麼 | 最簡單的關係 | 容易忽略什麼 | 不能直接推成 |
|---|---|---|---|---|
| 1. 面積利用率 | 一片載體有多少面積真的排進產品？ | 可排產品面積 ÷ 載體可用面積 | 產品尺寸、邊緣留白與不同排版規則 | 面積用得滿，不等於做出的產品都合格 |
| 2. 合格封裝良率 | 投入後最後有多少產品可交付？ | 最終合格封裝數 ÷ 投入封裝數 | 缺陷分布、測試條件、返工與可靠度 | 幾何效率較高，不等於最終良率較高 |
| 3. 單位時間合格產出 | 一小時真正做出多少合格品？ | 每小時完成面板數 × 每片可排數 × 合格封裝良率 | 製程週期、停機、換線、搬運與設備利用率 | 面板較大，不等於每小時合格產出較高 |
| 4. 每顆合格品總成本 | 每交付一顆合格品，實際付出多少？ | 面板、材料、折舊、時間、返工與報廢成本 ÷ 最終合格品數 | 產能利用、整片損失、長期可靠度與重複生產 | 其中一把尺改善，不等於總成本一定下降 |

四把尺要按順序接起來：排得下更多，只增加理論機會；做得良、做得快且失敗成本受控，才可能
降低每顆合格品總成本。這是本文的成本讀法，不是跨公司的成本比較、價格預測或投資排序。

## 再看五個生產關卡如何接力

| 本文五個生產關卡 | 先回答什麼 | 主要接力角色 | 過不了會怎樣 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 載體與共同尺寸 | 面板的長寬、厚度、材料與載具能否被整條產線共同處理？ | 面板／基板、材料、設備與自動搬運團隊 | 每站可處理尺寸不同，轉站、搬運與良率無法穩定 | 設備商已展示大型面板能力，但生態系仍在決定共同尺寸 |
| 2. 圖形、金屬與均勻度 | 中央與邊緣的曝光、沉積、蝕刻、清洗與線寬能否一起達標？ | 微影、電鍍、薄膜、蝕刻、清洗與量測設備 | 平均值看似合格，局部產品仍因厚度或圖形偏差失敗 | 公開資料列出多種製程能力與大面積均勻度難題；沒有客戶線分布 |
| 3. 翹曲、搬運與缺陷 | 大面板能否保持平整、乾淨並在各站安全移動？ | 材料、載具、自動化、製程整合與維修團隊 | 卡料、破損、定位偏差或整片缺陷讓理論可排數失去意義 | 公開資料把自動化與大面積製程列為轉換難題；沒有停機與報廢數據 |
| 4. 封裝整合、測試與認證 | 完整封裝能否通過電性、尺寸與長期可靠度？ | 封測、測試、產品客戶與可靠度團隊 | 製程做得出來，成品仍不能交付或需要大量返工 | 場域定位包含工程測試與早期認證；沒有具名產品認證結果 |
| 5. 良率、產出與財務 | 合格品比例、每小時產出與總成本能否在連續批次維持？ | 製造營運、設備維護、品質、客戶與財務團隊 | 技術可做卻產量不足、成本過高或無法形成重複收入 | 沒有具名產品的合格品良率、產出速度、成本、出貨或收入 |

五個關卡是接力關係：前一關達標不會替下一關畢業。這是本文用來找資料與分責任的地圖，不是
完整製程規格、供應商名單、訂單判定或公司快慢排名。

## 最後用六關分開研發能力與收入

| 本文六關 | 這一關要證明 | 本輪公開資料 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 研發場域與設備能力 | 有可處理大面板的場域、工具與製程入口 | Lam 開設面板濕製程研發中心；Applied 簽約收購 NEXX 以補大型面板電鍍能力 | 交易完成、工具整合與可核對的設備規格 | 研發中心或簽約不等於客戶已認證、交易已整合或形成收入 |
| 2. 試產與工程測試 | 製程能在試產線重複運作並留下缺陷與量測結果 | Lam 將場域定位涵蓋試產與工程測試 | 重複批次、跨面板分布、停機、返工與報廢資料 | 場域具備試產能力，不等於已有具名產品試產結果 |
| 3. 早期共同開發與認證 | 客戶把目標產品帶入早期測試，開始核對製程條件 | Lam 將客戶共同開發與早期認證列入場域定位 | 具名客戶、產品、面板尺寸、測試條件與結果 | 未具名的早期認證能力不等於產品已通過資格認證 |
| 4. 共同尺寸與具名產品認證 | 設備、材料與客戶對上同一面板規格，產品通過功能與可靠度 | 未公開 | 客戶與製造端共同揭露面板規格、產品與認證結果 | 單一設備可處理的最大尺寸不是共同標準，也不是產品認證 |
| 5. 穩定大量生產 | 良率、每小時產出、停機、返工、可靠度與成本能持續達標 | 未公開 | 具名產品的連續批次良率、產出、設備利用與可靠度 | 樣品、工程批次或量產準備敘事不等於穩定大量生產 |
| 6. 重複出貨與形成收入 | 供應商產品或服務可重複交付並反映在財務 | 未公開 | 客戶與供應商雙向核對料號、量產出貨、收入或毛利 | 製程需要某類設備、材料或基板不等於台灣公司已受惠 |

本輪資料涵蓋第 1～3 關的場域與能力定位，但沒有第 2、3 關的具名產品結果，第 4～6 關也仍缺
證據。六關是本文的查證順序，不是共同產業標準，也不替公司建立量產名次、訂單、份額或投資排序。

## 來源與證據邊界

- [Lam：Panel-Level Packaging Center of Excellence](https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE)
- [Lam：From Wafer to Panel](https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing)
- [Applied Materials：pending NEXX acquisition and panel-level ECD](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-broadens-advanced-packaging-portfolio)

Lam 與 Applied Materials 都是設備商，對產業採用、產品優勢與量產準備有商業立場。本篇只把
它們直接揭露的研發場域、製程問題與交易狀態標成已證實；「面板級封裝將更便宜」與「台灣公司
已受惠」均未被當成事實。

## 影響路由

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: OSAT 可能承擔 panel process integration、良率與可靠度，但本輪沒有 universe 公司具名 HVM 產品與財務證據
evidence_boundary: 先進封裝產能、fan-out 能力或大型 AI package 討論不等於 panel-level 客戶 qualification、訂單或毛利
-->

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: ECD、PVD、CVD、etch、clean、lithography、metrology 與 automation 都是 panel 工具入口，但具名證據集中在 Lam、Applied 與 NEXX
evidence_boundary: 製程需要某類設備不等於任一台灣設備商能處理目標 panel size、已通過 qualification 或取得量產收入
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-10-31
rationale: 大型基板與 panel form factor 可能改變載板材料、尺寸與製程路由，但尚無 universe PCB／CCL 公司具名採用證據
evidence_boundary: 方形基板、ABF 載板或大尺寸板能力不能自動等同先進 panel-level packaging 量產供應
-->

## 下一個可證明／否定的節點

- NEXX 交易完成與實際整合結果，而不是沿用簽約日的前瞻敘述。
- 具名人工智慧封裝或委外封測廠公布面板尺寸、客戶資格認證、合格封裝良率、單位時間產出與可靠度。
- 設備、材料與基板公司對同一客戶面板流程完成雙向核對，並出現量產及財務資料。
- 若面板尺寸標準長期分裂、試產無法進入穩定大量生產，或每顆合格品成本不優於晶圓路徑，研究優先級應下修。
