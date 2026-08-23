# 資料先是電、再變成光：別只問 CPO 或可插拔，要拆光引擎、訊號處理與雷射位置

<!-- research_topic
topic_id: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
schema_version: 3
status: triaged
priority: p1
captured_at: 2026-08-01
source_published_at: 2026-05-31
last_reviewed_at: 2026-08-12
review_due: 2026-08-26
source_type: mixed
publisher_domain: nvidia.com
canonical_url: https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory
source_chain_id: nvidia-cpo-production-marvell-1p6t-20260312-20260721
stock_ids: 3711
group_ids: packtest
trigger_type: product_ramp
evidence_role: candidate_source
route: market_issue_watch
thesis_claim_id: C9
base_confidence: medium
confidence_basis: OIF 正式文件把光引擎位置、訊號處理方式與雷射位置拆成可組合的設計選擇，NVIDIA 與 Marvell 又證實 CPO 與可插拔產品路徑同時存在；但 NPO／外部雷射的具名部署、多供應商互通、現場可靠度、產品配比與財務分母仍未公開
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

<!-- research_source
source_id: S8
role: standard
source_kind: document
publisher: OIF
title: Co-Packaging Framework Document
published_at: 2022-02-03
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-FD-01.0.pdf
locator: PDF pp. 9–10 的 co-packaging／socketed NPO 位置圖，以及 pp. 18–21 的 integrated／external laser、connector、loss 與 safety 討論
limitation: 這是資訊性框架文件，用來定義安排與工程取捨；不是 Implementation Agreement、產品合格報告、多供應商互通結果或客戶部署證據
independence_group: oif
-->

<!-- research_source
source_id: S9
role: standard
source_kind: document
publisher: OIF
title: 3.2T Co-Packaged Module Implementation Agreement 01.0
published_at: 2023-03-29
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-3.2T-Module-01.0.pdf
locator: 封面與 PDF p. 16；3.2T CPO module scope、外部光源耦合及 optical power／loss tolerance
limitation: IA 定義互通所需的介面與最低契約，不證明任何具名模組已通過完整 qualification、量產、客戶驗收或長期可靠度
independence_group: oif
-->

<!-- research_source
source_id: S10
role: standard
source_kind: document
publisher: OIF
title: External Laser Small Form Factor Pluggable Implementation Agreement 02.0
published_at: 2025-01-08
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/wp-content/uploads/OIF-ELSFP-02.0.pdf
locator: PDF pp. 1、3、9、52；field-replaceable blindmate ELSFP、CPO optical-engine 使用情境與 IA 未涵蓋的 application-specific optical power／noise／wavelength
limitation: 規格只建立 ELSFP 外形、管理與最低互通要求；不證明特定雷射、光引擎或交換器彼此合格，也未給現場故障率、維修時間、部署量或財務資料
independence_group: oif
-->

<!-- research_source
source_id: S11
role: standard
source_kind: living_index
publisher: OIF
title: Current OIF Work
published_at:
captured_at: 2026-08-12
accepted_at: 2026-08-12
status: active
url: https://www.oiforum.com/technical-work/current-work/
locator: 2026-08-12 capture 的 CEI-224G-Linear、Energy Efficient Interfaces 與 Co-Packaged Optics for AI Scale-Up Networks 段落
limitation: 活頁列的是 current project scope；linear、retimed、transmit-retimed、pluggable、NPO、CPO 或 COI 被納入工作範圍，不等於正式 IA 已發布、實作已互通或產品已部署
independence_group: oif
-->

<!-- research_source
source_id: S12
role: company_release
source_kind: document
publisher: Broadcom Inc.
title: Broadcom Showcases Industry-Leading Quality and Reliability of Co-Packaged Optics
published_at: 2025-10-01
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://investors.broadcom.com/node/63616/pdf
locator: 1 頁官方新聞稿；標題與正文的 one million cumulative 400G equivalent port device hours／without a single link flap、Meta high-temperature lab characterization、65% optics-power comparison，以及 footnote 指向 Meta ECOC 2025 技術評估
limitation: 這是 Broadcom 發布、引用 Meta 會議研究的單頁摘要，不含底層埠數、各埠觀察時間、交換器／光引擎／ELS 數、拓撲、軟硬體版本、link-flap 定義、其他故障、比較組樣本、功耗量測邊界或供應商財務；累計 port-device-hours 也不證明觀測彼此獨立
independence_group: broadcom-meta-cpo
-->

<!-- research_source
source_id: S13
role: other_primary
source_kind: living_index
publisher: National Institute of Standards and Technology / SEMATECH
title: e-Handbook of Statistical Methods — Constant repair rate (HPP/exponential) model
published_at:
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm
locator: §8.4.5.1 的 zero-fails case；在 HPP／exponential、固定總測試時間等條件下，零失效只有單側 MTBF 下限，公式 MTBF_lower=T/(-ln alpha)，其他情境為近似；另參 §8.1.7.1 對獨立同分布 interarrival times 與 constant rate 的 HPP 假設
limitation: 這是通用可靠度統計方法，不是 CPO、光引擎、link flap 或 Meta 測試的模型適配認證；若埠時數相關、失效率隨時間變化、故障定義漏項、觀測期間或單元異質，公式不能無條件套用
independence_group: nist
-->

<!-- research_source
source_id: S14
role: standard
source_kind: document
publisher: ITU-T
title: G Supplement 39 (10/2025) — Optical system design and engineering considerations
published_at: 2025-10-24
captured_at: 2026-08-14
accepted_at: 2026-08-14
status: active
url: https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=16678
locator: 現行 2025-10 版 134 頁官方 PDF，SHA-256 414847951f85143d7802fbbccd50ab52264b81191a66bc9f6c684471b204a49f；PDF p. 23（印刷 p. 15）界定 end-of-life worst-case sensitivity、path effects 另計與 overload，PDF pp. 60–61（印刷 pp. 52–53）列 worst-case power-budget 參數並要求 minimum received power 高於 sensitivity 加 optical path penalty；實際引用頁及前後頁 PDF pp. 22–24、59–62 已逐頁渲染核對
limitation: 這是 ITU 光傳輸系統的通用設計方法，不是 CPO、ELSFP、Ethernet、1.6T 或任一具名產品的 application specification、量測報告或互通結果；本文教材另加的 1 dB 工程裕量也不是 ITU 預設值
independence_group: itu-optical-engineering
-->

<!-- research_source
source_id: S15
role: company_release
source_kind: living_index
publisher: NVIDIA
title: Q32xx and Q34xx XDR 800Gb/s InfiniBand Switch Systems User Manual
published_at:
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://networking-docs.nvidia.com/xdrswitcheshw/
locator: Cable Installation（2026-05-14）Splitting Options 的 72 MPO／每接頭兩個 ports／144 XDR data ports／no OSFP cages 與 Q3450 CPO topology；Overview Ordering Information 的 144 XDR ports over 144 MPO connectors；Specifications（2026-08-21）的 144 MPO connectors；FRU Replacements 的 144 lasers 與一顆 laser 對一個 MPO；Introduction 的獨立 OSFP in-band management port
limitation: 同一 NVIDIA 手冊對 Q3450 前面板 MPO connectors 有未解衝突：Cable Installation 寫 72×2 ports，Overview／Specifications／FRU 指向 144×1；因此只能鎖定 144 XDR data ports、Q3450 本地 XDR data ports 不使用 OSFP cages 與支援拓撲，不能選一個 connector 數做 BOM／module 算術，也不是客戶 installed-base、實際端點配比、transceiver shipment 或財務資料
independence_group: nvidia
-->

<!-- research_source
source_id: S16
role: company_release
source_kind: living_index
publisher: NVIDIA
title: NVIDIA Silicon Photonics
published_at:
captured_at: 2026-08-23
accepted_at: 2026-08-23
status: active
url: https://www.nvidia.com/en-us/networking/products/silicon-photonics/
locator: Introduction／Lower TCO 的 CPO switch-side pluggable replacement；Products 的 Q3450 144-port listing；Powering on NVIDIA Quantum-X InfiniBand Photonics Switch 的 GB300 racks with OSFP pluggable optical modules
limitation: 活頁混合 NVIDIA 產品定位、效益 headline、產品清單與展示影片說明；只能用來追現行架構與遠端可插拔共存，不證明客戶部署占比、淨模組減量、跨架構效益、成本或財務結果
independence_group: nvidia
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
status: superseded
claim: 現有證據較支持 CPO 與 1.6T 可插拔在本階段共存，而非可插拔立即被全面取代
supporting_source_ids: S3,S4
contrary_source_ids:
as_of: 2026-07-21
basis: Spectrum-6 公開支援兩種形式，且 Marvell 同期宣告 1.6T 可插拔 DSP 大量出貨
boundary: 這是由產品組合與供應商階段推導的市場結構判讀，沒有全市場出貨占比可直接驗證
verification_needed:
corrected_by_claim_id: C9
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

