# 接點變少不等於設計變簡單：用四層契約讀懂 SPHBM4

<!-- research_topic
topic_id: MI-2026-08-01-SPHBM4-ORGANIC-SUBSTRATE
schema_version: 3
status: triaged
priority: p2
captured_at: 2026-08-01
source_published_at: 2026-07-13
last_reviewed_at: 2026-08-12
review_due: 2026-08-26
source_type: mixed
publisher_domain: jedec.org
canonical_url: https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates
source_chain_id: jedec-sphbm4-hbm4-product-clock-20260618-20260713
stock_ids:
group_ids: pcb,ipdesign,packtest
trigger_type: industry_standard
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C7
base_confidence: medium
confidence_basis: JEDEC 現行標準頁可確認 DRAM 堆疊、base die、分散式獨立通道與封裝路徑必須分層閱讀，Eliyan 也已提出具名 PHY 路徑；但 bump-map addendum 尚未公開、且沒有記憶體產品、跨廠互通、客戶資格或財務分子
cross_company_numbers: false
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: jedec_sphbm4_standard_captured
evidence: source_chain:jedec-sphbm4-hbm4-product-clock-20260618-20260713
-->

<!-- research_source
source_id: S1
role: standard
publisher: JEDEC
title: JESD330-4 SPHBM4 標準公告
published_at: 2026-07-13
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates
locator: interface base die、4:1 serialization 與 organic substrate 段落
limitation: 標準公告沒有產品、客戶採用、量產時程、良率或供應商名單
-->

<!-- research_source
source_id: S2
role: company_release
publisher: Micron
title: Micron 2026 財年第三季產品與 HBM4 進度
published_at: 2026-06-24
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://investors.micron.com/node/50671
locator: HBM4 high-volume production 段落
limitation: Micron 談的是既有 HBM4 產品，沒有表示採用 SPHBM4
-->

<!-- research_source
source_id: S3
role: competitor_primary
publisher: SK hynix
title: 12 層 HBM4E 樣品公告
published_at: 2026-06-18
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://news.skhynix.com/en/12-layer-hbm4e-sample-1/
locator: sample 與 base die 產品時程段落
limitation: 樣品公告沒有說明 SPHBM4 介面、量產採用或外部封裝供應商
-->

<!-- research_source
source_id: S4
role: exchange
source_kind: living_index
publisher: Taiwan Stock Exchange
title: 公開資訊觀測站公司申報查詢入口
published_at:
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://mops.twse.com.tw/mops/web/index
locator: 台灣基板、矽智財與封測公司季報、法說及重大訊息查找入口
limitation: JEDEC 與記憶體供應商資料只支持技術路徑；入口本身不證明台灣公司料號、認證或量產
-->

<!-- research_source
source_id: S5
role: standard
source_kind: living_index
publisher: JEDEC
title: JESD330-4 Version 1.0 標準頁與 bump-map addendum 狀態
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.jedec.org/standards-documents/docs/jesd330-4
locator: 2026-08-12 頁面之 Release Number／Published、公開摘要，以及 JESD330-4-1 Addendum No. 1 to JESD330-4 SPHBM4 for Bump Map 段落
limitation: 公開頁只提供摘要；完整規格需註冊或登入，bump-map addendum 仍只供 JC-42 會員並等待董事會核准公開，不能補寫未公開的速率、訓練、等化、FEC、接點或測試細節
independence_group: jedec
-->

<!-- research_source
source_id: S6
role: company_release
source_kind: living_index
publisher: Eliyan
title: NuLink-SP 標準有機封裝 D2D PHY 產品頁
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://eliyan.com/products/
locator: 2026-08-12 頁面之 NuLink-SP high-bandwidth interface IP cores、standard organic／laminate package substrate 與產品表
limitation: 公司產品頁證實的是標準封裝 D2D PHY 產品家族與公司規格，不直接宣告 JESD330-4 compliance，也沒有記憶體樣品、跨廠互通、客戶資格、出貨或財務分子
independence_group: eliyan
-->

<!-- research_source
source_id: S7
role: company_release
source_kind: living_index
publisher: Eliyan
title: 官方公司貼文對 SPHBM4 與 NuLink-SP 的產品定位
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.linkedin.com/posts/eliyan-corporation_hbm4-and-sphbm4-scaling-memory-bandwidth-activity-7447249719749156864-xvXH
locator: 2026-08-12 查得官方公司貼文之 NuLink-SP PHY designed specifically for SPHBM4 與公司功耗效率主張
limitation: 這是供應商社群行銷陳述，不是 JEDEC compliance report、完整 datasheet、第三方功耗比較、記憶體廠採用、客戶資格或量產財務證據
independence_group: eliyan
-->

<!-- research_source
source_id: S8
role: other_primary
source_kind: document
publisher: Open Compute Project
title: Electrical Interfaces Performance Metrics
published_at: 2024-11-19
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.opencompute.org/documents/odsa-whitepaper-2024-electrical-interfaces-performance-metrics-nov-19-2024-docx-pdf
locator: file pp.32–42；BER／latency measurement points、unit bandwidth、power efficiency、edge／area bandwidth density 與 recommended minimum list of parameters
limitation: 這是 OCP 對一般 electrical D2D PHY 的量測框架，不是 JESD330-4 規格、SPHBM4 compliance plan 或任何產品成績；published_at 取自官方檔名日期，文件正文未另列發布日。命令列與 web screenshot 端點回 403，未建立本地 SHA；官方瀏覽器 PDF viewer 已把實際引用頁及相鄰頁 file pp.32–42 逐頁渲染目視核對
independence_group: ocp-phy-metrics
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: JEDEC 的 JESD330-4 定義以 interface base die 將 2,048 個 HBM4 資料訊號透過 4 比 1 序列化降為 512 個主機側訊號，並支援標準有機基板
supporting_source_ids: S1
contrary_source_ids:
as_of: 2026-07-13
basis: 標準組織公告直接列出訊號數、序列化比例與基板路徑
boundary: 證實的是介面規格，不是產品效能、採用率、良率或量產時程
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: superseded
claim: SPHBM4 提供一條降低主機側連線密度、讓 HBM4 級頻寬可使用有機基板的工程路徑，但近期基準情境仍是補充而非立刻取代既有 HBM4 封裝
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-13
basis: JEDEC 已定義新路徑，而兩家記憶體廠同期仍以既有 HBM4 或 HBM4E 產品階段推進
boundary: 沒有 SPHBM4 產品、客戶採用或成本良率資料，不能估計滲透率與替代速度
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id: C7
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: Micron 公告 HBM4 已進入大量生產，SK hynix 公告 HBM4E 仍處於樣品階段
supporting_source_ids: S2,S3
contrary_source_ids:
as_of: 2026-06-24
basis: 兩家記憶體供應商分別直接揭露自身產品階段
boundary: 不同公司的產品名稱與階段不可拿來排名技術優劣，也都沒有證實 SPHBM4 採用
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: unverified
status: active
claim: 台灣 PCB、矽智財或封測公司已取得 SPHBM4 量產訂單或可量化受惠
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: JEDEC 與兩家記憶體公司均未列名台灣供應商，也沒有產品級採用資料
boundary: 不建立特定基板材料、base die 設計服務、OSAT 訂單、收入或毛利事實
verification_needed: 需記憶體供應商產品文件與台灣公司法說雙向確認料號、客戶、驗證與量產
resolution:
-->

