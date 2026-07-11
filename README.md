# strong-weak-scanner · 台股汰弱留強掃描

台股半導體與 AI 供應鏈九族群(**被動元件 / 功率元件 / 封測 / 記憶體 / 矽智財 /
半導體設備 / 半導體材料 / 散熱 / PCB·CCL**,名單見 `config/universe.csv`,現 98 檔)
的量化籌碼掃描系統:每個交易日自動抓取價量與籌碼資料,在**族群內**互相排名比強弱,
產出評級與儀表板,並每週以樣本外資料驗證規則是否仍然有效。

- **儀表板**:<https://dennisliuck.github.io/strong-weak-scanner/>(GitHub Pages,每日更新;
  頁首「資料至」日期選單可回看任一日的歷史報告快照)
- **零第三方依賴**:純 Python 標準庫 + SQLite;資料庫與報告 commit 在 repo,全程可稽核
- 本檔說明**現行系統**的設計與實作;版本沿革與各決策的實證依據見 [CHANGELOG.md](CHANGELOG.md)

## 設計理念:兩層訊號,各司其職

系統的核心實證(推導過程與數字見 CHANGELOG v2.1):

> **族群內分強弱,靠價格相對因子;籌碼因子的價值在「選族群」。**
> 外資/投信買賣超在「族群內」幾乎沒有選股力——它們回答的是「資金在佈局哪個族群」,
> 不是「族群裡哪一檔最強」。

因此架構拆成兩層,加一個大盤旗標:

| 層 | 回答的問題 | 主要訊號 | 產出 |
|---|---|---|---|
| 個股層 | 族群內誰強誰弱 | 相對強弱、修正日抗跌(價格相對因子) | 五元素分數 → 綜合分 → tier |
| 族群層 | 哪個族群正被佈局 | 佈局廣度、修正日中位逆勢買超(籌碼聚合) | 族群狀態(儀表板「族群雷達」) |
| 大盤層 | 多頭還是修正 | 報酬指數距 20 日高 | regime 旗標(修正期價值/抗跌因子更有效) |

**為什麼是排名制、不是絕對門檻**:絕對門檻有個股結構偏誤——外資持股本來就高的
大型股永遠拿不到「外資增持 +2」,小型股股本小、稍有買超就滿分。族群內分位數排名
讓每檔跟「處境相同的同業」比,天生控制了產業與規模效應。

## 資料管線

```
每交易日盤後(預設由 GitHub Actions 21:40 台北執行,也可隨時從本地 run_daily.py 觸發；
排程時點依 FinMind 各 dataset 更新時間而定——最晚的持股/融資券 21:00 更新,
對照表見 workflow 註解。提早執行若資料未齊,只保存已抓缺口、不發布正式快照)
  fetch_tdcc.py    TDCC 股權分散週快照(opendata 直抓,免 token;僅供最新一週)
                   → tdcc_holding(append-only;失敗自動略過不擋管線)
  fetch_daily.py   先探測新交易日,再只補 FinMind 5 資料集的股票×日期缺口
                   + 依 coverage 補除權息/分割事件 + 報酬指數
                   → SQLite 原始表(append-only)
                   → price_adj 還原價(本地重算)
                   → daily_metrics 五元素衍生指標
                   → group_metrics / market_daily 族群層聚合 + 大盤 regime
  score.py         族群內排名評分 → composite → tier(daily_scores)
  snapshot_signals.py → 凍結本次實際發布的 OOS as-seen 原始指標+評分
                        (append-only;同日重跑保留各版,驗證採最早正式發布版)
  build_dashboard.py → index.html(GitHub Pages)
                     → archive/<資料日>.html + manifest.json(as-seen 歷史快照:
                       首次建立後不覆寫,供日期選單回看;不事後從 db 重繪,
                       因衍生表每日全量重建,重繪會被現行規則污染)
每週六 09:00(weekly-validate.yml)
  validate.py      → reports/validate_*.md(元素 IC、tier 超額報酬、IS/OOS 對照)
每月 12 日 / 每季申報截止後(fetch-financials.yml)
  fetch_financials.py 財報四表(FinMind:月營收+損益表+資產負債表+現金流量表)
                   → month_revenue/financials/balance_sheet/cash_flow(append-only)
                   ⚠ 基本面資料,不進 daily_metrics/daily_scores;供 Universe 治理
                     (R1 業務歸屬)等質化查證用——同 tdcc_holding 屬另一類資料
```

