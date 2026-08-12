# 高頻寬記憶體可以客製到哪裡：先分規格、底部晶片與工作搬移

<!-- research_topic
topic_id: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-03
source_published_at: 2026-02-12
last_reviewed_at: 2026-08-03
review_due: 2026-09-15
source_type: mixed
publisher: Samsung Electronics
publisher_domain: news.samsung.com
canonical_url: https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing
source_chain_id: custom-hbm-scope-ladder-20260803
stock_ids:
group_ids: memory,packtest,ipdesign
trigger_type: memory_architecture_and_customer_customization
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C5
base_confidence: medium
confidence_basis: Samsung、SK hynix 與 Micron 三條獨立一手來源可確認各自揭露的客製範圍與階段，但用語、產品世代、客戶、qualification、NRE、量產與財務口徑不同，因此只能建立分層框架，不能做供應商領先排名
cross_company_numbers: false
-->

<!-- transition
date: 2026-08-03
from: initial
to: inbox
reason: frozen_candidate_selected_for_scope_disambiguation
evidence: source_chain:custom-hbm-scope-ladder-20260803
-->
<!-- transition
date: 2026-08-03
from: inbox
to: triaged
reason: separated_customization_object_sampling_qualification_and_production
evidence: sources:S1,S2,S3,S4,S5
-->

<!-- research_source
source_id: S1
role: company_release
source_kind: document
publisher: Samsung Electronics
title: Samsung Ships Industry-First Commercial HBM4 With Ultimate Performance for AI Computing
published_at: 2026-02-12
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing
locator: Comprehensive Yet Agile Production Capabilities 最後一段；HBM4E 樣品與 custom HBM 2027 客戶樣品時程
limitation: Samsung 自述的 roadmap 與商業主張不證明 2027 樣品一定如期、具名客戶資格、量產或相對競爭位置
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S2
role: company_release
source_kind: document
publisher: Samsung Electronics
title: 삼성전자 세계 최초 업계 최고 성능의 HBM4 양산 출하
published_at: 2026-02-12
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EC%84%B8%EA%B3%84-%EC%B5%9C%EC%B4%88-%EC%97%85%EA%B3%84-%EC%B5%9C%EA%B3%A0-%EC%84%B1%EB%8A%A5%EC%9D%98-hbm4-%EC%96%91%EC%82%B0-%EC%B6%9C%ED%95%98
locator: 2026년 HBM4E·2027년 Custom HBM 샘플 출하로 차세대 라인업 가동；腳註定義容量、速度、電力特性與介面依客戶架構客製
limitation: 與 S1 同一公司消息鏈，只補足韓文官方頁的定義；不能當作第二條獨立驗證，也沒有具名客戶或資格結果
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S3
role: competitor_primary
source_kind: document
publisher: SK hynix
title: SOD's Review GTC 2026 From Models to Infrastructure
published_at: 2026-03-27
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.skhynix.com/gtc-2026-review/
locator: cHBM 展示段落；Stream DQ Architecture 位於 base die，將部分 preprocessing 從 GPU 移到 base die
limitation: 公司展場回顧與自有架構效能宣稱不是共同 benchmark、客戶 qualification、量產或財務貢獻
independence_group: sk-hynix
-->

<!-- research_source
source_id: S4
role: competitor_primary
source_kind: document
publisher: Micron
title: Micron Fiscal Q4 2025 Earnings Slides
published_at: 2025-09-23
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02
locator: p.13 Data center HBM4E；standard 與 customized base logic die、TSMC 製造分工及毛利預期
limitation: 管理層揭露的是 HBM4E 選項與預期；未提供客戶名稱、NRE、qualification、量產數量或已實現毛利
independence_group: micron
-->

<!-- research_source
source_id: S5
role: company_release
source_kind: document
publisher: Samsung Electronics
title: Samsung Electronics Begins Shipment of Industry-First HBM4E Samples
published_at: 2026-05-29
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/samsung-electronics-begins-shipment-of-industry-first-hbm4e-samples
locator: 標題、產品配置與量產段落；12-layer HBM4E 樣品已出貨，使用 Samsung Foundry 4nm logic base die，量產仍依客戶時程
limitation: 這是標準 HBM4E 樣品的公司公告，不能替代 2027 custom HBM 樣品、具名客戶 qualification 或量產證據
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Samsung Electronics
title: Samsung Global Newsroom HBM4 Index
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.samsung.com/global/tag/hbm4
locator: 2026-08-03 查得 HBM4、HBM4E、合作與後續 custom HBM 文件入口
limitation: 動態標籤頁只供未來重查；新標題不能替代附件內容或刷新證據時鐘
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S7
role: competitor_primary
source_kind: living_index
publisher: SK hynix
title: SK hynix Press Center
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://news.skhynix.com/press-center/press-release/
locator: 2026-08-03 查得 cHBM、HBM4E、樣品與量產後續入口
limitation: 新聞索引只供監測，不能證明 Stream DQ 已取得客戶資格、量產或財務貢獻
independence_group: sk-hynix
-->

