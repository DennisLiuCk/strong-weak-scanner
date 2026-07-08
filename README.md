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
每交易日 21:40(台北,GitHub Actions:.github/workflows/daily-fetch.yml;
排程時點依 FinMind 各 dataset 更新時間而定——最晚的持股/融資券 21:00 更新,
對照表見 workflow 註解)
  fetch_tdcc.py    TDCC 股權分散週快照(opendata 直抓,免 token;僅供最新一週)
                   → tdcc_holding(append-only;失敗自動略過不擋管線)
  fetch_daily.py   FinMind 5 資料集 × 全 universe + 除權息/分割事件 + 報酬指數
                   → SQLite 原始表(append-only)
                   → price_adj 還原價(本地重算)
                   → daily_metrics 五元素衍生指標
                   → group_metrics / market_daily 族群層聚合 + 大盤 regime
  score.py         族群內排名評分 → composite → tier(daily_scores)
  build_dashboard.py → index.html(GitHub Pages)
                     → archive/<資料日>.html + manifest.json(as-seen 歷史快照:
                       凍結當日產出原樣,供日期選單回看;不事後從 db 重繪,
                       因衍生表每日全量重建,重繪會被現行規則污染)
每週六 09:00(weekly-validate.yml)
  validate.py      → reports/validate_*.md(元素 IC、tier 超額報酬、IS/OOS 對照)
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

**衍生層(每次全量重建、冪等——調規則後重跑即一致)**

| 表 | 內容 |
|---|---|
| price_adj | 還原收盤價:除權息/分割以倒推法本地重算(事件日前歷史價 × 係數連乘,最新區段=原始價);減資 dataset 需付費未涵蓋,以「無事件 >15% 跳空」偵測示警兜底 |
| daily_metrics | 五元素原始指標:ret1/ret20、dist_hi20/60、rs20、down_rs20、turnover_pct、vol_ratio60、foreign_pct、fpct_chg5/20、dipbuy20、trust5(_pct)、margin_bal/chg、margin_util_pct、券資比等;**觀察欄(未計分)**:tdcc_big400/1000_pct·chg、tdcc_people_chg、sbl_pct/chg(TDCC pct 分母為集保庫存,非發行股本) |
| daily_scores | 各元素分數、composite / composite_s(3 日平滑)、tier_raw / tier、warn、pending(蓄勢候補差哪些條件) |
| group_metrics | 族群聚合:breadth_f、med_dist60、rel20、med_dip、breadth_t、state/note |
| market_daily | dd20(報酬指數距 20 日高)、regime 旗標 |
| universe / groups | 每次由 `config/universe.csv`、`config/groups.csv` 重建 |

凍結表 `daily_scores_v1`:舊絕對門檻制(v1)最後結果,供 validate 新舊對照。

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
  (族群中位與排名都會變),審計軌跡以 CHANGELOG 為準。
- **新增族群**(2026-07-05 記憶體為範例,細節見 CHANGELOG):全管線配置驅動,
  `groups.csv` + `universe.csv` 各加行即生效、零改碼;一檔只屬一個族群(跨域者
  依籌碼行為歸屬,如記憶體封測歸封測);族群設計下限約 6 檔有效樣本(低於
  `GRP_MIN_N` 族群層聚合不給值,子鏈拆太細會算不出來);候選一樣走 R1~R4 +
  `screen.py`。回補至現有基期後全歷史即有分數,但**新族群的 OOS 從加入日起算**
  ——「事後挑族群」的回補歷史含 look-ahead,不得當策略證據;TDCC 週快照自
  加入日起累積,之前為永久洞。

## 用法

```bash
# 每日三步(Actions 自動跑;本機手動也可)
uv run --no-project python scripts/fetch_daily.py     # 增量抓取(預設補最近 15 天)
uv run --no-project python scripts/score.py           # 重算全歷史評分
uv run --no-project python scripts/build_dashboard.py # 重生 index.html

# TDCC 週快照(Actions 每日自動抓;週六 opendata 更新後手動跑可提早入庫)
uv run --no-project python scripts/fetch_tdcc.py

# 回補歷史 / 定向補缺(只抓指定股票,省 API 額度)/ 盤後唯讀簡報 / 週度驗證
uv run --no-project python scripts/fetch_daily.py --start 2026-03-01
uv run --no-project python scripts/fetch_daily.py --stocks 6510,6515 --start 2026-03-01
uv run --no-project python scripts/daily_brief.py
uv run --no-project python scripts/validate.py
```

Token 讀取順序:環境變數 `FINMIND_TOKEN`(+選配 `FINMIND_TOKEN2`)→ 本機
`.mcp.json` 同名欄位(已被 `.gitignore` 排除);雲端由 Actions secret 注入。
多組 token 組成時額輪替池——免費層 600 req/hr,遇 402 自動換下一組
(`fetch_daily.api_get`,screen.py 共用);同日多輪「screen+全量回補」單組
token 必爆額度,參考量:回補一輪 ≈ 5 datasets × 檔數 + 事件段。Runbook:盤後檢視
[DAILY_CHECK.md](DAILY_CHECK.md)、週六策略檢視 [WEEKLY_REVIEW.md](WEEKLY_REVIEW.md)。

## 侷限與註記

- 券商分點(真主力)需 FinMind Sponsor 等級,未開通——看得到法人別、看不到分點。
- TDCC 股權分散 opendata 僅提供最新一週、歷史不可回補——自 2026-07-03 起累積,
  缺週即永久洞(每日管線重抓同週快照 = 5 次保險);FinMind 的歷史版 dataset 需付費。
- 小型股外資持股單日數字含保管行重分類雜訊:看 20 日趨勢並與買賣超交叉驗證。
- 本專案為量化籌碼研究,**非投資建議**。
