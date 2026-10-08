# strong-weak-scanner · 台股汰弱留強掃描

針對台股半導體與 AI 供應鏈的相對強弱研究系統。現行 universe 由
[`config/universe.csv`](config/universe.csv) 定義，共 121 檔、11 個族群：被動元件、
功率元件、封測、記憶體、矽智財、半導體設備、半導體材料、散熱、PCB/CCL、電源供應、
伺服器組裝/機構。

- **儀表板**：<https://dennisliuck.github.io/strong-weak-scanner/>
- **設定來源**：[`config/groups.csv`](config/groups.csv)、
  [`config/universe.csv`](config/universe.csv)、[`config/candidates.csv`](config/candidates.csv)、
  [`config/ranking_roles.csv`](config/ranking_roles.csv)
- **版本沿革與實證依據**：[`CHANGELOG.md`](CHANGELOG.md)
- **短週期策略實驗**：[`reports/experiment_lab.html`](reports/experiment_lab.html)，
  [實驗規格與操作](EXPERIMENT_LAB.md)。以歷史重播及 1／3／5 日前瞻，在約 2～5 週內安排
  下一輪保留／簡化／重設；目前比較短線反轉的兩日平滑與 25% 趨勢搭配，
  同時檢查 IC 與名單穩定度。專案用於實驗，不用於真實交易。

核心每日管線只使用 Python 3.12 標準庫與 SQLite。原始資料、正式 OOS 快照、儀表板歷史頁
與驗證報告都保留在 repo，讓每次發布可以追溯。質化證據包的 PDF 驗證與轉圖另需 Poppler。

## 方法論

> **先用籌碼聚合判斷資金正在佈局哪個族群，再用價格相對因子在族群內選強汰弱。**

這個拆分是系統最重要的邊界：外資或投信在整個市場的流向，適合回答「哪個族群受關注」；
同一族群內誰較強，主要交給相對強弱與修正日抗跌。排名結果只代表同業相對位置，不能反推
原始值一定為正，也不代表未來股價方向。

| 層級 | 回答的問題 | 現行訊號 | 輸出 |
|---|---|---|---|
| 個股層 | 同族群裡誰強、誰弱 | 六個計分因子＋一個分層 gate、3 日平滑、分層確認 | composite 與 tier |
| 族群層 | 哪個供應鏈正在被佈局或領漲 | 外資廣度、修正日中位買賣、相對動能、距高 | 族群狀態，不改個股分數 |
| 大盤層 | 目前是否進入修正環境 | 含息報酬指數距 20 日高 | regime，不改個股分數 |
| 多視角觀察層 | 換一個問題時，族群內名次如何改變 | A 趨勢領先、B 防守韌性、C 籌碼支持、D 基本面改善、角色同儕與 Pareto | 平行百分位，不改 composite/tier |
| 觀察與研究層 | 數字如何形成、公司在做什麼、市場在傳什麼 | 官方資料解剖、技術/基本面、TDCC、借券、研究筆記、領先假說、台積電事件 | 閱讀背景，不計分 |

### 個股層：六個計分因子＋一個分層 gate

[`scripts/score.py`](scripts/score.py) 的 CONFIG 是正式個股策略唯一旋鈕來源。
實驗候選另集中在 [`config/experiment_lab.json`](config/experiment_lab.json)，採獨立 round，
不受正式 F10 長期升格門檻限制，也不改正式分數。價格、抗跌、外資、
投信與修正日買賣先在同族群內排五分位，得到 −2～+2 分；有效樣本少於 4 檔時不排名。
外資、投信、修正日買賣另有雜訊死區，避免全族群都接近零時仍被硬分高低。
相同原始值採平均序位後映射分數；`composite`與三日平滑值均round到小數2位。
tier前2／倒2的同分邊界也採平均名次，同分者一同納入或排除，結果不依輸入列順序。

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

### 多視角排名：同一組股票回答四個問題

