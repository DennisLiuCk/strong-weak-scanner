# AI 基建支出續增、自由現金流卻分化：三家雲端巨頭不能只比 CapEx 標題

<!-- research_topic
topic_id: MI-2026-08-01-AI-CAPEX-CASH-CONVERSION
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-07-29
last_reviewed_at: 2026-08-01
review_due: 2026-08-15
source_type: mixed
publisher_domain: microsoft.com
canonical_url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
source_chain_id: hyperscaler-capex-cash-conversion-20260729-30
stock_ids:
group_ids: serverodm,pcb,powersupply,thermal
trigger_type: earnings_release
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C2
base_confidence: medium
confidence_basis: 三家公司官方數字與公式可回溯，但期間和定義不同且台灣供應鏈映射未證
cross_company_numbers: true
schema_migrated_at: 2026-08-02
-->

<!-- transition
date: 2026-08-01
from: initial
to: inbox
reason: hyperscaler_cash_and_capex_disclosures_captured
evidence: source_chain:hyperscaler-capex-cash-conversion-20260729-30
-->

<!-- research_source
source_id: S1
role: company_release
publisher: Microsoft
title: Microsoft FY2026 Q4 earnings call 與財務表
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
locator: capital expenditures、cash flow、Azure demand 與 useful-life 段落
limitation: CapEx 包含現金購置與 finance leases，且沒有完整拆分 AI 晶片、建物與網路設備
-->

<!-- research_source
source_id: S2
role: company_release
publisher: Meta Platforms
title: Meta 2026 Q2 results
published_at: 2026-07-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx
locator: cash flow、capital expenditures 與 2026 outlook 表格
limitation: 公司自訂 FCF 公式含 finance-lease principal，不能直接套用到同業
-->

<!-- research_source
source_id: S3
role: company_release
publisher: Amazon
title: Amazon 2026 Q2 results
published_at: 2026-07-30
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx
locator: trailing twelve months cash flow、PP&E 與 AWS results 表格
limitation: 核心現金流資料是 TTM 而非單季，淨 PP&E 公式也不同於 Microsoft 與 Meta
-->

<!-- research_source
source_id: S4
role: company_filing
publisher: Meta Platforms
title: Meta 2025 Form 10-K
published_at: 2026-01-29
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm
locator: useful lives of servers and network equipment 會計估計段落
limitation: 會計估計變更影響折舊與淨利，不直接衡量 AI 投資報酬率
-->

<!-- research_source
source_id: S5
role: company_filing
publisher: Amazon
title: Amazon 2025 Form 10-K
published_at: 2026-02-06
captured_at: 2026-08-01
accepted_at: 2026-08-01
status: active
url: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm
locator: useful life change for servers and networking equipment 段落
limitation: 折舊年限變更不等於實際伺服器汰換速度或 AI ROI 排名
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
locator: 台灣 ODM、PCB、電源與散熱公司季報、法說及重大訊息查找入口
limitation: 買方 CapEx 只能觸發此入口的公司級查找；入口本身不證明訂單、收入或毛利
-->

<!-- research_source
source_id: S7
role: company_filing
source_kind: document
publisher: Meta Platforms
title: Meta Platforms 2026 Q1 Form 10-Q
published_at: 2026-04-30
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm
locator: Note 6 Property and Equipment 的 construction in progress 與 held-for-sale assets；Note 8 尚未起租的租賃及 contractual commitments
limitation: 申報把承諾 在建工程與待售資產分開，但沒有逐批 placed-in-service 日期 使用率 AI 專屬資產分子或台灣供應商對應
independence_group: meta
-->

<!-- research_source
source_id: S8
role: company_filing
source_kind: document
publisher: Amazon
title: Amazon 2026 Q1 Form 10-Q
published_at: 2026-04-30
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm
locator: supplemental cash-flow information 的 acquired but not yet paid；Note 1 AWS performance obligations 與 revenue timing；segment PP&E net additions
limitation: Amazon 的資產增加與履約義務是公司級口徑，沒有把同一資產批次連到 AI 使用量 邊際收入 現金回收或台灣供應商
independence_group: amazon
-->