<!-- research_source
source_id: S8
role: competitor_primary
source_kind: living_index
publisher: Micron
title: Micron News Releases
published_at:
captured_at: 2026-08-03
accepted_at: 2026-08-03
status: active
url: https://investors.micron.com/news-releases
locator: 2026-08-03 查得 HBM4E custom base logic die、樣品、qualification 與量產後續入口
limitation: IR 索引只供找到新附件；不能把管理層重複說法視為獨立新證據
independence_group: micron
-->

<!-- research_source
source_id: S9
role: company_release
source_kind: living_index
publisher: Samsung Semiconductor
title: Memory Labs — DRAM Design Lab and AGI Computing Lab
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://semiconductor.samsung.com/about-us/locations/us-rnd-labs/memory-labs/
locator: DRAM Design Lab 的 HBM、MID、ESS、ACD teams，以及 AGI Computing Lab 的 System Technology／Architecture groups；逐項列出 HBM4E architecture／IP、Custom HBM I/O architecture／circuit／IP、firmware、base die、technical customer engagement、workload modeling 與 system software
limitation: 這是會變動的公司研發組織與招募說明，只能證明公司公開描述的工作分解；不證明任一實際專案按同一流程執行、外部供應商分工、客戶 qualification、量產或財務貢獻
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S10
role: company_release
source_kind: living_index
publisher: Samsung Foundry
title: Application Specific Service — HPC and AI
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://semiconductor.samsung.com/foundry/application-specific-service/hpc-ai/
locator: Logic and memory integration 段落；把 die-to-die interface、base-die controller、additional logic、bandwidth／capacity、power／latency 與 application customization 放在同一供應商架構圖
limitation: 動態應用服務頁與供應商效益主張不是產業共同標準、獨立 benchmark、具名 customer design、完整 PPA／thermal sign-off、qualification 或 production result
independence_group: samsung-electronics
-->