[`scripts/ranking_views.py`](scripts/ranking_views.py) 是觀察層，不修改 `daily_scores` 或 tier。
每個視角都在正式族群內使用平均秩百分位：exact tie 拿同一個中點名次，輸入列順序不影響
結果。畫面同時顯示共識數、視角分歧、Pareto frontier、leave-one-peer-out 敏感度，以及
[`config/ranking_roles.csv`](config/ranking_roles.csv) 的角色同儕排名；角色樣本少於 4 檔時
只顯示角色，不硬排小樣本。

| 視角 | 問題 | 原料 | 更新頻率 |
|---|---|---|---|
| A 趨勢領先 | 誰在不同價格週期相對領先？ | 收盤/MA5、20 日報酬、MA20/MA60 | 每日 |
| B 防守韌性 | 誰目前較不脆弱？ | 修正日抗跌、低融資水位、低量價過熱；官方風險旗標封頂 | 每日 |
| C 籌碼支持 | 誰的法人相對位置靠前？ | 外資、投信、修正日買賣、融資；TDCC/借券只作未驗證旁證 | 每日／週 |
| D 基本面改善 | 截至當時已知資料，誰的成長與營運品質靠前？ | 3 月營收年增與加速度、營益率與年變化 | 月／季 |

D 視角只讀 `fundamental_availability.first_seen_at` 已證明當時可見的資料。既有歷史資料在
ledger 建立前不回填過去排名；2026-08-13 migration 時的既有資料只從該時點起視為已知，
後續抓取同樣保留第一次看到的時間。這個保守下界避免用財報期間日冒充發布日造成 look-ahead。

D 的月、季比較期間分別採「正式 universe 當期原始值 100% 到齊」的最新共同月份／季度，
參考股票不參與選期；季度須同時有營收與營業利益。少數早報者只更新新期間覆蓋提示，
不推動整體切期。前年比較或必要 component 缺失仍保留空值；共同期間到齊不保證每檔都有
足夠 component 可排名。沒有共同期間時暫停 D，並以品質警告顯示，不補 0。
每次新期間資料不齊，頁面與 ranking audit 都顯示已收檔數、比較期與待切換期。

正式 Champion 權重維持上表。三個影子 challenger 隨正式快照 append-only 累積：
C1 把量能權重設為0、C2 把價格權重降為1.0、C3 把抗跌權重降為0.5；它們只比較族群名次，
不改正式tier。`spec_sha`覆蓋ranking contract、會影響計算的helper與score規則依賴；
score也有自己的spec與建置metadata。定義一變就開新OOS時鐘，只有同spec的首次及時正式
快照可進成效样本，後來修正版不能代替首次發布。

平行視角不以短期勝率互相比賽，也不因單日 tie／Pareto 數量調參。完整的五層評估矩陣、
分階段門檻、factor 保留／移除／新增條件與 UX 任務見
[`PARALLEL_VIEWS_ROADMAP.md`](PARALLEL_VIEWS_ROADMAP.md)。
[`scripts/audit_ranking_views.py`](scripts/audit_ranking_views.py) 每日只讀檢查覆蓋、tie、
peer sensitivity、component 與 append-only spec 進度；正式 final pipeline 在凍結快照後
要求當日完整，缺列、混 spec 或 JSON 損壞會先於儀表板發布失敗。

儀表板的多視角工作台固定在單一正式族群內比較。使用者直接點正式綜合或 A–D 問題頁籤，
左側排行會立即重排，右側同步解釋所選個股為何在不同問題下位置不同；手機依相同順序改成
單欄。共識、Pareto、tie、角色同儕與 peer sensitivity 都留在按需展開的結構診斷，不作預設
篩選，也不合成另一個推薦分數。

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

大盤使用 TWSE 官方 `MI_INDEX` 的發行量加權股價報酬指數（含息）；距 20 日高 ≤−3%
時標為修正 regime。FinMind 同口徑 TAIEX 只做逐日交叉驗證，官方缺值時才作備援。
含息口徑可避免除息季的機械性下跌被誤判為市場修正，與個股使用還原價的原則一致。

### 明確不計分的內容

- `chip_health` 是七個籌碼方向的描述性診斷，不是族群內排名；其中 TDCC 大戶、股東人數、
  借券三項仍待 OOS 累積後裁決。交易所處置/注意旗標會直接標成待觀察，但不改 composite。