<!-- research_claim
claim_id: C5
label: verified
status: active
claim: JEDEC 的現行 JESD330-4 公開摘要把 SPHBM4 定義為分散式主機介面；各通道彼此完全獨立且不必同步，每個通道以 16-bit DDR 資料匯流排、四倍於對應 64-bit HBM4 通道的速率運作
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-12
basis: S5 的 JEDEC 現行標準頁逐句列出 distributed interface、independent channels、not necessarily synchronous、16-bit DDR 與 four times faster mapping
boundary: 公開摘要沒有提供完整通道狀態機、時脈、延遲、訓練、等化、錯誤處理、測試或互通條件，不能用二手規格表補齊
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
claim: JESD330-4 Version 1.0 主標準已於 2026 年 6 月發布，但截至 2026-08-12，JESD330-4-1 bump-map addendum 仍只供 JC-42 會員，JEDEC 表示待董事會核准後才會把公開連結放上標準頁
supporting_source_ids: S5
contrary_source_ids:
as_of: 2026-08-12
basis: S5 現行頁面的 Release Number／Published 與 Addendum No. 1 狀態可直接定位
boundary: 這只表示公開文件鏈仍有後續治理節點；不能推論 addendum 技術失敗、產品延期、廠商無法先行設計，或任一基板／封裝商已取得規格
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C7
label: inference
status: active
claim: SPHBM4 不應只讀成「把 2,048 條資料線縮成 512 條」；研究上必須把 HBM4 DRAM 堆疊、interface base die 的通道轉換、分散式高速主機通道、bump map 與有機封裝路徑四層分開，並再逐關核對元件、封裝、系統、客戶與財務，任何一層成立都不能替其餘層補證據
supporting_source_ids: S1,S2,S3,S5,S6,S7
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C2；S1／S5 把同一記憶體堆疊、不同 base die、獨立通道與封裝路徑分開，S5 又顯示 bump-map 文件仍有獨立治理節點；S6／S7 只把具名 PHY 路徑推進到供應商陳述，仍未接到記憶體與客戶產品
boundary: 四層框架不判斷 SPHBM4 與傳統 HBM4 的成本、功耗、延遲、可靠度、滲透率或勝負，也不把 Eliyan、台灣 PCB、矽智財與封測公司升格為已採用供應商
verification_needed:
correction_kind: supersedes
corrects_claim_id: C2
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Eliyan 現行產品頁列出面向標準有機／laminate package 的 NuLink-SP D2D PHY 產品家族，官方公司貼文另把 NuLink-SP 描述為 specifically designed for SPHBM4
supporting_source_ids: S6,S7
contrary_source_ids:
as_of: 2026-08-12
basis: S6 的公司產品頁與 S7 的官方公司貼文可直接核對產品家族及 SPHBM4 定位
boundary: 證實的是單一供應商的產品與定位陳述，不是 JESD330-4 compliance、記憶體 base die tape-out、第三方功耗結果、跨廠互通、客戶採用、量產或收入
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C9
label: unverified
status: active
claim: 任一具名 SPHBM4 記憶體、base die 與主機 PHY 已依同一 JESD330-4／bump-map 版本完成 silicon、跨廠互通、封裝可靠度、系統工作負載與客戶資格，並形成可辨識量產收入
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: 現有來源停在標準、待公開 addendum、既有 HBM4 產品時鐘與供應商 PHY 定位，沒有把同一具名產品的完整證據鏈接起
boundary: 不以標準會員、公司貼文、相鄰 D2D PHY 規格、既有 HBM4 出貨或產業供應鏈身分替代 SPHBM4 產品與客戶證據
verification_needed: 需公開版本化 bump map、具名 memory／base-die／host PHY datasheet、silicon 與跨廠測試、封裝可靠度、系統工作負載、客戶 qualification、量產出貨及同產品財務分子
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: JEDEC 公開的 2,048 個 HBM4 資料訊號與 512 個 SPHBM4 主機側資料訊號、4 比 1 序列化關係，在把原路徑每線速率正規化為 1 時，分別得到 2,048×1 與 512×4 的相同 raw throughput 指數 2,048；資料訊號數減少 75%，每線速率提高為 4 倍，但這個等式沒有包含 payload、延遲、錯誤、功耗、幾何或良率
supporting_source_ids: S1,S5
contrary_source_ids:
as_of: 2026-08-14
basis: S1／S5 直接固定資料訊號數與四倍速率映射；Python Fraction 與獨立 awk 對同一固定輸入重算一致
boundary: 正規化的 1 與 throughput index 不是 JESD330-4 GT/s、GB/s 或產品規格；相同 raw 指數不表示 payload goodput、read／write latency、BER、pJ/bit、shoreline density、成本或系統效能相同
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
claim: OCP Electrical Interfaces Performance Metrics 把 data-lane speed、Rx 加 Tx PHY bandwidth、shoreline bandwidth density、reach、pJ/bit、packaging、minimum bump pitch、BER 與 T0 latency 列為 D2D PHY 最小指標組，並把 serializer-to-deserializer、含 packet／FEC／CRC 與含 retry 的 BER／latency 量測點分開
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-08-14
basis: S8 file pp.32–42 的 measurement-point 表、unit-bandwidth／power-efficiency 定義與 minimum-parameter table 可逐頁定位
boundary: OCP 白皮書是一般量測方法，不規定 SPHBM4 必須採哪一種 FEC、CRC、retry、方向配置或測試值，也不能替 JEDEC、記憶體供應商、客戶或第三方出具 compliance 結果
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
claim: Eliyan 現行產品頁把標準有機／laminate package 的 NuLink-SP PHY 產品表分列 process node、data lanes、data rate per lane、beachfront bandwidth、area bandwidth 與 reach，證明一家供應商已用多欄而非只用 aggregate bandwidth 描述其產品家族
supporting_source_ids: S6
contrary_source_ids:
as_of: 2026-08-14
basis: S6 現行產品表可直接定位標準封裝 PHY 欄位與公司報告值
boundary: 這仍是單一供應商自報的相鄰 D2D 產品資料，不是每一欄都對應 SPHBM4、JESD330-4 compliance、獨立 benchmark、具名記憶體／主機產品、客戶資格、量產或收入；表格也不能補出未列的同口徑 BER、T0 latency、總 PHY power 與產品級 payload
verification_needed:
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 判讀 SPHBM4 的「同頻寬、較少接點、有機基板」敘事，應把標準版本、方向與通道、lane／wire／pin、每線速率與 raw、payload、latency measurement point、BER／recovery exposure、power／energy、shoreline／reach／package，以及 silicon—system—customer—financial evidence 綁成同一份十欄 PHY 效能護照
supporting_source_ids: S1,S5,S6,S8
contrary_source_ids:
as_of: 2026-08-14
basis: JEDEC 固定 SPHBM4 的通道與序列化架構，OCP 固定一般 D2D PHY 的量測欄位與分層測點，Eliyan 產品表顯示實作者會分列部分 PHY 指標；十欄護照把三種證據物件的共同鍵與缺口顯式化
boundary: 護照是研究可比性與拒絕過度外推的框架，不是 JEDEC 規格新增條文、OCP compliance score、Eliyan 產品背書、產品效能排名、成本模型、採用率、台灣供應商訂單或投資建議
verification_needed: 以同一具名 SPHBM4 memory／base die／host PHY／package／system 版本公開 raw 與 payload、方向、量測點、BER exposure、power、reach、silicon／customer qualification、良率成本及財務共同鍵
correction_kind:
corrects_claim_id:
corrected_by_claim_id:
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-12
retirement_reason: C2 的單一路徑補充框架已由 C7 的四層契約與公開文件節點框架取代
claim_ids: C1,C2,C3
metric: 記憶體供應商是否發布 SPHBM4 產品、樣品、客戶採用及功耗延遲數據
source_ids: S1,S2,S3
watch_source_ids: S4
frequency: monthly
frequency_detail: 每月產品公告與每季法說
next_check: 2026-08-15
trigger: 任一供應商首次直接使用 SPHBM4 名稱並揭露樣品、客戶或量產時程
invalidation: 若未出現產品採用且序列化功耗、延遲或可靠度代價抵銷基板優勢，快速採用假說失效
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C4
metric: 台灣基板、矽智財與封測公司的 SPHBM4 料號、認證與量產證據
source_ids: S1,S2,S3,S4
watch_source_ids: S4
frequency: quarterly
frequency_detail: 每季法說與重大訊息
next_check: 2026-10-31
trigger: 公司與記憶體客戶文件可雙向核對相同產品、時程及供應角色
invalidation: 若只有產業標準推導而沒有公司級產品與財務證據，個股受惠映射持續無效
-->

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C3,C5,C6,C7,C8,C9
metric: JESD330-4 公開文件鏈、具名記憶體／base-die／host PHY、跨廠互通、封裝可靠度、系統資格與量產證據
source_ids: S1,S2,S3,S5,S6,S7
watch_source_ids: S5,S6,S7
frequency: weekly
frequency_detail: 每兩週檢查 JEDEC 標準頁與具名實作者；記憶體廠或運算平台出現 SPHBM4 即提前重審
next_check: 2026-08-26
trigger: JESD330-4-1 公開，或任一記憶體／運算平台以同一版本列名 SPHBM4 memory、base die、host PHY、silicon 或 qualification
invalidation: 若完整 bump map、通道功耗延遲、封裝可靠度或系統工作負載長期無法閉合，或產品改採其他介面路徑，SPHBM4 快速產品化基準下修
-->

