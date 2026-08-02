# 2026-08-02 市場研究雷達

這份雷達把「現在要不要先研究」與「學完能否改善整個研究框架」分成兩個軸。排名是
研究資源配置，不是個股評等；升格也只代表已達研究文章與圖譜的證據門檻，不代表投資建議。

<!-- research_radar
schema_version: 1
radar_id: RR-2026-08-02-MARKET-MAP
as_of: 2026-08-02
next_review: 2026-08-09
status: active
method: 優先級依近期一手里程碑、可證偽性、成熟度落差、修正既有錯誤與台股研究路由排序；知識價值依能否重組既有概念、減少錯誤外推及連接多個研究主題判定；保留已升格與未升格項目供回測，不以兩軸加權成假精確分數
-->

<!-- research_candidate
candidate_id: RC-HBF-COMMERCIALIZATION
rank: 2
title: HBF 從 OCP 標準化走向樣品與裝置整合
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Sandisk 與 SK hynix 已在 2026 年成立 OCP HBF workstream，而公開時程仍把 memory sample 放在 2026 下半年、device sample 放在 2027 年初，標準與產品成熟度落差可被明確追蹤
knowledge_gain: 把 NAND、logic base die、KV cache、HBM／DRAM／storage 分層與 sample／qualification 階梯連起來，避免把新記憶體名詞直接當成量產市場
first_rejection: 若 2026 下半年沒有實體 memory sample、OCP 沒有公開規格，或延遲／寫入／耐久／熱測試無法支援目標工作負載，HBF 新記憶體層與商業化速度必須下修
next_evidence: OCP specification／compliance、Sandisk 或 SK hynix 實體 sample、具名 inference device 與客戶 qualification
next_check: 2026-08-17
route: article_and_graph
article_topic_id: MI-2026-08-02-HBF-COMMERCIALIZATION-LADDER
graph_id: hbf-commercialization
sources: Sandisk and SK hynix HBF standardization => https://www.sandisk.com/company/newsroom/press-releases/2026/2026-02-25-sandisk-and-sk-hynix-begin-global-standardization-of-next-generation-memory-solution-high-bandwidth-flash-hbf | OCP semi-private workstreams => https://www.opencompute.org/community/semi-private-workstreams | SK hynix TSMC Symposium HBF architecture => https://news.skhynix.com/en/tsmc-technology-symposium-2026/
-->

<!-- research_candidate
candidate_id: RC-HIGH-NA-EUV
rank: 3
title: High-NA EUV 從工具 fleet 走向製程資格與 HVM 插入
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: ASML 已揭露八台出貨、六台運轉與 product-wafer testing，imec 又把 EXE:5200 fully qualified 目標放在 2026Q4；工具、資格與 2027–2028 客戶插入開始有可分離時鐘
knowledge_gain: 建立 shipment→operation→qualification→product wafer→HVM insertion 階梯，並把 scanner、resist、mask、metrology 與良率放回同一製程系統
first_rejection: 若 imec qualification、ASML HVM requirements 或客戶 insertion 延後，或 Low-NA multi-patterning 在成本與良率持續勝出，不能由工具出貨推導先進節點量產
next_evidence: imec 2026Q4 qualification 結果、ASML HVM readiness，以及 Intel／其他客戶的實際節點、High-NA 層數、良率與產品
next_check: 2026-10-01
route: article_and_graph
article_topic_id: MI-2026-08-02-HIGH-NA-EUV-INSERTION-LADDER
graph_id: high-na-euv-readiness
sources: ASML 2026 AGM High-NA fleet and insertion => https://ourbrand.asml.com/asset/d5e933d7-78d0-406c-aed7-a46626e63381/2026_-AGM-_presentation.pdf | imec EXE 5200 arrival and qualification target => https://www.imec-int.com/en/press/imec-receives-worlds-most-advanced-high-na-euv-system | Intel High-NA installation baseline => https://newsroom.intel.com/press-kit/intel-high-na-euv
-->