- MA5/20/60、RSI14、價量關係與穿越事件只描述個股相對自身歷史。
- 官方資料「數據解剖」展示成交筆數、法人買賣兩側、融資券流量、外資限額、借券拆分與
  相對所屬市場報酬指數；個股與族群版本都不計分。
- 月營收、財報、質化筆記、領先假說與研究中心的台積電法說事件都是研究背景，不直接餵入 tier。

## 資料、重算與發布邊界

### 資料來源

| 類別 | 來源與用途 |
|---|---|
| 每日五張原始表 | TWSE/TPEx 全市場批次：價格、法人、融資券、外資持股、借券；另抓處置/注意公告 |
| 還原與市場序列 | FinMind 提供除權息/分割事件；TAIEX 含息序列以 TWSE 官方 `MI_INDEX` 為正式主來源，FinMind 同序列作交叉驗證／官方缺值備援；TPEx 報酬指數仍只供觀察 |
| 週/月/季資料 | TDCC 股權分散週快照；FinMind 月營收、損益表、資產負債表、現金流量表 |
| 研究資料 | 公司 IR、MOPS、TWSE/TPEx 文件與人工維護的質化筆記、領先假說、事件錨點 |

每日價格因子使用本地倒推的 `price_adj`。除權息與分割有事件資料可重算；減資參考價未涵蓋，
以「無事件大幅跳空」警告兜底。TDCC 只提供最新一週，週五快照到次週一才生效，避免前視。

### SQLite 分層

| 層 | 主要內容 | 更新語意 |
|---|---|---|
| 原始層 | `price`、`inst`、`margin`、`holding`、`sbl`、`risk_flags`、`market`、`market_provenance`、`market_index`、`tdcc_holding`、財報、`fundamental_availability` 與 `ref_*` | 依主鍵冪等補缺；財報 first-seen 不覆寫；大盤 canonical 保留逐日來源與雙邊原值 |
| 衍生層 | `price_adj`、`daily_metrics`、`observation_metrics`、`daily_scores`、`chip_health`、`group_metrics`、`market_daily` | 依目前規則全量重建，屬 restated history |
| OOS as-seen 層 | `oos_snapshot_runs`、`oos_signal_snapshots`、`oos_group_snapshots`、`oos_market_snapshots`、`oos_ranking_view_snapshots` | append-only，不覆寫舊發布；多視角另存 spec hash |
| 發布層 | `index.html`、`research.html`、`archive/<資料日>.html`、`reports/` | 首頁與研究中心可重建；同日 archive 首次建立後不覆寫 |

衍生表回答「把現行規則套回歷史會得到什麼」；正式 OOS 回答「當天第一次發布時，使用者
實際看到了什麼」。同一資料日若修復後重跑會新增快照，驗證固定採最早正式發布版；只有 HTML
舊頁、沒有機器快照的日期，不得事後拼成 OOS。

### 自動化流程

所有時間皆為台灣時間：

```text
平日 18:07  價格 + 法人 raw checkpoint（不重算、不發布）
平日 19:07  再次 checkpoint；若 Actions 延遲到 23:40 後才啟動，直接正式補完
平日 21:47  提前排隊；23:40 前啟動仍只做 checkpoint，延遲跨過門檻則正式補完
       ↓
平日 23:47  TDCC → 五表終版補完 → 衍生指標 → score → A/B/C/D 與 C1/C2/C3
             → 正式 OOS snapshot → index + immutable archive → commit

週六 09:00  validate.py → reports/validate_<資料日>.md
每月/每季   fetch_financials.py → 月營收與財報四表（不進評分）
```

正式晚場同時要求台北 23:40 終版時間門檻，以及五張原始表、universe、評分與
族群資料完整，兩者都通過才發布。任一交易所來源失敗時，
已成功部分會先寫入 SQLite 並保存 checkpoint，但工作流保持失敗，停止 score、OOS 快照與網站更新。
晚間 workflow 以 runner 的 UTC 日期鎖定資料目標日；因此排程即使延遲跨過台北午夜，
仍會補原交易日，不會誤把隔日當成當日 final pass。
所有會寫回 `main` 的工作流共用同一 FIFO concurrency group，並在實際開始時 checkout
最新 `main`；push/rebase 衝突一律標紅，不得以成功結束。完整場 push 後還會等待
Pages latest build 確認已部署同一 commit，失敗或 5 分鐘逾時都會標紅。