<!-- research_claim
claim_id: C1
label: verified
status: active
claim: Microsoft、Meta 與 Amazon 各自揭露的 CapEx 或 PP&E、OCF 與 FCF 可依各公司公式回溯
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-30
basis: 三家公司官方財務表提供各自數字與非 GAAP 公式
boundary: 可回溯只代表公司內部公式一致，不代表三家公司之間具有相同期間或定義
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C2
label: inference
status: active
claim: 三家公司 headline CapEx 或 PP&E 數字不能直接橫向排名 AI 投資強度或現金回收效率
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-30
basis: Microsoft 與 Meta 是單季、Amazon 是 TTM，且現金購置、租賃本金與淨 PP&E 定義不同
boundary: 這是可比性判定，不是三家公司 AI ROI、估值或投資優劣排名
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C3
label: verified
status: active
claim: 三家公司仍揭露 AI 或雲端基礎建設投入與需求成長訊號，但現金回收表現分化
supporting_source_ids: S1,S2,S3
contrary_source_ids:
as_of: 2026-07-30
basis: 官方資料同時揭露資本投入、Azure 或 AWS 成長、需求與自由現金流
boundary: 需求成長與 FCF 分化可以同時成立，不能由單一季度推定長期投資報酬率
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C4
label: verified
status: active
claim: Microsoft、Meta 與 Amazon 的資產耐用年限或租賃分類變更會改變折舊、CapEx 或淨利呈現
supporting_source_ids: S1,S4,S5
contrary_source_ids:
as_of: 2026-07-29
basis: 公司法說與 10-K 直接揭露會計估計變更及其財務影響
boundary: 會計呈現變化不等於實際建置意圖、設備物理壽命或 AI ROI 同幅改變
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C5
label: unverified
status: active
claim: 雲端巨頭整體 CapEx 可直接換算成任一台灣 ODM、PCB、電源或散熱公司的訂單與獲利
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-01
basis: 買方揭露沒有提供台灣供應商、料號、採購份額、上線時程或毛利資料
boundary: 目前只建立族群需求搜尋觸發，不建立任何個股收入、市占或獲利事實
verification_needed: 需要雲端客戶與台灣供應商文件雙向核對產品、時程、數量與財務貢獻
resolution:
-->

<!-- research_claim
claim_id: C6
label: inference
status: active
claim: 要把雲端買方 AI CapEx 連到台灣供應商財務，至少要分開資本承諾、現金與租賃支出、資產建置與試運轉、可用容量、工作負載與收入、買方現金回收、供應商財務歸因七道證據閘門
supporting_source_ids: S1,S2,S3,S4,S5
contrary_source_ids:
as_of: 2026-08-12
basis: 三家公司揭露把支出、租賃、雲端需求、FCF 與折舊政策放在不同表格和期間；逐站分開可避免把會計分類、資產上線與供應商受惠合併成同一結論
boundary: 七關是研究與對帳框架，不代表三家公司都已逐關揭露，也不證明任一台灣供應商已取得訂單、收入、毛利或現金
verification_needed: 需要買方與供應商以同一平台、料號、期間、數量與公司財務分母雙向核對
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: Meta 2026 Q1 申報分別揭露尚未起租的資料中心等租賃 在建工程中的資料中心 網路與伺服器成本，以及轉為待售的資料中心在建工程與土地
supporting_source_ids: S7
contrary_source_ids:
as_of: 2026-04-30
basis: S7 的 Note 6 與 Note 8 直接把 lease not yet commenced construction in progress 及 held-for-sale assets 分列
boundary: 只證明 Meta 報表中的不同資產與承諾狀態；不代表所有承諾都會取消，也不提供逐批上線 使用率 收入或供應商分子
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: Amazon 2026 Q1 申報明示 PP&E 淨增加包含已取得但尚未付款的非現金活動，而 AWS 未認列的未來服務承諾要依客戶使用與公司履約決定收入時點
supporting_source_ids: S8
contrary_source_ids:
as_of: 2026-04-30
basis: S8 的 supplemental cash-flow information segment PP&E 與 performance obligations 段落分別界定資產增加 付款及收入認列時點
boundary: 只證明 Amazon 報表裡三個時點可以分離；不表示任何特定 AI 專案的資產 客戶使用 收入與現金已完成逐筆配對
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: 閱讀 AI 基建投入至少要同時保留合約承諾 資產可用 客戶使用與收入認列 現金支付與回收四個獨立時鐘；任一時鐘前進都不能代替另外三個
supporting_source_ids: S1,S2,S3,S7,S8
contrary_source_ids:
as_of: 2026-08-12
basis: S1 至 S3 已把 headline CapEx cash PP&E 租賃 OCF 與 FCF 分開；S7 再分開未起租承諾 在建工程與待售；S8 又分開資產取得但未付款以及依使用與履約認列收入
boundary: 四時鐘是跨申報建立的研究對帳框架，不是所有公司的共同會計科目，也不證明任一台灣供應商訂單 收入 毛利 現金或投資報酬
verification_needed: 需要同一具名資產或平台批次的合約生效 placed-in-service 使用與收入 付款及供應商收款日期才能量出各時鐘的實際落差
resolution:
-->