<!-- research_claim
claim_id: C6
label: verified
status: active
claim: OIF co-packaging framework 把前面板可插拔、板上光引擎、socketed NPO 與同一第一層基板上的 co-packaging 畫成不同物理安排，光引擎位置因此不是只有前面板與 CPO 兩格
supporting_source_ids: S8
contrary_source_ids:
as_of: 2022-02-03
basis: S8 PDF pp. 9–10 直接描述 optical／electrical communication device 的多種安排，並把可於組裝或 rework 拆裝的共同基板 socketed arrangement 稱為 socketed NPO
boundary: 只證實 OIF 的位置分類與工程語彙，不表示所有廠商用相同定義，也不證明 NPO 已量產、具名部署或優於其他位置
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C7
label: verified
status: active
claim: CPO 光引擎與雷射光源的位置是兩個不同選擇；外部前面板雷射可把光源變成可替換單元並與交換晶片熱分離，但額外連接與光路會帶來 insertion loss、較高光功率需求，以及控制與眼睛安全責任
supporting_source_ids: S8,S10
contrary_source_ids:
as_of: 2025-01-08
basis: S8 PDF pp. 18–21 比較 integrated／external laser、connector／pigtail、loss 與 safety；S10 pp. 3、9 定義可現場替換的 blindmate ELSFP
boundary: 這些是架構取捨與標準設計目的，不是同一產品上的 A/B 測試，也沒有樣本數、故障率、修復時間、整機功耗或生命週期成本結果
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C8
label: verified
status: active
claim: OIF 3.2T CPO module 與 ELSFP Implementation Agreement 分別定義共同封裝模組及外部雷射的互通契約，但 ELSFP 02.0 明確不納入應用特定的 optical power、noise 與 wavelength，故 IA 不能替實際 link budget、產品 qualification 或部署背書
supporting_source_ids: S9,S10
contrary_source_ids:
as_of: 2025-01-08
basis: S9 建立 3.2T CPO module 的介面範圍並允許外部光源；S10 PDF p. 52 說明最低 multi-vendor interoperability 目標與刻意排除的應用特定光學條件
boundary: 只確認公開 IA 的內容邊界；未稽核任何廠商的 conformity claim、測試報告、互通矩陣或現場安裝
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C9
label: inference
status: active
claim: AI 光互連較完整的研究框架至少要拆成光引擎位置（pluggable／on-board 或 NPO／CPO）、電介面訊號處理（retimed／transmit-retimed／linear）與雷射位置（integrated／external）三個獨立決策軸；因此「CPO 對可插拔」不是一條能單獨判斷替代速度的二選一產品軸
supporting_source_ids: S3,S4,S8,S9,S10,S11
contrary_source_ids:
as_of: 2026-08-12
basis: correction_of:C2；S8–S10 把 optical-engine placement 與 laser placement 分開，S11 又把 pluggable／NPO／CPO 和 retimed／transmit-retimed／linear 同時納入能源效率工作範圍；S3／S4 保留同代具名 CPO 與可插拔商品路徑
boundary: 三軸是讀取產品組態與驗證責任的框架，不表示所有組合都可行、已標準化或已商品化，也不能推算架構市占、替代時程、每埠成本或供應商財務貢獻
verification_needed:
correction_kind: supersedes
corrects_claim_id: C2
corrected_by_claim_id:
resolution:
-->

<!-- research_claim
claim_id: C10
label: unverified
status: active
claim: 任一具名 CPO／NPO／可插拔產品已公開完整的三軸組態，並完成跨供應商 optical-engine／ELS 互通、應用 link budget、field replacement、長期可靠度、規模部署與公司財務歸因
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-12
basis: S8–S11 只提供框架、IA 與 current project scope；S1、S3、S4、S7 只提供各自產品階段或角色，沒有把同一具名產品的三軸組態、測試、部署與財務接成完整鏈
boundary: 不以 IA 存在、標準會員、ecosystem 名單、production 用語、單廠展示或可替換設計目的替代跨廠實測、客戶營運資料與財務分母
verification_needed: 公開同一產品與版本的 optical-engine placement、signal-processing mode、laser placement、link budget、互通矩陣、故障／更換／可靠度結果、部署埠數，以及買方與供應商同期間出貨與財務文件
resolution:
-->

<!-- research_claim
claim_id: C11
label: verified
status: active
claim: Broadcom 2025-10-01 官方新聞稿表示，Broadcom CPO 在 Meta 高溫實驗室 characterization 累積 100 萬個 400G-equivalent port-device-hours，期間沒有 single link flap；同稿另稱相較可插拔方案 optics power 降低 65%，但沒有公開底層分母、比較組與方法全文
supporting_source_ids: S12
contrary_source_ids:
as_of: 2025-10-01
basis: S12 標題與正文直接列 cumulative port-device-hours、零 link flap、測試環境與 65% headline；同一頁 footnote 把數據來源指向 Meta ECOC 2025 技術評估
boundary: 這只逐字保存發行人公布的特定 observation 與比較 headline；不等於零故障率、全類型無失效、現場 production deployment、所有 CPO 組態、獨立埠時數、完整 lifetime、跨架構因果比較或任何台灣供應商財務貢獻
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C12
label: verified
status: active
claim: NIST／SEMATECH 可靠度手冊指出，零失效觀測在 HPP／exponential 模型下只有單側 MTBF 下限；若總 unit test time 為 T、單側顯著水準為 alpha，則 MTBF_lower=T/(-ln alpha)，而模型要求固定失效率及相應獨立同分布失效間隔，其他資料情境的界線可能只是近似
supporting_source_ids: S13
contrary_source_ids:
as_of: 2026-08-14
basis: S13 §8.4.5.1 直接給 zero-fails 公式、單側下限與適用邊界，§8.1.7.1 另列 HPP 的 constant-rate 及 independent／identically distributed interarrival-time 假設
boundary: 這是方法主張，不替 S12 判定 port-device-hours 是否獨立、link flap 是否涵蓋所有故障、測試是否 fixed-time／repairable、失效率是否常數，也不證明 CPO 相對可插拔的可靠度或成本
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C13
label: inference
status: active
claim: 若僅作條件式量綱檢查，把 Broadcom 公布的 100 萬 port-device-hours 視為 HPP 可加總總暴露 T、link flap 為唯一且完整的失效、失效率固定且觀測可依模型處理，零事件在單側 95% 下只能支持 MTBF 下限約 333,808 port-device-hours，等價失效率上限約每 port-device-hour 2.996×10^-6；這不是 Broadcom 或 Meta 公布值，也不是產品保固
supporting_source_ids: S12,S13
contrary_source_ids:
as_of: 2026-08-14
basis: 依 S13 的 MTBF_lower=T/(-ln alpha)，代入 S12 headline T=1,000,000、alpha=0.05；Python Decimal 與 awk 兩條獨立路徑均重算為 333,808.2007 與 2.995732×10^-6
boundary: port-device-hours 可能共享交換器、光源、環境、軟體與共同故障，新聞稿也沒有每埠時長、censoring、failure taxonomy 或 raw event log；因此數字只示範零事件不能寫成零失效率，不用來跨產品排名、推估 field MTBF、年故障率、備品、營收或估值
verification_needed: Meta ECOC 2025 完整論文／資料附錄，含設備與埠數、各自時長、拓撲、版本、環境、failure／flap／UCW 定義、censoring、共同故障、所有事件與 comparison cohort
resolution:
-->

<!-- research_claim
claim_id: C14
label: verified
status: active
claim: ITU-T G Supplement 39 的 worst-case optical power budget 同時要求最大／最小發射功率、最大／最小 attenuation、最大輸入功率或 overload、minimum receiver sensitivity、optical path penalty 與目標 BER；receiver sensitivity 已按 end-of-life worst-case 納入 ageing、temperature、transmitter eye／extinction、connector degradation 與 measurement tolerance，而 path effects 仍另列，故最低接收功率必須高於 sensitivity 加 path penalty，不能只報一個雷射輸出 headline
supporting_source_ids: S14
contrary_source_ids:
as_of: 2025-10-24
basis: S14 PDF p. 23 與 pp. 60–61 直接列出 sensitivity／overload、worst-case power-budget 參數及 minimum received power 相對 sensitivity／path penalty 的關係
boundary: 這是 ITU 光傳輸方法主張，不表示其 BER、參考點、平均功率、OMA、OSNR、attenuation、penalty 或 margin 數值可直接套到 OIF CPO／ELSFP 或任一 AI 網路產品；各應用仍須使用自己的同版次契約
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C15
label: inference
status: active
claim: CPO／外部雷射的應用驗收應保存共同 reference points、wavelength／lane、power quantity、Tx min／max、path attenuation min／max、receiver sensitivity／overload、path penalty、BER／FEC、溫度老化與額外工程裕量；本文固定假想 Tx 0 至 +3 dBm、sensitivity −8 dBm、overload +1 dBm、path penalty 1 dB、另列 design margin 1 dB 時，A 的 attenuation 2.5 至 4.5 dB 使 low-power margin +1.5 dB、overload headroom +0.5 dB 而通過，B 的 4.5 至 6.5 dB 雖有 +2.5 dB overload headroom，low-power margin 卻為 −0.5 dB 而失敗，因此相同速率、發射與接收元件不能替端到端 link margin 背書
supporting_source_ids: S8,S10,S14
contrary_source_ids:
as_of: 2026-08-14
basis: S8／S10 說明 external laser、connector／pigtail 與應用特定 power／noise／wavelength 邊界，S14 提供 two-sided worst-case power-budget 方法；Python Decimal 與獨立 awk 均重算 A／B 的 minimum received power、low-power margin、maximum received power、overload headroom 與 pass／fail
boundary: A／B 是 N=2 個純假想光路設定，不是 CPO、ELSFP、Ethernet、1.6T、產品、lane、module、switch、run 或 deployment 樣本；0 至 +3、−8、+1、1 dB penalty、1 dB design margin 與 attenuation ranges 都不是任何標準預設，沒有 sampling SE／t、BER 實測、可靠度、功耗、成本、收入或公司效果
verification_needed: 同一具名 CPO／ELS 組合與版本的 application profile、reference points、wavelength／lane、mean／OMA／OSNR 定義、Tx／Rx limits、逐元件 worst-case loss、path penalty、BER／FEC、溫度／老化、raw measurements、重複／不確定度、跨廠矩陣與客戶 qualification
resolution:
-->

