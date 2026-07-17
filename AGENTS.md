# strong-weak-scanner(台股汰弱留強掃描)

台股半導體與 AI 供應鏈族群(被動/功率/封測/記憶體/矽智財/設備/材料/散熱/PCB/電源/
伺服器組裝機構,約 121 檔)的兩層訊號系統:**個股層**族群內排名
選強汰弱、**族群層**籌碼聚合找被佈局的族群。每日 GitHub Actions 台灣 20:17
先抓價格/法人 checkpoint，23:40 補完 → 評分 → 儀表板；SQLite db 與報告都 commit 在 repo 裡。
儀表板:https://dennisliuck.github.io/strong-weak-scanner/

## 每個 session 開始前

- **先 `git pull`**——`data/findmind.db` 由 Actions 每日更新,不 pull 就是在看舊資料。
- Python 一律 `uv run --no-project --python 3.12 python ...`(系統 python 是 MS Store stub,不能用)。
- 中文 stdout 在 console 會亂碼(cp950),寫檔 UTF-8 正常;必要時輸出到檔案再讀。
- **判斷「現在台灣時間」直接下 `date`(不要加 `TZ=Asia/Taipei` 前綴)**——這台機器系統
  本地時區就是 Asia/Taipei,但 git-bash 沒裝 tzdata,`TZ=Asia/Taipei date` 會轉換失敗、
  靜默印出系統原始值並貼錯時區標籤(曾把 23:32 台灣時間誤判成 15:31,少算 8 小時,
  差點在收盤資料還沒發布時就手動 trigger 排程)。要 UTC 時間才用 `date -u`。

## 依任務選 runbook

| 情境 | 文件 / 工具 |
|---|---|
| 盤後確認執行狀況、討論今日資料 | `DAILY_CHECK.md`;核心工具 `scripts/daily_brief.py`(唯讀) |
| 週六策略檢視(報告已自動產生) | `WEEKLY_REVIEW.md`(行動門檻表,照走) |
| 季度 universe 調整、新增族群 | README「Universe 治理」+ `scripts/screen.py` |
| 個股質化筆記建立/維護、biz 對齊複核 | `QUALITATIVE_RESEARCH_RUNBOOK.md` + `QUALITATIVE_SOURCE_ACQUISITION.md` + README「質化研究筆記」+ `scripts/qual_notes.py` + `scripts/qual_evidence.py` |

## 鐵律

- **勿憑 in-sample 或單日/單週數據調策略**——一律走 `WEEKLY_REVIEW.md` 的 OOS 行動門檻;
  每次最多動 1~2 個旋鈕。
- 改了權重或 tier 條件,**必須同步把 `scripts/validate.py` 的 `IS_CUTOFF` 改成當天**
  (否則舊 OOS 會被新規則重複當證據)。
- 零第三方依賴(純 stdlib);策略旋鈕集中在 `score.py` CONFIG(個股層)與
  `fetch_daily.py` 頂部(族群/大盤層),不散落他處。
- 版本沿革與實證依據記 `CHANGELOG.md`;README 與網站只描述現行系統,不放版本敘事。
- commit 訊息用中文;策略變更需附依據數字(哪份報告、哪個指標)。
- **新建或重新展開完整研究的質化筆記一律使用 `research_profile: focused_v1`**;
  既有未標 profile 的 v2 筆記沿用原品質契約,不因 focused 規範回溯失效。
- focused 研究只選 3~5 份核心一手文件:年報、年度財報、最新季報、最新法說四種 role
  必備(年報含查核財報時可共用一份 PDF),股東會僅必要時選填;正文約 25~35 個真正重要
  claim block;
  找不到穩定來源時每份文件最多查找 10 分鐘,逾時就在 evidence manifest 記錄
  `source_search_timeout_minutes: 10` 與 `unverified_claims_removed: true`,並從正文刪除
  該主張,不可繼續追逐或以二手資料補洞。
- PDF 只渲染實際引用頁及前後各一頁。drafter 建立含完整 SHA、payload mode 唯讀且
  可離線偵測竄改的 evidence pack 後(不是不可繞過的 ACL 安全邊界),
  reviewer 必須使用同一 pack 離線重算檔案 SHA、數字、期間、單位與推論邊界,不得重下載。
  focused 簽核的 `review_method` 固定填 `offline_evidence_pack_independent_recalculation`。
