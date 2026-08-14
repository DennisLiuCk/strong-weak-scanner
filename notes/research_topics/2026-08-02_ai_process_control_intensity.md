# AI 製程控制強度：HBM 與 2.5D／3D 把良率學習推向先進封裝

<!-- research_topic
topic_id: MI-2026-08-02-AI-PROCESS-CONTROL-INTENSITY
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-02
source_published_at: 2026-07-28
last_reviewed_at: 2026-08-14
review_due: 2026-08-15
source_type: mixed
publisher: KLA Corporation
publisher_domain: ir.kla.com
canonical_url: https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full
source_chain_id: kla-fy26q4-process-control-20260728
stock_ids:
group_ids: semiequip,material,pcb,packtest
trigger_type: industry_results_and_product_qualification
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C22
base_confidence: medium
confidence_basis: KLA、Applied Materials、Onto Innovation、Camtek 與 Nova 的一手來源共同支持工程需求、客戶資格、供應商量產陳述、具名工具未來訂單與不同寬度的收入訊號；Camtek 又提供先進封裝約占公司收入四分之三的近似公司口徑，但未標明量測期間，且 Nova／Onto 都未拆出題材收入金額。現有資料仍沒有兩條獨立、同期間的題材分子—公司或客戶分母橋接，也沒有全產業 wallet share、台灣公司訂單或良率結果
cross_company_numbers: true
-->

<!-- transition
date: 2026-08-02
from: initial
to: inbox
reason: primary_source_process_control_scan
evidence: source_chain:kla-fy26q4-process-control-20260728
-->
<!-- transition
date: 2026-08-02
from: inbox
to: triaged
reason: separated_engineering_need_and_qualification_from_industry_wallet_share_and_taiwan_orders
evidence: sources:S1,S2,S3
-->
<!-- transition
date: 2026-08-09
from: triaged
to: triaged
reason: editorial_plain_language_wave3_no_conclusion_change
evidence: editorial:plain_language_wave3
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: onto_q2_bounded_revenue_signal_superseded_engineering_only_synthesis
evidence: sources:S8
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: editorial_process_control_loop_and_failure_map_for_beginner_learning
evidence: sources:S2,S9
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_control_plan_sampling_sensitivity_false_alarm_cycle_time_and_containment_without_refreshing_thesis_clock
evidence: sources:S10,S11,S12
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_measurement_system_contract_before_process_control_decisions_without_refreshing_thesis_clock
evidence: sources:S14,S15
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: camtek_named_orders_and_bounded_advanced_packaging_revenue_mix_plus_nova_category_record_superseded_broad_revenue_only_synthesis
evidence: sources:S16,S17,S18,S19
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: taiwan_equipment_category_and_product_capability_mapped_without_refreshing_thesis_clock
evidence: sources:S20,S21,S22,S23,S24
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: applied_advanced_packaging_forecast_denominator_separated_from_process_control_numerator_without_refreshing_thesis_clock
evidence: sources:S25
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: applied_fy26q3_company_segment_application_and_two_superset_forecasts_mapped_without_refreshing_thesis_clock
evidence: sources:S26,S27
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: defect_signal_classification_criticality_containment_and_yield_ladder_added_without_thesis_or_clock_refresh
evidence: sources:S28,S29,S30
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: alarm_validation_containment_genealogy_disposition_and_release_event_passport_added_without_thesis_or_clock_refresh
evidence: sources:S31,S32,S33
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_defect_threshold_base_rate_review_load_and_miss_cost_crossover_without_thesis_or_clock_refresh
evidence: sources:S28,S29,S34
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **製程控制**：在製造途中用量測、檢查與缺陷分析找出偏差，再把結果回饋到製程調整；它不同於封裝完成後才判定成品良否的成品最終測試（ATE final test）。
- **HBM**：把多層記憶體垂直堆疊的高頻寬記憶體；堆疊越複雜，晚發現缺陷的代價越高。
- **DRAM**：以電容儲存位元、需持續更新電荷的動態隨機存取記憶體；HBM 使用 DRAM die，但一般 DRAM、HBM 與整體記憶體設備收入不是同一個分子。
- **2.5D／3D 封裝**：把多顆晶片並排連接或上下堆疊；技術名稱不代表已通過客戶驗證。
- **量測／檢查**：前者確認尺寸與材料是否合規，後者尋找顆粒、刮傷或接合不良。
- **良率學習**：把缺陷資料回饋製程、找出報廢原因；不同於成品階段的最終測試。
- **設備預算占比（wallet share）**：客戶全部設備支出中，分給某類工具的比例；工程更重要不等於預算占比已上升。
- **財政年度第 4 季（FY26Q4）**：公司依自己的會計年度命名季度；它不一定等於曆年的第四季，跨公司閱讀時要先對齊期間。
- **電子束檢測（eBeam）**：用電子束觀察極細微結構與缺陷的量測方法；能看得更細不等於每一道製程都需要新增一台工具。
- **製程視窗（process window）**：一道製程可穩定做出合格結果的參數範圍；視窗越窄，微小漂移越容易變成缺陷。
- **TSV（矽穿孔）**：穿過矽晶片的垂直導電通道，常用於堆疊晶片；蝕刻深寬比、填孔空洞與介電層品質都可能成為控制點。
- **RDL（重佈線層）**：把晶片接點重新拉線到封裝所需位置的細金屬線路；線寬、間距與面板翹曲會影響可製造性。
- **翹曲（warpage）**：晶圓、面板或封裝受材料與溫度影響而彎曲；它會增加對位、量測與接合難度。
- **關鍵缺陷／雜訊缺陷（critical／nuisance defect）**：前者會傷害良率或可靠度，後者雖被工具看見卻未必影響產品；分類能力會影響工程師是否把時間用在真正重要的異常。
- **混淆矩陣（confusion matrix）**：把參考真值的「有／無目標缺陷」和系統判定的「有／無標記」交叉成 TP、FP、FN、TN 四格；四格的分母、真值方法與門檻版本都要固定，不能只報總缺陷數。
- **母體基準率（base rate／prevalence）**：受檢母體中真正有目標關鍵缺陷的比例；當缺陷很少，即使偽警報率看似不高，乾淨單位的龐大分母仍可能產生大量 FP。
- **召回率（recall／TPR）**：真正有目標缺陷的單位中，被系統標記出的比例，公式為 `TP ÷ (TP + FN)`；高 recall 仍不代表被標記者大多是真的。
- **偽陽性率（FPR）**：真正沒有目標缺陷的單位中，被錯誤標記的比例，公式為 `FP ÷ (FP + TN)`；它的分母和 precision 不同。
- **精確率（precision／PPV）**：所有被系統標記的候選中，經參考真值確認為真正目標缺陷的比例，公式為 `TP ÷ (TP + FP)`。
- **準確率（accuracy）**：全部受檢單位中判對的比例，公式為 `(TP + TN) ÷ 全母體`；在極度不平衡的母體裡可能看起來很高，卻遮住漏失或複判負荷。
- **錯判成本比**：把一個 FN／escape 的後果換成多少個 FP／複判工作量的假想比較單位；它必須由產品風險與工廠流程定義，不能從模型分數自動得出。
- **Killer defect（致命缺陷）**：在指定產品、結構與位置下足以造成電性失效、可靠度問題或良率損失的缺陷；同一種物理偏差換了產品或位置，影響可能不同。
- **Fab（製造廠）**：執行晶圓或封裝製造的工廠；本篇出現的 Intelligent Packaging Fab 是台積電對智慧先進封裝廠的命名，不是通用績效認證。
- **MES（製造執行系統）**：連接工單、設備、材料、製程站點與在製品紀錄的工廠資訊系統，讓派工、追溯與異常處置使用同一批次脈絡。
- **ADC（自動缺陷分類）**：automated defect classification，以規則或模型把檢查候選分到可處置的缺陷類別；自動分類仍需參考真值與錯誤代價才能評估。
- **機器學習（ML）**：讓模型從資料學習分類或預測規則的方法；模型分數、loss function 或離線 accuracy 不會自行決定量產門檻，仍要接參考真值、錯判成本與變更控制。
- **抽樣（sampling）**：只檢查部分晶圓、區域或製程批次，以速度換取資訊；抽樣較少不代表沒有風險，檢查較多也不保證能找到正確根因。
- **Control plan（製程控制計畫）**：先定義要攔截的失效、在哪一道工序看、抽樣多少、看多細、多久得到結果，以及異常發生後要採取什麼動作的製造規則。
- **OCAP（out-of-control action plan，失控處置計畫）**：監控訊號判定製程可能失控後，預先指定確認、責任人、停機／隔離、調查、修正與復機條件的流程；警報本身不是 OCAP 已執行。
- **Genealogy（製造履歷／系譜）**：把 lot、wafer、die、package 與經過的站點、機台、recipe、材料批次及時間連起來，供異常時界定可能受影響物件；可追到不等於已證明哪一項是根因。
- **Containment（圍堵）**：先阻止可疑材料、批次或設備繼續流動或放行，以限制風險擴大；它是暫時風險控制，不等於已完成根因分析、永久修正或良率改善。
- **`t0`～`t8` 事件時間**：本文為九個查核事件使用的研究標記，從最後已證實在控一路到修正後放行；它不是任何工廠的共同欄位名稱，也不表示九格都已公開。
- **Unique ID（唯一識別）**：讓同一 die、package 或其他物件在不同站點仍能被辨認的鍵；只有 ID 還不夠，必須再連事件時間、路由、工具、recipe 與材料資料才能重建影響範圍。
- **缺陷逃逸（defect escape）**：真正會影響良率或可靠度的缺陷沒有被現行檢查攔截，繼續流到後續製程或客戶端。
- **偽警報／雜訊（false alarm／nuisance）**：工具標記了異常候選，但複判後不屬於會傷害產品的關鍵缺陷；過多會消耗複判時間並延後真正異常的處理。
- **週期時間（cycle time）**：產品或資料走完指定製造、量測、複判與決策流程所需的時間；結果太慢，前方產線可能已累積更多受影響批次。
- **處置（disposition）**：依檢查結果決定放行、重工、報廢、隔離或追加檢查；它和找根因是相關但不同的工作。
- **虛擬量測（virtual metrology）**：用設備感測器與製程資料估計原本要靠實體量測得到的結果；它可輔助抽樣，但仍受模型漂移、校正資料與不確定性限制。
- **CMP（化學機械研磨）**：同時用化學反應與機械研磨把表面整平；本文引用的 NIST 公開資料用它示範動態抽樣方法，不代表 HBM 量產配方。
- **FAR（false-alarm rate，偽警報率）**：被系統標成異常、但複判後不是目標關鍵缺陷的比例；分母與缺陷定義不同時不能直接比較。
- **SEMVision 電子束系統**：Applied Materials 的缺陷複判產品系列；本文只用公司公告拆解速度、靈敏度、覆蓋與雜訊分類，不採用它推算市場規模。
- **ICOS**：KLA 的封裝檢查與量測產品系列名稱；不同型號對應切割後裂縫、元件外觀或量測等任務，不能合併成全產線的單一覆蓋率。
- **Dragonfly G5**：Onto Innovation 的檢查系統名稱；本文只引用公司揭露的資格節點，不把產品名稱等同 HBM 收入。
- **Hawk／Eagle G5**：Camtek 的先進封裝檢查與量測平台；具名訂單或公司預期占比不等於已交付、已認列收入或客戶端良率實績。
- **Sentronics**：Nova 的尺寸量測產品線；本文只引用公司對 advanced-packaging 銷售創高的陳述，不把產品線名稱當成已揭露的題材金額。
- **AOI（自動光學檢查）**：用相機、光學與演算法自動尋找外觀或幾何異常；產品清單出現 AOI，只證明公司列示該能力，不代表已通過具名客戶量產驗證或已拆出收入。
- **GAAP**：一般公認會計原則；本文的 `M1` 對齊兩家公司依 GAAP 報告的總營收，但會計口徑一致仍不會自動產生 AP 題材分子。
- **Financial highlights**：公司結果公告的重點摘要；它可快速定位數字，仍要回到完整財務表、期間、定義與附註確認分子分母。
- **OSAT／tier-1**：OSAT 是委外半導體封裝測試廠；`tier-1` 是 Camtek 對該客戶層級的匿名描述，不是客戶名稱或第三方排名。
- **non-AI／non-AI AP**：不以 AI 應用為主要歸類的收入／先進封裝收入；它和 HPC／AI 一起構成 Camtek 簡報的較寬 AP 組合，不能當成 HBM-only 分子。
- **CPO（Co-Packaged Optics，共同封裝光學）**：把光學引擎放到交換晶片附近的封裝路徑；本文只把它當作對位、污染與跨領域控制的相鄰案例，不推論其工具組合等同 HBM。
- **Packaging（封裝）**：把晶片接合、互連並保護成可使用元件的製造階段；`advanced packaging` 是較複雜的整合路徑，不是單一產品或單一設備類別。
- **Specialty Devices and Advanced Packaging**：Onto 使用的較寬事業組合名稱；它同時涵蓋多種應用，不能直接當成 HBM、2.5D 或 Dragonfly 的收入分子。
- **被測量（measurand）**：真正要量的性質，例如某層厚度、線寬、翹曲或缺陷尺寸；只寫設備名稱，還沒有說清楚量的是什麼。
- **準確度／偏差（accuracy／bias）**：準確度描述結果和參考值是否接近；偏差則把多次量測平均值與參考值之間的系統性差距量化。每次結果很集中，仍可能一起偏離目標。
- **重複性／再現性／穩定性（repeatability／reproducibility／stability）**：重複性看相同設備、設定與短時間條件下是否一致；再現性看跨日期、設備、操作或環境是否仍一致；穩定性再追更長時間是否漂移。不同標準對 `reproducibility` 的細部定義可能不同，本文只採 NIST／SEMATECH 該章的使用邊界。
- **量測不確定度（measurement uncertainty）**：量完之後對真值仍保留多少合理疑問；它不是「量錯了」的同義詞，而是判斷結果能否支撐放行、隔離或調參時不可缺的尺度。
- **計量可追溯性（metrological traceability）**：特定量測結果可經由有文件紀錄、不中斷的校正鏈連到指定參考，而且每一環都把自己的不確定度納入；它是結果的性質，不是設備或實驗室的永久標籤。
- **Gauge R＆R（量具重複性與再現性研究）**：用規劃好的重複量測，拆解設備、操作、日期、設定或樣品等來源造成的變異；一次短期研究不能自動代表日後長期穩定，也不能替代偏差與不確定度評估。
- **公開資訊觀測站（MOPS）**：台灣上市櫃公司的正式申報入口；要用它找具名產品、客戶階段與財務揭露，不能只靠海外設備商說法推導台灣公司受惠。
- **訂單（order intake）**：客戶已下單、但公司尚未必完成交付或符合營收認列條件的商業承諾；訂單金額不能直接當成同季營收。
- **營收認列（revenue recognition）**：公司在交付與會計條件成立後列入財報的收入；何時認列、認列多少，可能和接單日不同。
- **題材分子／公司分母**：題材分子是可歸屬於先進封裝製程控制的收入或訂單，公司分母是同期間公司總收入或總訂單；兩者期間、範圍與會計狀態一致，比例才有意義。
- **成長指數**：只說未來值相對基期增減多少，例如「Q4 比 Q1 高約 70%」；若沒有基期金額，它能表示方向，不能還原絕對收入。
- **設備類別比重**：公司自訂的一大類設備收入占總收入比例；即使名稱含「半導體」或「製程」，仍可能混合點膠、搬運、接合、檢查與量測，不能直接當成製程控制題材分子。
- **產品—商業護照**：把具名產品與任務、客戶階段、會計狀態、同期間分子與分母綁在同一筆證據；少一欄就停在較早的成熟度，不用相鄰名詞補空格。
- **Master Class**：Applied 對投資人與產業讀者發布的主題式技術／商業說明會；prepared remarks 是發行人一手資料，但其中的市場、排名、採用與預測仍是公司陳述。
- **VeritySEM 7AP／SEMVision G7AP**：Applied 分別定位為先進封裝 eBeam 尺寸量測與缺陷複判／分類工具；型號已被公司稱為 production，不代表公開資料已拆出各自收入或客戶端成效。
- **PDC（Process Diagnostics and Control，製程診斷與控制）**：Applied 使用的較寬產品類別，涵蓋不同晶圓製造與封裝應用；類別成長不等於其中 AP 子集合以相同比率成長。
- **FY26Q3**：Applied 依自己的財政年度命名、截至 2026 年 7 月 26 日的一季；不是一般曆年第三季，本文只按公司報告期間使用。
- **AP-specific PDC（先進封裝專屬製程診斷與控制）**：同時可歸屬 advanced packaging 與 PDC 的收入、訂單或工具分子；公司總營收、部門營收、全部 AP 或全部 PDC 都比它寬。
- **集合與交集**：若 `A` 代表全部 advanced-packaging revenue、`P` 代表全部 PDC revenue，本文真正要找的是同時屬於兩者的 `A ∩ P`；兩個大集合各自成長，仍不能唯一決定交集大小或成長率。
- **客戶應用組合（customer application mix）**：把部門收入按客戶製造應用分成 foundry／logic／other、DRAM、flash 等類別；它不是產品組合，也沒有把 AP 或 PDC 收入單獨拆出。
- **Applied 定義的 CY26**：本次簡報明定為 FQ2'26～FQ1'27，且 FQ1'27 是 14 週季度；不是一般 1～12 月曆年，跨公司比較前必須先對齊期間。

### 三句話抓重點

- 五家設備商的一手文件，分別說明需求方向、缺陷為何更昂貴、設備走到客戶驗證／未來交付的哪一步，以及不同寬度的訂單與收入訊號。
- 真正要查的是：每一代產品的 control plan 是否改變抽樣覆蓋、靈敏度、偽警報、週期時間與圍堵動作，而不只是設備名稱變多。
- Camtek 已提供較接近題材分子—公司分母的近似收入組合，但期間未標明；Applied FY26Q3 又證明 AP 與 PDC 兩個廣義集合各自成長仍解不出交集；弘塑、均華與萬潤的廣義設備收入、產品清單與研發計畫也不能替代具名製程控制分子。

### 為什麼重要

先進封裝把多顆昂貴晶片連在一起。若其中一顆在最後才被發現有缺陷，先前投入的晶片、封裝
材料與製程時間可能一起損失，因此越早找到問題越有價值。

但「更需要檢查」和「設備市場一定變大」仍是兩個問題。新工具、客戶驗證或一個較寬事業
組合的收入新高，只說明工程需求、採用節點與供應商商業訊號；產業的獲利池是否擴大，還要
看實際新增的步驟、工具數、採購金額與收入組成。

### 接下來怎麼追

- 追設備商是否揭露有期間與定義的訂單、收入、工具數或量產採用。
- 追客戶端是否公布缺陷攔截、良率學習週期、重工／報廢改善與每單位產能支出。
- 追同一產品世代的 control plan 是否公開抽樣單位、覆蓋範圍、靈敏度／逃逸、偽警報、結果時間與異常處置，避免把單一設備速度當成完整製程改善。
- 追客戶端能否把 inspection flag、複判真值、killer／non-killer 分類、圍堵與同一產品的良率／重工／報廢接成一條可重算鏈。
- 追公開資訊觀測站是否出現台灣公司的具名產品、客戶階段與財務貢獻。

### 想一想

- 若成長主要來自市占、漲價、產品組合或服務，主命題應如何縮小？
- 一套工具通過一名客戶認證，還缺哪些證據才能推論成產業錢包占比上升？
- 如果靈敏度提高卻同時產生大量偽警報、拖長複判時間，這份 control plan 一定更好嗎？
- 缺陷候選數上升，究竟是製程變差、覆蓋增加、門檻變敏感，還是分類定義改版？沒有四格分母時能分辨嗎？
- 如果同一個標準樣品每次都量得很接近、卻全部偏離參考值，這套系統是精密、準確，還是兩者兼具？
- 設備貼著校正標籤，是否就能證明今天這個產品、這個方法與這次結果都可追溯且適合拿來判定放行？
- 若公司只說「先進封裝事業創新高」，卻沒有產品分子與公司分母，你能安全地推論到哪一層？
- 若三家公司都公布「設備占營收九成上下」，但設備定義不同、也沒有檢查／量測分子，能否用百分比排出誰的製程控制曝險較高？