<!-- research_claim
claim_id: C16
label: verified
status: active
claim: NVIDIA Q3450-LD 手冊可確認 144 個 fixed four-lane XDR data ports 直接以 MPO 接單模光纖，且這些本地 XDR data ports 不使用 OSFP cages；但同一手冊對前面板是 72 個 MPO、每個承接兩個 ports，或 144 個 MPO、一對一承接，存在尚未解決的官方頁面衝突
supporting_source_ids: S15
contrary_source_ids:
as_of: 2026-08-23
basis: S15 Cable Installation 直接寫 72 MPO×每接頭兩個 ports＝144 ports，Overview／2026-08-21 Specifications 則寫 144 MPO，FRU 又寫 144 lasers 與一顆 laser 一對一映射一個 MPO；各頁對 144 XDR ports 並不衝突，且 Cable Installation 明列 Q3450 本地 XDR data ports 不使用 OSFP cages
boundary: 72／144 MPO 都不能當已裁決分母，也不能由任一版本推 module 數；no OSFP cages 只指 Q3450 的 XDR data ports，Introduction 明列全系列另有獨立 OSFP InfiniBand in-band management port，手冊亦未提供客戶安裝或出貨分母
verification_needed: NVIDIA 在同一 revision 公開一致的前面板圖、cabling／port notation、Specifications 與 FRU mapping，明確裁決每個 MPO 承接一個或兩個 XDR ports
resolution:
-->

<!-- research_claim
claim_id: C17
label: verified
status: active
claim: NVIDIA 的 Q3450 正式拓撲同時列出 CPO switch 直連另一台 CPO switch、透過 1.6T dual-port XDR transceiver 連 pluggable XDR switch，以及透過 800G single-port XDR transceiver 連 pluggable XDR HCA／compute side；因此一個 switch-side CPO data port 不代表鏈路遠端也沒有可插拔模組
supporting_source_ids: S15,S16
contrary_source_ids:
as_of: 2026-08-23
basis: S15 Q3450 CPO topology table 直接列兩個 transceiver 料號、遠端 switch／HCA 角色與可連 transceiver 或 CPO switch 的 MPO cable；S16 現行產品頁另描述 Q3450 連 GB300 racks 使用 OSFP pluggable optical modules
boundary: 這只證明 NVIDIA 支援的端點組合與展示，不證明三種路徑的客戶實際占比、每顆 dual-port 模組利用率、installed ports、出貨量、故障備品或供應商財務
verification_needed:
resolution:
-->

<!-- research_claim
claim_id: C18
label: inference
status: active
claim: CPO 與可插拔的需求或替代分析必須以逐條鏈路的 endpoint pair、transceiver part number、ports per module 與 deployed-link mix 為共同分母；不能把 Q3450 的 144 個 CPO data ports 機械換成 144、288 或零顆被取代／保留的 pluggable modules
supporting_source_ids: S15,S16
contrary_source_ids:
as_of: 2026-08-23
basis: S15 同一具名 switch 同時容許 CPO／CPO、CPO／dual-port pluggable switch 與 CPO／single-port pluggable compute 三種端點配對，且 port 與 module 分母不固定一對一；S16 同頁並列 local CPO replacement 與 remote OSFP demonstration
boundary: 逐鏈路端點護照是研究中心推論，不是 NVIDIA 標準或市場統計；目前沒有 deployed-link census、備品率、模組共用、價格、跨世代比較或供應商 shipment／財務共同鍵
verification_needed: 具名客戶以同一版本與期間公開 switch／compute topology、每條鏈路兩端、part number、ports per module、installed／active／spare counts、故障替換及採購／出貨／財務對帳
resolution:
-->

<!-- research_claim
claim_id: C19
label: unverified
status: active
claim: Q3450 客戶部署的 CPO↔CPO、CPO↔pluggable switch 與 CPO↔pluggable compute 實際配比、遠端 OSFP 數量、dual-port 使用率、淨模組減量與供應商財務貢獻已公開
supporting_source_ids:
contrary_source_ids:
as_of: 2026-08-23
basis: S15／S16 只提供支援拓撲、料號、產品定位與展示文字，沒有 installed-link census、客戶 BOM、採購、shipment 或財務分子
boundary: 未公開不等於遠端模組一定多或一定少；不以 144 ports、產品頁的 eliminate 用語、單支展示影片或 topology support 機械推估市場占比、TAM、營收或估值
verification_needed: 客戶或 NVIDIA 公開同版 endpoint-pair BOM／port census，並由 transceiver 供應商以相同期間的出貨、價格、收入與毛利雙向核對
resolution:
-->

<!-- monitoring_item
monitor_id: T1
status: retired
retired_at: 2026-08-12
retirement_reason: C2 的 CPO／pluggable 二選一框架已由 C9 的光引擎位置、訊號處理與雷射位置三軸框架取代；原產品組合與部署問題由 T3 保留較細組態後接續
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

<!-- monitoring_item
monitor_id: T3
status: active
claim_ids: C1,C6,C7,C8,C9,C10
metric: 具名 AI 光學產品的 optical-engine placement、signal-processing mode、laser placement、標準版本、跨廠互通、field replacement、可靠度與部署分母
source_ids: S1,S3,S4,S8,S9,S10,S11
watch_source_ids: S6,S11
frequency: event_driven
frequency_detail: 每兩週核對 OIF current work、平台產品與公司正式文件；出現新 IA、具名 NPO／ELS 組態、互通矩陣或客戶部署即重審
next_check: 2026-08-26
trigger: 同一具名產品首次公開三軸組態，並至少提供跨廠互通、應用 link budget、現場更換／可靠度或客戶部署分母之一
invalidation: 若後續多個產品世代仍把位置、訊號處理與雷射固定成不可拆的單一組合，且 NPO／ELS 長期沒有具名實作或互通結果，三軸作為商用產品組合框架的信心下修
-->

