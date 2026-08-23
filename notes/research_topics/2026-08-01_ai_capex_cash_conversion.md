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

<!-- research_source
source_id: S9
role: other_primary
source_kind: document
publisher: Financial Accounting Standards Board
title: Accounting Standards Update 2016-02 — Leases (Topic 842), Section A
published_at: 2016-02-25
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://storage.fasb.org/ASU%202016-02_Section%20A.pdf
locator: PDF pp.8–9、108–114；finance lease 初始 ROU asset／lease liability、後續 liability 衡量、principal／interest cash-flow classification 與 disclosure objective
limitation: 這是美國 GAAP 租賃會計規範與通用例示，不是 Microsoft、Meta、Amazon 或 AI 資料中心的公司數字，也不定義各公司自訂 CapEx／FCF 指標；後續修訂與公司政策仍須回到當期申報核對
independence_group: fasb-topic-842
-->

<!-- research_source
source_id: S10
role: other_primary
source_kind: document
publisher: Financial Accounting Standards Board
title: Leases under Topic 842 — 2024 GAAP Taxonomy Implementation Guide
published_at: 2024-03-26
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://xbrl.fasb.org/ix/?doc=..%2Fimpdocs%2FLE_TIG%2Finline_f2017leasesig.htm
locator: Illustrative facts L25–L30；分列 finance-lease principal payments、interest payments，以及 ROU assets obtained in exchange for new finance／operating lease liabilities
limitation: 這是 FASB 為 XBRL taxonomy 提供的虛構揭露範例；L25 的 1,500 與 L29 的 500 不是任何真實公司、資料中心、產業樣本或投資支出，也不能用來估計正常比率
independence_group: fasb-topic-842
-->

<!-- research_source
source_id: S11
role: company_filing
source_kind: document
publisher: Microsoft
title: Microsoft FY2026 Form 10-K
published_at: 2026-07-29
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm
locator: consolidated cash flows；Note 6 Property and Equipment；Note 12 Unearned Revenue；Note 13 Leases；AI infrastructure risk factors
limitation: 年報把公司總 PP&E、應付未付、折舊、未起租租賃與跨產品履約義務分開，但沒有同一 AI 資產批次的在建轉入、利用率、收入、毛利與現金回收橋接
independence_group: microsoft
-->

<!-- research_source
source_id: S12
role: company_filing
source_kind: document
publisher: Meta Platforms
title: Meta Platforms 2026 Q2 Form 10-Q
published_at: 2026-07-30
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm
locator: Note 6 Property and Equipment；Note 9 Leases and Contractual Commitments；H1 cash-flow discussion
limitation: 在建工程、折舊、尚未起租租賃、待售資產與 cash PP&E 的期間及狀態不同；申報未提供在建工程完整 rollforward、逐批 placed-in-service、利用率或 AI 專屬收入
independence_group: meta
-->

<!-- research_source
source_id: S13
role: company_filing
source_kind: document
publisher: Amazon
title: Amazon 2026 Q2 Form 10-Q
published_at: 2026-07-31
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm
locator: supplemental cash-flow information；Note 8 Segment Information 的 PP&E net additions 與 depreciation；AWS performance obligations；FCF reconciliation
limitation: 分部資產與折舊按 usage 分攤不是容量利用率揭露；淨新增含非現金未付款活動，履約義務也沒有與同一資產批次、AI 工作負載或供應商逐筆配對
independence_group: amazon
-->

<!-- research_source
source_id: S14
role: company_filing
source_kind: document
publisher: NVIDIA
title: NVIDIA 2026-08-17 Form 8-K — PORTS-Pike Residual Value Guaranties
published_at: 2026-08-17
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm
locator: 第 1.01 項 Residual Value Guaranties 與第 2.03 項；約 4.25 IT-GW、起租生效、1,050 億美元累計上限、ready-for-service、Trigger Event、重租／出售回收、終止與 OpenAI indemnity 段落
limitation: 8-K 明示摘要並不完整，完整 Agreements form 預計隨截至 2026-07-26 季度的 10-Q 提交；現有文件沒有逐租約保證最低值曲線、責任排程、折現率、違約機率、回收順位或預期損失
independence_group: ports-pike-transaction
-->

<!-- research_source
source_id: S15
role: company_release
source_kind: document
publisher: NVIDIA / SB Energy
title: NVIDIA Guarantees SB Energy's PORTS-Pike Technology Campus in Ohio
published_at: 2026-08-17
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm
locator: SEC Exhibit 99.1；20 年租約、分期自 2028 上線、8 IT-GW 規劃、SB Energy build／own／operate 與 NVIDIA 投資 15 億美元段落
limitation: 這是 S14 同一交易的公司新聞稿附件，不是第二個獨立專案或獨立合約驗證；規劃容量與投資額也不等於 NVIDIA 保證付款、專案建設總成本或當期 CapEx
independence_group: ports-pike-transaction
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: document
publisher: OpenAI
title: OpenAI joins PORTS-Pike project
published_at: 2026-08-17
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://openai.com/index/openai-joins-ports-pike-project/
locator: first 800MW expected in 2028、SB Energy build／own／operate、OpenAI completed-capacity payment、20-year lease、NVIDIA investment／credit support 與 permits／financing dependencies 段落
limitation: OpenAI 是同一交易的租戶當事人，不是獨立部署樣本；頁面說明付款與開發條件，但沒有完整租約、保證最低值、違約概率、每期租金、回收順位或 NVIDIA 淨損失
independence_group: ports-pike-transaction
-->

<!-- research_source
source_id: S17
role: regulator_or_policy
source_kind: living_index
publisher: U.S. Securities and Exchange Commission
title: NVIDIA EDGAR Company Filings
published_at:
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.sec.gov/edgar/browse/?CIK=1045810&owner=exclude&action=getcompany
locator: 2026-08-23 以 NVIDIA filings index 的 10-Q／8-K 類型重查；可定位 2026-08-17 Form 8-K，本輪未定位到截至 2026-07-26 的 Form 10-Q，後續追蹤 Residual Value Guaranties 完整 form 及修訂
limitation: 這是會持續更新的申報索引，不是固定證據文件；後續出現任何申報都必須另以 document source 登錄並逐段核對，不能由索引空白推定事件不存在
independence_group: ports-pike-transaction
-->

<!-- research_source
source_id: S18
role: company_release
source_kind: document
publisher: Micron Technology
title: Micron Unveils Micron Research Labs, a U.S.-Based Long-Horizon Innovation Hub to Shape the Future of Memory and AI
published_at: 2026-08-20
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://investors.micron.com/news/press-release/2026/Micron-Unveils-Micron-Research-Labs-a-U-S--Based-Long-Horizon-Innovation-Hub-to-Shape-the-Future-of-Memory-and-AI/default.aspx
locator: planned $10 billion investment over the next decade、Boise flagship campus、university collaborations、global satellite labs、research domains 與 calendar 2027 groundbreaking 段落
limitation: planned investment 是十年期前瞻計畫，沒有逐年 cash schedule、R&D expense／PP&E accounting split、incentive bridge、fab wafer capacity、tool／vendor order、技術 qualification 或財務回收分母；供應商引言不構成採購合約
independence_group: micron
-->

<!-- research_source
source_id: S19
role: company_filing
source_kind: document
publisher: Micron Technology
title: Micron FY2026 Q3 Form 10-Q
published_at: 2026-06-25
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm
locator: Statements of Operations 的 Q3／九個月 R&D expense；MD&A 的 R&D drivers、FY2026 estimated net PP&E CapEx、九個月 PP&E cash expenditures／government incentives 及 Boise／New York fab output timing
limitation: 申報期間截至 2026-05-28、早於 2026-08-20 Research Labs 公告，且數字皆為 Micron 公司級口徑；不能判定已包含或排除 Labs 十年計畫，也不能把 R&D expense、gross PP&E cash、net CapEx estimate 與 wafer capacity 互換
independence_group: micron
-->