## 儀表板怎麼看

建議依頁面順序閱讀：

1. **今日重點**：先確認「資料至」日期、陳舊警示與大盤 regime，不把最新頁誤認為最新資料。
2. **最近研究**：首頁保留正式筆記、多空小作文、市場議題三類入口；事件錨點歸入市場議題。
   點擊後在研究中心閱讀全文。研究中心的「文章」以搜尋、文章類型與排序找資料；
   族群、查核狀態與更新時間放在「篩選」抽屜。清單只列原題名、既有摘要、類型、狀態與日期，
   不把研究問題、任務與證據說明堆成多層卡片。新近不代表證據較強。

   桌機預設並排文章清單與正文；選文不另開頁、不隱藏清單。標題下保留更新日期、原始查核狀態、
   依臺北日曆即時判定的可信度、閱讀時間與複製連結，接著直接顯示原文段落。正文保持原順序、
   原數字、來源編號與證據邊界；不在每節前另外插入任務、章節接力、讀表教學或重複摘要。
   「專注閱讀」需讀者自行開啟，可隨時退出。

   閱讀工具列提供三個按需開啟的面板：「目錄」跳到正文原章節；「查核資料」收納可信度判定、
   全部來源、GitHub 原始文件及完整主張／追蹤附錄；「閱讀輔助」收納同篇新手導讀、名詞、
   研究摘要、產業角色、學習路線、下一站與相關研究類型。輔助內容沿用已發布的文字與正式路線，
   不從題名或正文生成新的研究結論。對話框可用 Escape 關閉，關閉後回到原閱讀位置。
   原始文件與外部一手來源可另開分頁；能對應到既有文章的站內研究連結則在同一閱讀器開啟。

   手機依序顯示清單或文章，文章上方固定保留「返回清單」與閱讀工具；從矩陣、雷達或圖譜開文，
   另可「返回來源」。瀏覽器上一頁／下一頁及重新整理保留搜尋、篩選、文章與閱讀位置。
   搜尋時不會重建正在閱讀的同篇正文；沿延伸連結換篇時，也不會被原篩選拉回舊文。

   市場議題表格在窄欄改為帶原欄名的逐列閱讀卡；查核附錄保留可聚焦的水平捲動表格。
   顯示層只清除可確定的中文排版空白、翻譯本文內部族群 ID 與固定維運詞，原始 Markdown、
   runs、研究 payload、連結、查核狀態與帳本均不回寫。名詞解釋優先逐字取自同篇字典，
   跨篇共通語則由 `config/research_reader_terms.csv` 明示來源與邊界。

   「產業探索」集中族群矩陣與知識圖譜；清單上的選用閱讀路線預設收合。
   「研究追蹤」開啟既有研究雷達。學習路線只安排閱讀次序；共同公司、族群與圖譜關係只作
   可回查的延伸入口，不推定上下游、受惠、訂單、因果或投資排序。

   研究雷達以白話問題、既有文章入口、下一次查核與候選順序呈現；目前線索、族群問句與研究
   查核可再展開。由雷達進入矩陣或文章時，保留同一問題與返回入口，不把候選研究順序當投資排名。
   族群矩陣提供「從問題開始」與「已知道族群」兩種入口，族群角色取自
   `config/research_group_guide.csv`；各列以族群起點、已完成、最大缺口、下一步呈現研究進度。
   題材財務影響仍區分公司整體、事業部、產品與單位經濟，不以公司總營收當成題材收入。

   知識圖譜沿用同一證據底層的「公司曝險／產業依賴」雙視圖；路線、階段與站次皆取正式登錄，
   關係解讀完整保留來源、證據層級、商業成熟度、材料性、集中度、期限與一跳邊界。
   從文章的閱讀輔助進圖時，保留原文章與既有關係；返回文章可繼續閱讀。族群角色只對回唯一
   已登錄關係，無對應或多條對應時不猜線。完整操作與版面驗收見 `design-qa.md`。
   介面圖示使用隨站保存的 Heroicons 2.2.0 outline SVG，授權保留於 `assets/heroicons/LICENSE`。