## 資料結構(`data/findmind.db`)

**原始層(append-only、只增不覆寫——歷史判定不可事後改寫)**

| 表 | 內容 | 來源 dataset |
|---|---|---|
| price | 日 OHLCV | TaiwanStockPrice |
| inst | 外資/投信/自營淨買賣(股) | TaiwanStockInstitutionalInvestorsBuySell |
| margin | 融資/融券餘額 | TaiwanStockMarginPurchaseShortSale |
| holding | 外資持股比率、發行股數 | TaiwanStockShareholding |
| sbl | 借券賣出餘額(股) | TaiwanDailyShortSaleBalances |
| tdcc_holding | 集保股權分散(週頻,17 級距,universe+候選) | TDCC opendata(**非 FinMind**;僅供最新一週) |
| dividend_result / split_event | 除權息、分割事件 | TaiwanStockDividendResult / TaiwanStockSplitPrice |
| market | 加權報酬指數(含息) | TaiwanStockTotalReturnIndex |
| month_revenue | 個股月營收 | TaiwanStockMonthRevenue |
| financials | 損益表(含EPS,type/value 窄表) | TaiwanStockFinancialStatements |
| balance_sheet | 資產負債表(type/value 窄表) | TaiwanStockBalanceSheet |
| cash_flow | 現金流量表(type/value 窄表) | TaiwanStockCashFlowsStatement |

**衍生層(每次全量重建、冪等——調規則後重跑即一致)**

| 表 | 內容 |
|---|---|
| price_adj | 還原收盤價:除權息/分割以倒推法本地重算(事件日前歷史價 × 係數連乘,最新區段=原始價);減資 dataset 需付費未涵蓋,以「無事件 >15% 跳空」偵測示警兜底 |
| daily_metrics | 五元素原始指標:ret1/ret20、dist_hi20/60、rs20、down_rs20、turnover_pct、vol_ratio60、foreign_pct、fpct_chg5/20、dipbuy20、trust5(_pct)、margin_bal/chg、margin_util_pct、券資比等;**個股自身技術觀察(未計分)**:ma5/20/60、rsi14(Wilder)、volume、vol_ma5/20/60、vol_ratio20(當日量÷20日均量);**其他觀察欄(未計分)**:tdcc_big400/1000_pct·chg、tdcc_people_chg、sbl_pct/chg(TDCC pct 分母為集保庫存,非發行股本) |
| daily_scores | 各元素分數、composite / composite_s(3 日平滑)、tier_raw / tier、warn、pending(蓄勢候補差哪些條件) |
| chip_health | 個股籌碼現況診斷(健康/中性/待觀察),不計 composite/tier、不是選股排名；儀表板逐列把原始方向翻成健康/中性/警示,TDCC/借券另標「方向待 OOS 驗證」 |
| group_metrics | 族群聚合:breadth_f、med_dist60、rel20、med_dip、breadth_t、state/note |
| market_daily | dd20(報酬指數距 20 日高)、regime 旗標 |
| universe / groups | 每次由 `config/universe.csv`、`config/groups.csv` 重建 |

儀表板的「個股技術面」使用還原收盤價與成交量，從五個互補角度描述個股相對自身歷史：
短中長均線結構、現價偏離均線、RSI 動能及 5 日變化、價格與 20 日均量的確認關係、
現價/MA20 與 MA5/MA20 的最近一日穿越。這些都是觀察資訊，不做族群排名、不預測下一日
漲跌，也不進 `composite`、`tier` 或 `chip_health`。