<!-- research_source
source_id: S20
role: regulator_or_policy
source_kind: living_index
publisher: U.S. Securities and Exchange Commission
title: Micron EDGAR Company Filings
published_at:
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.sec.gov/edgar/browse/?CIK=723125&owner=exclude&action=getcompany
locator: 2026-08-23 以 Micron filings index 重查 10-Q／10-K／8-K，追蹤 Research Labs 年度 R&D expense、PP&E、新計畫、incentive、facility 與 capacity 對帳
limitation: 持續更新索引只供發現新申報；索引本身不證明 Labs 支出、建設、研究產出、fab capacity、供應商訂單或回收
independence_group: micron
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

<!-- research_claim
claim_id: C10
label: verified
status: active
claim: FASB Topic 842 將 finance lease 起租時認列的 ROU asset／lease liability、後續本金償還與利息分開處理；本金償還列為 financing cash flow，FASB taxonomy 範例也把 principal payments 與新租賃負債換得的 ROU assets 分成兩個事實
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2026-08-14
basis: S9 pp.8、108–114 直接規定初始認列、後續衡量及 principal／interest 現金流分類；S10 L25～L30 以不同標籤與虛構數值分列付款與新增 ROU assets
boundary: FASB 文件只建立通用會計與揭露契約，不代表任何 hyperscaler 的實際租賃新增額、付款、AI 資產範圍或投資報酬；S10 數值不能當產業基準
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C11
label: inference
status: active
claim: Microsoft FY2026Q4 揭露的 total finance leases 56 億美元與 Meta 2026Q2 揭露的 finance-lease principal payments 9.62 億美元位於不同租賃時鐘，即使兩家公司都把租賃項目納入 headline CapEx，也不能直接比較、相減或用同一公式與 cash PP&E 加總
supporting_source_ids: S1,S2,S9,S10
contrary_source_ids:
as_of: 2026-08-14
basis: S1 分列 410 億美元 CapEx、56 億 total finance leases 與 358 億 cash PP&E；S2 明確把 301.16 億 cash PP&E 與 9.62 億 finance-lease principal 相加成 310.78 億、四捨五入為 310.8 億 headline CapEx；C10 則證明新租賃／ROU 與償還本金是不同事實
boundary: Microsoft 所引法說沒有在同一段提供 finance-lease principal，Meta 所引結果也沒有在同一表提供新 finance-lease ROU additions；因此本判讀只裁決兩個已揭數字不可比，不補算缺值、不做公司 AI 投資強弱或 ROI 排名
verification_needed: 三家公司在同一單季各自分列 cash PP&E、新 finance-lease ROU／liability additions、finance-lease principal／interest、其他 lease remeasurement 與一致的 headline／FCF reconciliation
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: Microsoft FY2026 年報分列全年 cash PP&E additions 1,159.48 億美元、期末已購置尚未付款 PP&E 267 億美元、全年折舊 343 億美元、尚未起租租賃 3,291 億美元與公司履約義務 6,840 億美元
supporting_source_ids: S11
contrary_source_ids:
as_of: 2026-07-29
basis: S11 的現金流量表、Note 6、Note 12 與 Note 13 各自直接揭露上述數字與期間
boundary: 五個數字分屬期間現金流、期末應付存量、成本分攤、未開始合約與跨產品未來收入；不能相加、相除成利用率，也不能改寫為 AI 專屬資產或 ROI
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: verified
status: active
claim: Meta 2026 Q2 申報分列 H1 cash PP&E 491.1 億美元、6 月底在建工程 803.45 億美元、H1 折舊 116.7 億美元、尚未起租租賃 2,789.9 億美元與期末待售資產 20.3 億美元
supporting_source_ids: S12
contrary_source_ids:
as_of: 2026-07-30
basis: S12 的 Note 6、Note 9 與現金流討論直接揭露資產存量、期間費用、未來租賃承諾與現金購置
boundary: 在建工程期末存量不等於 H1 新增，待售重分類也顯示資產狀態會移動；沒有逐批轉入可使用、利用率、AI 收入或現金回收資料
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: Amazon 2026 Q2 申報分列 H1 PP&E 淨新增 1,186.48 億美元、已取得但未付款 PP&E 增加 206.20 億美元、H1 PP&E 折舊攤銷 267.03 億美元，並稱 4,960 億美元 AWS 未來服務承諾的收入時點由客戶使用與公司履約決定
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-07-31
basis: S13 的 supplemental cash-flow、segment information 與 performance-obligation 段落直接分列非現金資產、分部折舊與未來服務承諾
boundary: 淨新增含非現金活動，折舊按分部 usage 分攤也不是容量利用率；履約義務不能與本期新增資產、AI 工作負載或台灣供應商一對一
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: 折舊與折舊攤銷是資產成本進入損益的碼表，不是容量利用率、客戶變現或現金回收碼表；三家公司若沒有共同資產批次鍵，就不能用折舊除以 CapEx 或資產新增推算 AI 利用率
supporting_source_ids: S11,S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: 三份申報都把現金或非現金資產新增、資產存量、折舊、合約承諾與收入證據放在不同報表或期間，且沒有逐批 cohort reconciliation
boundary: 這是報表可識別性判定，不否定管理層內部可能有利用率資料，也不衡量三家公司 AI ROI、估值或任何供應商受惠
verification_needed: 同一具名資料中心或設備批次的取得方式、在建轉入日、折舊起算、可用容量、客戶使用與收入、付款及收款日期
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: NVIDIA 2026-08-17 Form 8-K 表示，其為 PORTS-Pike 約 4.25 IT-GW 租賃簽訂多份殘值保證，協議一般在對應租約起租時生效；初始承諾的累計付款義務上限為 1,050 億美元，且 NVIDIA 付款義務另以相關場所滿足預計自 2028 年起達成的 ready-for-service 條件為前提
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-17
basis: S14 第 1.01 項直接分列租賃容量、Agreement 生效點、aggregate cumulative cap 與 ready-for-service 前提
boundary: 上限是附條件的累計責任邊界，不是 2026-08-17 已支付現金、當期 CapEx、租賃本金、建設總成本、資產公允價值或預期損失；另約 3.8 IT-GW 的信用支持仍由 NVIDIA 自行選擇是否行使
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: S14 所述保證一般在對應租約起租時生效，但 NVIDIA 的付款與救濟程序只在 OpenAI 因無力償債造成租約違約或未支付租款等 Trigger Event 發生後啟動；NVIDIA 一般補足保證最低值與重租或出售回收額之間的差額，OpenAI 並同意補償 NVIDIA 實際支付給出租人的金額
supporting_source_ids: S14
contrary_source_ids:
as_of: 2026-08-17
basis: S14 第 1.01 項直接定義兩類 Trigger Event、shortfall 計算、NVIDIA 可選救濟路徑及 OpenAI reimbursement／indemnity
boundary: 文件沒有公布每份租約的保證最低值、重租或出售可回收多少、OpenAI 補償能力、付款時間或 NVIDIA 最終淨損失；補償承諾也不是已收到現金
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: 閱讀大型 AI 基建信用支持時，應把公告揭露的保證上限放在第 0 層，再分開 ready-for-service、租約起租與保證生效、租戶正常付款或 Trigger Event、重租或出售回收、保證人實際補差額、租戶補償六個經濟時鐘；保證上限、股權投資與 IT-GW 容量分屬不同帳本，不能相加或改寫成同一期 CapEx
supporting_source_ids: S14,S15,S16
contrary_source_ids:
as_of: 2026-08-17
basis: S14 把保證的 ready-for-service 條件、生效、觸發、回收、補差額與補償分開；S15／S16 又把 NVIDIA 15 億美元股權投資、20 年租賃、分期容量及 OpenAI 在 completed capacity 可租時才開始付款分列
boundary: 六時鐘是針對這一交易建立的現金責任閱讀框架，不是美國 GAAP 通用科目、違約預測模型或 NVIDIA／OpenAI 信用品質評分，也不衡量台灣供應商訂單、估值或市場是否反映
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C19
label: unverified
status: active
claim: 現有公開摘要足以重算 PORTS-Pike 各租約的逐期最大曝險、保證最低值折減曲線、違約機率、重租或出售回收率、OpenAI 補償回收率與 NVIDIA 預期損失
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-23
basis: S14 明示現有描述不完整，完整 Agreements form 尚待後續 10-Q exhibit；S14 至 S16 均未提供逐租約現金流、機率、折現與回收分母
boundary: 找不到完整參數不是保證一定發生損失或一定不會損失；本文只把可公開重算的上限擋在摘要已揭露的條件，並保留缺值
verification_needed: NVIDIA 後續 10-Q 所附完整 Agreements form、逐租約保證最低值與期限、實際 lease commencement／ready-for-service、任何 Trigger Event、重租或出售回收及 OpenAI reimbursement 結果
resolution:
-->