3. **族群比較**：四象限看價籌位置與 5 日位移，熱圖比較各欄名次，排行榜逐欄排序；三個視圖
   使用同一批資料並聯動高亮。明細可直接開啟成分股，再返回來源族群。相對最好不等於原始值已轉正。
4. **個股分層**：可按族群篩選、展開所有成員，並查看近 5 日已確認分層的變化。
5. **多視角排名**：先固定一個族群，再直接點正式綜合或 A/B/C/D 問題重排；左側選股、右側
   比較五個百分位與差異說明，共識、Pareto、角色 rank、peer sensitivity 與 tie 收在診斷層。
6. **族群內個股**：搜尋或單維排序；可選「全部族群」分組查找，空結果提供跨族群命中入口
   與清除搜尋。搜尋保留族群原排序位置，各族群分開排序。六個計分因子與一個 gate
   可展開原始值、門檻量尺、權重與加權貢獻。
7. **個股抽屜**：同一處查看分數驗算、技術/基本面、籌碼健康度、官方數據解剖，以及分頁保存的
   正式筆記與領先假說。後四者都不會偷偷改變分數。

「快速前往」中的歷史日期選單會另開當日首次建立的 archive，保留目前掃描頁；
不會拿今天的規則或研究內容回填舊畫面。瀏覽器無法儲存偏好時，深淺色與閱讀模式
仍可在本次頁面切換。

## OOS 驗證與策略治理

[`scripts/validate.py`](scripts/validate.py) 預設以 10 個交易日後、相對族群中位報酬驗證：

- 六個計分因子、分層 gate 與 composite 的族群內 IC。
- 各 tier 與 tier 轉移的前瞻超額報酬。
- 蓄勢條件鏈、族群狀態與 `med_dip` 命中率。
- 市值公平性，以及 TDCC/借券等未計分觀察因子。
- §⑫ 只以現行spec的 append-only 快照比較 Champion、C1/C2/C3，並追蹤 A/B/C/D；未成熟
  時不報假精確的 SE/t，也不以點估計更換 Champion。

策略判斷只認正式 as-seen 快照的 OOS 欄。完整門檻見
[`WEEKLY_REVIEW.md`](WEEKLY_REVIEW.md)：不因單日、單週或 in-sample 結果調參；每次最多改
1～2 個旋鈕。若更動權重或 tier 條件，必須同時把 `validate.py` 的 `IS_CUTOFF` 更新為當天，
並在 `CHANGELOG.md` 記錄報告、指標與決策依據。

多視角另以 [`PARALLEL_VIEWS_ROADMAP.md`](PARALLEL_VIEWS_ROADMAP.md) 分開處理操作完整性、
量測可靠性、視角差異性、使用者效用與 OOS 結果；前四層不等同預測證據，第五層也只有
C1/C2/C3 能依 §⑫ 取得進一步研究資格。現行驗收、固定首100／200／300個成熟配對日的
檢視與前瞻成本研究，依[策略驗證契約](STRATEGY_VALIDATION_PROTOCOL.md)；每週
`reports/validation_progress.json`顯示樣本進度。分級t只是探索門檻，不保證多重比較錯誤率，
沒有自動更換正式策略的路徑。

## 本地使用與維運

所有 session 先 `git pull`，Python 使用 3.12（python.org 安裝，PSF 簽章）。正式晚場還需要
`FINMIND_TOKEN`；可選配 `FINMIND_TOKEN2`、`FINMIND_TOKEN3`，或放在已忽略的 `.mcp.json`。

```powershell
# 只讀：盤後資料鮮度、族群、分層變化與品質摘要
git pull
python scripts/daily_brief.py

# 23:40 後人工補跑完整正式管線；會發布本地 OOS snapshot，但不 commit/push
python scripts/run_daily.py

# 週度驗證、正式 DB 唯讀稽核、完整測試
python scripts/audit_ranking_views.py --compact
python scripts/validate.py
python scripts/audit_raw_data.py
python scripts/audit_storage.py
python -m unittest discover -s tests
```