<!-- monitoring_item
monitor_id: T4
status: active
claim_ids: C16,C17,C18,C19
metric: Q3450／後續 CPO 部署的 CPO↔CPO、pluggable switch、pluggable compute endpoint mix，以及 part number、ports per module、installed／active／spare modules 與供應商財務共同鍵
source_ids: S15,S16
watch_source_ids: S15,S16
frequency: event_driven
frequency_detail: NVIDIA 手冊、產品頁或客戶拓撲更新時重審；首份具名 endpoint-pair BOM／port census 出現即提前核對
next_check: 2026-09-30
trigger: 客戶或平台公開逐鏈路兩端、transceiver 料號、每模組埠數、installed／active／spare counts，並能與供應商 shipment／財務同期間對帳
invalidation: 主要部署轉成 CPO↔CPO、compute side 也整合光學而使遠端 OSFP 接近零，或正式手冊移除 remote-transceiver 路徑時，下修可插拔共存與需求邊界
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
<!-- transition
date: 2026-08-12
from: triaged
to: triaged
reason: corrected_binary_optics_frame_with_engine_signal_and_laser_axes
evidence: sources:S3,S4,S8,S9,S10,S11
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: zero_link_flap_exposure_reframed_as_model_conditional_reliability_bound_without_thesis_clock_refresh
evidence: sources:S12,S13
-->
<!-- transition
date: 2026-08-14
from: triaged
to: triaged
reason: added_two_sided_worst_case_optical_power_budget_without_thesis_or_clock_refresh
evidence: sources:S8,S10,S14
-->
<!-- transition
date: 2026-08-23
from: triaged
to: triaged
reason: added_q3450_endpoint_pair_boundary_without_thesis_or_clock_refresh
evidence: sources:S15,S16
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
- **板上光學（on-board optics）**：把光引擎放在交換器電路板上、介於前面板模組與交換晶片旁之間；板上不等於與交換晶片共同封裝。
- **近封裝光學（NPO）**：把光引擎靠近交換晶片、但仍保留可分開安裝的封裝安排；OIF 也描述可在組裝或返修時拆裝的 socketed NPO。
- **外部雷射光源（ELS）**：把連續波雷射留在光引擎之外，再用另一條光路供光；光引擎靠近交換晶片，不代表雷射也必須封在旁邊。
- **ELSFP**：OIF 定義的前面板可插拔外部雷射形式，以 blindmate 光電連接器讓失效光源可在現場替換；它不是完整資料收發光模組。
- **前面板**：交換器機箱面向維修人員、安裝光模組與光纖接頭的位置。
- **連接埠**：交換器對外收送一條連線的介面；產品開始生產不等於已知部署了多少個連接埠。
- **鏈路端點（link endpoint）**：一條光連線的其中一端；判斷 CPO 是否取代可插拔模組時，必須把交換器端與另一台交換器或運算設備端分開記錄。
- **OSFP**：可插拔高速光收發器使用的一種實體外形與插槽；本文的 1.6T dual-port 與 800G single-port 是不同料號，不能把 port 數直接當 module 數。
- **MPO connector**：一次接合多芯光纖的前面板接頭；它負責把光纖接到設備，不等於接頭本身就是可插拔收發模組。
- **Q3450-LD**：NVIDIA Quantum-X800 系列的具名共同封裝光學交換器；本文只用它示範正式支援的端點配對，不把單一型號當成全市場部署樣本。
- **XDR port**：NVIDIA Q3450 手冊對其 800Gb/s InfiniBand 資料介面使用的產品語彙；XDR port 數不等於 OSFP module 數。
- **HCA（Host Channel Adapter）**：運算設備連接 InfiniBand 網路的介面卡；本文的 pluggable compute endpoint 指光纖另一端接到這類介面。
- **GB300 rack**：NVIDIA 的具名運算機櫃世代；產品頁展示它以 OSFP modules 連 Q3450，只能證明可支援／展示的遠端形式，不是客戶 installed-base。
- **高速序列介面（SerDes）**：把資料轉成高速序列電訊號並在另一端還原的電路；速度愈高，傳輸距離、耗電與訊號完整性愈難兼顧。
- **Tx／Rx**：Tx 是送出光訊號的 transmitter，Rx 是接收並解碼的 receiver；link budget 必須把 Tx 的上下限和 Rx 的太暗、太亮界線成對核對。
- **光訊號處理晶片（DSP）**：在光模組中處理高速訊號補償與轉換的晶片；晶片大量出貨不等於整體模組市場只剩一種架構。
- **重定時（retimed）**：在電介面重新判決並整理高速訊號，讓主晶片與光學端較能分開滿足訊號要求，但會增加晶片功能、功耗與驗證項目。
- **線性光學（linear optics）**：不以完整重定時把主晶片與光學端隔開，而讓兩端共同滿足訊號完整性；「線性」不等於沒有任何晶片或不需系統驗證。
- **線性可插拔光學（LPO）**：把 linear electrical interface 放進前面板可插拔形式；LPO 同時描述訊號處理與光引擎位置的特定組合，不是所有 linear optics 的總稱。
- **傳送端重定時（transmit-retimed）**：介於完整重定時與全線性之間的處理選項；名稱說的是電介面責任分配，不是光引擎一定放在哪裡。
- **1.6T**：每秒 1.6 兆位元的連線容量；它描述速度，不是固定的封裝形式、產品數量或營收。
- **雷射光源**：提供穩定光能給光引擎調變與傳輸的元件；光源位置與維修方式會影響整體設計。
- **光學損耗預算（optical loss budget）**：從雷射到接收端沿途可容許的總光功率損失；多一個連接器、分光器或耦合點，都可能吃掉一部分預算。
- **dBm**：以 1 mW 為參考的對數光功率單位，表示某個參考點上的絕對功率；`0 dBm` 是 1 mW，不是「沒有光」。
- **dB**：表示兩個功率之比或沿途損耗的對數單位；從 dBm 的發射功率減掉 dB 損耗，結果仍是接收端的 dBm。
- **光學參考點（reference point）**：指定在哪個連接器、模組端面或光路位置量功率；沒有共同參考點，即使都寫 dBm 也可能量到不同段。
- **平均光功率／OMA**：平均光功率是資料週期中的平均值；OMA 是邏輯高低光功率的調變幅度。兩者量測定義不同，不能把一個數值直接塞進另一個規格欄。
- **最小／最大發射功率**：同一發射端在規定環境與壽命條件下必須提供的下限與不得超過的上限；最小值用來防太暗，最大值還要和接收 overload 對帳。
- **接收靈敏度（receiver sensitivity）**：接收端在指定訊號品質與 BER 條件下仍能正確工作的最低輸入功率；它不是任意低功率都能解碼的承諾。
- **接收過載（receiver overload）**：接收端仍能達到指定 BER 的最高可接受輸入功率；光太強也可能失敗，因此不能只追求更高雷射輸出。
- **光路懲罰（optical path penalty）**：色散、抖動、反射等光路效應對接收需求增加的功率代價；它和連接器、光纖等 attenuation 不是同一欄。
- **光功率裕量（optical power margin）**：在共同參考點與同一功率定義下，規格可用預算扣除 worst-case attenuation、path penalty 與明列工程保留後的餘額；正值也仍要靠量測與 BER 驗收。
- **FEC（前向錯誤更正）**：接收端用冗餘碼修正部分傳輸錯誤的方法；規格必須說清 BER 是在 FEC 前還是 FEC 後，不能只寫「有 FEC」。
- **OSNR（光訊號雜訊比）**：光訊號相對光雜訊的比值；含光放大器的系統可能以 OSNR tolerance／penalty 建預算，不能和 mean power 或 OMA 混成同一欄。
- **ITU-T Supplement**：ITU-T 是國際電信聯盟的電信標準部門，Supplement 是說明設計背景與方法的補充文件；本文用它建立通用讀法，不把它冒充 CPO application profile。
- **Python Decimal／awk 雙路重算**：先用十進位精確算術、再用獨立文字運算工具重算同一固定小數；一致只證明教材算式可重現，不是兩次光學實驗或兩個樣本。
- **尾纖（pigtail）**：由元件固定帶出的短光纖；它可少一個可拆連接點，卻也會改變組裝與返修邊界。
- **盲插（blindmate）**：不用直接看見或手動對準內部接點就能插合的介面；可盲插不等於任意兩家產品已通過互通。
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
- **Port-device-hour（埠裝置小時）**：一個連接埠裝置運作一小時形成一個暴露單位；100 個埠各跑 10 小時和 1 個埠跑 1,000 小時都能加成 1,000，但共同交換器、光源、環境與軟體會讓暴露不一定獨立。
- **Link flap（連線短暫中斷）**：連線狀態短暫掉落再恢復的事件；它是可靠度事件的一類，不等於所有位元錯誤、不可校正碼字、硬體失效、效能退化或維修事件的全集。
- **右設限（right censoring）**：觀察在產品尚未失效時結束，只知道它至少活到該時點；零失效資料資訊有限，不等於後續永遠不會失效。
- **HPP（齊次卜瓦松過程）**：把修復型系統事件視為固定失效率、失效間隔獨立同分布的模型；模型可用來做條件式界線，不是資料天然具有的事實。
- **MTBF（平均故障間隔）**：在指定失效定義與模型下，修復型系統兩次故障間的平均運作時間；沒有失效時不能用「總時數 ÷ 0」得到無限大，只能報有假設的單側下限。
- **UCW（不可校正碼字）**：forward error correction 已無法修正的資料碼字；沒有 UCW 和沒有 link flap 是不同事件定義，兩者都不能單獨代表所有網路故障。
- **ECOC（歐洲光通訊會議）**：European Conference on Optical Communication 的縮寫；本文新聞稿把 100 萬埠裝置小時的技術來源指向該會議研究，但新聞稿本身不是完整論文或資料附錄。
- **生命週期成本**：從購買、耗電、維修、備品、停機到升級的總成本；不能只用單一元件價格比較。
- **客戶驗收**：營運者依功能、可靠度、維修與系統條件確認產品是否可正式使用。
- **部署分母**：判斷需求規模的共同基準，例如交換器數、連接埠數、光連線數與兩種形式的使用比例。
- **雙向核對**：平台端與供應商端文件能對上同一產品、角色、期間與量產狀態。
- **財務足跡**：能在出貨、收入、毛利或現金流中辨識的結果；生態系列名與技術合作還不算。

### 三句話抓重點

- 資料先以電訊號進入交換晶片，再轉成光訊號送往下一台設備；先問光引擎放前面板、板上／NPO，還是和晶片共同封裝。
- 再分開問電介面是重定時、傳送端重定時或線性，以及雷射整合在光引擎內還是放在外部；三個答案可以重新組合，不能濃縮成「CPO 對可插拔」。
- 最後才追同一具名產品的互通、link budget、現場更換、可靠度、部署埠數與財務分母；標準存在或產品進入生產，都不能替後面幾關背書。

### 為什麼重要

**先找「電在哪裡變成光」。** 可插拔光模組把轉換器留在前面板，板上／NPO 把它搬近但仍
保留獨立安裝邊界，共同封裝光學則把光引擎移到交換晶片的第一層基板旁。這不是一條只有新舊
兩端的直線，而是光引擎位置改變後，功耗、密度、維修、封裝與測試責任跟著重排。

**再找「誰整理電訊號、雷射又放哪裡」。** 同一個光引擎位置仍可搭配不同程度的重定時；
共同封裝的光引擎也可以使用整合或外部雷射。把雷射移到前面板可建立獨立替換邊界，卻會新增
光纖、連接器、損耗、安全與控制問題。把三軸混成一個名詞，會看不見真正失效與維修的是哪一段。

**再看誰承接每一段工作。** 平台與交換晶片團隊決定架構，光引擎與雷射提供電光轉換，封裝
測試把光學和電路整合，模組與系統團隊負責連接、維修與部署。任何一個角色被列名，都只證明
它在接力中有位置，還沒有回答數量、份額與獲利。

**最後分開標準、產品生產與公司受惠。** OIF 的框架與 IA 讓不同廠商有共同語彙和最低介面
契約，不代表某一組合已通過產品 qualification。同一世代仍可同時提供多種組態；真正要量的是
每種組態部署在哪裡、占多少連接埠、故障與維修結果如何，以及供應商的出貨、收入、毛利和現金流。

### 接下來怎麼追

- 先追平台端是否公布具名產品的光引擎位置、訊號處理方式與雷射位置，而不是只給 CPO、NPO、LPO 或 pluggable 標籤。
- 再追同一組態的 link budget、跨供應商互通、故障率、現場更換時間、交換器數與連接埠數，並由平台端和供應商端對上同一版本、期間、驗收與出貨。
- 看到「零 flap」時，先追埠數、每埠時長、交換器／光源共享結構、失效分類、事件日誌、設限與比較組，再決定能否套可靠度模型。
- 最後追日月光投控是否拆出矽品相關產能、收入、毛利與現金流；其他台灣公司沒有具名文件前，維持研究候選。

### 想一想

- 如果 CPO 光引擎使用可插拔外部雷射，光源壞掉和光引擎壞掉的更換範圍會一樣嗎？
- 兩個產品都叫 CPO，但一個完整重定時、另一個走線性介面，它們的功耗與訊號驗收責任能直接比較嗎？
- IA 已經發布，但廠商沒有公開同一應用的 link budget、互通矩陣與現場結果時，技術信心應該升到哪一層就停？
- 100 萬 port-device-hours 沒有 link flap，為什麼仍不能寫成「失效率為零」或「MTBF 無限大」？

## 先用五個位置看資料怎麼從電變成光

| 本文五個位置 | 資料現在是什麼 | 這裡負責什麼 | 主要接力角色 | 不能直接推成 |
|---|---|---|---|---|
| 1. 交換晶片內部 | 電訊號 | 決定資料要從哪個連接埠送出 | 平台、交換晶片與系統軟體 | 晶片速度更快，不等於光學架構或供應商已確定 |
| 2. 晶片到轉換器的高速電路 | 電訊號 | 把資料送到電光轉換位置 | SerDes、電路板、封裝與訊號設計 | 電路較短通常是目標，不等於已知整機節能多少 |
| 3. 電光轉換位置 | 電轉成光 | 由可插拔模組或晶片旁光引擎完成轉換 | 光引擎、DSP、驅動與矽光子 | 能完成轉換，不等於通過客戶驗收或穩定量產 |
| 4. 雷射與光纖耦合 | 光訊號 | 提供光源並把光準確送進光纖 | 雷射、光學元件、耦合、封裝與測試 | 具名雷射角色不等於獨家供應、份額或財務貢獻 |
| 5. 光纖與下一台設備 | 光訊號 | 把資料送到另一台交換器或運算設備，再轉回電 | 光纖、連接器、交換器、營運與維修團隊 | 一條連線可用，不等於整個網路都採相同形式 |