<!-- research_claim
claim_id: C20
label: verified
status: active
claim: Micron 於 2026-08-20 公布 Micron Research Labs，公告的精確措辭是未來十年 planned $10 billion investment；用途包含 Boise flagship campus、大學合作、全球 satellite labs 與生態夥伴，研究範圍涵蓋記憶體技術、memory／compute architecture、packaging 與未來半導體製造
supporting_source_ids: S18
contrary_source_ids:
as_of: 2026-08-20
basis: S18 標題下摘要及正文直接提供金額、十年期間、組織形式與研究領域
boundary: 公告原文不是 up to，但 planned 仍不保證每年核准、執行或最終花足，也不是公告日現金支出或逐年預算；公司未公布年度排程、R&D expense／PP&E 分拆、政府補助、設備清單、研究產出、wafer capacity、供應商份額或回收
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C21
label: verified
status: active
claim: Micron FY2026 Q3 10-Q 分列截至 2026-05-28 單季／九個月 R&D expense 13.16／37.37 億美元、九個月 PP&E cash expenditures 196.0 億美元與 government-incentive proceeds 29.9 億美元，另估 FY2026 PP&E CapEx net of incentive proceeds 約 270 億美元
supporting_source_ids: S19
contrary_source_ids:
as_of: 2026-06-25
basis: S19 Statements of Operations 以 USD million 列 1,316／3,737，MD&A 另列 $19.60 billion gross PP&E expenditures、$2.99 billion incentive proceeds 與約 $27 billion full-year net CapEx estimate；只做 million-to-billion 單位正規化
boundary: 期間 R&D expense、gross PP&E cash outflow、incentive inflow 與 full-year net estimate 是不同帳；申報期又早於 Labs 公告，不能說上述實際數字已包含、排除或等於十年 $10 billion 計畫，也不能跨期相加成 Labs spend
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C22
label: inference
status: active
claim: 閱讀企業長期研究投資時，應分開保存 planned research envelope、期間 R&D expense、PP&E／CapEx 與 incentive cash、research-facility execution、technical transfer／product qualification／fab capacity，以及 supplier financial attribution 六本帳
supporting_source_ids: S18,S19
contrary_source_ids:
as_of: 2026-08-23
basis: S18 把十年計畫、合作網路、研究領域與 facility groundbreaking 放在前瞻公告，S19 則把期間費用、PP&E cash、incentive、net CapEx estimate 與 manufacturing wafer-output dates 放在不同報表和段落
boundary: 六本帳是研究中心建立的可追溯框架，不是 Micron 會計政策或研究成功機率模型；任一欄前進都不能代替產品 qualification、量產容量、設備採購或台灣供應商收入
verification_needed: 同一 Labs program／facility／project key 的年度核准額、actual R&D expense、capitalized PP&E、cash／incentive、construction／staffing、research output、transfer／qualification、wafer output、vendor 與財務共同鍵
resolution:
-->

<!-- research_claim
claim_id: C23
label: unverified
status: active
claim: Micron Research Labs 的十年 100 億美元 planned investment 已可直接視為新增晶圓廠 CapEx、年度均勻支出、已增加的 wafer capacity、半導體設備 TAM 或台灣供應商訂單與收入
supporting_source_ids:
contrary_source_ids: S18,S19
as_of: 2026-08-23
basis: S18 沒有年度 accounting／cash／capacity／vendor bridge，S19 又把 R&D expense、PP&E CapEx 與具名 fab output 時程分開；現有來源不足以完成任一直接換算
boundary: 不把長期研究計畫貶為零，也不把它提前改名為量產與財務；研究價值、facility execution、technical transfer、production capacity 與 supplier attribution 各需自己的證據
verification_needed: Micron 逐年 Labs budget／actual、R&D expense 與 PP&E reconciliation、facility tools、具名 research outputs、product／process transfer、qualification、incremental wafer／bit capacity、vendor award、shipment、revenue、cost 與 margin
resolution:
-->

<!-- research_claim
claim_id: C24
label: verified
status: active
claim: Micron 將 Research Labs 預計 calendar 2027 破土、可容納數百名研究人員的設施節點，與製造 fab 的 wafer-output／supply 節點分開揭露；FY2026 Q3 10-Q 分別把首座 Boise DRAM fab 的 mid-2027 output、第二座 Boise fab 的 late-2028 output 與首座 New York fab 的 2030-and-beyond supply 列為產能時程
supporting_source_ids: S18,S19
contrary_source_ids:
as_of: 2026-08-20
basis: S18 直接描述 Research Labs facility groundbreaking／researcher capacity，S19 MD&A 直接描述三個 manufacturing fab 的 output／supply milestones
boundary: 同為 2027 不代表 Labs facility 就是首座 Boise manufacturing fab，也不表示研究設施沒有 PP&E、pilot tools 或未來製造轉移；兩份來源未提供資產、預算、設備或產能共同鍵
verification_needed:
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C16,C17,C18,C19
metric: PORTS-Pike 殘值保證由第 0 層上限走到 ready-for-service、租約起租與保證生效、租戶正常付款或 Trigger Event、重租或出售回收、NVIDIA 實際補差額、OpenAI 補償的現金曝險
source_ids: S14,S15,S16
watch_source_ids: S17
frequency: event_driven
frequency_detail: 2026-08-26 NVIDIA FY2027 Q2 結果後先查下一份 10-Q；其後遇完整 Agreements form、修訂或任何實際觸發事件即重審
next_check: 2026-08-27
trigger: 10-Q 提交完整保證 form，或出現逐租約最低值、lease commencement、ready-for-service、Trigger Event、重租／出售回收、NVIDIA 實際付款與 OpenAI reimbursement
invalidation: 後續正式文件取消或修改保證、上限、生效條件、Trigger Event、回收公式、終止條款或 OpenAI 補償，使現有六時鐘與曝險邊界不再適用
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C20,C21,C22,C23,C24
metric: Micron Research Labs 十年 planned envelope 到年度 R&D／PP&E cash、facility execution、technical transfer、fab capacity 與 supplier financial attribution 的共同對帳
source_ids: S18,S19
watch_source_ids: S20
frequency: quarterly
frequency_detail: 每季 10-Q／10-K 回查 R&D expense、PP&E、incentive 與 Labs 計畫更新；若 Micron 提前公布 Labs budget、groundbreaking、facility tools、研究成果、product transfer 或 supplier award 即事件重審
next_check: 2026-09-30
trigger: Micron 首次以同一 Labs program／facility key 公布年度 plan-to-actual、R&D／PP&E split、construction、research output、qualification、capacity 或 vendor／financial attribution 中任一可串接欄位
invalidation: 若後續正式申報重定義 $10 billion 的範圍、期間、與既有 $250 billion 計畫關係或會計分類，六本帳須按新 reconciliation 改畫，不能沿用公告 headline
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
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: finance_lease_addition_and_principal_clocks_separated_with_fasb_contract_without_refreshing_thesis_clock
evidence: sources:S1,S2,S9,S10
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: depreciation_cost_clock_separated_from_utilization_and_recovery_with_latest_filings_without_refreshing_thesis_clock
evidence: sources:S11,S12,S13
-->