## 用一條回饋迴路理解製程控制

### 第一步：先看見偏差

量測回答尺寸、厚度或材料是否落在規格內；檢查則尋找顆粒、刮傷、翹曲與接合不良。兩者都
發生在產品完成之前，目的不是替成品打分數，而是及早知道哪一道製程開始偏離。

### 第二步：找出原因並調整製程

看到缺陷之後，工程師要把位置、形狀與發生條件連回設備參數、材料批次或製程步驟。若資料
只停在「發現一個壞點」，就還沒有形成良率學習；能找到根因並回頭調整，才是完整的回饋迴路。

### 第三步：再判斷商業價值落在哪裡

同一個工程問題可能由新增工具、既有設備升級、更聰明的抽樣，或設計規則改善來解決。因此
研究者要追的是每代新增多少步驟、哪些工具進入重複採購，以及收入來自工具數、價格、服務
還是市占變動。只有把這些來源拆開，才能判斷需求是否真的擴大。

對台灣族群也要走完同一條路：公司先具名產品，再說明客戶驗證或量產階段，最後才看得到
訂單、收入或毛利。海外設備商說「先進封裝更需要製程控制」，只能建立搜尋方向，不能替本地
公司完成後面三步。

## 一個控制閉環，其實包含五種不同工作

「製程控制設備」不是單一機器的同義詞。新手可以先把閉環拆成五種工作；同一平台可能做
其中數項，也可能由不同工具與軟體接力，因此不能看到五個名詞就直接推論需要五台新設備。

| 工作 | 它回答的問題 | 常見輸出 | 研究時最容易誤讀之處 |
|---|---|---|---|
| 量測 | 尺寸、厚度、形貌或材料是否落在規格內？ | CD、膜厚、翹曲或形貌資料 | 數值更精細不等於每片、每層都全面量測 |
| 檢查 | 哪裡出現顆粒、刮傷、空洞、對位或接合異常？ | 缺陷位置、影像與分布圖 | 找到更多訊號不等於找到更多會傷害良率的缺陷 |
| 缺陷複判與分類 | 哪些是關鍵缺陷，哪些只是雜訊？ | 缺陷類別、嚴重度與複判結果 | 自動分類是供應商功能陳述，仍要看誤報、漏報與客戶實績 |
| 根因分析 | 缺陷和哪台設備、材料批次、參數或製程步驟一起出現？ | 批次、機台與製程參數的關聯 | 同時發生只是一條線索，不等於已證明因果 |
| 回饋與管制 | 要調參數、停線、重工、改抽樣，還是修改設計規則？ | 製程調整、警報與抽樣策略 | 有資料不等於已形成可重複、可量化的良率改善 |

Applied 的文件把高解析 eBeam 量測、缺陷複判與自動分類分成不同任務；SEMI 議程中的 3DIC
摘要則把 equipment intelligence、data-driven control 與 yield learning 放在製造閉環裡。兩者
共同提醒讀者：真正的價值不只在「看見」，而在能否把訊號變成製程決策；但公開資料尚未
提供誤報率、漏報率、抽樣比例或客戶端良率改善，這些欄位不能自行補值。

## 缺陷數不是良率：從「被看到」走到「會殺死產品」的五道閘門

檢查工具輸出的第一個數字通常是候選訊號，不是「已證明會造成報廢的缺陷」。NIST 對 patterned
wafer 的研究指出，製程圖形偏差可以是不影響產品的變異，也可以是傷害良率的關鍵缺陷；線邊
粗糙等 wafer noise 又可能遮蔽 killer-defect 訊號，同時製造 false positive 與 overlooked defect。
因此，候選數增加只證明「在這個 recipe 與門檻下標記得更多」，還沒有回答產品是否變差。

### 先用四格表停止把「工具標記」當成「參考真值」

NIST 的持續研究頁把光學缺陷檢查寫成四種可能結果。以下把目標明確限定為「需要採取行動的
關鍵缺陷」；參考真值仍要靠複判、破壞分析、電性結果或其他有文件紀錄的方法建立，並不是
研究者憑空知道的上帝視角。

|  | 參考真值：有目標關鍵缺陷 | 參考真值：沒有目標關鍵缺陷 |
|---|---|---|
| **系統有標記** | TP：成功攔截，仍要判斷位置、嚴重度與處置 | FP／nuisance：消耗複判與工程容量，未必傷害產品 |
| **系統未標記** | FN／escape：缺陷繼續流到後站或客戶，代價可能延後才出現 | TN：正確不標記，但只有在受檢母體與真值抽查已知時才有分母 |

只報「標記 10,000 個候選」其實只給出 `TP + FP`，沒有告訴讀者未標記母體中的 `FN`，也沒有
說 TP 中哪些真的會殺死產品。就算 capture rate 或 FAR 被公布，仍要核對各公司採用的 actual
positive、分母與複判真值定義；名字相同不保證公式與母體相同。

### 99.8801% accuracy，仍可能讓總錯判成本更高

NIST 2023 年的 patterning-defect metrology 研究再補上一個常被忽略的分母：把 defect 錯標成
nominal，與把 nominal 錯標成 defect，後果通常不對稱。研究明說真實量化成本未公開，並以公開
ML 資料集代替工業影像；所以它報告的 loss function、門檻、cost ratio 與 15%～40% 結果都不能
搬到 HBM 或先進封裝產線。本文只沿用「門檻必須同時看 base rate、兩種錯誤與成本比」的方法，
另建一個完全假想、可以手算的四格表。

先固定 **N=1,000,000 個假想受檢單位**，其中真正有目標關鍵缺陷 1,000 個、真正沒有 999,000
個，base rate 為 0.1%。兩個門檻使用同一母體與參考真值；所有數字都是事先指定的整數，不是
從任何工廠估計：

| 四格與指標 | 敏感門檻 A | 較嚴門檻 B |
|---|---:|---:|
| TP：真正缺陷且有標記 | 900 | 800 |
| FN：真正缺陷但未標記 | 100 | 200 |
| FP：乾淨單位卻被標記 | 9,990 | 999 |
| TN：乾淨單位且未標記 | 989,010 | 998,001 |
| Recall＝TP／(TP＋FN) | 90.000000000000% | 80.000000000000% |
| FPR＝FP／(FP＋TN) | 1.000000000000% | 0.100000000000% |
| Precision＝TP／(TP＋FP) | 8.264462809917% | 44.469149527515% |
| Accuracy＝(TP＋TN)／N | 98.991000000000% | 99.880100000000% |
| 需進入複判的 TP＋FP | 10,890 | 1,799 |
| 候選中的 nuisance share | 91.735537190083% | 55.530850472485% |

門檻 A 的 FPR 看似只有 1%，但它乘在 999,000 個真正乾淨的龐大分母上，就產生 9,990 個 FP，
是 900 個 TP 的 11.1 倍；因此 accuracy 接近 99%，被標記候選的 precision 卻只有 8.2645%。門檻
B 把複判量減少 83.480257116621%，accuracy 與 precision 也都更高，看起來全面勝出；代價是
FN 從 100 個增為 200 個。只看 dashboard 上最漂亮的百分比，會把這 100 個新增 escape 藏掉。

接著把每個被標記候選的複判工作量定為 `R`，每個 FN／escape 的後果定為 `C`；兩者只是同一張
教材上的「複判等價成本單位」，不是貨幣、報廢金額或生命週期成本：

```text
門檻 A 的教材總成本 K_A = 10,890R + 100C
門檻 B 的教材總成本 K_B =  1,799R + 200C

令 R = 1 且 K_A = K_B：
C = (10,890 − 1,799) ÷ (200 − 100) = 90.91
```

| 假想 FN 成本 | 門檻 A 的教材總成本 | 門檻 B 的教材總成本 | 這組假設下較低者 |
|---|---:|---:|---|
| `C = 50R` | 15,890 | 11,799 | B；複判節省大於新增漏失代價 |
| `C = 100R` | 20,890 | 21,799 | A；新增漏失代價反超複判節省 |

所以沒有脫離產品風險與工廠容量的「最佳 accuracy」。若一個 escape 的後果高於 90.91 個複判
單位，這個教材會選 A；若低於 90.91，才選 B。實務上還要納入 defect class、位置、後站損失、
複判佇列、cycle time、重工／報廢、客戶風險與門檻漂移，不能把所有 FN 或 FP 視為同價。

一份可稽核的 **defect-threshold cost passport** 至少要保存：

| 護照欄位 | 必須固定什麼 | 少了會怎麼誤讀 |
|---|---|---|
| 母體與 base rate | product／layer／station、受檢與未檢母體、目標缺陷定義與真值抽查 | 把低 FPR 直接當成少量 FP |
| 四格與門檻版本 | TP／FP／FN／TN、score threshold、model／recipe／class version | 只報 accuracy 或候選數，看不見錯在哪一格 |
| 複判容量 | 每候選工時、設備／人員、佇列、time-to-truth 與可用容量 | 把 FP 下降直接寫成整廠 cycle-time 改善 |
| 漏失後果 | defect class／位置、後站投入、escape、rework／scrap／reliability 與客戶處置 | 用一個平均成本掩蓋高代價尾部 |
| 決策與變更控制 | cost ratio、選門檻者、核准日、漂移監控、回退與再驗條件 | 把一次離線最佳點當成永久量產設定 |

本例由 Python `Fraction` 與獨立 `awk` 以相同整數四格重算，accuracy、recall、FPR、precision、
nuisance share、複判量減幅、兩條成本式與 90.91 crossover 在顯示精度內一致。這是確定性教材，
不是抽樣估計，所以沒有 sampling SE／t；NIST 的論文結果也沒有被當成第三個量產樣本。

多空兩邊必須共用這份護照：偏多情境要證明維持可接受 FN 時，低 base rate 造成的複判負荷已
超過既有設備、人工與軟體容量，並真的形成新增工具或服務；偏空情境則要證明分類、care area、
動態抽樣或門檻控制能在不惡化高代價 escape 下，讓既有 installed base 吸收工作量。只有 accuracy
上升、候選下降或「AI 分類」四個字，都不足以裁決設備需求與財務結果。

### 五道閘門：每往後一關，責任人才不同

| 閘門 | 必須回答的問題 | 需要保留的共同鍵 | 前一關不能代替什麼 |
|---|---|---|---|
| 1. 訊號／候選 | 哪個工具、方法、recipe、門檻在何處看見什麼？ | product／layer／station／tool／recipe version | 標記不等於物理缺陷已確認 |
| 2. 複判／分類 | 參考真值怎麼建立，TP／FP／FN／TN 各是多少？ | truth method／audited sample／class／threshold | 分類不等於已證明會傷害產品 |
| 3. 關鍵性 | 缺陷的尺寸、位置、拓樸與失效模式是否讓它成為 killer defect？ | design location／failure mode／severity／product revision | killer 分類不等於已找到來源 |
| 4. 圍堵／根因 | 哪個 lot、wafer、die、tool、材料批次或時間窗要隔離與調整？ | genealogy／timestamp／containment／disposition／retest | 停線或隔離不等於良率已改善 |
| 5. 製造與經濟結果 | 良率、重工、報廢、可靠度、cycle time 與成本如何改變？ | same cohort／before-after rule／yield／scrap／cost | 工程改善不等於設備商已取得收入 |

台積電的現行 Intelligent Packaging Fab 頁面提供了少見的客戶端方向證據：公司描述先進封裝廠
使用 die-level MES 提供即時資訊、派工、缺陷攔截與分類，以及自動良率預測與最佳化；ADC 在
流程中做缺陷攔截與分類，良率分析引擎再偵測缺陷並隔離不良材料。這證明閉環不只存在於設備商
行銷圖，也不只停在「工具看見訊號」。但頁面沒有公開同一產品／layer 的 sampling universe、
recipe version、TP／FP／FN／TN、結果延遲、圍堵批數、良率、重工、報廢、工具數或成本。

### 為什麼缺陷數上升至少有四種解釋

1. **製程真的變差**：同一 recipe、覆蓋與分類下，actionable／killer defect 增加。
2. **覆蓋變大**：多看 wafer、die、site、layer 或產品，候選總數自然增加。
3. **門檻變敏感**：更低 threshold 找到先前看不到的訊號，也可能同步增加 nuisance。
4. **分類或產品改版**：原本 non-killer 的偏差在新設計位置變成 critical，或 class definition 改變。

反過來，候選數下降也可能是製程改善、覆蓋縮小、門檻提高或分類改版。沒有同一 product／layer、
受檢母體、recipe、truth method 與版本，就不能把趨勢命名成 yield improvement，更不能把候選數
乘上臆測報廢成本或設備 ASP。

### 多方小作文：可以寫到哪裡

製程控制需求的較強多方版本是：若新一代 HBM／2.5D／3D 在更多關鍵位置產生更小、代價更高的
actionable defect，客戶又必須增加覆蓋、縮短攔截時間並維持可接受的 FP／FN，既有工具與軟體
無法吸收全部工作量，新增檢查、複判、量測與資料基礎設施才可能轉成工具數、服務與收入。升格
需要同一產品世代的四格分母、control-plan 變更、工具／支出增加及供應商 actual revenue 雙向證據。

### 空方小作文：可以寫到哪裡

較強的空方版本是：die-level MES、ADC、ML 分類、care-area 設計或動態抽樣可能先移除 nuisance、
集中複判容量並提高既有 installed base 的利用；候選數增加也可能只是更敏感或更廣的觀察，不是
良率惡化。若客戶在相同產品世代以軟體、抽樣或既有工具吸收新增複雜度，單位產能工具量與支出
可能持平，設備供應商的成長則可能主要來自市占、ASP、服務或產品組合，而非產業 wallet 擴張。

| 共同裁決欄位 | 多方要看到 | 空方要看到 | 目前公開狀態 |
|---|---|---|---|
| 四格品質 | 同門檻下 FN／escape 風險要求新增能力且 FP 可控 | 軟體／分類降低 FP、既有能力已控制 FN | NIST 只給方法與模擬方向 |
| 覆蓋與時間 | 同產品增加 station／layer／sample，time-to-result 仍受限 | adaptive sampling／care area 維持或降低工具負荷 | 客戶數值未揭露 |
| 製造結果 | 同 cohort 良率、重工、報廢或 cycle time 可重算改善 | 新增檢查未帶來材料性結果，或既有流程已足夠 | 台積電只公開功能鏈 |
| 工具與財務 | 客戶工具數／支出與供應商 actual revenue 同期增加 | 工具密度／單位產能支出持平，成長由其他因素解釋 | 尚無雙向分母 |

### 分母、誤差與限制

本節定向使用 `N=2` 條消息鏈：兩個 NIST 頁面同屬一條中立方法鏈，台積電現行服務頁是另一條
客戶公司鏈；不是封裝廠、產品世代、製程站點或 121 檔公司的統計樣本。NIST 的 2015 研究是
patterned-wafer optical inspection，不是 HBM 封裝 production recipe；NIST ongoing project 的
四格說明與 threshold 研究也沒有公開本篇可用的量產混淆矩陣。台積電頁面沒有數字分母或版本化
結果，因此沒有 sampling SE／t，也不建立跨公司 performance comparison。五道閘門與共同裁決表
是研究中心整合三份來源的查核框架，不是 NIST 或台積電發布的共同標準。

## 「多檢查」不是規格：先拆三種任務與六個 control-plan 欄位

同一台設備可以用在新製程除錯、量產監控或成品篩選，但三種任務要回答的問題不同。若只把
它們統稱為「檢查需求增加」，就會把研發期間的高靈敏度模式、量產中的抽樣監控，以及特定
關鍵站點的全面篩選重複加總。

| 任務 | 它要做的決定 | 常見資訊取捨 | 研究時不能直接推論 |
|---|---|---|---|
| 缺陷發現／製程除錯 | 新缺陷是什麼、在哪裡生成、要改哪個參數？ | 可把較多時間換成更細影像、更多候選與根因資訊 | 除錯模式會原樣進入每片量產晶圓，或必須新增同數量工具 |
| 量產監控／異常圍堵 | 製程是否漂移、哪個 lot／wafer／tool 要隔離？ | 在抽樣覆蓋、結果速度、靈敏度與偽警報間維持可重複節奏 | 抽樣增加就一定降低逃逸，或單次結果較快就已縮短整體週期 |
| 篩選／產品處置 | 哪一顆 die 或 package 可放行、重工或報廢？ | 對指定失效與站點提高覆蓋，必要時做到全面檢查 | 某站 100% screening 代表所有工序、所有缺陷都全面檢查 |

KLA 的封裝產品公告本身就列出不同任務：Kronos 做 wafer-level inline control，ICOS F160XP
在切割後找側壁裂縫，另以提升 throughput 支援指定的 100% IR inspection。這是供應商對自家
產品的功能陳述，不是全產業共同 recipe；它的重要性在於證明「檢查」沒有單一覆蓋分母。

接著把 control plan 寫成六個不能互相替代的欄位：

| Control-plan 欄位 | 必須先回答什麼 | 少了這欄會怎麼誤讀 |
|---|---|---|
| 1. 失效與決策 | 要攔截哪種 defect of interest，結果用來調參、隔離、重工還是放行？ | 把看得見但不影響產品的訊號當成良率改善 |
| 2. 工序與檢查單位 | 在哪一站看 lot、wafer、die、site 或 package？ | 把一個位置的覆蓋率外推到整條產線 |
| 3. 抽樣與覆蓋 | 每批、每片、每區域看多少，是否會依漂移與不確定性調整？ | 把「樣本更多」直接寫成「風險已消失」 |
| 4. 靈敏度與逃逸 | 最小可見缺陷、漏掉關鍵缺陷的風險與產品失效怎麼接起？ | 只看解析度，不知道真正 killer defect 是否被攔截 |
| 5. 偽警報與分類 | 候選中有多少是 nuisance，分類錯誤會占用多少複判能力？ | 把缺陷候選數增加誤寫成關鍵缺陷增加 |
| 6. 結果時間與圍堵 | 從量測、複判到停線／隔離要多久，期間會再流過多少產品？ | 把單機 throughput 當成完整 factory cycle-time 改善 |

NIST 的 2025 研究用 CMP 公開資料示範：量測昂貴、資料有限且會漂移時，可以把模型不確定性
帶入動態抽樣，依 process-control need 選擇何時量測。Applied 的 SEMVision H20 公告則從另一
角度說明，光學檢查產生更密集候選後，eBeam review 必須同時維持速度、靈敏度、覆蓋與
nuisance 分類。兩份文件都沒有公開 HBM 客戶的完整 control plan、逃逸率、偽警報率或整廠
週期時間，因此本文只建立閱讀框架，不替任何量產線補寫數值。

## 警報不是處置：用九個事件讀懂異常圍堵

控制圖或模型亮紅燈，只代表「依目前規則，這筆資料值得處理」。NIST／SEMATECH 把
process monitoring 與 process control 分得很清楚：前者偵測 out-of-control 狀態，後者才是
依監控結果主動改變製程；OCAP 用來規定偵測後的動作，而且不同製程可以有不同流程圖。
因此，工具較快產生訊號，不等於材料已停住、受影響範圍已找完，也不等於製程已安全復機。

### 三個時鐘不能合成一個「反應很快」

一份可稽核的異常紀錄至少要保存下列九個事件。`t0` 只是最後一次**已證實在控**的界線，
不保證異常物理原因恰好從那一刻才開始；`t6` 則要記實際執行完成，而不是工程師按下指令的
時間。若 command 和 enforcement 共用一個時間戳，就無法知道控制系統、設備或物流是否延遲。

