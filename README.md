# strong-weak-scanner · 台股汰弱留強掃描

針對台股半導體與 AI 供應鏈的相對強弱研究系統。現行 universe 由
[`config/universe.csv`](config/universe.csv) 定義，共 121 檔、11 個族群：被動元件、
功率元件、封測、記憶體、矽智財、半導體設備、半導體材料、散熱、PCB/CCL、電源供應、
伺服器組裝/機構。

- **儀表板**：<https://dennisliuck.github.io/strong-weak-scanner/>
- **設定來源**：[`config/groups.csv`](config/groups.csv)、
  [`config/universe.csv`](config/universe.csv)、[`config/candidates.csv`](config/candidates.csv)
- **版本沿革與實證依據**：[`CHANGELOG.md`](CHANGELOG.md)

核心每日管線只使用 Python 3.12 標準庫與 SQLite。原始資料、正式 OOS 快照、儀表板歷史頁
與驗證報告都保留在 repo，讓每次發布可以追溯。質化證據包的 PDF 驗證與轉圖另需 Poppler。

## 方法論

> **先用籌碼聚合判斷資金正在佈局哪個族群，再用價格相對因子在族群內選強汰弱。**

這個拆分是系統最重要的邊界：外資或投信在整個市場的流向，適合回答「哪個族群受關注」；
同一族群內誰較強，主要交給相對強弱與修正日抗跌。排名結果只代表同業相對位置，不能反推
原始值一定為正，也不代表未來股價方向。

| 層級 | 回答的問題 | 現行訊號 | 輸出 |
|---|---|---|---|
| 個股層 | 同族群裡誰強、誰弱 | 七因子分數、3 日平滑、分層確認 | composite 與 tier |
| 族群層 | 哪個供應鏈正在被佈局或領漲 | 外資廣度、修正日中位買賣、相對動能、距高 | 族群狀態，不改個股分數 |
| 大盤層 | 目前是否進入修正環境 | 含息報酬指數距 20 日高 | regime，不改個股分數 |
| 觀察與研究層 | 數字如何形成、公司在做什麼、市場在傳什麼 | 官方資料解剖、技術/基本面、TDCC、借券、研究筆記、領先假說、台積電事件 | 閱讀背景，不計分 |

### 個股層：族群內七因子

[`scripts/score.py`](scripts/score.py) 的 CONFIG 是個股策略唯一旋鈕來源。價格、抗跌、外資、
投信與修正日買賣先在同族群內排五分位，得到 −2～+2 分；有效樣本少於 4 檔時不排名。
外資、投信、修正日買賣另有雜訊死區，避免全族群都接近零時仍被硬分高低。

| 因子 | 原始量與規則 | 權重 |
|---|---|---:|
| 價格相對強弱 | `rs20`＝20 日還原報酬－同族群中位報酬；族群內排名 | 1.4 |
| 修正日抗跌 | 近 20 日族群下跌日，相對同業的平均表現；至少 3 個有效日後排名 | 1.0 |
| 投信 | 近 5 日投信淨買占股本；族群內排名，±0.03% 內歸零 | 0.8 |
| 外資 | 20 日外資持股率變化；族群內排名，±0.3pp 內歸零 | 0.5 |
| 融資券 | 價格方向 × 10 日融資變化；融資減碼加分、暴增或下跌接刀扣分，並受 6%/9% 融資水位封頂 | 0.4 |
| 量能 | 當日周轉率 ÷ 自身 60 日中位；1.2～3.0 倍為 +1、低於 0.5 倍為 −1 | 0.3 |
| 修正日買賣 | 族群下跌日的外資淨買占股本；族群內排名，±0.03% 內歸零 | 0.0 |

修正日買賣目前不進 composite，但仍參與「相對蓄勢」條件與族群層聚合。每日 composite
以近 3 個交易日平均形成 `composite_s`；既有股票的 raw tier 需連續 2 日相同才正式轉層，
降低單日跳動。

分層按下表由上到下判定。括號內是資料庫使用的策略 key；儀表板使用較保守的讀者標籤。

