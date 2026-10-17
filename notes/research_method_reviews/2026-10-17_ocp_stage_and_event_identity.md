# 2026-10-17 研究循環：初始運行、展示與驗收分層

## 本輪結果

起始pull至`41a19f4bc9a08c009568dd9b990560c2a6a9b7eb`，前次研究與最新main的CI／Pages
已完成且SHA一致，沒有待續的研究發布。保留未追蹤`.superdesign/`、既有stash、正式DB與
歷史archive。10/4已完成十月完整方法回溯，本輪只追加增量快照。

凍結77個到期monitor後，69項留下實際讀取或取件嘗試：1項限定來源的`no_new_evidence`、
68項`not_yet_testable`。這是工作紀錄，不是69次獨立驗收；共享來源不能重複當獨立支持。
8項未查保留原逾期，不產review或延後工作日。所有topic主命題時計與原可信度基準保留。

## 三篇更新與新手學習重點

- **Helios初始運行：** [AMD 10/12原稿](https://newsroom.amd.com/news/ocp-2026-amd-ceo-lisa-su-keynote-takeaways/)
  自述四家初始系統已安裝運行，交付／部署／工作負載驗證進行中。這比未來計畫前進，
  但一份公告點名四家公司仍只有一條消息鏈；不是四份客戶驗收、GA或容量分母。
  緯穎展稿另支持整合角色，不能把AMD客戶名單接成緯穎供貨。新增C29/C30與T14，圖譜
  保留公司自述及驗證邊界，並把舊正文只有未來規劃的說法更新。
- **CPO系統展示：** [緯穎、Ayar與GUC 10/13原稿](https://www.wiwynn.com/news/wiwynn-ayar-labs-and-guc-advance-co-packaged-optics-with-live-demonstration-of-integrated-optical-compute-system-at-ocp-global-summit-2026)
  給出多晶片封裝、光引擎、外部光源及運算系統的具名組合。新增C25與T6，圖譜限
  integration；可拆光纖、遙測及現場連線不等長期可靠度或無中斷更換。訊號處理模式
  仍未補齊，不把完整三軸trigger當通過。
- **液冷規格可比性：** [台達10/8](https://www.delta-americas.com/en-US/news/40271)與
  [10/15](https://www.delta-americas.com/en-US/news/40272)分別列Project Deschutes與不同
  800VDC CDU。新增C40–C42、三列比較與公司產品能力線。3°C條件只屬Deschutes，
  2027Q1量產仍是計畫；3.6MW與2.5MW沒有共同料號／版本，不能叫同款降規。
  新手先辨設備、條件和單位，再問平台資格、客戶驗收及交付財務。

這些新增不是投資推薦，沒有新增營收受惠、排他或財務材料性結論。原文章均保留主張帳本、
證實／推論／待驗證、追蹤與失效條件；首頁與研究中心以transition同步近期修訂。

## 到期工作的已查與未查

| 來源組 | 本輪可確認的範圍 | 未完成與下一證據 |
|---|---|---|
| 20項政策／財報／製程／材料 | 公告逐列、MOPS索引、ASML Q3全文、NVIDIA 10-Q指定條款及官方技術頁 | 附件、同產品版本、客戶資格與財務共同鍵；10/21 |
| 18項運算／光學／互連 | AMD與緯穎正文、HBF展品、規格索引及部分技術文件 | 展品不代HBF樣品、CPU proof不代GPU測試；10/19–23 |
| 17項電力／功率／電容 | 供應商產品／架構、OCP規範文字與實際失敗取件 | Mt.Diablo／DCF原PDF及目視、同事件波形與買方驗收；10/19–21 |
| 14項液冷／動作／信任 | Delta正文、BMS指南、OCP會議PDF有限頁、SPDM索引 | Marketplace列項、PG25本體、同場域實測及正式版本差異；10/19–21 |

尚未查的8項：tester T4、process-control T10、EMC T2、SDC T3、800V保護T2、
電容T2/T4、buffering T2。它們的原工作日仍是10/15或10/16，沒有被本輪69項回查代填。
10/14留下的預付款、局部復工與光寶工程契約線索，也未完成雙端附件核對。

ASML10/14 Q3新聞的擴產腳註是low-NA EUV與DUV immersion，不能讀成High-NA擴散。
NVIDIA PORTS-Pike仍須逐租約ready-for-service、起租、觸發及支付資料；本輪新定位
SB Energy S-1/A2但未全文核，留10/21而非宣稱沒有新資料。原7篇source_internal衝突不清除。

## PDF與日期邊界

主代理以相同本地原件重算SHA，並親看PG25 panel p4、SAFE p5/8/9、OpenRMC p7。
原件均來自[OCP官方峰會錄影索引](https://www.opencompute.org/events/ocp-summit/2026-ocp-global-summit/recorded-content/)
的簡報連結，不是重新下載另一版來覆核。其餘技術頁未做數字驗收。

| 原件 | SHA256 | 本輪接受的範圍 |
|---|---|---|
| PG25 panel | e82734b41711f44b310f74666b1c0bac4ce5c78e5818d982ede2788ce9a7ef6c | p4稱Base PG25／水基8月發布、Guidelines9月更新／發布，精確日期未知 |
| SAFE AI age | 4817cac503c8d21aed3a491dcaaa755dd0566cf4f83bb129f6f887da1eb4ed45 | 制度要求與獨立point-in-time評估，不等新產品認證 |
| OpenRMC GraphQL | 570ee19941fa48bee978455b81d7ac36a53694e8f49ad9928cea4dbccb1e446f | p7是telemetry proxy提案，不等兩家action conformance |

PG25 panel不能替仍403的Guidelines本體核對新門檻；現行document契約要求精確發布日，
本輪不虛填峰會日或冒充living index，故不新增正式S36，T7仍待驗。Mt.Diablo v1.0.0
只有網頁文字、原件403且截圖未交付可檢視像素，沒有本地pack，不發布新技術數字。
這些限制按不同文件分開，不能把一份PDF成功說成所有附件已取得。

## 事件掃描與方法改善

TWSE／TPEx10/17出表只觀測10/16發言。10/14–17窗口兩市場都缺10/14、15、17，
18列命中13家公司仍是partial。115Q2損益、資產負債及交集各121只代表索引存在。
公告13家公司直接MOPS索引成功；另3035、6271、3675、3260、3131成功，2327、2337、
6488、8261、2308解析失敗。未核這批PDF，不把索引成功當財報已審或失敗當無檔。

新方法規範保留全部原始列，另核「經濟事件鍵」：公司／子公司、相對人、標的、幣別與
事實期間。8358的Co-Tech改CoTech是同一筆投資的名稱更正，不再加一次14億元；
6213四層集團內股利不能相加成合併新增現金。6531公告引用8月自結、1815是9月自結，
3211則分Q3及前九月，均不得由公告日期換成同期間，或推成特定AI／BBU收入。
這是保留原證據後的人工判讀，不用標題相似度自動刪掉更正稿。

10/17財報排程38994366909成功且latest-month完整檢查無缺口；主代理另用db_ro對121檔
universe重查2026年9月非空營收，121/121齊備，原9檔皆存在。這只確認資料覆蓋，
未逐檔核數值、期間變更或產品財務，沒有解除質化來源衝突。

SSCB與HBFSim維持原凍結順位1/2與watch，10/21補同型號測試與配對原始run；玻璃本輪
未重查，維持順位3與10/19。Aries7仍僅供應商介紹，10/23補測試／資格，不強制升格。

## 方法快照與驗證收據

新增`2026-10-17_01.json`，UTF-8／LF直接寫入，不改舊快照。當下42個active topic、
894個active claim、788份active source、159個monitor、40張圖譜共888條active edge；
623列review為99新支持、4反方、172限定查無新證據、348待驗。這是登錄項目計數，
不是獨立樣本或正確率；不報支持率。40篇topic與819條edge仍過期，8項monitor逾期。
183次scan中2次full、181次partial；本輪partial不因公告列數增加而升格。

Windows 11／python.org Python 3.12.10：預設`utf8_mode=0`、`PYTHONUTF8`未設，
以及`PYTHONUTF8=1`兩環境各執行883項完整測試，882通過、1略過。研究lint、正式筆記、
H#、圖譜、雷達、方法／topic歷史保護及隔離build一致性均通過；研究lint仍有42則提醒
（40篇過期、2項既有術語），不是零警告。最終收據保存在本地
`tmp/prepublish/20261017-default-release/`及`tmp/prepublish/20261017-utf8-release/`。

初次完整檢查抓到5項舊內容預期：固定篇內數量、舊部署用詞及舊雷達工作日。
修正可追加資料的數量上限假設，但保留指定歷史ID、主時計、固定選擇與append-only保護；
新增9項本輪回歸涵蓋單一消息鏈、不同產品不可比、公司／圖譜分層、69項回查與8項未查、
快照及首頁同步。另修Helios交付表殘留未來式、學習問題與舊「下一個」工作日描述；
CPO補緯穎公司及serverodm篩選入口，方向仍uncertain，不新增財務結論。

重建資料日為10/16，研究中心282篇（含正式筆記／小作文／市場議題）；三篇市場議題
均以10/17修訂出現在首頁與研究中心。本輪不寫正式DB；相對起始基準及兩環境隔離檢查，
DB與70份archive共71檔未變。`.superdesign/`、既有stash與AGENTS／CLAUDE保持不動。
Git發布結果以本次提交及對應CI／Pages同SHA驗收為準，不以本地build成功代替上線。