`run_daily.py` 可安全重跑，只補缺口；上游未齊時會拒絕正式發布。它不會替你 review、commit
或 push。
補過去資料日請明確指定 `--end YYYY-MM-DD`；本地與 Actions 在評分前都先執行五表稽核。
正式快照保留實際 `captured_at`；新快照若晚於資料日次日台北 09:00 的保守期限，標為
`late_recovery`／`oos_eligible=false`，可發布完整資料，但不計入週報及首頁的 OOS 成效樣本。
此期限不推定休市日，可能保守排除假日延遲；不回填或改寫舊快照的判定。

`audit_storage.py` 只讀取 DB 容量、表／索引配置與 GitHub 單檔門檻；可加
`--gzip-probe --json` 在記憶體測試壓縮及 SHA-256 復原，不改資料或產生備份檔。
超過 50 MiB 只警告，超過 100 MiB 或量測不一致才回傳錯誤；退出碼與後續方案見
[SQLite 儲存評估](reports/storage_audit_2026-08-29.md)。

`db_artifact.py` 可從指定完整 commit 建立 gzip＋manifest，並只復原到隔離副本；
目的地禁止正式 `data/`，復原前必須提供可信來源的 commit 與 manifest SHA-256。
`check_db_artifact.py` 會比對原始 bytes、raw／OOS 稽核、完整測試與儀表板輸出。
手動 `db-artifact-smoke` 使用兩個獨立 runner 演練發布／下載，artifact 只保留一天，
不寫 main、不替代正式備份，也未改變每日管線。操作與限制見
[DB artifact 隔離演練](DB_ARTIFACT_RUNBOOK.md)。

### Daily Fetch 日誌判讀與續跑語意

- 日誌的「官方批次 `P` 次」只計五張表的 TWSE/TPEx 呼叫。完整新交易日通常為 10 次；
  早場為 4 次，早場已完成時晚場通常再補 6 次。
- `P=0` 代表指定缺口已完整而跳過，不是資料源失敗。FinMind 事件呼叫與 `market_index`
  額外官方請求會分開列示；其中 TWSE 含息報酬指數是正式大盤主來源，TPEx 指數仍是
  非阻斷觀察層。
- 一個市場成功、另一個失敗時，成功資料先落地；下次依 SQLite 缺口接續。空回應或 universe
  覆蓋不足不會被補成 0。
- 交易所價格表若明確回傳 OHLC 全空、成交量／金額／筆數皆為 0，會衍生一筆
  `trading_status=no_trade`。這類股票當日不在法人日報的有效母體內，但 price、margin、
  holding、sbl 仍須有官方列；未知或未被原始價格列驗證的缺口照常標紅。停牌日不產生
  `daily_metrics`／`daily_scores`，不推進平滑分數或 tier，復牌後的技術視窗接續前一有效交易日。
- 若價格整列缺席，先查 TWSE／TPEx 官方減資預告表。只有明確「停止日 ≤ 資料日 < 復牌日」
  的公告可豁免該股的 price／inst；margin／holding／sbl 仍須完整，不補零、不沿用昨日價格。
  `suspension_evidence` 保存該資料日的完整 JSON、官方 URL、取件時間與 SHA256；抓取、
  稽核、快照與儀表板都離線重算原文與日期。舊日查核不能授權新日，復牌日自動恢復必填；
  未知／無復牌日停牌、來源失敗、缺欄或公告與成交衝突仍標紅。只在缺價時額外查兩市場，
  同日成功續跑不再重打。SHA 是完整性檢查，不是來源簽章或 ACL。
- 角色設定仍驗完整 universe；當日排名只使用有效交易母體。停牌股保留在畫面，顯示前次
  訊號日期及停牌來源，不產生新的分數或排名。
- `holding` 日內初版不視為正式終版；`--final-pass` 對當日資料有台北 23:40 硬門檻，
  23:47 排程會刷新 holding，上游資料未齊時不發布，同日重跑維持冪等。