五個位置是閱讀資料流的最短路徑，不是完整交換器設計圖。真正要記住的是：第三格的光引擎
可以在前面板、板上／近封裝或共同封裝；第四格的雷射又可以留在光引擎內或移到外部。只寫
「CPO」仍沒有說完訊號如何處理、光從哪裡來，以及哪個單元能在現場更換。

## 一個 CPO 連接埠，不等於光纖兩端都沒有可插拔模組

一條光鏈路像一座橋，左右兩端各有自己的電光轉換方式。看到交換器這一端使用 CPO，只能說
**本地 data port** 不再把離散收發器插進前面板；還要再看光纖另一端接的是另一台 CPO switch、
傳統可插拔 switch，還是運算設備的可插拔網路介面。少看一端，就會把「本地少一顆模組」誤寫成
「整條鏈路兩端都沒有模組」。

NVIDIA Q3450 手冊提供一個具名例子：144 個 XDR data ports 直接以 MPO 出纖，本地 data ports
沒有 OSFP cages；但精確接頭數不能直接抄表。佈線頁寫 72 個 MPO、每個承接兩個 ports，
總覽、2026-08-21 規格頁與可更換元件對照卻指向 144 個 MPO、一對一承接。
這是同一份官方手冊尚未解決的衝突，所以本文只鎖定 144 data ports 與端點拓撲，不用 72 或
144 MPO 做模組算術。[S15] NVIDIA 現行產品頁
也一面說 CPO switch-side 取代 pluggable transceiver，一面展示 Q3450 連接使用 OSFP pluggable
optical modules 的 GB300 racks。[S16]

| 一條鏈路的端點配對 | Q3450 近端 | 光纖遠端 | 正確讀法 |
|---|---|---|---|
| CPO ↔ CPO | MPO 直接連到本地 CPO data port | 另一台 CPO switch | 這條 switch-to-switch data link 的兩端都可不放離散 data transceiver；不能外推整台設備沒有獨立管理用 OSFP |
| CPO ↔ pluggable switch | 本地 CPO | 1.6T dual-port XDR transceiver，接 pluggable XDR switch | 本地模組消失、遠端仍保留；一顆 dual-port part 可承接兩個 ports，module 與 port 不是一比一 |
| CPO ↔ pluggable compute | 本地 CPO | 800G single-port XDR transceiver，接 pluggable XDR HCA／運算端 | switch-side CPO 與 compute-side pluggable 可以同時存在；支援拓撲不等於已知部署占比 |

因此 144 CPO data ports 不是 144 顆模組被取代，也不是 288 顆兩端模組全部消失，更不是
整個網路保留零顆可插拔模組。正確分母必須落到逐條鏈路：兩端各是什麼、使用哪個料號、一顆
module 承接幾個 ports，以及三種 endpoint pairs 實際部署多少條。

一份可重建的端點配對部署護照至少要保留八欄：

| 端點護照欄位 | 要保存什麼 | 少了最容易誤判成 |
|---|---|---|
| 1. 系統與文件版本 | switch／HCA 型號、硬體與手冊 revision | 所有 CPO 世代都支援同一拓撲 |
| 2. 近端角色 | CPO、pluggable 或其他 optical-engine placement | 看到產品名就知道本地 module 數 |
| 3. 遠端角色 | CPO switch、pluggable switch 或 pluggable compute | 一端 CPO 等於兩端都 CPO |
| 4. 料號與 ports per module | transceiver、cable、connector part number 與單顆承接埠數 | port 數可以直接當 module 數 |
| 5. Installed／active links | 已安裝、實際啟用與預留鏈路各多少 | 支援一條路徑等於客戶主要採用 |
| 6. 備品與維修邊界 | spare modules、失效替換單元與修復時間 | installed 淨減量等於採購淨減量 |
| 7. 同期比較組 | 同一網路層級、速率、拓撲與世代的 baseline | 把不同 radix／架構的 module 數硬比 |
| 8. 商業共同鍵 | 客戶期間、採購、shipment、價格、收入與毛利 | 拓撲表可以直接推 TAM 或供應商獲利 |

### 多空小作文：同一份 endpoint mix，兩邊才有共同分母

- **偏多可插拔的條件**：具名客戶的鏈路多數是 CPO ↔ pluggable switch／compute，遠端料號、每模組
  埠數、installed／spare counts 與供應商 shipment 能對上；此時 CPO 改的是其中一端，不是整條鏈路歸零。
- **偏空可插拔的條件**：實際部署轉向 CPO ↔ CPO，或 compute side 也把光學整合進系統，使遠端
  OSFP 接近零；後續正式拓撲若移除 remote transceiver 路徑，也會削弱共存敘事。

本輪登錄 N=2 個 NVIDIA 官方來源紀錄（S15 是一份跨頁 living manual bundle，S16 是產品活頁），
但只有 N=1 條公司消息鏈、N=1 個 Q3450 支援拓撲，不是兩個獨立客戶或 deployment 樣本；
具名客戶 endpoint mix、installed modules、shipments 與財務
共同觀測 N=0，因此沒有 sampling SE／t，也不由支援拓撲推估模組需求、公司收入或投資結論。

## 不要把架構畫成一條線：先拆三個獨立決策軸

| 決策軸 | 常見選項 | 真正移動或改變的東西 | 先問哪個驗證問題 | 不能只看名稱推成 |
|---|---|---|---|---|
| 1. 光引擎位置 | 前面板可插拔、板上光學、NPO、CPO | 電訊號要走多遠、光引擎與主晶片共用多少封裝與散熱邊界 | 同一具名產品的實際 placement、electrical reach、組裝與更換單元是什麼 | NPO 不等於 CPO；靠近晶片也不等於雷射一定一起封裝 |
| 2. 電介面訊號處理 | retimed、transmit-retimed、linear | 重定時與補償責任留在光學端多少、主晶片與通道要共同承擔多少訊號完整性 | 同一速度、通道與誤碼條件下，DSP／retimer 功能、功耗與 pass/fail contract 是什麼 | LPO／linear 不等於沒有晶片、免測試或一定最低功耗 |
| 3. 雷射位置 | 光引擎內整合、晶片上整合、板上／前面板／機架外部光源 | 熱源、可更換單元、供光纖路、連接點、光學損耗與安全控制 | 雷射到光引擎的 power／loss budget、備援、interlock 與 field replacement 是否通過 | 外部雷射可插拔，不等於承載資料的整個光引擎也可拔換 |

OIF 的 current-work 頁把 pluggable、NPO、CPO 與 retimed、transmit-retimed、linear 同時放在
能源效率介面研究範圍；co-packaging framework 又把 optical-engine placement 與 laser placement
分開。這支持三軸閱讀法，卻不表示表中的每個排列組合都有正式 IA、可互通產品或客戶部署。

一個最容易記住的例子是：`CPO 光引擎 + 外部 ELSFP 雷射`。資料仍由交換晶片旁的光引擎調變，
所以電訊號路徑很短；ELSFP 只把連續波光送進光引擎，讓雷射故障可以在前面板更換。它沒有把
整個 CPO 光引擎搬回前面板，也沒有自動解決光學損耗、眼睛安全或跨廠互通。

## 雷射移到外部後，維修邊界與損耗一起改變

| 設計問題 | 雷射整合在光引擎 | 外部雷射／ELSFP | 下一份可裁決證據 |
|---|---|---|---|
| 故障替換 | 雷射與光引擎共用較深的維修邊界 | 光源可成為前面板 field-replaceable unit | 同型號故障模式、平均修復時間、備品與停機範圍 |
| 熱管理 | 雷射熱源靠近光引擎與交換晶片 | 可把雷射熱源與交換晶片分開 | 同一輸出條件的溫度、效率、壽命與整機冷卻結果 |
| 光學損耗 | 光路較短、連接點可較少 | 多一段供光纖路、連接器或分光可能增加 insertion loss | 從 ELS 到每顆光引擎的 power／loss budget 與最差條件 margin |
| 組裝與返修 | 整合較深，實際返修範圍看封裝設計 | connector 方便分離，pigtail 可少一個接點但改變返修方式 | connector／pigtail 的 loss、污染、插拔壽命與返修良率 |
| 控制與安全 | 仍需雷射監控與保護 | 另需跨模組控制、interlock、shutdown 與 eye-safety contract | 故障注入、斷纖／拔插情境與安全測試報告 |

OIF framework 支持的是表中的工程方向，不是統計比較。沒有同一產品、條件與樣本的失效次數、
測試時間和信賴區間，就不能宣稱外部或整合雷射「較可靠」；能說的只有它們把故障、散熱、損耗
與控制責任放在不同位置。

## 同樣速率與元件，為什麼一條光路通過、另一條失敗

`1.6T`、CPO、ELSFP 或高功率雷射都不是 link-budget 結論。速率只說每秒傳多少資料，架構名稱
只說元件大致放在哪裡；真正到接收端時，還要把發射端最弱與最強可能值、每段光路損耗、接收端
太暗與太亮的界線、path penalty，以及哪些溫度、老化與量測容差已經算過逐欄對齊。