<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: standard_product_timeline_and_supplier_boundary_reviewed
evidence: sources:S1,S2,S3
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
reason: editorial_plain_language_wave93_sphbm4_signal_tradeoffs_roles_and_six_gate_ladder
evidence: editorial:reader_layer_only_no_claim_source_monitor_or_impact_change
-->

<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: corrected_pin_count_frame_with_four_layer_interface_package_and_qualification_contract
evidence: sources:S5,S6,S7
-->

<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: lane_raw_payload_energy_and_phy_measurement_passport_added_without_thesis_clock_refresh
evidence: sources:S1,S5,S6,S8
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **記憶體堆疊**：把多層記憶體裸晶垂直整合，以增加容量與資料傳輸量；層數增加也會提高接合、測試、供電與散熱難度。
- **記憶體裸晶（memory die／DRAM die）**：尚未完成封裝的單片動態記憶體晶片；上方裸晶沿用同一世代，不代表底部介面與封裝路徑也相同。
- **運算晶片／主機端**：接收記憶體資料並執行運算的一側；本文的「主機側訊號」是連到這一側的資料線，不是整個封裝的全部接點。
- **資料訊號**：專門搬運資料內容的電氣連線；封裝仍另有電源、接地、命令與時脈等接點，不能把資料訊號數當成總接點數。
- **接點（pin）**：晶片或封裝對外傳送訊號與電力的連接位置；接點變少可能降低扇出密度，但不會自動降低整體成本。
- **平行傳輸**：同一時間用很多條線各自搬運一部分資料；線多可分攤速度，但會增加接點、佈線與封裝密度。
- **序列傳輸**：把資料排成順序，用較少的線以更高速度傳送；線少不代表更容易，因為每條線的速度與訊號品質要求會提高。
- **四比一序列化與 DDR（4:1 serialization）**：把原本四條資料路徑合併到一條更快的路徑；DDR 表示一個時脈週期的上升與下降邊緣都能搬資料，本文標準用兩者把主機側資料訊號由 2,048 個降為 512 個。
- **總傳輸量（throughput）**：一段時間內整體可以搬運多少資料；總量相同不代表功耗、等待時間、錯誤率與實作成本相同。
- **每線速率／GT/s**：單一資料線每秒要完成多少十億次傳輸；資料線變少時，每條線通常要跑得更快，設計與測試難度也會增加，GT/s 仍不等於有效資料量。
- **延遲**：送出要求到收到資料之間的等待時間；增加轉換與控制邏輯後，必須用實測確認是否仍符合系統需求。
- **功耗**：晶片與連線傳送資料所需的電力；接點減少不代表高速介面、時脈與轉換邏輯一定更省電。
- **熱管理**：把晶片與封裝產生的熱帶走；介面邏輯、記憶體堆疊與運算晶片共存時，要一起檢查熱點與散熱路徑。
- **較長通道（longer channel）**：訊號可以走更長的實體距離；距離增加可能擴大配置彈性，也會增加損耗、反射與干擾風險。
- **訊號完整性**：訊號抵達接收端時仍能清楚辨認資料的程度；速度、距離、材料、接點與雜訊都會影響結果。
- **位元錯誤率（BER／bit error rate）**：傳輸資料中出錯位元的比例；沒有共同條件下的實測，就不能判斷新連線是否足夠可靠。
- **資料通道與資料導線（data lane／data wire）**：通道是資料傳輸的邏輯或電氣路徑，導線是實際承載訊號的導體；單端、差分、時脈與輔助訊號配置不同時，兩個數不一定相等。
- **傳送、接收與方向（Tx／Rx）**：Tx 是送出，Rx 是接收；單向、雙向合計、半雙工與同時雙向的頻寬分母不同，不能只看一個總數。
- **原始頻寬與有效資料吞吐（raw bandwidth／payload goodput）**：前者由通道數與每線速率得到，後者只計真正送達的有效資料，還會受控制資訊、閒置、錯誤處理與重試影響。
- **序列器與解序列器（serializer／deserializer）**：前者把較寬的平行資料排成高速序列，後者在接收端還原；兩端之間的等待只是整體記憶體延遲的一部分。
- **FEC、CRC 與重試**：FEC 用冗餘資訊更正部分錯誤，CRC 用校驗值偵測錯誤，重試則重新傳送；可靠度可能改善，但額外資料與處理也要另記延遲及功耗。
- **T0／T1 量測點**：OCP 白皮書把序列器到解序列器的 PHY 延遲稱為 T0，把含封包、FEC／CRC 區塊的延遲另列為 T1；兩者不能互相替代。
- **beachfront／shoreline 與頻寬密度**：晶粒邊緣留給互連的線性寬度，以及每毫米能承載的頻寬；需要實際幾何與方向，不能由資料訊號總數單獨反推。
- **每位元能耗（pJ/bit）**：以同一量測範圍的 PHY 功率除以同口徑頻寬；OCP 指出 mW/Gbps 與 pJ/bit 在量綱上等價，但分子是否含 Tx、Rx、clock 必須說清楚。
- **reach**：在指定通道、封裝、速率與錯誤條件下可維持目標表現的傳輸距離；「可以走更遠」不等於任何材料、佈線或產品都已通過。
- **介面基礎晶片（interface base die）**：位在記憶體堆疊底部、管理資料轉換與高速介面的邏輯晶片；換這一層不等於上方記憶體裸晶也換代。
- **高速序列介面／PHY／D2D 與 NuLink-SP**：PHY 是實體電氣介面，D2D 是同一封裝內的晶粒互連；NuLink-SP 是 Eliyan 的標準封裝 D2D PHY 產品家族，公司把它定位到新標準，但定位不等於通過標準或客戶驗證。
- **微凸塊**：封裝內連接晶粒的微小金屬接點；接點越密，對準、接合、檢查與良率控制越困難。
- **矽中介層**：用矽材料製成、在運算晶片與記憶體之間提供高密度連線的封裝結構；它是既有高密度路徑之一。
- **有機基板（organic substrate）**：由樹脂等有機材料製成、負責在晶片與電路板之間扇出訊號與電源的封裝基板；「有機」不是環保認證。
- **ABF**：高階封裝載板常見的絕緣材料類型；標準只寫有機基板時，不能自行指定一定採用 ABF。
- **BT**：另一類常見封裝基板樹脂材料；它與 ABF 的材料、線寬與應用不同，標準也沒有指定一定採用 BT。
- **封裝良率**：投入組裝後能成為合格產品的比例；接點數或材料路徑改變後，仍要用實際製造結果判斷成本是否改善。
- **可靠度認證**：在溫度、壽命、機械與電氣等條件下確認產品能否長期使用；單次功能展示不能代替可靠度結果。
- **高頻寬記憶體第四代（HBM4）**：把多層動態記憶體疊在一起，以很寬的介面連到運算晶片；重點是同時搬運大量資料。
- **標準封裝高頻寬記憶體第四代（SPHBM4）**：沿用第四代高頻寬記憶體裸晶，但更換底部介面與主機側連線方式，讓有機基板成為可選路徑。
- **JESD330-4／JESD330-4-1 與版本（version）**：前者是 SPHBM4 主標準，後者是接點圖附錄；版本要和晶片、封裝及測試一起固定，主標準發布不等於附錄已公開或已有產品採用。
- **強化版高頻寬記憶體第四代（HBM4E）**：記憶體廠對 HBM4 後續強化版本的產品名稱；它與 SPHBM4 的有機基板介面路徑不是同一件事。
- **CoWoS**：台積電的先進封裝平台名稱，可用矽中介層等方式把運算晶片與高頻寬記憶體放在同一封裝；新標準發布不代表它立即被取代。
- **標準／樣品／客戶認證**：共同規則、可測實體與客戶通過是三種不同證據；前一項完成不代表後一項自動成立。
- **量產與可辨識收入**：產品持續穩定製造、交付與重複採購，且財務金額能對應同一產品；公司總營收不能直接證明新標準貢獻。