- 完整場的 TAIEX canonical 必須精確到最新交易日：優先採 TWSE 官方含息報酬指數；
  FinMind 未發布只留下「待交叉驗證」狀態，不阻擋官方值。若 TWSE 缺值而 FinMind 已有
  同日值，明示啟用 FinMind 備援；兩邊同日值超出 `1e-6` 容許誤差則硬停，兩邊都缺也會
  在重建 `daily_metrics`／`market_daily` 前停止。Actions 會先保存五表與 TDCC checkpoint，
  不會把舊 regime 凍結成新 OOS 快照。
- schema 新增欄位的歷史 `NULL` 使用 `--backfill-expanded-fields`；只有交易所公告來源修正版、
  既有非空值也必須覆寫時才用 `--force`。

完整退出碼、請求量與 restatement 順序見
[`RAW_DATA_BACKFILL.md`](RAW_DATA_BACKFILL.md)。每日異常排查見
[`DAILY_CHECK.md`](DAILY_CHECK.md)。

## Universe 治理

Universe 每季檢視一次；[`scripts/screen.py`](scripts/screen.py) 產生現有成員體檢與候選報告，
但不自動改名單或族群。候選體檢會呼叫 FinMind（1 + 2×候選數 次），只想看既有成員時用
`--no-candidates`（零 API call、不需 token），探索性執行用 `--dry-run` 避免在 `reports/`
留下看似正式的季度報告。

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
同一份一手文件內的數字矛盾可標 `conflict_kind: source_internal`，但須由完整
focused_v1 pack 綁定至少兩個已引用 PDF 頁碼，仍維持 `conflicted`；跨來源衝突
仍須並列兩份一手來源。

```powershell
python scripts/qual_notes.py --needs-review
python scripts/qual_notes.py --lint
python scripts/qual_review.py <股號>
```

逐篇查核與 evidence pack 命令見
[`QUALITATIVE_RESEARCH_RUNBOOK.md`](QUALITATIVE_RESEARCH_RUNBOOK.md)；官方文件取得順序與備援見
[`QUALITATIVE_SOURCE_ACQUISITION.md`](QUALITATIVE_SOURCE_ACQUISITION.md)。

## 領先假說（市場小作文）

[`notes/leading_hypotheses/`](notes/leading_hypotheses/) 保存市場流傳、可追溯且可證偽，
但尚未被正式一手文件完整覆蓋的主張。它不是事實認證，也不進分數。

- 只為有效 `independently_verified` 正式筆記建立，並以內容 SHA 錨定當時比較的正式版本。
- 正式筆記後續降為有效 `conflicted` 時，只允許全終態的 closed 報告保存歷史，
  仍綁定當前完整 SHA 並顯示衝突警語；不據此建立新的活躍假說。
- 每則保留消息發布日、實際研究收錄日、前瞻/回溯、獨立消息鏈、證據警示、生命週期、
  可證偽條件與期限；轉載同一原始事件不算多條獨立證據。
- 狀態只能由正式文件、可重算實績或事前里程碑轉移；股價與觀察層數據只可當捕捉觸發器。
- 看多/看空敘事必須各引用現有 H#、說明最脆弱處，並用 1～3 條「勝負手」交給未來資料裁決。

```powershell
python scripts/leading_hypotheses.py --lint
python scripts/leading_hypotheses.py --due
python scripts/leading_hypotheses.py --context <股號>
```

完整收錄邊界與操作見 [`LEADING_HYPOTHESES.md`](LEADING_HYPOTHESES.md) 與
[`LEADING_HYPOTHESES_PHASE2_RUNBOOK.md`](LEADING_HYPOTHESES_PHASE2_RUNBOOK.md)。

## 研究更新佇列與市場議題

`scripts/research_queue.py` 把正式筆記、逐則 H#、事件錨點、財報覆蓋、候選市場議題與
實際掃描紀錄聚成一張唯讀待辦；A–D 四個 cohort 每週輪一組，四週涵蓋全 universe。
`notes/research_topics/` 只保存「值得查」的候選議題，不是第四套正式事實庫，也不計分。

```powershell
python scripts/research_queue.py --attention
python scripts/research_queue.py --calendar --weeks 8 --output tmp/research_calendar.md
python scripts/research_queue.py --lint
python scripts/research_radar.py --lint
python scripts/research_method_audit.py --lint --baseline-ref HEAD
```

