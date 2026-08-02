# 2026-08-02 市場研究雷達

這份雷達把「現在要不要先研究」與「學完能否改善整個研究框架」分成兩個軸。排名是
研究資源配置，不是個股評等；升格也只代表已達研究文章與圖譜的證據門檻，不代表投資建議。

<!-- research_radar
schema_version: 1
radar_id: RR-2026-08-02-MARKET-MAP
as_of: 2026-08-02
next_review: 2026-08-09
status: active
method: 優先級依近期一手里程碑、可證偽性與台股研究路由排序；知識價值依能否重組既有概念、減少錯誤外推及連接多個研究主題判定；兩軸不加權成假精確分數
-->

<!-- research_candidate
candidate_id: RC-BACKSIDE-POWER
rank: 1
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
rank: 2
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
rank: 3
title: 開放 AI 互連的分工：UALink scale-up 與 UEC scale-out
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: UALink 2.0 於 2026 年 4 月完成新一輪規格，UEC 1.0.3 於 7 月成為現行版本，AMD Helios 則把兩者放進同一個機架到資料中心架構
knowledge_gain: 釐清 GPU pod 內的 scale-up 與機架間 scale-out 是不同網路層，標準發布、產品整合與雲端部署也分屬不同成熟度
first_rejection: 若 2026 至 2027 仍沒有互通測試、商用交換器或具名雲端部署，開放標準的產業影響只能停在規格與開發階段
next_evidence: UALink／UEC 互通與合規計畫、商用晶片及交換器時程，以及 Oracle／AMD 的 MI450 叢集實際可用狀態
next_check: 2026-08-10
route: article_and_graph
article_topic_id: MI-2026-08-02-OPEN-AI-FABRICS
graph_id: open-ai-fabrics
sources: UALink 2.0 release => https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf | UEC specification history => https://ultraethernet.org/specification-history/ | AMD Helios product page => https://www.amd.com/en/products/rackscale-solutions/helios.html | Oracle and AMD deployment plan => https://newsroom.amd.com/news/oracle-and-amd-expand-partnership-to-help-customers-achieve-next-gen-ai-scale/
-->

<!-- research_candidate
candidate_id: RC-HYBRID-BONDING
rank: 4
title: 細間距 hybrid bonding 與 RDL 從 PDK、試驗車走向量產資格
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: imec 在 2026 年開放 fine-pitch RDL／D2W hybrid bonding PDK，並公布 200nm W2W 接點間距試驗；設備商也將平坦度、沉積與檢查連到 3D 封裝
knowledge_gain: 能把接合間距、表面平坦度、疊對、缺陷檢查與良率學習連成一條可追蹤製程鏈，而不是只把 hybrid bonding 當成單一設備題材
first_rejection: 若證據持續只有研究試驗車與設備商產品主張，沒有客戶資格或量產良率，不能建立台灣供應商收入映射
next_evidence: 客戶資格完成、量產封裝產品、良率／throughput 邊界，以及台灣公司具名產品的雙向核對
next_check: 2026-08-16
route: watch_only
article_topic_id:
graph_id:
sources: imec fine-pitch RDL and D2W PDK => https://www.imec-int.com/en/press/nanoic-opens-access-first-ever-fine-pitch-rdl-and-d2w-hybrid-bonding-interconnect-pdks | imec and EVG 200nm W2W demonstration => https://www.imec-int.com/en/press/imec-and-ev-group-demonstrate-wafer-wafer-hybrid-bonding-200nm-interconnect-pitch-and-record | Applied Materials 3D packaging systems => https://investors.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-new-systems-accelerate-dram-and
-->