| 儀表板分層 | 現行條件 |
|---|---|
| 相對弱勢·槓桿風險（`真弱·陷阱`） | 外資分 ≤−1、融資分 ≤−1，且 `rs20 < 0` |
| 相對強勢·過熱（`強但過熱`） | 價格分 ≥+1，且周轉率 ≥20%、量比 ≥5 倍或融資水位 ≥9% |
| 相對蓄勢（`蓄勢·外資佈局`） | 外資或修正日買賣分 ≥+2、距 60 日高 ≤−3%、抗跌不輸同業，且 `composite_s ≥ 1.5` |
| 相對強勢（`真強`） | 族群內前 2 名、`composite_s ≥ 2.5`、價格分 ≥+1，且至少一項法人分 ≥+1 |
| 相對弱勢（`真弱`） | `composite_s ≤ −3.5`，或族群倒數 2 名且分數 <0 |
| 中性觀察（`潛在/中性`） | 以上皆非；籌碼已達蓄勢前提者另列尚缺條件 |

### 族群層與大盤

[`scripts/fetch_daily.py`](scripts/fetch_daily.py) 以至少 6 檔有效樣本聚合族群指標：

- `breadth_f`：20 日外資持股率增加的成員比例。
- `med_dip`：成員在族群下跌日的外資淨買占股本中位數；目前是候選主訊號，仍在 OOS 驗證。
- `rel20`：族群 20 日中位報酬相對全 universe 中位數。
- `med_dist60`：族群成員距 60 日高的中位數。
- `breadth_t`：近 5 日投信買超的成員比例。

族群狀態同樣按優先序判定：

| 狀態 | 條件 |
|---|---|
| 蓄勢·被佈局 | `med_dip > 0` 且 `med_dist60 ≤ −5%` |
| 發動·領漲 | `rel20 > 0` 且 `med_dist60 > −5%` |
| 籌碼退潮 | `med_dip < 0` 且 `breadth_f ≤ 40%` |
| 中性觀察 / 資料不足 | 其他情況 / 樣本不足 |

大盤使用含息報酬指數；距 20 日高 ≤−3% 時標為修正 regime。含息口徑可避免除息季的
機械性下跌被誤判為市場修正，與個股使用還原價的原則一致。

### 明確不計分的內容

- `chip_health` 是七個籌碼方向的描述性診斷，不是族群內排名；其中 TDCC 大戶、股東人數、
  借券三項仍待 OOS 累積後裁決。交易所處置/注意旗標會直接標成待觀察，但不改 composite。
- MA5/20/60、RSI14、價量關係與穿越事件只描述個股相對自身歷史。
- 官方資料「數據解剖」展示成交筆數、法人買賣兩側、融資券流量、外資限額、借券拆分與
  相對所屬市場報酬指數；個股與族群版本都不計分。
- 月營收、財報、質化筆記、領先假說與台積電專區都是研究背景，不直接餵入 tier。

## 資料、重算與發布邊界

### 資料來源

| 類別 | 來源與用途 |
|---|---|
| 每日五張原始表 | TWSE/TPEx 全市場批次：價格、法人、融資券、外資持股、借券；另抓處置/注意公告 |
| 還原與市場序列 | FinMind：除權息/分割事件、TAIEX 含息報酬指數；交易所官方 `market_index` 只供觀察，不取代 regime |
| 週/月/季資料 | TDCC 股權分散週快照；FinMind 月營收、損益表、資產負債表、現金流量表 |
| 研究資料 | 公司 IR、MOPS、TWSE/TPEx 文件與人工維護的質化筆記、領先假說、事件錨點 |

每日價格因子使用本地倒推的 `price_adj`。除權息與分割有事件資料可重算；減資參考價未涵蓋，
以「無事件大幅跳空」警告兜底。TDCC 只提供最新一週，週五快照到次週一才生效，避免前視。

### SQLite 分層

| 層 | 主要內容 | 更新語意 |
|---|---|---|
| 原始層 | `price`、`inst`、`margin`、`holding`、`sbl`、`risk_flags`、`market`、`market_index`、`tdcc_holding`、財報與 `ref_*` | 依主鍵冪等補缺；成功來源可先 checkpoint |
| 衍生層 | `price_adj`、`daily_metrics`、`observation_metrics`、`daily_scores`、`chip_health`、`group_metrics`、`market_daily` | 依目前規則全量重建，屬 restated history |
| OOS as-seen 層 | `oos_snapshot_runs`、`oos_signal_snapshots`、`oos_group_snapshots`、`oos_market_snapshots` | append-only，不覆寫舊發布 |
| 發布層 | `index.html`、`archive/<資料日>.html`、`reports/` | 首頁可重建；同日 archive 首次建立後不覆寫 |

衍生表回答「把現行規則套回歷史會得到什麼」；正式 OOS 回答「當天第一次發布時，使用者
實際看到了什麼」。同一資料日若修復後重跑會新增快照，驗證固定採最早正式發布版；只有 HTML
舊頁、沒有機器快照的日期，不得事後拼成 OOS。

