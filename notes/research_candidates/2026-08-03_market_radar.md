# 研究中心候選雷達｜2026-08-03

<!-- research_radar
schema_version: 2
radar_id: RADAR-2026-08-03
as_of: 2026-08-03
next_review: 2026-08-10
status: retired
method: 先凍結初始排行、第一拒絕條件與下一份證據，再以一手來源拆分定義、產品階段、官方驗證及部署；升格只代表值得形成可證偽研究，不代表題材成立或投資有效。
selection_cycle_id: RS-2026-08-03-01
-->

本輪先留下研究前選擇紀錄，再做深研。排行衡量的是「現在多做一小時研究，能消除多少重要
不確定性」，不是公司報酬、產業 TAM 或新聞熱度。深研後若碰到預先寫下的拒絕條件，候選可以
降回觀察或暫緩，原始排名不回填。

<!-- research_candidate
candidate_id: RC-CUSTOM-HBM
rank: 1
title: Custom HBM：同一名稱下的三種客製範圍與商用時鐘
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: Samsung 已把 2027 客戶別樣品寫入 roadmap，SK hynix 公開 base-die 運算架構，Micron 則揭露客製 base logic die 與晶圓代工分工；三條一手證據首次足以檢查市場是否把不同產品範圍誤當同一賽道。
knowledge_gain: 把容量／介面客製、base-die 邏輯客製、工作負載下放與客戶 qualification 分開，避免用「Custom HBM」一詞直接做領先排名。
first_rejection: 若深研後仍只能重述供應商 roadmap，無法分離標準 HBM4E、客製 base die、運算下放與客戶 qualification，就不升格。
next_evidence: 逐一核對 Samsung、SK hynix、Micron 對 custom HBM 的精確定義、樣品／量產時鐘、foundry 分工與具名客戶證據。
next_check: 2026-09-15
route: article_and_graph
article_topic_id: MI-2026-08-03-CUSTOM-HBM-SCOPE-LADDER
graph_id: custom-hbm-scope-ladder
sources: Samsung HBM4 and custom HBM roadmap => https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4-with-ultimate-performance-for-ai-computing | SK hynix GTC 2026 cHBM review => https://news.skhynix.com/gtc-2026-review/ | Micron FY2025 Q4 earnings slides => https://investors.micron.com/static-files/5fb98d73-2134-4446-8d1b-0f90285f6c02
-->

<!-- research_candidate
candidate_id: RC-PCIE6-COMPLIANCE
rank: 2
title: PCIe 6：產品名稱、供應商互通、官方測試與部署的四個時鐘
priority: p1
knowledge_value: high
status: promoted
evidence_posture: research_grade
why_now: PCI-SIG Workshop #140 首度提供 PCIe 6.x 64 GT/s official testing，但現行 Integrators List 仍可見 Gen6 功能產品列在 PCIe 5.0 32 GT/s 測試欄；同時 retimer 與 SSD 供應商已宣稱量產。
knowledge_gain: 建立標準／silicon／vendor interop／official compliance／platform deployment 的不可跳階框架，讓產品名與正式驗證不再混為一談。
first_rejection: 若官方測試與 integrators list 仍無法辨認 Gen6 實測層級，或只有供應商自述而沒有獨立 host／endpoint 互通，不能把 production 宣稱升格為生態系成熟。
next_evidence: 核對 PCI-SIG official testing／integrators list、retimer 與 endpoint 的實測速率、平台互通、量產與客戶部署。
next_check: 2026-08-10
route: article_and_graph
article_topic_id: MI-2026-08-03-PCIE6-COMPLIANCE-LADDER
graph_id: pcie6-compliance-ladder
sources: PCI-SIG Compliance Workshop 140 => https://pcisig.com/events/pci-sig-compliance-workshop-140 | PCI-SIG Integrators List => https://pcisig.com/developers/integrators-list | Astera Labs PCIe 6 production ramp => https://ir.asteralabs.com/news-releases/news-release-details/astera-labs-ramps-production-pcie-6-connectivity-portfolio | Micron 9650 PCIe Gen6 SSD production => https://investors.micron.com/news-releases/news-release-details/micron-high-volume-production-hbm4-designed-nvidia-vera-rubin
-->