<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: residual_value_guarantee_six_clock_cash_waterfall_added_without_refreshing_thesis_clock
evidence: sources:S14,S15,S16
-->

<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: micron_research_plan_rd_expense_capex_capacity_and_supplier_ledgers_separated_without_refreshing_thesis_clock
evidence: sources:S18,S19
-->

## 新手先讀：這篇在講什麼

### 名詞小字典

- **CapEx（資本支出）**：買進或建造可使用多年的資產，例如資料中心、伺服器與網路設備；公司對 CapEx 的揭露可能含現金購置、融資租賃或兩者。
- **planned investment（計畫投資）**：管理層對未來投入範圍與時間窗的前瞻計畫；若沒有逐年核准額與實際數，它不是公告日已付款、當期費用、已下採購單或平均年度預算。
- **R&D expense（研發費用）**：一段會計期間內列入損益的研發成本；它可能包含人員、開發／資格前晶圓等項目，卻不等於整份長期研究計畫的現金、資本化資產或未來產能。
- **PP&E（不動產、廠房及設備）**：資產負債表上的長期實體資產類別；「cash paid for PP&E」是期間現金流，「PP&E 餘額」是某一時點仍留在帳上的資產，兩者不是同一個數字。
- **研究設施與製造晶圓廠**：研究設施主要承載人員、實驗與長期技術探索；製造晶圓廠則以可量測的 wafer／bit output 供貨。兩者都可能使用建物與設備，但動土、容納研究員與量產不是同一個里程碑。
- **開發／資格前晶圓（development／pre-qualification wafers）**：產品或製程正式通過內部性能、功能與可靠度資格前，用於研發與測試的晶圓；有這類成本不等於產品已量產。
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
- **RPO（remaining performance obligations，剩餘履約義務）**：已簽約但尚待提供產品或服務、未來才可能認列的收入；它是合約存量，不是當期營收、收款或新增資產的回收率。
- **非現金資產增加**：資產已取得或記入 PP&E，但付款可能尚未發生，或由租賃等方式取得；它會讓資產時鐘早於現金時鐘。
- **折舊／折舊攤銷**：把已資本化資產的成本，依估計耐用年限分期列入費用；它是成本分攤，不是設備利用率、客戶收入或現金回收率。
- **融資租賃（finance lease）**：先取得資產使用權、分期付款的融資方式；它可能計入 headline CapEx，卻不在當期「cash paid for PP&E」裡一次流出。
- **使用權資產（ROU asset）**：承租人取得在租期內使用標的資產的權利；起租時可與租賃負債同時認列，不代表當期已支付同額現金。
- **租賃負債（lease liability）**：承租人尚待支付租賃款的現值；新租賃開始、利息累積、本金償還、修改與重新衡量會沿不同方向改變它。
- **起租／租賃開始（lease commencement）**：標的資產可供承租人使用、開始認列 ROU asset 與 lease liability 的節點；它不同於簽約日，也不同於日後每期付款日。
- **租賃新增額／本金償還**：前者描述本期開始使用的新租賃資產與負債，常是非現金事實；後者是償還既有 finance-lease liability 的現金流，兩者不能互換。
- **IT-GW（IT gigawatt）**：供伺服器、網路與儲存等資訊設備使用的十億瓦負載容量；它不是園區總用電、GPU 數量、美元支出或收入。
- **PORTS-Pike**：本案位於美國俄亥俄州 Pike County 的大型資料中心園區名稱；本文只用它指向 NVIDIA、SB Energy 與 OpenAI 這一交易，不代表所有 AI 園區都採相同合約。
- **Micron Research Labs**：Micron 於 2026-08-20 公布的長期研究平台，預計以 Boise 為總部並連結大學、衛星實驗室與生態夥伴；本文不把它和 Micron 已具名的製造晶圓廠視為同一資產。
- **DRAM（動態隨機存取記憶體）**：伺服器、個人電腦與其他系統常用的揮發性工作記憶體；本文提到 DRAM fab 時，指製造這類記憶體的晶圓廠，不等於一般研究設施。
- **SEC（美國證券交易委員會）**：美國公開公司提交財務與重大事件申報的監管機關；本文引用向 SEC 提交的 8-K，不代表 SEC 替交易風險背書。
- **Agreements（本案保證協議）**：NVIDIA 8-K 對多份殘值保證的合稱；目前公開的是摘要，完整 form 尚待後續申報。
- **殘值保證（residual value guarantee）**：若租賃資產在約定情境下的回收價值不足，由保證人依合約補足部分差額的信用支持；它不是簽約當天就支付全部上限。
- **保證上限（guarantee cap）**：保證人在指定範圍內最多承擔的累計付款邊界；上限不等於預期損失、當期 CapEx 或已流出的現金。
- **ready-for-service**：出租人把約定場所完成到租約可開始提供的狀態；本案還要依租約條件逐期判定，不等於整座園區在公告日已上線。
- **觸發事件（Trigger Event）**：讓保證責任進入處理程序的合約事件；本案列的是 OpenAI 無力償債導致租約違約，或未依租約付款，不是 AI 需求變弱的泛稱。
- **重租／出售回收**：原租戶違約後，出租人或保證人藉由替換租戶或出售資產收回的金額；它會影響待補差額，不能在估算時當成零。
- **補償／賠償（reimbursement／indemnity）**：一方承諾對另一方實際支付的指定款項予以補償；它多一層求償權，但不代表對方在壓力情境下必然能立即付清。
- **FASB／Topic 842**：FASB 是制定美國 GAAP 的 Financial Accounting Standards Board；Topic 842 是租賃會計主題，本文只用它界定認列、付款與揭露時鐘，不把會計規範當公司績效。
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
- 對 Micron Research Labs 分開追年度 plan-to-actual、R&D／PP&E 與 incentive、研究設施建置與工具、研究產出、技術轉移／資格、製造產能及供應商財務，不讓十年 headline 一次跨完六本帳。

### 想一想

- 如果公司只把資料中心租賃從融資租賃改成營業租賃，headline CapEx 下降但實際投資期待不變，需求應該被解讀成變弱嗎？
- 一美元 CapEx 有多少是建物、電力與網路，有多少真的變成 GPU、伺服器或台灣零組件收入？
- FCF 轉負是暫時把現金換成會產生未來收入的資產，還是需求、利用率與定價不足以回收投資；要看哪些後續數字才能分辨？
- 為什麼不能把 Micron 的十年 100 億美元研究計畫除以十，當成每年 10 億美元 R&D，再加進 FY2026 CapEx 或設備商訂單？

## 三家公司要先按各自口徑讀

單位為十億美元；微軟與 Meta 是截至 2026-06-30 的**單季**，Amazon 的 OCF／淨 PP&E／FCF 是截至同日的**過去十二個月（TTM）**。這張表刻意不做橫向排名。CapEx／PP&E、OCF、公司自訂 FCF 分別對應比較帳本 `M1`、`M2`、`M3`。