<!-- metric_comparison
comparison_id: M1
observation_id: M1-O1
claim_id: C2
entity: Microsoft
metric: reported capital expenditure or PP&E
reported_value: 41.0
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal quarter
unit: USD billion
definition_key: headline_capex_including_finance_leases
definition: 公司 headline CapEx，包含 cash paid for PP&E 與 finance leases
evidence_ids: S1
comparability: not_comparable
comparability_reason: 與 Meta 的租賃本金公式及 Amazon 的 TTM 淨 PP&E 期間和口徑不同
normalization_method:
normalized_value:
normalized_unit:
-->

<!-- metric_comparison
comparison_id: M1
observation_id: M1-O2
claim_id: C2
entity: Meta Platforms
metric: reported capital expenditure or PP&E
reported_value: 31.08
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: calendar quarter
unit: USD billion
definition_key: cash_ppe_plus_finance_lease_principal
definition: cash paid for PP&E 加 finance-lease principal payments
evidence_ids: S2
comparability: not_comparable
comparability_reason: 雖與 Microsoft 同為單季，租賃與 FCF 定義不同，亦不同於 Amazon TTM 淨 PP&E
normalization_method:
normalized_value:
normalized_unit:
-->

<!-- metric_comparison
comparison_id: M1
observation_id: M1-O3
claim_id: C2
entity: Amazon
metric: reported capital expenditure or PP&E
reported_value: 169.007
period_start: 2025-07-01
period_end: 2026-06-30
period_basis: trailing twelve months
unit: USD billion
definition_key: net_cash_ppe_after_sales_and_incentives
definition: PP&E purchases 扣除出售與設備 incentives 的 TTM 淨額
evidence_ids: S3
comparability: not_comparable
comparability_reason: 資料為 TTM、未另扣 finance-lease principal，不能和兩家單季 headline 直接排名
normalization_method:
normalized_value:
normalized_unit:
-->

<!-- metric_comparison
comparison_id: M2
observation_id: M2-O1
claim_id: C2
entity: Microsoft
metric: operating cash flow
reported_value: 55.4
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal quarter
unit: USD billion
definition_key: issuer_reported_net_cash_from_operations
definition: 公司財務表揭露的單季營業活動現金流量淨額
evidence_ids: S1
comparability: not_comparable
comparability_reason: Microsoft 與 Meta 為單季但財務季口徑不同，Amazon 則為 TTM，不能直接排現金產生能力
-->

<!-- metric_comparison
comparison_id: M2
observation_id: M2-O2
claim_id: C2
entity: Meta Platforms
metric: operating cash flow
reported_value: 31.862
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: calendar quarter
unit: USD billion
definition_key: issuer_reported_net_cash_from_operations
definition: 公司財務表揭露的單季營業活動現金流量淨額
evidence_ids: S2
comparability: not_comparable
comparability_reason: Microsoft 與 Meta 為單季但財務季口徑不同，Amazon 則為 TTM，不能直接排現金產生能力
-->

<!-- metric_comparison
comparison_id: M2
observation_id: M2-O3
claim_id: C2
entity: Amazon
metric: operating cash flow
reported_value: 161.403
period_start: 2025-07-01
period_end: 2026-06-30
period_basis: trailing twelve months
unit: USD billion
definition_key: issuer_reported_net_cash_from_operations
definition: 公司財務表揭露的過去十二個月營業活動現金流量淨額
evidence_ids: S3
comparability: not_comparable
comparability_reason: Amazon 是 TTM，另外兩家是單季；期間未對齊前不能用金額高低判斷回收效率
-->

<!-- metric_comparison
comparison_id: M3
observation_id: M3-O1
claim_id: C2
entity: Microsoft
metric: issuer-defined free cash flow
reported_value: 19.6
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: fiscal quarter
unit: USD billion
definition_key: ocf_minus_cash_paid_for_ppe
definition: 單季 OCF 減 cash paid for PP&E，不直接扣 headline finance leases
evidence_ids: S1
comparability: not_comparable
comparability_reason: Meta 另扣 finance-lease principal，Amazon 又是 TTM 淨 PP&E；公式與期間均不同
-->

<!-- metric_comparison
comparison_id: M3
observation_id: M3-O2
claim_id: C2
entity: Meta Platforms
metric: issuer-defined free cash flow
reported_value: 0.784
period_start: 2026-04-01
period_end: 2026-06-30
period_basis: calendar quarter
unit: USD billion
definition_key: ocf_minus_cash_ppe_minus_finance_lease_principal
definition: 單季 OCF 減 cash paid for PP&E，再減 finance-lease principal payments
evidence_ids: S2
comparability: not_comparable
comparability_reason: Microsoft 未用相同方式扣租賃本金，Amazon 又是 TTM 淨 PP&E；不能做 FCF 高低榜
-->