| 事件 | 必須保存的內容 | 這一格不能被什麼代替 |
|---|---|---|
| `t0` 最後已證實在控 | control limit／check、方法與版本、被接受的最後物件 | 不能當成真實 excursion onset |
| `t1` 製程／材料事件 | 物件經過的站點、tool／chamber、recipe、材料批次與完成時間 | 不能只留工單日期或整批平均 |
| `t2` 取樣／影像／量測 | sampling unit、取得時間、佇列入口與資料品質 | 不能用設備 nominal throughput 回填 |
| `t3` 產生警報 | rule／model／threshold 版本、原始值、limit、event time | 警報數不等於 actionable defect 數 |
| `t4` 確認／分類 | 自動或人工複判、參考真值、嚴重度、false-alarm 分支 | 分類完成不等於材料已被攔住 |
| `t5` 下達圍堵 | 決策人／系統、OCAP 版本、stop／hold／isolate 範圍與 command time | 電子指令不等於物理執行完成 |
| `t6` 圍堵生效 | tool stopped、material isolated 或 lot held 的完成狀態與確認來源 | 不能只看 `t3` 或單機 image time |
| `t7` 範圍與處置 | genealogy 查得的 lot／wafer／die／package、retest／rework／scrap／release | 可疑集合不等於全部都真正失效 |
| `t8` 修正後放行 | 根因、永久修正、重驗規則、approver、新基線與 release time | 復機不等於已證明長期良率改善 |

這九格可以拆出三段不同瓶頸：`t2→t3` 是資料／運算延遲，`t3→t5` 是確認與決策延遲，
`t5→t6` 是控制動作真正落地的延遲；`t6→t8` 則是調查、修正、驗證與復機時間。常見的
`signal-to-hold` 只等於 `t6−t3`，它沒有涵蓋取樣以前的製程歷史，也不能代表完整
excursion exposure。把工具「每小時看幾片」直接倒數成 factory containment time，會漏掉
取樣間隔、資料佇列、複判、權限裁決、設備停機確認與已經流到後站的材料。

### 受影響量要從物件集合重建，不能只拿流率乘時間

SEMI 的 traceability 頁面把 unique device identification 延伸到 IC 製造、測試、組裝乃至
最終系統，並說明端到端追溯對 performance／failure analysis 的重要性。台積電公開的先進
封裝自動化頁則提供實作方向：inline ADC 在製程中偵測並隔離受影響材料，offline ADC 在
製程後偵測並 hold lots；per-die 履歷再把原始 wafer 位置、bin、製程歷史、tool logs、材料與
yield 接起來，用來界定影響範圍與分析低良率根因。

研究時應把候選受影響範圍寫成一個**物件集合**：同一 product／revision 下，沿著可疑
tool／chamber、recipe、材料批次與時間窗實際走過的 lot、wafer、die 或 package。流率乘上
`t6−t3` 最多只是「警報後到圍堵生效間、在固定流率假設下又流過多少」的簡化量；它會漏掉
警報前已加工的物件、抽樣間隔、不同路由、重工回流、佇列與異常真正起點未知。沒有共同
identity key、事件時間與 genealogy，就不能把一個 lot hold 推算成受影響 die 數、報廢金額
或避免損失。

### 多空小作文要用同一張事件護照裁決

| 觀察欄位 | 多方版本需要什麼 | 空方／替代版本需要什麼 | 現有公開狀態 |
|---|---|---|---|
| 訊號到圍堵 | 新增感測、複判、控制或資料設備讓同口徑 `t2→t6` 縮短 | edge ADC、軟體與既有設備已吸收負荷，硬體密度未增加 | 沒有產品級時間戳 |
| 影響範圍 | genealogy 讓同類 excursion 的候選物件、報廢或重工下降 | 只把範圍找得更完整，物理 defect rate 未改善 | 台積電只公開功能鏈 |
| 修正與復機 | 同根因的 recurrence、`t6→t8`、良率或 cycle time 改善 | hold／複判增加反而拉長週期，或 false alarm 消耗工程容量 | 沒有同 cohort 結果 |
| 工具與財務 | 客戶新增工具／支出與供應商 actual revenue 同期對回 | 改善主要來自 installed-base 軟體、流程或內部系統 | 沒有雙向財務共同鍵 |

本節定向使用 `N=3` 條消息鏈：NIST／SEMATECH 是通用監控與 OCAP 方法鏈，台積電是一條
客戶公司功能鏈，SEMI 是追溯標準入口；它們不是三座封裝廠、三個產品或量產事件樣本。
九事件護照是研究中心把三條來源整合後的查核框架，不是三方共同發布的標準。來源沒有提供
任何 HBM／2.5D／3D 產品的九個時間戳、受影響物件數、重複事件或對照組，因此沒有可估的
sampling SE／t，也不建立延遲、良率、損失避免或供應商績效排名。

## 量得出數字，不代表能拿去控製程：先過量測系統六關

把製程控制想成醫師依檢驗結果決定是否治療：若檢驗方法本身會偏、不同儀器彼此不一致，或
結果的不確定度大到跨過判定門檻，再精細的小數點也不能安全地支撐決策。半導體產線同樣要
先證明「量測系統能否回答這個問題」，才輪到抽樣、攔截與圍堵。

### 先分清「準」與「穩」

| 問題 | 它在檢查什麼 | 看似漂亮但仍可能失敗的例子 |
|---|---|---|
| 偏差／準確度 | 多次結果的中心是否接近參考值？ | 十次結果非常集中，卻全部比參考值高 2 nm |
| 重複性 | 相同設備、設定與短時間條件下能否得到一致結果？ | 同一片晶圓連續量測就大幅跳動 |
| 再現性 | 換日期、設備、操作或環境後，結果是否仍可比較？ | A 機與 B 機各自很穩，兩機平均值卻不同 |
| 穩定性／漂移 | 量測系統跨較長時間是否仍維持原有特性？ | 上週校正後合格，本週因溫度或設備漂移而偏移 |
| 不確定度 | 綜合已辨識誤差後，結果還有多大的合理範圍？ | 規格門檻是 10 nm，結果 9.9 nm，但不確定度足以跨過門檻 |

NIST／SEMATECH 的 Measurement Process Characterization 把量測系統本身視為一個產出
「量測結果」的製程，要求分開看 bias、短期精密度、日間／長期變異與 uncertainty；Gauge
R&amp;R 章節又把 repeatability、reproducibility、stability、resolution、linearity、hysteresis、
drift，以及設備、設定與操作差異列成不同誤差來源。這些是通用量測方法，不是 HBM 客戶的
合格門檻，也不代表每個任務都要採相同統計設計。

### 一份可用的 measurement-system contract 至少有六欄

| 量測系統欄位 | 必須先固定什麼 | 少了這欄會怎麼誤讀 |
|---|---|---|
| 1. 被測量、單位與決策 | 量的是哪個性質、用什麼單位，結果要支撐調參、隔離、重工還是放行？ | 只看設備解析度，卻不知道數字是否對應真正失效 |
| 2. 方法、組態與環境 | 樣品準備、演算法／recipe 版本、設備設定、操作、溫濕度與量測範圍為何？ | 把不同方法或環境的數字當成同口徑趨勢 |
| 3. 參考、校正與可追溯鏈 | 結果連到哪個參考、何時如何校正，校正鏈與量測保證紀錄是否完整？ | 把一張校正證書當成所有後續結果的永久背書 |
| 4. 偏差、解析度與線性 | 系統性偏移、可辨識最小變化及量測範圍內的反應是否已知？ | 結果很穩就誤以為一定接近真值，或在量程邊緣照樣外推 |
| 5. 重複性、再現性與穩定性 | 同機短期、跨機／跨日與長期漂移各有多大？ | 只用一次 gauge study，忽略工作環境與時間變化 |
| 6. 不確定度與決策規則 | 各誤差如何合成，結果靠近規格線時如何判定與處置？ | 用很多小數位製造確定感，卻沒有說明跨過門檻的風險 |

NIST 的可追溯性政策再補上一條很容易被誤讀的界線：可追溯的是**特定量測結果**，不是設備、
校正報告或實驗室本身；只有使用一台曾由 NIST 校正的儀器，並不足以建立後續結果的可追溯性。
提供結果的一方仍要交代被測量、完整量測系統、帶不確定度的結果、校正參考與量測保證程序，
而且要隨設備、標準與環境變化定期重查。

因此本文把製程控制拆成兩層，不把欄位混在一起：

1. **量測系統契約**先證明數字在指定方法、環境與時間內可信，且足以支撐決策。
2. **Control plan 契約**再決定在哪一站、抽樣多少、要攔截什麼、容許多少逃逸與偽警報、多久形成處置。

這兩層都完整，才有資格追問良率、重工、報廢與週期時間是否改善。它們仍只是工程證據；要
推到設備商收入，還要另證明新增步驟、工具量、價格、重複採購與供應商份額，不能把方法完整
直接當成財務材料性。

## 沿著工序看：風險不是只出現在最後一站

SEMI 2026 先進封裝峰會的官方議程摘要列出多個控制點。這些是講者對議題的摘要，不是完整
簡報或經同口徑驗證的量產數據；它們適合建立「要問什麼」，不適合直接估算市場規模。

| 工序／結構 | 摘要點出的風險 | 製程控制要回答的問題 | 目前證據邊界 |
|---|---|---|---|
| 高深寬比 TSV 蝕刻、填孔與介電層 | 蝕刻形貌、填孔空洞、沉積均勻性 | 孔的幾何與材料是否落在可接續堆疊的製程視窗？ | 議程列出挑戰，沒有工具數或單位產能支出 |
| CMP、hybrid bonding 表面與異質基材 | 厚膜、較長拋光、非均勻、翹曲與細微缺陷 | 表面是否平坦、潔淨並足以接合？光學與 eBeam 各負責哪一段？ | Applied 為供應商自述，沒有客戶端良率橋接 |
| 面板級封裝與細 RDL | 大面積翹曲與細線路製造 | 面板不同區域是否維持對位、線寬／線距與均勻性？ | Samsung 摘要說明技術題目，不代表全產業已量產 |
| inter-die gap fill、切割與組裝 | 填隙、邊緣品質、die strength 與顆粒 | 缺陷在切割前後哪一站生成，能否在更多價值投入前攔截？ | 只有議程摘要，未揭露攔截率或報廢改善 |
| CPO 封裝（相鄰案例） | 光學對位、熱、翹曲、CTE mismatch、污染、測試與重工 | 電、光、機、熱資料如何共同定位問題？ | 這是 CPO 的相鄰案例，不能反推 HBM 採相同 BOM 或工具組合 |

這張表也說明為什麼「先進封裝」不能只用一個設備名稱代表。不同產品架構、材料、抽樣策略
與既有工具能力，會改變新增量測點及採購內容。要把工程複雜度換成設備需求，至少還要知道
哪些步驟是新增、哪些只是升級，以及同一工具能否覆蓋多個控制點。

## 8 月 6 日的新訊號：從資格節點前進，但只前進一格

Onto Innovation 的 2026Q2 8-K 附件把成熟度往前推了一步：公司稱
`Specialty Devices and Advanced Packaging` 收入創季度新高，並把 2.5D logic、HBM 與
silicon photonics 都列為支撐來源。這比 2026Q1 只揭露 Dragonfly G5 在兩類客戶完成資格
認證更接近商業結果。

但安全讀法只有「較寬事業組合出現收入訊號」，不能寫成「Dragonfly HBM 收入創高」：

1. 公司沒有公布該較寬類別的收入金額或占公司總收入比例。
2. 同一類別同時包含 2.5D logic、HBM、silicon photonics 與其他 specialty-device 曝險。
3. 文件沒有把成長分解到 Dragonfly、量測、檢查、微影、工具數、價格或客戶數。

因此證據階梯由「工程機制＋資格節點」升為「工程機制＋資格節點＋較寬收入訊號」，仍未到
「題材收入分子」「客戶資本支出分母」或「全產業 wallet share」。這一格很重要，因為它
證明商業訊號開始出現；界線也同樣重要，因為它還不能回答產業獲利池到底擴大多少。

## 看見金額先問：它是訂單、營收，還是成長指數？

工程證據回答「工具能做什麼」，商業證據則要回答「哪一種工具、在哪個期間、占哪個分母
多少」。2026 年 6～8 月的 Camtek 與 Nova 文件正好示範：同一家公司可以同時公布未來
訂單、當季公司營收、近似產品組合與未來成長率；它們都是有用資訊，卻不能放進同一個分數
相加。

Camtek 6 月 2 日隨 6-K 公開的公告把訂單具體到兩組客戶與工具：一筆來自支援 AI 應用的
tier-1 OSAT、多系統合計 5,500 萬美元；另一組來自 leading HBM player、超過 5,000 萬美元，
而且全部是 Hawk 系統。公告標題把兩組合稱超過 1.05 億美元，並說預計都在 2027 年交付。
這是目前最接近「具名產品＋客戶類型＋金額＋交付時點」的一格，但客戶仍匿名，也沒有收入
認列、毛利、工具台數或客戶產能分母。

8 月資料再提供三種不同口徑。Camtek Q2 結果公布截至 6 月 30 日的公司營收 1.332 億美元，
並表示年初至發布時累計接單超過 6 億美元、預計在 2026 年剩餘期間至 2027 年交付；同份
文件預期先進封裝收入從 Q1 到 Q4 約成長 70%。同月投資人簡報另以公司收入組合圖，把約
55% 的 HPC／AI 與 20% 的 non-AI advanced packaging 合計標為約 75% 的收入，卻沒有在該圖
標示量測期間；它又把 Eagle G5／Hawk「預期占 2026 年收入 50%」寫成全年預測。這些集合
彼此重疊，不能把 75% 與 50% 相加，也不能把未標期間的近似占比直接乘上 Q2 的 1.332 億
美元，製造一個來源沒有公布的假精確題材收入。

Nova 的 Q2 6-K 則提供另一個常見句型：公司 GAAP 營收為 2.54958 億美元，advanced-packaging
solutions 收入創高，並稱 Sentronics dimensional-metrology solutions for advanced packaging
是多個創高產品線之一。它證實產品線已產生銷售與方向性新高，但沒有公布 advanced
packaging 的金額或占公司比例。因此公司總營收只是分母候選，不能替代題材分子；同樣地，
Onto 的較寬事業組合新高也不能與 Nova 的「record」互相比大小。

| 揭露句型 | 真正的分子／狀態 | 分母與期間 | 目前能說 | 不能換算成 |
|---|---|---|---|---|
| Camtek 兩組訂單合計超過 1.05 億美元 | 已接單、預計 2027 交付；其中一組具名 Hawk | 沒有同期間公司總訂單或客戶產能分母 | 具名工具的未來交付需求已出現 | 2026Q2 營收、2027 已認列收入、毛利或工具台數 |
| Camtek 2026Q2 營收 1.332 億美元 | 公司全部已認列營收 | 2026-04-01～06-30 的公司全集合 | 可當同季公司規模分母 | 先進封裝、HBM 或 Hawk 題材分子 |
| Camtek 簡報約 75% 公司收入來自 advanced packaging | 約 55% HPC／AI 加 20% non-AI AP 的近似組合 | 圖示未標明量測期間 | 公司收入結構高度曝險於較寬 AP 應用 | 特定季度 AP 金額、HBM 金額或工具毛利 |
| Camtek 年初至今接單超過 6 億美元 | lower-bound order intake | 2026 年初至 8 月 10 日；跨 2026～2027 交付 | 訂單能見度增加 | 用它除以單季營收得到 book-to-bill |
| Camtek AP 收入 Q1→Q4 預期約增 70% | 未來相對成長指數 | 基期與終點不同季，未附 AP 絕對金額 | 管理層的方向與幅度預期 | 已實現收入或全年 AP 金額 |
| Nova AP solutions 收入創高 | 類別序位訊號，沒有數值 | 公司 Q2 營收有分母，AP 分子未揭露 | AP 與 Sentronics 產品線有商業訊號 | AP 占比、HBM 占比、跨公司強弱排名 |

閱讀時可依四道閘門停手：先分訂單與已認列營收，再對齊期間，再確認題材範圍，最後標出
數值是精確值、近似值、下限還是預測。只有四道都一致，比例才可比較。本文的 `M1` 只把
Camtek 與 Nova 同一曆季、同幣別的公司總營收列為「可直接比較」；它的用途是證明分母可以
對齊，並反過來提醒讀者：沒有同定義的 AP 分子，兩家公司仍不能比較題材強度。

## 兩個「超過」仍拼不出製程控制收入：讀懂 Applied 的 20 億美元

Applied Materials 2026 年 6 月的 DRAM／Advanced Packaging Master Class 提供了一個比
「收入創高」更窄、卻仍不是本文題材分子的數字。公司表示，2020～2024 年的 advanced
packaging business 實際成長超過三倍，並預期 2026 年 advanced-packaging revenue 年增超過
50%、超過 20 億美元。同份 prepared remarks 又表示 VeritySEM 7AP 與 SEMVision G7AP 已在
多家 leading memory／logic advanced-packaging customers 的 production 中使用。前者是整體
AP 的公司預測，後者是具名製程控制工具的供應商端採用陳述；來源沒有把兩者接成同一個
收入分子。

### 先看兩個大於號，而不是自行補一個點估計

把 2025 年 AP 收入寫成 `B`、2026 年預測寫成 `F`、年增率寫成 `g`，關係是
`F = B × (1 + g)`。來源只給 `F > 20 億美元` 與 `g > 50%`；`F`、`g` 都不是精確值，
所以 `B = F ÷ (1 + g)` 沒有唯一答案。舉例來說，`F=21 億、g=60%` 會得到
`B=13.125 億`，`F=25 億、g=55%` 則會得到約 `16.129 億`，兩組都符合原句。這兩組只是
驗證不可識別性的假設情境，不是 Applied 的 2025／2026 估計，也沒有任何一組比較接近
公司實際預測。

因此不能把「超過 20 億」除以 1.5，寫成 2025 年 AP 收入「至少」或「約」13.33 億美元；
那等於同時把兩個下限偷換成等號。更不能再把該結果乘上任意檢查／量測占比，因為公司沒有
提供這個占比。

### 再沿著分子樹往下走

| 分子層級 | S25 實際提供 | 可以說 | 還不能說 |
|---|---|---|---|
| Applied 整體 advanced packaging | 2026 年收入預期年增逾 50%、超過 20 億美元 | 管理層給出較寬 AP 事業的方向與雙下限預測 | 精確 2025 基期、精確 2026 終值或已實現收入 |
| AP 製程控制 | 文件列出 eBeam 量測、缺陷複判，並稱另有 optical／x-ray 系統開發中 | 製程控制是 AP 產品組合的一部分 | 它占 AP 收入多少、成長多少或毛利多少 |
| VeritySEM 7AP／SEMVision G7AP | 供應商稱已在多家 leading memory／logic AP 客戶 production | 具名工具已前進到供應商端量產陳述 | 客戶名稱、部署台數、驗收收入、重複採購與客戶端良率 |

這個案例把「財務成熟度」與「產品成熟度」分開：整體 AP 已有發行人數值預測，具名工具也
有 production 陳述，但交集仍未量化。本文所需的分子是 advanced-packaging process-control
actual revenue 或 order intake，不是 Applied 全部沉積、蝕刻、電鍍、CMP、接合與控制工具
的 AP forecast。`N=1` 是一份指定發行人 prepared remarks 的文件級核對，不是設備商或客戶
樣本；兩組算例是確定性代數情境，沒有 sampling SE／t，也不衡量預測準確度。

## 8 月 13 日 FY26Q3：兩條成長線仍不是交集

Applied FY26Q3 結果把公司分母補得更完整：截至 2026 年 7 月 26 日的一季，公司實際營收
91.15 億美元，Semiconductor Systems（半導體系統）部門實際營收 70.40 億美元。該部門再按
客戶應用列出 foundry／logic／other 67%、DRAM 26%、flash 7%。同一結果公告也重述六項
DRAM／先進封裝系統，其中包含 VeritySEM 7AP 與 SEMVision G7AP。這些資料依序回答公司
多大、半導體系統部門多大、客戶應用如何分布，以及哪些產品被公司具名；卻沒有回答 AP
製程控制收入是多少。