<!-- research_source
source_id: S11
role: other_primary
source_kind: document
publisher: Taiwan Semiconductor Manufacturing Company
title: A Shared Commitment to Energy-Efficient AI
published_at: 2025-11-07
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.tsmc.com/english/node/233
locator: OIP Forum 回顧的 memory capacity／bandwidth／latency 段落；明列 HBM4 logic base die 使用 N12、custom HBM4E design 使用 N3P
limitation: 台積電 OIP 生態系文章只支持兩種設計路徑所述製程節點，不提供具名記憶體供應商或客戶、tape-out／qualification、wafer volume、yield、pricing 或財務歸因
independence_group: tsmc-oip
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: living_index
publisher: Samsung Semiconductor
title: Samsung Showcases Next-Generation AI Semiconductor Innovations at COMPUTEX 2026
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://semiconductor.samsung.com/kr/news-events/tech-blog/samsung-showcases-next-generation-ai-semiconductor-innovations-at-computex-2026/
locator: COMPUTEX 2026 HBM4E／HPB 段落；說明 base die 內 D2D PHY 是主要發熱區、HPB 提供獨立 thermal path，並標示 HBM4E validation 與未來 HBM5 adoption 的不同階段
limitation: 公司展會技術回顧與前瞻規劃只支持特定 HBM4E／HPB 的熱邊界；它不是 custom HBM 的共同要求、客戶 pass result、量產採用或供應鏈財務證據
independence_group: samsung-electronics
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Samsung 於 2026-02-12 表示 custom HBM 樣品預計自 2027 年開始送達客戶；同一份英文公告把 HBM4E 的 2026 下半年樣品時程與 custom HBM 的 2027 時程分開
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-02-12
basis: S1 最後一段直接列出兩個不同產品與樣品時鐘
boundary: 這是公司前瞻時程，不是 2027 樣品已交付、客戶已完成 qualification 或產品已量產
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
claim: Samsung 的韓文官方定義把 custom HBM 描述為依客戶 AI accelerator 或 GPU 架構調整容量、速度、電力特性與介面，而不是只換一個容量 SKU
supporting_source_ids: S2
contrary_source_ids:
as_of: 2026-02-12
basis: S2 的 Custom HBM 腳註逐項列出客製欄位與客戶架構
boundary: 定義範圍不表示每一個客戶都會同時客製所有欄位，也不證明產品已完成設計或資格
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
claim: SK hynix 在 GTC 2026 展示的 cHBM 核心是實作於 base die 的 Stream DQ Architecture，並將部分 preprocessing 從 GPU 移到 base die
supporting_source_ids: S3
contrary_source_ids:
as_of: 2026-03-27
basis: S3 的 cHBM 展示段落直接說明架構位置與工作搬移方向
boundary: 展示與公司模擬不等於通用 custom HBM 定義、跨廠可比 benchmark、具名客戶資格或量產
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
claim: Micron 表示 HBM4E 會同時提供標準產品與客製 base logic die 選項，兩者的 base logic die 都由 TSMC 製造；公司預期客製版本毛利較高，但沒有表示該毛利已實現
supporting_source_ids: S4
contrary_source_ids:
as_of: 2025-09-23
basis: S4 p.13 逐項列出產品選項、TSMC 分工與 expect higher gross margins 的管理層預期
boundary: 這不證明具名客戶、qualification、NRE、量產數量、實際售價或已實現毛利，也不能與其他公司的客製層次直接排名
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
claim: 截至 2026-08-03，Custom HBM 應被研究成「客製對象 × 商用階段」矩陣，而不是單一供應商賽跑：Samsung 公開的是客戶規格範圍與 2027 樣品時鐘，SK hynix 展示的是 base-die 工作負載下放，Micron 揭露的是 HBM4E 客製 base logic die 與 foundry 分工；三者尚無共同產品定義、qualification 或量產分母
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-03
basis: S1／S2、S3、S4 分屬三個獨立公司消息鏈，揭露的客製對象與階段不同；S5 又證明 Samsung 已出貨的 HBM4E 樣品不能自動視為 2027 custom HBM 樣品
boundary: 不以公告日期、產品名稱、公司自述效能或毛利預期計算領先分數，不推估客戶份額、TAM、台灣供應商訂單或市場是否反映
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C6
label: unverified
status: active
claim: 三家公司公開的 custom HBM 已能用同一口徑比較客戶數、qualification、NRE、量產數量、售價、良率或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: 現有文件分別提供 roadmap、展示架構與管理層產品選項，沒有共同定義、具名客戶、測試條件、數量或已實現財務欄位
boundary: 不可把「都有 custom HBM」改寫為處在同一產品世代或同一商用階段
verification_needed: 至少兩家供應商及其客戶交叉揭露同一產品世代、客製欄位、sample／qualification／production 時點、數量與可核對財務口徑
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: unverified
status: active
claim: universe 內記憶體、IC 設計或封測公司已因 custom HBM 取得可辨識 design win、qualification、訂單、收入或毛利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-03
basis: Samsung、SK hynix 與 Micron 的文件沒有完成任何 universe 公司與客戶產品、資格及財務的雙向核對
boundary: HBM、base die、ASIC、TSV、bonding 或測試能力只形成搜尋路由，不是受惠事實
verification_needed: 平台／記憶體供應商與台灣公司端須同時揭露具名產品、客戶資格、量產出貨及可辨識財務貢獻
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Samsung Memory Labs 公開頁把 Custom HBM 相關研發拆到 I/O architecture／circuit／IP、firmware、base die 與 technical customer engagement，並另列 workload architecture、modeling、runtime prototype 與 system software；這些不是同一個工作項目
supporting_source_ids: S9
contrary_source_ids:
as_of: 2026-08-12
basis: S9 的 DRAM Design Lab 與 AGI Computing Lab team descriptions 逐項列出上述工作分工，可直接定位到不同團隊與輸出
boundary: 組織頁只能證明三星如何公開描述研發範圍，不證明每個 custom HBM 專案都採相同組織、責任已完整交接、任何外部供應商參與或產品已通過客戶驗證
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: verified
status: active
claim: Samsung Foundry 的 HPC／AI 應用頁把 custom HBM 的公開架構描述為使用 die-to-die interface、把 HBM controller 整合進 base die，並可在 base die 加入 accelerator、memory controller 或 CPU 等額外邏輯
supporting_source_ids: S10
contrary_source_ids:
as_of: 2026-08-12
basis: S10 Logic and memory integration 段落逐項列出 interface、controller placement 與 additional logic examples
boundary: 這是單一供應商的應用架構與效益主張，不是 JEDEC 共同定義，也不證明所有 custom HBM 都採相同 partition、效能數字可跨公司比較、具名客戶已 tape-out 或產品已量產
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: 台積電 2025 OIP Forum 回顧把 HBM4 logic base die 的 N12 路徑與 custom HBM4E design 的 N3P 路徑分開，顯示「底部邏輯晶片」名稱相同也不能假設製程節點與設計契約相同
supporting_source_ids: S11
contrary_source_ids:
as_of: 2025-11-07
basis: S11 直接並列 N12 for HBM4 logic base die 與 N3P for custom HBM4E designs
boundary: 製程路徑差異不證明具名客戶、記憶體供應商、tape-out、qualification、量產數量、良率、價格或台灣 IC 設計公司參與
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
claim: Samsung COMPUTEX 2026 技術頁把 HBM4E base die 內的 D2D PHY 定位為主要發熱區，並把 HPB thermal path 描述為仍在 HBM4E 驗證、預計未來 HBM5 採用，證明介面邏輯改動與熱路徑不能被視為兩個完全獨立的設計問題
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-08-12
basis: S12 明示 D2D PHY 的位置與發熱原因、HPB 的散熱用途，以及 validation 與 future adoption 兩個不同階段
boundary: 這只支持三星特定 HBM4E／HPB 技術邊界；不表示 HPB 是 custom HBM 必備項、驗證已通過、客戶會採用、封測供應商已取得資格或財務價值已形成
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C12
label: inference
status: active
claim: 研究一個具名 custom HBM 專案時，至少要把工作負載與功能、容量／速度／功耗／介面、base-die 邏輯與 IP、firmware／software、製程／封裝／熱，以及 sample／qualification／量產財務六份交接合約分開；任何一份成立都不能替另外五份背書
supporting_source_ids: S2,S3,S4,S5,S9,S10,S11,S12
contrary_source_ids:
as_of: 2026-08-12
basis: S2 定義客戶規格欄位，S3 定位 workload offload，S4／S11 定位 base-die 與 foundry 路徑，S9 分開 architecture／IP／firmware／customer engagement，S10 定位 controller／D2D partition，S12 定位熱耦合，S5 則證明 sample 與 production 時鐘必須另列；合併後形成六份不可互相替代的查核欄位
boundary: 六份合約是本文的研究閱讀框架，不是 JEDEC 標準、固定開發順序、供應商價值分配或成熟度分數；現有來源沒有同一具名客戶專案把六份文件、版本、sign-off 與財務全部公開接起
verification_needed: 記憶體供應商與具名客戶雙向公開同一產品世代的 workload target、介面版本、base-die／firmware build、製程封裝熱條件、change control、qualification pass criteria、量產與財務分母
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C3,C4,C5,C6
metric: custom HBM 客製欄位、實體樣品、具名客戶與 qualification 階段
source_ids: S1,S2,S3,S4,S5
watch_source_ids: S6,S7,S8
frequency: event_driven
frequency_detail: Samsung、SK hynix 或 Micron 發布 custom HBM 樣品、客戶設計或 qualification 文件時重審
next_check: 2026-09-15
trigger: 至少一家交付可定位的 custom HBM sample 並揭露客製對象、產品世代、接收方與 qualification 條件
invalidation: 2027 樣品時程延後、架構停留展示、客戶改採標準 HBM，或公開資料顯示客製成本與良率無法通過資格
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4,C6,C7
metric: NRE、量產、售價、良率、毛利與台灣供應鏈財務足跡
source_ids: S3,S4
watch_source_ids: S7,S8
frequency: quarterly
frequency_detail: 每季檢查供應商季報與法說；只有共同口徑與雙向公司證據才建立比較或公司線
next_check: 2026-09-23
trigger: 公司揭露已實現 custom HBM 收入／毛利或具名客戶 qualification，且能和產品範圍及量產時點對上
invalidation: 管理層只重複較高毛利或合作敘事，沒有 NRE、產品資格、量產與財務分母
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C6,C8,C9,C10,C11,C12
metric: 同一具名 custom HBM 專案的 workload、介面、base-die／IP、firmware／software、製程封裝熱、qualification／量產財務六份交接是否以版本與責任人閉合
source_ids: S2,S3,S4,S5,S9,S10,S11,S12
watch_source_ids: S6,S7,S8,S9,S10
frequency: event_driven
frequency_detail: 任一供應商或客戶公布 custom HBM design handoff、sample qualification、change control 或 production 文件時逐欄重審
next_check: 2026-09-15
trigger: 同一具名產品與客戶公開可對齊的 workload target、interface／base-die／firmware build、foundry／package／thermal condition、pass criteria、變更紀錄與量產結果
invalidation: 後續一手資料顯示部分欄位由共同標準完整固定、某些客製路徑不需要 firmware 或 workload offload，或責任分界與本文六欄不同，則重畫合約而不是保留固定六欄
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
reason: editorial_plain_language_wave2_no_conclusion_change
evidence: editorial:plain_language_wave2
-->
<!-- transition
date: 2026-08-10
from: triaged
to: triaged
reason: editorial_plain_language_wave90_custom_scope_and_progress_no_conclusion_change
evidence: editorial:plain_language_wave90_custom_scope_and_progress
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: added_workload_interface_base_die_firmware_manufacturing_and_qualification_handoff_contract_without_refreshing_thesis_clock
evidence: sources:S2,S3,S4,S5,S9,S10,S11,S12
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **高頻寬記憶體（HBM）**：把多層動態隨機存取記憶體垂直堆疊，放在運算晶片附近，用較寬的連接介面搬動大量資料。
- **動態隨機存取記憶體（DRAM）**：需要持續供電才能保存資料的工作記憶體；本文只把它當成高頻寬記憶體的堆疊材料，不據此推定供應商份額。
- **記憶體堆疊**：把多層記憶體晶粒垂直組合，底部再接控制資料流的邏輯晶片；形成堆疊不等於已通過客戶驗證。
- **人工智慧加速器（AI accelerator）**：為大量人工智慧運算設計的晶片；客製記憶體會依它的資料需求調整，但加速器名稱不代表記憶體已量產。
- **圖形運算晶片（GPU）**：擅長大量平行運算的晶片。本文用它說明原本執行資料整理工作的運算端，不代表所有人工智慧工作都只在這裡完成。
- **客戶架構**：客戶的運算晶片、資料路徑與系統配置。依客戶架構調整規格，不代表每個客戶會改相同欄位。
- **容量**：一顆產品能存放多少資料；容量變大不等於資料搬得更快，也不等於已完成客戶驗證。
- **資料傳輸速度／頻寬**：單位時間內可以搬動多少資料。公司自述的速度不能直接當成跨公司共同測試結果。
- **電力特性／耗電**：產品在指定工作條件下使用電力的方式；若工作條件不同，數字就不能直接比較。
- **介面**：記憶體與運算晶片交換資料的連接規則與訊號方式；改介面可能需要雙方共同設計。
- **堆疊底部邏輯晶片（logic base die）**：位在記憶體堆疊底部，負責介面、資料路徑與控制；能做多少額外運算要看實際設計。
- **客製高頻寬記憶體（Custom HBM）**：不是已有共同規格的單一產品。公開資料可能指調整產品規格、重做底部邏輯晶片，或把部分工作搬到記憶體附近。
- **工作負載**：一套系統實際要執行的資料與運算任務；不同工作負載的效能數字不能直接放在同一排行榜。
- **資料前處理（preprocessing）**：正式運算前先整理、轉換或篩選資料。把它移到記憶體旁是工作位置改變，不等於產品已量產。
- **架構展示**：公司公開說明設計如何運作或展示原型；仍須另外確認樣品、客戶驗證與量產。
- **客戶樣品（sample）**：供應商把可測試產品交給客戶；樣品規劃、樣品已交付與客戶驗證完成是三種不同狀態。
- **客戶資格認證（qualification）**：客戶依指定條件測試產品是否符合要求；完成認證仍需另查量產與採購。
- **量產（production）**：產品進入穩定製造與交付階段；量產不會自動揭示客戶數、供應份額或獲利。
- **財務認列／收入認列**：公司把已符合會計條件的交易列入財務報表；合作、送樣或量產規劃不能直接替代它。
- **產品世代**：同一類產品的版本與時間位置；不同世代即使名稱相近，也不能直接共用樣品或量產時程。
- **第四代強化版高頻寬記憶體（HBM4E）**：供應商對第四代產品後續強化版本使用的名稱；不同文件不必然採用相同客製範圍或時程。
- **底部晶片資料流架構（Stream DQ）**：SK 海力士展示的架構名稱，把部分資料前處理從圖形運算晶片移到底部邏輯晶片；展示不等於已送樣或量產。
- **特殊用途晶片（ASIC）**：為特定功能設計的晶片；本文只用它描述可能承擔客製邏輯的角色，不代表任何台灣公司已取得設計案。
- **晶圓代工（foundry）**：依晶片設計製造晶圓的分工角色；知道代工夥伴不等於知道客戶資格、量產數量或獲利。
- **產品時程規劃（roadmap）**：公司對未來產品與里程碑的安排；規劃日期不是已完成日期。
- **共同基準測試（benchmark）**：讓不同方案在相同工作、條件與量測方式下比較；各公司自測不能自動視為共同基準。
- **具名客戶**：公開資料能辨認出實際接收或採用產品的客戶；只有「正在合作」不一定達到這個條件。
- **一次性工程費（NRE）**：為特定客戶進行設計、驗證與開發所收取或投入的一次性費用；沒有金額與認列方式就不能比較。
- **良率**：投入生產後能符合規格的產品比例；客製程度較深不會自動證明良率較高或較低。
- **毛利**：收入扣除直接成本後留下的金額或比率；沒有相同產品與會計分母時不能跨公司排名。
- **預期毛利／已實現毛利**：前者是管理層對未來的看法，後者是已進入財務結果的數字；兩者不能互相替代。
- **共同分母**：比較時各家公司都用相同產品範圍、階段、期間、數量與計算方式；缺少共同分母就不產生單一名次。
- **輸入輸出架構（I/O architecture）**：規定資料、命令與狀態如何進出記憶體及底部邏輯；名稱相同不代表版本、通道與錯誤處理相同。
- **晶粒對晶粒實體介面（D2D PHY）**：讓底部邏輯晶片與運算晶片交換高速訊號的實體電路；速度提高也會改變耗電與發熱條件。
- **控制器**：接收請求、安排資料傳輸並處理狀態與錯誤的邏輯；把它移到底部晶片會改變設計、驗證與責任邊界。
- **韌體（firmware）**：貼近硬體運作、負責初始化、控制與錯誤處理的程式；晶片完成不等於韌體已能配合客戶系統。
- **設計凍結（design freeze）**：開發各方同意某一版規格與設計不再任意改動的節點；凍結一層不表示其他層也已凍結。
- **變更控制（change control）**：設計凍結後記錄誰改了什麼、影響哪些介面，以及哪些測試必須重跑的程序。
- **設計簽核（sign-off）**：負責方確認指定版本在既定條件下達標；模擬簽核、晶片簽核、封裝簽核與客戶驗收是不同結果。
- **熱路徑（thermal path）**：熱從發熱位置傳到封裝與冷卻系統的路線；功能放進底部晶片後，熱不會自動消失。
- **熱傳路徑塊（HPB）**：三星展示的獨立導熱結構，用來把底部晶片高速介面產生的熱向外傳；仍在驗證不等於已量產採用。
- **N12／N3P 製程節點**：台積電兩種邏輯製程名稱；本文只用來說明一般 HBM4 與客製 HBM4E 的底部晶片路徑可能不同，不比較製程優劣。
- **Memory Labs（記憶體實驗室）**：三星官方頁對多個研發團隊的合稱；組織頁列出能力範圍，不代表一個具名產品已完成所有工作。