<!-- metric_comparison
comparison_id: M3
observation_id: M3-O3
claim_id: C2
entity: Amazon
metric: issuer-defined free cash flow
reported_value: -7.604
period_start: 2025-07-01
period_end: 2026-06-30
period_basis: trailing twelve months
unit: USD billion
definition_key: ocf_minus_net_cash_ppe_after_sales_and_incentives
definition: TTM OCF 減 PP&E purchases，再加回出售與設備 incentives
evidence_ids: S3
comparability: not_comparable
comparability_reason: Amazon 是 TTM 且公式不同，不能和 Microsoft、Meta 的單季公司定義 FCF 排名
-->

<!-- monitoring_item
monitor_id: T1
status: active
claim_ids: C1,C2,C4
metric: 三家公司 cash PP&E、finance leases、租賃本金、折舊政策與 FCF 公式
source_ids: S1,S2,S3,S4,S5
watch_source_ids: S6
frequency: quarterly
frequency_detail: 每季財報與重大會計政策更新
next_check: 2026-08-15
trigger: 公司首次提供可對齊的單季現金購置、租賃增加與本金付款橋接表
invalidation: 若未先完成期間與定義正規化，任何跨公司 CapEx 或 FCF 高低排名均視為無效
-->

<!-- monitoring_item
monitor_id: T2
status: active
claim_ids: C3,C5
metric: AI 基礎設施投入、上線容量、雲端營收利用率與供應商財務貢獻
source_ids: S1,S2,S3,S6
watch_source_ids: S6
frequency: quarterly
frequency_detail: 每季法說與財報
next_check: 2026-10-31
trigger: 支出增加後出現可核對的容量上線、使用率、營收與毛利改善，或台灣供應商直接揭露訂單
invalidation: 若投入未轉為容量、需求與現金回收，或供應商文件無法雙向核對，受惠論維持未證
-->

<!-- transition
date: 2026-08-01
from: inbox
to: triaged
reason: periods_definitions_and_supplier_mapping_reviewed
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
reason: editorial_plain_language_wave8_learning_no_conclusion_change
evidence: editorial:plain_language_wave8
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: capex_to_supplier_financial_bridge_synthesized_from_existing_disclosures
evidence: sources:S1,S2,S3,S4,S5
-->
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: four_accounting_clocks_added_from_meta_and_amazon_filings_without_refreshing_thesis_clock
evidence: sources:S7,S8
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CapEx（資本支出）**：買進或建造可使用多年的資產，例如資料中心、伺服器與網路設備；公司對 CapEx 的揭露可能含現金購置、融資租賃或兩者。
- **PP&E（不動產、廠房及設備）**：資產負債表上的長期實體資產類別；「cash paid for PP&E」是期間現金流，「PP&E 餘額」是某一時點仍留在帳上的資產，兩者不是同一個數字。
- **在建工程（CIP）**：仍在施工、安裝或測試，通常還沒準備好按預定方式使用的資產；預算已花不代表它已能提供雲端容量。
- **尚未起租的租賃（lease not yet commenced）**：合約已簽，但租期與資產使用權尚未開始；承諾金額不等於當期 CapEx、現金付款或可用容量。
- **試運轉／啟用（commissioning／placed in service）**：設備完成通電、測試與驗收，轉成可使用資產的交接點；它不自動代表客戶已把容量用滿。
- **利用率（utilization）**：可用容量實際被工作負載使用的程度；若沒有共同分母、時間窗和產品範圍，不同公司利用率不能直接比較。
- **營業現金流（OCF）**：本業在一段期間內帶進或用掉的現金，會受收款、付款、預收與存貨等營運資金影響。
- **自由現金流（FCF）**：公司用營業現金流減掉某種資本支出口徑後得到的非 GAAP 指標；不同公司公式不同，不能只看同一個名稱就直接比較。
- **營運資金（working capital）**：存貨、應收、應付與預收等日常營運項目占用或釋放的資金；供應商即使已認列收入，也可能尚未收到現金。
- **存貨**：已買入或製成、但尚未完成銷售與認列成本的原料、在製品或成品；增加可能是備貨，也可能是出貨延遲，需和訂單、出貨與周轉一起看。
- **應收帳款**：已認列收入、但客戶尚未付款的金額；收入增加而應收同步拉長，不等於現金已回收。
- **供應商財務歸因**：用同一平台、產品、期間與公司分母，把客戶需求連到供應商的出貨、收入、毛利與現金；只知道買方 CapEx 不足以完成歸因。
- **履約義務（performance obligation）**：公司已承諾未來提供的服務；簽約或客戶預付不等於收入已認列，仍要看客戶使用與公司是否完成約定服務。
- **非現金資產增加**：資產已取得或記入 PP&E，但付款可能尚未發生，或由租賃等方式取得；它會讓資產時鐘早於現金時鐘。
- **融資租賃（finance lease）**：先取得資產使用權、分期付款的融資方式；它可能計入 headline CapEx，卻不在當期「cash paid for PP&E」裡一次流出。
- **耐用年限**：會計上預估資產可使用多久，決定每年折舊速度；改變耐用年限會改變損益與租賃分類，卻不一定改變實際建置計畫。
- **AWS**：Amazon Web Services，Amazon 的雲端運算事業；其營收成長不能直接分配到任一台灣供應商。
- **TTM**：Trailing Twelve Months，往回累計十二個月；它不是單季數字，與季度資料不能直接並排比較。
- **FY2026（2026 財政年度）**：公司的 2026 會計年度，起訖日不一定等於 2026 曆年；跨公司比較前要先核對涵蓋月份。
- **ROI（投資報酬率）**：投入資本後產生多少收益的比例。CapEx 或自由現金流單一數字不足以計算 AI ROI，還需要收入、成本、利用率與可比期間。

