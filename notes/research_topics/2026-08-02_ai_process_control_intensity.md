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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **製程控制**：在製造途中用量測、檢查與缺陷分析找出偏差，再把結果回饋到製程調整；它不同於封裝完成後才判定成品良否的成品最終測試（ATE final test）。
- **HBM**：把多層記憶體垂直堆疊的高頻寬記憶體；堆疊越複雜，晚發現缺陷的代價越高。
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
- **抽樣（sampling）**：只檢查部分晶圓、區域或製程批次，以速度換取資訊；抽樣較少不代表沒有風險，檢查較多也不保證能找到正確根因。
- **Control plan（製程控制計畫）**：先定義要攔截的失效、在哪一道工序看、抽樣多少、看多細、多久得到結果，以及異常發生後要採取什麼動作的製造規則。
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

### 三句話抓重點

- 五家設備商的一手文件，分別說明需求方向、缺陷為何更昂貴、設備走到客戶驗證／未來交付的哪一步，以及不同寬度的訂單與收入訊號。
- 真正要查的是：每一代產品的 control plan 是否改變抽樣覆蓋、靈敏度、偽警報、週期時間與圍堵動作，而不只是設備名稱變多。
- Camtek 已提供較接近題材分子—公司分母的近似收入組合，但期間未標明；Nova 與 Onto 仍只到較寬類別新高，現有資料不能證明全產業設備預算占比上升或台灣公司訂單。

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
- 追公開資訊觀測站是否出現台灣公司的具名產品、客戶階段與財務貢獻。

### 想一想

- 若成長主要來自市占、漲價、產品組合或服務，主命題應如何縮小？
- 一套工具通過一名客戶認證，還缺哪些證據才能推論成產業錢包占比上升？
- 如果靈敏度提高卻同時產生大量偽警報、拖長複判時間，這份 control plan 一定更好嗎？
- 如果同一個標準樣品每次都量得很接近、卻全部偏離參考值，這套系統是精密、準確，還是兩者兼具？
- 設備貼著校正標籤，是否就能證明今天這個產品、這個方法與這次結果都可追溯且適合拿來判定放行？
- 若公司只說「先進封裝事業創新高」，卻沒有產品分子與公司分母，你能安全地推論到哪一層？

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

## 為何值得進佇列

KLA 提供需求方向，Applied Materials 說明缺陷機制與自述的高量產使用，Onto Innovation
先提供 2.5D logic／HBM 客戶資格節點，再新增較寬事業組合的收入訊號；Camtek 把具名 Hawk
訂單、交付年度、公司總營收與近似 AP 收入組合分開，Nova 則補上另一條具名量測產品線的
銷售訊號。SEMI 議程把控制問題落到 TSV、填孔、沉積、翹曲、RDL、切割與相鄰的 CPO
整合。這些資料讓工程與供應商商業成熟度比單一廠商說法更完整。NIST、Applied 與 KLA 的方法／產品文件又把 control plan
拆成動態抽樣、靈敏度、覆蓋、偽警報、結果時間與不同製程任務；NIST／SEMATECH 的量測
章節再補上 bias、repeatability、reproducibility、stability、uncertainty 與 traceability 的前置
契約。本題也不同於 ATE tester TAM：它研究製程中的量測、
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
| 採用節點 | Onto 披露 2.5D logic 與 HBM 客戶資格認證 | 大量採購、收入或台灣參與 |
| 供應商端量產陳述 | Applied 稱特定 eBeam defect-analysis 系統已用於高量產先進封裝 | 客戶端部署數、良率實績或市占 |
| 具名工具未來訂單 | Camtek 披露 tier-1 OSAT 與 HBM player 合計超過 1.05 億美元的 multi-system orders，其中 HBM 訂單全為 Hawk，預計 2027 交付 | 已認列收入、工具台數、客戶名稱、毛利或客戶產能分母 |
| 較寬收入組合 | Camtek 簡報把約 55% HPC／AI 與 20% non-AI AP 合計標為約 75% 公司收入 | 期間未標，不能乘上單季公司營收或拆成 HBM-only 金額 |
| 較寬收入訊號 | Onto 稱 Specialty Devices and Advanced Packaging 收入創高，支撐含 2.5D／HBM | 類別金額、題材分子、特定工具收入或全產業支出 |
| 具名產品線銷售訊號 | Nova 稱 Sentronics advanced-packaging dimensional-metrology solutions 是創高產品線之一 | 產品線金額／占比、HBM 分解、工具數或跨公司 record 排名 |

