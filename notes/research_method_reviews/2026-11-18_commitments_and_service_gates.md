# 11月18日晚間研究循環：承諾、測試程序與服務可取得性

## 接續、母體與日期

先在使用者工作樹pull取得遠端；原分支沒有上游，不擅自設定或合併，保留未追蹤內容。
隔離工作樹以`bde076f4baf6d41703895be19b62a6e422f8f9d6`為基準，分支為
`codex/research-cycle-20261118`。確認上一輪研究`d25a557c6178bd7fdb84f9b232a4f02bafbf4fdf`
的tests、quality與Pages成功，最新每日部署已到bde076，沒有未完成發布需要重做。

queue、radar及method audit先行凍結11項有效到期工作。所有檢查在台灣11/18執行；
排序後topic#monitor集合SHA256為`9a701e986cb2a24600fa9377a9c2bf3e5541b7e048580768a535e03447c56f34`。
11項結果為10待驗、1限定正式簽核登錄無新增；另提前回查Rubin T3，僅命中具名服務開放分支，
不混入到期母體。這些是工作盤點數，不是獨立實驗，不能報支持率。11/2已做完整月度回溯，
本輪只新增第二份11/18方法快照，不覆寫凌晨快照或任何舊帳本。

## 三篇既有文章更新，不提高整篇可信度

