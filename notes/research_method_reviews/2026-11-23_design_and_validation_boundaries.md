# 11月23日研究循環 設計文件與驗收結果的界線

## 接續與到期母體

原工作目錄先pull取得遠端；使用者分支沒有上游，未擅改設定或合併，未追蹤內容亦保留。
既有隔離目錄快轉至main `3111184755c9947ad78263670fe9859d945c3a55`後建立本輪分支。
該SHA的tests、qualitative-quality及Pages均成功，latest build也為同SHA，沒有待補發布或重複文章。

先跑queue、radar及method audit，凍結23項到期monitor。topic與monitor組合排序後以換行連接，
SHA256為`5f2c954a8a61afb3ca1ad9cd2cff24890c5408bdaa97529c25a6dc5ba5bf6e68`。
全部按原AND／OR條件做有界回查；檢查入口與取得限制逐項追加到帳本，未把工作日期當證據日期。
11/2已做本月完整回溯，本輪為增量檢驗，不重寫月初快照。

## 新材料應該改變哪一層結論

- **液冷設計與交付分開。** [Daikin D60-W公告](https://www.daikin.com/press/2026/20261111)的60MW是整套設計的IT負載，高溫迴路接CDU、低溫迴路接RCU；同稿明示CDU與乾式冷卻器仍在開發，目標2027H2可供應。Global頁11/11與內文11/10 dateline分列，不把它當NTT DATA的PoC成果或台灣供應商訂單。
- **測試範例與測試結果分開。** [Dynamo v1.6.0](https://docs.nvidia.com/dynamo/v1.6.0/reference/releases/v1-6-0)收錄KVCR復原範例；[原PR](https://github.com/ai-dynamo/dynamo/pull/14695)明說跨主機RDMA需執行期驗證。自動摘要提到live-cluster testing，不能因此宣稱已取得實際通過紀錄。新來源是固定版本與範圍，不是正式operator原始故障包。
- **相鄰展示不能互借驗證。** [SK hynix 11/20 SC26回顧](https://news.skhynix.com/en/sc26-ai-hpc-exhibition/)把CXL卸載驗證、共享KV/token展示及Custom HBM Array模型分成不同段落。公司驗證自述不是Array具名客戶資格，也不是同一任務三層資料、成本與復原的完整對帳。
- **未對齊配置，不強判反證。** [AMD／Arista白皮書官方入口](https://docs.amd.com/v/u/en-US/Powering_Next-Gen_AI_Clusters_High-Performance_Networking_with_AMD_and_Arista_WP-73780)列11/10、v1.0；第8頁描述AMD實驗室網路驗證及尚未production。不能直接拿它推翻既有首批出貨／工作負載陳述，還缺相同配置、資訊截點及production定義的調節。

上述材料回到四篇既有文章及既有圖譜關係，未新增重複題目或台股財務受惠線；原到期條件沒有因旁支材料而放寬。保留新手導讀、精確claim與下一份文件，主命題時鐘不刷新。

## 本輪排除的誤判與候選

[SAFE 11/10提交](https://github.com/opencomputeproject/OCP-Security-SAFE/commit/4745fe3ff8efc21a42d5b5deea10e0450aa7d30b)標題為Recommend Mantis；完整diff只在`Documentation/ai_scanning.md`把建議掃描harness由Arm Metis換成Google Mantis。它不是provider名單變更，不符合信任根T2的新增稽核機構分支。這是本輪暫定線索的排除，不是已發布claim的反證或歷史更正。

HBFSim候選按期重讀release、公開main與固定版本重建說明，仍是v0.1.2／10/23提交；兩份原件SHA與11/9一致。完整乾淨環境GPU重建與跨機重現仍未有新收據，大型原始log未公開。維持順位2、watch及第一拒絕，不報效能倍率；12/7按兩週工作回查。SSCB12/5與玻璃11/24未到期，本輪不重作裁決或改順位。

OCP HBF正式Storage索引仍連到v0.7.0封面；Sandisk入口空殼與SK舊路徑404另列，不能據此宣稱整個產業沒有新合規結果。FCSA既有1.1正式版不重複計新支持。NTT DATA、TDK、NIST與224G的額外附件只按實際讀取範圍留補件，未完成頁面核對或完整取得者不升為新數字主張。沒有登入、申請或繞過受限資料。

## 公告掃描與方法限制

全121檔請求窗口11/21–11/23；上市批次只觀測11/22、上櫃只觀測11/21，各源2列／3列，但universe命中0列0公司。上市缺11/21與11/23，上櫃缺11/22與11/23，兩市場不得互補。這是partial，不能解讀為三天零公告，更不能追認滾過的缺日。

Q3損益與資產負債索引121配對只是文件線索；本輪未新查逐檔MOPS附件，不稱121份財報已驗。後續先補11/24玻璃候選，再按11/25全域工作日處理其他到期文件；缺件重試與公司承諾日期分開。

42篇主命題原先皆逾期，例行工作完成不能解除降級；圖邊亦只依其實際引用資料保留範圍。review筆數、候選數、文章數是帳本盤點，不是獨立經濟觀測或支持率。新來源即使由兩位讀者核對，也不會因此變成兩條獨立消息鏈。

## 增量帳本與獨立複核

本輪追加23筆`not_yet_testable`，沒有新增支持或反證事件；累計1312筆回查為113支持、4反證、189查無新證據、1006仍不可完整測試。這是事件計數，不報支持率。新增6個主張、6筆來源紀錄及2個monitor後，現有1007個active claim、186個active monitor；當日到期待查0項，不代表論點全部獲證實。42篇主命題仍逾期，869條圖邊逾期；Daikin整合邊的新設計證據可更新該邊，不能解除整篇主命題降級。

獨立讀者就四篇及四張圖譜的新增差異重新核對原件：四份已保存HTML／PDF的SHA吻合，AMD同一PDF重新渲染與目視第7–9頁，沒有重下載PDF。PR與AMD metadata另讀官方HTML，不假稱有離線原件SHA。沒有發現必修內容錯誤；受審範圍限本次增量，不是所有歷史主張再驗，也不是正式公司筆記簽核。四篇主命題、meta及所有既有monitor逐字比對基線不變。

## 發布檢查的問題與修正

Windows 11／python.org Python3.12.10的首次預設編碼與`PYTHONUTF8=1`兩輪完整測試，各執行1130項，皆有1 failure與3 errors、9 skips。失敗位於與本輪基線相同的測試：兩個財報查核連線只退出交易卻未關閉，另一個同程序模擬CLI中斷保留連線，造成暫存目錄刪除被Windows阻擋；實驗封存核對則因`core.autocrlf=true`將三份原收據checkout為CRLF而失敗。

修正限於測試連線生命週期，以及兩個實驗封存目錄的LF屬性。原收據先驗明除CRLF外與Git原件相同，且Git原件SHA等於manifest，才恢復既有LF位元組；沒有改manifest、歷史紀錄內容或正式抓取程式。相關三組定向測試12、73、4項各自通過；未略過失敗測試或放寬雜湊判斷。正式DB與歷史頁面在失敗檢查中仍未改動。

修正後同環境的預設模式與`PYTHONUTF8=1`各執行1130項完整測試，均`OK (skipped=9)`；略過為Windows帳號沒有符號連結權限的案例及子案例，保留Linux CI驗證，不說全平台無略過。六項研究lint與append-only基線核對、隔離dashboard重建皆exit0。topic lint保留42篇過期降級及2項既有術語警示，不藉發布消除。

首頁RECENT與研究頁LIB均含本輪四篇11/23修訂，總數282篇，方法快照為RMA-2026-11-23-01、回查1312筆。另按Git物件雜湊核對318個受保護檔案（含正式DB、92份archive、正式質化筆記、入口規範等）未改，42篇主命題時計未改，AGENTS與CLAUDE位元組相同。本輪未作瀏覽器互動或全頁視覺驗收；檢驗範圍是內容payload、建置與測試。推送後仍須確認同一SHA的tests、qualitative-quality、Pages及兩份公開HTML位元組，不能把本地通過寫成已部署。