<!-- research_candidate
candidate_id: RC-CPO-PRODUCTION
rank: 7
title: CPO 從平台生產走向部署與財務驗證
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: NVIDIA 已把 Spectrum-X Ethernet Photonics 定義為進入生產，並列出 SPIL 與外部雷射角色；研究問題已從有沒有產品轉為部署分母、可插拔共存與價值量落點
knowledge_gain: 把平台產品、共同封裝光學、具名生態系、可插拔替代路徑與供應商財務認列拆成不同節點，避免以 production 一詞同步升級所有公司
first_rejection: 若後續沒有 production shipment／deployment 分母，或 Spectrum-6 長期仍由可插拔主導，CPO 快速擴散與供應鏈財務外推必須下修
next_evidence: 首批雲端採用者的交換器與埠數、CPO／pluggable 產品組合，以及日月光對 SPIL CPO 量產收入與毛利的直接揭露
next_check: 2026-08-15
route: article_and_graph
article_topic_id: MI-2026-08-01-CPO-PLUGGABLE-COEXISTENCE
graph_id: cpo-networking
sources: NVIDIA Vera Rubin and Spectrum-X production => https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Vera-Rubin-Ramps-Into-Full-Production-to-Power-Agentic-AI-Factories-Worldwide/default.aspx | Lumentum Spectrum-X laser role => https://investor.lumentum.com/financial-news-releases/news-details/2025/Lumentum-Selected-as-an-NVIDIA-Silicon-Photonics-Ecosystem-Partner-to-Advance-AI-Networking-at-Scale/default.aspx | Marvell 1.6T pluggable production => https://www.marvell.com/company/newsroom/marvell-1-6t-optical-dsp-ai-data-center-connectivity.html
-->

<!-- research_candidate
candidate_id: RC-BACKSIDE-POWER
rank: 10
title: 背面供電從研發概念進入量產時鐘
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Intel 18A 已進入生產、18A-P 進入風險生產，台積電則把 A16 量產排在 2026 下半年；技術詞已開始對應不同製造節點
knowledge_gain: 建立前段電晶體、背面供電、埋置電源軌、晶圓薄化與奈米 TSV 的因果鏈，並學會區分各晶圓代工廠不可直接相比的里程碑
first_rejection: 若台積電 A16 量產時程延後，或後續客戶產品仍不採背面供電，從製程方向外推供應鏈需求的速度必須下修
next_evidence: 台積電確認 A16 實際量產與客戶採用範圍，並由設備或材料商揭露可雙向核對的具名製程步驟
next_check: 2026-08-09
route: article_and_graph
article_topic_id: MI-2026-08-02-BACKSIDE-POWER-DELIVERY
graph_id: backside-power
sources: TSMC 2025 Annual Report => https://investor.tsmc.com/static/annualReports/2025/english/index.html | Intel Foundry 2026 VLSI update => https://newsroom.intel.com/intel-foundry/intel-foundry-details-process-milestones-future-innovation-at-vlsi-symposium | imec backside power primer => https://www.imec-int.com/en/articles/how-power-chips-backside
-->

<!-- research_candidate
candidate_id: RC-AI-MEMORY-HIERARCHY
rank: 11
title: AI 記憶體分層：HBM、SOCAMM、CXL 與 context storage
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Rubin 同時配置 HBM4 與 SOCAMM 系統記憶體，NVIDIA 另提出 CMX context tier，美光開始送樣 256GB SOCAMM2，CXL 4.0 規格也已發布
knowledge_gain: 把頻寬、容量、延遲、持久性與可共享性放回同一張分層圖，避免把所有 AI memory 需求誤讀成 HBM 的單一路徑
first_rejection: 若 SOCAMM 或 CMX 長期停在樣品／參考架構，且平台沒有可觀察的部署與軟體調度證據，新增記憶體層的商業重要性必須降級
next_evidence: Rubin 客戶部署時揭露各層容量與工作負載，SOCAMM2 由送樣轉量產，CXL 4.0 出現可核對的主機與裝置互通清單
next_check: 2026-08-10
route: article_and_graph
article_topic_id: MI-2026-08-02-AI-MEMORY-HIERARCHY
graph_id: ai-memory-hierarchy
sources: NVIDIA Vera Rubin architecture => https://developer.nvidia.com/blog/inside-the-nvidia-rubin-platform-six-new-chips-one-ai-supercomputer/ | NVIDIA CMX context memory => https://developer.nvidia.com/blog/introducing-nvidia-bluefield-4-powered-inference-context-memory-storage-platform-for-the-next-frontier-of-ai/ | Micron 256GB SOCAMM2 => https://investors.micron.com/news-releases/news-release-details/meiguangtuichuquanqiushoukuangaorongliang256gb-lpdram | CXL 4.0 overview => https://computeexpresslink.org/about-cxl/
-->

