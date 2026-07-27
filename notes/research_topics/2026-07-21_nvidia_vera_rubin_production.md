# NVIDIA Vera Rubin 由路線圖進入量產與首波部署

<!-- research_topic
topic_id: MI-2026-07-21-NVIDIA-VERA-RUBIN-RAMP
schema_version: 1
status: triaged
priority: p1
captured_at: 2026-07-27
source_published_at: 2026-07-21
last_reviewed_at: 2026-07-27
review_due: 2026-08-03
source_type: official_company
publisher_domain: nvidia.com
canonical_url: https://blogs.nvidia.com/blog/vera-rubin/
source_chain_id: nvidia-vera-rubin-20260721
stock_ids: 2376,2382,3231,6669
group_ids: memory,pcb,powersupply,serverodm,thermal
trigger_type: product_ramp_and_deployment
evidence_role: candidate_source
route: market_issue_watch
-->

<!-- transition
date: 2026-07-27
from: initial
to: inbox
reason: weekly_primary_source_scan
evidence: source_chain:nvidia-vera-rubin-20260721
-->
<!-- transition
date: 2026-07-27
from: inbox
to: triaged
reason: cross_group_mapping_completed_with_explicit_evidence_boundaries
evidence: source_chain:nvidia-vera-rubin-20260721
-->

## 為何值得進佇列

NVIDIA 7 月 21 日已把 Vera Rubin 描述從「規劃採用」推進到 NVL72 量產爬坡、合作夥伴
機架運行與 350 多個 AI factory site 的供應鏈部署；Spectrum-6 也被描述為已進入首批
gigascale AI factories。這是供應鏈時程的重要變化，值得檢查現有小作文是否仍停留在
「未量產／僅路線圖」的舊前提。

## 來源與證據邊界

- [Vera Rubin 量產與部署](https://blogs.nvidia.com/blog/vera-rubin/)（NVIDIA，2026-07-21）。
- [Spectrum-6 首波導入](https://blogs.nvidia.com/blog/nvidia-spectrum-six-arrives-in-gigascale-ai-factories/)（NVIDIA，2026-07-21）。
- [NAVER／NVIDIA／Brookfield 韓國 AI factory 擴建提案](https://investor.nvidia.com/news/press-release-details/2026/NAVER-NVIDIA-and-Brookfield-to-Expand-Koreas-National-AI-Factory-Infrastructure-Buildout/default.aspx)（NVIDIA，2026-07-24；含非拘束性條款與條件）。
- [SK Group／NVIDIA AI factory 與 HBM 合作意向](https://investor.nvidia.com/news/press-release-details/2026/SK-Group-and-NVIDIA-Expand-Strategic-Partnership-Across-AI-Factories-and-Next-Generation-Memory/default.aspx)（NVIDIA，2026-07-24；LOI／計畫，不是已交付訂單）。
- [NVIDIA 先前列名的台灣 Vera 系統廠](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Unveils-Vera-the-CPU-for-Agents/default.aspx)（NVIDIA，2026-05-31）包含 GIGABYTE、QCT、Wistron、Wiwynn。

上述資料只證實 NVIDIA 平台與其公開列名生態系。它沒有披露技嘉、廣達、緯創或緯穎的
新增訂單、單價、出貨占比或獲利；也沒有點名本 universe 的散熱、PCB、電源或記憶體個股。
SK hynix 的 HBM 合作尤其不能外推為台灣傳統 DRAM 廠的直接受惠證據。

## 影響路由

<!-- impact
group_id: serverodm
stock_ids: 2376
direction: tailwind
hypothesis_refs:
note_action: done
action_due:
rationale: 已把技嘉小作文中未加日期限定的「Rubin 仍在 early-stage」改回 5/15 公司法說的歷史切面，並收窄公司級驗證節點
evidence_boundary: 正式筆記的 5/15 歷史紀錄與 H1 均未改；NVIDIA 平台 ramp 不證實技嘉新增訂單、收入或毛利
-->

<!-- impact
group_id: serverodm
stock_ids: 2382,3231,6669
direction: tailwind
hypothesis_refs:
note_action: review_due
action_due: 2026-08-03
rationale: 三份小作文沒有過時的 Rubin 階段敘述，只需在下一公司 IR 檢查驗證、量產、客戶驗收與財務認列
evidence_boundary: QCT、Wistron、Wiwynn 被列入生態系不等於個別公司新增訂單、收入或毛利
-->

<!-- impact
group_id: thermal
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: Spectrum-6 與 Vera Rubin 公告明確提到液冷及高溫進水設計，可能改變散熱內容量
evidence_boundary: NVIDIA 未在這批公告點名 universe 散熱供應商
-->

<!-- impact
group_id: pcb
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: 更高密度互連與交換器量產構成檢查高階板需求的產業觸發
evidence_boundary: 未有公司層級料號、份額或訂單證據
-->

<!-- impact
group_id: powersupply
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: 大型 AI factory 與每瓦效能訴求構成檢查電源架構變化的產業觸發
evidence_boundary: 未有公司層級供應關係或財務貢獻證據
-->

<!-- impact
group_id: memory
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: 2026-08-03
rationale: SK hynix 與 NVIDIA 正式揭露 HBM4 及下一代 AI memory 合作，需檢查台灣記憶體小作文是否誤用同業事件
evidence_boundary: SK hynix HBM 合作不是台灣 DRAM 個股直接受惠證據
-->

## 下一個可證明／否定的節點

- 技嘉下一份公司 IR 是否把 Rubin 從生態系／開發名單推進到可量化的驗證、量產出貨、
  客戶驗收或收入認列；正式筆記仍保留 5/15 當時的公司揭露，不以 NVIDIA 公告覆寫。
- 廣達、緯創、緯穎下一次法說或財務結果是否明確區分驗證、量產、出貨、收入認列，
  並留下毛利、存貨、現金流或淨利的公司級足跡。
- 散熱、PCB、電源供應商是否以一手文件揭露 Rubin/Spectrum-6 相關產品與量產時程。
- 若只看到產業轉述或股價反應，維持 `watch`；不得升格為正式筆記或 H# 終態證據。