<!-- research_candidate
candidate_id: RC-PANEL-LEVEL-PACKAGING
rank: 5
title: Panel-level packaging 的面積效率與量產難題
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: Lam 在 2026 年建立 panel-level packaging 研發中心，Applied Materials 也透過 NEXX 交易擴大大面積封裝設備布局，但來源仍多停在 R&D 與 manufacturing readiness
knowledge_gain: 可把大型 AI 封裝的幾何利用率，與 uniformity、yield、throughput、設備尺寸及標準化約束放在同一個成本框架
first_rejection: 若 panel 尺寸、載板翹曲、均勻度或良率無法在客戶線達標，較佳面積利用率不會自動轉成較低單位成本
next_evidence: 客戶 pilot line 資格、panel 尺寸標準、量產 throughput／yield，以及實際 AI 封裝產品採用
next_check: 2026-08-23
route: watch_only
article_topic_id:
graph_id:
sources: Lam Panel-Level Packaging CoE => https://newsroom.lamresearch.com/Lam-Research-Establishes-Panel-Level-Packaging-CoE | Lam wafer-to-panel manufacturing note => https://newsroom.lamresearch.com/wafer-to-panel-lam-scaling-advanced-packaging-panel-level-processing | Applied Materials Q2 2026 results => https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-announces-second-quarter-2026-results/
-->

<!-- research_candidate
candidate_id: RC-UCIE-3
rank: 6
title: UCIe 3.0 把 chiplet 互通延伸到更高速率與 UALink chiplet
priority: p2
knowledge_value: high
status: expand_existing
evidence_posture: research_grade
why_now: UCIe 3.0 已成為現行公開規格，UALink 2.0 的 chiplet specification 又明確宣告與 UCIe 3.0 相容，使封裝內與機架級互連開始出現可追蹤介面
knowledge_gain: 分辨 package 內 die-to-die、pod 內 accelerator scale-up 與機架間 scale-out 三層，並找出測試、PHY、封裝與系統整合的不同證據
first_rejection: 規格相容若沒有 multi-vendor compliance 與實體 silicon，不構成可替換 chiplet 生態或供應商財務曝險
next_evidence: UCIe 3.0 compliance、UALink chiplet 測試平台、具名 silicon 與封裝產品
next_check: 2026-08-23
route: fold_into_graph
article_topic_id: MI-2026-08-02-OPEN-AI-FABRICS
graph_id: open-ai-fabrics
sources: UCIe specifications => https://www.uciexpress.org/specifications | UALink 2.0 release => https://ualinkconsortium.org/wp-content/uploads/2026/04/UALink-2.0-Specification-PR_FINAL.pdf | UCIe resources => https://www.uciexpress.org/ucie-resources
-->

<!-- research_candidate
candidate_id: RC-800V-WBG
rank: 7
title: 800VDC 內部的 Si、SiC 與 GaN 分工
priority: p2
knowledge_value: medium
status: expand_existing
evidence_posture: preliminary
why_now: Infineon 與 onsemi 已把 SiC、GaN、hot-swap 與中間匯流排放進 NVIDIA MGX／800VDC 架構，但目前多為供應商產品與生態系主張
knowledge_gain: 將 800V 題目由單一電源規格拆成 grid-to-rack、保護、hot-swap、中間匯流排與 point-of-load，不再把所有寬能隙元件視為同一個位置
first_rejection: 若客戶長期使用 hybrid 50V 過渡方案，或 SiC／GaN 內容沒有量產與收入證據，材料分工只能停在設計機會
next_evidence: 800V 客戶驗證、具名料號、量產時間與台灣公司可辨識財務貢獻
next_check: 2026-08-16
route: expand_existing_article
article_topic_id: MI-2026-08-01-800VDC-EXECUTION-READINESS
graph_id:
sources: Infineon joins NVIDIA MGX ecosystem => https://www.infineon.com/press-release/2026/infxx202605-092 | onsemi 800V and solid-state transformer note => https://www.onsemi.com/company/newsroom/featured-stories/data-center/the-emerging-way-to-conquer-power-challenges-in-ai-data-centers | onsemi NVIDIA 800V collaboration => https://www.onsemi.com/company/newsroom/news-and-insights/onsemi-collaborates-with-nvidia-to-accelerate-transition-to-800-vdc-power-solutions-for-next-generation-ai-data-centers
-->

## 排名判讀

- **優先級**回答「現在先花研究時間在哪裡」；它受近期一手里程碑、可證偽性與台股路由影響。
- **知識價值**回答「研究完是否能改善其他主題的理解」；能跨記憶體、封裝、製程、網路或電源建立共同語言者較高。
- **升格**只表示文章與圖譜已能逐條查回來源。沒有客戶驗收、量產或財務資料時，圖上的公司關係仍停在規劃、樣品或相鄰搜尋路由。