### 三句話抓重點

- 同樣寫「客製」，公開資料可能在談三種不同改法：只調整記憶體規格、重新設計堆疊底部的控制晶片，或把原本由運算晶片處理的部分資料整理工作搬到記憶體旁。
- 三星、SK 海力士與美光目前公開的也不是同一種進度：一家提出 2027 年客戶樣品規劃，一家展示架構，另一家說明產品選項、製造分工與較高毛利預期。
- 所以要把「改了哪裡」和「走到哪一步」分成兩把尺；只有產品世代、客製範圍、樣品、客戶驗證與量產都對齊，才適合比較。

### 為什麼重要

讀到「客製」、「樣品」或「量產」很容易以為三家公司正在跑同一場比賽。實際上，一家公司
可能只公開規格調整與未來樣品時程，另一家公司展示把資料整理工作移到底部晶片，第三家公司
則說明客製晶片的製造分工與預期毛利。公告早、產品名稱新或效能數字大，都不能單獨代表領先。

第一把尺問「改了哪裡」：產品規格、堆疊底部邏輯，還是工作位置。第二把尺問「走到哪一步」：
設計或展示、樣品規劃、樣品交付、客戶驗證、量產，還是已認列收入。兩把尺沒有一起對齊，
就不適合排成一條進度名次。