ITU-T G Supplement 39 的 worst-case 方法把 maximum／minimum output power、maximum／minimum
attenuation、maximum input／overload、receiver sensitivity、optical path penalty 與 BER 分開；
它也明說 sensitivity 已按 end-of-life worst case 納入部分老化、溫度、發射品質、連接器退化與
量測容差，而 path effects 仍另計。[S14] 這是通用光傳輸方法，不是 CPO 規格。OIF ELSFP IA
又刻意把應用特定的 optical power、noise 與 wavelength 留在 IA 之外，所以具名 CPO／ELS 組合
仍須另外填完整應用帳。[S8][S10]

### 先畫兩道門：不能太暗，也不能太亮

以下是 `N=2` 個純假想光路，不是 CPO、ELSFP、Ethernet 或 1.6T 產品數據。兩案共用同一組
發射與接收規格，只讓 B 的 attenuation envelope 比 A 多 2 dB。

| 共同假設 | 教材固定值 | 這一欄回答什麼 |
|---|---:|---|
| 最小／最大发射平均光功率 | `0 至 +3 dBm` | 最弱與最強發射情境 |
| Receiver sensitivity | `−8 dBm` | 沒有另加 path effects 時的太暗界線 |
| Receiver overload | `+1 dBm` | 接收端仍能達指定 BER 的太亮界線 |
| Optical path penalty | `1 dB` | 另列的色散、反射、抖動等 path-effects 保留 |
| 額外 design margin | `1 dB` | 本教材明示另留的工程裕量；不是 ITU 預設值 |

在同一 average-power 定義與 reference points 下，dBm 減 dB 仍是 dBm；兩道門可寫成：

```text
P_rx,low  = P_tx,min − L_max
M_low     = P_rx,low − (receiver sensitivity + path penalty + design margin)
P_rx,high = P_tx,max − L_min
M_high    = receiver overload − P_rx,high
pass      = M_low ≥ 0 且 M_high ≥ 0
```

| 假想光路 | Attenuation min／max | 最弱接收功率 | 太暗端 margin | 最強接收功率 | Overload headroom | 結果 |
|---|---:|---:|---:|---:|---:|---|
| A | `2.5／4.5 dB` | `0−4.5 = −4.5 dBm` | `−4.5−(−8+1+1) = +1.5 dB` | `3−2.5 = +0.5 dBm` | `1−0.5 = +0.5 dB` | 兩道門皆通過 |
| B | `4.5／6.5 dB` | `0−6.5 = −6.5 dBm` | `−6.5−(−8+1+1) = −0.5 dB` | `3−4.5 = −1.5 dBm` | `1−(−1.5) = +2.5 dB` | 太暗端失敗 |

從另一種等價讀法看，發射最小值與 sensitivity 之間共有 `0−(−8)=8 dB` 的名目預算；A 的
maximum attenuation、path penalty 與明列 margin 合計 `4.5+1+1=6.5 dB`，餘 `+1.5 dB`；
B 合計 `6.5+1+1=8.5 dB`，短缺 `0.5 dB`。增加損耗會讓太亮端更安全，卻可能把太暗端推過線，
因此不能只看一個「雷射功率更高」或「短距離」標籤。

Python `Decimal` 與獨立 `awk` 浮點路徑均重算出 A 的 low／high margin 為 `+1.5／+0.5 dB`、
B 為 `−0.5／+2.5 dB`，pass 分別為 true／false。這是固定小數的確定性單位展開，不是抽樣或
光學實驗，沒有 sampling SE／t、BER observation、lane、module、switch、run、可靠度、功耗、
成本或財務效果。實際產品若用 OMA、OSNR、不同 BER／FEC 或其他 reference points，就必須換回
該應用的完整公式，不能沿用本例數字。

### 多空小作文要共用十欄光功率護照

| 十欄光功率護照 | 至少保存什麼 | 少了最容易被誤寫成 |
|---|---|---|
| 1. Application 與版本 | CPO／NPO／pluggable 組態、ELS／engine／receiver 型號、IA 與 profile 版次 | 同名架構都能互通 |
| 2. Reference points 與方向 | 從哪個 connector／module plane 到哪個 receiver plane，單向或雙向 | 不同量測位置的 dBm 可直接相減 |
| 3. Wavelength、lane 與光路 | 波長、lane 數、fiber／splitter／connector／coupling 路徑及長度 | 總速率自動等於每 lane 餘量 |
| 4. Power quantity 與單位 | mean power、OMA、OSNR 或其他定義，dBm／dB 的正負號與儀器設定 | 平均功率、調變幅度與訊噪比是同一數字 |
| 5. Tx min／max | 在指定溫度、電壓、壽命與控制模式下的上下限 | Typical 或 maximum output 能替 weakest case 背書 |
| 6. Attenuation min／max | 每個 connector、split、coupling、fiber 與污染／插拔條件的 worst-case roll-up | 一次 bench loss 就是全壽命 link loss |
| 7. Rx sensitivity／overload | 共同 BER／FEC、訊號品質與測試發射端下的太暗／太亮界線 | 靈敏度通過就不可能 overload |
| 8. Path penalty | dispersion、jitter、reflection、crosstalk、TDECQ／其他 penalty 的定義與分配 | 所有劣化都已含在 attenuation 或 sensitivity |
| 9. Inclusion map 與 margin | ageing、temperature、connector degradation、measurement tolerance 各算在哪裡，另留多少工程裕量 | 同一風險被重複扣除，或完全漏算 |
| 10. Qualification result | raw measurements、unit／lot／run、重複、量測不確定度、pass/fail、跨廠組合與客戶 sign-off | 紙上算術已等於產品合格與部署 |

**多方小作文可以寫到哪裡：** 若同一具名版本在 end-of-life／temperature corners 下，太暗與
overload margin 都為正，raw BER／FEC、跨廠 ELS—engine—receiver 組合與客戶 qualification
也重複通過，再配上 field 埠數、維修與成本資料，外部雷射或 CPO 的系統風險才真正下降。

**空方小作文可以寫到哪裡：** 若新聞只報 typical output、單一短纖 bench、maximum loss 或
「符合 IA」，卻沒有 common reference points、minimum Tx、overload、path penalty、inclusion map
與 raw BER，2 dB 的 connector／split／coupling 差異就可能吃完整個低功率 margin；架構優勢仍
可能被污染、溫漂、老化、重插與多供應商公差抵銷。

兩方應共用同一份十欄護照。工程 margin 通過仍只到 qualification 層；沒有部署分母、合格品
良率、維修成本、出貨、收入與毛利共同鍵，不能把正 dB 餘量改寫成任何台灣公司的財務受惠。

## 「100 萬小時零 flap」不是零失效率：先拆暴露、事件與模型

Broadcom 的 2025 年 10 月官方新聞稿引用 Meta 的 ECOC 2025 評估，公布 Broadcom CPO 在 Meta
高溫實驗室 characterization 累積 **100 萬個 400G-equivalent port-device-hours**，期間沒有
single link flap；同稿另稱相較可插拔方案 optics power 降低 65%。這是比「產品已進入生產」
更靠近客戶端的可靠度觀測，但仍不是一份可以直接寫成 field failure rate 或 lifetime 的完整資料集。

### 第一步：先問 100 萬究竟由什麼組成

`port-device-hours = 各埠被觀察時間的加總`。若是 100 個埠各 10,000 小時，和 10,000 個埠各
100 小時，總暴露都等於 100 萬；前者較能看長時間老化，後者較能看單元分散，兩者回答的問題
不同。若多個埠共用同一台交換器、光引擎、外部雷射、韌體、電源或高溫環境，一次共同原因也可能
同時影響多個埠，所以「加總暴露」不自動等於「100 萬次獨立觀測」。

| 可靠度護照欄位 | 新聞稿直接給什麼 | 還缺什麼 | 少了會怎麼誤讀 |
|---|---|---|---|
| 受測單元與版本 | Broadcom CPO、400G-equivalent port | 交換器、光引擎、雷射、連接器、韌體與軟體版本 | 把不同硬體或版本混成一個產品 lifetime |
| 暴露結構 | 累計 100 萬 port-device-hours | 埠數、各埠時長、同時運作比例、日曆期間與右設限 | 把很多短觀察當成少數長壽命，或反過來 |
| 環境與工作量 | Meta 高溫實驗室 characterization | 溫度分布、流量、拓撲、重啟、故障注入與 duty cycle | 把實驗室壓力觀察改寫成現場全年運轉 |
| 事件定義 | 沒有 single link flap | flap 門檻、UCW／BER、降速、告警、硬體更換與其他 failure taxonomy | 把「沒有這一類事件」寫成「沒有任何故障」 |
| 依賴與共同故障 | 未揭露 | 共享交換器、光源、電源、散熱、管理與維修群組 | 把相關埠時數當成獨立樣本而高估資訊量 |
| 比較組 | 同稿稱 optics power 較 pluggable 低 65% | 可插拔型號、埠數、流量、溫度、邊界、重複試驗與可靠度事件 | 把功耗 headline 變成可靠度因果比較 |

### 第二步：零次事件只能做有條件的單側界線

NIST／SEMATECH 手冊提醒，可靠度資料常遇到設限與缺少失效：產品愈可靠，愈難取得足夠失效來
估計整條分布。若先做一個**明示假設的量綱檢查**——把 100 萬 port-device-hours 當成 HPP 可加總
總暴露 `T`，把 link flap 當成唯一且完整的失效，並假設固定失效率、模型所需的獨立性與觀察
設計皆成立——零事件時的單側 MTBF 下限為：

```text
MTBF_lower = T / (-ln α)
單側 95%：α = 0.05，T = 1,000,000 port-device-hours
MTBF_lower ≈ 333,808 port-device-hours
等價失效率上限 ≈ 2.996 × 10^-6 / port-device-hour
```

Python `Decimal` 與 `awk` 兩條獨立路徑都得到相同結果。它不是 Broadcom 或 Meta 公布的 MTBF，
也不是保固承諾；它只示範即使暫時接受強假設，正確寫法仍是「下限／上限」，不是 `0 failures ÷
1,000,000 hours = 0 risk` 或 `1,000,000 ÷ 0 = infinite MTBF`。若共同故障、事件漏記、失效率隨
老化改變或每埠暴露異質，這個 HPP 情境甚至不能直接當成產品估計。