凍結表 `daily_scores_v1`:舊絕對門檻制(v1)最後結果,供 validate 新舊對照。

**OOS as-seen 凍結層(append-only、不可重算覆寫)**

| 表 | 內容 |
|---|---|
| oos_snapshot_runs | 每次快照的 run id、資料日、UTC 擷取時間、觸發來源(source)、正式發布旗標(is_official)、git SHA、score/metrics/universe/groups SHA-256、資料品質計數 |
| oos_signal_snapshots | 當時分組、`daily_metrics` 全部原始欄、`daily_scores` 全部評分欄、chip health、官方風險旗標 |
| oos_group_snapshots | 當時九族群定義、聚合指標與 state |
| oos_market_snapshots | 當時大盤資料日、dd20 與 regime |

`daily_scores` 等衍生表仍可用最新規則重算全歷史,供研究「現行模型放回過去」的
restated history；正式 OOS 則只讀上述每日快照。同資料日若修復資料後重跑,新版本會
另存而非覆蓋,驗證固定採**最早正式發布的快照**——觸發來源可以是 GitHub Actions 或
本地 runner；`source` 只供追溯,不決定 OOS 資格。正式發布前會要求五張原始表、評分與
族群表都涵蓋完整 universe。這才是使用者當天第一次實際看到、可能據以決策的訊號。
舊日期只有 HTML archive、沒有完整機器快照者
不事後拼湊,一律標為 restated、不得計入 OOS。快照最早資料日鎖為 2026-07-10；遇休市
或資料源尚未產生新交易日、最新資料仍早於此日，就正常略過，不把 7/9 回算值偽裝成新 OOS。

**防前視(lookahead)設計**:周轉率/散戶水位/投信佔股本用**當日**發行股數
(forward-fill,不用最新股本回填歷史);dist/dd 視窗有最少樣本保護(新股冷啟動
不會假新高);外資持股有申報遞延,回測一律只用「當日可得」資料;TDCC 週快照
(週五結算、週六才公布)以 T−3 日曆日生效——當週快照最早次週一才進指標。

## 個股層評分(`scripts/score.py`,策略旋鈕集中在 CONFIG)

1. **排名制**:相對強弱(rs20)、抗跌(down_rs20)、外資(fpct_chg20)、投信
   (trust5_pct)、逆勢買超(dipbuy20)五項在族群內取分位數:前 20% → +2、
   20~40% → +1、中段 → 0、60~80% → −1、後 20% → −2;有效樣本 <4 檔全給 0。
2. **雜訊死區**:外資 ±0.3pp、投信 ±0.03%、逆勢 ±0.03% 內強制 0 分——
   全族群無訊號時,排名只會放大雜訊。
3. **規則式元素(不排名)**:
   - ②量:量比 = 當日周轉率 ÷ 自身 60 日中位;1.2~3.0 → +1、<0.5 → −1;
     量比 ≥5 或周轉率 ≥20% → 過熱旗標 ⚠(不改分數,進 tier 判斷)。
   - ⑤融資券:價(ret20)× 融資(margin_chg10)交互——價跌融資減=洗盤 +2
     (價漲融資減=健康換手 +1)、融資 10 日暴增 ≥20% = −2、價跌融資增=接刀 −2
     (價漲融資增=追高 −1);散戶水位 ≥9% 分數封頂 −1 並示警、≥6% 封頂 +1。
4. **加權合成**:權重 price 1.4 / resil 1.0 / trust 0.8 / foreign 0.5 /
   margin 0.4 / vol 0.3 / dip 0(僅供 tier 條件)。composite 取 3 日平均為
   composite_s,理論範圍約 ±8.5。
5. **tier**(判定優先序由上而下;raw tier 需連 2 日相同才正式轉層):