### 三句話抓重點

- 微軟 FY2026 Q4、Meta 2026 Q2 與 Amazon 2026 Q2 都顯示 AI 基建支出很強，但三家的 CapEx、租賃與 FCF 定義並不相同。
- 微軟單季仍有 196 億美元 FCF，Meta 單季只剩 7.84 億美元；Amazon 公布的是過去十二個月 FCF 流出 76.04 億美元，不能把三個數字排成簡單高低榜。
- Meta 與 Amazon 的申報再顯示，合約承諾、資產可用、客戶使用／收入與現金是四個不同時鐘；任一個前進都不能單獨證明台灣供應商訂單或投資回收。

### 為什麼重要

市場常把「四大雲端業者 CapEx 合計」當成 AI 供應鏈需求的單一溫度計，但 headline 可能混合現金購置、租賃、土地建物、CPU／GPU、網路與其他設備。若不先對齊期間與公式，CapEx 增加可能被誤讀成同幅度的晶片訂單，FCF 下降也可能被誤讀成需求崩潰。更好的方法是分開追支出、上線、營收與現金回收四個階段。

### 接下來怎麼追

- 每季同時記錄 cash PP&E、finance lease、OCF 與公司自訂 FCF，不用單一 CapEx headline 跨公司排名。
- 追新增容量是否轉為 Azure／AWS 等雲端營收、使用率與毛利，而不是只看建置承諾。
- 追台灣供應商自己的客戶認證、出貨、存貨、應收、毛利與營業現金流；只有買方支出、沒有公司級文件，不建立個股訂單事實。

### 想一想

- 如果公司只把資料中心租賃從融資租賃改成營業租賃，headline CapEx 下降但實際投資期待不變，需求應該被解讀成變弱嗎？
- 一美元 CapEx 有多少是建物、電力與網路，有多少真的變成 GPU、伺服器或台灣零組件收入？
- FCF 轉負是暫時把現金換成會產生未來收入的資產，還是需求、利用率與定價不足以回收投資；要看哪些後續數字才能分辨？

## 三家公司要先按各自口徑讀

單位為十億美元；微軟與 Meta 是截至 2026-06-30 的**單季**，Amazon 的 OCF／淨 PP&E／FCF 是截至同日的**過去十二個月（TTM）**。這張表刻意不做橫向排名。CapEx／PP&E、OCF、公司自訂 FCF 分別對應比較帳本 `M1`、`M2`、`M3`。

| 公司／期間 | 公司揭露的 CapEx 或 PP&E 口徑 | OCF | FCF | 讀法 |
|---|---:|---:|---:|---|
| Microsoft FY2026 Q4 | CapEx 41.0；其中 finance leases 5.6，cash paid for PP&E 35.8 | 55.4 | 19.6 | Headline CapEx 含租賃；FCF 反映 cash PP&E，而不是直接減掉 41.0。
| Meta 2026 Q2 | CapEx 31.08，等於 cash PP&E 30.116 加 finance-lease principal 0.962 | 31.862 | 0.784 | Meta 的 FCF 同時扣 cash PP&E 與 finance-lease principal；公司明示此非 GAAP 口徑可能與同業不同。
| Amazon 截至 2026 Q2 TTM | PP&E purchases 173.028；扣出售與 incentives 後為 169.007 | 161.403 | -7.604 | Amazon 的 FCF 公式是 TTM OCF 減淨 PP&E；這不是單季，也沒有再扣 finance-lease principal。