### 三句話抓重點

- 記憶體可以用很多條較慢的資料線，也可以用較少但更快的資料線；後者減少接點，卻把壓力移到每線速度、訊號品質、功耗與測試。
- 新路徑不只把四條資料合成一條更快的線；每條主機通道可以獨立工作、彼此不必同步，因此控制、時序與驗證也要逐通道閉合。
- 主標準與一家供應商的對應介面路徑已出現，但封裝接點附錄仍未公開，也沒有具名記憶體、系統整合、客戶認證、量產產品或可辨識收入。

### 為什麼重要

判斷新連線不能只看接點數，也不能先假設有機基板一定比較便宜。整體成本還包含底部介面晶片、
高速傳輸功耗、材料與佈線、組裝測試、散熱、良率和客戶驗證。某一段變簡單，另一段可能變得
更難，最後仍要由完整產品的效能、可靠度與製造結果裁決。

如果這條路徑真的進入產品，價值可能在記憶體、邏輯設計、基板和封裝測試之間重新分配；但
標準本文、封裝接點圖、實體晶片、完整記憶體、系統與客戶是不同證據。在同一具名產品把這些
關係接起以前，它仍是設計選項與供應商產品方向，不是供應鏈訂單。

### 接下來怎麼追

- 先等封裝接點附錄公開，固定主標準、附錄與實作者各自使用的版本，避免把同名介面當成同一實作。
- 再找具名底部介面晶片、主機端介面與完整記憶體，核對通道、時脈、功耗、延遲、錯誤處理、基板、熱與可靠度。
- 最後找運算晶片或系統端的跨廠測試、客戶認證、量產出貨與可辨識收入；沒有雙向文件前，不建立台灣公司訂單。