| FY26Q3 新增揭露 | 數字或狀態 | 它的分母 | 不能改寫成 |
|---|---:|---|---|
| Applied 公司實際營收 | 91.15 億美元 | 公司全部收入 | AP、PDC 或 AP 製程控制收入 |
| Semiconductor Systems 實際營收 | 70.40 億美元 | 廣義半導體設備部門 | 製程控制產品收入或 AP 收入 |
| 部門客戶應用組合 | foundry／logic／other 67%、DRAM 26%、flash 7% | Semiconductor Systems 部門收入 | 產品組合、AP 占比或 PDC 占比 |
| 六項 DRAM／AP 系統 | 產品已由公司具名；其中兩項為 eBeam PDC | 沒有產品收入分母 | 六項各自收入、工具數、訂單或客戶成效 |

例如把 70.40 億美元乘上 DRAM 的 26%，只能得到公司按客戶應用分類的 DRAM 相關部門收入，
不能稱為 HBM、advanced packaging 或 eBeam 製程控制收入。反過來，把具名產品放進公告，
也不能把整個部門收入歸因給那些產品。這是「產品名存在」與「財務分子存在」之間最常見的
斷橋。

### AP 成長逾 70%、PDC 成長逾 50%，仍解不出 `A ∩ P`

Q3 簡報另給兩條 2026 年管理層預測：advanced-packaging revenues 預期成長超過 70%，
process diagnostics and control revenue 預期成長超過 50%。前者是包含電鍍、CMP、沉積、
接合與控制工具的廣義 AP 集合 `A`；後者是跨 leading-edge logic、DRAM 與其他應用的廣義
PDC 集合 `P`。本文要量的 AP 製程控制收入則是交集 `X = A ∩ P`。

兩個大集合的成長率不會替交集設定成長率。以下只用虛構指數證明不可識別性：假設基期
`A₀=100`、`P₀=100`，本期 `A₁=180`、`P₁=160`，確實分別滿足成長逾 70% 與逾 50%；若
基期交集 `X₀=50`，本期交集 `X₁` 可以是 20、50 或 100，分別代表 −60%、0% 或 +100%，
而三種情境都沒有超過兩個大集合。這些數字不是 Applied 的收入、預測或機率，只是集合
邊界的確定性教材。

因此不能把 70% 與 50% 平均成 60%、相乘成一個題材放大率，也不能主張 AP 製程控制的
成長率一定介於兩者之間。要完成交集，至少需要公司在同一期間揭露 AP-specific PDC 的
actual revenue、order intake、工具數或可重建產品分子，再對回公司／部門分母。

### 期間也不是一般曆年

簡報把 `CY26` 明定為 FQ2'26～FQ1'27，並註明 FQ1'27 是 14 週季度。這個公司定義的窗口
不是 2026 年 1 月 1 日到 12 月 31 日；也比四個標準 13 週季度多一週。未先取得其他公司相同
期間或做可稽核的週數／會計期調整前，不能把 Applied 的兩條成長下限直接和 Camtek、Nova
或台灣公司的曆年／曆季數字排名。

本段的 `N=1` 是同一發行人的一組結果資料（公告與簡報共一條公司消息鏈），不是設備商、
客戶或產業樣本；91.15 億與 70.40 億美元是該季發行人實際報告值，70% 與 50% 是管理層
lower-bound forecasts，來源均未提供預測區間。集合算例沒有 sampling SE／t，也不衡量預測
準確度。新資料沒有價格、估值、共識或持倉，因此不支持「市場已反映」或任何投資方向。

## 台灣映射的三個同名陷阱：先進封裝、設備與製程控制不是同一個分子

海外設備商出現 HBM 訂單後，最容易犯的錯不是算錯，而是把台灣公司的「先進封裝」、
「半導體設備」或「檢測」三個相鄰名詞當成同一筆收入。弘塑、均華與萬潤的正式文件正好
提供三個受控案例：都有已認列設備收入，也都能找到與先進封裝、檢查或量測相鄰的產品，
但沒有一家在所引文件中把具名製程控制產品、客戶階段與同期間題材分子完整接起來。

| 公司 | 已認列的廣義數字 | 產品／計畫層證據 | 目前停在哪一格 | 仍缺什麼 |
|---|---|---|---|---|
| 弘塑 | 2025 年機台設備產品收入 45.50881 億元，占公司收入 69.86% | 集團簡報把本業列為濕製程設備，另由集團成員代理 metrology／inspection；2.5D、3D、HBM、CPO 列為 application opportunities | 廣義機台收入＋應用機會＋集團代理能力 | 哪一項檢查／量測產品、哪個客戶階段、實際訂單或驗收收入及同期間分母 |
| 均華 | 2025 年半導體製程設備及相關精密模具 25.26471 億元，占 93.90% | 年報列 Chip Sorter、Die Bonder、AOI；另把 CPO sorter、1 µm 固晶位移量測與高解析六面檢查列為 2026 開發計畫 | 廣義設備收入＋既有產品清單＋未來研發計畫 | 各機種收入、客戶 qualification、接單／交付／簽收與重複採購 |
| 萬潤 | 2025 年半導體設備占收入 96.13% | 年報列錫球／六面外觀檢查與厚度量測；官網 CPO 平台描述主動對準、光學驗證與資料回饋 | 廣義設備收入＋公開產品能力 | 各工具收入、具名客戶採用、量產驗收、良率結果與產品毛利 |

這張表刻意不把 69.86%、93.90% 與 96.13% 排名。本文的 `M2` 把它們登錄為
`heterogeneous_evidence`：三筆都是 2025 年發行人自訂類別占比，卻分別量「機台設備產品」、
「半導體製程設備及相關精密模具」與「半導體設備」。類別範圍不同，而且三個分子都大於
製程控制；數字越高只能表示該發行人收入越集中於自己的廣義類別，不能表示檢查、量測或
良率學習曝險越高。

### 用四欄產品—商業護照停止過度映射

1. **產品與任務**：先寫具名工具到底負責清洗、搬運、接合、AOI、尺寸量測、缺陷複判，
   還是回饋控制；同一台整合設備也要拆出真正被研究的任務。
2. **客戶階段**：把研發計畫、樣機、共同開發、qualification、首次訂單與重複採購分開；
   「應用機會」與產品頁都不能自動跳到量產採用。
3. **會計狀態**：把預算、訂單、交機、安裝、驗收、已認列收入與收款分開。台灣設備商
   常受客戶簽收或驗收時點影響，產品已做出來仍不等於收入已成立。
4. **同期間分子—分母**：最後才要求具名題材收入或訂單，對上同期間公司／部門總額；
   廣義設備占比只能當搜尋入口，不能替缺少的製程控制分子補值。

這一輪是三家指定台灣公司的五份既有一手文件定向核對，`N=3` 是教材案例母體，不是 121 檔
universe、台灣設備業或製程控制供應商的抽樣，因此沒有 sampling SE／t，也不能由「尚未拆分」
推論公司沒有相關收入。它只量到一個可重現的閱讀結論：產品名、收入類別與商業成熟度必須
逐欄對齊，否則相鄰題材不能升格成受惠或排名。

## 主張與證據帳本

`證實` 只表示指定文件直接支持該句精確措辭；它不代表設備商的產業預測必然實現，
也不代表研究端已證明全產業支出、台灣公司訂單或獲利。

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: KLA Corporation
title: KLA Corporation Reports Fiscal 2026 Fourth Quarter and Full Year Results
published_at: 2026-07-28
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full
locator: FY26Q4（截至 2026-06-30）結果頁的 CEO 評論段，起句為 KLA remains uniquely positioned；另見 First Quarter Fiscal 2027 Guidance 與 Segment Information
limitation: 管理層把 memory complexity 與 advanced packaging 連到 process-control demand，但未分解產業錢包占比、單位工具量、客戶採購，也未區分成長來自市占、ASP、產品組合或服務
independence_group: kla
-->

<!-- research_source
source_id: S2
role: competitor_primary
source_kind: document
publisher: Applied Materials
title: Applied Materials Introduces New Systems to Accelerate DRAM and Advanced Packaging for AI Chips
published_at: 2026-06-25
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and/
locator: New eBeam Systems Bring Wafer-Fab Process Control to Advanced Packaging 小節；另見 HBM die warpage、VeritySEM 7AP 與 SEMVision G7AP 段落
limitation: 來源直接描述缺陷、量測與高量產使用情境，但仍是產品供應商公告，沒有全產業支出、第三方良率實績或台灣供應商訂單
independence_group: applied-materials
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: Onto Innovation
title: Onto Innovation Reports 2026 First Quarter Results
published_at: 2026-05-05
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-First-Quarter-Results/default.aspx
locator: First Quarter Business and Financial Highlights 的 Dragonfly G5 qualification bullet，以及 CEO 評論的 Dragonfly G5 inspection 與 Atlas G6 OCD adoption 段落
limitation: 只證實特定工具在一名 2.5D logic 客戶與一名 HBM 客戶的資格節點，以及公司對採用進度的描述；不提供訂單規模、產業滲透率或台灣映射
independence_group: onto-innovation
-->

<!-- research_source
source_id: S4
role: company_release
source_kind: living_index
publisher: KLA Corporation
title: KLA Financial Results
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.kla.com/financial-information/financial-results
locator: 2026-08-02 觀察到 2026 → FY 2026 下列 Earnings Release、Letter to Shareholders、Earnings Slide Presentation 與 Earnings Infographic
limitation: 持續更新的索引只供重查新附件，不能替代特定季度文件，也不能單獨證明需求或財務貢獻
independence_group: kla
-->

<!-- research_source
source_id: S5
role: competitor_primary
source_kind: living_index
publisher: Applied Materials
title: Applied Materials News Releases
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://ir.appliedmaterials.com/news-releases/
locator: 2026-08-02 觀察到 2026 年公告清單，包含 2026-06-25 DRAM and Advanced Packaging for AI Chips 公告
limitation: 持續更新的新聞索引只供未來重查；索引與產品標題本身不證明客戶採購、產業錢包占比或財務貢獻
independence_group: applied-materials
-->

<!-- research_source
source_id: S6
role: competitor_primary
source_kind: living_index
publisher: Onto Innovation
title: Onto Innovation News
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://investors.ontoinnovation.com/news/default.aspx
locator: 2026-08-02 以 2026 年公司新聞與季度結果作為 Dragonfly、Atlas、HBM 與 advanced packaging 後續資格及量產更新入口
limitation: 動態索引不等於新的資格、訂單或收入證據；出現新公告時須另建 document source
independence_group: onto-innovation
-->

<!-- research_source
source_id: S7
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-02
accepted_at: 2026-08-02
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 2026-08-02 建立 semiequip、material、pcb、packtest 族群重大訊息、法說與季度財報的後續查詢入口
limitation: 查詢入口會持續更新；入口本身不證明任何台灣公司取得 HBM／先進封裝量測檢查訂單或財務貢獻
independence_group: twse-mops
-->

<!-- research_source
source_id: S8
role: company_filing
source_kind: document
publisher: Onto Innovation
title: Onto Innovation Reports 2026 Second Quarter Results
published_at: 2026-08-06
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.sec.gov/Archives/edgar/data/704532/000119312526337990/onto-ex99_1.htm
locator: 2026-08-06 Form 8-K Exhibit 99.1，Second Quarter Business and Financial Highlights 的 Specialty Devices and Advanced Packaging bullet，以及其後 CEO 評論與 Operating Results
limitation: 公司只表示較寬的 Specialty Devices and Advanced Packaging 收入創新高，並把 2.5D logic、HBM、silicon photonics 列為支撐；沒有揭露該類別金額、產品分子、客戶名稱、工具數或各驅動貢獻，不能改寫成 Dragonfly／HBM 專屬收入
independence_group: onto-innovation
-->

<!-- research_source
source_id: S9
role: other_primary
source_kind: document
publisher: SEMI
title: Advanced Packaging Summit 2026
published_at: 2026-07-15
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.semi.org/en/connect/events/advanced-packaging-summit-2026
locator: Agenda 中 Lam Research Making 3DIC Manufacturable for AI、Samsung Electronics Advanced Packaging Technology for AI/HPC，以及 NVIDIA CPO Packaging: Challenges and Opportunities 三段公開摘要
limitation: 官方頁保存的是議程與講者摘要，不是完整簡報、同口徑實驗資料或第三方驗證；內容可建立 TSV、fill、deposition、warpage、RDL、alignment、contamination、test／rework、metrology 與 yield-learning 問題地圖，不能用來估算工具量、市場規模或台灣公司收入
independence_group: semi
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: A Comparative Study of Semiconductor Virtual Metrology Methods and Novel Algorithmic Framework for Dynamic Sampling
published_at: 2025-01-20
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic
locator: Abstract；limited availability of metrology data、sensor drift／shift、uncertainty quantification、adaptive sampling，以及 public CMP dataset validation 段落
limitation: 這是一篇以公開 CMP 資料驗證 virtual-metrology／dynamic-sampling 方法的研究，不是 HBM 或 advanced-packaging production recipe；摘要沒有客戶產線、逃逸率、偽警報率、工具數或財務資料
independence_group: nist
-->

<!-- research_source
source_id: S11
role: competitor_primary
source_kind: document
publisher: Applied Materials
title: Applied Materials Accelerates Chip Defect Review with Next-Gen eBeam System
published_at: 2025-02-19
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-accelerates-chip-defect-review-next-gen-ebeam/
locator: SEMVision H20 發布頁的 dense defect maps／sampling 段落與 Next-generation CFE、Deep learning AI image models 兩個 bullet；同頁另有 adoption 及 coverage 公司陳述
limitation: 這是 Applied 對自家 leading-edge logic／memory defect-review 產品的技術與採用陳述；倍數、解析度、速度、分類及 adoption 未由客戶端同口徑資料驗證，也不能直接套到 HBM 封裝 control plan
independence_group: applied-materials
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: document
publisher: KLA Corporation
title: KLA Announces Enhanced Portfolio of Systems for Advanced Packaging
published_at: 2020-09-21
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://ir.kla.com/news-events/press-releases/detail/9/kla-announces-enhanced-portfolio-of-systems-for-advanced
locator: Kronos 1190、ICOS F160XP 與 ICOS T3／T7 段落；分列 wafer-level inline control、切割後 crack inspection、100% IR inspection、component inspection／metrology 與 defect binning
limitation: 這是 2020 年 KLA 自家封裝工具組合與功能公告；不同工具任務可用來拆 control-plan 分母，但不代表現行 HBM 客戶共同 recipe、部署量、良率改善、工具替代或台灣公司訂單
independence_group: kla
-->

<!-- research_source
source_id: S13
role: other_primary
source_kind: living_index
publisher: National Institute of Standards and Technology
title: CHIPS Metrology Program
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nist.gov/chips/research-development-programs/metrology-program
locator: 2026-08-12 的 CHIPS Metrology Program 活頁；後續回查 fit-for-purpose metrology、advanced packaging、modeling、standards 與 METIS 研究成果
limitation: 動態計畫頁只供後續重查，不能替代具日期的研究成果，也不證明任何方法已進入客戶 production、改善良率或形成設備需求
independence_group: nist
-->

<!-- research_source
source_id: S14
role: other_primary
source_kind: living_index
publisher: National Institute of Standards and Technology / SEMATECH
title: NIST/SEMATECH e-Handbook of Statistical Methods — Measurement Process Characterization
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm
locator: Chapter 2 的 2.1.1 What are the issues for characterization、2.1.1.3 Bias and Accuracy、2.1.1.4 Variability、2.4 Gauge R and R studies 與 2.4.6 Quantifying uncertainties from a gauge study
limitation: 這是持續更新的通用工程統計手冊；章節以 ongoing measurement process 及 gauge study 建立 bias、repeatability、reproducibility、stability 與 uncertainty 方法，不是 HBM／advanced-packaging 客戶 recipe、產品允收門檻、產業標準或量產結果；reproducibility 一詞也可能和其他標準採不同細部定義
independence_group: nist
-->

<!-- research_source
source_id: S15
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: Metrological Traceability Frequently Asked Questions and NIST Policy
published_at: 2021-05-06
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.nist.gov/publications/metrological-traceability-frequently-asked-questions-and-nist-policy
locator: NIST Technical Note 2156 的 §§5.1.1–5.1.3、5.2.1–5.2.3 與 5.4.3；定義 traceability 為特定 measurement result 的性質，並列出 calibration chain、uncertainty、measurement-system documentation 與 measurement-assurance 要件
limitation: 這是跨領域計量政策與術語文件，不是半導體特定方法資格、產品 pass／fail 規格或客戶良率資料；可追溯也不表示不確定度一定適合某個製程決策，更不構成 NIST 對設備商或產品的背書
independence_group: nist
-->

<!-- research_source
source_id: S16
role: company_filing
source_kind: document
publisher: Camtek Ltd.
title: Camtek Receives Over $105 Million Multi-System Orders from a Tier-1 OSAT and a Leading HBM Manufacturer
published_at: 2026-06-02
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.sec.gov/Archives/edgar/data/1109138/000117891326003033/zk2635474.htm
locator: 2026 年 6 月 Form 6-K 附件正文；標題及第一段分列 tier-1 OSAT 的 5,500 萬美元 multi-system order、leading HBM player 的超過 5,000 萬美元全 Hawk 訂單與 2027 expected delivery
limitation: 訂單不是已認列營收；兩名客戶未具名，文件沒有工具台數、認列時點、取消條件、客戶產能分母、產品毛利或台灣供應鏈映射
independence_group: camtek
-->

<!-- research_source
source_id: S17
role: company_release
source_kind: document
publisher: Camtek Ltd.
title: Camtek Announces Results for the Second Quarter of 2026
published_at: 2026-08-10
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.camtek.com/news-and-events/camtek-announces-results-for-the-second-quarter-of-2026/
locator: 2026 Second Quarter Financial Highlights、CEO 評論與 Second Quarter 2026 Financial Results；分別列出截至 2026-06-30 的 1.332 億美元營收、年初至今超過 6 億美元接單、跨 2026 剩餘期間至 2027 交付，以及 Q1 到 Q4 AP revenue expected growth 約 70%
limitation: 公司總營收沒有拆出 AP／HBM／Hawk 分子；超過 6 億美元是跨期交付的 order intake，下限值不是同季營收；70% 是未附絕對基期的前瞻陳述，不是已實現結果
independence_group: camtek
-->

<!-- research_source
source_id: S18
role: company_release
source_kind: document
publisher: Camtek Ltd.
title: Camtek Investor Presentation — August 2026
published_at: 2026-08-12
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://cdn.camtek.com/wp-content/uploads/IR-Presentation_Aug26.pdf
locator: PDF pp.6、8、17；收入組合圖列約 55% HPC／AI、20% non-AI AP 與約 75% Advanced Packaging，產品頁表示 Eagle G5／Hawk expected to account for 50% of 2026 revenue，Q2 highlights 列 1.332 億美元營收與 2026 年 1～7 月 6 億美元訂單
limitation: 這是發行人投資人簡報；約 75% 的圖示沒有標明量測期間，50% 是 2026 全年預期，兩個集合可能重疊；簡報沒有 AP 絕對收入、HBM-only 分子、客戶名稱、工具台數、產品毛利或客戶端驗證
independence_group: camtek
-->

<!-- research_source
source_id: S19
role: company_filing
source_kind: document
publisher: Nova Ltd.
title: Nova Reports Second Quarter 2026 Financial Results
published_at: 2026-08-06
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.sec.gov/Archives/edgar/data/1109345/000117891326003892/zk2635873.htm
locator: 2026Q2 Form 6-K 附件的 highlights、GAAP Results (K) 與 Management Comments；列出 254,958 千美元營收、Advanced Packaging solutions record revenue，以及 Sentronics dimensional metrology solutions for advanced packaging 為創高產品線之一
limitation: 公司只提供總營收與類別／產品線創高方向，沒有 advanced-packaging 金額、占比、HBM／2.5D 分解、客戶、工具數、毛利或可與其他公司 record 口徑比較的基準
independence_group: nova
-->