| tier | 條件 |
|---|---|
| 真弱·陷阱 | 外資 ≤−1 且 融資 ≤−1 且 rs20 <0(外資出、散戶接) |
| 強但過熱 | 價 ≥+1 且 過熱旗標 |
| 蓄勢·外資佈局 | (外資 ≥+2 或 逆勢 ≥+2)且 距 60 日高 ≤−3%(價未動)且 抗跌 ≥0(質量濾網)且 composite_s ≥1.5 |
| 真強 | 族群 composite_s 前 2 名 且 ≥2.5 且 價 ≥+1 且 任一法人(外資/投信/逆勢)≥+1 |
| 真弱 | composite_s ≤−3.5,或族群倒數 2 名且 <0 |
| 潛在/中性 | 以上皆非;籌碼已符蓄勢但差其他條件者標「◇蓄勢候補」(pending 欄標明差哪些) |

## 族群層與大盤(`scripts/fetch_daily.py`,旋鈕在檔頭)

- `group_metrics`:佈局廣度(fpct_chg20>0 檔數比例)、中位距 60 日高、rel20
  (族群中位 20 日報酬 − 全體中位)、med_dip(修正日中位逆勢買超——選族群
  **候選**主訊號,OOS 驗證中)、投信買超廣度;聚合需 ≥6 檔有效樣本才給值。
- 族群狀態(`_gstate`):修正日有人接 + 價未回高 → 蓄勢·被佈局;動能領先 +
  價近波段高 → 發動·領漲;修正日遭調節 + 廣度低 → 籌碼退潮;其餘中性觀察。
- 大盤 regime:報酬指數距 20 日高 ≤−3% → 修正。**刻意用含息指數**——除息季
  價格指數會機械性下跌,含息指數只反映經濟性修正(與個股層用還原價同一邏輯)。

## 驗證與策略治理

- **週報**(每週六自動,`validate.py` → `reports/`):元素 IC(族群內/混池 ×
  IS/OOS × 修正/多頭 regime)、tier 前瞻超額與轉移事件、新舊制對照、蓄勢濾網
  cohort、族群層命中率、市值公平性監測(同尺檢核)、觀察因子 IC(TDCC 大戶/
  借券,未計分,等 OOS 裁決歸宿)。
- **OOS 口徑**:`validate.py` 只把 `snapshot_signals.py` 留下的正式 as-seen 快照列入
  OOS,並同時顯示「快照累積日數」與「前瞻報酬已成熟日數」;cutoff 後但由最新規則
  回算的日期只供背景,不進任何 OOS 行動門檻。
- **鐵律**:不憑 in-sample 或單日/單週數據調策略;一律走
  [WEEKLY_REVIEW.md](WEEKLY_REVIEW.md) 的 OOS 行動門檻,每次最多動 1~2 個旋鈕;
  改權重或 tier 條件,必須同步把 `validate.py` 的 `IS_CUTOFF` 改成當天。
- **Universe 治理**(季度,工具 `scripts/screen.py` + `config/candidates.csv`):
  R1 業務歸屬(主營收 >50% 屬族群業務,人工覆核)——**先判斷商業模式**:營收主要
  來自賣自己的產品、還是收加工/服務費?後者(封測代工/測試代工/通路代理/工程
  服務等)優先看 packtest/semiequip 這類「服務型」族群,不依終端應用分到
  power/memory 等「產品型」族群(2026-07-09 6525 捷敏-KY 曾誤判為例,見
  CHANGELOG);`screen.py` 另跑一次零 API 的業務歸屬關鍵字複檢(`check_biz_grp`),
  抓 biz 欄與族群歸類疑似不符的既有成員,供人工覆核、不自動改分類 /
  R2 市值遲滯(≥50 億納入、現有成員 <30 億才剔除,防反覆進出)/ R3 近 20 日
  中位成交值 ≥3,000 萬 / R4 上市 ≥60 交易日。變更後全歷史按新名單重算
  (族群中位與排名都會變),審計軌跡以 CHANGELOG 為準。R1 商業模式判斷的質化佐證
  (年報 MD&A、法說會重點)以 AI 協作整理在 `notes/qualitative/*.md`,並由獨立
  reviewer 依一手證據簽核；狀態與品質契約由 `scripts/qual_notes.py` 追蹤,見下方
  「質化研究筆記」。