### 自動化流程

所有時間皆為台灣時間：

```text
平日 18:07  價格 + 法人 raw checkpoint（不重算、不發布）
平日 19:07  再次 checkpoint；若 Actions 延遲到 23:40 後才啟動，直接正式補完
       ↓
平日 23:47  TDCC → 五表終版補完 → 衍生指標 → score
             → 正式 OOS snapshot → index + immutable archive → commit

週六 09:00  validate.py → reports/validate_<資料日>.md
每月/每季   fetch_financials.py → 月營收與財報四表（不進評分）
```

正式晚場同時要求台北 23:40 終版時間門檻，以及五張原始表、universe、評分與
族群資料完整，兩者都通過才發布。任一交易所來源失敗時，
已成功部分會先寫入 SQLite 並保存 checkpoint，但工作流保持失敗，停止 score、OOS 快照與網站更新。
所有會寫回 `main` 的工作流共用同一 FIFO concurrency group，並在實際開始時 checkout
最新 `main`；push/rebase 衝突一律標紅，不得以成功結束。完整場 push 後還會等待
Pages latest build 確認已部署同一 commit，失敗或 5 分鐘逾時都會標紅。

## 儀表板怎麼看

建議依頁面順序閱讀：

1. **今日重點**：先確認「資料至」日期、陳舊警示與大盤 regime，不把最新頁誤認為最新資料。
2. **台積電專區**：閱讀上游價格、外資持股、月營收與法說指引；這一區全為觀察層。
3. **族群比較**：四象限看價籌位置與 5 日位移，熱圖比較各欄名次，排行榜逐欄排序；三個視圖
   使用同一批資料並聯動高亮。相對最好不等於原始值已轉正。
4. **個股分層**：可按族群篩選、展開所有成員，並查看近 5 日已確認分層的變化。
5. **族群內個股**：搜尋或單維排序；七因子列可展開原始值、門檻量尺、權重與加權貢獻。
6. **個股抽屜**：同一處查看分數驗算、技術/基本面、籌碼健康度、官方數據解剖，以及分頁保存的
   正式筆記與領先假說。後四者都不會偷偷改變分數。

歷史日期選單讀的是當日首次建立的 archive，不會拿今天的規則或研究內容回填舊畫面。

## OOS 驗證與策略治理

[`scripts/validate.py`](scripts/validate.py) 預設以 10 個交易日後、相對族群中位報酬驗證：

- 七因子與 composite 的族群內 IC。
- 各 tier 與 tier 轉移的前瞻超額報酬。
- 蓄勢條件鏈、族群狀態與 `med_dip` 命中率。
- 市值公平性，以及 TDCC/借券等未計分觀察因子。

策略判斷只認正式 as-seen 快照的 OOS 欄。完整門檻見
[`WEEKLY_REVIEW.md`](WEEKLY_REVIEW.md)：不因單日、單週或 in-sample 結果調參；每次最多改
1～2 個旋鈕。若更動權重或 tier 條件，必須同時把 `validate.py` 的 `IS_CUTOFF` 更新為當天，
並在 `CHANGELOG.md` 記錄報告、指標與決策依據。

## 本地使用與維運

所有 session 先 `git pull`，Python 一律透過 `uv` 使用 3.12。正式晚場還需要
`FINMIND_TOKEN`；可選配 `FINMIND_TOKEN2`、`FINMIND_TOKEN3`，或放在已忽略的 `.mcp.json`。

```powershell
# 只讀：盤後資料鮮度、族群、分層變化與品質摘要
git pull
uv run --no-project --python 3.12 python scripts/daily_brief.py

# 23:40 後人工補跑完整正式管線；會發布本地 OOS snapshot，但不 commit/push
uv run --no-project --python 3.12 python scripts/run_daily.py

# 週度驗證、正式 DB 唯讀稽核、完整測試
uv run --no-project --python 3.12 python scripts/validate.py
uv run --no-project --python 3.12 python scripts/audit_raw_data.py
uv run --no-project --python 3.12 python -m unittest discover -s tests
```

`run_daily.py` 可安全重跑，只補缺口；上游未齊時會拒絕正式發布。它不會替你 review、commit
或 push。

### Daily Fetch 日誌判讀與續跑語意

- 日誌的「官方批次 `P` 次」只計五張表的 TWSE/TPEx 呼叫。完整新交易日通常為 10 次；
  早場為 4 次，早場已完成時晚場通常再補 6 次。