<!-- research_source
source_id: S20
role: company_release
source_kind: document
publisher: 弘塑科技股份有限公司
title: Honsu Group 2026Q2 Business Update
published_at: 2026-05-26
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://mopsov.twse.com.tw/nas/STR/313120260526M001.pdf
locator: PDF pp.5–6、13；Group Member 分列 wet-process equipment 與代理 metrology／inspection，Demand vs. Capacity 及 Process Application Opp. 把 2.5D、3D、HBM、CPO 列為需求增量或應用機會
limitation: 這是公司簡報的集團角色、無單位需求／產能指數與應用機會；沒有具名客戶、產品訂單、交付台數、檢查／量測收入、良率或工具毛利，也不能把集團代理能力全歸到弘塑本體
independence_group: honsu
-->

<!-- research_source
source_id: S21
role: company_filing
source_kind: document
publisher: 弘塑科技股份有限公司
title: 弘塑科技 2025 年度年報
published_at: 2026-06-17
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://doc.twse.com.tw/server-java/t57sb01?co_id=3131&colorchg=1&filename=2025_3131_20260617F04.pdf&kind=F&step=9
locator: PDF pp.49、59；主要產品營業比重列機台設備產品 4,550,881 千元／69.86%，客戶說明另把匿名 F 收入增加歸因 CoWoS 市場需求擴張
limitation: 機台設備產品是含清洗、顯影、蝕刻、去光阻與化學供應等的廣義類別，不是製程控制分子；年報的軟體／設備代理兩列金額與查核財報對調，F 客戶占比也和金額不符，因此本文只使用經既有獨立複核確認的機台設備金額與 69.86%，不採錯欄或替匿名 F 實名化
independence_group: honsu
-->

<!-- research_source
source_id: S22
role: company_filing
source_kind: document
publisher: 均華精密工業股份有限公司
title: 均華 2025 年度年報
published_at: 2026-05-19
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.gmmcorp.com.tw/upload-files/investor-zone/shareholder-area/2026/20260519-annual-report-cn.pdf
locator: PDF pp.5–7、61–62、70；列半導體製程設備及相關精密模具 2,526,471 千元／93.90%、Chip Sorter／Die Bonder／AOI 產品，以及 CPO sorter、1 µm 固晶位移量測與高解析六面檢查等 2026 開發計畫
limitation: 93.90% 是包含多種製程設備與精密模具的廣義發行人類別；既有產品與計畫開發清單沒有各機種收入、客戶 qualification、訂單、交付、簽收、良率或毛利，2026 開發計畫也不是已完成產品或已認列收入
independence_group: gallant-micro-machining
-->

<!-- research_source
source_id: S23
role: company_filing
source_kind: document
publisher: 萬潤科技股份有限公司
title: 萬潤科技 2025 年度年報
published_at: 2026-06-26
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://doc.twse.com.tw/server-java/t57sb01?co_id=6187&colorchg=1&filename=2025_6187_20260626F04.pdf&kind=F&step=9
locator: PDF pp.62–63、68–69；主要產品營業比重列半導體設備 96.13%，產品表列錫球檢查、六面外觀檢查與厚度量測，研發表列影像辨識、量測及光通／AI 封裝設備方向
limitation: 96.13% 是同時涵蓋點膠、送收料、耦合、貼合、植球、檢查、量測與自動化的廣義類別；產品與研發表沒有各工具收入、具名客戶、qualification、訂單、驗收、良率或毛利
independence_group: all-ring-tech
-->

<!-- research_source
source_id: S24
role: company_release
source_kind: living_index
publisher: 萬潤科技股份有限公司
title: 高精度光學耦合技術，驅動新一代光電整合應用
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.allring-tech.com.tw/product-detail20.htm
locator: 2026-08-14 現行產品頁；高精度主動耦光、精密點膠與固化補償、即時光學驗證與製程閉環控制、整合式光耦合流程小節
limitation: 這是發行人現行產品行銷頁，能證明公開描述的功能與整合流程，不能證明具名客戶採用、qualification、量產稼動、良率改善、售價、收入、毛利或頁面功能均已由客戶獨立驗證
independence_group: all-ring-tech
-->

<!-- research_source
source_id: S25
role: company_release
source_kind: document
publisher: Applied Materials
title: DRAM and Advanced Packaging Master Class — Prepared Remarks
published_at: 2026-06-25
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://investors.appliedmaterials.com/static-files/e8307fb9-c40b-4fee-abf9-3209c76ab08d
locator: PDF pp.5、38–42；pp.38–40 列 eBeam process-control 任務、VeritySEM 7AP／SEMVision G7AP 與多家 memory／logic AP 客戶 production 陳述，pp.41–42 列 2020～2024 AP business 成長與 2026 年收入預測
limitation: 這是發行人 prepared remarks；超過 20 億美元與逾 50% 都是 2026 整體 advanced-packaging revenue 的下限式預測，不是已實現結果，也沒有拆 advanced-packaging process-control、具名工具、客戶、台數、訂單、收入、毛利或客戶端良率；production 是供應商陳述
independence_group: applied-materials
-->

<!-- research_source
source_id: S26
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials Announces Third Quarter 2026 Results
published_at: 2026-08-13
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://investors.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results
locator: Quarter ended 2026-07-26 的 Financial Results、Recent Highlights 與 Semiconductor Systems revenue／customer application table；列公司營收 9.115 billion 美元、部門營收 7.040 billion 美元、67%／26%／7% 客戶應用組合及六項 DRAM／AP 系統
limitation: 公司與部門實際營收、客戶應用組合及具名產品是四種不同分母；公告沒有拆 advanced-packaging、PDC、AP-specific PDC、VeritySEM 7AP 或 SEMVision G7AP 的 actual revenue、order intake、工具數、客戶、毛利或客戶端成效，且產品與需求評論都是發行人陳述
independence_group: applied-materials
-->

<!-- research_source
source_id: S27
role: company_release
source_kind: document
publisher: Applied Materials
title: Applied Materials Q3 FY2026 Earnings Presentation
published_at: 2026-08-13
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://ir.appliedmaterials.com/static-files/9d5d182d-f060-4b22-a32c-4582257fdc9b
locator: PDF pp.5、8–9、15–18；p.5 定義 CY26 為 FQ2'26～FQ1'27 且 FQ1'27 為 14 週，pp.8–9 分列 AP revenues expected to grow over 70% 與 PDC revenue expected to grow over 50%，pp.15–18 列 Q3 公司／部門結果與 Q4 展望
limitation: 兩個百分比都是管理層對不同廣義集合的 lower-bound forecasts，不是已實現收入，也沒有揭露兩集合交集、基期／終值金額、AP-specific PDC、產品收入、order intake、工具數、客戶成效或預測區間；公司定義 CY26 不是一般 1～12 月曆年
independence_group: applied-materials
-->

<!-- research_source
source_id: S28
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: Effects of Wafer Noise on the Detection of 20 nm Defects Using Optical Volumetric Inspection
published_at: 2015-02-11
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.nist.gov/publications/effects-wafer-noise-detection-20-nm-defects-using-optical-volumetric-inspection
locator: NIST publication abstract；分開 noncritical patterning imperfections 與 impact manufacturing yield 的 critical defects，並描述 line-edge roughness wafer noise 降低 signal-to-noise ratio、增加 false positives 與 overlooked defects 的檢查問題
limitation: 這是 20 nm patterned-wafer optical inspection 的研究摘要與 intentional-defect-array／simulation 脈絡，不是 HBM／2.5D／3D 封裝量產 recipe、客戶 control plan 或任何工具的現行量產績效；critical／noncritical 與 noise 機制不能直接外推成封裝良率或設備需求
independence_group: nist
-->

<!-- research_source
source_id: S29
role: other_primary
source_kind: living_index
publisher: National Institute of Standards and Technology
title: Quantitative Nanoscale Imaging Through Artificial Intelligence
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.nist.gov/programs-projects/quantitative-nanoscale-imaging-through-artificial-intelligence
locator: 2026-08-14 現行 ongoing project page；Description 的 defect／defect-free 四種判定結果，以及 2019 accomplishments 對 line-edge roughness、false detection、classification 與調整 decision threshold 的說明；頁面 metadata 為 Created 2019-09-19、Updated 2026-07-08
limitation: 這是 NIST 持續更新的研究計畫頁，主要使用模擬 patterned-defect images 與 ML 方法；四格結果是一般分類框架，沒有本文可用的 production TP／FP／FN／TN、重複試驗、封裝客戶、良率、工具數或財務資料
independence_group: nist
-->

<!-- research_source
source_id: S30
role: company_release
source_kind: living_index
publisher: Taiwan Semiconductor Manufacturing Company Limited
title: Intelligent Packaging Fab
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.tsmc.com/english/dedicatedFoundry/services/apm_intelligent_packaging_fab
locator: 2026-08-14 現行頁面正文；die-level MES 的 instant die information／dispatch／defect interception and classification／yield prediction，ADC 的 defect interception and classification，以及 yield analysis engine 的 defective-material isolation 段落
limitation: 這是台積電對自家先進封裝智慧製造能力的現行服務頁；沒有固定產品／layer、sampling universe、recipe version、truth method、TP／FP／FN／TN、結果時間、圍堵批數、良率、重工、報廢、工具供應商、工具數、支出或收入，不能量化成效或設備 wallet share
independence_group: tsmc
-->

<!-- research_source
source_id: S31
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: NIST／SEMATECH Engineering Statistics Handbook Chapter 6 — Process or Product Monitoring and Control
published_at: 2003-06-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc13.htm
locator: §§6.1.3–6.1.4；§6.1.3 將 process control 定義為依監控結果主動改變製程，分列 process-specific OCAP 與自動 APC loop；§6.1.4 說明 out-of-control 後依 control-chart OCAP 尋找 assignable cause
limitation: 這是 NIST／SEMATECH 通用統計工程手冊，不是 HBM／advanced-packaging 客戶 recipe、法規或共同產業標準；沒有固定 sampling unit、警報門檻、時間戳、材料範圍、重工／報廢、良率、成本或財務資料
independence_group: nist
-->

<!-- research_source
source_id: S32
role: company_release
source_kind: living_index
publisher: Taiwan Semiconductor Manufacturing Company Limited
title: Automation in Packaging Fab
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.tsmc.com/english/dedicatedFoundry/services/apm_intelligent_packaging_fab/intelligentFab_automation
locator: 2026-08-14 現行頁面 Machine Learning for Quality Management 與 Big Data Analysis for Yield and Quality Defense；inline ADC 的 during-processing detection／affected-material isolation、offline ADC 的 post-process detection／lot hold，以及 per-die 2D barcode、process history、tool logs、material data、yield、impact-scope 與 root-cause 段落
limitation: 這是台積電對自家先進封裝自動化能力的現行服務頁；沒有 product／revision、tool／recipe、OCAP、完整九事件時間戳、受影響 lot／die 數、false-alarm／escape、重驗／放行規則、良率、損失避免、工具供應商、支出或財務分母；inline／offline 功能不能外推成任一產線延遲或外部設備商收入
independence_group: tsmc
-->

<!-- research_source
source_id: S33
role: other_primary
source_kind: living_index
publisher: SEMI
title: Traceability Standards and Activities
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.semi.org/en/products-services/standards/traceability
locator: 2026-08-14 現行頁面 Traceability Standards and Activities 正文；unique device identification 跨 IC manufacturing／test／assembly 至 final system，以及 end-to-end traceability 對 performance／failure analysis 的說明
limitation: 這是 SEMI 標準入口與活動摘要，不是標準全文，也沒有證明任何 HBM 客戶採用 T23／E142 或特定實作；頁面未提供 event schema、時間戳、OCAP、圍堵、樣本、良率、工具數或財務資料
independence_group: semi
-->