### 想一想

- 把四條資料線合成一條更快的線後，哪些難題會從封裝接點移到晶片、基板、供電與測試？
- 一份主標準、尚未公開的接點附錄、一顆供應商介面晶片與一套可出貨系統，分別證明了什麼？
- 如果總搬運量相同，卻讓等待時間、錯誤率或良率變差，這條路徑應全面替代、只做補充，還是暫時不被採用？

## 先把一顆 SPHBM4 拆成四層

「2,048 變 512」只描述主機側**資料訊號**的縮減，不是整顆產品的全部接點，也沒有回答哪一層
負責記憶、轉換、傳輸或封裝。初學者可先把一顆產品拆成四層，再問每層交付什麼。

| 四層契約 | 這一層在做什麼 | JEDEC 公開資料已確認 | 尚未被公開資料證明 |
|---|---|---|---|
| 1. 記憶體裸晶與堆疊 | 儲存資料，決定單一堆疊的容量、記憶體核心行為與堆疊製造 | 沿用 HBM4 的記憶體裸晶／堆疊，單一堆疊的容量能力相同 | 具名 SPHBM4 堆疊、堆疊良率、熱、供應量與價格 |
| 2. 介面基礎晶片 | 在記憶體核心與主機之間轉換通道寬度與速度 | 使用不同 buffer／interface base die；每個 64-bit HBM4 通道對應一個速度為四倍的 16-bit DDR 主機通道 | 具名晶片、製程、面積、功耗、延遲、時脈與錯誤處理實測 |
| 3. 分散式主機通道 | 把資料送到運算晶片；各通道可獨立運作 | 通道彼此完全獨立，且不一定彼此同步 | 完整控制狀態、訓練、等化、錯誤更正、跨廠互通與主機控制器結果 |
| 4. 接點圖與有機封裝 | 把訊號、命令、時脈、電源與接地落到實際接點、基板與組裝流程 | 較少資料訊號可放寬接點間距並支援有機基板；主標準頁已列出 bump-map addendum | addendum 的公開核准版本、材料、線路、供應商、可靠度、良率與量產流程 |

這四層可以由不同公司負責，也可能在不同時間成熟。例如一家介面供應商可以先宣布產品方向，
但記憶體廠尚未交付堆疊、主機廠尚未完成控制器，封裝廠也尚未拿到公開接點圖。此時能說的是
「實作生態開始出現」，不能把四層一起標成完成。

### 512 是資料訊號，不是「整顆只有 512 個接點」

一顆記憶體還要傳命令、位址與時脈，也要有電源、接地與其他控制連線。JEDEC 公告比較的是
2,048 與 512 個**資料訊號**；它沒有在公開摘要提供整顆產品的總接點數。因此「資料線減為四分之一」
不能改寫成「封裝接點、面積或成本都減為四分之一」。

## 相同總傳輸量，不等於每一次存取體驗相同

總傳輸量回答「長時間平均可以搬多少資料」，但系統仍要逐一處理每次要求、各條通道、錯誤與熱。
下表把已知架構與仍待實測的問題分開；右欄是驗證問題，不表示公開摘要已規定特定做法。

| 閱讀問題 | 已知的架構變化 | 必須另外驗證 |
|---|---|---|
| 一次要求要等多久 | 資料要經過不同的介面基礎晶片與更高速的主機通道 | 讀寫延遲、排隊、轉換與錯誤重送代價 |
| 各通道能否各自前進 | 公開摘要明列通道獨立且不必同步 | 排程、順序、跨通道協調、故障隔離與服務品質 |
| 高速訊號能否穩定抵達 | 資料線較少、每條速度更高，且有機基板可支援較長路徑 | 損耗、反射、雜訊、時脈對齊、訓練、等化與位元錯誤率 |
| 出錯後系統怎麼恢復 | 公開摘要沒有列出完整錯誤契約 | 錯誤偵測／更正、回報、重試、降速與可用性策略 |
| 總功耗與熱點是否改善 | 接點密度下降，但介面轉換與高速傳輸增加工作 | 每位元能耗、base die 熱點、記憶體溫度與整個封裝功耗 |

二手文章列出的訓練、等化或錯誤更正細節，本輪沒有可公開逐頁核對的 JEDEC 原文，因此只保留成
測試清單，不升格成已驗證規格。這個停點很重要：研究中心教的是如何辨認缺少哪份證據，不是把
讀不到的標準內容用看似合理的工程常識補完。

## 2,048 變 512，只守住 raw throughput 的等式

JEDEC 的公開關係可以先做一個不帶產品速率的正規化核對：把 HBM4 對應路徑的每線速率設為
1 個教學單位，SPHBM4 主機側每線就是 4 個單位。這裡的 1 不是 1 GT/s，也不是任何產品時脈；
它只用來確認「線數減為四分之一、每線速度變成四倍」在 raw 層是否仍能守住相同乘積。

| 公開架構的正規化讀法 | 主機側資料訊號 | 每線速率指數 | raw throughput 指數 | 這一列沒有回答什麼 |
|---|---:|---:|---:|---|
| HBM4 對應資料路徑 | 2,048 | 1 | 2,048 | payload、延遲、錯誤、功耗與封裝幾何 |
| SPHBM4 主機側映射 | 512 | 4 | 2,048 | 實際 GT/s、控制開銷、良率、成本與產品效能 |

因此資料訊號數機械上減少 75%，每線速率提高為 4 倍，raw throughput 指數比例仍是 1。這個
等式只證明 JEDEC 公開架構的算術一致，不會自動證明兩條路徑的有效資料吞吐、讀寫等待、功耗、
可靠度或完整產品成本相同。

### 同一個 raw，payload 與每位元能耗仍可分岔

OCP 的 D2D PHY 指標白皮書把每線速率、Rx 加 Tx 的 PHY bandwidth、PHY power efficiency、
shoreline density、reach、BER 與 latency 分開。以下再做兩個匿名的假想實作，刻意固定同口徑
Rx 加 Tx raw bandwidth 為 2,048 Gbps；它們不是 HBM4 與 SPHBM4 的比較，也不是 JEDEC、
Eliyan 或任何記憶體產品數字。

本文另設一個教學用 payload 保留比例 η，把真正送達的有效資料除以 raw bandwidth；η 會把控制
資訊、閒置與重試等結果合在一起，只為展示分母，不是 OCP 或 JEDEC 規定的單一標準欄位。