三家公司都能由官方表格對回各自公式，但**公式對得上不代表彼此可比**。例如 Meta 的 0.784 = 31.862 - 30.116 - 0.962；Amazon 的 -7.604 = 161.403 - 169.007。這些是會計恆等式，不是 AI 投資報酬率。

## 需求證據與回收證據要分開

### 需求仍強，有正式資料支持

- 微軟稱約三分之二單季 CapEx 用於較短耐用資產，主要是 CPU 與 GPU；Azure 成長 43%，且客戶需求仍超過可用容量。
- Meta 把 2026 全年 CapEx（含 finance-lease principal）區間收斂到 1,300–1,450 億美元，沒有下修上緣。
- Amazon 的 AWS Q2 營收年增 37%至 422 億美元；公司明言 TTM 淨 PP&E 增加主要反映 AI 投資。

以上證明三家公司仍在投入、且雲端需求有成長訊號；它們沒有回答一美元資本支出何時轉成多少增量毛利與現金。

### 現金回收已明顯分化

- 微軟在 410 億美元 headline CapEx 下仍產生 196 億美元單季 FCF。
- Meta 單季 OCF 幾乎被 cash PP&E 與租賃本金吸收，FCF 只剩 7.84 億美元。
- Amazon 的 TTM OCF 雖達 1,614 億美元，淨 PP&E 更高，因此 FCF 轉為流出；同期間 AWS 仍維持高成長。負 FCF 與需求成長可以同時存在。

所以「CapEx 高＝一定好」與「FCF 低＝需求崩潰」都太快。研究上應建立四道閘門：

1. **投入**：現金 PP&E 與租賃承諾是否真的增加。
2. **上線**：資產何時通電、認列與可供客戶使用。
3. **變現**：雲端／AI 營收、使用率、定價與毛利是否跟上。
4. **回收**：OCF、FCF 與資產報酬是否在合理時間內改善。

## 同一個資料中心有四個時鐘

七關橋接可以逐站查證；第一次閱讀時，先把資料放進四個時鐘更容易避免重複計算。四個時鐘可能互相重疊，卻不會自動同步。

| 時鐘 | 報表或文件裡會看到什麼 | 這個時鐘何時前進 | 還不能代替哪個時鐘 |
|---|---|---|---|
| 合約承諾 | 尚未起租的租賃、不可取消承諾、採購或容量合約 | 合約生效、租期開始，或承諾轉成實際採購 | 不代表資產已可用、客戶已使用或現金已全數支付 |
| 資產可用 | 在建工程、設備安裝、試運轉、轉入可使用資產 | 通電、測試、驗收並可按預定用途服務 | 不代表容量已售出、利用率足夠或收入已認列 |
| 客戶使用與收入 | 使用量、履約義務、未實現收入、服務收入與毛利 | 客戶實際使用，且公司完成合約要求的服務 | 不代表客戶已付款，也不直接等於供應商已收現 |
| 現金支付與回收 | cash PP&E、租賃本金、應付、OCF、FCF、應收與收款 | 公司支付資產款，或由營運與客戶收款帶回現金 | 不說明資產是否已上線，也不能單獨證明是哪一批設備產生現金 |

Meta 的 2026 Q1 申報提供一個很有用的反例：同一份報表同時列出尚未起租的資料中心等租賃、資料中心／網路／伺服器在建工程，以及被轉為待售的資料中心在建工程與土地。這證明「已承諾」與「仍在建」都不能自動改寫成「已提供服務」；轉為待售也提醒讀者，不是每一筆在建資本最後都照原路線上線。

Amazon 的 2026 Q1 申報則把另外兩個時差寫得很清楚：PP&E 淨增加可包含資產已取得但尚未付款的非現金活動；AWS 的未來服務承諾則要依客戶使用與公司履約決定收入認列時點。因此資產時鐘可以早於現金時鐘，合約時鐘也可以早於收入時鐘。

四個時鐘不是新的一套公司排名。真正可重算的橋接，仍要用同一具名資產或平台批次，把合約生效、轉入可使用、客戶使用與收入、付款與供應商收款日期一一對上；目前公開資料還做不到。

## 把四道閘門展成七張交接單

四道閘門適合快速閱讀；要把「大買方正在花錢」一路接到「台灣公司真的賺到錢」，則要拆成七張可以逐欄驗收的交接單。這七站是**研究順序**，不是保證每一美元都照同一天發生的物理流水線。