- `P=0` 代表指定缺口已完整而跳過，不是資料源失敗。FinMind 事件呼叫與 `market_index`
  額外官方請求會分開列示；後者是非阻斷觀察層。
- 一個市場成功、另一個失敗時，成功資料先落地；下次依 SQLite 缺口接續。空回應或 universe
  覆蓋不足不會被補成 0。
- `holding` 日內初版不視為正式終版；`--final-pass` 對當日資料有台北 23:40 硬門檻，
  23:47 排程會刷新 holding，上游資料未齊時不發布，同日重跑維持冪等。
- schema 新增欄位的歷史 `NULL` 使用 `--backfill-expanded-fields`；只有交易所公告來源修正版、
  既有非空值也必須覆寫時才用 `--force`。

完整退出碼、請求量與 restatement 順序見
[`RAW_DATA_BACKFILL.md`](RAW_DATA_BACKFILL.md)。每日異常排查見
[`DAILY_CHECK.md`](DAILY_CHECK.md)。

## Universe 治理

Universe 每季檢視一次；[`scripts/screen.py`](scripts/screen.py) 產生現有成員體檢與候選報告，
但不自動改名單或族群。

| 規則 | 現行標準 |
|---|---|
| R1 業務歸屬 | 主營收 >50% 屬該族群；優先判斷公司賣自有產品，或收代工/測試/通路/工程服務費，由一手文件人工覆核 |
| R2 規模遲滯 | 候選市值 ≥50 億才可納入；既有成員跌破 30 億才建議剔除，30～50 億留在緩衝帶 |
| R3 流動性 | 候選近 20 日中位成交值 ≥3,000 萬；既有成員未達時列觀察，不自動剔除 |
| R4 冷啟動 | 候選至少有 60 個交易日 |

一檔股票只屬一個族群，跨域公司依主要商業模式與籌碼可比性歸類。`screen.py` 的業務關鍵字
檢查只負責提示疑點，不可取代 R1 人工判斷。季度檢視也應以正式質化筆記重新核對
`universe.csv` 的 `biz` 與 group：純文字過時可修 metadata；族群歸類疑義必須回到治理流程，
不得自動搬移。

### 新增族群

族群由 `groups.csv` 與 `universe.csv` 配置驅動，但仍須同時完成下列工作：

1. 維持至少 6 檔有效樣本，避免中位數與排名被少數個股主導。
2. 回補新成員原始資料，重建衍生表，並補齊質化筆記與事件錨點的 `guidance_<group>`。
3. 檢查儀表板、lint、測試與資料完整度，將治理依據記入 `CHANGELOG.md`。
4. 將回補歷史明確視為 restated；新成員/新族群的 OOS 只能從加入後第一份正式快照起算。

TDCC 只提供最新一週，新成員加入前的週資料無法補回。Universe 變更也會改變族群中位數與
所有成員排名，因此回補後的漂亮歷史不能當成策略證據。

## 質化研究筆記(`notes/qualitative/`)

正式筆記用於 R1 業務歸屬與公司研究，不進量化分數。搜尋結果、新聞與法說摘要只能協助定位；
主張必須回到公司 IR、年報/財報、MOPS 或交易所文件。

新建或重新展開完整研究一律使用 `research_profile: focused_v1`；既有未標 profile 的 v2
筆記仍依原契約有效，等下次實質重做才遷移。focused 流程的核心要求是：

- 使用 3～5 份核心一手文件，涵蓋年報、年度財報、最新季報與最新法說；年報含查核財報時
  可由同一 PDF 承擔兩個 role。
- 正文聚焦約 25～35 個重要 claim block，每個實質段落、bullet 或表格列以 `[S#]` 對到實際頁。
- 每份缺失文件最多尋找 10 分鐘；找不到就記錄 timeout、刪除未驗證主張，不用二手來源補洞。
- Drafter 建立內容定址 evidence pack；reviewer 使用同一 pack 離線重算 SHA、數字、期間、
  單位與推論邊界，不重新下載另一份文件。
- `qual_review.py` 只做唯讀 triage；HARD 項未清除不能簽核，機器命中也不等於人工驗證通過。
- 完成 `independently_verified` 後，只提交該 note 與對應 manifest，立即做成一個獨立中文 commit；
  PDF/PNG 留在 `tmp/`。

筆記品質狀態分為 `ai_draft`、`partially_verified`、`independently_verified`、`conflicted`；
內容時效與查核品質是兩條獨立軸，儀表板會分開顯示。

