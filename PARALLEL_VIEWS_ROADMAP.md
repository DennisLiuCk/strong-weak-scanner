# 平行視角評估、調整與 UX Roadmap

> 適用範圍：A 領先、B 防守、C 籌碼、D 基本面、角色同儕、共識與 Pareto。
> Champion、C1/C2、tier 與交易成本驗證仍依 `WEEKLY_REVIEW.md`／`validate.py`。
> 本文件規定「什麼時候可以判斷、可以動什麼」，不預告哪個視角會勝出。

## 0. 現在先做什麼

1. **保留 Champion，不把 A–D 合成第五個分數。** A–D 回答四個不同的現在式問題；
   C1/C2 才是用完全相同 OOS 樣本挑戰 Champion 的正式候選。
2. **先凍結 evaluator 並累積正式快照。** 在第一批 append-only 資料形成前，不因單日
   排名、畫面觀感或 restated history 改 components、權重、cap、tie 或 Pareto 定義。
3. **每日先驗操作完整性。** `scripts/audit_ranking_views.py` 在正式快照後執行；缺當日正式
   快照、漏列、混入不同 spec 或 JSON 損壞會硬停，tie／Pareto 過寬等只警告。
4. **UX 改成「先選問題、再看族群內答案」。** 不把不同族群的百分位混成全市場名次；
   共識與 Pareto 是診斷，不是預設的候選聯集。
5. **目前不刪 factor，也不新增第五視角。** 先量出現行四視角的可用性、差異性與理解成本，
   再決定要精簡、拆分或新增，避免資料少時靠主觀增加自由度。

## 1. 每個排名的固定問題

| 顯示名稱 | 使用者真正問的問題 | 允許的解讀 | 不允許的解讀 |
|---|---|---|---|
| Champion／正式綜合 | 依 production composite，族群內目前誰較強？ | 現行正式篩選順序 | 報酬保證 |
| A 趨勢領先／進攻 | 短、波段、趨勢位置目前誰領先？ | 價格行為較強 | 基本面最好、一定續漲 |
| B 防守韌性／懷疑 | 抗跌、低槓桿、低過熱後，誰較安全？ | 分數越高越防守 | 「風險越高」或看空名次 |
| C 籌碼支持／偵察 | 法人、融資與修正日籌碼目前支持誰？ | 可觀察的籌碼支持較強 | 主力身分、內線資訊 |
| D 基本面改善／全局 | point-in-time 可見的營收與營益率誰較強？ | 已公布基本面相對位置 | 全產業絕對可比、估值便宜 |
| 角色同儕 | 相近業務角色內，正式綜合位置如何？ | 小範圍補充比較 | 取代正式族群、角色少於 4 檔硬排名 |

「激進分析師／保守分析師／全球分析師」可以是導覽語氣，但不能掩蓋操作定義。現行 C 是
籌碼，不是全球視角；B 高分代表較防守，不是較看空。若未來要做全球供應鏈視角，必須另立
point-in-time 資料契約與 spec，不應改名假裝現有資料已回答。

## 2. 五層評估矩陣

| 層 | 要回答的問題 | 固定量測 | 何時可行動 |
|---|---|---|---|
| 1. 操作完整性 | 今天的正式排名是否完整、可重現？ | stock/group 覆蓋、duplicate、單一 spec、JSON、當日正式快照、query-only | 每日；hard error 立即修管線，不做策略判斷 |
| 2. 量測可靠性 | 名次是否被缺值、平手或同儕邊界支配？ | component 覆蓋、族群內 tie rate、unique share、top-2 邊界 tie、peer sensitivity、資料 freshness | 每週看趨勢；只跨警戒線不調權重 |
| 3. 視角差異性 | 四個問題是否真的提供不同答案？ | 同日族群內 pairwise rank correlation、top-20 Jaccard、各視角獨有 top-20、相對打散 component 的機械底線 | 現行 spec 累積 20–40 個完整正式日後做第一次結構檢視 |
| 4. 使用者效用 | 使用者能否找對答案、理解方向與限制？ | 任務完成率、第一次點擊、完成時間、B 方向誤讀、跨族群誤讀、能否說明「排名不是預測」 | 每次 UX 選稿前後，以固定任務做 moderated check |
| 5. OOS 結果 | 候選是否在相同樣本上優於 Champion？ | 同日配對 Δrank-IC、Newey-West SE/t、有效獨立觀測、連續區段；通過後另驗 tier／隔日開盤淨成本 | 只有 C1/C2 依 §⑫ gate；A–D 不以短期勝率互相淘汰 |