| 匿名假想實作 | 同口徑 Rx＋Tx raw bandwidth | 教學用 η | payload goodput | Tx＋Rx＋clock power | OCP 口徑 pJ／raw bit | pJ／useful bit |
|---|---:|---:|---:|---:|---:|---:|
| 甲 | 2,048 Gbps | 95% | 1,945.6 Gbps | 12,288 mW | 6.000000 | 6.315789 |
| 乙 | 2,048 Gbps | 80% | 1,638.4 Gbps | 16,384 mW | 8.000000 | 10.000000 |

兩列 raw 完全相同，乙的 payload goodput 卻比甲低 15.789474%；以 OCP 的 unit power ÷ unit
bandwidth 量綱核對，乙的 pJ／raw bit 高 33.333333%，改用有效資料作分母後則高 58.333333%。
這不表示真實 SPHBM4 會落在任一列；它只說明「同頻寬」至少要追問 raw 還是 payload，以及
功率分子是否包含相同的 Tx、Rx、clock、工作模式與資料型態。

### 延遲與 BER 要先固定量測點

OCP 白皮書沒有把一個 latency 或 BER 數字用到底。它把資料路徑切成至少三個量測層級；後一層
可能包含更多錯誤處理，也可能需要不同的測試輸入與曝光時間。

| OCP 量測層 | 起點與終點 | 延遲欄位 | BER 欄位 | 讀者要保留的邊界 |
|---|---|---|---|---|
| Serializer → Deserializer | 序列器輸入到解序列器輸出 | T0 | BL0 | 排除 clock-domain crossing elastic buffer，不是完整記憶體存取 |
| Packet／FEC／CRC → Packet／FEC／CRC | 把封包與錯誤偵測／更正區塊納入 | T1 | BL1 | 要同時固定資料率、FEC／CRC 與處理範圍 |
| CRC＋Retry | 再把錯誤偵測後的重傳納入 | 白皮書摘要表不給單一 latency 欄 | BL2 | 必須另留 retry policy、事件數、暴露 bit／時間與尾端延遲 |

所以「BER 更低」要先問是 raw error、FEC 後、CRC 未更正錯誤，還是重試後的服務結果；「延遲
更低」也要先問量到 PHY、packet、memory controller、DRAM core 還是應用。沒有共同起終點、
資料型態、lane 方向、速率、錯誤機制、測試時間與環境，兩個數字不具可比性。

### 512 條資料訊號也不能直接算 shoreline density

OCP 把 PHY bandwidth per shoreline、packaging type、minimum bump pitch 與 reach 分開列欄。
這提醒我們：頻寬密度的分母是實際晶粒邊緣寬度，不是資料訊號數；512 也不是總接點數。要重算
Tbps/mm，還要知道 Tx／Rx 方向、data／clock／sideband／power／ground 配置、bump map、pitch、
可堆疊單元與占用 beachfront。JEDEC 接點附錄尚未公開時，這些幾何不能用猜的。

Eliyan 現行 NuLink-SP 產品表已把 process node、lane、per-lane rate、beachfront／area bandwidth
與 reach 分開，這證明實作者知道不能只報 aggregate bandwidth；但它仍是單一供應商對相鄰 D2D
產品家族的自報表，不能因欄位看起來相似，就改寫成 JESD330-4 compliance、具名 SPHBM4 memory
或跨廠客戶測試。

### 多空小作文共用的 SPHBM4 PHY 十欄護照

| 護照欄位 | 至少要固定什麼 | 少了最容易誤讀成什麼 |
|---|---|---|
| 1. 標準與產品身分 | JESD330-4、JESD330-4-1 版本，memory／base die／host PHY／package／system 版本 | 主標準發布等於接點、產品與客戶都完成 |
| 2. 方向與通道 | Tx／Rx、單向／半雙工／同時雙向、16-bit channel mapping、同步與排程 | 單向、雙向 aggregate 與讀寫頻寬可以直接互換 |
| 3. lane、wire 與 pin | data lane、single-ended／differential wire、clock、sideband、command、power、ground 與 spare | 512 data signals 等於整顆只有 512 個接點 |
| 4. 每線與 raw | data rate per lane、lane 數、方向、raw 計算式與量測速率 | 4 倍每線速率自動得到 4 倍系統效能 |
| 5. payload 與工作負載 | 有效資料定義、read／write 比、burst、idle、overhead、retry 與 memory pattern | raw bandwidth 等於應用 goodput 或模型加速 |
| 6. latency measurement point | T0／T1、controller／DRAM／application 起終點、平均與 tail、clock buffer inclusion | 一個 ns 可以替整條記憶體存取路徑背書 |
| 7. BER 與恢復 | raw／FEC 後／CRC／retry 後、事件與 bit／時間暴露、pattern、溫度、電壓、lane 分布 | 零觀察錯誤等於 BER 為零或可靠度已通過 |
| 8. power 與 energy | Tx＋Rx＋clock／controller／base die 範圍、工作模式、溫度、raw 或 useful-bit 分母 | 接點少就一定省電、較高 pJ/bit 就一定使產品失敗 |
| 9. 幾何、封裝與 reach | bump map、pitch、shoreline、area、材料、層疊、路長、損耗、阻抗、電源與熱 | 有機基板一定較便宜、較長通道一定可放更多記憶體 |
| 10. silicon 到財務 | process、test chip、memory sample、跨廠互通、可靠度、客戶 qualification、良率、成本、量產與收入 | 一家 PHY 供應商頁面等於台灣基板、矽智財或封測訂單 |

較強的多方版本不是「2,048 變 512，所以成本一定大降」，而是同一具名產品在相同版本與工作
負載下，仍守住 payload、延遲、BER、功耗與熱，並把較鬆接點和有機基板路徑轉成可重複的良率、
合格產出、成本與客戶資格；供應商還要能對上同一產品與財務分子。

較強的空方版本也不是「每線快四倍，所以 SPHBM4 一定失敗」，而是同一產品的高速通道、較長
reach、base-die 邏輯、錯誤恢復、供電與熱代價，實測上侵蝕 payload 或產品裕量，且在多片 wafer／
lot、可靠度與成本後無法守住目標。兩邊都必須交同一張護照，不能一邊只談接點，另一邊只談
PHY 風險。

### 分母、誤差與限制

第一個教材是 N＝2 種公開架構映射的固定輸入換算；第二個教材是 N＝2 個匿名假想 PHY 實作。
Python Fraction 與獨立 awk 在顯示精度內完全一致。這些都是確定性算術，不是抽樣、silicon
量測、JEDEC compliance、封裝實驗、記憶體 benchmark 或客戶資料，因此沒有 sampling SE／t，
也沒有真實 GT/s、payload、BER exposure、latency distribution、pJ/bit、die／wafer／lot、良率、
可靠度、成本、需求、收入、毛利或公司效果。