<!-- research_candidate
candidate_id: RC-OPEN-AI-FABRICS
rank: 1
title: 修正開放 AI 互連二分法：ESUN 與 SUE-T 也進入 scale-up
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: OCP ESUN 1.0 已明確把 Ethernet 帶入 scale-up，SUE-T 又處理 endpoint／transport，Arista 7060XE7 同時定位 scale-up／scale-out；現有 UALink scale-up／UEC scale-out 二分法必須立即修正
knowledge_gain: 把 UALink、ESUN、SUE-T、UEC 的 network／endpoint／transport 分工與規格、silicon、互通、產品、部署分開，並保存舊主張被新證據縮窄的修正鏈
first_rejection: 若 ESUN／SUE-T 長期沒有 multi-vendor endpoint 與 switch compliance、具名產品對應或客戶部署，Ethernet scale-up 的商業成熟度只能停在規格與產品用途
next_evidence: UALink／ESUN／SUE-T／UEC compliance、至少兩家 endpoint 與 switch silicon 互通、7060XE7 實際標準對應與部署，以及 Oracle／AMD MI450 可用狀態
next_check: 2026-08-10
route: article_and_graph
article_topic_id: MI-2026-08-02-OPEN-AI-FABRICS
graph_id: open-ai-fabrics
sources: OCP ESUN 1.0 release => https://www.opencompute.org/blog/the-ocp-esun-10-specification-has-been-released | Arista 7060XE7 scale-up and scale-out => https://investors.arista.com/Communications/Press-Releases-and-Events/Press-Release-Detail/2026/Arista-Introduces-Next-Generation-1-6Terabit-Portfolio-for-AI-Fabrics/default.aspx | UALink 2.0 release => https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf | UEC specification history => https://ultraethernet.org/specification-history/
-->

<!-- research_candidate
candidate_id: RC-HYBRID-BONDING
rank: 8
title: 細間距 hybrid bonding 與 RDL 從 PDK、試驗車走向量產資格
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: imec 在 2026 年開放 fine-pitch RDL／D2W hybrid bonding PDK，並公布 200nm W2W 接點間距試驗；設備商也將平坦度、沉積與檢查連到 3D 封裝
knowledge_gain: 能把接合間距、表面平坦度、疊對、缺陷檢查與良率學習連成一條可追蹤製程鏈，而不是只把 hybrid bonding 當成單一設備題材
first_rejection: 若證據持續只有研究試驗車與設備商產品主張，沒有客戶資格或量產良率，不能建立台灣供應商收入映射
next_evidence: 客戶資格完成、量產封裝產品、良率／throughput 邊界，以及台灣公司具名產品的雙向核對
next_check: 2026-08-16
route: article_and_graph
article_topic_id: MI-2026-08-02-HYBRID-BONDING-READINESS
graph_id: hybrid-bonding
sources: imec fine-pitch RDL and D2W PDK => https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks | imec and EVG 200nm W2W demonstration => https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record | Applied Materials 3D packaging systems => https://investors.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and
-->