這五層不能互相替代。操作完整不代表有效；低相關不代表有用；使用者喜歡不代表能預測；
短期 IC 較高也不代表已通過統計門檻。

## 3. 分階段節奏

下列日數是治理節點，不是假裝獨立樣本的統計門檻；所有績效結論仍以 `validate.py` 的
有效獨立觀測與連續區段為準。

### Phase 0 — 第一個正式快照以前

- 只驗 121 檔覆蓋、族群內計算、point-in-time、tie safety、spec 與 pipeline wiring。
- 可以修資料漏列、序列化、文案與資訊架構；不依單日橫斷面調 evaluator。
- 2026-08-12 的 exact census：A/B/C/D 各 121/121；族群內 tie 暴露 A/B/C/D =
  23/24/20/14；共識至少 2 視角 19；Pareto 89；peer sensitivity ≥25 為 36。
  這是完整庫存計數，不是抽樣估計、績效或未來報酬證據。現行 spec 正式日 0、成熟日 0。

### Phase 1 — 1–9 個完整正式日

- 每日 hard gate；每週保存 coverage、tie、peer sensitivity、Pareto selectivity 的走勢。
- 只修明確 bug。任何 component／權重／cap／normalization 變動都建立新 spec，不能接舊資料。
- 開始固定使用者任務，不從點擊偏好反推投資有效性。

### Phase 2 — 至少 10 個完整正式日

- 可判斷操作穩定性與資料 freshness；仍不宣稱預測能力。
- 分 lens 量一日 rank change、top-20 保留率與 turnover。A 應比 D 靈敏，不能用同一個
  「越穩越好」門檻評四個視角。
- 若高 tie 集中在某 component，先查量尺／缺值／低基數；不得直接用 stock_id 打破經濟同分。

### Phase 3 — 20–40 個完整正式日

- 做第一次差異性檢視：實際相關、top-20 overlap 與打散 component 的機械底線一起看。
- 兩視角即使高度重疊，只要回答的任務不同且使用者能正確使用，可以保留但收進同一比較面板；
  若問題相同、結果高度重疊、又沒有獨有使用情境，優先合併顯示，而非再加權湊差異。
- 這一階段可以調 UX 呈現；若要改 evaluator，需寫清楚新問題、失敗條件並重啟 OOS 時鐘。

### Phase 4 — 前瞻成熟且有效獨立觀測達門檻

- 前瞻 10 日下，10 個成熟日約只是一個獨立觀測；實際進度一律讀 §⑨／§⑫。
- C1/C2 的有效獨立觀測 <10 一律累積。達 10 後，正向 paired t 仍須通過
  `stats_ci.t_threshold()`；通過只取得另開 production gate 的資格。
- A–D 的 rank-IC 可作校準背景，但不能選出「最準分析師」。若真要讓 persona 競賽，需另行
  事先登錄同一 outcome、horizon、放棄條件與多重比較處理。

## 4. 保留、精簡、移除或新增的判準

### 保留

- 問題與其他視角不同，point-in-time 資料完整，使用者能正確說明其方向與限制。
- 即使與另一視角相關，只要有穩定的獨有 top cohort 或不同的決策任務，仍可保留。

### 精簡或合併顯示

- 同一問題、長期高度重疊、幾乎沒有獨有候選，且使用者無法說出兩者差別。
- Pareto 長期保留多數股票時，降為進階診斷或顯示 dominance count；不與 consensus 用 OR
  合成「推薦名單」。
- component 長期造成大量 exact tie 時，先改善尺度或改成 gate；不可用任意 tie-break
  製造假精確。

### 移除 factor／component

同時滿足才排入移除候選：

1. point-in-time／coverage 無法可靠維持，或操作定義與視角問題不一致；
2. 結構上沒有獨有資訊，且使用者看不懂它帶來的差異；
3. 若它進入 production challenger，OOS 邊際貢獻依預登錄規則反向成立或無訊號；
4. 一次只移 1 個 component，建立新 spec；若連動 production 權重／tier，同步重設
   `IS_CUTOFF`。

### 新增維度

預設先不加。候選優先順序如下：

1. **估值／預期差**：現行 D 有成長與獲利、沒有估值；只有取得可靠 point-in-time 股數、
   盈餘與預期資料後才另立視角，不用今日資料回填歷史。
2. **全球供應鏈曝險**：可由正式質化證據建立，但必須有 claim first-seen、覆蓋與 reviewer
   契約；資料成熟前留在研究中心，不進每日分數。
3. **可交易性**：流動性、處置／注意與交易狀態更適合作 gate／badge，不宜包成「公司好壞」。