候選議題必須明列來源發布日、研究捕捉日、受影響族群／股票、route、action due 與
證據邊界；沒有新題目也要在 `scan_log.csv` 留下實際掃描範圍。已簽筆記的 `next_review`
不可單獨 snooze，否則內容 SHA 會失效。跨市場候選另記於 `notes/research_candidates/` 的
active radar，優先級、知識價值、反證與下次證據都要可機讀；只有文章與圖譜同時通過契約後
才可標為升格。完整節奏、SLA 與路由規則見
[`RESEARCH_MAINTENANCE.md`](RESEARCH_MAINTENANCE.md)。

機構公開研究的來源選擇、基本驗證與人工試作流程見
[`MARKET_INTELLIGENCE_SOURCING.md`](MARKET_INTELLIGENCE_SOURCING.md)。

## 事件錨點與研究中心的台積電法說

台積電 2330 是觀察層參考股，不在 universe，也不參與 `daily_metrics`、`daily_scores` 或任何
排名。每日收盤/外資持股寫入隔離的 `ref_price`、`ref_holding`；月營收與財報由獨立排程更新。

[`notes/events/`](notes/events/) 保存每季法說會等跨個股事件。每份事件必須為所有正式族群提供
`guidance_<group>`，即使未提及也明確寫 `none`；研究中心把事件發布為「市場議題」完整文章，
並保留結構化族群方向；儀表板主頁不再放置整個台積電專區。
這些方向是編輯彙整，不是預測。每季法說後更新事件日期、KPI、guidance、`next_review`，並執行：

```powershell
python scripts/qual_notes.py --lint
```

## 專案入口

| 需求 | 入口 |
|---|---|
| 盤後確認與今日討論 | [`DAILY_CHECK.md`](DAILY_CHECK.md)、`scripts/daily_brief.py` |
| 原始欄位回補/正式 DB 稽核 | [`RAW_DATA_BACKFILL.md`](RAW_DATA_BACKFILL.md)、`scripts/audit_raw_data.py` |
| DB 容量／壓縮復原檢查 | [SQLite 儲存評估](reports/storage_audit_2026-08-29.md)、[隔離演練](DB_ARTIFACT_RUNBOOK.md)、`scripts/audit_storage.py` |
| 週六策略檢視 | [`WEEKLY_REVIEW.md`](WEEKLY_REVIEW.md)、`scripts/validate.py` |
| 平行視角評估／UX 調整 | [`PARALLEL_VIEWS_ROADMAP.md`](PARALLEL_VIEWS_ROADMAP.md)、`scripts/audit_ranking_views.py` |
| Universe 與候選 | 本頁「Universe 治理」、`scripts/screen.py`、`config/` |
| 質化筆記 | [`QUALITATIVE_RESEARCH_RUNBOOK.md`](QUALITATIVE_RESEARCH_RUNBOOK.md)、`scripts/qual_notes.py`、`scripts/qual_evidence.py`、`scripts/qual_review.py` |
| 領先假說 | [`LEADING_HYPOTHESES.md`](LEADING_HYPOTHESES.md)、[`LEADING_HYPOTHESES_PHASE2_RUNBOOK.md`](LEADING_HYPOTHESES_PHASE2_RUNBOOK.md) |
| 研究更新／市場議題 | [`RESEARCH_MAINTENANCE.md`](RESEARCH_MAINTENANCE.md)、`scripts/research_queue.py`、`scripts/research_method_audit.py`、`notes/research_topics/`、`notes/research_method_reviews/` |
| 策略與資料變更歷史 | [`CHANGELOG.md`](CHANGELOG.md) |

## 已知限制

- 券商分點資料未涵蓋；系統能看法人別，不能辨識實際分點主力。
- TDCC opendata 只有最新一週，漏抓無法事後補回；外資持股也可能受保管行重分類影響。
- 減資參考價未納入還原事件；無事件大幅跳空只能警告，仍需人工查核。
- 歷史最前段若尚無當日股本，衍生指標會以第一筆可得股本作種子；研究長窗時應注意這個邊界。
- 排名、tier、族群狀態、研究筆記與領先假說都不是報酬保證。本專案為研究工具，**非投資建議**。