<!-- research_source
source_id: S34
role: other_primary
source_kind: document
publisher: National Institute of Standards and Technology
title: Addressing Misclassification Costs in Machine Learning Through Asymmetric Loss Functions
published_at: 2023-04-27
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.nist.gov/publications/addressing-misclassification-costs-machine-learning-through-asymmetric-loss-functions
locator: NIST publication abstract；patterning-defect metrology 的 asymmetric misclassification cost、defect-as-nominal 後果、公開成本缺值、cost ratio／classification threshold 掃描、surrogate public datasets 與 strong class imbalance 段落
limitation: 這是 SPIE 2023 研究的 NIST 摘要，實驗使用公開 ML 資料集代替工業影像；論文的門檻、cost ratio 與 15%～40% 結果不是 HBM／advanced-packaging production 數據，也不能外推成客戶 recipe、複判產能、良率、設備需求或財務效果
independence_group: nist
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: KLA 在 FY26Q4 發布中表示，leading-edge foundry／logic 設計增加、記憶體效能規格複雜化與先進封裝機會正在帶動更高的 process-control 需求
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-28
basis: S1 的 CEO 評論直接把上述三項技術向量與 process-control demand 連結
boundary: 這是 KLA 管理層對需求驅動的陳述，不證明全產業支出比例、KLA 成長來源分解、客戶投資報酬或台灣公司訂單
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
claim: Applied Materials 表示，先進封裝已面臨過去只在晶圓廠出現的缺陷與量測問題，較小特徵與 HBM 堆疊的缺陷代價使製程控制成為關鍵，並稱其 SEMVision G7AP eBeam defect-analysis 系統已用於記憶體與邏輯廠商的高量產先進封裝
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-06-25
basis: S2 的 New eBeam Systems 小節直接描述 optical inspection 限制、HBM stack 報廢風險、CD metrology、defect review 與 high-volume production 使用狀態
boundary: 證實的是 Applied 的工程機制與自家產品部署陳述，不代表第三方驗證的全產業良率效果、市占或收入
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
claim: Onto Innovation 在 2026Q1 結果中表示，Dragonfly G5 已在一名 leading 2.5D logic 客戶與一名 HBM 客戶完成資格認證，且 Atlas G6 用於下一代邏輯與記憶體元件的 OCD metrology
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-05-05
basis: S3 的 Business Highlights 與 CEO 評論直接列出客戶類型、qualification 與產品用途
boundary: 資格認證是採用節點，不等於量產採購規模、收入、產業滲透率或台灣公司參與
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
claim: 三個獨立設備供應商的一手文件共同支持一個縮窄後的研究判讀：HBM、2.5D 與 3D 整合提高幾何、材料、翹曲與缺陷代價，使量測、檢查及良率學習在工程上的重要性上升
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-28
basis: S1 提供 memory／advanced-packaging process-control 需求方向，S2 提供缺陷與量測機制及高量產使用敘述，S3 提供 2.5D logic 與 HBM 客戶資格節點
boundary: 交叉證據只支持需求機制與資格節點，不證明全產業 wallet share、工具數量、供應商排名、價格、毛利或台灣公司訂單
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C9
resolution: 2026-08-06 Onto Q2 文件新增較寬事業組合的收入訊號，原工程需求與資格節點判讀仍成立，但已不足以描述目前證據成熟度；由 C9 接續並保留不可歸因邊界
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 全產業配置給 metrology、inspection 與 yield-learning 的設備 wallet share 已隨 HBM／先進封裝世代結構性上升
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: 現有來源來自三家設備供應商，沒有共同口徑的客戶資本支出、工具數、製程步驟或全市場資料
boundary: 不以三家公司產品公告、資格節點或單一發行人營收成長替代全產業 wallet-share 證據
verification_needed: 需要客戶端資本支出與製程控制步驟、兩期以上同口徑工具需求，或可信產業資料交叉驗證支出比例與定義
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 台灣 semiequip、material、pcb 或 packtest 族群中的特定公司已因這波製程控制需求取得新增訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 至 S3 未點名 universe 內公司、產品、客戶或財務貢獻
boundary: 目前只建立族群搜尋路由，stock_ids 保持空白，不把同族群或相鄰製程自動改寫成受惠者
verification_needed: 台灣公司公告、財報或法說須明確連結量測／檢查產品、HBM／先進封裝客戶階段，以及可辨識的訂單或財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: KLA 的 FY26Q4 成長主要反映全產業製程控制強度提高，而不是 KLA 自身市占、ASP、產品組合或服務收入變化
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-02
basis: S1 提供管理層需求解釋與發行人分部揭露，但沒有可重建的 growth bridge 將上述驅動逐一分解
boundary: 不用 KLA 單一公司的結果反推全產業支出比例，也不把未分解成長當成台灣供應鏈需求
verification_needed: 需要 KLA 單位出貨、ASP、服務與產品組合分解，並以同期間客戶支出及獨立同業資料交叉核對
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Onto Innovation 在 2026Q2 結果中表示，Specialty Devices and Advanced Packaging 收入創季度新高，支撐來源包含 advanced packaging 的 2.5D logic、HBM 與 silicon photonics 應用
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-06
basis: S8 的 Second Quarter Business and Financial Highlights 直接列出收入成熟度與支撐應用，且該附件隨 Form 8-K 公開
boundary: 這是 Onto 對較寬事業組合的公司陳述；沒有揭露該類別收入金額、占比、產品分子、工具數、客戶數或各應用貢獻，不能改寫成 Dragonfly、HBM 或製程控制工具的專屬收入新高
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: superseded
claim: 現有跨公司一手證據支持一個更新後且仍受限的成熟度判讀：HBM、2.5D 與 3D 整合提高製程控制的工程重要性，至少部分供應商產品已走到客戶資格或供應商自述的高量產，而 Onto 較寬事業組合又出現收入訊號
supporting_source_ids: S1,S2,S3,S8
contrary_source_ids:
as_of: 2026-08-06
basis: correction_of:C4；S1 提供需求方向，S2 提供缺陷機制及高量產使用陳述，S3 提供 2.5D logic／HBM 客戶資格節點，S8 提供較寬事業組合的收入成熟度；S8 與 S3 同屬 Onto 消息鏈，不另算第四個獨立公司
boundary: 更新後判讀只把證據階梯推到供應商端商業訊號；它不證明全產業 wallet share、每世代工具數、題材收入分子、客戶資本支出分母、台灣公司訂單、價格、毛利或供應商排名
verification_needed:
correction_kind: supersedes
corrects_claim_id: C4
corrected_by_claim_id: C22
resolution: 保留 C4 的工程機制與 S8 的較寬收入訊號，但 2026-08-14 新增 Camtek 具名工具訂單、近似 AP／公司收入占比及 Nova 產品線銷售訊號後，C9 已不足以描述目前商業證據階梯；由 C22 接續
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: SEMI 2026 先進封裝峰會的官方議程摘要把 3DIC 製造挑戰具體拆到高深寬比 TSV 蝕刻、無空洞填孔、介電層沉積、inter-die gap fill、plasma dicing、面板翹曲與細 RDL，並把 data-driven control、metrology 與 yield learning 列為製造或採用問題
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-07-15
basis: S9 的 Lam、Samsung 與 NVIDIA 三段公開議程摘要直接列出上述工序、控制點與整合障礙
boundary: 證實的是 SEMI 官方頁保存的講者摘要內容，不是完整簡報、共同測試、第三方量產驗證或市場資料；CPO 段只作相鄰案例，不能反推 HBM 使用相同 BOM 或工具組合
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: NIST 的 2025 研究把 semiconductor virtual metrology 的限制拆成量測資料成本、sensor drift／shift 與資料可得性，並以模型不確定性驅動 adaptive sampling，在公開 CMP dataset 上驗證追蹤漂移且減少實體量測資料需求的方法
supporting_source_ids: S10
contrary_source_ids:
as_of: 2025-01-20
basis: S10 abstract 直接列出問題、online Gaussian-process framework、uncertainty quantification、adaptive sampling 與 public CMP dataset validation
boundary: 只證實該論文的方法與單一公開資料驗證；不代表 HBM／先進封裝量產線已採用、抽樣可以任意降低，或模型能取代實體量測、客戶 recipe 與失效驗證
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
claim: Applied Materials 表示，先進邏輯與記憶體的 optical inspection defect map 變密後，eBeam review 要在更多 sampling candidates 下同時維持 throughput、sensitivity 與 coverage，並以 deep-learning classification 分離 true defects 與 nuisance signals
supporting_source_ids: S11
contrary_source_ids:
as_of: 2025-02-19
basis: S11 的 dense defect maps／sampling 段落及 CFE、Deep learning AI image models 兩個 bullet 直接列出四項取捨與產品功能
boundary: 這是 Applied 對 SEMVision H20 的公司技術陳述；不採用其倍數作共同產業參數，也不把 leading-edge wafer defect review 直接視為 HBM advanced-packaging control plan、客戶良率或收入
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
claim: KLA 的 advanced-packaging 產品公告把 wafer-level inline control、切割後 sidewall-crack inspection、指定 100% IR inspection，以及 package assembly inspection／metrology 分成不同工具與任務
supporting_source_ids: S12
contrary_source_ids:
as_of: 2020-09-21
basis: S12 的 Kronos 1190、ICOS F160XP 與 ICOS T3／T7 段落逐項列出製程位置、檢查對象、coverage 與處置功能
boundary: 只證實 KLA 2020 產品組合的任務分工；不代表每座先進封裝廠採相同 recipe、每站都 100% inspection、現行 HBM 使用相同工具，或工具數與收入等比例增加
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
claim: 研究 advanced-packaging process control 時，「多檢查」不是可比較規格；一份可用 control plan 至少要對齊失效與決策、工序與檢查單位、抽樣覆蓋、靈敏度與逃逸、偽警報與分類，以及結果時間與異常圍堵六個欄位
supporting_source_ids: S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S10 建立成本、漂移、不確定性與 adaptive sampling；S11 建立 candidate density、throughput、sensitivity、coverage 與 nuisance classification；S12 建立 inline monitoring、post-dicing inspection、100% screening 與 disposition 的不同任務，研究端將其整理為六欄閱讀契約
boundary: 六欄是研究與 control-plan 查核框架，不是標準、唯一 recipe 或設備計分；沒有客戶端同產品 escape／false-alarm／cycle-time／yield 數據，不支持工具量、wallet share、供應商排名、台灣公司訂單或財務貢獻
verification_needed: 同一 production product／layer 的版本化 control plan，公開 sampling unit／coverage、sensitivity／escape、FAR／classification、time-to-result／containment、良率與重工／報廢結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C15
label: verified
status: active
claim: NIST／SEMATECH e-Handbook 把量測系統視為一個以量測結果為輸出的製程，要求把 bias、短期精密度、日間／長期變異與 uncertainty 分開；Gauge R and R 章節另把 repeatability、reproducibility、stability、resolution、linearity、hysteresis、drift，以及設備、設定與操作差異列為不同誤差來源
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-12
basis: S14 Chapter 2 的 characterization、variability、Gauge R and R 與 uncertainty 章節直接列出量測品質、變異分層及 gauge-study 誤差來源
boundary: 只證實 NIST／SEMATECH 手冊的通用量測框架；不代表所有半導體任務採相同研究設計、術語或允收值，也沒有提供 HBM 客戶 recipe、設備能力門檻、良率結果或財務資料
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
claim: NIST 將計量可追溯性定義為特定量測結果可經由有文件紀錄且不中斷的校正鏈連到參考、每一環均納入不確定度；只使用曾校正的設備並不足夠，仍須交代被測量、量測系統、帶不確定度的結果、校正參考與持續量測保證
supporting_source_ids: S15
contrary_source_ids:
as_of: 2021-05-06
basis: S15 §§5.1.1、5.2.1 與 5.4.3 直接區分 measurement result 與 instrument 的 traceability，並列出建立可追溯鏈所需文件及 measurement-assurance elements
boundary: 可追溯不表示不確定度一定 fit for purpose，也不替特定產品決定放行／隔離門檻；NIST 校正或參考鏈不是對設備品牌、供應商能力、量產良率或收入的認證
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
claim: 在把量測或檢查結果用於 advanced-packaging process control 前，研究端應先對齊一份六欄 measurement-system contract：被測量／單位／決策、方法／組態／環境、參考／校正／可追溯鏈、偏差／解析度／線性、重複性／再現性／穩定性，以及不確定度／決策規則；通過後才接 control plan 的工序、抽樣、逃逸、偽警報、結果時間與圍堵
supporting_source_ids: S10,S11,S12,S14,S15
contrary_source_ids:
as_of: 2026-08-12
basis: S14 建立 measurement-process error 與 variability 分層，S15 建立 measurand、calibration chain、uncertainty 與 measurement assurance，S10 顯示半導體 virtual metrology 仍受資料成本、drift／shift 與不確定性約束，S11／S12 分別拆出 defect review 的速度靈敏度覆蓋雜訊取捨及封裝檢查的不同工序任務；研究端將五者整理成量測系統與 control plan 兩層契約
boundary: 六欄是本研究中心的閱讀與查核框架，不是正式半導體標準、唯一 Gauge R and R 設計或客戶 recipe；框架完整不代表新增工具、客戶良率、wallet share、台灣公司訂單或財務貢獻
verification_needed: 同一 production product／layer 的版本化 measurement-system record，公開 measurand／unit、method／configuration／environment、reference／calibration chain、bias／resolution／linearity、repeatability／reproducibility／stability、uncertainty／decision rule，並接到實際 control-plan decision 與製造結果
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C18
label: verified
status: active
claim: Camtek 2026 年 6 月隨 6-K 公開的公告表示，公司取得 tier-1 OSAT 的 5,500 萬美元 multi-system order，以及 leading HBM player 超過 5,000 萬美元、全部為 Hawk 系統的訂單，兩組都預計在 2027 年交付
supporting_source_ids: S16
contrary_source_ids:
as_of: 2026-06-02
basis: S16 標題把兩組訂單合稱超過 1.05 億美元，正文逐組列出客戶類型、金額、Hawk 產品範圍與預計交付年度
boundary: 證實的是發行人收到訂單的陳述；客戶未具名，訂單不是已認列營收，也沒有工具台數、客戶產能、取消條件、產品毛利、台灣供應鏈或 2027 實際交付結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C19
label: verified
status: active
claim: Camtek 2026 年 8 月投資人簡報的收入組合圖把約 55% HPC／AI 與 20% non-AI advanced packaging 合計標為約 75% 的公司收入，並表示 Eagle G5 與 Hawk 預期占 2026 年收入 50%
supporting_source_ids: S18
contrary_source_ids:
as_of: 2026-08-12
basis: S18 PDF p.6 的 revenue mix 圖與 p.8 的 new-products 頁分別直接列出上述占比與預期
boundary: 約 75% 圖示沒有標明量測期間，50% 是全年預期而非實績，且 AP／AI 與產品集合可能重疊；不能反推特定季度 AP 金額、HBM-only 收入、客戶、工具數或毛利
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: Camtek 2026Q2 結果公布公司營收 1.332 億美元，並表示年初至今接單超過 6 億美元、交付橫跨 2026 年剩餘期間至 2027 年，另預期 AP revenue 從 2026Q1 到 Q4 約成長 70%
supporting_source_ids: S17
contrary_source_ids:
as_of: 2026-08-10
basis: S17 的 Financial Highlights、CEO 評論與 Financial Results 直接列出公司營收、order-intake lower bound、交付窗口及 AP 相對成長預期
boundary: 1.332 億美元是公司全部已認列營收，沒有 AP 分子；超過 6 億美元是跨期訂單下限，70% 是未附絕對基期的前瞻陳述，三者不能互除或相加
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: Nova 2026Q2 6-K 附件列出 GAAP 營收 254,958 千美元，並表示 Advanced Packaging solutions 收入創高，Sentronics dimensional-metrology solutions for advanced packaging 是創高產品線之一
supporting_source_ids: S19
contrary_source_ids:
as_of: 2026-08-06
basis: S19 的 highlights、GAAP Results (K) 與 Management Comments 分別提供公司總營收、AP 類別新高及具名產品線銷售方向
boundary: 公司沒有公布 AP 金額／占比、HBM／2.5D 分解、客戶、工具數或產品毛利；公司總營收不能替代題材分子，Nova 的 record 也不能和 Onto 的較寬 record 直接排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: 現有跨公司一手證據把製程控制的商業成熟度推進到「工程需求—客戶資格／供應商量產陳述—具名工具未來訂單—一家公司較寬 AP 收入占比—兩家供應商較寬類別／產品線收入訊號」，但仍沒有兩條獨立且同期間的題材分子—公司或客戶分母橋接
supporting_source_ids: S1,S2,S3,S8,S16,S17,S18,S19
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C9；S1～S3 建立需求機制、量產陳述與資格節點，S8 建立 Onto 較寬類別收入訊號，S16～S18 同一 Camtek 鏈新增 Hawk 未來訂單、公司總營收、跨期總訂單與未標期間的近似 AP 收入組合，S19 獨立新增 Nova AP／Sentronics 銷售訊號；Camtek 三份文件只算一條公司鏈
boundary: 這條階梯仍不是全產業 wallet share 證據；Camtek 約 75% 的期間未標，Nova／Onto 無 AP 金額，沒有客戶資本支出或產能分母、同口徑工具數、良率結果、台灣公司訂單、價格、毛利或供應商排名
verification_needed: 至少再一條獨立公司鏈，以同一期間公開具名 advanced-packaging process-control 產品／類別的已認列收入或已接訂單及公司分母，並分開 actual、order 與 forecast；或一份客戶文件公開每單位產能支出與工具／控制步驟
correction_kind: supersedes
corrects_claim_id: C9
corrected_by_claim_id:
resolution: 保留 C9 的工程—資格—量產陳述—較寬收入階梯，新增 Camtek 的具名 Hawk 訂單與近似 AP／公司收入占比，以及 Nova 的獨立產品線銷售訊號；同時維持期間與題材分子尚未對齊的限制
-->

<!-- research_claim
claim_id: C23
label: verified
status: active
claim: 弘塑 2025 年報列機台設備產品收入 4,550,881 千元、占公司收入 69.86%；集團簡報另把濕製程設備、代理 metrology／inspection 與 2.5D／3D／HBM／CPO 應用機會分開呈現
supporting_source_ids: S20,S21
contrary_source_ids:
as_of: 2026-06-17
basis: S21 的主要產品營業比重提供已認列廣義機台金額與占比，S20 的 Group Member 及 Process Application Opp. 提供集團產品角色與應用機會；兩份文件未把代理檢查／量測收入併入具名製程控制分子
boundary: 69.86% 含廣義濕製程與化學供應等機台；應用機會、集團代理能力與匿名客戶說明都不能替代具名檢查／量測產品、客戶階段、訂單、驗收收入、良率或毛利，也不得替匿名 F 客戶實名化
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C24
label: verified
status: active
claim: 均華 2025 年報列半導體製程設備及相關精密模具收入 2,526,471 千元、占公司收入 93.90%，並分開列示既有 Chip Sorter／Die Bonder／AOI 與 2026 年 CPO sorter、1 µm 固晶位移量測、高解析六面檢查等開發計畫
supporting_source_ids: S22
contrary_source_ids:
as_of: 2026-05-19
basis: S22 的營業比重、商品項目及計畫開發新商品表直接提供廣義收入類別、既有產品與未來研發清單
boundary: 93.90% 沒有拆到任一 AOI／量測工具；產品清單不證明客戶 qualification 或量產採用，開發計畫也不是訂單、交付、簽收、收入、良率或毛利
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C25
label: verified
status: active
claim: 萬潤 2025 年報列半導體設備占公司收入 96.13%，並列出錫球／六面外觀檢查與厚度量測產品；現行 CPO 產品頁另描述主動對準、即時光學驗證與製程資料回饋能力
supporting_source_ids: S23,S24
contrary_source_ids:
as_of: 2026-08-14
basis: S23 的主要產品比重與商品表提供廣義設備占比及具名檢查／量測工具，S24 的產品頁提供光耦合平台公開功能描述
boundary: 96.13% 同時包含多種點膠、搬運、接合、檢查、量測與自動化設備；產品表與行銷頁不證明各工具收入、客戶 qualification、訂單、驗收、量產稼動、良率改善或毛利
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C26
label: inference
status: active
claim: 弘塑、均華與萬潤的正式揭露共同示範：廣義先進封裝／半導體設備收入、具名檢查量測產品與研發計畫是三種不同證據，只有把產品任務、客戶階段、會計狀態及同期間題材分子—公司分母對齊，才能判定製程控制的商業材料性
supporting_source_ids: S20,S21,S22,S23,S24
contrary_source_ids:
as_of: 2026-08-14
basis: C23～C25 分別建立三家公司廣義收入類別、產品／應用與研發成熟度；M2 又保存三個發行人類別定義不同、不可排名的可比性裁決
boundary: 這是 N=3 指定案例的一手文件教材，不是 121 檔、台灣設備業或全產業抽樣；沒有 sampling SE／t，也不能由未拆分題材分子推論三家公司沒有相關收入、訂單或技術能力
verification_needed: 任一公司以同一期間把具名檢查／量測／良率學習產品、客戶 qualification 或量產階段、actual／order／forecast 狀態及公司／部門分母完整接起；跨公司比較另須統一定義
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C27
label: verified
status: active
claim: Applied 2026 DRAM／Advanced Packaging Master Class prepared remarks 表示 2020～2024 年 AP business 成長超過三倍，並預期 2026 年 AP revenue 年增超過 50% 至超過 20 億美元；同份文件稱 VeritySEM 7AP 與 SEMVision G7AP 已在多家 leading memory／logic AP 客戶 production，但未拆出 AP process-control 收入
supporting_source_ids: S25
contrary_source_ids:
as_of: 2026-06-25
basis: S25 pp.38–42 分別直接提供具名 eBeam 工具的 production 陳述與整體 AP 事業的歷史方向及 2026 雙下限預測；完整 prepared remarks 沒有把整體 AP 數值分解到 process-control 或兩項工具
boundary: 超過 20 億美元與逾 50% 都是 forecast lower bounds，不能反推精確 2025 基期；整體 AP 範圍大於製程控制，production 也沒有客戶名稱、工具數、actual revenue、order intake、毛利或客戶端良率，文件級未拆分不代表公司沒有內部數據
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C28
label: verified
status: active
claim: Applied FY26Q3 截至 2026-07-26 的公司實際營收為 91.15 億美元、Semiconductor Systems 實際營收為 70.40 億美元，部門客戶應用組合為 foundry／logic／other 67%、DRAM 26%、flash 7%；同一公告重述六項 DRAM／AP 系統，但未拆 AP、PDC 或 AP-specific PDC 財務分子
supporting_source_ids: S26
contrary_source_ids:
as_of: 2026-08-13
basis: S26 的 Financial Results、Recent Highlights 與 Semiconductor Systems table 直接列出公司／部門實際營收、客戶應用組合及六項系統；公告沒有把任一數字分解到 AP、PDC 或兩者交集
boundary: 客戶應用組合不是產品組合，不能把 DRAM 26% 改寫成 HBM／AP／eBeam 收入；具名產品也沒有收入、order intake、工具數、客戶、毛利或成效，單份公告未拆分不代表公司內部沒有資料
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C29
label: verified
status: active
claim: Applied Q3 FY2026 簡報預期 CY26 advanced-packaging revenues 成長超過 70%、process diagnostics and control revenue 成長超過 50%，並把 CY26 定義為 FQ2'26～FQ1'27、其中 FQ1'27 為 14 週季度
supporting_source_ids: S27
contrary_source_ids:
as_of: 2026-08-13
basis: S27 pp.5、8–9 分別直接提供公司定義期間與兩項 lower-bound growth forecasts
boundary: AP 與 PDC 是兩個不同廣義集合；百分比不是 actual、沒有基期／終值金額或預測區間，CY26 也不是一般 1～12 月曆年，不能未對齊期間就和其他公司排名
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C30
label: inference
status: active
claim: Applied 的 AP 成長逾 70% 與 PDC 成長逾 50% 不能決定 AP-specific PDC 交集的收入或成長率；公司／部門實績、客戶應用組合與產品名也不能替代該交集分子
supporting_source_ids: S26,S27
contrary_source_ids:
as_of: 2026-08-13
basis: C28 建立公司—部門—客戶應用—產品四層仍無 AP-specific PDC 分解，C29 建立 AP 與 PDC 兩個廣義集合的各自預測；集合的邊際總額／成長率不會唯一決定交集，虛構指數案例只作確定性不可識別證明
boundary: N=1 是同一發行人的一組結果資料、公告與簡報只算一條公司消息鏈，不是設備商／客戶／產業樣本；集合算例不是公司估計且沒有 sampling SE／t，也不能由未揭露推論交集為零、成長或衰退
verification_needed: Applied 以同一期間揭露 AP-specific PDC 的 actual revenue、order intake、工具數或可重建產品分子及公司／部門分母；跨公司比較另須對齊會計期間與類別定義
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C31
label: verified
status: active
claim: NIST 的 2015 patterned-wafer 研究把製程圖形偏差分為 noncritical 與會影響製造良率的 critical defects，並指出 line-edge roughness 形成的 wafer noise 會降低 killer-defect signal-to-noise ratio，使檢查同時面臨 false positives 與 overlooked defects
supporting_source_ids: S28
contrary_source_ids:
as_of: 2015-02-11
basis: S28 abstract 直接區分 noncritical／critical patterning imperfections，並描述模擬 line-edge roughness 增加時 signal-to-noise ratio 下降及兩類錯誤判定問題
boundary: 這是 patterned-wafer optical inspection 的 intentional-defect-array／simulation 研究，不是 HBM／先進封裝客戶的 production recipe、混淆矩陣、良率或工具需求，也不能由研究年份推論現行設備仍有相同限制
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C32
label: verified
status: active
claim: NIST 的 ongoing nanoscale-imaging project page 將光學缺陷檢查明列為四種判定結果：defect／defect-free 各自可能被正確判定，也可能把 defect-free 誤判或把 actual defect 誤分；同頁並說明 decision threshold 可依錯誤代價調整，而不是只追求候選數最多
supporting_source_ids: S29
contrary_source_ids:
as_of: 2026-08-14
basis: S29 Description 直接列四種結果與兩種 false case 的不同 ramifications，2019 accomplishments 另描述針對 defect-inspection challenge 調整 threshold 以減少 wrong detections
boundary: 這是 NIST 對模擬 patterned-defect images 與 ML metrology 的方法頁，不提供封裝 production 的 TP／FP／FN／TN、樣本分母、confidence interval、良率、工具數或財務成效；threshold 方向不是任何客戶的允收值
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C33
label: verified
status: active
claim: 台積電現行 Intelligent Packaging Fab 頁面表示，先進封裝廠採用 die-level MES 提供即時 die 資訊、派工、缺陷攔截／分類及自動良率預測／最佳化，並以 ADC 在流程中攔截分類缺陷、由良率分析引擎偵測缺陷與隔離不良材料
supporting_source_ids: S30
contrary_source_ids:
as_of: 2026-08-14
basis: S30 現行正文逐項描述 die-level MES、ADC 與 yield analysis engine 在先進封裝廠的公開功能鏈
boundary: 這是客戶公司對自有能力的功能陳述，沒有產品／layer、受檢母體、recipe version、truth method、四格數據、cycle time、良率、重工／報廢、工具商、工具數、支出或財務分母；不能由 deployed 字樣推論任一外部設備商收入或成效幅度
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C34
label: inference
status: active
claim: 缺陷候選數只有在同一 product／layer、受檢母體、recipe／threshold、參考真值與分類版本下，才能先拆成 TP／FP／FN／TN；之後仍須通過 criticality、圍堵／根因與同 cohort 製造結果，才可連到良率損失。沒有客戶工具／支出與供應商 actual revenue 的共同期間鍵，也不能再跳接成設備 wallet share
supporting_source_ids: S11,S28,S29,S30
contrary_source_ids:
as_of: 2026-08-14
basis: S28／S29 建立 noncritical／critical、noise 與四格錯誤判定，S30 建立客戶端攔截—分類—良率預測—隔離功能鏈，S11 則顯示供應商工具還必須在 candidate density、throughput、sensitivity、coverage 與 nuisance classification 間取捨；研究端據此整理五道閘門
boundary: 五道閘門是研究中心查核框架，不是 NIST、台積電或 Applied Materials 共同發布的標準；三條消息鏈沒有公開同一封裝產品的混淆矩陣、因果良率結果、工具數或財務橋接，也不能由缺值推論成效為零或設備需求必然增加
verification_needed: 同一 production product／layer 的受檢與未檢母體、recipe／threshold version、reference-truth method、TP／FP／FN／TN、killer-defect mapping、containment／root-cause、良率／重工／報廢／cycle-time 結果，以及同期間客戶工具／支出與供應商 actual revenue
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C35
label: verified
status: active
claim: NIST／SEMATECH 將 process monitoring 偵測失控與 process control 主動改變製程分開，並說明 OCAP 規定失控訊號之後的動作、可按不同製程設計流程，再沿 control-chart OCAP 尋找 assignable cause
supporting_source_ids: S31
contrary_source_ids:
as_of: 2003-06-01
basis: S31 §§6.1.3–6.1.4 直接定義 monitoring 後的兩種 intervention、OCAP 與 out-of-control 後的 assignable-cause investigation
boundary: 這是通用方法定義，不表示每個訊號都是真異常、所有工廠使用同一 OCAP，也沒有指定 advanced-packaging 的 sampling、threshold、owner、stop／hold、recovery 或量化延遲
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C36
label: verified
status: active
claim: 台積電現行先進封裝自動化頁面分開描述 inline ADC 在製程中偵測並隔離受影響材料、offline ADC 在製程後偵測並 hold lots；同頁再以 per-die 識別把 wafer 位置、bin、製程歷史、tool logs、材料與 yield 接起來，以界定問題影響範圍並分析低良率根因
supporting_source_ids: S32
contrary_source_ids:
as_of: 2026-08-14
basis: S32 的兩個正文小節逐項提供 inline／offline 的動作差異與 product-resume 追溯欄位及用途
boundary: 這是客戶公司對自有功能的公開陳述，沒有 product／recipe／OCAP version、九事件 timestamp、affected count、false alarm／escape、rework／scrap、release、yield effect 或成本；不能推論每個場站均採相同流程或任一供應商財務貢獻
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C37
label: verified
status: active
claim: SEMI 的現行 traceability 入口表示，其標準範圍支援 unique device identification 從 IC 製造、測試與組裝一路到最終系統，並把端到端追溯連到 performance／failure analysis
supporting_source_ids: S33
contrary_source_ids:
as_of: 2026-08-14
basis: S33 正文直接描述 identification 範圍與 end-to-end traceability 用途
boundary: 入口摘要不等於標準全文、客戶採用證明或特定事件資料完整；unique ID 也不自動提供時間、工具、recipe、材料、OCAP、根因、圍堵成效或財務歸因
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C38
label: inference
status: active
claim: 研究 advanced-packaging excursion 時，工具訊號、確認、圍堵指令與實際 hold／isolate 必須分時記錄；受影響範圍再用 product／revision、lot／wafer／die／package、tool／chamber、recipe、材料批次與時間窗的 genealogy 重建，最後另記處置、修正、重驗與放行。只有 `signal-to-hold` 或單機 throughput，不能推出完整 excursion exposure、良率改善或避免損失
supporting_source_ids: S31,S32,S33
contrary_source_ids:
as_of: 2026-08-14
basis: S31 把 detection 與 OCAP intervention 分開，S32 提供 inline isolate、post-process hold 與 per-die impact-scope／root-cause 功能鏈，S33 建立跨製造測試組裝的 Unique ID 追溯邊界；研究端據此整理 t0–t8 九事件與共同識別鍵
boundary: 九事件護照是研究中心整合框架，不是 NIST、台積電與 SEMI 共同標準；N=3 條消息鏈不是廠、產品或事件樣本，沒有公開 HBM 量產時間戳、受影響量、對照組、sampling SE／t、工具數或財務共同鍵，也不能由缺值推論成效為零
verification_needed: 同一 production product／layer 的 product／recipe／OCAP version、t0–t8 原始時間戳、command／enforcement acknowledgement、genealogy 物件集合、retest／rework／scrap／release、同 cohort 良率／cycle-time／成本，以及同期間客戶工具／支出與供應商 actual revenue
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C39
label: verified
status: active
claim: NIST 2023 patterning-defect metrology 研究明確把 defect 誤標為 nominal 與 nominal 誤標為 defect 視為不對稱的錯判成本，指出前者影響較大、真實量化成本未公開，並以公開 ML 資料集作工業影像替代，在強類別不平衡下跨 cost ratio 與 classification threshold 評估總錯判成本
supporting_source_ids: S34
contrary_source_ids:
as_of: 2023-04-27
basis: S34 官方摘要的 Background、Aim、Approach 與 Conclusions 直接提供錯判不對稱、成本缺值、替代資料、門檻與 cost-ratio 掃描及 class-imbalance 範圍
boundary: 只驗證該研究的公開方法與資料邊界；摘要中的門檻、cost ratio、loss function 與 15%～40% 結果屬公開 surrogate datasets，不是 HBM／先進封裝量產線、客戶成本、模型績效、設備產能或財務結果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C40
label: inference
status: active
claim: 在本文 1,000,000 個假想受檢單位、真正關鍵缺陷 1,000 個的固定母體中，敏感門檻 A 的 accuracy 98.991%、precision 8.264462809917%、複判候選 10,890 個與 FN 100 個；較嚴門檻 B 的 accuracy 99.8801%、precision 44.469149527515%、候選 1,799 個與 FN 200 個。若每個候選複判成本為 1 單位，兩門檻總成本在每個 FN 成本 90.91 單位時相等；因此 accuracy、precision 或複判量任何單項都不能決定門檻
supporting_source_ids: S28,S29,S34
contrary_source_ids:
as_of: 2026-08-14
basis: Python Fraction 與獨立 awk 兩路用相同 TP／FP／FN／TN 整數表重算 accuracy、recall、FPR、precision、nuisance share、review-load reduction、兩條成本式與 crossover，所有顯示結果一致
boundary: 這是 N=1,000,000 個假想受檢單位與兩個假想門檻的確定性教材，不是抽樣或量產實驗；0.1% base rate、四格數、1 單位複判成本及 90.91 crossover 都不是任何產品、工廠或 NIST 實測，因此沒有 sampling SE／t，也不提供良率、工具數、收入或投資效果
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