| 公司／期間 | 公司揭露的 CapEx 或 PP&E 口徑 | OCF | FCF | 讀法 |
|---|---:|---:|---:|---|
| Microsoft FY2026 Q4 | CapEx 41.0；其中 finance leases 5.6，cash paid for PP&E 35.8 | 55.4 | 19.6 | Headline CapEx 含租賃；FCF 反映 cash PP&E，而不是直接減掉 41.0。
| Meta 2026 Q2 | CapEx 31.08，等於 cash PP&E 30.116 加 finance-lease principal 0.962 | 31.862 | 0.784 | Meta 的 FCF 同時扣 cash PP&E 與 finance-lease principal；公司明示此非 GAAP 口徑可能與同業不同。
| Amazon 截至 2026 Q2 TTM | PP&E purchases 173.028；扣出售與 incentives 後為 169.007 | 161.403 | -7.604 | Amazon 的 FCF 公式是 TTM OCF 減淨 PP&E；這不是單季，也沒有再扣 finance-lease principal。

三家公司都能由官方表格對回各自公式，但**公式對得上不代表彼此可比**。例如 Meta 的 0.784 = 31.862 - 30.116 - 0.962；Amazon 的 -7.604 = 161.403 - 169.007。這些是會計恆等式，不是 AI 投資報酬率。

## 都寫「含租賃」，仍可能是兩支碼表：新增額不等於本金

Finance lease 至少會走過兩個不同的量測時點。租賃開始時，承租人依 FASB Topic 842 認列
ROU asset 與 lease liability；這通常是取得使用權並承諾未來付款的資產／負債事實，不要求
當天一次付清。租期中實際付款時，又要把利息與償還本金分開；finance-lease principal
repayment 列在 financing cash flow，會降低既有租賃負債。換句話說，「本期新開始多少租賃」
與「本期替新舊租賃還多少本金」沒有一對一關係。

| 租賃時鐘 | 本期發生什麼 | 常見揭露 | 不能替代 |
|---|---|---|---|
| 簽約但尚未起租 | 已有未來承諾，資產尚不可供使用 | lease not yet commenced／future payments | 新增 ROU asset、當期本金或可用容量 |
| 起租／新增 | 取得使用權，認列 ROU asset 與 lease liability | ROU assets obtained in exchange for new lease liabilities | 當期現金支出或日後本金付款 |
| 付款 | 支付本期租賃款，拆成利息與本金 | interest payments／principal payments | 本期新租賃規模或新上線容量 |
| 期末餘額 | 累積新租賃、付款、利息、修改與重新衡量後的存量 | finance-lease assets／liabilities | 本期新增額或本期現金流 |

FASB 的 2024 taxonomy implementation guide 刻意把兩者分成不同標籤：虛構範例的
`principal payments under finance lease obligations` 是 1,500，`ROU assets obtained in
exchange for new finance lease liabilities` 是 500。這不是要提供 3 倍的正常比例，而是示範
同一期間可以同時償還很多既有租賃、只新增少量租賃，兩筆資訊必須分開報。數字屬會計範例，
不是任何公司、資料中心或產業統計。

### 套回 Microsoft 與 Meta，差別就看得見

| 公司揭露 | 原文口徑 | 位在哪支碼表 | 安全讀法 |
|---|---|---|---|
| Microsoft FY2026Q4 | CapEx 410 億美元、`total finance leases` 56 億美元、cash PP&E 358 億美元 | 法說把 finance leases 放進 headline capital metric，卻未在同一段揭露 principal | 能說公司 CapEx 含 finance leases；不能把 56 億和另一公司的本金比較 |
| Meta 2026Q2 | cash PP&E 301.16 億美元、finance-lease principal 9.62 億美元 | 兩筆都是當期 cash-flow 項目；本金列 financing activities | `301.16 + 9.62 = 310.78` 億，四捨五入為公司 headline CapEx 310.8 億美元 |

Meta 的加法可由同一份結果表逐項重算；Microsoft 的 410 億、56 億與 358 億則分別只報到
整數或一位小數，公司沒有在該段給精確 reconciliation。不能硬算 `358 + 56 = 414` 億後，
把 4 億美元差距解讀成漏報、錯誤或另一類資產；它可完全落在揭露精度與口徑差異裡。

更不能把 Microsoft 的 56 億除以 Meta 的 9.62 億，宣稱前者租賃投資約為後者 5.8 倍：
前者標成 total finance leases，後者明確是償還本金，既不是相同分子，也沒有共同資產範圍。
要建立可比橋接，三家公司都必須在同一單季分列 cash PP&E、新 finance-lease ROU／liability
additions、principal、interest、modification／remeasurement，以及各自 headline CapEx 與 FCF
公式。

本段是 `N=2` 家指定發行人的當期揭露，加上一條 FASB 會計規範／taxonomy 消息鏈；不是
hyperscaler 或資料中心產業樣本。公司數字是各自報告值，Meta 加法與 FASB 分類是確定性
核對，沒有 sampling SE／t；FASB 的 1,500／500 是虛構示例，不納入公司比較。這一段只裁決
口徑，不衡量 AI ROI、供應商訂單、估值或市場是否反映。

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

## 100 億美元研究計畫不是 100 億美元晶圓廠：Micron 六本帳

Micron 在 2026 年 8 月 20 日公布 Micron Research Labs，原文是**計畫於未來十年投入
100 億美元**。這個研究平台以 Boise 為總部，範圍涵蓋關鍵記憶體技術、先進記憶體與運算
架構、封裝、未來半導體製造，也會資助大學合作、全球衛星實驗室與生態夥伴。這足以證明公司
提出一項長期研究計畫，卻還不能證明 100 億美元已成為現金支出、當期研發費用、晶圓廠產能
或設備供應商訂單。

### 公司公布的是十年 planned investment，不是逐年預算表

公告沒有列出精確的會計年度起訖、每年核准額、實際支出、R&D expense／PP&E 分拆、政府
incentive 調節或工具清單。因此不能把 `100 億美元 ÷ 10 年` 改寫成「每年固定 10 億美元」，
也不能把十年總額一次加進 FY2026 CapEx。公告所說的研究將看向超過十年的問題，描述的是
技術視野；「未來十年」才是 planned investment 的時間窗，兩個十年不是同一欄。

Micron 也說這項新計畫建立在先前超過 2,500 億美元的美國製造與研發規劃之上，但沒有提供
兩者的 project、期間與會計口徑調節表。讀者可以知道兩個 headline 都存在，不能機械相加成
一個可稽核的 2,600 億美元支出表。

### 公司自己的 10-Q 已把 R&D、PP&E 與 incentive 分開

以下全部換成十億美元，只為看清不同帳本與期間，不做加總或高低比較：

| 揭露項目 | 金額（USD billion） | 期間／狀態 | 正確讀法 |
|---|---:|---|---|
| Micron Research Labs planned envelope | 10 | 2026-08-20 公布；未來十年 | 長期研究計畫，不是公告日 actual |
| R&D expense | 1.316 | 截至 2026-05-28 的單季 | 公司級當期損益費用，不是 Labs 年度分子 |
| R&D expense | 3.737 | 截至 2026-05-28 的九個月 | 公司級累計費用，期間不同於十年計畫 |
| gross PP&E cash expenditures | 19.60 | FY2026 前九個月 | 公司級投資現金流，不是 Labs 或單一 fab 支出 |
| government-incentive proceeds | 2.99 | FY2026 前九個月 | 另列的現金流入，不能冒充研發收入或產能 |
| estimated net PP&E CapEx | 約 27 | FY2026 全年估計，已扣 incentive proceeds | 前瞻公司級淨口徑，不是全年 actual |