拆開後才能再問價值落在哪個角色：記憶體製造、邏輯設計、晶圓代工、封裝測試或客戶軟體。
也要避免把一般版本已送樣或已量產的時程，直接套到仍停留在規劃或展示的客製版本。

### 接下來怎麼追

- 先替每家公司填「改了哪裡」：產品規格、底部邏輯晶片，或資料整理工作的執行位置。
- 再填「走到哪一步」：設計或展示、樣品規劃、樣品交付、客戶驗證、量產或財務認列。
- 只有客戶與供應商雙方都能對上產品世代、測試條件與時點，才把客戶驗證標成完成。
- 談較高毛利時，先分管理層預期與已實現結果；沒有一次性工程費、售價、良率或毛利分母就不比較。

### 想一想

- 一家只重做堆疊底部的邏輯晶片，另一家還把資料整理工作搬進去，能用同一條進度排名嗎？先要對齊哪兩把尺？
- 客製提高單位價值時，額外設計費、驗證時間、良率與單一客戶風險可能如何變化？各要什麼證據？
- 一般版本的樣品已出貨，為什麼不能直接證明客製版本也已送樣？

## 先拆「改了哪裡」，再看「走到哪一步」

以下三種只是本文整理公開說法的讀法，不是產業共同標準，也不是由淺到深的技術或價值排名。