## 為何值得進佇列

KLA 提供需求方向，Applied Materials 說明缺陷機制與自述的高量產使用，Onto Innovation
先提供 2.5D logic／HBM 客戶資格節點，再新增較寬事業組合的收入訊號；Camtek 把具名 Hawk
訂單、交付年度、公司總營收與近似 AP 收入組合分開，Nova 則補上另一條具名量測產品線的
銷售訊號。Applied 又為整體 AP 提供 2026 年超過 20 億美元、年增逾 50% 的雙下限預測，
FY26Q3 再補公司／部門實績、客戶應用組合與 AP 逾 70%／PDC 逾 50% 兩條成長預測，
卻仍沒有拆出兩者交集。SEMI 議程把控制問題落到 TSV、填孔、沉積、翹曲、RDL、切割與相鄰的 CPO
整合。弘塑、均華與萬潤則把台灣映射落到廣義設備收入、產品清單與研發計畫三個不同層級，
並顯示其中任何一層都不能單獨替代製程控制題材分子。這些資料讓工程與供應商商業成熟度比
單一廠商說法更完整。NIST、Applied 與 KLA 的方法／產品文件又把 control plan
拆成動態抽樣、靈敏度、覆蓋、偽警報、結果時間與不同製程任務；NIST／SEMATECH 的量測
章節再補上 bias、repeatability、reproducibility、stability、uncertainty 與 traceability 的前置
契約；NIST／SEMATECH 的 OCAP、台積電 inline／offline 圍堵與 die-level 履歷、SEMI 的唯一
識別入口，又把「警報之後」拆成確認、指令、實際隔離、影響範圍、處置與復機。本題也不同於 ATE tester TAM：它研究製程中的量測、
缺陷定位與良率回饋。尚待證明的是需求有沒有變成更多工具步驟與較高支出占比；未拆出
產品分子、客戶分母、市占、ASP、產品組合與服務前，不能用發行人結果代表全產業，更不能
外推台灣公司受惠。

## 已驗證的證據階梯

| 層級 | 一手來源目前支持 | 仍不能外推 |
|---|---|---|
| 需求方向 | KLA 把 memory complexity、advanced packaging 連到 process control | 全產業 wallet share 或工具數 |
| 工程機制 | Applied 描述細小特徵、翹曲與高缺陷代價 | 第三方良率、總市場或排名 |
| 量測可信度前置關卡 | NIST／SEMATECH 把 bias、短長期變異、不確定度與可追溯鏈分開 | 特定 HBM 客戶方法、允收門檻或設備收入 |
| Control-plan 方法 | NIST、Applied 與 KLA 分別支持 adaptive sampling、coverage／sensitivity／nuisance 取捨及不同封裝檢查任務 | HBM 客戶 recipe、逃逸／偽警報、整廠 cycle time 或新增工具量 |
| 警報—圍堵功能鏈 | NIST／SEMATECH 分開 detection 與 OCAP intervention；台積電分開 inline isolate、post-process hold 與 per-die impact tracing；SEMI 建立跨製造／測試／組裝的 Unique ID 方向 | 同產品九事件時間戳、affected objects、處置／復機、良率／成本與工具財務 |
| 採用節點 | Onto 披露 2.5D logic 與 HBM 客戶資格認證 | 大量採購、收入或台灣參與 |
| 供應商端量產陳述 | Applied 稱特定 eBeam defect-analysis 系統已用於高量產先進封裝 | 客戶端部署數、良率實績或市占 |
| 具名工具未來訂單 | Camtek 披露 tier-1 OSAT 與 HBM player 合計超過 1.05 億美元的 multi-system orders，其中 HBM 訂單全為 Hawk，預計 2027 交付 | 已認列收入、工具台數、客戶名稱、毛利或客戶產能分母 |
| 較寬收入組合 | Camtek 簡報把約 55% HPC／AI 與 20% non-AI AP 合計標為約 75% 公司收入 | 期間未標，不能乘上單季公司營收或拆成 HBM-only 金額 |
| 較寬收入訊號 | Onto 稱 Specialty Devices and Advanced Packaging 收入創高，支撐含 2.5D／HBM | 類別金額、題材分子、特定工具收入或全產業支出 |
| 具名產品線銷售訊號 | Nova 稱 Sentronics advanced-packaging dimensional-metrology solutions 是創高產品線之一 | 產品線金額／占比、HBM 分解、工具數或跨公司 record 排名 |
| 較寬 AP 財務預測 | Applied 預期 2026 年整體 AP revenue 年增逾 50%、超過 20 億美元，並另稱兩項 AP eBeam 工具已在多家客戶 production | 兩個下限不是精確基期／終值；整體 AP 不等於 process-control 分子，採用陳述也未接到產品收入 |
| 公司／部門實績＋兩個廣義集合預測 | Applied FY26Q3 公布公司 91.15 億美元、Semiconductor Systems 70.40 億美元，並預期 CY26 AP revenue 成長逾 70%、PDC revenue 成長逾 50% | 客戶應用組合不是產品組合；兩個集合的成長率不能決定 AP-specific PDC 交集，CY26 也須按公司定義對齊 |
| 台灣廣義設備收入＋產品能力 | 弘塑、均華、萬潤各自揭露廣義設備比重，並列相鄰的檢查／量測產品、代理能力或研發計畫 | 同定義製程控制分子、具名客戶階段、實際訂單／驗收收入或跨公司排名 |

## 跨公司數字與可比性

本篇 `cross_company_numbers: true`，但只有 `M1` 的兩筆公司總營收符合直接比較條件：Camtek
與 Nova 都是截至 2026 年 6 月 30 日的三個月、GAAP 公司總營收，幣別與單位也相同。這只
能比較公司總營收數值，不能比較 advanced-packaging 強度；Camtek 的近似 75% 未標期間，
Nova 與 Onto 沒有 AP 金額，因此不建立跨公司的 AP 占比、訂單、工具數、市占或排名。

`M2` 則刻意保存相反的裁決：弘塑、均華與萬潤雖然都公布 2025 年百分比，但三個 metric
是發行人自訂的不同廣義設備類別，不能可靠正規化為同一製程控制曝險。它們只是一組
異質證據籃子，不提供高低、差距或投資排序。

<!-- metric_comparison
comparison_id: M1
comparison_kind: aligned_metric
observation_id: M1-O1
claim_id: C22
entity: Camtek
metric: GAAP consolidated total revenue
reported_value: 133.2
value_kind: point
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: calendar_quarter
unit: USD_million
definition_key: gaap_consolidated_total_revenue
definition: 截至 2026-06-30 三個月的發行人 GAAP 公司總營收；只作公司分母，不是 advanced-packaging 題材分子
evidence_ids: S17
comparability: directly_comparable
comparability_reason: 兩筆都是同一曆季、同幣別與同單位的發行人 GAAP 公司總營收；只比較公司分母，不比較 AP 收入、訂單、產品組合、毛利或投資價值
-->

<!-- metric_comparison
comparison_id: M1
comparison_kind: aligned_metric
observation_id: M1-O2
claim_id: C22
entity: Nova
metric: GAAP consolidated total revenue
reported_value: 254.958
value_kind: point
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: calendar_quarter
unit: USD_million
definition_key: gaap_consolidated_total_revenue
definition: 截至 2026-06-30 三個月的發行人 GAAP 公司總營收；只作公司分母，不是 advanced-packaging 題材分子
evidence_ids: S19
comparability: directly_comparable
comparability_reason: 兩筆都是同一曆季、同幣別與同單位的發行人 GAAP 公司總營收；只比較公司分母，不比較 AP 收入、訂單、產品組合、毛利或投資價值
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: heterogeneous_evidence
observation_id: M2-O1
claim_id: C26
entity: 弘塑
metric: issuer-defined machine equipment product revenue share
reported_value: 69.86
value_kind: point
period_start: 2025-01-01
period_end: 2025-12-31
period_basis: fiscal_year
unit: percent
definition_key: honsu_machine_equipment_product_revenue_share
definition: 弘塑 2025 年機台設備產品收入 4,550,881 千元占公司客戶合約收入 6,514,495 千元的發行人產品類別比重；類別含廣義濕製程與化學供應設備，不是製程控制題材分子
evidence_ids: S21
comparability: not_comparable
comparability_reason: 弘塑量的是自訂機台設備產品類別，與均華的半導體製程設備及精密模具、萬潤的半導體設備範圍不同；三者都未拆出同定義檢查／量測收入，只能作異質證據籃子，不能排名
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: heterogeneous_evidence
observation_id: M2-O2
claim_id: C26
entity: 均華
metric: issuer-defined semiconductor process equipment and precision mold revenue share
reported_value: 93.90
value_kind: point
period_start: 2025-01-01
period_end: 2025-12-31
period_basis: fiscal_year
unit: percent
definition_key: gmm_semiconductor_process_equipment_and_precision_mold_revenue_share
definition: 均華 2025 年半導體製程設備及相關精密模具收入 2,526,471 千元占公司收入 2,690,692 千元的發行人類別比重；沒有拆 Chip Sorter、Die Bonder、AOI 或量測工具
evidence_ids: S22
comparability: not_comparable
comparability_reason: 均華分子把製程設備與精密模具合併，與弘塑及萬潤的發行人分類不同；既有工具與研發計畫也不能補成同定義題材收入，只能作異質證據籃子，不能排名
-->

<!-- metric_comparison
comparison_id: M2
comparison_kind: heterogeneous_evidence
observation_id: M2-O3
claim_id: C26
entity: 萬潤
metric: issuer-defined semiconductor equipment revenue share
reported_value: 96.13
value_kind: point
period_start: 2025-01-01
period_end: 2025-12-31
period_basis: fiscal_year
unit: percent
definition_key: allring_semiconductor_equipment_revenue_share
definition: 萬潤 2025 年半導體設備占公司收入的發行人類別比重；類別同時包含點膠、搬運、耦合、貼合、植球、檢查、量測與自動化，不是製程控制題材分子
evidence_ids: S23
comparability: not_comparable
comparability_reason: 萬潤的半導體設備範圍大於檢查／量測，且不等於弘塑或均華的分類；產品頁功能不能正規化出財務分子，只能作異質證據籃子，不能排名
-->

## 來源與證據邊界