10-Q 的申報期間截至 2026 年 5 月 28 日，早於 8 月 20 日 Labs 公告。它能教我們 Micron
本來就把 R&D expense、gross PP&E cash、incentive 與 net CapEx estimate 分開，卻不能
證明 Labs 已包含在、或排除於其中任一數字。表內 `1,316 ÷ 1,000 = 1.316`、
`3,737 ÷ 1,000 = 3.737` 只做 USD million 到 billion 的單位正規化，沒有拿它們
估計 Labs 年支出。

### 同樣寫 2027，破土與 wafer output 仍是不同時鐘

Labs 公告預期在曆年 2027 年為 Boise 研究設施破土，設施可容納數百名研究人員。較早的
10-Q 則把首座 Boise DRAM fab 的首次 wafer output 放在 2027 年中，第二座 Boise fab
放在 2028 年底，首座 New York fab 的供貨則在 2030 年及以後。地名或年份接近，不會自動
產生共同資產鍵：研究設施的 groundbreaking 是建設節點，「數百名研究人員」是人員／空間
容量；fab output 才是製造產出節點。

所以不能因兩處都出現 Boise 與 2027，就把 Labs 改名為首座 DRAM fab，也不能說研究設施
完全沒有 PP&E、試驗工具或未來技術轉移。現有兩份文件沒有共同的 project ID、資產清單、
預算或 wafer／bit 分母，最誠實的答案是先分帳、等待串接。

### 多空小作文要共用六本帳

| 本帳 | 現在已知 | 下一個可驗證節點 |
|---|---|---|
| 1. planned research envelope | 未來十年 100 億美元與研究範圍 | 同一 Labs program 的年度核准額、版本與 plan-to-actual |
| 2. 期間 R&D expense | 公司級單季與九個月費用 | Labs 分子、期間、成本類型與實際發生額 |
| 3. PP&E／CapEx 與 incentive cash | 公司級 gross cash、incentive 與全年淨估計 | Labs／facility 資產、capitalized PP&E、cash 與補助調節 |
| 4. research-facility execution | 預期 2027 破土、可容納數百名研究人員 | 許可、施工、工具安裝、啟用、staffing 與研究運作 |
| 5. technical transfer／qualification／fab capacity | 已具名 fab 各有自己的 output 時程 | 具名研究成果、產品／製程轉移、資格完成與增量 wafer／bit output |
| 6. supplier financial attribution | 公告中的供應商主管引言只屬支持性評論 | PO、order intake、具名工具出貨／驗收、供應商收入、毛利與現金 |

偏多的合理版本是：長時間窗、跨記憶體／運算／封裝／製造的研究範圍，加上大學、衛星實驗室
與生態夥伴，可能擴大 Micron 的長期技術選擇權。如果年度資金、設施、研究成果、技術轉移與
產品資格依序前進，故事會逐步變成可觀察的研發能力。現在能支持的是計畫與組織設計，不是
成功機率、量產位元或供應商收入。

偏空的合理版本是：十年 headline 尚無年度 schedule、會計分拆、工具、研究產出或
qualification，未來也可能因執行、資金與技術風險而調整。可是「目前不能分拆」也不等於
「價值為零」或「不會花錢」；那同樣超出來源。Applied Materials、Lam Research 等主管在
公告中的引言，也只是對研究合作重要性的評論，不是採購合約、得標、工具數或訂單。

多空共同的裁決方式，是每次只讓有證據的本帳前進：同一 program／facility 的 plan-to-actual
先接會計與現金，再接建置與研究成果，之後才接產品 qualification、製造 output 與供應商
財務。前一欄不能替後一欄畢業，但後一欄尚未公開也不能倒推前一欄不存在。

本段核對 `N=2` 份固定官方文件，兩份都屬 Micron 同一公司消息鏈；這是 `N=1` 家公司與
`N=1` 個 planned program，不是兩家公司的獨立樣本，且 10-Q 早於 Labs 公告。Labs 的
逐年 plan／actual、R&D／PP&E allocation、facility tools、研究成果、技術轉移、產品資格、
增量產能、供應商訂單、收入與毛利共同觀測 `N=0`。公司報告值與計畫值不是隨機抽樣，因此
沒有 sampling SE／t；本段不提供價格、估值、共識、部位、投資建議或市場是否反映的判斷。

## 保證上限不是當期支出：1,050 億美元還隔著六個時鐘

2026 年 8 月 17 日，NVIDIA 向 SEC 提交 PORTS-Pike 交易的 Form 8-K，將殘值保證列入
第 2.03 項的直接財務義務或表外安排。申報中最醒目的數字是 1,050 億美元，但文件寫的
是**初始保證協議下的累計付款義務上限**，不是 NVIDIA 在公告日已開出同額支票。要讓上限中的
一部分真的變成現金流出，仍要核對租約、生效條件、違約、資產回收與後續補償。

### 先把三個大數字放回三本帳

| 文件裡的數字 | 它屬於哪本帳 | 目前能說什麼 | 不能改寫成什麼 |
|---|---|---|---|
| 1,050 億美元 | NVIDIA 初始殘值保證的累計付款上限 | 保證責任的最外層邊界 | 當期 CapEx、已付款、建設總成本或預期損失 |
| 15 億美元 | NVIDIA 對 SB Energy 的投資 | 一筆另行揭露的股權投資 | 殘值保證已動用額、租金或整個園區成本 |
| 初始約 4.25 IT-GW；園區規劃約 8 IT-GW | 資料中心可承載的 IT 負載容量 | 專案範圍與分期建置方向 | 美元支出、收入、GPU 數量或台灣供應商訂單 |

這三列連單位都不同。15 億美元不能和 1,050 億美元相加成「NVIDIA CapEx」，約 8 IT-GW
也不能乘上一個外部假設的每 GW 成本就冒充公司申報值。SEC 附件說 SB Energy 負責 build、
own、operate，OpenAI 是 20 年租約的租戶；因此還要先辨認誰擁有資產、誰付租金、誰提供信用
支持，以及哪一方在什麼條件下才有現金責任。

### 六個時鐘：從第 0 層上限走到可能的淨現金

公告日與 1,050 億美元額度先放在**第 0 層**：它告訴我們合約存在與最大邊界，卻還不是一個
營運現金事件。之後才有六個經濟時鐘；它們也不是保證每份租約都以完全相同日期嚴格排隊。
尤其 ready-for-service 與起租是否同日、哪一項是另一項的前提，仍要等完整 Agreements form
才能逐份確認。第三個時鐘還會分岔：若 OpenAI 正常付款，後面的違約回收、補差額與補償可以
一直不被啟動。

| 時鐘 | 本案公開文件寫到哪裡 | 這一步能證明什麼 | 還不能證明什麼 |
|---|---|---|---|
| 第 0 層：公告與額度 | NVIDIA 在 8 月 17 日簽訂多份殘值保證，初始累計上限 1,050 億美元 | 合約架構與最大邊界已公開 | 每份保證都已生效，或已支付同額現金 |
| 1. ready-for-service | 出租人須先滿足場所的可服務條件；預計自 2028 年分期開始，OpenAI 也表示 completed capacity 可租時才開始付款 | 完成容量跨過可出租條件 | 所有容量已用滿、租戶已付完整租期款或 NVIDIA 保證已被請求 |
| 2. 租約起租／保證生效 | Agreement 一般在對應租約 commencement 時生效 | 指定場所的租約與保證進入適用期 | 整個約 8 IT-GW 園區同時完成，或上限成為當期現金流出 |
| 3. 租戶付款或 Trigger Event | 正常情況由 OpenAI 付租金；無力償債造成租約違約，或未付款，才是文件定義的 Trigger Event | 是否沿正常付款路徑，或進入保證救濟程序 | 一發生事件就必須支付整筆上限，或資產回收必為零 |
| 4. 重租或出售回收 | NVIDIA 可選擇承接租約、要求重租、啟動出售、允許終止，或在支付指定專案成本下延後處置最多一年 | 計算補差額前要先處理資產與替代租戶回收 | 公開摘要尚未提供實際售價、重租金額、回收時間與順位 |
| 5. NVIDIA 實際補差額 | NVIDIA 一般補「保證最低值減重租／出售回收」的差額 | 保證何時由或有責任變成實際現金付款 | 單筆付款等於 1,050 億美元上限，或等於最終淨損失 |
| 6. OpenAI 補償 | OpenAI 承諾補償 NVIDIA 實際付給出租人的金額 | NVIDIA 付款後仍有一層合約求償 | OpenAI 在壓力情境下必能立即全額補償，或 NVIDIA 已收回現金 |