- 每完成一篇 `independently_verified` 就只把該 note 與對應 evidence manifest 做成一個
  獨立 commit;不可累積三篇或多篇後一起提交。PDF/PNG pack 留在 `tmp/`,不得進版控。

## 架構速覽

```
fetch_tdcc.py    TDCC 股權分散週快照(opendata 直抓,免 token)→ tdcc_holding
                 ⚠ 僅供最新一週、缺週=永久洞;失敗 exit 0 不擋管線(Actions 綠≠成功)
fetch_daily.py   TWSE/TPEx 全市場批次五張原始表；FinMind 只留事件/指數/參考個股
                 → 還原價(除權息/分割自算)→ 五元素+觀察欄 → 族群層聚合
                 ⚠ 每張待補表每交易日各呼叫 TWSE/TPEx 一次；五表完整新日共 10 次免 token
                 ⚠ 20:17 只落地價格/法人 checkpoint；23:40 final pass 補三表、刷新 holding
                 ⚠ 另直抓 TWSE/TPEx 處置/注意股票旗標；日誌批次 0 次=缺口已完整、非失敗
                 日誌/API 次數/斷點續跑判讀見 README「Daily Fetch 日誌判讀與續跑語意」
fetch_financials.py 財報四表(FinMind,月營收+損益表+資產負債表+現金流量表)
                 → month_revenue/financials/balance_sheet/cash_flow;獨立月/季排程,不掛每日管線
score.py         族群內分位數排名(−2..+2)→ 綜合分(3日平滑)→ tier(連2日確認)
build_dashboard.py → index.html + archive/日期.html(as-seen 快照,勿從 db 回填)
                 archive 同資料日首次建立後不覆寫;本地重跑只更新 index.html
validate.py      → reports/ 週報(§⑥=觀察因子 IC)
config/          universe.csv(成員+主業)、groups.csv(族群定義)、candidates.csv(候選)
qual_notes.py    notes/qualitative/*.md(年報MD&A/法說會重點,人工撰寫)狀態追蹤+骨架建立
                 ⚠ 唯讀盤點工具,不抓資料;已有筆記的股票不會被要求重寫,除非模板版本升級
qual_evidence.py focused_v1 evidence pack 建立/渲染規劃/離線驗證;可提交 manifest
                 → notes/qualitative/evidence/,PDF/PNG → tmp/qualitative_evidence/(不進版控)
```

資料表:原始 price/inst/margin/holding/sbl(借券餘額,單位=股)+ tdcc_holding(週頻)+
risk_flags(TWSE/TPEx 處置/注意公告)(依主鍵冪等 upsert；holding 當日初版只在 23:40
final pass 刷新一次)+ 衍生
price_adj/daily_metrics/daily_scores/group_metrics/market_daily(每次重建)。
舊制凍結:daily_scores_v1。**觀察層(TDCC 大戶/借券)未計分**,歸宿等 OOS 裁決
(WEEKLY_REVIEW §4-8,約 2026-08-29 後)。**risk_flags(處置/注意)屬另一類**——
交易所官方認證的異常價量列管,設計上就是永久顯示用警示(儀表板紅框 badge),
不進 OOS 排程、不會變成計分項。**month_revenue/financials/balance_sheet/cash_flow
(2026-07-09 起,`fetch_financials.py` 獨立填入)也是另一類**——FinMind 官方財報,
月/季頻、不進 daily_metrics/daily_scores,供 Universe 治理(R1 業務歸屬)等質化查證用;
financials/balance_sheet/cash_flow 是 FinMind 原生 type/value 窄表(EAV),非寬表。
**`notes/qualitative/*.md`(2026-07-09 起)也是另一類**——年報 MD&A、法說會重點,人工
撰寫(非 FinMind、零自動抓取),供理解個股業務/商業模式用;`build_dashboard.py` 讀 meta
區塊把「最後更新/建議複核」狀態顯示成儀表板個股列的筆記 badge,點擊連到 GitHub 全文。