<!-- research_candidate
candidate_id: RC-PANEL-LEVEL-PACKAGING
rank: 9
title: Panel-level packaging 的面積效率與量產難題
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Lam 在 2026 年建立 panel-level packaging 研發中心，Applied Materials 也透過 NEXX 交易擴大大面積封裝設備布局，但來源仍多停在 R&D 與 manufacturing readiness
knowledge_gain: 可把大型 AI 封裝的幾何利用率，與 uniformity、yield、throughput、設備尺寸及標準化約束放在同一個成本框架
first_rejection: 若 panel 尺寸、載板翹曲、均勻度或良率無法在客戶線達標，較佳面積利用率不會自動轉成較低單位成本
next_evidence: 客戶 pilot line 資格、panel 尺寸標準、量產 throughput／yield，以及實際 AI 封裝產品採用
next_check: 2026-08-23
route: article_and_graph
article_topic_id: MI-2026-08-02-PANEL-LEVEL-PACKAGING-READINESS
graph_id: panel-level-packaging
sources: Lam Panel-Level Packaging CoE => https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE | Lam wafer-to-panel manufacturing note => https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing | Applied Materials Q2 2026 results => https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-second-quarter-2026-results/
-->

<!-- research_candidate
candidate_id: RC-UCIE-3
rank: 5
title: UCIe 3.0：64G 規格、16G 跨廠 demo 與客戶產品之間的落差
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: UCIe 3.0 已定義 64 GT/s，2026 Chiplet Summit 又出現 Intel／Cadence 16G 實體跨廠 demo，Synopsys 於 6 月完成 64G IP tape-out；速度與互通階段第一次能被明確拆開驗證
knowledge_gain: 把規格、IP tape-out、回片、跨廠 demo、compliance 與客戶產品分開，避免用 16G 互通替 64G UCIe 3.0 提前畢業
first_rejection: 規格相容或單一 IP tape-out 若沒有 64G multi-vendor compliance 與實體 silicon，不構成可替換 chiplet 生態或供應商財務曝險
next_evidence: 64G test silicon 回片、第三方 compliance，以及至少兩家獨立 chiplet 的實體互通與客戶 qualification
next_check: 2026-08-17
route: article_and_graph
article_topic_id: MI-2026-08-02-UCIE-INTEROPERABILITY-LADDER
graph_id: ucie-interoperability
sources: UCIe 3.0 release => https://www.uciexpress.org/_files/ugd/8dc731_ae67289d0ec646cdba5c1aee245538b3.pdf | UCIe 2026 cross-vendor demo => https://www.uciexpress.org/post/chiplet-summit-2026-ucie-momentum-across-a-growing-ecosystem | Synopsys 64G IP tape-out => https://www.synopsys.com/blogs/chip-design/64g-ucie-ip-high-speed-die-to-die-connectivity.html
-->

<!-- research_candidate
candidate_id: RC-800V-WBG
rank: 6
title: 800VDC 內部的 Si、SiC 與 GaN 分工
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Infineon 已分別公開 GaN HV IBC 與 SiC HV BBU reference design，onsemi 把高壓 SiC 放進 SST，ROHM 則規劃 Si 與 SiC 共存於 PSU；材料分工已可由一手設計驗證
knowledge_gain: 將 800V 由單一題材拆成 SST、PSU、BBU、保護、IBC 與 point-of-load，辨認 SiC、GaN 與 Si 的功能位置及可能被 topology 移除的價值段
first_rejection: Reference design、planned adoption 與 2027 full-scale architecture 不是同一量產事件；沒有 production BOM 與客戶財務證據時不能宣稱材料勝負
next_evidence: 同一 production rack 的完整 power tree、客戶 qualification、具名料號、出貨與台灣公司可辨識財務貢獻
next_check: 2026-08-16
route: article_and_graph
article_topic_id: MI-2026-08-02-800V-POWER-SEMICONDUCTOR-PARTITION
graph_id: 800v-power-tree
sources: Infineon joins NVIDIA MGX ecosystem => https://www.infineon.com/press-release/2026/infxx202605-092 | onsemi 800V and solid-state transformer note => https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers | onsemi NVIDIA 800V collaboration => https://www.onsemi.com/company/newsroom/news-and-insights/onsemi-collaborates-with-nvidia-to-accelerate-transition-to-800-vdc-power-solutions-for-next-generation-ai-data-centers
-->