| 站點 | 要找的原始證據 | 這一站能證明什麼 | 還不能證明什麼 |
|---|---|---|---|
| 1. 資本計畫與承諾 | 全年 CapEx 指引、董事會預算、採購或租賃承諾 | 管理層打算配置多少資本 | 當期已付款、設備已交付或供應商已認列收入 |
| 2. 現金 PP&E 與租賃 | cash paid for PP&E、finance-lease additions／principal、其他租賃付款 | 哪部分已用現金或融資方式取得資產 | 這些支出全是 AI，也不能直接拆成 GPU、伺服器、建物或電力份額 |
| 3. 資產建置與試運轉 | 在建工程、安裝、通電、測試、驗收、placed-in-service 日期 | 資本是否從付款進到可使用資產 | 容量已對客戶開放或已有足夠工作負載 |
| 4. 服務容量可用 | 可供使用的運算、儲存、網路或電力容量與開通區域 | 系統已能承接工作負載 | 利用率、售價、營收與毛利已足以回收投資 |
| 5. 工作負載、利用與收入 | 使用量、客戶數、定價、雲端／AI 收入與毛利 | 可用容量是否轉成商業活動 | 收入增量全由本期新資產造成，或買方現金已回收 |
| 6. 買方現金回收 | 同期間 OCF、公司定義 FCF、營運資金與折舊政策 | 營運現金是否足以吸收資本投入 | 任一供應商取得多少訂單、毛利或現金 |
| 7. 供應商財務歸因 | 共同平台／料號、客戶資格、出貨期間、收入分母、毛利、存貨、應收與 OCF | 題材是否真的落到具名公司的財務結果 | 沒有雙向核對時，不能由公司總額反推單一客戶或產品貢獻 |

### 同一美元會在不同帳本、不同時間出現

「預計投入一美元」、「簽下一美元租賃」、「支付一美元 PP&E」、「把一美元資產轉入可使用狀態」、「認列折舊」、「雲端收到一美元收入」與「供應商收回一美元應收」是不同事件。把它們加總會重複計算，把其中任何一個當成其他事件也會跳過證據。研究紀錄至少要保存**公司、期間、資產或產品範圍、現金／非現金分類、公式與交接狀態**。

### 買方與供應商要做兩端對帳

| 對帳端 | 最少需要的欄位 | 目前三家公司資料做到哪裡 |
|---|---|---|
| 買方資本端 | 資本指引、cash PP&E、租賃增加／本金、資產範圍、上線時間 | 已有公司總額與部分資產說明；缺少完整 AI 品項、站點與上線批次 |
| 買方營運端 | 可用容量、使用量、收入、毛利、OCF 與一致公式 FCF | 已有需求、雲端成長與公司現金流；缺少同一批新增容量的利用率與回收橋接 |
| 供應商交付端 | 平台、料號、資格日期、數量、出貨與驗收期間 | 買方資料沒有列出台灣供應商與份額 |
| 供應商財務端 | 同期間收入分母、產品／客戶分子、毛利、存貨、應收、OCF | 尚無足以把三家買方支出直接歸因到 universe 個股的雙向文件 |

供應商端還多一道時間差：先備料會增加存貨，出貨驗收後才可能認列收入，允許賒帳時又先形成應收，客戶付款後才進現金。因此「買方 CapEx 增加」與「供應商 OCF 改善」不必同季發生；反過來，供應商營收上升但存貨、應收或毛利惡化，也不能只看營收就說已完整受惠。

### 新手最常把哪幾件事畫上等號

- 資本**承諾**不等於已支付現金。
- 已支付現金不等於全部是 AI 伺服器或台灣零組件。
- 資產轉入可使用狀態不等於容量已被客戶用滿。
- 雲端收入成長不等於本期新容量的 ROI 已可重算。
- 買方 FCF 下降不等於供應商需求同步下降；兩端付款、存貨與認列時點不同。
- 供應商營收成長不等於毛利與現金同步改善，更不等於可把增量全歸因單一題材。

### 在研究中心裡接著怎麼學

本篇是「資本投入與公司財務」路線第一站，教的是買方七關與雙向對帳。下一站的**國巨 Q2 公司財務分母**案例，會再示範：即使一家公司總營收可以由兩條官方路徑交叉重算，題材產品分子未揭露時，仍不能把公司總額改寫成 AI、單一產品或單一客戶收入。

## 會計口徑本身也會移動

微軟宣布自 FY2027 起把資料中心與辦公建物的估計耐用年限由 15 年延長到 25 年。公司明說，此變動只改變未來折舊時點，對 FY2027 營業利益的好處很小；較大的影響是更多資料中心租賃會由 finance lease 轉為 operating lease。前者計入 CapEx、後者不計，因此公司把 calendar 2026 CapEx 預期調整為約 1,750 億美元，同時強調排除耐用年限影響後，投資期待沒有改變。

這是一個很好的教材：**reported CapEx 可以因分類而改變，實際建置意圖卻不變**。跨公司比較至少要把 cash PP&E、租賃增加、租賃本金與折舊政策放在同一頁，才不會把會計光學誤判成供應鏈拐點。