| 問題 | 新接受的內容 | 仍缺什麼 |
| --- | --- | --- |
| AI CapEx／現金回收 | [NVIDIA 11/17 8-K附件](https://d18rn0p25nwr6d.cloudfront.net/CIK-0001045810/46a9c98c-87ae-40f5-acac-7d9264b18eb4.pdf)第19至20頁：未來承諾、額外附條件承諾、保證最高毛額及明示未付款狀態 | 逐租約可重算、實際可服務／觸發／回收／付款及OpenAI補償共同鍵；原T5仍待驗 |
| AMD Helios | [Microsoft工程說明](https://techcommunity.microsoft.com/blog/AzureHighPerformanceComputingBlog/from-silicon-to-service-bringing-amd-helios%E2%84%A2-to-azure/4573029)的固定配置、整群負載、修復重驗；[11/17修訂活動文](https://techcommunity.microsoft.com/blog/azureinfrastructureblog/visit-azure-and-amd-at-microsoft-ignite-and-sc26/4570345)分開三個產品狀態 | 同配置場站結果、ND MI455X v7開放區域及客戶驗收；MI300X GA不能移植 |
| Rubin雲端可取得性 | [Oracle 10/27](https://www.oracle.com/news/announcement/ai-world-nvidia-and-oracle-expand-nvidia-vera-rubin-to-multi-gigawatt-scale-2026-10-27/)具名GA；[Google更新](https://cloud.google.com/blog/topics/ai-infrastructure/google-cloud-infrastructure-at-nvidia-gtc-berlin-2026)及[產品文件](https://docs.cloud.google.com/compute/docs/gpus/)的GA日期、機型、預留方式 | 指定區域帳戶配額、交付、客戶驗收、利用與台灣供應商財務；NVL8及多GW擴張仍是計畫 |

新增10個claim、6個source及CAPEX T7一個monitor；三份圖譜僅更新有來源支撐的邊，另增Oracle
具名服務關係，不新增台廠受惠關係。全42篇原主命題時鐘與舊來源保留。新手段落解釋不同錢的定義、
程序與結果之別、GA與實際取得之別，並留下讀者下一步提問。

## 同包重算與方法修正

NVIDIA IR原件293590bytes，SHA256為
`b159699ab63e9b0ca79fbe5cff51716e46709a99850a1d56572a5e546ddb0572`。
主撰及另一讀者對同一份原件核第2、19、20頁；只渲染引用頁及前後各一頁。另一讀者不重下載，
離線重算SHA、整數與Decimal加總：五列390／28／74／20／6，六欄82／222／103／22／16／73，
總額518；另表32；保證3.5＋105.0＋9.5＝118.0。表內破折號只在重算已顯示加總時作零，
不把缺少披露補成零。這是確定性算術，不報SE／t，也不是正式個股全篇簽核。

表格基準日10/25、未來財年與11/17「迄今未付款」陳述時點分開。518不是當期CapEx，32另有條件，
118不是預期損失且已含105；當期未起租74與前季雲端加租約合計74同數不同義。第2頁明示附件
furnished而非Section18意義下filed；不把8-K附件說成新10-Q或經查核報表。
方法新增上述範圍防重算與原事件門檻規則：明示未付款雖是新旁支，不能降格原付款／補償門檻；
Rubin原T3只需任一來源推進一關，具名GA可命中，不反向增設全區域庫存要求。

交叉閱讀另抓出Google新列來源的原稿日期差異；以同包可見頁首日期為準，分開原稿、11/6更新與
11/18取得日期，不把抓取時間當事件時間。Google兩頁同一消息鏈，Oracle與NVIDIA聯合稿只算一條。
本輪Google閱讀服務曾回錯誤頁，但已保存原HTML及正文；不能將某一路徑失敗描述成所有管道失敗。

## 未成熟項目與下一證據

公司四項：3035／3131／3711／3260已有Q2正式簽核，不能重列未完成；6271與3675仍需完整focused
同包及獨立重算。6271經MOPS恢復取得既有7/30 Q2檔，不是11/18新上傳；國巨Q3局部現金橋不代替
舊Q2正式全篇簽核。環球晶Q3仍缺火災／調配／爬坡至產能交付價格橋，不重複新增旁支。
KLA新季數字不代替原FY26Q4同口徑拆解，原附件兩條官方路徑均受限。液冷平台僅取得外殼或逾時，
不是型號刪除或狀態未變。其餘每週項11/25工作重試；Helios11/20先補會後同產品文件，非廠商承諾日。

三雷達候選未到期，不改順位、知識價值與第一拒絕：SSCB11/21、HBFSim11/23、玻璃11/24。
[NVIDIA供應鏈11/17公告](https://nvidianews.nvidia.com/news/nvidia-expands-commitments-with-supply-chain-partners-to-support-ai-infrastructure-buildout)
只留下新選題線索，11/20先凍結選題及失效條件，再作供應商雙向調節；不由預付款／專供產能直接
改成台灣公司收入。矽品先進封裝與光引擎、景碩ABF與SPHBM4／Helios不是相同產品範圍。

121檔11/17–18公告窗口，兩市場只覆蓋11/17，13列6家公司；標題及說明已讀，未宣稱全附件驗收。
6213更正的是iXBRL約當股數，不憑公告推PDF已替換或EPS修正；5234所列雙位數是媒體內容，
不當正式公司預測；3711投資人活動明示沿用10/29簡報，不重計新資料。設備批次不是機台數，
工程契約不是付現或NVIDIA訂單，8299已公告未來股利日不等已付款。缺少11/18仍標partial，11/20補查。

## 發布驗證

以共同發布閘門核append-only、完整測試、研究lint與隔離build，另驗首頁三篇修訂及研究中心新快照。
DB、archive、正式筆記、AGENTS／CLAUDE與原主時計均列保護；未完成公開同SHA位元組核對前不宣稱發布成功。
實際檢驗結果於下方追加，原始收據留tmp；沒有瀏覽器視覺驗收或新的投資績效宣稱。

Windows11 10.0.26200／python.org Python3.12.10，預設編碼（PYTHONUTF8未設、utf8_mode=0）與
獨立UTF-8程序（PYTHONUTF8=1、utf8_mode=1）各跑994項完整測試，993通過、1略過；六項lint及隔離
build通過。收據為`tmp/prepublish/20261118-evening-default-2/verification.json`及
`tmp/prepublish/20261118-evening-utf8-1/verification.json`。

本輪新增8項回歸。初驗發現新增CAPEX縮寫欠解釋，已加SHA／RFS白話定義；另有11/4歷史fixture讀入
11/18新區塊而誤判未來證據，修正為先按fixture日期切出當時來源、主張與transition，保留原排程及
時鐘斷言。新測試一處圖邊識別碼筆誤亦已修正。失敗紀錄留存，沒有刪除原內容契約或回寫舊快照。

新快照RMA-2026-11-18-02列989個active claim、853個來源、183個active monitor、1285筆review；
本輪工作日期已接續，但42主命題、870條圖邊仍過期，不將追蹤到期歸零誤說成研究已證實。
首頁三篇修訂日皆11/18、研究總數282不變；315個受保護檔案含DB、89份archive、正式筆記及入口規範
逐一對基準相同，42篇主時計不動，AGENTS與CLAUDE逐位元一致。

推送後另核tests、qualitative-quality、Pages同一SHA成功及latest build／deployment，公開首頁和研究頁
逐位元比對commit。最終發布收據預定為`tmp/publication_20261118_evening.json`；須該收據成功後才報完成。