```powershell
uv run --no-project --python 3.12 python scripts/qual_notes.py --needs-review
uv run --no-project --python 3.12 python scripts/qual_notes.py --lint
uv run --no-project --python 3.12 python scripts/qual_review.py <股號>
```

逐篇查核與 evidence pack 命令見
[`QUALITATIVE_RESEARCH_RUNBOOK.md`](QUALITATIVE_RESEARCH_RUNBOOK.md)；官方文件取得順序與備援見
[`QUALITATIVE_SOURCE_ACQUISITION.md`](QUALITATIVE_SOURCE_ACQUISITION.md)。

## 領先假說（市場小作文）

[`notes/leading_hypotheses/`](notes/leading_hypotheses/) 保存市場流傳、可追溯且可證偽，
但尚未被正式一手文件完整覆蓋的主張。它不是事實認證，也不進分數。

- 只為有效 `independently_verified` 正式筆記建立，並以內容 SHA 錨定當時比較的正式版本。
- 每則保留消息發布日、實際研究收錄日、前瞻/回溯、獨立消息鏈、證據警示、生命週期、
  可證偽條件與期限；轉載同一原始事件不算多條獨立證據。
- 狀態只能由正式文件、可重算實績或事前里程碑轉移；股價與觀察層數據只可當捕捉觸發器。
- 看多/看空敘事必須各引用現有 H#、說明最脆弱處，並用 1～3 條「勝負手」交給未來資料裁決。

```powershell
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --lint
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --due
uv run --no-project --python 3.12 python scripts/leading_hypotheses.py --context <股號>
```

完整收錄邊界與操作見 [`LEADING_HYPOTHESES.md`](LEADING_HYPOTHESES.md) 與
[`LEADING_HYPOTHESES_PHASE2_RUNBOOK.md`](LEADING_HYPOTHESES_PHASE2_RUNBOOK.md)。

## 事件錨點與台積電專區

台積電 2330 是觀察層參考股，不在 universe，也不參與 `daily_metrics`、`daily_scores` 或任何
排名。每日收盤/外資持股寫入隔離的 `ref_price`、`ref_holding`；月營收與財報由獨立排程更新。

[`notes/events/`](notes/events/) 保存每季法說會等跨個股事件。每份事件必須為所有正式族群提供
`guidance_<group>`，即使未提及也明確寫 `none`；儀表板用它產生台積電專區與族群卡指引 chip。
這些方向是編輯彙整，不是預測。每季法說後更新事件日期、KPI、guidance、`next_review`，並執行：

```powershell
uv run --no-project --python 3.12 python scripts/qual_notes.py --lint
```

## 專案入口

| 需求 | 入口 |
|---|---|
| 盤後確認與今日討論 | [`DAILY_CHECK.md`](DAILY_CHECK.md)、`scripts/daily_brief.py` |
| 原始欄位回補/正式 DB 稽核 | [`RAW_DATA_BACKFILL.md`](RAW_DATA_BACKFILL.md)、`scripts/audit_raw_data.py` |
| 週六策略檢視 | [`WEEKLY_REVIEW.md`](WEEKLY_REVIEW.md)、`scripts/validate.py` |
| Universe 與候選 | 本頁「Universe 治理」、`scripts/screen.py`、`config/` |
| 質化筆記 | [`QUALITATIVE_RESEARCH_RUNBOOK.md`](QUALITATIVE_RESEARCH_RUNBOOK.md)、`scripts/qual_notes.py`、`scripts/qual_evidence.py`、`scripts/qual_review.py` |
| 領先假說 | [`LEADING_HYPOTHESES.md`](LEADING_HYPOTHESES.md)、[`LEADING_HYPOTHESES_PHASE2_RUNBOOK.md`](LEADING_HYPOTHESES_PHASE2_RUNBOOK.md) |
| 策略與資料變更歷史 | [`CHANGELOG.md`](CHANGELOG.md) |

## 已知限制

- 券商分點資料未涵蓋；系統能看法人別，不能辨識實際分點主力。
- TDCC opendata 只有最新一週，漏抓無法事後補回；外資持股也可能受保管行重分類影響。
- 減資參考價未納入還原事件；無事件大幅跳空只能警告，仍需人工查核。
- 歷史最前段若尚無當日股本，衍生指標會以第一筆可得股本作種子；研究長窗時應注意這個邊界。
- 排名、tier、族群狀態、研究筆記與領先假說都不是報酬保證。本專案為研究工具，**非投資建議**。