JEDEC、OCP 與 Eliyan 是標準組織、通用量測方法與單一供應商三條不同消息鏈，不是三個獨立
SPHBM4 產品、客戶或量產 run。OCP 官方 PDF 共 44 頁；實際引用 file pp.33–41，連同相鄰頁
pp.32–42 已由官方瀏覽器 PDF viewer 逐頁渲染目視核對。命令列與 web screenshot 端點回 403，
因此不宣稱本地檔案 SHA；published_at 只依官方檔名的 NOV_19_2024 正規化，不主張正文另有日精度。

## 先看難題從哪裡搬到哪裡

接點變少只回答「主機側要拉多少條資料線」，沒有回答整體產品是否更省電、更可靠、更好製造或
更便宜。以下五項是本文整理標準與既有產品資料的閱讀問題，不是完整電氣規格，也不是兩種路徑
的效能、成本或投資排名。

| 本文五項接力問題 | 原路徑較難的地方 | 新路徑把壓力移到 | 主要接力角色 | 本輪可確認到哪裡 |
|---|---|---|---|---|
| 1. 接點與扇出 | 主機側要處理 2,048 個資料訊號，高密度接點與佈線壓力大 | 資料訊號減為 512 個，但電源、接地、命令與時脈接點仍存在 | 底部介面晶片、封裝與基板 | 標準公告確認資料訊號數；沒有總接點數、面積與成本資料 |
| 2. 每線速度與訊號品質 | 很多平行資料線要在短距離內同時到達 | 四條合成一條後，每條線要跑得更快；較長通道還要處理損耗、反射、雜訊與時序 | 高速介面、底部介面晶片與基板 | 標準公告確認四比一序列化；沒有共同條件下的錯誤率或訊號品質實測 |
| 3. 功耗、延遲與熱 | 高密度介面與記憶體堆疊本來就要共同供電和散熱 | 新增高速轉換、時脈與控制邏輯後，要重算每次傳輸耗能、等待時間與熱點 | 邏輯設計、供電、散熱與系統角色 | 公開資料沒有量化新舊路徑的系統功耗、延遲或溫度 |
| 4. 材料、組裝與良率 | 既有高密度連線通常依賴矽基封裝路徑 | 有機基板成為可選路徑，但材料、線路、接合、可靠度與良率都要重新驗證 | 基板材料、封裝、測試與記憶體製造 | 標準只寫標準有機基板；沒有指定材料、供應商、良率或量產線 |
| 5. 系統容量與配置 | 記憶體堆疊的位置與數量受封裝空間和連線距離限制 | 較長通道可能增加配置彈性，但控制器、功耗、散熱與封裝尺寸仍可能成為限制 | 記憶體、運算晶片、系統與客戶 | 標準組織只說「可能」容納更多堆疊；沒有具名產品配置或運行結果 |

## 再把五組角色接力放回正確位置

新路徑不是把有機基板換上去就結束。每一組角色都要把電氣、熱、製造與驗證條件交給下一組；
下表只說明責任與本輪證據停點，不代表已具名供應商、訂單或收入。

| 接力角色 | 要交付什麼 | 要和下一角色說清楚 | 本輪證據 | 不能外推 |
|---|---|---|---|---|
| 記憶體裸晶與堆疊 | 提供容量、速度、供電與可堆疊的記憶體結構 | 裸晶介面、層數、測試、熱與可靠度邊界 | 標準沿用同一世代記憶體裸晶 | 既有裸晶可不經修改直接形成量產產品，或所有記憶體廠都會採用 |
| 底部介面晶片與高速介面 | 把大量平行資料轉成較少的高速訊號，並處理時脈、控制與錯誤 | 每線速率、功耗、延遲、時序、錯誤率與製程 | 標準定義四比一序列化與介面角色 | 晶片已設計完成、已選定晶圓代工、介面供應商或商業模式 |
| 有機基板與材料 | 在較長路徑上扇出高速訊號、命令與電力 | 材料損耗、線路、阻抗、過孔、電源完整性與可靠度 | 標準允許使用標準有機基板 | 一定採用 ABF 或 BT，或特定台灣基板公司已被選中 |
| 封裝、測試與熱管理 | 把堆疊、介面晶片與基板組裝成可測、可散熱的產品 | 接合、測試覆蓋、錯誤定位、良率、溫度與返修條件 | 只形成封裝與測試的搜尋入口 | 外部封測廠必然承接、製造良率已改善或成本已下降 |
| 運算晶片、系統與客戶 | 整合控制器與完整記憶體配置，執行工作負載和資格認證 | 裝置介面、容量配置、功耗預算、軟體、測試條件與通過標準 | 本輪沒有具名加速器、系統或客戶採用 | 標準存在就能部署，或規格可直接換算滲透率、訂單與收入 |

## 最後用七關判斷標準能不能變成收入

後一關需要新的實體與客戶證據，不能因為標準已發布，就把晶片、樣品、系統、客戶與量產一起
補成完成。這是本文的追蹤順序，不是公司快慢或技術價值排名。

| 本文七關 | 這一關要證明 | 本輪已有證據 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 主標準發布 | 多方已有共同的記憶體、base die 與主機通道規則 | JESD330-4 Version 1.0 已發布，公開摘要列出四比一通道轉換與有機基板路徑 | 完整規格的公開可定位條文或正式版本變更 | 已有封裝接點圖、產品、互通、成本優勢或供應商訂單 |
| 2. 封裝接點契約公開 | 實作者可以對上同一版接點、命令、時脈、電源與接地配置 | JEDEC 頁面列出 JESD330-4-1 bump-map addendum，但仍只供會員 | 董事會核准後的公開 addendum、版本與變更紀錄 | addendum 尚未公開等於技術失敗，或任一基板商已取得量產規格 |
| 3. 介面晶片與主機 PHY 完成 | 轉換與主機端邏輯已被設計、製造並可測 | Eliyan 宣稱 NuLink-SP 對應 SPHBM4；尚無本輪可核對的 compliance 或 silicon 結果 | 具名 base die／host PHY、製程、datasheet、功耗、延遲、錯誤率與版本 | 一家供應商的產品定位等於記憶體廠採用、跨廠互通或任一台灣設計服務公司得單 |
| 4. 記憶體與封裝樣品完成 | 裸晶、介面晶片、基板與封裝能組成可測產品 | 本輪沒有完成證據 | 具名樣品、容量、速度、材料、熱、良率與可靠度結果 | 路線可行就等於樣品已交付或成本較低 |
| 5. 運算晶片與系統整合 | 主機端能控制新記憶體並完成目標工作負載 | 本輪沒有完成證據 | 具名運算晶片、控制器、系統、配置與端到端實測 | 單一展示板等於可部署產品或所有平台都適用 |
| 6. 客戶資格與可靠度通過 | 客戶依指定產品、版本與條件完成長期驗證 | 本輪沒有完成證據 | 客戶名稱、測試條件、錯誤率、可靠度與通過結果 | 開始測試就等於通過，或單一客戶代表整個市場 |
| 7. 穩定量產與形成收入 | 良率、出貨與重複採購能持續，財務上可辨認同一產品 | 本輪沒有完成證據 | 穩定良率、量產出貨、重複訂單與可辨識收入 | 標準或產業總營收等於台灣公司已受惠 |

