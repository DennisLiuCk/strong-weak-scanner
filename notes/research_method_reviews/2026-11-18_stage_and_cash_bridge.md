# 11月17日研究循環、18日完成：證據前進一關，不代表整篇命題完成

## 接續與時間邊界

原使用者工作樹在無上游的`codex/framework-methodology-20261107`，先pull取得遠端後保留原分支與未追蹤檔。
在既有隔離工作樹建立本輪分支，開始基準`48aa77e82e4051f7a2a3ff65cce15d0d75e33f50`；確認11/11研究
`43d090eb05d9d527667ac9d6173d01449cb845a2`的tests、quality、Pages成功及後續每日部署，沒有重發舊文章。
11/17每日終版執行期間，安全暫存本輪已知變更、fast-forward至`735923a1b6822054f9faad1746c7564511314d79`
再還原研究，未覆寫DB或當日archive。發布驗證以後者為受保護檔基準。

先執行queue、radar與method audit，凍結11/17到期85項。11/17實查84項：4項窄義新支持、79待驗、
1項僅限定USTR具名清單無新文件；SPHBM4台灣端T2另於跨午夜後補查，依實際日期追加，不倒填11/17。
11/18新到期者不混入事前凍結母體。檢查是有界文件工作，不是全市場普查或獨立實驗，不報支持率。
十一月完整方法回溯已於11/2完成，本次追加增量快照；舊快照與42篇主命題時鐘不改。

補查完成後，凍結85項為80待驗、4窄分支新支持及1有界無新文件；累積1273筆review、182項active monitor。
快照按實際11/18產生，保留午夜新到期11項（0逾期）、42 stale topic及875 stale edge，不報「到期清零」。
SPHBM4來源包括Faraday同包、創意HBM IP、南電Q3指定頁、PTI同包及SK hynix正文；HBM4／FCBGA不等SPHBM4，
仍缺雙向產品鍵，欣興／創意Q3及Micron原件11/25補件，並明列其他issuer未覆蓋。

## 六篇既有文章的增量