## 跨公司數字與可比性

本篇 `cross_company_numbers: true`，但只有 `M1` 的兩筆公司總營收符合直接比較條件：Camtek
與 Nova 都是截至 2026 年 6 月 30 日的三個月、GAAP 公司總營收，幣別與單位也相同。這只
能比較公司總營收數值，不能比較 advanced-packaging 強度；Camtek 的近似 75% 未標期間，
Nova 與 Onto 沒有 AP 金額，因此不建立跨公司的 AP 占比、訂單、工具數、市占或排名。

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
- 後續入口：[KLA](https://ir.kla.com/financial-information/financial-results)、[Applied](https://ir.appliedmaterials.com/news-releases/)、[Onto](https://investors.ontoinnovation.com/news/default.aspx)、[MOPS](https://mops.twse.com.tw/mops/web/index)。
- 中立方法入口：[NIST CHIPS Metrology Program](https://www.nist.gov/chips/research-development-programs/metrology-program)。

五家設備商彼此獨立但都有商業動機，其中 Camtek 三份文件只算一條公司消息鏈；SEMI 議程保存多位講者摘要，也不能替代完整簡報、
客戶端或全產業資本支出證據。本輪沒有一致預期、估值、即時持倉或台灣公司客戶資料，
因此不談市場是否反映或個股方向。

## 反方與替代路徑

- **供應商特有效果**：KLA 成長可能來自市占、ASP、產品組合或服務，而非類別支出增加。
- **資格不等於規模**：Onto 的 qualification 可能停在單一工具或客戶，未形成跨客戶量產。
- **較寬收入組合混合**：Onto 的新高可能由 silicon photonics、其他 specialty devices、產品組合或價格帶動，不能全歸因 HBM／2.5D 製程控制。
- **訂單不等於營收**：Camtek 的具名訂單預計 2027 交付，可能受交期、驗收與會計認列影響；不能拿它除以 2026Q2 公司營收製造跨期 book-to-bill。
- **占比集合重疊**：Camtek 的 AP、HPC／AI 與 Eagle G5／Hawk 不是互斥分類，且近似 AP 圖未標期間；不能相加或套用到單季分母。
- **公司分母不等於題材分子**：Nova 公司總營收可以和 Camtek 的公司總營收對齊，卻不能在 Nova 未拆 AP 金額時用來比較 AP 強度。
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

- Applied Materials 台灣時間 8 月 14 日發布的 FY26Q3 結果是否提供 advanced-packaging process control 的收入、訂單、工具量或部署口徑；只有公司總額不算。
- Camtek 能否把約 75% AP 收入組合補上量測期間，並把具名 Hawk 訂單接到實際交付、收入與公司分母；Nova 能否拆出 AP／Sentronics 金額或占比。
- KLA 能否分解單位出貨、ASP、產品組合、服務與市占；否則 C7 維持待驗證。
- Onto 能否把較寬事業組合新高拆到 HBM／2.5D、具名工具、客戶數、重複採購或收入分子；「record」沒有金額仍不和 Nova 排名。
- 客戶或中立研究能否在同一產品／layer 公開 control plan 六欄與結果；若只有速度、解析度或 AI 分類功能，C14 仍只是閱讀框架。
- 同一產品／layer 能否先公開量測系統六欄，再把結果接到 control-plan 決策與良率、重工、報廢或週期時間；只有校正標籤或工具規格，C17 不升級。
- 台灣公司若沒有產品、客戶階段與財務貢獻，C6 不升級，`stock_ids` 留空。

到期時若沒有被 active thesis claim 引用的新證據，只在 append-only scan log 記錄重查結果，
不更新 `last_reviewed_at`、不延後 `review_due`，也不提高 `base_confidence`。