### 先用三種範圍讀懂「客製」

| 本文讀法 | 改了什麼 | 可能需要哪些角色一起做 | 本輪可能增加的功能 | 還不能因此判定 |
|---|---|---|---|---|
| 調整記憶體規格 | 依客戶架構改容量、資料傳輸速度、耗電或介面 | 記憶體供應商與客戶的晶片／系統團隊 | 讓記憶體規格更貼近特定系統 | 已完成設計、樣品交付、客戶驗證或量產 |
| 重做堆疊底部邏輯 | 依產品需求設計底部邏輯晶片與資料路徑 | 記憶體、邏輯設計與晶圓製造角色 | 增加客製控制、介面或資料路徑 | 客戶名稱、驗證結果、量產數量或已實現毛利 |
| 搬移部分資料整理工作 | 把原本由運算晶片執行的部分工作移到記憶體底部 | 記憶體、運算晶片、平台與軟體角色 | 改變資料在哪裡先被整理 | 共同測試結果、客戶採用、量產或財務貢獻 |

### 再把每家公司放回自己的證據位置

| 公開公司 | 本輪談的是哪種改法 | 已看到的公開證據 | 目前走到哪一步 | 還不能說什麼 |
|---|---|---|---|---|
| 三星（Samsung） | 依客戶架構調整容量、速度、耗電與介面 | 官方定義列出客製欄位，並把一般第四代強化版樣品與客製版本時程分開 | 客製版本規劃於 2027 年提供客戶樣品；一般版本另有樣品 | 客製樣品已交付、客戶驗證完成或已量產 |
| SK 海力士（SK hynix） | 把部分資料前處理移到堆疊底部邏輯晶片 | 公司展示底部晶片資料流架構 | 架構展示 | 共同基準測試、具名客戶、客戶驗證或量產 |
| 美光（Micron） | 提供客製底部邏輯晶片，並揭露晶圓製造分工 | 公司說明產品選項、客戶討論與較高毛利預期 | 產品選項與管理層預期 | 已實現較高毛利、客戶驗證或量產數量 |