- **新增族群**(2026-07-05 記憶體為範例,細節見 CHANGELOG):全管線配置驅動,
  `groups.csv` + `universe.csv` 各加行即生效、零改碼;一檔只屬一個族群(跨域者
  依籌碼行為歸屬,如記憶體封測歸封測);族群設計下限約 6 檔有效樣本(低於
  `GRP_MIN_N` 族群層聚合不給值,子鏈拆太細會算不出來);候選一樣走 R1~R4 +
  `screen.py`。回補至現有基期後全歷史即有分數,但**新族群的 OOS 從加入日後第一份
  正式 as-seen 快照起算**——「事後挑族群」的回補歷史含 look-ahead,不得當策略證據;TDCC 週快照自
  加入日起累積,之前為永久洞。

## 用法

```bash
# 本地每日正式管線(與 Actions 同序；可重跑、預設發布正式 OOS,但不 commit/push)
uv run --no-project --python 3.12 python scripts/run_daily.py

# 拆開執行；直接呼叫 snapshot 時本地預設只是 preview,正式發布需 --publish
uv run --no-project python scripts/fetch_daily.py     # 智慧補缺(預設最近 15 天)
uv run --no-project python scripts/score.py           # 重算全歷史評分
uv run --no-project python scripts/snapshot_signals.py --source local --publish
uv run --no-project python scripts/build_dashboard.py # 重生 index.html

# TDCC 週快照(Actions 每日自動抓;週六 opendata 更新後手動跑可提早入庫)
uv run --no-project python scripts/fetch_tdcc.py

# 財報四表(Actions 月/季自動跑;獨立於每日管線,見 fetch-financials.yml)
uv run --no-project python scripts/fetch_financials.py                     # 全部四個 dataset
uv run --no-project python scripts/fetch_financials.py --datasets TaiwanStockMonthRevenue

# 回補歷史 / 定向補缺(只抓指定股票,省 API 額度)/ 盤後唯讀簡報 / 週度驗證
uv run --no-project python scripts/fetch_daily.py --start 2026-03-01
uv run --no-project python scripts/fetch_daily.py --stocks 6510,6515 --start 2026-03-01
uv run --no-project python scripts/fetch_daily.py --force --start 2026-07-01 # 明確要求來源修正重抓
uv run --no-project python scripts/daily_brief.py
uv run --no-project python scripts/validate.py
```

Token 讀取順序:環境變數 `FINMIND_TOKEN`(+選配 `FINMIND_TOKEN2`)→ 本機
`.mcp.json` 同名欄位(已被 `.gitignore` 排除);雲端由 Actions secret 注入。
多組 token 組成時額輪替池——免費層 600 req/hr,遇 402 自動換下一組
(`fetch_daily.api_get`,screen.py 共用);同日多輪「screen+全量回補」單組
token 必爆額度。正常 daily 會跳過完整 pair；休市日通常只需 1 次價格探針，資料源延遲時
稍後重跑只補仍缺的 dataset。Runbook:盤後檢視
[DAILY_CHECK.md](DAILY_CHECK.md)、週六策略檢視 [WEEKLY_REVIEW.md](WEEKLY_REVIEW.md)。

## 質化研究筆記(`notes/qualitative/`)

年報 MD&A、財報、法說會與重大訊息這類質化揭露由 AI 協作整理成
`notes/qualitative/<股號>_<名稱>.md`,供 Universe 治理與個股研究參考。搜尋引擎、新聞、
法說摘要只能用來發現線索；主張應回到公司 IR、年報／財報原檔、MOPS 直接公告或
TWSE／TPEx 文件。FinMind 財報窄表用來交叉檢查量化口徑,不取代原始文件。