## 把「標準存在」拆成四條時鐘

- **既有第四代高頻寬記憶體**：Micron 2026-06-24 表示產品已對主力客戶平台大量出貨，並向多個終端客戶提供認證樣品；這是公司對既有路徑的正式披露，不證明採用新標準。
- **既有強化版本**：Micron 把 HBM4E 量產預期放在 2027 年；SK hynix 2026-06-18 宣布送出 12 層 HBM4E 樣品。前者是未來時程，後者是樣品，兩者都不等於 SPHBM4。
- **SPHBM4 公開文件**：JESD330-4 Version 1.0 已發布，公開摘要足以確認四層架構；但 JESD330-4-1 bump-map addendum 截至 2026-08-12 仍只供 JC-42 會員，等待董事會核准後公開。
- **介面供應商與完整產品**：Eliyan 已把 NuLink-SP 定位為 SPHBM4 PHY 路徑，但本輪沒有 compliance report、具名 memory／base-die／host-PHY silicon 組合、跨廠互通、記憶體樣品或運算平台採用。

因此不能用「新標準已發布」覆蓋「既有產品已在出貨」的現實。較合理的基準情境是：既有路徑
繼續服務近期平台；新路徑則分別追主標準、接點附錄、介面晶片、記憶體、系統與客戶，不能把
任一較快的時鐘當成其餘時鐘已完成。

## 來源與證據邊界

- [JEDEC：JESD330-4 SPHBM4 標準，2026-07-13](https://www.jedec.org/news/pressreleases/new-jedec%C2%AE-sphbm4-standard-enables-hbm4-class-bandwidth-organic-substrates)
- [JEDEC：JESD330-4 Version 1.0 與 bump-map addendum 現況](https://www.jedec.org/standards-documents/docs/jesd330-4)
- [Eliyan：NuLink-SP 標準有機封裝 D2D PHY 產品頁](https://eliyan.com/products/)
- [Eliyan：NuLink-SP 與 SPHBM4 官方公司貼文](https://www.linkedin.com/posts/eliyan-corporation_hbm4-and-sphbm4-scaling-memory-bandwidth-activity-7447249719749156864-xvXH)
- [Open Compute Project：Electrical Interfaces Performance Metrics](https://www.opencompute.org/documents/odsa-whitepaper-2024-electrical-interfaces-performance-metrics-nov-19-2024-docx-pdf)（一般 D2D PHY 量測方法，不是 SPHBM4 規格或產品成績）。
- [Micron：2026 財年第三季產品進度，2026-06-24](https://investors.micron.com/node/50671)
- [SK hynix：12 層 HBM4E 樣品，2026-06-18](https://news.skhynix.com/en/12-layer-hbm4e-sample-1/)

**已知：** SPHBM4 的 DRAM 堆疊、base die、獨立分散式通道與有機封裝方向已成為 JEDEC 標準；bump-map addendum 尚待公開核准；Eliyan 已宣稱具名 PHY 路徑；傳統 HBM4 已有記憶體供應商宣稱大量出貨。

**還不知道：** 公開核准 bump map、第一個符合相同版本的 SPHBM4 記憶體產品、加速器客戶、base-die 與 host-PHY 組合、跨廠互通、封裝商、基板材料、認證時程，以及相對傳統 HBM4 的成本、功耗、延遲、良率與可靠度。

**不可外推：** 「標準有機基板」不能直接等同 ABF 或 BT，也不能指定欣興、景碩、南電；「HBM4 級頻寬」是 JEDEC 的架構敘述，不是公開系統 benchmark。沒有價格、估值、共識與部位資料，本題不判斷市場是否已反映。

## 影響路由

本題只做**低信心族群 watch**，不列個股。方向是價值可能重新分配，而不是整條鏈一致受惠。

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-26
rationale: SPHBM4 明確把介面導向標準有機基板，可能改變高階基板需求；但 bump-map addendum 尚未公開，也沒有材料規格、供應商、客戶或量產。
evidence_boundary: JEDEC 未指定 ABF或BT，也未列名3037、3189、8046；只構成族群搜尋觸發。
-->

<!-- impact
group_id: ipdesign
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-26
rationale: 新 interface base die、獨立主機通道與高速序列化提高邏輯設計重要性；Eliyan 已提出具名 PHY 路徑，但沒有 compliance、記憶體採用或台灣公司商業角色。
evidence_boundary: 不能把需要base die或單一海外供應商產品定位自動映射成任一台灣ASIC設計服務或高速介面公司訂單。
-->

<!-- impact
group_id: packtest
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-26
rationale: 從矽基高密度路徑轉向有機基板可能改變接點圖、組裝與測試流程，但公開 addendum、封裝商、良率與量產線證據仍未閉合。
evidence_boundary: 記憶體供應商具自有封裝能力，標準發布不等於外部OSAT承接；不列個股。
-->

## 下一個可證明／否定的節點

- **公開實作契約**：JEDEC 公開董事會核准的 JESD330-4-1 bump-map addendum，並可核對版本與變更；未公開前，不把資料訊號數轉成完整接點與基板規格。
- **產品化**：任一記憶體廠公布符合具名 JESD330-4／addendum 版本的 SPHBM4 樣品、base die、host PHY、容量、速度與量產時程；若未出現，維持標準與供應商路徑觀察。
- **客戶採用**：任一加速器或系統廠具名採用 JESD330-4，並說明傳統 HBM4 與 SPHBM4 的使用場景；沒有具名客戶，不談滲透率。
- **工程裁決**：公開功耗、延遲、bit error rate、封裝面積、良率與可靠度。若序列化與長通道代價抵銷基板優勢，快速採用假說被否定。
- **台灣映射**：只有當正式文件列出基板種類、認證與供應者，才把族群 watch 升成個股 review；未列名之前，3037／3189／8046 不進 metadata。