### 第三步：把工程結果接回多空共同裁決

**多方小作文可以寫到哪裡：** CPO 已出現客戶高溫實驗室的長累計 link-flap-free 暴露，顯示
可靠度驗證不再只停在標準與元件頁。若後續公開同版本的 field 埠數、共同故障結構、完整事件
分類、維修資料與同條件可插拔比較，且可靠度、功耗與恢復時間共同改善，CPO 的營運風險折價可
下降；再配上量產部署與供應商分子，才可能推向商業價值。

**空方小作文可以寫到哪裡：** 新聞稿只有一個供應商—客戶鏈、單一事件類型與累計暴露，沒有
raw log、比較組分母、field mix 或全部故障。若埠時數高度共享同一環境，或其他錯誤、重啟、
更換與效能退化未納入 flap，headline 可能高估可泛化可靠度；即使光學功耗較低，也可能由封裝、
備品、維修、良率與 vendor lock-in 成本抵銷。

| 共同裁決欄位 | 多方要看到 | 空方要看到 | 本輪狀態 |
|---|---|---|---|
| 暴露與獨立性 | 多台、多版本、多站點仍一致，並交代共享群組 | 暴露集中於少數系統或共同原因主導 | 只有累計 port-device-hours |
| 完整事件集合 | flap、UCW／BER、降速、重啟、更換與維修皆可重算 | headline 事件不涵蓋材料性故障或服務中斷 | 只公開 link flap |
| 同條件比較 | CPO／pluggable 固定流量、環境、版本與量測邊界 | 65% 由不同型號、流量或功耗邊界解釋 | 比較組分母未揭露 |
| 營運與財務 | field availability、MTTR、備品、每埠 TCO 與供應商 actual revenue | 封裝／維修／良率成本抵銷功耗或可靠度利益 | 尚無共同財務鍵 |

### 分母、誤差與限制

本節有 `N=2` 條消息鏈：Broadcom／Meta 是一條平台—客戶測試鏈，NIST／SEMATECH 是一條中立
方法鏈；不是 CPO 廠商、交換器、埠、站點或台灣公司的抽樣。100 萬與零 flap 是發行人公布值，
不是 repo 從 raw log 重建；333,808 與 `2.996×10^-6` 是在明示 HPP 假設下的條件式單側界線，
不報一般 sampling SE／t，也不建立 CPO／pluggable performance comparison。65% 只保留原稿
headline，不納入比較帳本，因型號、功耗邊界、樣本與重複試驗缺失。

## 再用五把尺比較三種光引擎位置

| 本文五把尺 | 前面板可插拔 | 板上／NPO | CPO | 共同要量的結果 |
|---|---|---|---|---|
| 1. 高速電路與功耗 | 電訊號走到前面板模組 | 路徑縮短，但仍跨板上或 socketed 邊界 | 光引擎與晶片共用第一層基板，目標是最短電路 | 同速同流量的電介面功耗、通道 loss、誤碼與冷卻負擔 |
| 2. 空間與頻寬密度 | 模組占前面板體積 | 光引擎離開面板但仍占板上空間 | 光學靠近晶片，面板主要承接光纖介面 | 每台有效連接埠、纖芯、封裝面積、空間與散熱配置 |
| 3. 維修與故障範圍 | 可從外部替換整個收發模組 | 要看 socket、pigtail、connector 與板級返修設計 | 光引擎整合最深，但外部雷射仍可另設替換邊界 | 元件故障率、受影響埠數、平均修復時間、備品與停機範圍 |
| 4. 升級與第二來源 | 依相容規格更換的邊界最清楚 | 需核對板級尺寸、電介面、光纖與控制 | 光學、封裝與主晶片更早共同設計 | 具名相容名單、互通矩陣、版本升級與客戶驗收 |
| 5. 製造與生命週期成本 | 模組獨立製造、測試後插接 | 新增板上組裝、耦合與返修取捨 | 封裝、散熱、光耦合、測試與已知良率更緊密 | 合格品良率、測試時間、每埠成本、耗電、維修與資本支出 |

五把尺不是宣告誰勝出。NPO 讓「移近晶片」與「完全共同封裝」之間多一個可設計的組裝／返修
邊界；外部雷射又能替 CPO 建立另一個可換單元。沒有同一部署環境的三軸組態、連接埠比例、
耗電、故障與成本資料，就不能把一個架構標籤直接換成全面替代結論。

## 四份 OIF 資料各回答不同問題

| 文件層 | 它回答什麼 | 它沒有回答什麼 |
|---|---|---|
| Co-Packaging Framework（2022） | 有哪些光引擎與雷射安排、各自會移動哪些工程責任 | 哪個產品合格、哪家互通、誰已量產部署 |
| 3.2T CPO Module IA（2023） | 3.2T CPO module 的電、光、機械、管理介面，以及外部光源耦合邊界 | 特定交換器的完整 link budget、客戶 qualification 與現場結果 |
| ELSFP IA 02.0（2025） | 可現場替換外部雷射的 form factor、blindmate 與最低多供應商互通要求 | 應用特定 optical power、noise、wavelength，以及產品配對是否 pass |
| Current OIF Work（2026-08-12 capture） | 標準組織目前正在研究哪些 placement、signal-processing 與 AI scale-up photonic interface | project 何時成為正式 IA、廠商何時實作或客戶何時部署 |

閱讀順序應是「framework 建語彙 → IA 固定介面 → 廠商用具名版本做 qualification → 多供應商互通
→ 客戶現場驗收」。前一格成立，不會自動把後一格塗綠。

## 把五類角色放回同一條光電接力

| 本文五類角色 | 它交付什麼 | 本輪具名例子 | 已證實到哪裡 | 不能外推 |
|---|---|---|---|---|
| 1. 平台與交換器產品 | 決定交換晶片、連接埠與三軸光學組態 | NVIDIA 的 Spectrum-X Ethernet Photonics 與 Spectrum-6 | 前者被公司描述為進入生產，後者同代支援可插拔與 CPO | 名稱沒有完整揭露 NPO、訊號處理、雷射位置、客戶部署數與全市場占比 |
| 2. 訊號處理與光引擎 | 依產品設計完成 retimed／linear 電介面及電光轉換 | Marvell Ara 1.6T 可插拔 DSP | 供應商表示具名可插拔 DSP 已大量出貨 | 不能把一顆 retimed pluggable DSP 的階段外推到 NPO、CPO 或所有 linear 路徑 |
| 3. 雷射與光源 | 以整合或外部方式替光引擎供光 | Lumentum 的磷化銦雷射角色；OIF ELSFP 是標準形式 | 公司公告具名生態系角色；OIF 定義 field-replaceable ELSFP | 自身公告與 IA 都不證明獨家、產品配對互通、實際出貨量、收入或毛利 |
| 4. 封裝、組裝與測試 | 把晶片、光學與電路整合並完成製造測試 | NVIDIA 列名 SPIL；ASE 文件確認集團關係 | 平台端列名與公司歸屬可雙向確認 | 列名不等於日月光新增訂單、份額或財務重大性 |
| 5. 客戶部署與營運 | 決定連線位置、驗收、備援、維修與實際使用比例 | 本輪來源沒有可重算的部署分母 | 尚未確認交換器數、連接埠比例與營運結果 | 首批採用名單或展示不能改寫成規模部署 |

角色表說明「誰負責哪一段」，不是完整供應商名單。只有 SPIL 的封裝、組裝與測試角色由
NVIDIA 直接列名並可由 ASE 文件確認公司歸屬；Lumentum 是自身公告的雷射角色；Marvell
用來證明具名可插拔 DSP 路徑仍在出貨。OIF 文件只建立共同語彙與介面，不替任何供應商列名；
其他台灣公司不得借用標準或這三組公司證據升級。

## 產品時鐘不是一條「誰取代誰」的時鐘

NVIDIA 把 Spectrum-X Ethernet Photonics 描述為進入產品生產，又說 Spectrum-6 同代支援
可插拔與共同封裝兩種形式；Marvell 同期表示 Ara 1.6T 可插拔 DSP 已大量出貨。這三份一手
資料仍支持「本階段多條路並存」，卻沒有告訴我們各產品的 NPO／CPO placement、retimed／linear
處理、integrated／external laser 組態，也沒有各占多少交換器、連接埠、收入或網路資本支出。

因此可比較的是各自產品時鐘：具名共同封裝平台已被描述為進入生產，可插拔也有具名晶片大量
出貨。不能做的是只用其中一軸排列長期勝負；即使未來 CPO 埠數增加，外部雷射、linear 介面或
socketed NPO 的價值分配仍可能不同，更不能把平台生產直接改寫成台灣供應商財務貢獻。

## 最後用七關分開標準、產品、部署與公司受惠