新 session 逐篇執行時先依 [QUALITATIVE_RESEARCH_RUNBOOK.md](QUALITATIVE_RESEARCH_RUNBOOK.md)
的 checklist 完成來源取得、claim-page 對照、drafter／reviewer 交接、退回重建與單篇提交；
本節保留完整品質契約與工具參數說明。

### `focused_v1`（只套用新研究）

新建筆記或重新展開一輪完整研究時,在既有 template v2 上加入以下 meta；這是附加的
研究流程 profile,**不是 template v3**。既有未標 `research_profile` 的 v2 筆記繼續依原
品質契約有效,不批次改寫、不因 focused 規範回溯降級；待下一次實質重做時才加入。

```yaml
research_profile: focused_v1
core_source_ids: S1,S2,S3
evidence_pack_manifest: notes/qualitative/evidence/<股號>/<content_as_of>_<sha前16>.json
evidence_pack_sha256: <64 位十六進位 SHA-256>
review_method: offline_evidence_pack_independent_recalculation
```

focused 研究的範圍刻意收斂：

1. 只選 **3~5 份不重複的核心一手文件**：通常是最新年報、年度查核財報、最新季度
   核閱財報、最新法說；只有治理／股利等主張確有需要時才加入官方股東會文件。
   `core_source_ids` 必須與 evidence manifest 及正文證據索引一致。
2. 全文以 **約 25~35 個真正重要 claim block** 為目標。`qual_notes.py` 既有定義是一個
   實質段落、一個 bullet 或一列表格資料各算一個；超出區間應警告並要求聚焦,但不可
   為湊數拆句,也不可因此刪掉理解公司不可或缺的少數主張。
3. PDF 只渲染正文實際引用頁及前後各一頁（頁首／頁尾自動截斷）,不渲染整本。
4. 找不到穩定一手來源時,每份缺失文件最多查找 **10 分鐘**。逾時即停止追逐,
   從正文刪除相關未驗證主張；manifest 固定記錄 `source_search_timeout_minutes: 10`
   與 `unverified_claims_removed: true`。這不是來源衝突,不得改標 `conflicted`,也不得
   用新聞或搜尋摘要補洞。

evidence pack 使用內容定址且不可覆寫。`qual_evidence.py` 本身不下載文件；drafter 先把
3~5 份核心 PDF 放在本機,再對每份文件重複傳入
`--source/--url/--pages/--page-count/--role`。四個必備 role 是 `annual_report`、
`annual_financials`、`latest_quarterly_report`、`latest_investor_conference`；只有同一份年報
PDF 已包含查核財報時,前兩個 role 才能合併在同一個 S#,股東會文件則使用選填的
`shareholder_meeting`。`build` 與 reviewer 的 `verify` 都會用 Poppler `pdfinfo` 解析原檔並
核對實際頁數；若不在 PATH,以 `--pdfinfo <路徑>` 指定。以下 S1~S3 的路徑、URL、引用
實體頁與總頁數都必須換成實際值。

```bash
uv run --no-project --python 3.12 python scripts/qual_evidence.py build --stock-id 6525 --content-as-of 2026-07-11 --source S1=tmp/S1.pdf --url S1=https://example.com/S1.pdf --pages S1=4-6,12 --page-count S1=80 --role S1=annual_report,annual_financials --source S2=tmp/S2.pdf --url S2=https://example.com/S2.pdf --pages S2=5,18-19 --page-count S2=64 --role S2=latest_quarterly_report --source S3=tmp/S3.pdf --url S3=https://example.com/S3.pdf --pages S3=3,20 --page-count S3=40 --role S3=latest_investor_conference
uv run --no-project --python 3.12 python scripts/qual_evidence.py render-plan "$PACK_DIR"
uv run --no-project --python 3.12 python scripts/qual_evidence.py render "$PACK_DIR" --pdftoppm "$PDFTOPPM"
uv run --no-project --python 3.12 python scripts/qual_evidence.py verify "$PACK_DIR" --renders
```

