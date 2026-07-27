# 市場議題標題

<!-- research_topic
topic_id: MI-YYYY-MM-DD-SHORT-SLUG
schema_version: 1
status: inbox
priority: p2
captured_at: YYYY-MM-DD
source_published_at: YYYY-MM-DD
last_reviewed_at: YYYY-MM-DD
review_due: YYYY-MM-DD
source_type: official_company
publisher_domain: example.com
canonical_url: https://example.com/source
source_chain_id: publisher-event-yyyymmdd
stock_ids:
group_ids:
trigger_type: industry_event
evidence_role: candidate_source
route: undecided
-->

<!-- transition
date: YYYY-MM-DD
from: initial
to: inbox
reason: initial_capture
evidence: source_chain:publisher-event-yyyymmdd
-->

## 為何值得進佇列

用一段話區分「來源明講的事實」與「研究端待驗證的映射」。

## 來源與證據邊界

- [一手來源](https://example.com/source)
- 尚未證實的公司層級主張必須明列，不可把產業事件自動改寫成公司營收、訂單或市占。

## 影響路由

<!-- impact
group_id: serverodm
stock_ids:
direction: uncertain
hypothesis_refs:
note_action: watch
action_due: YYYY-MM-DD
rationale: 為何此族群或個股需要複核
evidence_boundary: 目前只構成搜尋觸發，不構成正式筆記事實
-->

## 下一個可證明／否定的節點

- 公司正式公告、季報或法說是否明確對應這個事件。
- 若沒有新增公司層級證據，保留在候選議題，不更新正式筆記。
