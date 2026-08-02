# Panel-level packaging 的成本題：面積利用率只是起點，good-package yield 才是終點

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

## 新手先讀：這篇在講什麼

### 名詞小字典

- **Panel-level packaging（PLP）**：用方形或長方形大面板處理封裝，而不是在圓形晶圓上排版。
- **面積利用率**：原始載體有多少面積真的能排進產品；方形面板的幾何損失通常較少，但這不是最終良率。
- **Good-package yield**：投入製程後最後能通過電性、可靠度與尺寸要求的合格封裝比例，才真正影響每顆成本。
- **Uniformity**：面板中央與邊緣的沉積、蝕刻、清洗、線寬或厚度是否一致。
- **Throughput**：設備在單位時間能完成多少面板；面板較大不代表每小時一定做出更多合格產品。

### 三句話抓重點

- 方形面板確實提供較好的幾何利用率，設備商也已建立 panel R&D、pilot 與 early qualification 能力。
- 但 Lam 自己同時列出 uniformity、yield、throughput、automation 與 panel-size standards 等量產難題，Applied 的 NEXX 交易在公告時也仍待完成。
- 所以研究重點應是每個合格大型封裝的總成本，而不是看到面板面積更大就直接推導台灣供應鏈量產受惠。

### 為什麼重要

AI 封裝把 GPU、HBM 與 I/O chiplet 放在更大的基板上，圓形晶圓邊緣的排版損失會變得更顯眼。
然而面板越大，翹曲、邊緣控制、均勻度與自動搬運也越難；若報廢一片，損失的產品數可能更高。
因此 PLP 是「可能改善成本結構的製造路徑」，不是單靠幾何就成立的成本答案。

### 接下來怎麼追

- 每次看到 panel 新聞，先標記是 R&D、pilot、early qualification、HVM readiness 還是真正 HVM。
- 要求同時披露 panel 長寬／厚度、可排產品數、good-package yield、cycle time、設備利用率與可靠度。
- 公司映射要對上具名客戶、料號或工具、qualification 與財務，不把一般先進封裝能力當作 PLP 訂單。

### 想一想

- 面板一次能排更多封裝，但若良率較低、cycle time 較長，每顆合格品成本一定會更低嗎？
- 510x515mm 只是某家設備商的能力描述，還是供應鏈已共同採用的標準尺寸？
- 一座 pilot line 距離客戶 HVM，還缺哪些材料、設備、自動化、測試與可靠度證據？

## 從幾何利用率走到單位經濟

可以把每顆合格封裝成本想成：

`面板與材料 + 設備折舊 + 製程時間 + 報廢損失 ÷ 最終合格封裝數`

面積利用率只改善分子與理論可排數的一部分；uniformity、翹曲、edge control、yield 與 throughput
會共同決定分母。沒有這些欄位，就只能說 PLP 有幾何潛力，不能說已具經濟優勢。

| 證據層級 | 本輪看見什麼 | 還不能知道什麼 |
|---|---|---|
| R&D／pilot | Lam Salzburg 有 panel wet-process R&D、pilot、engineering testing 與 early qualification | 客戶 HVM、good-package yield、產能與收入 |
| 製造問題 | Lam 明列 uniformity、yield、throughput、automation 與 standards | 問題已被解決的程度與客戶線成本 |
| 設備布局 | Applied 簽約收購 NEXX、補 panel ECD；自身已有 PVD／CVD／etch／lithography 等布局 | 交易完成、整合效果、客戶採用、份額與財務回報 |

## 為什麼不能把 panel size 當成進度分數

不同公司可能展示不同長寬、厚度、材料與用途的面板。尺寸更大會提高理論面積，卻也可能增加翹曲、
均勻度與搬運難度；若沒有同一產品、同一製程與同一良率定義，就不能把 300mm wafer、510x515mm
panel 或其他 panel form factor 排成單一優劣名次。本篇因此不建立跨公司數字比較帳本。

## 來源與證據邊界

- [Lam：Panel-Level Packaging Center of Excellence](https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE)
- [Lam：From Wafer to Panel](https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing)
- [Applied Materials：pending NEXX acquisition and panel-level ECD](https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-broadens-advanced-packaging-portfolio)

Lam 與 Applied Materials 都是設備商，對產業採用、產品優勢與 HVM readiness 有商業立場。本篇只把
它們直接揭露的 facility、製程問題與交易狀態標成 verified；「PLP 將更便宜」與「台灣公司已受惠」
均未被當成事實。

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
- 具名 AI package 或 OSAT 公布 panel form factor、qualification、good-package yield、throughput 與可靠度。
- 設備、材料與基板公司對同一客戶 panel 流程完成雙向核對，並出現量產及財務資料。
- 若 panel standard 長期分裂、pilot 無法進 HVM 或單位良率成本不優於 wafer，PLP 的優先級應下修。
