# {{STOCK_ID}} {{NAME}} — 質化研究筆記

<!-- meta
stock_id: {{STOCK_ID}}
template_version: {{TEMPLATE_VERSION}}
research_profile: focused_v1
verification_status: ai_draft
drafted_by: ai
last_updated:
content_as_of:
latest_financial_period:
next_review:
core_source_ids:
evidence_pack_manifest:
evidence_pack_sha256:
reviewed_by:
reviewed_at:
review_method:
review_scope:
reviewed_content_sha256:
conflict_summary:
-->

> 族群：{{GROUP}}（{{BIZ}}）。本筆記為 Universe 質化參考，非投資建議。
>
> 查核狀態以 meta 與 `qual_notes.py --lint` 為準；`last_updated` 只代表編修日，
> 不代表內容已被獨立核驗。

<!--
重要主張契約：
1. 每個實質段落、bullet 與表格資料列都在同一 block 標 [S#]，不可用章末引用包辦。
2. 一手來源只能證明「該來源如此揭露」；展望、排名、客戶推測須保留其不確定性。
3. partially_verified 只核驗 review_scope 明列的範圍；independently_verified 必須把
   review_scope 設為 all_material_claims，且所有 claim block 都有一手來源。
4. reviewer 完成複核後執行 `qual_notes.py --hash {{STOCK_ID}}`，將結果填入
   reviewed_content_sha256；正文再被修改就會自動失去簽核資格。
5. focused_v1 只使用 3–5 份核心一手文件，全文以約 25–35 個真正重要 claim block
   為目標；manifest 必須涵蓋年報、年度財報、最新季報與最新法說 role，股東會僅在
   必要時加入。這是聚焦警示，不鼓勵為湊數拆句或保留不重要主張。
6. PDF 只渲染正文實際引用頁及前後各一頁，不渲染全本。drafter 建立完整 SHA、payload
   mode 唯讀且可偵測竄改的 evidence pack；reviewer 使用同一 pack 離線執行 verify、
   重算數字並獨立判讀，不重下載。這是流程封存，不是不可繞過的 ACL 安全邊界。
   focused_v1 簽核時 review_method 固定填 offline_evidence_pack_independent_recalculation。
7. 每份缺失核心文件只找 10 分鐘；manifest 固定記 `source_search_timeout_minutes: 10`
   與 `unverified_claims_removed: true`，正文必須刪除未驗證主張。來源衝突才使用
   conflicted，找不到來源不等於來源衝突。
8. 每完成一篇獨立簽核，該 note 與其 evidence manifest 必須單獨 commit，不累積多篇。
9. 既有未標 research_profile 的 v2 筆記仍依原契約有效；focused_v1 只套用新建或
   重新展開完整研究的筆記。
-->

## 30 秒摘要

（待填：用 3–5 點回答公司做什麼、靠什麼賺錢、目前最大動能、主要弱點及最重要觀察指標；每點附 `[S#]`。）

## 產業位置與競爭格局

（待填：價值鏈位置、產業結構、可比公司、供需與議價權；區分公司揭露與研究判斷。）

## 業務與獲利模式

（待填：自有產品、代理、加工或服務費模式；收入、毛利與現金流如何形成，並說明 Universe 歸屬。）

## 客戶、產品與地區結構

（待填：近一期產品／應用／客戶／地區占比及集中度。表格每一資料列都要有「依據」欄與 `[S#]`。）

## 財務品質與資本配置

（待填：最新財報期間、營收與毛利變化的原因、現金流、存貨／應收、負債、股利與擴產；量化值本身仍以資料庫為準。）

## 優勢、弱點與護城河

（待填：把可驗證的競爭優勢與結構性弱點並列；「領先」「唯一」「市占第一」等高風險主張必須有一手依據。）

## 成長動能、催化劑與驗證 KPI

（待填：新產品、客戶、產能、價格或技術升級；每項動能同時列出可證偽的 KPI、時間窗與失效條件。）

## 風險與預警指標

（待填：需求、價格、客戶集中、技術、執行、財務、匯率、地緣政治與治理風險；列領先觀察指標。）

## 管理層與治理

（待填：資本配置紀錄、關係人交易、股權／董監結構、承諾與實際成果；沒有一手資料就明寫未知。）

## 未決衝突（僅有來源衝突時保留）

（待填：並列至少兩個互相矛盾的來源 `[S#][S#]`、衝突口徑與待查證事項；meta 設為 `conflicted`。）

## 證據索引與資料來源（擷取日期：{{TODAY}}）

<!-- 固定格式：- [S1] **一手**｜文件名稱與發布／資料日期｜頁碼、表格或章節｜直接 HTTPS URL -->
（待填：刪除此行後，只列 core_source_ids 指定的 3–5 份正文實際引用核心文件；不要保留範例網址。）

## 下次更新與事件觸發

- **固定複核**：（待填：日期或固定週期，例如下一季財報發布後。）
- **事件觸發**：（待填：法說、新產能、重大訊息、核心 KPI 偏離或來源衝突。）