`build` 的 JSON stdout 會回傳 `pack_dir`、可提交的 `manifest` 路徑與 `pack_sha256`；把後
兩者填回 meta。PDF／PNG 留在已忽略的 `tmp/qualitative_evidence/`,只有自動產生於
`notes/qualitative/evidence/` 的小型 manifest 進版控。`build` 會把 SHA payload 檔案標成
唯讀,`verify` 重算完整 64 位址、PDF 頁數與精確目錄內容；這是可偵測竄改的唯讀封存,
不是阻止檔案擁有者自行改 ACL／chmod 的安全邊界。`render` 只在 pack 外建立衍生 PNG,
不會改動 evidence payload。不同於 drafter 的
reviewer 使用**同一個 pack**執行 `verify --renders`,離線重算
文件與 pack SHA,並獨立重算數字、期間、單位及判斷推論邊界,不得重新下載另一份文件。
簽核時必須把 `review_method` 填成 `offline_evidence_pack_independent_recalculation`；這個
固定值連同 pack SHA 會被正文 hash 鎖住,明確 attested reviewer 採用同 pack 離線重算流程。

每完成一篇 `independently_verified`,先執行 `qual_notes.py --hash <股號>`、把輸出填入
`reviewed_content_sha256`,再執行 `--lint <股號>`；通過後只 stage 該 note 與其 manifest
並立即做一個中文 commit,不可等三篇或多篇完成後才一起提交。這個單篇 commit 邊界不需
寫入 meta,避免 commit SHA 與內容 hash 形成循環依賴。

品質狀態與資料時效是兩條獨立軸：

- `ai_draft`：預設；即使剛更新或已有引用,也不代表經 reviewer 查核。
- `partially_verified`：只有 `review_scope` 明列的更正／章節完成獨立核驗,其餘仍是草稿。
- `independently_verified`：template v2 的每個實質段落、bullet 與表格資料列皆有一手
  `[S#]`，且由不同於撰稿者的 reviewer 完成全文簽核。
- `conflicted`：兩個可信來源口徑不一致,保留雙方證據與未決問題,不可自行挑有利版本。

正文的重要主張在同一 claim block 後標 `[S1]`;證據索引固定使用：

```markdown
- [S1] **一手**｜文件名稱與發布／資料日期｜頁碼、表格或章節｜https://直接文件網址
```

`last_updated` 只是內容編修日。部分／完整核驗另須填 `drafted_by`、`reviewed_by`、
`reviewed_at`、`review_scope` 與 `reviewed_content_sha256`;撰稿者與 reviewer 不得相同。
雜湊鎖住 reviewer 實際看過的版本,簽核後再改正文會由 lint 自動降回 AI 草稿。
這是可稽核的流程 attestation,不是密碼學身分簽章：字串本身仍可被編輯。正式多人維護時
應再用 GitHub branch protection／指定 reviewer 的 PR approval 鎖住身分與核准權限。

```bash
uv run --no-project --python 3.12 python scripts/qual_notes.py                         # 時效＋查核品質總覽
uv run --no-project --python 3.12 python scripts/qual_notes.py --lint                  # 全庫品質契約；error 時 exit 1
uv run --no-project --python 3.12 python scripts/qual_notes.py --lint 6525             # 只稽核一篇
uv run --no-project --python 3.12 python scripts/qual_notes.py --needs-review          # 全文尚未獨立核驗／過期／無效
uv run --no-project --python 3.12 python scripts/qual_notes.py --quality ai_draft      # 依有效品質狀態篩選
uv run --no-project --python 3.12 python scripts/qual_notes.py --missing               # universe 尚無筆記
uv run --no-project --python 3.12 python scripts/qual_notes.py --stale                 # 到達／超過 next_review
uv run --no-project --python 3.12 python scripts/qual_notes.py --invalid               # 品質契約有 error
uv run --no-project --python 3.12 python scripts/qual_notes.py --outdated              # 舊模板遷移佇列
uv run --no-project --python 3.12 python scripts/qual_notes.py --new 6525              # 建立 v2 骨架
uv run --no-project --python 3.12 python scripts/qual_notes.py --hash 6525             # reviewer 核完後產生內容雜湊
```