| 本文七關 | 這一關要證明 | 本輪可確認到哪裡 | 下一份證據 | 不能外推 |
|---|---|---|---|---|
| 1. 三軸組態可辨識 | 同一具名產品說清光引擎位置、訊號處理與雷射位置 | OIF 提供分類；NVIDIA／Marvell 的公開產品資料未完整填滿三軸 | 產品 block diagram、BOM、介面與可更換單元 | 只寫 CPO、NPO、LPO 或 pluggable 不等於組態完整 |
| 2. 標準與應用契約閉合 | 正式 IA、應用 link budget、管理、安全與版本彼此對得上 | 3.2T CPO 與 ELSFP IA 已發布；應用特定 power／noise／wavelength 仍在 IA 外 | 具名產品的 IA 版本、loss budget、control／safety 與 pass criteria | IA 發布不等於產品合格或任意兩家互通 |
| 3. 產品進入持續生產 | 具名產品從路線圖走到持續製造或大量出貨 | NVIDIA 描述 CPO 產品進入生產；Marvell 描述可插拔 DSP 大量出貨 | 實際出貨數、版本、qualification、退貨與故障資料 | 各公司 production 用語不能當共同量尺 |
| 4. 供應商角色能雙向核對 | 平台端與供應商端對上同一產品、角色與公司 | SPIL 角色與集團關係可核對；Lumentum 有自身具名雷射公告 | 平台與供應商共同確認料號、組態、期間與量產角色 | 生態系列名不能改寫成份額、獨家或訂單金額 |
| 5. 互通、客戶驗收與部署分母出現 | 同一組態跨廠可用，且知道用在哪些連線與多少埠 | 尚無完整互通矩陣、field result、交換器數與三軸組態比例 | 跨廠組合、客戶驗收、埠數、故障率、修復時間與耗電 | 展示、blindmate 或首批採用者不等於規模部署 |
| 6. 供應商出貨、份額與價格可辨識 | 具名供應商有出貨量、單價、份額、產能利用與重複訂單 | 現有來源沒有 SPIL 或 Lumentum 的產品分母 | 公司與客戶文件對上同期間組態與量產出貨 | 平台產品生產不能直接換算供應商營收 |
| 7. 收入、毛利與現金流留下來 | 新增製造內容能接回公司收入、成本、毛利與現金流 | 日月光尚未拆出 Spectrum-X／CPO 的財務貢獻 | 具名產品收入、成本、毛利、資本支出與收款 | 營收成長不等於扣除良率、設備與維修成本後仍受惠 |

本輪框架與 IA 能到第一、二關，兩條具名產品路徑各自走到第三關；SPIL 與 Lumentum 最多提供
第四關的角色線索，尚未通過第五到第七關。七關是證據排序，不是技術排名、供應商名單、營收
預測或投資建議。

## 這篇對公司判斷的用處與界線

日月光投控是目前可追的台灣公司入口，因為 NVIDIA 直接列名旗下 SPIL 負責 CPO 晶片級封裝、
組裝與測試；這能確認角色，卻沒有回答產品出貨量、產能利用、收入占比、毛利與資本回報。
頎邦與訊芯等既有研究候選沒有被本輪平台或可插拔文件列名，仍要依自己的正式文件補齊客戶、
料號、驗收與財務證據。

因此研究下一步不是把所有光通訊或矽光子公司排成受惠名單，而是沿七關尋找完整組態、互通、
部署分母、雙向核對與公司財務足跡。在第五到第七關出現前，本文不支持個股排序、營收推估或
投資動作。

## 來源與證據邊界

- [NVIDIA：Vera Rubin 與 Spectrum-X Ethernet Photonics 進入生產，2026-05-31](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)
- [NVIDIA GTC Taipei：列名 TSMC、SPIL、TFC、Foxconn 的製造角色，2026-06-01 更新](https://blogs.nvidia.com/blog/nvidia-gtc-taipei-computex-2026-news/)
- [NVIDIA：Spectrum-6 同時支援可插拔與 CPO，2026-07-21](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)
- [NVIDIA：Q32xx／Q34xx XDR Switch Systems User Manual](https://networking-docs.nvidia.com/xdrswitcheshw/)（同一手冊的佈線頁寫 72 MPO×2 ports，總覽／規格／可更換元件頁指向 144 MPO×1；衝突未裁決。144 XDR data ports、Q3450 本地 XDR data ports 不使用 OSFP cages 與三種端點拓撲仍可確認）。
- [NVIDIA：Silicon Photonics 產品與展示入口，2026-08-23 capture](https://www.nvidia.com/en-us/networking/products/silicon-photonics/)（同頁分開 local CPO replacement 與 Q3450 連 GB300 racks 的 remote OSFP modules；不是 deployment census）。
- [Marvell：Ara 1.6T 可插拔 DSP 大量出貨，2026-03-12](https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html)
- [ASE：SPIL 為日月光投控子公司，2025-01-16](https://www.aseglobal.com/press-room/spil-hosts-nvidia-founder-and-ceo-at-new-factory-site/)
- [Lumentum：Spectrum-X Photonics 的具名 InP laser 生態系角色，2025-03-18](https://investor.lumentum.com/financial-news-releases/news-details/2025/Lumentum-Selected-as-an-NVIDIA-Silicon-Photonics-Ecosystem-Partner-to-Advance-AI-Networking-at-Scale/default.aspx)
- [OIF：Co-Packaging Framework Document，2022-02-03](https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-FD-01.0.pdf)（pp. 9–10、18–21：光引擎／雷射位置、connector、loss 與 safety）。
- [OIF：3.2T Co-Packaged Module IA 01.0，2023-03-29](https://www.oiforum.com/wp-content/uploads/OIF-Co-Packaging-3.2T-Module-01.0.pdf)（p. 16：外部光源與 optical loss tolerance）。
- [OIF：ELSFP IA 02.0，2025-01-08](https://www.oiforum.com/wp-content/uploads/OIF-ELSFP-02.0.pdf)（pp. 3、9、52：field replacement、blindmate 與規格排除項）。
- [OIF：Current Work，2026-08-12 capture](https://www.oiforum.com/technical-work/current-work/)（pluggable／NPO／CPO、retimed／transmit-retimed／linear 與 AI scale-up photonic interface 工作範圍）。
- [Broadcom：Meta 測試的 100 萬個 400G-equivalent port-device-hours／零 link flap，2025-10-01](https://investors.broadcom.com/node/63616/pdf)（1 頁官方新聞稿與 ECOC 研究註腳；不是 raw event log 或 field lifetime study）。
- [NIST／SEMATECH：HPP／exponential zero-fails confidence bound](https://www.itl.nist.gov/div898/handbook/apr/section4/apr451.htm)（通用可靠度方法與條件，不是 CPO 模型適配認證）。
- [ITU-T：G Supplement 39 (10/2025) Optical system design and engineering considerations，2025-10-24](https://www.itu.int/ITU-T/recommendations/rec.aspx?lang=en&rec=16678)（PDF p. 23、pp. 60–61：end-of-life worst-case sensitivity／overload、power-budget 參數與 path penalty；是通用光傳輸方法，不是 CPO application profile）。

**已知：** OIF 文件證實光引擎位置、訊號處理與雷射位置必須分開閱讀，且 IA 只覆蓋指定互通
邊界；NVIDIA 將具名共同封裝產品描述為進入生產並直接列名 SPIL，Spectrum-6 與 Marvell 的
資料也證明可插拔路徑仍在同代產品與量產生態中。Q3450 正式手冊再證明本地 CPO data port
可連另一台 CPO switch，也可連遠端 pluggable switch／compute，且 dual-port／single-port part
讓 port 與 module 分母不同。Broadcom／Meta 另新增一筆客戶高溫實驗室的
累計 100 萬 port-device-hours／零 link-flap 觀測，但正確統計解讀仍需模型與底層分母。ITU 方法
再確認 link budget 必須同時保存最小／最大发射、最小／最大 attenuation、sensitivity／overload、
path penalty 與 BER，而不是用雷射輸出或架構標籤代替端到端驗收。

**還不知道：** 具名產品完整三軸組態、NPO／ELS 實際部署、應用 link budget、跨廠互通、
共同 reference points／power quantity／inclusion map／兩端 margin、field replacement 與完整長期
可靠度結果、各埠暴露／共同故障／事件日誌、同條件比較組、
Q3450 前面板究竟是 72 MPO×2 ports 或 144 MPO×1 port、Q3450／後續 CPO 的 endpoint-pair mix、
遠端 OSFP installed／active／spare counts、dual-port 利用率、
淨模組減量、各組態出貨配比、每埠成本、台灣供應商收入與毛利，
以及 6147、6451 是否參與上述具名平台。

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
action_due: 2026-08-26
rationale: SPIL 被 NVIDIA 直接列為 CPO 封裝組裝測試夥伴；新 OIF 三軸框架要求再固定具名產品組態、互通與部署，並由日月光投控正式文件裁決量產收入與獲利。
evidence_boundary: OIF framework／IA、平台 production 與生態系列名都不等於 3711 已有可量化新增訂單；不建立收入、市占或毛利事實，6147與6451僅保留在正文的既有 H# 複核清單。
-->

## 下一個可證明／否定的節點

- **端點層**：NVIDIA 是否先在同一 revision 裁決 Q3450 的 72／144 MPO 衝突；客戶或平台是否再公布每條鏈路的近端／遠端角色、transceiver 料號、ports per module、installed／active／spare counts。只公布 CPO port 數仍不能估算淨模組變化。
- **組態層**：具名產品是否同時公布 optical-engine placement、signal-processing mode 與 laser placement；只有一個 CPO／NPO／LPO 標籤就不算填滿。
- **互通層**：3.2T CPO module、ELSFP 與應用 link budget 是否由多家產品在同一版本與條件下，以共同 reference points、mean／OMA／OSNR 定義、Tx／Rx limits、逐段 attenuation、path penalty、inclusion map、兩端 margin 與 raw BER 完成互通、故障注入、field replacement 與長期可靠度。
- **可靠度層**：Meta ECOC 2025 完整論文或資料附錄能否補上 100 萬 port-device-hours 的埠數、各埠時長、共同故障群組、版本、所有事件與比較組；只有零 link-flap headline 不能估 field lifetime。
- **平台層**：首批雲端採用者是否公布各三軸組態的交換器數、部署位置、可靠度、修復時間或節能實際值；若只停在 IA、展示或少量部署，量產解讀不升級。
- **公司層**：3711 是否拆出光電共同封裝的收入／毛利；6147、6451 是否由送樣或小量生產轉為正式量產收入。沒有公司文件，就不把平台證據寫進正式筆記事實。
- **經濟層**：新增封裝與測試內容量是否高於所需資本支出、良率爬坡與維修成本；若收入增加但毛利、現金流未改善，受惠只停在營收表面。