| 問題 | 本輪可接受的新證據 | 仍不能推論 |
| --- | --- | --- |
| Rubin供應 | [CoreWeave 11/16](https://wf.coreweave.com/news/coreweave-becomes-first-cloud-provider-to-deliver-multi-rack-nvidia-vera-rubin-results-in-mlperf-r-training-v6-1)的Available類別／正式叢集與[NVIDIA正文](https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/)一般供應陳述 | 逐地區庫存、全部客戶驗收、未核驗rerun效能或台灣ODM損益 |
| 國巨現金橋 | [Q3完整財報](https://doc.twse.com.tw/server-java/t57sb01?step=9&kind=A&co_id=2327&filename=202603_2327_AI1.pdf)的累計減H1可重算單季FCF及現金變動 | 管理現金永久定義、640百萬元舊比較差異已解，或產品漲價毛利橋已完成 |
| 液冷 | [台達公司稿p7](https://filecenter.deltaww.com/IR/download/calendar/3Q26_Transcript.pdf)的產品族收入約數；[光寶Q3 FAQ](https://www.liteon.com/en/download/investor-conference)的120kW CDU開始出貨 | 單一CDU損益、出貨等驗收、120kW等380kW型號、預期放量等實績 |
| UCIe 4.0 | [11/12規格公告p1–2](https://www.uciexpress.org/_files/ugd/0c1418_970201e6ba294a0fa690ae864082fc46.pdf)的記憶體連線及管理功能 | 64G跨廠silicon互通、客戶整合驗收或台灣收入 |
| AI儲存 | [群聯Q3 p5](https://www.phison.com/wp-content/uploads/2026/11/3Q26_Phison-Earnings-Call_EN_Official_uploaded-version.pdf)廣義AI應用分類圖表57% | Pascari、純企業級SSD或三種I/O工作的獨立收入；摘要57%+不改成更精確數值 |
| 鎵許可 | [AXT Q3 pp44–45](https://www.sec.gov/Archives/edgar/data/1051627/000143774926036542/axti20261101_10q.htm)對InP／GaAs及歐洲收入的公司解釋 | 兩張邊際表可拼交叉金額、美國全部放行、客戶收貨已核驗或台廠財務 |

新增14個claim、8個source及3個monitor，六篇均保留新手解釋、問題與後續條件。五份圖譜更新，
新增UCIe4規格節點、規格關係及光寶出貨關係；舊產品族和新季度觀察分開，國巨公司現金不硬接AI產品線。
沒有新增重複文章，亦未把供應鏈鄰接升為財務受惠或股票排名。

主代理目視同包UCIe p1–2、群聯p5與台達p7，核對光寶FAQ的出貨／預期／設計原句，並對讀兩份Rubin正文，
不採AI摘要或效能倍率。另一代理獨立重算國巨四份同包原件SHA、p5／8–10及兩版簡報：Q3營業現金
11,412,532減現金PPE 2,176,610得FCF 9,235,922千元，圓整9,236百萬元；四條現金流合計
-65,171,939千元，精確接期初／期末現金。三項流動資產合計減少75,670,596千元，但存量差不是交易現金流。
這是確定性算術，無抽樣SE或t；不是正式個股筆記重新簽核，也不是全附註審計。

國巨Q3原件SHA256為`3544cf33d6789fb6d6a6e979db700573c54494075fc6bdcc473116f017c62f99`；
H1為`cf0bc1a51edb3fc3fc0160310c7c903b36e3766ce80fb3eaa8d949bc0c4d9561`；
UCIe4為`f07d39232b3e37e5f73cd3fc4fe392b71789890e36cd85856c1058cb12afd6ba`。
完整原件及覆核收據在忽略的tmp，不進版控。AXT原HTML取件403，只有官方URL閱讀服務文字可查，
沒有原件SHA或圖表圖像，因此只接納可定位的質化解釋，不報交叉數字。另由非撰稿代理對讀同一官方段落，
兩次閱讀仍是一條AXT消息鏈，不偽稱獨立來源或完整離線證據包。

## 原觸發語意與方法修正

Rubin T3原為「任一來源」推進一關；國巨T6是管理定義**或**下一季同公式重算；AXT T1／T2要求
產品／目的地／進展及分產品收入解釋，沒有事前要求完整定量矩陣。四筆new_support只對這些分支，
不擅自加AND門檻，也不退役monitor。AXT兩筆共用S5，不算兩個獨立成功樣本。反過來，原本需要完整
產品、部署及財務共同鍵的項目，不因旁支新公告而改判；UCIe新版及液冷產品族新數字也不替舊門檻結案。

方法新增三項可重用約束：累計轉單季須列兩端與存量橋；邊際表不是聯合表；按原AND／OR分支判定，
不得事後抬高或降低門檻。未執行、取件失敗、原文已讀但未命中、命中新分支分開。樣本不足及消息鏈重複
時不報支持率；方法改進不是宣稱它已被統計證明更準確。

## 公告、候選與未成熟項目

121檔、11/11–17窗口的官方公告只見兩市場11/16，21列16家公司；各市場缺11/11–15及17，
連週末也不以假定零公告填補。21列標題已讀，定向讀6415、2383、6830澄清／更正正文；矽力媒體成長數
不當公司預測，台光電客戶占比澄清不改成無期間的精確季報占比，汎銓iXBRL更正不當已替換PDF或EPS影響。
其他公告不是全附件驗收。原列、取件時間與SHA留在event scan收據。

Q3 MOPS定向查2327、2428、2472、2478、3035、3443、3661、4770、4755、6239、3264、8261，
12次均found、0missing，含上次2428受限重試；不代表舊69家清單或全121檔完成。只有國巨本輪取得並核
指定頁的完整財報；其他索引成功不等全文讀完。正式個股筆記7項P0衝突保留，不擅自改正式簽核。

三候選維持凍結排序：SSCB 11/21、HBFSim 11/23、玻璃11/24。玻璃官方入口仍缺同產品客戶放行及製造結果，
不由版本／展示重排。11/20總工作先補當輪未完原件及下一到期項；公司端測試、出貨與財務共同鍵是優先，
不是為篇數升格。研究排序僅是查證工作的先後，不是投資建議。

## 發布驗證紀錄

新增10項回歸，覆蓋84筆日期／結果、原時計、單季算式、原OR語意、消息鏈、規格／驗收、產品混用、
跑分核驗、廣義分類與partial覆蓋；85項凍結集合另用排序後識別碼SHA核對，補查的11/18日期不可倒填。
首輪查出新文字頁碼縮寫造成的可讀性債、未產生新快照時的日期不一致，以及舊測試把合法追加數量與
未來修訂匯入歷史fixture。已以中文頁碼消除新增術語、產生新快照，並保留原ID唯一性／歷史內容斷言，
只讓成長型帳本容許新ID、歷史fixture截在當時日期。反思段落測試只讀該節，不吞進後續新增正文；
財務稽核由登錄重算筆數，另確認2025全年與2026Q3兩筆台達觀察分開。失敗收據保留，未刪測試或回改舊快照。

Windows11 10.0.26200／python.org Python3.12.10：預設PYTHONUTF8未設、utf8_mode=0，以及獨立程序
PYTHONUTF8=1、utf8_mode=1，各執行986項完整測試，985通過、1略過。六項lint與隔離dashboard build皆通過，
兩環境收據為`tmp/prepublish/20261118-default-verified/verification.json`與
`tmp/prepublish/20261118-utf8-verified/verification.json`；正式DB及archive未改。

首頁六篇修訂日11/17、282篇研究資料、RMA-2026-11-18-01及1273筆review均已核對。
315個受保護檔案含DB、89份archive、manifest、正式筆記與入口規範逐一對基準735923a相同，42篇主時計不動，
AGENTS與CLAUDE逐位元一致；收據`tmp/payload_20261118.json`。本輪做內容、資料與建置驗證，沒有瀏覽器視覺驗收。

推送後須另核同一SHA的tests、qualitative-quality、Pages成功及latest build／deployment，並逐位元比對公開
index.html與research.html。預定發布收據`tmp/publication_20261118.json`，只有該收據成功才對外報發布完成。