任何新維度先寫一句固定問題、資料可得時間、最低 coverage、預期 cadence、tie policy、
失敗／放棄條件，再決定是否實作；「資料拿得到」不是新增理由。

## 5. UX 決策方向

### 共通必改原則

- **強制族群脈絡。** 預設不提供 121 檔跨族群總排行，因每個百分位只在自己的族群內有意義。
- **問題先於代號。** 卡片先寫「誰正在領先？」「誰較防守？」「誰有籌碼支持？」
  「誰的基本面較強？」；A/B/C/D 作次要標記。
- **B 改稱防守韌性。** 明示高分 = 較防守；避免「B 風險」被理解成風險較高。
- **摘要與診斷分層。** 預設只顯示 Champion、四視角位置、共識與主要分歧；tie、peer
  sensitivity、component、Pareto 放進「為什麼／進階診斷」。
- **點卡即切排序。** 問題摘要卡必須是控制，不應要求使用者再到另一個 select 找同一選項。
- **導覽不遮內容。** Quick nav 選擇後關閉；drawer 需有 focus trap、背景 inert 與關閉後還原焦點。

### 已採用方向：漸進揭露雙欄探索

- **先固定族群，再直接選問題。** 上方只保留一個族群脈絡；正式綜合與 A–D 都是可操作頁籤，
  點選後立即重排同一批成分股，不再以第二個排序選單重複問一次。
- **左選股、右解釋。** 桌機以 master-detail 同時呈現族群內排名與單檔五視角位置；手機保持
  同一閱讀順序，先看精簡排行，再往下讀所選個股的差異說明。
- **摘要先行，診斷按需展開。** 預設顯示百分位、主要分歧、資料期間與更新頻率；tie、
  leave-one-peer-out sensitivity、共識、Pareto 與角色同儕收進「名次為何可能變動」。
- **不展示沒有行為的控制。** 例如收藏圖示只有在真正具備保存契約後才加入，避免看似可按、
  實際沒有結果。窄幅頁籤會自動把目前視角捲入可見範圍，quick nav 與 drawer 完整管理焦點。

這個方向已依選定參考稿完成 production UI 與桌機／手機 Browser 驗收；只改資訊架構、文案、
排序互動與無障礙行為，snapshot payload、ranking evaluator、Champion、C1/C2 與 OOS 時鐘不變。

## 6. 固定使用者任務與成功條件

每次選稿與實作後，用同一組任務比較，不以「好不好看」代替：

1. 在指定族群找出 Champion 前兩名，且知道這不是全市場排名。
2. 找出「較防守」前兩名，正確理解 B 高分方向。
3. 比較兩檔股票為何 A 與 D 結果不同。
4. 找到 tie／peer sensitivity，能說明名次不穩的原因。
5. 說出共識與 Pareto 都不是第五個分數或買進建議。

先以少量 moderated sessions 找主導性誤讀，再用事件量測確認；少量 usability session 只用來
發現問題，不宣稱母體成功率。若未來加入匿名 telemetry，必須先定義事件、保留期與隱私邊界，
不能把股票查詢內容或個人偏好默默送出。

## 7. 哪些變動會重啟時鐘

| 變動 | 現行 ranking spec | `IS_CUTOFF` | 備註 |
|---|---|---|---|
| 文案、標籤、順序、預設族群、收合層級、無障礙修正 | 不重啟 | 不變 | 前提是 snapshot payload／evaluator 不變 |
| component、權重、最低 component 數、cap、normalization、tie 或 Pareto 定義 | **新 spec** | production 未動則不變 | 舊新快照不可串接 |
| C1/C2 evaluator／成功門檻 | **新 spec／新預登錄** | production 未動則不變 | 不能沿用既有 OOS |
| Champion 權重或 tier 條件 | 新 ranking spec | **改成當天** | 每次最多 1–2 個旋鈕，另走淨成本 gate |
| universe／group／role 定義 | 依受影響輸出分版 | production 受影響時重設 | 報告須標出成員 regime，不混成一條 |

## 8. 例行命令

```powershell
# 每日／臨時 exact-census 健康檢查（唯讀）
python scripts/audit_ranking_views.py --compact

# 正式 final pipeline 的硬門檻；當日 append-only 快照缺失即失敗
python scripts/audit_ranking_views.py --compact --require-current-snapshot

# 週度 OOS 結果與 challenger gate
python scripts/validate.py
```

`audit_ranking_views.py` 不估計績效、不選勝負；`validate.py` 不替 UX 可靠性背書。兩者分工是
刻意的，避免用一個看似完整的總分掩蓋不同種類的失敗。