<!-- research_candidate
candidate_id: RC-224G-ELECTRICAL-OPTICAL
rank: 3
title: 224G／1.6T：電連接 reach、功耗與光學切換邊界
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: Ethernet Alliance 已把 1.6T 與 224G 生態放入 2026 roadmap／互通展示，OIF 也同時推進 XSR、VSR、MR、LR 與 Linear；但不同 reach 的 electrical／optical 分工尚未形成共同部署口徑。
knowledge_gain: 若取得正式 IA 與可重現功耗／reach，可把 CPO、LPO、AEC、PCB 與連接器的價值路由從速度敘事改成物理邊界。
first_rejection: 若只有 roadmap 與展場 demo，沒有正式 IA／標準、可重現 reach／power 邊界與量產系統，就不建立電連接與光連接的勝負或台廠收入映射。
next_evidence: 等待 IEEE P802.3dj／OIF CEI-224G 里程碑、multi-vendor compliance、系統 BOM 與可核對的 reach／power 資料。
next_check: 2026-09-14
route: watch_only
sources: Ethernet Alliance 2026 roadmap => https://ethernetalliance.org/technology/ethernet-roadmap/ | Ethernet Alliance OFC 2026 demo => https://ethernetalliance.org/blog/2026/03/03/ai-scale-ethernet-at-the-heart-of-ethernet-alliances-ofc-2026-demo/ | OIF current CEI work => https://www.oiforum.com/technical-work/current-work/
-->

<!-- research_candidate
candidate_id: RC-CXL4-DEPLOYMENT
rank: 4
title: CXL 4.0：規格頻寬與 pooled-memory 部署代差
priority: p2
knowledge_value: high
status: watch
evidence_posture: preliminary
why_now: CXL 4.0 已公開發布並提高到 128 GT/s、bundled ports 與新 RAS 能力，但規格發布本身沒有提供 host、switch、memory device 與軟體共同 qualification 的部署分母。
knowledge_gain: 併入既有 AI memory hierarchy，追蹤規格世代與實際 CXL 2／3／4 產品、pooling 及軟體成熟度的代差。
first_rejection: 若 CXL 4.0 長期沒有 host、switch、memory device 與軟體共同 qualification，不能由規格頻寬推導部署或記憶體需求。
next_evidence: 追蹤 CXL 4.0 compliance、CXL 3.2／PCIe 6 產品 qualification、multi-host pooling 部署分母與軟體支援。
next_check: 2026-09-30
route: watch_only
sources: CXL 4.0 release => https://computeexpresslink.org/wp-content/uploads/2025/11/CXL_4.0-Specification-Release_FINAL_Website-Copy.pdf | CXL specification index => https://computeexpresslink.org/cxl-specification/ | CXL pressroom => https://computeexpresslink.org/news/
-->

<!-- research_candidate
candidate_id: RC-BYOP-GRID-TO-CHIP
rank: 5
title: BYOP／Grid-to-chip：電網排隊是否轉成現地供電架構
priority: p3
knowledge_value: medium
status: deferred
evidence_posture: assumption_led
why_now: Eaton 與 Vertiv 已把 on-site generation、BESS、UPS、液冷與 grid-to-chip 放進 AI data center 方案，但可見證據仍由解決方案供應商主導。
knowledge_gain: 若取得買方、utility、實際 MW 與運轉資料，可把「缺電」從總體題材拆成併網、融資、發電、儲能、配電與散熱節點。
first_rejection: 若沒有 hyperscaler／公用事業實際容量、併網條件與具名設備採用，供應商架構圖不足以證明 BYOP 成為主流或台股受惠。
next_evidence: 等待買方／utility 專案、實際 MW、併網與運轉資料，以及台灣公司具名產品與收入證據。
next_check: 2026-10-01
route: watch_only
sources: Eaton grid-to-chip overview => https://www.eaton.com/content/dam/eaton/products/backup-power-ups-surge-it-power-distribution/eaton-critical-power-distributed-IT-line-overview-br153163en.pdf | Vertiv and Generate BYOP collaboration => https://www.vertiv.com/en-us/about/news-and-events/corporate-news/2026/vertiv-and-generate-capital-collaborate-to-accelerate-data-center-capacity-with-complete-power-and-cooling-infrastructure/ | Vertiv BYOP and cooling architecture => https://www.vertiv.com/it-emea/insights/articles/e-book/vertiv-byopc-accelerate-grid-to-chip-ai-infrastructure/
-->

## 本輪輸出與拒絕結果

| 初始排名 | 候選 | 研究後路由 | 方法上的收穫 |
|---:|---|---|---|
| 1 | Custom HBM | 文章＋圖譜 | 同一名詞可包含不同客製功能與時鐘，先判定可比性再談排名 |
| 2 | PCIe 6 compliance | 文章＋圖譜 | product label、vendor interop、official testing、listing 與 deployment 分開 |
| 3 | 224G／1.6T | 保留觀察 | demo 尚不能替代 reach／power IA 與量產系統 |
| 4 | CXL 4.0 | 保留觀察 | 規格升版不等於共同 qualification 或 pooling 部署 |
| 5 | BYOP | 暫緩 | 供應商架構仍缺買方／utility 與可核對容量 |

本表只記錄研究路由，不計算「2/5 命中率」。升格與否由證據可否形成可證偽主張決定；真正的
方法校準要等各主題 monitor 到期後，累積支持、反證、無新證據與不可測結果。