所以最安全的算式不是 `保證上限 = CapEx`，而是先保留未知值。概念上，單一適用責任會先算
`max（保證最低值 − 合約認列的重租／出售回收，0）`，再受尚餘累計上限與完整合約條款約束；
這不是可以直接代入 1,050 億美元的完整法律算式。

若 NVIDIA 後來真的付款，研究上還要從實際付款另扣**實際收到**的 OpenAI 補償，才能接近
最終淨曝險；只有一紙補償承諾，仍不能先當成已回收現金。

這兩層目前都**不能代入完整數字**。8-K 明示現有描述不完整，完整 Agreements form 預計
隨截至 2026 年 7 月 26 日季度的 10-Q 提交；在逐租約最低值、期限、回收與補償能力尚未公開
前，只能確認法律摘要中的上限與瀑布，不能重算違約概率或預期損失。

### 多方小作文：信用支持可能先換來可建置的容量

偏多的讀法不是「1,050 億美元已變成營收」，而是信用支持可能幫專案先鎖住土地、電力與
建物外殼，讓 SB Energy 有條件融資並分期交付。首批 800MW 預計 2028 年可用，OpenAI 只在
completed capacity 可租時開始付款；若場所如期完成、租戶正常付款且沒有 Trigger Event，
NVIDIA 可以取得自家運算平台的長期部署機會，而殘值保證未必產生付款。這仍只是合約機制的
上行情境，公開資料沒有給 NVIDIA 因此新增多少 GPU 銷售、毛利或現金。

### 空方小作文：上限雖非支出，仍是長天期或有風險

偏空也不能只說「表外所以不用管」。8-K 把它列進第 2.03 項，相關租約最長可延續到起租後
20 年；如果 OpenAI 違約、替代租戶租金或資產售價低於保證最低值，NVIDIA 就可能需要補差額。
專案還依賴電力、輸電、許可、環境審查與融資，分期延誤也可能改變何時起租與曝險。只是現有
文件沒有保證最低值曲線、違約概率或回收率，不能把 1,050 億美元直接當成最壞情境的必然損失，
也不能自行替它估一個看似精確的預期損失。

### 多空共同裁決：每季更新六格，不用一個 headline 代替

真正能讓判斷前進的不是重複引用上限，而是逐租約更新：是否起租、多少容量已
ready-for-service、OpenAI 是否正常付款、是否發生 Trigger Event、重租或出售回收多少、
NVIDIA 實付及 OpenAI 補償多少。若第 1、2 格完成且第 3 格維持正常付款，第 4 至 6 格可以
一直不被啟動，信用支持可能只扮演建置工具。
若改走違約分支、回收不足且補償無法實現，上限內的或有責任才會逐步變成可觀察的現金風險。

本段核對 `N=3` 份官方文件，但三份都屬 PORTS-Pike 同一交易、`N=1` 條交易消息鏈，不是三個
獨立專案、三個客戶或三次違約樣本。合約金額與容量是發行人報告值，沒有抽樣母體，因此沒有
sampling SE／t；逐租約完整 form、實際起租、違約、回收、付款與補償的共同觀測 `N=0`。
本段不提供法律意見、信用評等、價格、估值、共識、部位、投資建議或市場是否反映的判斷。

## 折舊是成本碼表，不是利用率碼表

最新申報把四個時鐘再拆細了一步：資產開始分攤成本後，報表會出現折舊；但折舊增加只告訴我們
有更多或更高成本的資產正在進入損益，也可能受到耐用年限估計影響。它沒有共同的「可用 GPU
時數」或「已售算力」分母，不能直接回答容量用了幾成、哪一批設備產生多少收入，或現金何時
回收。

下表單位都是十億美元，但刻意不做加總或跨公司比率。每列同時混有**期間流量、期末存量、
尚未開始的合約與未來服務承諾**；數字並排只是辨認時鐘，不是比較規模或效率。

| 公司與最新申報 | 資產取得／存量 | 成本分攤 | 尚未開始或尚待履約 | 安全讀法 |
|---|---|---|---|---|
| Microsoft FY2026 10-K | 全年 cash PP&E additions 115.948；期末已購置尚未付款 PP&E 26.7 | 全年折舊 34.3 | 尚未起租租賃 329.1；公司 RPO 684 | cash additions 是全年流量，26.7 是期末應付存量；RPO 又涵蓋廣泛商業產品，五數沒有共同 AI 資產分母。 |
| Meta 2026 Q2 10-Q | H1 cash PP&E 49.11；6 月底 CIP 80.345 | H1 折舊 11.67 | 尚未起租租賃 278.99；期末待售資產 2.03 | CIP 是期末存量，會受轉入可使用、重分類與處分影響；不能把它當 H1 新增或可用容量。 |
| Amazon 2026 Q2 10-Q | H1 PP&E 淨新增 118.648，其中已取得未付款的增加為 20.620 | H1 PP&E 折舊攤銷 26.703 | AWS 未來服務承諾 496，收入時點由使用與履約決定 | 淨新增含非現金活動；分部成本按 usage 分攤也不是公開的容量利用率。 |

### 先辨認存量、流量與承諾

Meta 的 CIP 從 2025 年底 50.521 增至 2026 年 6 月底 80.345，機械相減是 29.824；這只是一段
期間的**淨存量變化**。同一期間還可能有新建、設備安裝、轉入可使用資產、轉為待售、處分與
其他重分類，因此不能把 29.824 改名為 H1 CapEx。S12 沒有提供能把每一項流入、流出逐筆
對回的完整 CIP rollforward，研究上就應把缺口留白。

Microsoft 的 26.7 也不是 115.948 的子期間流量：前者是 6 月 30 日仍掛在 accounts payable 的
期末存量，後者是整個財政年度已在投資現金流列出的 PP&E additions。Amazon 更直接提醒，
segment PP&E net additions 本來就含「已取得但尚未付款」的非現金活動。看到資產增加，不能
先假設現金已在同一期全數流出。

### 「按使用分攤」不是「公布利用率」

Amazon 表示 technology infrastructure assets、net additions 與折舊攤銷會按 usage 分配到
各部門，多數落在 AWS；這支持的是**成本與資產的部門歸屬規則**。申報沒有公開總可用算力、
已用算力、閒置容量、GPU 型號組合或同一時間窗，因此不能把 AWS 折舊除以 AWS 淨新增，命名
為「利用率」。分子涵蓋不同年份投入的資產，分母又含本期非現金新增，資產批次也不相同。

Microsoft 的 684 RPO 與 Amazon 的 496 AWS 未來服務承諾也不是本期新資產的收入分子。前者
涵蓋廣泛商業產品與服務；後者的收入時點還要由客戶使用與 Amazon 履約決定。兩者能證明有
未來合約需求，不能把一份多年期服務承諾逐美元配給本期新建資料中心、AI 晶片或台灣供應商。

### 建一張「資產批次護照」再談回收

若要把 CapEx 接到利用率與現金回收，同一批資產至少要有以下共同鍵；缺一欄就標示未知，
不要用公司總額代填。