- [S1：KLA FY26Q4 結果](https://ir.kla.com/news-events/press-releases/detail/518/kla-corporation-reports-fiscal-2026-fourth-quarter-and-full)。
- [S2：Applied Materials DRAM／先進封裝與 eBeam 系統](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and/)。
- [S3：Onto Innovation 2026Q1 結果與 qualification](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Reports-2026-First-Quarter-Results/default.aspx)。
- [S8：Onto Innovation 2026Q2 Form 8-K 附件](https://www.sec.gov/Archives/edgar/data/704532/000119312526337990/onto-ex99_1.htm)（較寬事業組合創高，不含產品分子）。
- [S9：SEMI Advanced Packaging Summit 2026 官方議程](https://www.semi.org/en/connect/events/advanced-packaging-summit-2026)（講者摘要，不是完整實驗或量產資料）。
- [S10：NIST virtual metrology 與 dynamic sampling 研究](https://www.nist.gov/publications/comparative-study-semiconductor-virtual-metrology-methods-and-novel-algorithmic)（public CMP dataset，不是 HBM production recipe）。
- [S11：Applied Materials SEMVision H20 defect-review 公告](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-accelerates-chip-defect-review-next-gen-ebeam/)（供應商技術與採用陳述）。
- [S12：KLA advanced-packaging inspection portfolio](https://ir.kla.com/news-events/press-releases/detail/9/kla-announces-enhanced-portfolio-of-systems-for-advanced)（2020 產品任務分工，不是共同 control plan）。
- [S14：NIST／SEMATECH Measurement Process Characterization](https://www.itl.nist.gov/div898/handbook/mpc/mpc.htm)（通用 bias、變異、Gauge R＆R 與 uncertainty 方法，不是 HBM recipe）。
- [S15：NIST Technical Note 2156 計量可追溯性政策](https://www.nist.gov/publications/metrological-traceability-frequently-asked-questions-and-nist-policy)（可追溯的是特定量測結果，不是設備品牌背書）。
- [S16：Camtek 超過 1.05 億美元 multi-system orders 的 6-K 附件](https://www.sec.gov/Archives/edgar/data/1109138/000117891326003033/zk2635474.htm)（預計 2027 交付，不是已認列營收）。
- [S17：Camtek 2026Q2 結果](https://www.camtek.com/news-and-events/camtek-announces-results-for-the-second-quarter-of-2026/)（公司總營收、跨期接單下限與 AP 成長預期須分開）。
- [S18：Camtek 2026 年 8 月投資人簡報](https://cdn.camtek.com/wp-content/uploads/IR-Presentation_Aug26.pdf)（近似 AP 收入組合未標期間，全年新產品占比仍是預期）。
- [S19：Nova 2026Q2 6-K 附件](https://www.sec.gov/Archives/edgar/data/1109345/000117891326003892/zk2635873.htm)（AP／Sentronics 銷售創高但無題材金額）。
- [S20：弘塑 2026Q2 Business Update](https://mopsov.twse.com.tw/nas/STR/313120260526M001.pdf)（集團角色與 AP 應用機會，不是訂單或題材收入）。
- [S21：弘塑 2025 年報](https://doc.twse.com.tw/server-java/t57sb01?co_id=3131&colorchg=1&filename=2025_3131_20260617F04.pdf&kind=F&step=9)（廣義機台設備占比；錯欄與匿名客戶限制保留）。
- [S22：均華 2025 年報](https://www.gmmcorp.com.tw/upload-files/investor-zone/shareholder-area/2026/20260519-annual-report-cn.pdf)（廣義設備／模具收入、既有產品與研發計畫須分開）。
- [S23：萬潤 2025 年報](https://doc.twse.com.tw/server-java/t57sb01?co_id=6187&colorchg=1&filename=2025_6187_20260626F04.pdf&kind=F&step=9)（廣義半導體設備占比與產品清單，不含工具分子）。
- [S24：萬潤 CPO 光耦合產品頁](https://www.allring-tech.com.tw/product-detail20.htm)（發行人功能描述，不是客戶採用或財務證明）。
- [S25：Applied DRAM／Advanced Packaging Master Class prepared remarks](https://investors.appliedmaterials.com/static-files/e8307fb9-c40b-4fee-abf9-3209c76ab08d)（整體 AP 雙下限預測與具名工具 production 陳述仍未形成 process-control 收入分子）。
- [S26：Applied FY26Q3 結果公告](https://investors.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-third-quarter-2026-results)（公司／部門實績、客戶應用與產品名仍不是 AP-specific PDC 分子）。
- [S27：Applied Q3 FY2026 earnings presentation](https://ir.appliedmaterials.com/static-files/9d5d182d-f060-4b22-a32c-4582257fdc9b)（AP 與 PDC 兩個廣義集合的成長下限及公司定義期間，沒有交集金額）。
- [S28：NIST 20 nm wafer-noise／defect-detection 研究](https://www.nist.gov/publications/effects-wafer-noise-detection-20-nm-defects-using-optical-volumetric-inspection)（區分 noncritical／critical defect 並說明 false positive／overlooked defect；不是封裝量產 recipe）。
- [S29：NIST Quantitative Nanoscale Imaging Through AI](https://www.nist.gov/programs-projects/quantitative-nanoscale-imaging-through-artificial-intelligence)（四格判定與 threshold 方法頁，沒有 production confusion matrix）。
- [S30：台積電 Intelligent Packaging Fab](https://www.tsmc.com/english/dedicatedFoundry/services/apm_intelligent_packaging_fab)（客戶端攔截、分類、良率預測與不良材料隔離功能鏈，沒有同產品數值分母）。
- [S31：NIST／SEMATECH Process Control 與 OCAP](https://www.itl.nist.gov/div898/handbook/pmc/section1/pmc13.htm)（偵測後的處置方法，不是 HBM 量產流程或延遲資料）。
- [S32：台積電 Automation in Packaging Fab](https://www.tsmc.com/english/dedicatedFoundry/services/apm_intelligent_packaging_fab/intelligentFab_automation)（inline isolate、post-process lot hold 與 per-die impact tracing，沒有完整九事件分母）。
- [S33：SEMI Traceability Standards and Activities](https://www.semi.org/en/products-services/standards/traceability)（跨製造、測試與組裝的 Unique ID 標準入口，不是採用或圍堵成效證明）。
- [S34：NIST patterning-defect misclassification-cost 研究](https://www.nist.gov/publications/addressing-misclassification-costs-machine-learning-through-asymmetric-loss-functions)（不對稱錯判成本、門檻與 class imbalance 方法；公開 surrogate datasets 不是量產線）。
- 後續入口：[KLA](https://ir.kla.com/financial-information/financial-results)、[Applied](https://ir.appliedmaterials.com/news-releases/)、[Onto](https://investors.ontoinnovation.com/news/default.aspx)、[MOPS](https://mops.twse.com.tw/mops/web/index)。
- 中立方法入口：[NIST CHIPS Metrology Program](https://www.nist.gov/chips/research-development-programs/metrology-program)。

海外五家設備商與台灣三家公司彼此獨立但都有商業動機，其中同一公司的多份文件仍只算
一條公司消息鏈；SEMI 議程保存多位講者摘要，也不能替代完整簡報、客戶端或全產業資本
支出證據。台灣三家公司是依既有獨立複核筆記選出的定向教材，不是全 universe 抽樣；本輪
新增的 NIST 頁面與論文仍只算一條中立方法鏈，兩個台積電頁面仍只算一條客戶公司鏈，SEMI 追溯入口
另算一條產業標準消息鏈；也沒有一致預期、
估值、即時持倉或具名客戶—供應商雙向資料，因此不談市場是否反映或個股方向。

## 反方與替代路徑

- **供應商特有效果**：KLA 成長可能來自市占、ASP、產品組合或服務，而非類別支出增加。
- **資格不等於規模**：Onto 的 qualification 可能停在單一工具或客戶，未形成跨客戶量產。
- **較寬收入組合混合**：Onto 的新高可能由 silicon photonics、其他 specialty devices、產品組合或價格帶動，不能全歸因 HBM／2.5D 製程控制。
- **訂單不等於營收**：Camtek 的具名訂單預計 2027 交付，可能受交期、驗收與會計認列影響；不能拿它除以 2026Q2 公司營收製造跨期 book-to-bill。
- **占比集合重疊**：Camtek 的 AP、HPC／AI 與 Eagle G5／Hawk 不是互斥分類，且近似 AP 圖未標期間；不能相加或套用到單季分母。
- **公司分母不等於題材分子**：Nova 公司總營收可以和 Camtek 的公司總營收對齊，卻不能在 Nova 未拆 AP 金額時用來比較 AP 強度。
- **廣義設備比重不等於製程控制曝險**：弘塑、均華、萬潤的發行人類別定義不同，且都大於檢查／量測任務；69.86%、93.90%、96.13% 不能拿來排名。
- **產品頁與研發計畫不等於客戶採用**：具名 AOI、量測或閉環功能能建立搜尋入口，仍需 qualification、訂單、驗收與收入逐關接續。
- **整體 AP 預測不等於製程控制分子**：Applied 的逾 50%／超過 20 億美元是整體 AP forecast；兩個下限不能反推精確基期，也不能歸給 VeritySEM／SEMVision。
- **兩個大集合不會自動產生交集**：Applied FY26Q3 的 AP 逾 70% 與 PDC 逾 50% 不能平均、相乘或視為 AP-specific PDC 的上下界；公司定義 CY26 也不能未對齊就和曆年數字排名。
- **替代解法**：設計規則、抽樣或既有光學工具升級，可能降低新增工具需求。
- **價值沒有外溢**：支出即使增加，也可能集中於海外平台；台灣族群不必然受惠。

## 台灣族群觀察邊界

<!-- impact
group_id: semiequip
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: 製程量測、缺陷檢查、分析與封裝設備最接近本題，但需逐家公司核對產品、客戶資格與收入
evidence_boundary: 多份海外設備商文件仍未點名 universe 公司；族群相近不等於本地工具取得訂單或能取代國際設備
-->

<!-- impact
group_id: material
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: 更細結構、翹曲與異質整合可能提高材料控制要求，後續需查材料規格與認證節點
evidence_boundary: 現有來源只描述設備與製程問題，沒有點名台灣材料、用量、價格或毛利
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: chiplet 與先進封裝涉及有機或其他封裝基板的缺陷管理，但須先確認本 universe PCB 公司實際產品層級
evidence_boundary: 來源不支持把一般 PCB 營收、載板題材或海外檢查工具需求直接改寫成台灣公司受惠
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-14
rationale: OSAT 與先進封裝產線是製程控制使用端，需追資本支出、工具導入、良率與客戶量產階段
evidence_boundary: 使用端增加檢測不必然改善封測商收入或毛利，也不證明其採購台灣設備
-->

`stock_ids` 刻意留空；公司文件把具名產品、客戶階段與財務貢獻接起來前，四個族群都不是
受惠名單。

## 持續驗證清單

`review_due` 為 2026-08-15，等於所有 active monitoring item 中最早的 `next_check`。

<!-- monitoring_item
monitor_id: T1
status: retired
claim_ids: C4,C5
metric: HBM／advanced-packaging 每一產品世代或單位產能所需的製程控制步驟、工具內容與客戶支出占比
source_ids: S1,S2,S3
watch_source_ids: S4,S5,S6
frequency: quarterly
frequency_detail: KLA、Applied Materials 與 Onto Innovation 季報、法說及投資人材料
next_check: 2026-08-13
trigger: 至少兩條獨立來源或一份客戶端文件，以相同期間與清楚定義顯示每一產品世代或單位產能的製程控制步驟、工具量或支出占比增加
invalidation: 客戶端同口徑資料顯示連續兩個產品世代的製程控制步驟、工具量或單位產能支出持平／下降，或明確指出既有光學、抽樣或設計規則已吸收新增複雜度
retired_at: 2026-08-12
retirement_reason: S8 新增供應商較寬事業組合的收入訊號，但未命中同口徑工具量／支出占比 trigger；C4 已由 C9 的工程—資格—量產陳述—較寬收入階梯取代，後續由 T5 分開追收入分子與客戶分母，不把相鄰商業訊號誤記成 wallet-share 證實
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C5
metric: inspection／metrology 從資格認證到高量產的客戶廣度、缺陷攔截與良率學習結果
source_ids: S2,S3
watch_source_ids: S5,S6
frequency: event_driven
frequency_detail: 新產品 qualification、production adoption、客戶技術論文或量產公告出現時重查
next_check: 2026-08-31
trigger: 不同客戶或供應商揭露由 qualification 進入高量產，並提供缺陷攔截、良率改善、重複採購或部署範圍
invalidation: 客戶或供應商明確揭露 qualification 撤回、量產未採用，或既有光學／抽樣方案已足以處理新增複雜度；只有未見第二客戶時維持 C5 待驗證，不視為反證
-->

<!-- monitoring_item
monitor_id: T3
status: retired
claim_ids: C6
metric: 台灣 semiequip／material／pcb／packtest 的具名產品、客戶資格、訂單與財務貢獻
source_ids: S1,S2,S3
watch_source_ids: S7
frequency: quarterly
frequency_detail: 公開資訊觀測站重大訊息、法說簡報與季度財報發布後逐公司核對
next_check: 2026-08-14
trigger: 公司一手文件首次把量測、檢查或良率學習產品連到 HBM／2.5D／3D 客戶階段，並提供可辨識訂單、收入或毛利資訊
invalidation: 公司明確否認相關產品／客戶曝險、退出該市場，或可定位的採購與供應商資料直接顯示相關資本支出由非 universe 公司取得；到期未見揭露只維持 C6 待驗證
retired_at: 2026-08-14
retirement_reason: C22 把商業證據拆成 actual、order、forecast 與同期間分母後，T3 原本只要求「可辨識訂單、收入或毛利」的觸發過寬，容易把跨期訂單或較寬部門收入誤記成台灣公司題材貢獻；由 T10 以產品—客戶階段—會計狀態—同期間分母四段橋接接續，這是新證據驅動的 monitor 規格修正，不表示 C6 已取得支持或反證
-->

<!-- monitoring_item
monitor_id: T4
status: retired
retired_at: 2026-08-12
retirement_reason: 本輪已完成 KLA 現行文件重查且沒有可重建分解；下一個公司結果時鐘由 T6 接續
claim_ids: C7
metric: KLA FY26Q4 同期間成長中，單位出貨、ASP、市占、產品組合、服務與產業類別支出的可重建貢獻
source_ids: S1
watch_source_ids: S4
frequency: quarterly
frequency_detail: KLA 季報、法說、股東信與分部附註發布後重做 growth bridge
next_check: 2026-08-13
trigger: 公司或可定位的獨立資料分解至少 80% 的同期間成長，且顯示超過 50% 來自同口徑工具量或客戶類別支出增加
invalidation: 可重建分解顯示超過 50% 的同期間成長來自市占、ASP、產品組合或服務，而非同口徑工具量或客戶類別支出增加
-->

<!-- monitoring_item
monitor_id: T5
status: retired
claim_ids: C5,C8,C9
metric: advanced-packaging process control 從工程需求、資格、高量產陳述到題材收入分子及客戶支出分母的逐層橋接
source_ids: S1,S2,S3,S8,S16,S17,S18,S19
watch_source_ids: S4,S5,S6
frequency: quarterly
frequency_detail: Applied Materials 2026-08-13 結果後先重查；其後按 KLA、Applied Materials、Onto Innovation 季報／法說與客戶端製造文件更新
next_check: 2026-08-14
trigger: 至少兩條獨立公司鏈或一份客戶端文件，以同期間揭露 advanced-packaging process-control 的產品／類別收入、工具數、重複採購或每單位產能支出，且能把題材分子對回公司或客戶分母
invalidation: 客戶端或同口徑供應商資料顯示新增複雜度主要由既有工具、抽樣、軟體或設計規則吸收，連續兩個產品世代的工具量／單位產能支出持平或下降；只有較寬事業組合新高而無分子時不視為 trigger 命中
retired_at: 2026-08-14
retirement_reason: Camtek 新增一條具名工具訂單與近似 AP／公司收入組合鏈，Nova 另新增產品線銷售訊號，但 Camtek 約 75% 未標期間、Nova／Onto 無題材金額，仍未完整命中兩條獨立同期間分子—分母 trigger；C9 已由 C22 取代，後續由 T9 把 actual、order 與 forecast 分開續追
-->

<!-- monitoring_item
monitor_id: T6
status: active
claim_ids: C7
metric: KLA FY26Q4 同期間成長中，單位出貨、ASP、市占、產品組合、服務與產業類別支出的可重建貢獻
source_ids: S1
watch_source_ids: S4
frequency: quarterly
frequency_detail: KLA 季報、法說、股東信與分部附註發布後重做 growth bridge
next_check: 2026-10-28
trigger: 公司或可定位的獨立資料分解至少 80% 的同期間成長，且顯示超過 50% 來自同口徑工具量或客戶類別支出增加
invalidation: 可重建分解顯示超過 50% 的同期間成長來自市占、ASP、產品組合或服務，而非同口徑工具量或客戶類別支出增加
-->

<!-- monitoring_item
monitor_id: T7
status: active
claim_ids: C11,C12,C13,C14
metric: 同一 production product／layer 的 control plan 是否同時公開抽樣覆蓋、靈敏度／逃逸、偽警報／分類、結果時間／圍堵及製造結果
source_ids: S10,S11,S12
watch_source_ids: S5,S13
frequency: event_driven
frequency_detail: 客戶技術論文、NIST／SEMI 方法文件或設備商公開版本化 control-plan evidence 時重查
next_check: 2026-08-31
trigger: 至少一份客戶端或可重建中立資料，以同一產品與製程層公開 sampling unit／coverage、sensitivity／escape、FAR／classification、time-to-result／containment，以及良率、重工或報廢結果
invalidation: 量產客戶同口徑資料顯示新增 3D／advanced-packaging 複雜度可由原 control plan 吸收，且 coverage、escape、FAR、cycle time 與製造結果沒有惡化；單一供應商速度或解析度數字不算推翻或命中
-->

<!-- monitoring_item
monitor_id: T8
status: active
claim_ids: C15,C16,C17
metric: 同一 production product／layer 的 measurement-system contract 是否同時公開被測量、方法環境、參考校正鏈、偏差解析度線性、重複性再現性穩定性、不確定度決策規則及實際 control-plan 用途
source_ids: S14,S15
watch_source_ids: S13
frequency: event_driven
frequency_detail: 客戶製造文件、NIST／SEMI 方法成果或版本化量測系統資格報告公開時重查
next_check: 2026-08-31
trigger: 至少一份客戶端或可重建中立資料，對同一產品與製程層公開 measurand／unit、method／configuration／environment、reference／calibration chain、bias／resolution／linearity、repeatability／reproducibility／stability、uncertainty／decision rule，並接到放行、隔離、調參或重工及製造結果
invalidation: 量產客戶以另一套可稽核且可重現的 measurement-assurance scheme 證明能在省略上述一個或多個欄位時維持同等 decision risk 與製造結果；只有沒有公開完整紀錄時維持 C17 閱讀框架，不視為反證
-->

<!-- monitoring_item
monitor_id: T9
status: active
claim_ids: C5,C18,C19,C20,C21,C22
metric: advanced-packaging process-control 的 actual revenue、order intake 與 forecast 是否各自取得同期間題材分子及公司或客戶分母
source_ids: S1,S2,S3,S8,S16,S17,S18,S19
watch_source_ids: S4,S5,S6
frequency: event_driven
frequency_detail: 先重查台灣時間 2026-08-14 發布的 Applied Materials FY26Q3 結果；其後按 Camtek、Nova、KLA、Applied Materials、Onto Innovation 季報／法說與客戶製造文件更新
next_check: 2026-08-15
trigger: 至少兩條獨立公司鏈各以同一期間公開具名 advanced-packaging process-control 產品／類別的 actual revenue 或 order intake 及公司分母，並把 actual、order、forecast 分開；或一份客戶文件公開每單位產能支出與工具／控制步驟
invalidation: 客戶端或同口徑供應商資料顯示新增複雜度主要由既有工具、抽樣、軟體或設計規則吸收，連續兩個產品世代的工具量或單位產能支出持平／下降；單一公司的未標期間占比、跨期訂單或無金額 record 不算命中或推翻
-->

<!-- monitoring_item
monitor_id: T10
status: active
claim_ids: C6,C22
metric: 台灣 semiequip／material／pcb／packtest 的具名產品、HBM／2.5D／3D 客戶階段、actual／order／forecast 狀態與同期間財務分母
source_ids: S1,S2,S3,S8,S16,S17,S18,S19
watch_source_ids: S7
frequency: quarterly
frequency_detail: 公開資訊觀測站重大訊息、法說簡報與季度財報發布後，按產品—客戶階段—會計狀態—同期間分母逐公司核對
next_check: 2026-08-21
trigger: 台灣公司一手文件首次把具名量測、檢查或良率學習產品連到 HBM／2.5D／3D 客戶階段，並提供同期間可辨識的 actual revenue、order intake 或毛利分子及公司／部門分母；actual、order、forecast 必須分開
invalidation: 公司明確否認相關產品／客戶曝險、退出該市場，或客戶採購與供應商資料直接顯示相關資本支出由非 universe 公司取得；只有到期未揭露、較寬部門收入、跨期訂單或產品名稱時維持 C6 待驗證
-->

## 下一個可證明／否定的節點

- Applied FY26Q3 公告與簡報仍未提供 AP-specific PDC 分子；下一步核對官方 earnings script、後續 10-Q／IR 是否出現同期間 actual revenue、order intake、工具量或部署口徑，只有公司／部門總額與兩個廣義集合成長率仍不算。
- Camtek 能否把約 75% AP 收入組合補上量測期間，並把具名 Hawk 訂單接到實際交付、收入與公司分母；Nova 能否拆出 AP／Sentronics 金額或占比。
- KLA 能否分解單位出貨、ASP、產品組合、服務與市占；否則 C7 維持待驗證。
- Onto 能否把較寬事業組合新高拆到 HBM／2.5D、具名工具、客戶數、重複採購或收入分子；「record」沒有金額仍不和 Nova 排名。
- 客戶或中立研究能否在同一產品／layer 公開 control plan 六欄與結果；若只有速度、解析度或 AI 分類功能，C14 仍只是閱讀框架。
- 同一產品／layer 能否先公開量測系統六欄，再把結果接到 control-plan 決策與良率、重工、報廢或週期時間；只有校正標籤或工具規格，C17 不升級。
- 弘塑能否把集團代理檢查／量測能力拆成具名產品收入；均華能否把 AOI／1 µm 量測計畫接到 qualification、簽收與機種收入；萬潤能否把檢查／量測或 CPO 閉環功能接到具名客戶、量產驗收與同期間分母。
- 台灣公司若沒有產品、客戶階段與財務貢獻，C6 不升級，`stock_ids` 留空。

到期時若沒有被 active thesis claim 引用的新證據，只在 append-only scan log 記錄重查結果，
不更新 `last_reviewed_at`、不延後 `review_due`，也不提高 `base_confidence`。