<!-- research_candidate
candidate_id: RC-GLASS-SUBSTRATE
rank: 4
title: 玻璃基板商業化：工廠、樣品、客戶可靠度與量產良率
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Intel 與 Lens Technology 於 2026-07-24 新增玻璃封裝合作，但 SKC 2026 文件顯示 Absolics 仍在 proof sample／客戶 reliability evaluation，足以修正先前 2025 HVM 預期
knowledge_gain: 建立 collaboration→pilot→proof sample→reliability→qualification→production→repeat order 階梯，並把 roadmap 滑動保存成可追溯修正，而不是只整理材料優點
first_rejection: 有工廠、CAPEX、production-ready sample 或合作公告，都不等於客戶可靠度通過、穩定 production yield 與重複出貨
next_evidence: Absolics 客戶 evaluation 結果、production yield／throughput、具名客戶或 repeat order；Intel／Lens 與 Samsung 的 sample／qualification 更新
next_check: 2026-08-14
route: article_and_graph
article_topic_id: MI-2026-08-02-GLASS-SUBSTRATE-COMMERCIALIZATION
graph_id: glass-substrate-commercialization
sources: SKC 4Q25 proof samples and reliability plan => https://www.skc.kr/upload/ir/20260212/20260212093406953002.pdf | SKC May 2026 customer evaluation => https://www.skc.kr/m/eng/Conmmunication/pr/newsDetail.do?gubun=004003&seq=1723 | Intel and Lens collaboration => https://newsroom.intel.com/new-technologies/intel-and-lens-technology-collaborate-to-enable-advanced-semiconductor-packaging-for-the-ai-era | Samsung glass substrate roadmap => https://samsungsem.com/global/newsroom/news/view.do?id=8922
-->

<!-- research_candidate
candidate_id: RC-CUSTOM-HBM
rank: 12
title: Custom HBM 與 logic base die 的客製化價值鏈
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: SK hynix 已把 custom HBM、base die 與 workload optimization 連在一起，Samsung 將 custom HBM sample 排在 2027，Micron 也公開 TSMC base logic die 與客製化方向；但三家公司所稱 custom 的範圍與產品世代尚未完全對齊
knowledge_gain: 可把標準 HBM、logic base die、foundry、記憶體供應商、accelerator co-design、qualification 與較長設計週期放進同一張價值鏈
first_rejection: 若客製化只停在供應商 roadmap、不同客戶無法重用設計、良率與成本抵消毛利，或客戶仍採標準 HBM，不能把 base die 客製化外推成普遍高價值市場
next_evidence: 具名客戶 custom HBM sample／qualification、可比較的 base die 功能定義、產品世代與量產時程，以及 foundry／memory 雙方財務揭露
next_check: 2026-09-15
route: watch_only
sources: SK hynix full-stack memory roadmap => https://news.skhynix.com/hbm-to-essd/ | Samsung commercial HBM4 and custom HBM timeline => https://news.samsungsemiconductor.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing/ | Micron HBM4E customized base logic die plan => https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02
-->

## 排名判讀

- **優先級**回答「現在先花研究時間在哪裡」；它受近期一手里程碑、可證偽性與台股路由影響。
- **知識價值**回答「研究完是否能改善其他主題的理解」；能跨記憶體、封裝、製程、網路或電源建立共同語言者較高。
- **升格**只表示文章與圖譜已能逐條查回來源。沒有客戶驗收、量產或財務資料時，圖上的公司關係仍停在規劃、樣品或相鄰搜尋路由。
- **保留觀察**也是研究結果：Custom HBM 有高知識價值，但本輪因定義、世代與具名客戶資格尚未對齊而不升格，避免雷達只留下成功候選。