第一張表回答「改了哪裡」，第二張表回答「公開證據走到哪一步」。一般版本的樣品、客製版本的
樣品規劃與底部晶片架構展示，不是同一個完成節點。三家公司也沒有共同產品定義、測試條件、
數量與財務分母，因此目前不能合併成一條供應商進度排名。

## 客製不是一顆晶片：六份交接合約要一起凍結

「底部邏輯可以客製」只指出一個設計位置，沒有說明整套系統怎麼完成。三星公開的研發分工把
工作負載建模、輸入輸出架構與智財、韌體、底部晶片及客戶技術合作分開；三星 Foundry 與台積電
的資料又顯示控制器位置、晶粒介面與製程節點會跟著設計路徑改變。三星在另一份 HBM4E 技術頁
還指出，底部晶片內的高速介面本身就是主要發熱區。這些資料不能合成一個已量產專案，卻足以
說明研究時為何要逐份查六種交接。

| 本文六份交接合約 | 要固定哪些欄位 | 現有一手資料提供的入口 | 沒有這份合約會發生什麼誤讀 |
|---|---|---|---|
| 1. 工作負載與功能 | 輸入資料、要搬走的工作、正確答案、等待時間、耗電目標與失效條件 | SK 海力士把資料前處理移到底部晶片；三星研發頁另列 workload modeling、runtime prototype 與 system software | 只看到功能名稱，就把模擬概念當成端到端效能或客戶需要 |
| 2. 容量、速度、功耗與介面 | 容量、通道、腳位速度、電力包絡、命令／資料／錯誤規則與版本 | 三星的 custom HBM 定義列出容量、速度、電力特性與介面；研發頁另列 I/O architecture、circuit 與 IP | 用一個最高頻寬數字替整份介面與電力契約背書 |
| 3. 底部邏輯與智財 | 控制器與額外邏輯放哪裡、誰提供 IP、製程、面積、時序、功耗與驗證版本 | 三星 Foundry 描述 controller／additional logic placement；美光與台積電分別揭露客製 base die 與 foundry node 路徑 | 看到「base die」三個字，就假設三家公司做的是同一顆晶片 |
| 4. 韌體與系統軟體 | 初始化、排程、錯誤處理、資料格式、runtime／compiler 版本與回退方法 | 三星 Memory Labs 把 custom HBM firmware 與 architecture／base-die 工作分列 | 晶片能開機或展示，就被改寫成客戶軟體已能穩定使用 |
| 5. 製造、封裝與熱 | DRAM／logic 製程、堆疊、接合、中介層、供電、熱點、測試與可製造條件 | 台積電分開 N12 HBM4 與 N3P custom HBM4E；三星把 D2D PHY 發熱與仍在驗證的 thermal path 分開 | 只比較邏輯功能，漏掉發熱、良率、封裝與重驗成本 |
| 6. 樣品、資格與商業 | 樣品身分、客戶、pass criteria、change control、良率、量產數量、NRE、售價與毛利 | 現有公告只分別到樣品規劃、架構展示、產品選項或一般 HBM4E 樣品 | 把設計完成、送樣、客戶通過、量產與收入合成同一個里程碑 |