另外兩家公司在 2025 年對伺服器／網路設備做了方向相反的耐用年限調整。Meta 把多數此類資產延長至 5.5 年，並揭露當年折舊少 29.2 億美元、淨利多 25.9 億美元；Amazon 則因 AI／ML 技術迭代加快，把部分設備由 6 年縮到 5 年，揭露 2025 年折舊多 14 億美元、淨利少 10 億美元，主要影響 AWS。微軟調的是資料中心與辦公**建物**，Meta／Amazon 調的是多數或部分**伺服器與網路設備**，資產範圍不同；不能據此把任一家公司貼成「較保守」或直接比較 AI ROI。

## 來源與證據邊界

- [Microsoft FY2026 Q4 earnings call，2026-07-29](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- [Meta 2026 Q2 results，2026-07-29](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Second-Quarter-2026-Results/default.aspx)
- [Amazon 2026 Q2 results，2026-07-30](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)
- [Meta 2025 Form 10-K：伺服器／網路設備耐用年限，2026-01-29](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm)
- [Amazon 2025 Form 10-K：伺服器／網路設備耐用年限，2026-02-06](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm)
- [Meta 2026 Q1 Form 10-Q：尚未起租、在建工程與待售資產](https://www.sec.gov/Archives/edgar/data/1326801/000162828026028526/meta-20260331.htm)
- [Amazon 2026 Q1 Form 10-Q：未付款資產與 AWS 履約義務](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000014/amzn-20260331.htm)

**已知：** 三家公司各自的 OCF、PP&E／CapEx、租賃與 FCF 可由官方表格或法說對回；Meta 與 Amazon 的申報也直接證明合約承諾、資產狀態、使用／履約與現金時點不能合併成一個數字。

**還不知道：** CapEx 中每一項 AI 晶片、伺服器、網路、電力與建物的精確拆分，新增容量的上線時間與利用率，以及台灣 universe 個股的訂單與獲利份額。

**不可外推：** 這不是三家公司 AI ROI 排名；期間與公式不同。買方 CapEx 也不能直接等同任何台灣供應商收入。沒有價格、估值、共識與部位資料，本題不判斷市場是否已反映。

七關圖譜只把待交接的證據層畫清楚。它不把「資本計畫 → 現金支出 → 上線 → 利用 → 現金回收」當成已完成的因果鏈，也不把四個台灣族群的搜尋路由當成公司財務曝險。

## 影響路由

四個台灣族群都只做 `group watch`，不列個股。方向定為 `mixed` 或 `uncertain`：需求投入是順風，現金回收壓力、產品組合與資本密度則可能改變採購節奏與供應商獲利。

<!-- impact
group_id: serverodm
stock_ids:
direction: mixed
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: 大型買方維持高額AI基建投入，但官方來源未拆伺服器台數、ODM份額、上線節奏或議價條件。
evidence_boundary: 不把雲端公司CapEx直接換算成任一台灣ODM訂單或營收。
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: 伺服器與網路擴建可能增加高階板需求，但CapEx同時包含建物、晶片、電力與其他資產，沒有PCB內容量拆分。
evidence_boundary: 只構成需求搜尋觸發，不建立板層、材料、客戶或個股份額。
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: 資料中心容量與功率密度提高可能增加電源內容量，但買方文件未列架構、供應商與認證。
evidence_boundary: 不把資料中心總CapEx等同電源系統訂單；需公司與平台文件雙向核對。
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-15
rationale: AI容量上線需要散熱，但官方CapEx與FCF資料沒有液冷比例、CDU數量、供應商或毛利。
evidence_boundary: 不由雲端需求直接指認台灣散熱個股受惠，等待量產與損益證據。
-->

## 下一個可證明／否定的節點

- **下一季現金表**：同口徑追 cash PP&E、finance lease、OCF 與 FCF；若支出維持但 OCF／毛利持續惡化，資本回收風險升高。
- **容量變現**：Azure、AWS 與 Meta AI 產品的使用量、營收與毛利是否跟上資產上線；若容量投入增加卻無法變現，需求故事要降權。
- **分類調節**：微軟租賃分類改變後，同時看 reported CapEx 與 operating-lease cash payments，避免把分類位移誤讀為採購位移。
- **台灣公司交叉驗證**：供應商 Q2／Q3 正式文件是否出現客戶認證、出貨、存貨／應收、毛利與 OCF 的同向改善；只有營收、沒有毛利與現金，不算完整受惠。
- **兩端共同鍵**：買方與供應商能否同時指向同一平台、料號、期間、數量與驗收節點；缺任一端，就只保留需求搜尋路由，不建立題材財務歸因。