研究流程是：先建立／更新 AI 草稿 → focused_v1 drafter 建立 evidence pack 並逐 claim 補
`[S#]` → 未參與撰稿的 reviewer 用同一 pack 離線驗 SHA、文件、數字、期間、單位與推論
邊界 → 填簽核 meta → 產生 hash → `--lint` → 該 note 與 manifest 立即獨立 commit。
質化檔案或 parser 變更時，獨立的 `qualitative-quality` GitHub workflow 會執行 lint 與
dashboard 契約測試；它不阻斷每日市場資料抓取。品質無效的宣告狀態會在 dashboard 保守
降級（已知來源衝突則維持衝突警示），避免人工研究層故障使核心量化資料整批過期。
完整核驗只能使用 v2 與 `review_scope: all_material_claims`;舊 v1 可留作遷移佇列,已確認的
局部修正可明確標成 partial,但不會因局部修正冒充全文已驗證。純刪除錯誤敘事且沒有存續
claim 時使用 `confirmed_correction_deletion_only`。法說頻率因公司而異,`next_review` 依各公司
實際頻率設定；財報、法說、重大訊息、KPI 偏離或來源衝突也可提前觸發更新。

儀表板 badge 主色表示有效查核狀態,外圈才表示 `next_review` 已逾期；詳情會顯示 reviewer、
核驗範圍、資料截至日與 claim／一手證據覆蓋。無筆記的股票不顯示 badge。查核只代表筆記
在明列範圍內與所列來源一致,不保證管理層預測實現,也不把公司說法自動視為客觀真相。

**biz/群組對齊複核**(不定期,建議跟季度 Universe 治理一起做,或補完一批新筆記後執行):
筆記內容通常比 `universe.csv` 的 biz 欄豐富得多,值得回頭核對兩者是否還對得上——拿每檔
筆記的「業務概況」「客戶/產品結構」章節,對照現有 biz 描述與 group 歸類是否仍準確,
判斷框架同上面「Universe 治理」的 R1 商業模式準則。結果分兩類:
- **biz 文字疑慮**(描述跟不上筆記揭露的最新營收結構,不影響族群歸屬,如舊描述漏列
  已躍居主力的新產品線):可直接修正 `universe.csv` 的 biz 欄,並用
  `fetch_daily.load_universe(con)` 同步 db 的 `universe` 表(純 metadata 更新,
  不必重跑整條抓取管線,也不影響 price/score)。
- **族群歸類疑慮**(商業模式與現有族群定位有張力,例如實際收代工/服務費卻歸在
  產品型族群,但現行 9 族群未必有對應的服務型分類可放):記錄下來留給人工 Universe
  治理判斷,**不自動改分類**。
複核結果整理成 `reports/biz_audit_<日期>.md`(範例見 2026-07-09 那份,含逐檔判定表與
依據引用),比照 `screen.py` 報告的存放慣例;修正/擱置項目一併記入 CHANGELOG。

## 侷限與註記

- 券商分點(真主力)需 FinMind Sponsor 等級,未開通——看得到法人別、看不到分點。
- TDCC 股權分散 opendata 僅提供最新一週、歷史不可回補——自 2026-07-03 起累積,
  缺週即永久洞(每日管線重抓同週快照 = 5 次保險);FinMind 的歷史版 dataset 需付費。
- 小型股外資持股單日數字含保管行重分類雜訊:看 20 日趨勢並與買賣超交叉驗證。
- 本專案為量化籌碼研究,**非投資建議**。