六份合約不是固定的產業標準，也不表示每家公司都用相同組織開發。它們是查漏用的閱讀表：
前五份回答「系統如何做出來」，第六份回答「客戶是否真的接受，以及是否進入公司財務」。目前
沒有任何一份公開資料把同一具名客戶、同一產品世代與六份簽核全部接起來。

### 一個功能變更，為什麼會沿六份合約傳下去

假設供應商把一段資料前處理移到底部晶片，研究者不能只記「多了一項功能」。先要固定它處理
哪種資料與正確結果；接著確認資料如何經過介面、控制器與客製邏輯，再核對韌體和系統軟體如何
啟用、停用或回退。新增邏輯會占用面積與電力，也可能改變高速介面熱點、封裝及散熱，所以製程、
封裝與熱測試要重新對齊。最後若其中任何欄位改版，客戶要依變更範圍決定重跑哪些資格測試。

這條連鎖只說明要查哪些責任，不代表改動一定提高效能、成本或毛利。沒有固定版本、測試輸入、
通過條件、變更紀錄與量產分母時，仍不能把技術相鄰關係寫成 design win 或台灣公司收入。

## 來源與證據邊界

- [Samsung HBM4／Custom HBM roadmap](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing)（2027 樣品時程）。
- [Samsung 韓文官方定義](https://news.samsung.com/kr/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90-%EC%84%B8%EA%B3%84-%EC%B5%9C%EC%B4%88-%EC%97%85%EA%B3%84-%EC%B5%9C%EA%B3%A0-%EC%84%B1%EB%8A%A5%EC%9D%98-hbm4-%EC%96%91%EC%82%B0-%EC%B6%9C%ED%95%98)（客製欄位）。
- [SK hynix GTC 2026 review](https://news.skhynix.com/gtc-2026-review/)（Stream DQ 與 base die）。
- [Micron FY2025 Q4 slides](https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02)（p.13，標準／客製 base logic die 與管理層毛利預期）。
- [Samsung HBM4E sample shipment](https://news.samsung.com/global/samsung-electronics-begins-shipment-of-industry-first-hbm4e-samples)（標準 HBM4E 樣品與 custom 時鐘的分界）。
- [Samsung Memory Labs](https://semiconductor.samsung.com/about-us/locations/us-rnd-labs/memory-labs/)（I/O architecture／IP、firmware、base die、customer engagement 與 workload／software 分工）。
- [Samsung Foundry HPC／AI application service](https://semiconductor.samsung.com/foundry/application-specific-service/hpc-ai/)（die-to-die interface、base-die controller 與 additional logic 的供應商架構邊界）。
- [TSMC OIP Forum：A Shared Commitment to Energy-Efficient AI](https://www.tsmc.com/english/node/233)（HBM4 N12 與 custom HBM4E N3P logic-base-die 路徑）。
- [Samsung COMPUTEX 2026 HBM4E／HPB 技術頁](https://semiconductor.samsung.com/kr/news-events/tech-blog/samsung-showcases-next-generation-ai-semiconductor-innovations-at-computex-2026/)（D2D PHY 發熱位置、thermal path 驗證與未來採用時鐘）。

本文不採用三家公司自述效能做跨公司比較，也不把客戶數、HBM 總銷售或 HBM4 量產套用到
custom HBM。現有資料沒有同一產品世代、共同 benchmark、客戶資格、數量與財務定義，因此不報
領先者、TAM、市占或市場是否反映。

## 影響路由

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: Custom HBM 可能改變 DRAM 與 base-die 價值分配，但本輪沒有 universe 記憶體公司的具名 custom HBM 產品、客戶資格或財務證據
evidence_boundary: HBM 產能、記憶體景氣或一般 HBM 客戶不等於 custom HBM design win、量產與較高毛利
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: 客製 base die 與堆疊形成 bonding、TSV、測試與熱管理搜尋入口，但產品世代與 qualification 尚未對齊
evidence_boundary: 具備 HBM 封測能力不等於參與任一具名 custom HBM、取得訂單或收入
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-09-15
rationale: Base-die 邏輯與客戶 ASIC 共同設計可能增加介面、控制與邏輯 IP，但沒有 universe 公司被供應商或客戶具名
evidence_boundary: 可設計高速介面或 ASIC 不證明 custom HBM IP tape-out、qualification、NRE 或財務貢獻
-->

## 下一個可證明／否定的節點

- 供應商交付實體 custom HBM sample，並說清楚產品世代、客製欄位、接收方與測試條件。
- 客戶端獨立確認 qualification，而不是只有記憶體供應商說正在合作。
- 將 base-die 工作負載下放放入可重現 workload，揭露 latency、power、thermal 與端到端限制。
- 季報或法說把 custom HBM 的 NRE、量產、售價、良率或毛利從預期升級為可核對結果。
- 台灣公司必須由平台／記憶體端與公司端完成產品、資格、出貨及財務雙向核對，否則只保留族群搜尋路由。