| 護照欄位 | 要回答的問題 | 缺少時不能做的推論 |
|---|---|---|
| 資產批次／站點 | 哪座資料中心、哪批伺服器或哪個平台？ | 不能把不同年份與設備世代混成一批。 |
| 取得方式與日期 | 現金購置、finance lease 或其他融資；何時取得？ | 不能把非現金新增等同當期現金流出。 |
| 在建、驗收與可使用日 | 何時由 CIP 轉成可按預定用途使用？ | 不能由承諾或在建存量推定容量已上線。 |
| 折舊分類與起算 | 資產類別、耐用年限與成本何時進入損益？ | 不能把折舊變化全歸因實體容量變化。 |
| 容量與利用分母 | 可用 GPU 時數、機櫃、MW 或其他共同容量是多少？ | 不能算利用率，也不能跨公司比較。 |
| 工作負載、收入與毛利 | 哪些客戶使用、何時履約、產生多少收入與成本？ | 不能把 RPO 或雲端總營收配給這一批資產。 |
| 付款、收款與供應商共同鍵 | 買方何時付款、客戶何時付費、供應商何時出貨與收現？ | 不能重算回收期，也不能建立台灣公司財務歸因。 |

本段是三家指定發行人的最新申報 `N=3` 定向核對，不是全球 hyperscaler、資料中心或台灣
供應鏈樣本。金額是發行人依各自口徑揭露的報告值，29.824 是兩個期末存量的確定性相減；
沒有 sampling SE／t，也沒有共同 AI 資產分母。本文只判斷哪些除法與因果橋接目前不可識別，
不衡量公司 ROI、估值、投資優劣或市場是否反映。

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
- [FASB Accounting Standards Update 2016-02：Leases (Topic 842), Section A](https://storage.fasb.org/ASU%202016-02_Section%20A.pdf)（租賃初始認列、後續衡量與 principal／interest 現金流分類）。
- [FASB 2024 GAAP Taxonomy Implementation Guide：Leases under Topic 842](https://xbrl.fasb.org/ix/?doc=..%2Fimpdocs%2FLE_TIG%2Finline_f2017leasesig.htm)（虛構揭露例，不是公司或產業數據）。
- [Microsoft FY2026 Form 10-K：PP&E、折舊、未起租租賃與履約義務](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm)
- [Meta 2026 Q2 Form 10-Q：CIP、折舊、待售資產與尚未起租租賃](https://www.sec.gov/Archives/edgar/data/1326801/000162828026050705/meta-20260630.htm)
- [Amazon 2026 Q2 Form 10-Q：非現金 PP&E、分部折舊與 AWS 履約義務](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000026/amzn-20260630.htm)
- [NVIDIA 2026-08-17 Form 8-K：PORTS-Pike 殘值保證](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)（累計上限、生效條件、Trigger Event、回收、補差額、終止與 OpenAI 補償摘要）。
- [NVIDIA／SB Energy SEC Exhibit 99.1：PORTS-Pike 專案與 15 億美元投資](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)（20 年租約、分期容量與 build／own／operate；屬同一交易附件）。
- [OpenAI：PORTS-Pike 專案](https://openai.com/index/openai-joins-ports-pike-project/)（首批 800MW、completed-capacity payment 與許可／融資前提；OpenAI 是同一交易當事人）。
- [SEC：NVIDIA EDGAR Company Filings](https://www.sec.gov/edgar/browse/?CIK=1045810&owner=exclude&action=getcompany)（後續 10-Q 完整 Agreements form 與修訂的 living watch；索引本身不當固定證據）。
- [Micron：Micron Research Labs 公告，2026-08-20](https://investors.micron.com/news/press-release/2026/Micron-Unveils-Micron-Research-Labs-a-U-S--Based-Long-Horizon-Innovation-Hub-to-Shape-the-Future-of-Memory-and-AI/default.aspx)（十年 planned investment、研究範圍、合作網路與預期 2027 破土；不是年度 actual 或供應商訂單）。
- [Micron FY2026 Q3 Form 10-Q，2026-06-25](https://www.sec.gov/Archives/edgar/data/723125/000072312526000015/mu-20260528.htm)（公司級 R&D expense、PP&E cash、incentive、net CapEx estimate 與具名 fab output；申報期早於 Labs 公告）。
- [SEC：Micron EDGAR Company Filings](https://www.sec.gov/edgar/browse/?CIK=723125&owner=exclude&action=getcompany)（後續 10-Q／10-K 與 8-K 的 living watch；索引本身不證明 Labs 執行）。

**已知：** 三家公司各自的 OCF、PP&E／CapEx、租賃與 FCF 可由官方表格或法說對回；Meta 與 Amazon 的申報也直接證明合約承諾、資產狀態、使用／履約與現金時點不能合併成一個數字。FASB 文件再證明新 finance-lease ROU／liability 與償還本金是兩個不同事實。最新三份申報還把資產新增或存量、未付款、折舊、未起租租賃與履約義務分列，足以判定折舊不是利用率碼表。NVIDIA 的 8-K 又把殘值保證的累計上限、生效、ready-for-service、租戶違約、資產回收、保證人補差額與租戶補償分開，證明保證上限不能直接改名為當期 CapEx。Micron 的公告與較早 10-Q 則把十年研究計畫、期間 R&D expense、PP&E／incentive、研究設施破土及製造 fab output 放在不同文件與時鐘。

**還不知道：** CapEx 中每一項 AI 晶片、伺服器、網路、電力與建物的精確拆分，同一資產批次的在建轉入、折舊起算、容量上線、利用率、收入與現金回收，以及台灣 universe 個股的訂單與獲利份額。PORTS-Pike 也還缺逐租約保證最低值、責任排程、回收順位、違約概率、實際付款與補償結果。Micron Research Labs 另缺逐年 plan-to-actual、R&D／PP&E 與 incentive 調節、設施工具、研究產出、技術轉移、資格、增量產能及供應商財務共同鍵。

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
- **租賃雙碼表**：要求同季同時揭露新 finance-lease ROU／liability additions、principal、interest 與 modification／remeasurement；只有「含租賃」三個字仍不能跨公司比較。
- **容量變現**：Azure、AWS 與 Meta AI 產品的使用量、營收與毛利是否跟上資產上線；若容量投入增加卻無法變現，需求故事要降權。
- **分類調節**：微軟租賃分類改變後，同時看 reported CapEx 與 operating-lease cash payments，避免把分類位移誤讀為採購位移。
- **台灣公司交叉驗證**：供應商 Q2／Q3 正式文件是否出現客戶認證、出貨、存貨／應收、毛利與 OCF 的同向改善；只有營收、沒有毛利與現金，不算完整受惠。
- **兩端共同鍵**：買方與供應商能否同時指向同一平台、料號、期間、數量與驗收節點；缺任一端，就只保留需求搜尋路由，不建立題材財務歸因。
- **資產批次護照**：三家公司後續是否提供站點／設備批次、取得方式、placed-in-service、折舊分類、容量分母、工作負載、收入與現金的共同鍵；沒有共同 cohort，就不以折舊／新增資產比率冒充利用率。
- **保證六時鐘**：NVIDIA 後續 10-Q 是否提交完整 Agreements form，並逐租約揭露起租、ready-for-service、保證最低值、Trigger Event、重租／出售回收、實際補差額與 OpenAI 補償；缺少這些欄位，就不把 1,050 億美元上限改寫成預期損失。
- **Micron 六本帳**：後續 10-Q／10-K 或 Labs 更新能否把同一 program／facility 的年度計畫與實際額，接到 R&D／PP&E／incentive、施工與工具、研究產出、轉移／資格、增量產能及 supplier PO／出貨／驗收／財務；在共同鍵出現前，不把十年 100 億美元除十或改寫成 fab 與設備訂單。
