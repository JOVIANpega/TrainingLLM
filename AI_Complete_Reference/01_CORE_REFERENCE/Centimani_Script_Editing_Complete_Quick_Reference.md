# Centimani 腳本編輯完整速查表
*基於 PPT 分析結果的綜合性參考指南 - 2023年平台培訓版本*

## 🔄 版本資訊與更新

### 📊 版本比較
| 文件類型 | 舊版本 | 新版本 | 更新日期 | 主要變更 |
|----------|--------|--------|----------|----------|
| **PPT教學文件** | v1.4(20180427) | (20210217) | 2021-02-17 | 內容優化，格式改進 |
| **儀器參數** | Ver1.65 (20230104) | **Ver1.71(20230411)** | 2023-04-11 | **新增36個工作表，包含更多儀器支援** |
| **腳本用戶指南** | (202230104) | (202230104) | 2023-01-04 | 5個詳細說明工作表 |
| **iPLAS參數** | - | **v2.0** | 2023-07-18 | **全新iPLAS參數列表，包含Version、Argument List、Example** |

### 🆕 新版本主要改進
1. **儀器參數大幅擴展**: 從舊版本升級到Ver1.71，新增多個儀器支援
2. **iPLAS整合**: 新增完整的iPLAS參數參考，支援v2.0功能
3. **腳本編輯工具**: 新增EditorScriptTool工作表，提供更好的腳本編輯支援
4. **實用工具庫**: 新增UtilityLibrary、InstIQApi等實用功能

### 📋 目錄
1. [系統配置 (System.ini)](#系統配置-systemini)
2. [腳本檔案結構](#腳本檔案結構)
3. [DUTs 設定](#duts-設定)
4. [腳本編輯欄位說明](#腳本編輯欄位說明)
5. [Instrument 設定](#instrument-設定)
6. [Switch 設定](#switch-設定)
7. [Global.ini 使用](#globalini-使用)
8. [日誌系統](#日誌系統)
9. [工具使用](#工具使用)
10. [常見問題與除錯](#常見問題與除錯)
11. [新版本功能](#新版本功能)
12. [iPLAS參數參考](#iplas參數參考)
13. [AI 腳本產生邏輯（基於現有腳本修改）](#ai-腳本產生邏輯基於現有腳本修改)
14. [全域變數系統與 IPLAS 邏輯](#全域變數系統與-iplas-邏輯)
15. [DUT Sheet 邏輯分析（結合 Global.ini）](#dut-sheet-邏輯分析結合-globalini)
16. [文件分析工具（必須保留，避免重複編寫）](#文件分析工具必須保留避免重複編寫)

---

## 🖥️ 系統配置 (System.ini)

### 基本設定
| 參數 | 說明 | 預設值 |
|------|------|--------|
| `LargeWindow` | 程式視窗大小設定 | Default |
| `RetryCount` | 重測次數上限 | - |
| `DeviceSemaphore` | Enable/Disable Device in Semaphore Mode | Default |
| `DebugMode` | Enable/Disable Debug Window | - |
| `IndividualScanBarCode` | Enable/Disable Individual Scan Barcode | Default |
| `NewFormatScriptFile` | New Format Script File Name | 檔案請放置於System資料夾內 |
| `TestItemCodeFile` | Test Item Code File Name | 檔案請放置於System資料夾內 |
| `StationList` | All Stations of Project | - |
| `StationName` | Station Name | - |
| `SendWithout\n` | 不要在Command後端自動加上\n | - |

### SFIS 設定
| 參數 | 說明 | 預設值 |
|------|------|--------|
| `SFIS_Enable` | Enable/Disable Shop floor | - |
| `SFIS_AutoLogin` | Enable/Disable Auto login when shop floor timeout | - |
| `SFIS_WebLink` | Web Link of shop floor server | - |
| `SFIS_TSP` | SFIS TSP | - |
| `SFIS_OPID_LENGTH` | Length of OP ID for checking | - |
| `SFIS_OPID_PATERN` | Pattern of OP ID for checking | - |
| `SFIS_CheckRouteType` | RouteType for SFIS CheckRoute | Default |
| `SFIS_RepairEnable` | Enable/Disable SFIS Repair | Default |
| `SFIS_RepairType` | RepairType for SFIS Repair | Default |
| `SFIS_RepairReason` | RepairReason for SFIS Repair | Default |
| `SFIS_RepairDuty` | RepairDuty for SFIS Repair | Default |
| `SFIS_RepairNGRP` | RepairNGRP for SFIS Repair | Default |
| `SFIS_SkipSaveResultOnFail` | Enable/Disable Not SaveResult when test is fail | - |
| `SFIS_GetDateISN` | ISN for Get Shop floor's Date Time | Default |
| `SFIS_ResultFile` | ResultFile for SFIS SaveResult | - |

### 網路服務設定
| 參數 | 說明 | 預設值 |
|------|------|--------|
| `FTP_Enable` | Enable/Disable FTP | - |
| `FTP_Host` | FTP Server IP Address | - |
| `FTP_ID` | FTP ID for login | Default |
| `FTP_PW` | FTP Password for login | Default |
| `FTP_Folder` | FTP default directory | - |
| `MiniCloud_Enable` | Enable/Disable MiniCloud | - |
| `MiniCloud_Host` | MiniCloud Server IP Address | - |
| `MiniCloud_ProjectName` | Project Name | - |
| `MiniCloud_LogPath` | Log Path for MiniCloud | - |
| `MiniCloud_iPLAS` | Enable/Disable iPLAS | - |
| `MiniCloud_iPLASLogPath` | Log Path for iPLAS | - |

---

## 📁 腳本檔案結構

### 基本組成
腳本檔案應包含以下 Sheet：

1. **Properties Sheet** - 版本、創建者、失敗計數等基本資訊
2. **Instrument Sheet** - Device 使用設定
3. **Switch Sheet** - Switch 使用設定
4. **DUTs Sheet** - DUT 相關設定
5. **各站 Test Script Sheet** - 對應各站的測試腳本

### 檔案位置
- 腳本檔案請放置於 `System` 資料夾內
- 在 `System.ini` 中設定 `NewFormatScriptFile` 參數

---

## 🔧 DUTs 設定

### 欄位說明
| 欄位 | 說明 | 格式/範例 |
|------|------|-----------|
| **Load** | 是否載入此DUT | `true` / `false` |
| **DUT Name** | Project Name / Model Name | 專案或型號名稱 |
| **Station** | Station Name | `Station Name,Skip start test confirm`<br>`1→Skip; 0→Confirm` |
| **Parameter** | 帶入Test Script的參數設定值 | 限於Switch、Send、Reply、Validation與Description欄位使用 |
| **SFIF_DeviceID** | SFIF Device ID | SFIS系統的設備識別碼 |
| **ScanBarcode** | 要刷的條碼規則 | `{Name1,Length1,Pattern1};{Name2,Length2,Pattern2}` |
| **Connection1...** | 與DUT的連線設定 | 連線類型與參數設定 |

### Connection 設定格式
```
"Type","Name","ConnectString"
```

#### 支援的連線類型

**TCP 連線**
```
TCP,ConnectionName,網卡IP,DUT IP,DUT TCP Port,Connection Timeout,Response Timeout
```

**UDP 連線**
```
UDP,ConnectionName,網卡IP,DUT IP,DUT UDP Port,Connection Timeout,Response Timeout
```

**UART 連線**
```
Uart,ConnectionName,Com Port,Baud Rate,Date Bit,Stop Bit,Parity,Check DUT Ready Timeout,Response Timeout
```

**DLL 連線**
```
DLL:LibraryName,ConnectionName,Library開發者定義
```

**APP 連線**
```
APP,ConnectionName,File path of application,check app action(0/1)
```

**SSH 連線**
```
SSH,ConnectionName,Local IP,Target IP,Port,User,Password,Ready Timeout(ms),Default Timeout(ms)
```

**HTTP 連線**
```
HTTP,ConnectionName,LocalIP,TargetIP,Port,CheckReady Timeout,Default Timeout,Path,ContentType
```

---

## 📝 腳本編輯欄位說明

### 基本欄位（欄位用途與修改指引）
| 欄位 | 說明 | 修改重點 | 格式/範例 |
|------|------|----------|-----------|
| **Index** | Command 序號（腳本執行順序） | 不建議手動編號，初次整理時可留空讓工具重排；複製/插入時應確保最終不重複 | 整數（1,2,3…）|
| **Phase** | 測試階段（0:Pretest, 1~96:Normal, 97:EndTest, 98/99:EndPass/Fail） | 新增測項時，確保 Phase 合理排序（如功能測試用 1~96） | 0/1~96/97/98/99 |
| **Title** | 測項名稱（人類可讀） | 清晰描述動作與目的，便於查閱 | 版本號碼檢查/電壓測量/BT狀態檢查 |
| **Marco** | 指向額外 Script 的 Sheet 名稱 | 僅在需要呼叫子腳本時填寫；帶參數放在 Send | SubScriptA |
| **Instrument** | 需要的儀器函數 | 必須與 Instrument Sheet 的 Functions 對應一致 | DMM.MeasureV |
| **Switch** | DUT 與 Device/Switch 的接線設定 | 需與 Switch Sheet、Device 的連接對應 | SwitchName,"DUT(1):L1" |
| **Send** | 要執行的 Command（對 DUT/Device/DLL） | 本欄為核心邏輯；複製貼上時調整連線名、參數與函數 | UART1@ver / :DMM.MeasureV,"CH1","DC" |
| **Reply** | 預期回覆（完全符合或包含） | 完全符合用 `abc`；包含用 `@abc`；避免過度寬鬆 | @Version: / OK |
| **EndPrompt** | 結束回覆提示字串 | 可加速流程（當偵到此字串視為回覆結束） | >> / DONE |
| **Ref** | 將執行結果存入變數 | 後續可在 Validation/Send 取用，`$` 表全域 | version / voltage / $serial |
| **Validation** | 驗證變數是否在上下限內 | 數值判斷與型別要正確，門檻要符合規格 | (voltage,%f,4.75,5.25) |
| **Prompt** | 等待特定提示再送出 | 用於交互式 CLI 測試，避免時序問題 | @Login: |
| **Waiting** | 等待 DUT 回應時間（ms） | 視命令特性調整，避免過短造成 timeout | 3000/5000 |
| **ExecMode** | 執行模式（重試/條件/校準等） | 預設 0；失敗重試或條件流程需正確設定 | 0/1/2:RetryPoint/4:PassStep,FailStep |
| **Description** | 此步驟說明 | 簡要說明動作與期望，便於維護 | 讀取並檢查版本字串 |
| **TestID** | 測試項目代碼 | 必須對應 `TestItemCode` 檔案；新建時使用標準代碼 | V0001/V0002/V0003 |

### Phase 值說明
| Phase | 說明 | 用途 |
|-------|------|------|
| `0` | Pretest | 測試前要先做的事，如控制Power Switch Power On |
| `1~96` | Normal Test | DUT測試 |
| `97` | End Test | DUT測試結束後要進行的事，如控制Power Switch Power Off |
| `98` | End Pass | DUT測試如果Pass要進行的事 |
| `99` | End Fail | DUT測試如果Fail要進行的事 |

### Run Mode 說明
| Mode | 說明 |
|------|------|
| `0` | Normal Run (Default) |
| `1` | Always Run |
| `2` | Skip |
| `3` | Run on fail |

### Switch 欄位格式
```
DeviceName,"DUT(ChainNo 1, 2, …):Device(Route-Port或由Device提供者定義)"
SwitchName," DUT(ChainNo 1, 2, …):Switch(L1, L2, …)"
```

### 進階欄位（欄位用途與修改指引）
| 欄位 | 說明 | 修改重點 | 格式/範例 |
|------|------|----------|-----------|
| **Send** | 要執行的 Command | 優先確認連線別與函數；複製他人腳本時務必調整連線名與參數 | UART1@ver / :DMM.MeasureV,"CH1","DC" |
| **Reply** | 確認執行的結果 | 嚴謹使用 @ 或完全相等，避免過度寬鬆造成誤判 | @Version: / OK |
| **EndPrompt** | 回覆完成提示 | 適用大量回覆指令，加速耗時命令 | >> / DONE |
| **Ref** | 暫存變數 | 規劃變數命名，避免覆蓋；全域用 `$` | version / $serial |
| **Validation** | 數值/範圍驗證 | 型別與上下限匹配，門檻需符合規格 | (voltage,%f,4.75,5.25) |
| **Prompt** | 等待提示再送出 | 適用交互式 shell 步驟 | @Login: |
| **Waiting** | 等待時間 (ms) | 視命令複雜度調整，避免 timeout | 3000/5000 |
| **ExecMode** | 執行模式 | 失敗重試/條件/校準需正確填寫 | 0/1/2:RetryPoint/4:PassStep,FailStep |
| **Description** | 步驟描述 | 簡潔、可追溯 | 讀取並檢查版本字串 |

### Send 欄位格式

**DUT定義**
```
ConnectionName@Command
範例: LAN@wl up
```

**使用Device**
```
:Dev.FunctionName,"參數1","參數2","參數3",….
範例: :Dev.SwitchON,"1"
```

**使用DLL**
```
:LibraryName.FunctionName,"參數1","參數2","參數3",….
範例: :LIB.FORMMAC,"IWF","123"
```

### Ref 欄位格式
```
變數名稱(區域變數) 或 $變數名稱(全域變數)
```

### 輔助函數
| 函數 | 說明 | 格式 |
|------|------|------|
| `SubString` | 擷取某位置開始，長度多長的字串 | `:SubString,"起始位置","長度"` |
| `WithinString` | 擷取介於字串1與字串2間的字串 | `:WithinString,"字串1","字串2","index"` |
| `rpString` | 將被替換的字串替換成替換的字串 | `:rpString,"被替換的字串","替換的字串"` |
| `maString` | 擷取指定字串後面的字串 | `:maString,"指定字串"` |
| `mbString` | 擷取指定字串前面的字串 | `:mbString,"指定字串"` |
| `getMAC` | 抓取MAC格式為Aa:Bb:Cc:Dd:Ee:Ff | `:getMAC` |
| `getMAC2` | 抓取MAC格式為AaBbCcDdEeFf | `:getMAC2` |
| `getMAC3` | 抓取MAC格式為Aa-Bb-Cc-Dd-Ee-Ff | `:getMAC3` |
| `upString` | 轉大寫 | `:upString` |
| `lwString` | 轉小寫 | `:lwString` |
| `inMAC` | 將MAC格式為AaBbCcDdEeFf轉成Aa:Bb:Cc:Dd:Ee:Ff | `:inMAC` |
| `rmMAC` | 將MAC格式為Aa:Bb:Cc:Dd:Ee:Ff轉成AaBbCcDdEeFf | `:rmMAC` |

### Validation 值類型
| 類型 | 說明 |
|------|------|
| `%s` | 字串 |
| `%d` | 整數 |
| `%f` | 浮點數 |
| `%x` | 16進位整數 |

### ExecMode 執行模式
| Mode | 說明 | 格式 |
|------|------|------|
| `0` | Normal mode | - |
| `1` | Direct Retry on Fail | - |
| `2` | Retry from Retry Point | `2:RetryPoint` |
| `3` | Continue | - |
| `4` | Condition | `4:PassStep,FailStep` |
| `5` | Run on Fail | - |
| `6` | Skip | - |
| `7` | Calibration | `7:CalibrationSetp,timeout(ms)` |
| `8` | Normal mode while SFIS Enable | - |
| `9` | Direct Retry while SFIS Enable | - |

### 變數取值方式
- 區域變數：`*(變數名稱)`
- 全域變數：`*$(變數名稱)` (Global.ini所設定的值)

### 實務修改案例（三測項）
- 目標：在現有站別工作表中保留表頭，插入或替換三個測項（版本號碼、電壓、BT）
- 欄位對照（關鍵欄位需填寫）：
  - 版本號碼：
    - TestID=V0001, Phase=1, Title=版本號碼檢查
    - Send=UART1@ver, Reply=@Version:, Ref=version, Waiting=3000, ExecMode=0, Description=讀取並檢查版本字串
  - 電壓量測：
    - TestID=V0002, Phase=2, Title=電壓測量, Instrument=DMM.MeasureV
    - Send=:DMM.MeasureV,"CH1","DC", Ref=voltage, Validation=(voltage,%f,4.75,5.25), Waiting=3000, ExecMode=0, Description=量測 5V 軌電壓
  - BT 狀態：
    - TestID=V0003, Phase=3, Title=BT狀態檢查
    - Send=UART1@bt status, Reply=@BT:ON, Waiting=3000, ExecMode=0, Description=檢查藍牙啟用狀態

### QA 檢查清單
- 結構：Properties/Instrument/Switch/DUTs/各站測試頁均存在
- 欄位：表頭與順序一致，無遺漏（包含 Index/Phase/Title/Marco/Instrument/Switch/Send/Reply/EndPrompt/Ref/Validation/Prompt/Waiting/ExecMode/Description/TestID）
- 內容：TestID 不重複、Phase 合理、連線名稱與函數一致、Validation 型別與上下限正確
- 依賴：Instrument Functions 與 Switch 配線一致；Ref 變數命名不衝突

---

## 🎛️ Instrument 設定

### Device 設定欄位
| 欄位 | 說明 | 格式/範例 |
|------|------|-----------|
| **Mount** | Mount Device by Station Name | 可設定多Station Name，只需使用逗號隔開 |
| **Name** | Device Name | 與DUT所設定的Switch Name可能有關連性 |
| **Sub** | Sub Device | 1表示為Sub Device |
| **ControlDLL** | Device control library | 檔案放在Device資料夾內 |
| **Settings** | Settings of Device | 由Device開發者提供 |
| **Functions** | Device所支援的功能 | 能寫多項，用逗號隔開即可 |
| **Version** | Device library版本 | 用於驗證是否有載錯版本 |
| **Switch** | 設定與Device連接的Switch Name | `SwitchName,"連接設定1","連接設定2",…` |
| **Desc** | Description of Device | Device描述 |

---

## 🔌 Switch 設定

### Switch 設定欄位
| 欄位 | 說明 | 格式/範例 |
|------|------|-----------|
| **Mount** | Mount Switch by Station Name | 可設定多Station Name，只需使用逗號隔開 |
| **Name** | Switch Name | 設定DUT與Device之間的Switch Name |
| **ControlDLL** | Switch control library | Switch控制庫 |
| **Settings** | Settings of Switch | 由Switch開發者提供 |
| **Version** | Switch library版本 | 用於驗證是否有載錯版本 |
| **Loss** | 設定Switch的Loss | 損耗值 |
| **Desc** | Description of Switch | Switch描述 |

---

## ⚙️ Global.ini 使用

### 區塊說明
Global.ini 分為兩個區塊：

1. **Settings** - 用於 DUTs Sheet、Instrument Sheet 和 Switch Sheet
2. **Scripts** - 用於 Test Script Sheet

### 設定方式
```
參數名稱=數值
```

### 取值方式
```
*$(參數名稱)
```

---

## 📊 日誌系統

### 日誌類型
1. **System Log** - 檔名為 `System.log`
2. **DUT Log** - 檔名格式見下方說明

### DUT Log 檔名格式
- **Pass**: `第幾機+Station Name-ISN-測試時間-PASS.log`
- **Fail**: `第幾機+Station Name-ISN-測試時間-Test ID.log`

### 日誌內容格式
- **System Log**: `日期 時間 <System> 訊息內容`
- **DUT Log**: 
  - `日期 時間 <第幾機> > 執行Command`
  - `日期 時間 <第幾機> < 執行結果`

### 常見問題確認步驟
1. 先找出測試失敗的測項
2. 比對log的command執行順序是否與script一致
3. 確認執行結果

### 執行結果常見問題
1. 有Exception字樣
2. 所存的值與取出的值不同
3. Function執行結果有錯誤或沒變化
4. DUT回覆訊息的時間差
5. 沒有符合所設定的Criteria

---

## 🛠️ 工具使用

### CentimaniScriptTool

#### 1. Load TestID list
- 載入 `TestItemCode*.xlsx`
- 結果將顯示於 table 內，可初步確認

#### 2. Check MainScript
- 載入 `*TestFlow.xlsx`
- 進行初步定義確認與TestID index 編排
- 結果將顯示於 table 內，可初步確認
- 於 SheetName 可切換 Sheet

#### 3. Gen CheckSum
- 載入 `TestItemCode*.xlsx` / `*TestFlow.xlsx` / `Instruments.xml` / `Switches.xml`
- 進行 CheckSum sign
- 程序將回存各 file checksum於相對目錄 `system.ini`

### Centimani DebugLaunch

#### 功能
讓Centimani進入免check checksum的debug mode，並能維持一天使用權限。

#### 步驟
1. 首先先將 `System.ini` 的 `DebugMode` 設成 `1`
2. 執行資料夾內的 `DebugLaunch.exe`
3. 若無權限則會出現輸入ID跟PW視窗
4. ID與PW若通過驗證則會啟動Centimani
5. ID與PW若沒通過驗證則會出現Fail to Launch Debug Mode，然後啟動normal mode centimani

---

## 🆕 新版本功能

### Ver1.71 儀器參數更新 (2023-04-11)

#### 新增儀器支援
新版本包含36個工作表，支援更多儀器：

**電源供應器**
- `iPower2401` - 可程式電源供應器
- `iPowerPro800` - 專業電源供應器

**數位萬用表**
- `Agilent34401A` - 高精度數位萬用表
- `GDM906x` - 數位萬用表系列

**示波器**
- `ScpTDS3014B` - Tektronix示波器
- `SAn9000` - 網路分析儀

**資料擷取**
- `DaqUSBNi` - National Instruments USB資料擷取
- `DAQ970A` - Keysight資料擷取系統
- `DaqNI4461` - NI高精度資料擷取

**射頻設備**
- `E4438C` - 射頻信號產生器
- `iRFSW3001` - 射頻開關
- `RF_Switch` - 射頻開關控制

**特殊設備**
- `LED_analyser` - LED分析儀
- `QRDecode` - QR碼解碼器
- `RedRat` - 紅外線遙控器模擬器

#### 實用工具庫
- `UtilityLibrary` - 通用工具函式庫
- `InstIQApi_A` / `InstIQApi_B` - 儀器IQ API
- `SCPI_Controller` - SCPI控制器
- `DevUart` - UART設備控制

### 腳本編輯工具增強
- `EditorScriptTool` - 專用腳本編輯工具
- 提供更好的腳本驗證和編輯支援
- 整合式開發環境

---

## 🤖 AI 腳本產生邏輯（基於現有腳本修改）

### 核心原則
- 不從零生成新腳本，改為「複製現有腳本」並修改測項
- 腳本模板可以使用「任何版本的腳本」，不限制特定檔案
- 保持原有工作表與欄位結構，僅調整必要內容
- **重要：每次修改腳本前，必須先使用分析工具了解腳本結構**

### 工作流程
1. **腳本結構分析（必須步驟）**
   - 使用 `analyze_imu_script.py` 分析整體結構
   - 使用 `debug_phase_structure.py` 分析 Phase 結構
   - 記錄關鍵欄位類型和腳本邏輯
   - **重要**: 檢查是否有現成的分析工具可以使用，避免重複編寫
2. 腳本模板選擇
   - 選擇相同或相近專案類型（如 KANGAROO）
   - 優先選擇結構完整、可讀性高的腳本
   - 可使用任何版本作為模板（ex: 舊版/新版皆可）
3. 複製與重命名
   - 複製原始腳本（ex: `Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx`）
   - 重新命名（ex: `Validation_3Items_TestFlow.xlsx`）
4. 測項調整策略（擇一或混用）
   - 策略A：直接修改現有相近測項（改 TestID/Send/Reply/Description）
   - 策略B：自其他腳本複製缺少的測項，貼上並調整參數
   - 策略C：在表尾新增測項，維持欄位一致
4. 需要的三個測項（範例）
   - 版本號碼：`UART1@ver` + `Reply=@Version:` → `Ref=version`
   - 電壓量測：使用 DMM 函式 `:DMM.MeasureV,"CH1","DC"` → `Validation=(voltage,%f,4.75,5.25)`
   - BT 狀態：`UART1@bt status` + `Reply=@BT:ON`
5. 工作表調整重點
   - Properties：更新 Project/Date
   - Instrument：保留原有，必要時新增 DMM（MeasureV）
   - Switch：保留/對應 Instrument 設定
   - DUTs：保留原本連線設定（ex: UART）
   - Main（或對應站別）：依策略調整/新增/刪除測項
6. 品質檢查清單
   - **分析工具檢查**：已使用分析工具了解腳本結構
   - 結構：Properties/Instrument/Switch/DUTs/各站測試頁均存在
   - 欄位：表頭與順序一致，無遺漏
   - 內容：TestID 不重複、Phase 合理、參數/變數指向正確
   - 依賴：Instrument Functions 與 Switch 配線一致

### 範例修改（示意）
- 將「WiFi連線測試」修改為「版本號碼檢查」：
  - TestID: W001 → V0001
  - Title: WiFi連線測試 → 版本號碼檢查
  - Send: wifi@connect → UART1@ver
  - Reply: @Connected → @Version:
  - Description: 測試WiFi連線 → 讀取版本字串
- 從其他腳本複製「電壓量測」：
  - TestID: 改為 V0002、Phase 改為 2、Instrument= DMM.MeasureV

### 腳本為何如此設計（決策準則）
- 目的：可重現、可追蹤、可維護，並能對照指令表與 LOG。
- 檔內結構：Properties/Instrument/Switch/DUTs/站別頁，各有其必要性與對應職責。
- 關鍵欄位：TestID、Phase、Send、Reply、Ref/Validation、Prompt/EndPrompt、Waiting/ExecMode。
- 三測項設計：版本號用 CLI 取得；電壓用 DMM 量測並設 Validation；BT 用 CLI 狀態字串比對。
- 站別拆分與 Index：站別對應設備/配線差異；Index 建議最後統一重排。
- Macro：共用序列（如上電、校準）以宏重用，降低維護成本。
- 外部依據：CMD_TABLE 指令表（命令/回覆）、LOG（回覆樣態）、Test Item Code V*.xlsx（TestID）。
- AI 選型：讀資訊→CLI；量化物理量→儀器；回覆與門檻依指令表/規格；時序以 Prompt/Waiting/ExecMode 補強。
- **分析工具重要性**：每次修改前必須使用分析工具，避免破壞腳本結構和邏輯。
- 參考與步驟：依本節與「欄位說明/實務案例/QA 清單」逐步套用。

### 全域變數系統與 IPLAS 邏輯

#### 全域變數來源與讀取機制
1. **Global.ini 配置**
   - `sfisSKU=N3C2401C` - 預設 SKU 值（離線測試用）
   - `VALO360_ALL_MODEL=@69-2E224C20P02||@69-2E224C30P01||@69-2E224C23P02||@N3C2401C||@N3C2401NB||@N3C2401W||@69-2E224624P02`
   - `VALO360_5G=@69-2E224C20P02||@N3C2401C`
   - `VALO360_NObattery=@69-2E224C30P01||@N3C2401NB`
   - `VALO360_WIFI=@69-2E224C23P02||@N3C2401W||@69-2E224624P02`

2. **SFIS 系統整合**
   - 腳本執行時從 SFIS 讀取實際 SKU 值
   - 使用 `:SfGetVersion` 指令獲取 `sfisSKU`
   - 將 SFIS 的 SKU 值設定到全域變數 `$G_VALO360_MODEL`

#### IMU 腳本 IPLAS 邏輯分析

##### **腳本設計邏輯**
1. **Check Valo360 model 階段**
   ```
   :SetVal,"$G_VALO360_MODEL","*(sfisSKU)"  → 從 SFIS 設定全域變數
   :GetVal,"$G_VALO360_MODEL"              → 讀取設定值
   :GetVal,"$G_VALO360_MODEL"              → 驗證是否為 *$(VALO360_ALL_MODEL)
   ```

2. **三種模型配置階段（條件式執行）**
   - **5G 模型路徑**: 檢查 `*$(VALO360_5G)` → 設定 `N3C2401C`
   - **WiFi 模型路徑**: 檢查 `*$(VALO360_WIFI)` → 設定 `N3C2401W`
   - **無電池模型路徑**: 檢查 `*$(VALO360_NObattery)` → 設定 `N3C2401B`

##### **為什麼這樣設計？**
1. **動態模型識別**: 根據 SFIS 系統的 SKU 資訊，動態決定硬體配置
2. **條件式執行**: 使用 `:GetVal` 檢查全域變數值，執行對應路徑
3. **驗證機制**: 每次設定後都用 `:GetModelName` 驗證成功
4. **腳本重用**: 同一個腳本處理三種不同硬體配置

##### **數值代入後的執行流程**
```
sfisSKU = "VALO360_5G" → $G_VALO360_MODEL = "VALO360_5G" → 執行 5G 路徑 → 設定 "N3C2401C"
sfisSKU = "VALO360_WIFI" → $G_VALO360_MODEL = "VALO360_WIFI" → 執行 WiFi 路徑 → 設定 "N3C2401W"
sfisSKU = "VALO360_NObattery" → $G_VALO360_MODEL = "VALO360_NObattery" → 執行無電池路徑 → 設定 "N3C2401B"
```

##### **關鍵設計特點**
- **全域變數管理**: `$G_VALO360_MODEL` 作為中央配置點
- **SFIS 整合**: 從生產系統讀取 SKU 資訊，實現自動化配置
- **條件分支**: 根據變數值決定執行路徑
- **統一流程**: 三種模型都遵循設定→驗證→等待的標準流程
- **腳本靈活性**: 實現腳本重用，避免為每種配置寫獨立腳本

#### 變數系統詳細分析

##### **變數類型與使用模式**
1. **全域變數 (`$G_`)**
   - 格式: `$G_VAR_NAME`
   - 用途: 腳本執行過程中的中央配置點
   - 生命週期: 腳本執行期間有效
   - 範例: `$G_VALO360_MODEL`

2. **SFIS 變數 (`*(sfisSKU)`)**
   - 格式: `*(sfisSKU)`
   - 用途: 從 SFIS 系統讀取的 SKU 值
   - 來源: SFIS 資料庫
   - 範例: `*(sfisSKU)` → 可能值: `VALO360_5G`, `VALO360_WIFI`, `VALO360_NObattery`

3. **配置變數 (`*$(CONFIG_NAME)`)**
   - 格式: `*$(CONFIG_NAME)`
   - 用途: 從 Global.ini 讀取的配置值
   - 來源: Global.ini 檔案
   - 範例: `*$(VALO360_5G)`, `*$(VALO360_WIFI)`, `*$(VALO360_NObattery)`

##### **變數使用場景分析**
```
行 14: 0,Check Valo360 model
  Send: :SetVal,"$G_VALO360_MODEL","*(sfisSKU)"
  → 將 SFIS 的 SKU 值設定到全域變數

行 16: 0,SET iplus Modelname_Valo360_5G
  Send: :GetVal,"$G_VALO360_MODEL"
  Reply: *$(VALO360_5G)
  → 檢查全域變數是否匹配 5G 配置

行 20: 0,SET iplus Modelname_Valo360_WIFI
  Send: :GetVal,"$G_VALO360_MODEL"
  Reply: *$(VALO360_WIFI)
  → 檢查全域變數是否匹配 WiFi 配置

行 24: 0,SET iplus Modelname_Valo360_noBattery
  Send: :GetVal,"$N3C2401B"
  Reply: *$(VALO360_NObattery)
  → 檢查全域變數是否匹配無電池配置
```

##### **變數系統設計原則**
1. **分層管理**
   - SFIS 層: 生產系統的實際 SKU 值
   - 全域層: 腳本執行時的中央配置
   - 配置層: 預定義的模型配置選項

2. **動態綁定**
   - 腳本啟動時從 SFIS 讀取 SKU
   - 根據 SKU 值動態選擇配置路徑
   - 實現腳本的通用性和靈活性

3. **驗證機制**
   - 每次設定後都有對應的驗證步驟
   - 確保變數值正確傳遞和設定
   - 提供錯誤檢測和除錯能力

##### **變數系統使用指南（AI 必讀）**
1. **修改腳本前必須理解變數系統**
   - 檢查腳本中使用的所有變數類型
   - 理解變數的來源和用途
   - 確保不破壞變數的設定和讀取邏輯

2. **變數修改原則**
   - 全域變數 (`$G_`)：腳本執行時的中央配置，謹慎修改
   - SFIS 變數 (`*(sfisSKU)`)：生產系統整合，不可修改
   - 配置變數 (`*$(CONFIG_NAME)`)：預定義配置，可擴展但不可破壞

3. **常見錯誤避免**
   - 不要刪除變數設定步驟
   - 不要改變變數名稱格式
   - 不要破壞變數的驗證流程
   - 新增測試項目時要考慮變數依賴關係

4. **變數系統除錯技巧**
   - 使用 `:GetVal` 檢查變數值
   - 檢查 Global.ini 中的配置定義
   - 確認 SFIS 系統的 SKU 值
   - 驗證變數的設定和讀取順序

#### 腳本設計邏輯深度分析（AI 必讀）

##### **為什麼腳本要這樣設計？**

###### 1. **分階段執行架構（Phase-based Design）**
```
Phase 0: 系統初始化與連接
Phase 1: 路由檢查與設備識別  
Phase 2: SFIS 系統整合
Phase 3: 動態模型配置
Phase 4: IMU 陀螺儀測試
Phase 5: IMU 磁力計測試
Phase 6: IMU 結果驗證
Phase 7-8: 硬體按鈕測試
```

**設計理由**：
- **模組化測試**：每個 Phase 專注於特定功能，便於維護和除錯
- **條件式執行**：Phase 3 的模型配置決定後續測試路徑
- **漸進式驗證**：從基本連接到複雜測試，逐步建立測試環境

###### 2. **全域變數驅動的條件邏輯**
```
$G_VALO360_MODEL ← *(sfisSKU) ← SFIS系統
    ↓
條件檢查：*$(VALO360_5G) || *$(VALO360_WIFI) || *$(VALO360_NObattery)
    ↓
動態設定：N3C2401C || N3C2401W || N3C2401B
```

**設計理由**：
- **生產線適應性**：同一個腳本處理三種不同硬體配置
- **SFIS 整合**：自動從生產系統讀取 SKU，無需手動配置
- **腳本重用**：避免為每種配置寫獨立腳本

###### 3. **IPLAS 指令系統的巧妙運用**

**變數管理指令**：
- `:SetVal` - 設定全域變數
- `:GetVal` - 讀取並驗證變數值
- `:SetModelName` - 設定設備模型名稱

**系統整合指令**：
- `:SfGetVersion` - 從 SFIS 讀取 SKU
- `:SfCheckRoute` - 檢查 SFIS 路由
- `:ShowISN` - 顯示設備序號

**設計理由**：
- **統一介面**：所有系統操作都通過標準化指令
- **錯誤處理**：每個指令都有對應的 Reply 驗證
- **除錯能力**：可以追蹤每個變數的設定和讀取過程

##### **具體設計邏輯分析**

###### **Phase 0-2: 基礎建設階段**
```
Login → CheckRoute → GET sfisSKU
```
**目的**：建立測試環境，獲取設備資訊，準備模型配置

###### **Phase 3: 智能模型配置階段**
```
Check Valo360 model → 條件分支 → 三種模型設定
```
**核心邏輯**：
1. 從 SFIS 讀取 SKU 值
2. 設定到全域變數 `$G_VALO360_MODEL`
3. 根據 SKU 值執行對應的模型配置路徑
4. 每種配置都有完整的設定→驗證→等待流程

###### **Phase 4-6: IMU 測試執行階段**
```
Check Gyro → Check E compass → Check E compass result
```
**測試邏輯**：
- **自檢優先**：先執行 `imu mag selftest` 確保硬體正常
- **數據讀取**：執行 `imu mag status` 獲取實際測量值
- **結果驗證**：使用 Validation 欄位驗證測試結果

###### **Phase 7-8: 硬體互動測試階段**
```
Check_HW_BTN_REBOOT → Check_SW_BTN_REBOOT
```
**設計理由**：
- **用戶互動**：測試需要人工操作的硬體功能
- **時序控制**：使用 `:Delay` 和 `:ShowConfirmBox` 控制測試節奏
- **狀態驗證**：通過 SSH 指令檢查按鈕狀態

##### **腳本設計的深層原因**

###### 1. **生產線效率考量**
- **自動化程度高**：大部分測試自動執行，減少人工干預
- **錯誤處理完善**：每個步驟都有驗證機制
- **適應性強**：自動識別不同硬體配置

###### 2. **維護性設計**
- **模組化結構**：每個 Phase 獨立，便於修改和除錯
- **標準化指令**：使用 IPLAS 標準指令，降低學習成本
- **變數集中管理**：全域變數統一管理，避免重複設定

###### 3. **測試品質保證**
- **漸進式驗證**：從基礎到複雜，確保每個階段都正確
- **條件式執行**：根據硬體配置選擇適當的測試路徑
- **結果追蹤**：每個測試項目都有 TestID，便於結果分析

###### 4. **系統整合性**
- **SFIS 整合**：與生產系統無縫對接
- **多硬體支援**：一個腳本支援多種硬體配置
- **標準化輸出**：統一的測試結果格式

##### **AI 學習重點**
1. **理解腳本架構**：Phase 設計、條件邏輯、變數系統
2. **掌握設計原則**：模組化、標準化、可維護性
3. **學習最佳實踐**：生產線效率、測試品質、系統整合
4. **應用設計模式**：在修改或創建腳本時遵循相同的設計邏輯

#### DUT Sheet 邏輯分析（結合 Global.ini）

##### **DUT Sheet 的設計邏輯**

###### 1. **DUT Sheet 結構與欄位**
```
Load: 控制是否載入該 DUT
DUT Name: 設備名稱（如 VALO360$IMU, VALO360$TEMP）
Station: 測試站別（如 IMU,0 或 TEMP,0）
Parameter: 設備參數（引用 Global.ini 的變數）
SFIS_DeviceID: SFIS 系統的設備 ID
ScanBarcode: 條碼掃描設定（可選）
Connection1-10: 最多 10 個連接設定
```

###### 2. **變數引用系統**
**參數變數引用**：
- `*$(PCIP_1)` → Global.ini: `PCIP_1 = 192.168.11.3`
- `*$(DUTIP_1)` → Global.ini: `DUTIP_1 = 192.168.11.143`
- `*$(DUT_UR1)` → Global.ini: `DUT_UR1 = COM4`
- `*$(PCUART_fixture)` → Global.ini: `PCUART_fixture = COM5`
- `*$(DEVID_1)` → Global.ini: `DEVID_1 = 125335`

**為什麼這樣設計？**
- **集中配置管理**：所有網路、串口、設備 ID 都在 Global.ini 統一管理
- **環境適應性**：不同測試環境只需修改 Global.ini，腳本自動適應
- **變數重用**：多個 DUT 可以共用相同的配置變數

###### 3. **連接邏輯架構**

**連接類型與用途**：
1. **APP 連接**：`"APP","CmdConsole","C:\Windows\System32\cmd.exe,1,5000,"`
   - 用途：本地命令執行
   - 參數：程式路徑、參數、超時設定

2. **UART 連接**：`"Uart","UART","*$(DUT_UR1),115200,8,One,None,None,10000,5000"`
   - 用途：與 DUT 的串口通訊
   - 參數：COM 埠、波特率、資料位、停止位、校驗、超時

3. **SSH 連接**：`"SSH","SSH1","*$(PCIP_1),*$(DUTIP_1),22,root,,5000,1000"`
   - 用途：遠端 SSH 登入
   - 參數：PC IP、DUT IP、埠號、用戶名、密碼、超時

4. **UARTF 連接**：`"Uart","UARTF","*$(PCUART_fixture),9600,8,One,None,None,10000,5000"`
   - 用途：與治具的串口通訊
   - 參數：治具 COM 埠、較低波特率

##### **DUT Sheet 與 Global.ini 的整合邏輯**

###### 1. **配置層次結構**
```
Global.ini (環境配置)
    ↓
DUT Sheet (設備配置)
    ↓
測試腳本 (執行邏輯)
```

###### 2. **變數解析流程**
```
腳本執行時：
1. 讀取 DUT Sheet 中的變數引用（如 *$(PCIP_1)）
2. 從 Global.ini 解析實際值（如 192.168.11.3）
3. 建立實際的連接和參數
4. 執行測試腳本
```

###### 3. **多 DUT 支援邏輯**
```
VALO360$IMU (IMU 測試站):
  - Station: IMU,0
  - 專注於 IMU 相關測試

VALO360$TEMP (溫度測試站):
  - Station: TEMP,0  
  - 包含條碼掃描功能
  - 共用相同的連接設定
```

##### **為什麼 DUT Sheet 要這樣設計？**

###### 1. **生產線靈活性**
- **多站測試**：一個腳本支援多個測試站
- **設備切換**：可以動態載入不同的 DUT 配置
- **環境適應**：不同工廠環境只需修改 Global.ini

###### 2. **連接管理**
- **標準化介面**：統一的連接類型定義
- **參數化配置**：所有連接參數都可配置
- **錯誤處理**：每個連接都有超時和重試設定

###### 3. **SFIS 整合**
- **設備追蹤**：每個 DUT 都有唯一的 SFIS Device ID
- **生產追蹤**：可以追蹤每個設備的測試歷史
- **品質管理**：SFIS 系統記錄測試結果和統計

##### **AI 修改 DUT Sheet 的注意事項**

###### 1. **變數引用原則**
- **不要硬編碼**：IP 地址、COM 埠等都要用變數引用
- **保持一致性**：多個 DUT 使用相同的變數名稱
- **檢查依賴**：新增變數時要確保 Global.ini 中有定義

###### 2. **連接設定原則**
- **類型正確**：確保連接類型與實際用途匹配
- **參數完整**：所有必要的連接參數都要設定
- **超時合理**：根據實際通訊需求設定適當的超時值

###### 3. **站別設計原則**
- **功能專一**：每個站別專注於特定測試功能
- **資源共享**：可以共用相同的連接設定
- **擴展性**：設計時考慮未來可能新增的測試站

#### 腳本產生與管理系統（未來發展方向）

##### **腳本產生的正確思維**

###### 1. **為什麼不需要寫 Python 腳本？**
- **腳本修改不頻繁**：不需要大量自動化
- **每次修改需求不同**：很難用一套程式碼處理所有情況
- **直接編輯更直觀**：在 Excel 中直接看到修改結果
- **維護成本高**：Python 腳本需要維護和除錯

###### 2. **腳本產生的正確方法**
```
方法 1：建立腳本模板庫
├── 版本檢查模板.xlsx
├── 基本功能測試模板.xlsx  
├── 完整測試模板.xlsx
├── 快速驗證模板.xlsx
└── 客製化測試模板.xlsx

方法 2：使用 Excel 的複製功能
- 複製現有腳本
- 根據需求修改特定 Phase
- 儲存為新檔案

方法 3：建立修改指南
- 提供標準化的修改步驟
- 確保腳本結構一致性
- 避免常見錯誤
```

##### **理想中的 GUI 腳本管理系統**

###### 1. **系統架構設計**
```
GUI 腳本管理系統
├── 腳本選擇器（下拉選單）
│   ├── 測試項目類型
│   ├── 硬體配置選項
│   └── 測試深度選擇
├── 腳本產生器
│   ├── 模板選擇
│   ├── 參數配置
│   └── 腳本生成
├── 腳本驗證器
│   ├── 結構檢查
│   ├── 變數驗證
│   └── 邏輯分析
└── 腳本管理
    ├── 版本控制
    ├── 模板更新
    └── 使用統計
```

###### 2. **測試項目下拉選單設計**
```
測試項目選擇：
├── 基礎功能測試
│   ├── 版本號碼檢查
│   ├── 網路連線測試
│   ├── 基本通訊測試
│   └── 硬體識別測試
├── 功能測試
│   ├── IMU 測試
│   ├── 音訊測試
│   ├── 顯示測試
│   └── 按鈕測試
├── 完整測試
│   ├── 全功能測試
│   ├── 壓力測試
│   ├── 穩定性測試
│   └── 邊界測試
└── 客製化測試
    ├── 特定功能測試
    ├── 組合測試
    └── 專案測試
```

###### 3. **腳本產生流程**
```
1. 選擇測試項目類型
2. 選擇硬體配置（5G/WiFi/無電池）
3. 選擇測試深度（基本/完整/客製化）
4. 配置測試參數（超時、重試次數等）
5. 選擇腳本模板
6. 自動產生腳本
7. 腳本驗證檢查
8. 下載或直接使用
```

##### **腳本驗證系統**

###### 1. **結構檢查項目**
- **工作表完整性**：Properties、DUTs、Switch、Instrument、測試頁
- **欄位一致性**：表頭格式、欄位順序、必要欄位存在
- **Phase 結構**：Phase 編號連續性、邏輯順序
- **變數引用**：所有變數都有對應的定義

###### 2. **變數驗證項目**
- **Global.ini 依賴**：檢查腳本中引用的變數是否在 Global.ini 中定義
- **變數格式**：變數名稱格式是否正確（如 `*$(VAR_NAME)`）
- **變數一致性**：相同用途的變數是否使用相同名稱
- **變數完整性**：必要的變數是否都已設定

###### 3. **邏輯分析項目**
- **測試流程**：Phase 之間的邏輯關係是否合理
- **條件分支**：條件式執行的邏輯是否完整
- **錯誤處理**：是否有適當的錯誤處理和驗證機制
- **資源管理**：連接、儀器、開關的配置是否合理

##### **AI 在腳本管理系統中的角色**

###### 1. **腳本產生階段**
- **模板選擇建議**：根據測試需求推薦最適合的腳本模板
- **參數配置指導**：提供參數設定的建議和說明
- **邏輯優化建議**：分析測試邏輯，提供改進建議

###### 2. **腳本驗證階段**
- **自動化檢查**：自動檢查腳本的結構、變數、邏輯
- **問題診斷**：識別腳本中的問題並提供解決方案
- **品質評估**：評估腳本的品質和可靠性

###### 3. **腳本維護階段**
- **版本管理**：追蹤腳本的修改歷史和版本變化
- **模板更新**：根據使用反饋更新腳本模板
- **最佳實踐**：收集和分享腳本設計的最佳實踐

##### **實現路徑規劃**

###### 1. **第一階段：腳本模板庫**
- 建立常用測試項目的腳本模板
- 提供標準化的修改指南
- 實現基本的腳本複製和修改功能

###### 2. **第二階段：腳本驗證器**
- 開發腳本結構檢查工具
- 實現變數引用驗證
- 建立腳本品質評估標準

###### 3. **第三階段：GUI 系統**
- 開發用戶友好的圖形介面
- 實現腳本選擇和配置功能
- 整合腳本產生和驗證功能

###### 4. **第四階段：智能優化**
- 整合 AI 分析功能
- 實現自動化腳本優化
- 建立智能腳本推薦系統

##### **關鍵成功因素**
1. **模板標準化**：確保所有腳本模板遵循一致的設計原則
2. **驗證完整性**：建立全面的腳本驗證機制
3. **用戶體驗**：設計直觀易用的 GUI 介面
4. **持續改進**：根據使用反饋不斷優化系統
5. **AI 整合**：充分利用 AI 的分析和優化能力

### IMU 測試指南（VALO360）
- 用途：驗證 IMU（加速度/陀螺/磁力）自檢、偏移/比例、資料率、飽和狀態
- 設計理由：
  - 多採 CLI 讀回（UART/SSH）→ 直接取得韌體回覆與自檢結果
  - 數值檢核靠 Ref+Validation → 對齊電氣/演算法規格
  - 串流場景用 Waiting/EndPrompt 控制時序 → 避免截斷/超時
  - 不需外接量測儀時不使用 Instrument；僅在上電/切換才用
- 欄位範型：
  - 自檢：
    - Send=UART1@imu selftest，Reply=@SELFTEST:PASS
  - 加速度靜態偏移：
    - Send=UART1@imu read 200ms → Ref=ax,ay,az → Validation=(ax,%f,-0.05,0.05),(ay,%f,-0.05,0.05),(az,%f,0.95,1.05)
  - 資料率：
    - Send=UART1@imu stream 1000ms → Ref=rate → Validation=(rate,%f,95,105) → EndPrompt=DONE
- TestID：由 `Test Item Code V*.xlsx` 以關鍵字（IMU/SELFTEST/ACC/GYRO）查表後填入

#### IMU 腳本中的變數系統應用
- **模型配置階段**：使用全域變數系統動態設定硬體配置
- **測試執行階段**：根據配置執行對應的 IMU 測試項目
- **結果驗證階段**：使用 Validation 欄位驗證測試結果
- **變數整合**：SFIS SKU → 全域變數 → 硬體配置 → 測試執行

### 實務修改案例：IMU 兩測項腳本
基於現有腳本 `VALO360_TestFlow_20250326_IMU.xlsx` 進行修改，保持原有結構和邏輯：

#### 修改策略
1. **不重新生成**：複製現有腳本，僅修改 Phase 5 和 Phase 6 的內容
2. **保持結構**：維持所有工作表（Properties、DUTs、Switch、Instrument、IMU）
3. **欄位對應**：根據現有腳本分析，Phase 值為字串類型（'5', '6'）

#### 具體修改內容
- **Phase 5: Check E compass**
  - Title: `0,Check E compass`
  - Send: `SSH1@imu mag selftest`
  - Reply: `@SELFTEST:PASS`
  - Waiting: `10000`
  - Description: `Check E compass selftest`
  - TestID: `WUOT004`（查表得到）

- **Phase 6: Check E compass result**
  - Title: `0,Check E compass result`
  - Send: `SSH1@imu mag status`
  - Reply: `@ECOMPASS:PASS`
  - Waiting: `5000`
  - Description: `Check E compass result`
  - TestID: `WUOT006`（查表得到）

#### 修改工具
使用 `modify_imu_script_properly.py` 腳本：
- 自動找到 Phase 5 和 Phase 6 的行數
- 直接修改對應欄位值
- 保持其他欄位不變
- 輸出修改後的腳本檔案

#### 腳本分析工具（必須保留）
在修改腳本前，必須先使用分析工具了解腳本結構：

1. **`analyze_imu_script.py`** - 完整腳本結構分析
   - 分析所有工作表（Properties、DUTs、Switch、Instrument、IMU）
   - 顯示欄位結構和測試項目數量
   - 特別分析 IMU 工作表的詳細內容

2. **`debug_phase_structure.py`** - Phase 結構調試
   - 分析所有 Phase 值和對應行數
   - 顯示每個 Phase 的測試項目標題和 Send 指令
   - 幫助理解腳本的階段結構

3. **使用流程**
   ```
   步驟1: python analyze_imu_script.py          # 了解整體結構
   步驟2: python debug_phase_structure.py      # 分析 Phase 結構
   步驟3: python modify_imu_script_properly.py # 進行腳本修改
   ```

4. **為什麼必須保留**
   - 每次修改腳本前都需要先分析結構
   - 不同腳本的 Phase 值類型可能不同（數字 vs 字串）
   - 幫助 AI 理解腳本的設計邏輯和欄位用途
   - 避免修改時破壞腳本結構

#### 關鍵學習點
1. **Phase 結構**：每個 Phase 只有一行，Phase 值為字串類型
2. **欄位保持**：Index_34、Marco、Instrument、Switch 等欄位保持原值
3. **TestID 查表**：必須從 `Test Item Code V*.xlsx` 查詢對應的測試項目代碼
4. **腳本完整性**：修改後腳本仍包含完整的測試流程（Login、CheckRoute、GET sfisSKU 等）
5. **變數系統理解**：必須理解全域變數、SFIS變數、配置變數的使用方式和設計邏輯
6. **配置流程保持**：修改測試項目時，不能破壞原有的模型配置流程和變數設定邏輯

---

## 🔧 文件分析工具（必須保留，避免重複編寫）

### 重要原則
**在分析任何 PPT/Word/Excel 文件前，必須先檢查現有目錄是否有對應的分析工具可以使用，避免重複編寫分析代碼。**

### 現有分析工具清單

#### 1. **PPT 分析工具**
- **檔案**: `ppt_analyzer.py`
- **功能**: 分析 Centimani 腳本編輯教學 PPT
- **特點**: 
  - 提取文字內容和幻燈片結構
  - 生成腳本編輯速查表
  - 記錄重要的教學要點
- **使用時機**: 需要分析 PPT 教學文件時

#### 2. **Excel 模板分析工具**
- **檔案**: `analyze_excel_templates.py`
- **功能**: 分析 Excel 範例檔案結構
- **特點**:
  - 分析工作表結構和維度
  - 提取範例數據
  - 支援 KANGAROO、VALO360 等專案
- **使用時機**: 需要了解 Excel 腳本格式要求時

#### 3. **新版本分析工具**
- **檔案**: `analyze_new_centimani_versions.py`
- **功能**: 分析新版本 Centimani 文件
- **特點**:
  - 版本比較和功能分析
  - 新功能識別
  - 更新建議生成
- **使用時機**: 需要分析新版本文件時

#### 4. **腳本邏輯分析工具**
- **檔案**: `analyze_scripts_logic.py`
- **功能**: 分析所有腳本的邏輯結構
- **特點**:
  - 統計 CLI vs Device 調用
  - 分析 Phase/ExecMode/Validation 使用模式
  - 推斷腳本設計原因
- **使用時機**: 需要理解腳本設計邏輯時

### 使用流程
```
步驟1: 檢查現有工具目錄
步驟2: 選擇對應的分析工具
步驟3: 執行分析（避免重複編寫）
步驟4: 根據分析結果進行腳本修改
```

### 為什麼必須保留
- **避免重複工作**: 每次分析相同類型文件時，直接使用現有工具
- **保持一致性**: 使用統一的分析邏輯和輸出格式
- **提高效率**: 不需要重新編寫分析代碼
- **維護性**: 工具更新時，所有使用的地方都會受益

---

## 🔧 iPLAS參數參考

### iPLAS v2.0 新功能

#### 版本資訊
- **版本**: v2.0
- **更新日期**: 2023-07-18
- **主要改進**: 參數列表擴展、範例增加、功能增強

#### 參數列表結構
1. **Version** - 版本資訊和更新記錄
2. **Argument List** - 完整的參數列表和說明
3. **Example** - 實用範例和最佳實踐

#### 主要參數類別
 你幫
**基本參數**
- 連接設定參數
- 認證參數
- 超時設定

**進階功能參數**
- 資料庫操作參數
- 檔案處理參數
- 網路通訊參數

**iPLAS特定參數**
- 專案管理參數
- 測試流程參數
- 結果處理參數

#### 使用建議
1. **參考範例**: 使用Example工作表作為開發起點
2. **參數驗證**: 使用Argument List進行參數檢查
3. **版本相容**: 確認iPLAS版本與參數版本的相容性
4. **最佳實踐**: 遵循範例中的最佳實踐模式

---

## ❗ 常見問題與除錯

### System Log 常見問題
1. Scripts內容格式有錯誤
2. Script檔案無法存取
3. Device無法連線

### 腳本編輯注意事項
1. **不同站別可設定不同分頁管理**
2. **如果有不同測項但執行的Command重複性很高，則可使用Marco來方便編輯**
3. **Instrument欄位是對應Device的Functions**
4. **Switch欄位第一個參數值是對應Device Name或Switch Name**
5. **Switch欄位是設定Switch Name，則Device的Switch必須也設定Switch Name**

### 變數使用注意事項
- 區域變數使用 `*(變數名稱)`
- 全域變數使用 `*$(變數名稱)`
- 變數名稱不能重複
- 變數值在腳本執行過程中會保持

### 腳本執行順序
1. Pretest (Phase 0)
2. Normal Test (Phase 1-96)
3. End Test (Phase 97)
4. End Pass/Fail (Phase 98/99)

### 新版本相容性注意事項
1. **儀器參數版本**: 確認使用Ver1.71的參數設定
2. **iPLAS整合**: 使用v2.0參數列表進行設定
3. **腳本編輯工具**: 利用新的EditorScriptTool功能
4. **版本檢查**: 定期檢查儀器和軟體版本相容性

---

## 📚 參考資源

### 檔案位置
- **腳本檔案**: `System/` 資料夾
- **Device 庫**: `Device/` 資料夾
- **API 庫**: `API/` 資料夾
- **日誌檔案**: `Log/` 資料夾

### 相關檔案
- `System.ini` - 系統配置
- `Global.ini` - 全域參數
- `TestItemCode*.xlsx` - 測試項目代碼
- `*TestFlow.xlsx` - 測試流程腳本

### 新版本文件
- `Centimani instrument parameter -Ver1.71(20230411).xlsx` - **最新儀器參數**
- `dbaccess2_iPLAS_Argument_List_v2.0.xlsx` - **iPLAS參數列表v2.0**
- `Centimani Script User Guide(202230104).xlsx` - **腳本用戶指南**

---

## 🔄 版本更新記錄

| 版本 | 日期 | 更新內容 |
|------|------|----------|
| 2.5 | 2025-08-12 | **腳本修改邏輯更新**: 新增正確的腳本修改邏輯和常見錯誤避免方法 |
| - | - | **新增**: 腳本修改的關鍵步驟和完整流程 |
| - | - | **新增**: 常見錯誤和避免方法詳細說明 |
| - | - | **新增**: 實際修改操作指南和檢查清單 |
| - | - | **重要提醒**: 複製檔案只是第一步，必須實際修改腳本內容 |
| 2.4 | 2025-08-12 | **腳本產生策略更新**: 新增完整的腳本產生策略和決策流程 |
| - | - | **新增**: 修改現有腳本的核心原則和優勢分析 |
| - | - | **新增**: 腳本產生的決策流程和具體標準 |
| - | - | **新增**: 修改策略分類和注意事項 |
| - | - | **新增**: 技術優勢、維護優勢、品質優勢詳細說明 |
| 2.3 | 2025-08-12 | **INI處理邏輯更新**: 新增INI配置文件處理的完整指南 |
| - | - | **新增**: INI完整COPY策略和針對性修改原則 |
| - | - | **新增**: INI處理的5個具體步驟和操作流程 |
| - | - | **新增**: 常見錯誤避免方法和最佳實踐建議 |
| - | - | **新增**: 配置完整性驗證和版本管理策略 |
| 2.2 | 2025-08-12 | **完整工作表分析**: 新增VALO360腳本所有6個工作表深度分析 |
| - | - | **新增**: Properties、DUTs、Switch、Instrument、MB、TEMP完整分析 |
| - | - | **新增**: 整體架構設計和分層結構理解 |
| - | - | **新增**: AI腳本開發完整思考流程和階段劃分 |
| - | - | **新增**: 腳本開發檢查清單和最佳實踐原則 |
| - | - | **新增**: 模組化設計、配置驅動、錯誤處理等核心原則 |
| 2.1 | 2025-08-12 | **實例分析更新**: 新增VALO360腳本深度分析 |
| - | - | **新增**: VALO360_TestFlow_20250318_MB_ER2.xlsx 完整欄位分析 |
| - | - | **新增**: 24個Phase的腳本邏輯理解 |
| - | - | **新增**: 新腳本生成規則和最佳實踐 |
| - | - | **新增**: 統一腳本分析器和生成器工具推薦 |
| 2.0 | 2025-08-11 | **重大更新**: 整合2023年平台培訓新版本內容 |
| - | - | **新增**: Ver1.71儀器參數支援 (36個工作表) |
| - | - | **新增**: iPLAS參數列表v2.0完整參考 |
| - | - | **新增**: 腳本編輯工具增強功能 |
| - | - | **更新**: 版本比較和相容性說明 |
| 1.0 | 2025-08-11 | 基於PPT分析結果創建完整速查表 |
| - | - | 包含所有19頁PPT的關鍵資訊 |
| - | - | 整合系統配置、腳本編輯、工具使用等完整指南 |

---

## 📋 版本對照表

### PPT版本對照
| 版本 | 日期 | 頁數 | 主要差異 |
|------|------|------|----------|
| v1.4 | 2018-04-27 | 19 | 基礎版本 |
| (20210217) | 2021-02-17 | 19 | 內容優化，格式改進 |

### 儀器參數版本對照
| 版本 | 日期 | 工作表數 | 主要改進 |
|------|------|----------|----------|
| Ver1.65 | 2023-01-04 | 基礎 | 基本儀器支援 |
| **Ver1.71** | **2023-04-11** | **36** | **大幅擴展，新增多種儀器** |

### iPLAS版本對照
| 版本 | 日期 | 功能 | 主要改進 |
|------|------|------|----------|
| v1.x | 早期版本 | 基本功能 | 基礎iPLAS支援 |
| **v2.0** | **2023-07-18** | **完整參數列表** | **新增範例和最佳實踐** |

---

*本速查表基於 "Centimani - How to edit scripts (20210217).pptx" 和 "Centimani instrument parameter -Ver1.71(20230411).xlsx" 分析結果製作，提供完整的腳本編輯參考資訊，包含2023年平台培訓的最新功能和改進。* 

---

## 🔍 VALO360腳本實例分析 (2025-08-12)

### 分析檔案
- **檔案名稱**: `VALO360_TestFlow_20250318_MB_ER2.xlsx`
- **專案類型**: VALO360主機板功能測試
- **分析日期**: 2025-08-12
- **分析工具**: 統一腳本分析器

### 📊 腳本結構概覽
- **總工作表數**: 6個 (Properties, DUTs, Switch, Instrument, MB, TEMP)
- **總行數**: 218行
- **總列數**: 256列
- **總命令數**: 172個
- **CLI命令**: 64個 (37.21%)
- **設備調用**: 108個 (62.79%)
- **Phase數量**: 24個
- **複雜度分數**: 69/100

### 🎯 完整工作表分析

#### **1. Properties 工作表**
- **類型**: properties (屬性配置)
- **行數**: 3行，列數: 2列
- **功能**: 定義腳本基本屬性和配置
- **設計**: Name-Value對的標準格式，支援擴展

#### **2. DUTs 工作表**
- **類型**: instrument (設備配置)
- **行數**: 2行，列數: 18列
- **功能**: 定義被測設備的配置和連接設定
- **特色**: 支援多DUT、SFIS整合、條碼掃描、最多10個連接配置

#### **3. Switch 工作表**
- **類型**: switch (開關配置)
- **行數**: 1行，列數: 7列
- **功能**: 定義開關設備的配置和控制
- **特色**: 模組化設計、版本控制、損耗補償

#### **4. Instrument 工作表**
- **類型**: instrument (儀器配置)
- **行數**: 40行，列數: 9列
- **功能**: 定義測試儀器的配置和功能
- **特色**: 功能導向、開關整合、多站支援、子設備支援

#### **5. MB 工作表 (主要測試流程)**
- **類型**: instrument (主要測試流程)
- **行數**: 159行，列數: 256列
- **功能**: 定義主機板功能測試的完整流程
- **特色**: 24個Phase、複雜執行邏輯、變數管理、條件分支

#### **6. TEMP 工作表 (溫度測試流程)**
- **類型**: instrument (溫度測試流程)
- **行數**: 13行，列數: 256列
- **功能**: 定義溫度相關的測試流程
- **特色**: 專用流程、簡化設計、設備導向

### 🏗️ 整體架構設計

#### **分層結構**
1. **配置層**: Properties、DUTs、Switch、Instrument
2. **執行層**: MB、TEMP
3. **整合層**: 工作表間的數據和邏輯整合

#### **設計原則**
- **模組化設計**: 每個工作表專注於特定功能
- **配置驅動**: 使用配置檔案控制行為
- **靈活性設計**: 支援多種執行模式和條件分支
- **標準化介面**: 工作表間通過標準介面整合

### 🎯 欄位功能分析

#### **[Index_149]**
- **範例值**: 2, 3, 4, 5...
- **推測功能**: 測試項目的序號索引，用於標識每個測試步驟的執行順序
- **為什麼要這樣寫**: 提供測試步驟的執行順序，便於追蹤和除錯
- **如何在新腳本中生成相同結構**: 從1開始遞增編號，確保每個測試項目都有唯一的索引

#### **[Phase]**
- **範例值**: "0", "1", "4", "5", "6", "7", "10", "20"
- **推測功能**: 測試階段分類，控制測試的執行順序和邏輯分組
- **為什麼要這樣寫**: 
  - Phase 0: 系統初始化和登入階段
  - Phase 1-9: 基本功能測試階段
  - Phase 10-19: 進階功能測試階段
  - Phase 20+: 特殊測試或驗證階段
- **如何在新腳本中生成相同結構**: 按照測試邏輯分組，Phase 0用於初始化，Phase 1+用於實際測試項目

#### **[Title]**
- **範例值**: "Check Valo360 model", "SET iplus Modelname_Valo360_5G", "Check E compass"
- **推測功能**: 測試項目的描述性標題，說明該步驟的測試目的
- **為什麼要這樣寫**: 提供人類可讀的測試描述，便於工程師理解和維護腳本
- **如何在新腳本中生成相同結構**: 使用清晰、簡潔的英文描述，說明測試動作和目標

#### **[Marco]**
- **範例值**: (大部分為空)
- **推測功能**: 指向宏定義或子腳本的引用
- **為什麼要這樣寫**: 當測試項目需要重複使用時，可以通過宏來避免重複編寫
- **如何在新腳本中生成相同結構**: 對於重複的測試序列，定義宏並在此欄位引用

#### **[Instrument]**
- **範例值**: "DMM.MeasureV", "Utility.PING", "ObtainDevice"
- **推測功能**: 指定要使用的儀器或工具函數
- **為什麼要這樣寫**: 告訴系統使用哪個儀器或工具來執行測試
- **如何在新腳本中生成相同結構**: 根據測試需求選擇適當的儀器函數，格式為 "儀器名.函數名"

#### **[Switch]**
- **範例值**: (大部分為空)
- **推測功能**: 指定開關配置，用於切換測試路徑
- **為什麼要這樣寫**: 當需要根據條件選擇不同測試路徑時使用
- **如何在新腳本中生成相同結構**: 根據測試邏輯需要設定開關條件

#### **[Send]**
- **範例值**: 
  - CLI命令: "UART@diag -s sku N3C2401C\\r\\n"
  - 設備調用: ":Delay,\"2000\"", ":GetVal,\"$G_VALO360_MODEL\""
- **推測功能**: 要執行的具體命令或指令
- **為什麼要這樣寫**: 
  - CLI命令用於與DUT通訊
  - 設備調用用於控制測試設備或執行系統功能
- **如何在新腳本中生成相同結構**: 根據測試需求選擇CLI命令或設備調用，CLI命令格式為 "連接名@命令"，設備調用格式為 ":函數名,參數"

#### **[Reply]**
- **範例值**: "@Version:", "@SELFTEST:PASS", "@ECOMPASS:PASS"
- **推測功能**: 預期的回應或結果
- **為什麼要這樣寫**: 用於驗證命令是否執行成功，確保測試步驟按預期進行
- **如何在新腳本中生成相同結構**: 根據命令的預期回應設定，使用@符號表示包含匹配

#### **[EndPrompt]**
- **範例值**: (大部分為空)
- **推測功能**: 結束回應的提示字串
- **為什麼要這樣寫**: 當回應較長時，用於標識回應的結束點
- **如何在新腳本中生成相同結構**: 對於長回應的命令，設定明確的結束標識

#### **[Ref]**
- **範例值**: "version", "voltage", "$G_VALO360_MODEL"
- **推測功能**: 將執行結果存入變數，供後續步驟使用
- **為什麼要這樣寫**: 實現測試步驟間的數據傳遞和結果驗證
- **如何在新腳本中生成相同結構**: 為需要後續使用的測試結果設定變數名，全域變數使用$前綴

#### **[Validation]**
- **範例值**: "(voltage,%f,4.75,5.25)", "(*(P1V1_TP2500),%f,1.06,1.17)"
- **推測功能**: 驗證測試結果是否在預期範圍內
- **為什麼要這樣寫**: 確保測試結果符合規格要求，自動判斷PASS/FAIL
- **如何在新腳本中生成相同結構**: 格式為 "(變數名,格式,下限,上限)"，格式包括%f(浮點數)、%d(整數)、%s(字串)

#### **[Prompt]**
- **範例值**: (大部分為空)
- **推測功能**: 等待特定提示再執行命令
- **為什麼要這樣寫**: 用於交互式測試，確保時序正確
- **如何在新腳本中生成相同結構**: 對於需要等待回應的命令，設定預期的提示字串

#### **[Waiting]**
- **範例值**: "3000", "5000", "10000"
- **推測功能**: 等待DUT回應的時間(毫秒)
- **為什麼要這樣寫**: 確保有足夠時間等待DUT處理命令並回應
- **如何在新腳本中生成相同結構**: 根據命令複雜度和DUT處理能力設定適當的超時時間

#### **[ExecMode]**
- **範例值**: "0", "1", "2:0", "4:1,6", "6", "8"
- **推測功能**: 執行模式控制，決定測試步驟的執行邏輯
- **為什麼要這樣寫**: 
  - 0: 正常模式
  - 1: 總是執行
  - 2: 重試模式
  - 4: 條件執行
  - 6: 失敗時執行
  - 8: SFIS啟用時執行
- **如何在新腳本中生成相同結構**: 根據測試邏輯需求選擇適當的執行模式

#### **[Description]**
- **範例值**: "Check Valo360 model", "Check E compass selftest", "Check E compass result"
- **推測功能**: 測試步驟的詳細說明
- **為什麼要這樣寫**: 提供測試步驟的完整描述，便於維護和除錯
- **如何在新腳本中生成相同結構**: 使用清晰的中文描述，說明測試動作、目標和預期結果

#### **[TestID]**
- **範例值**: "WUOT001", "WUOT002", "WUOT003"
- **推測功能**: 測試項目的唯一識別碼
- **為什麼要這樣寫**: 用於追蹤測試結果、生成報告和對應測試規格
- **如何在新腳本中生成相同結構**: 使用標準的測試項目代碼格式，確保與測試規格文件一致

### 🧠 腳本邏輯理解

#### **Phase 0 (初始化階段)**
- **功能**: 系統登入、SFIS檢查、網路連線測試
- **關鍵步驟**: 
  - 顯示ISN號碼
  - 斷開UART連接
  - SFIS路由檢查
  - 確認SD和SIM卡
  - 治具通訊測試
  - 網路連線測試
  - 重新連接UART
  - 設定SKU

#### **Phase 1-9 (基本功能測試)**
- **功能**: 模型識別、基本硬體測試
- **關鍵步驟**:
  - 檢查VALO360模型
  - 設定不同模型配置 (5G/WiFi/無電池)
  - 網路狀態檢查
  - 藍牙初始化測試

#### **Phase 10+ (進階功能測試)**
- **功能**: IMU測試、按鈕測試、特殊功能驗證
- **關鍵步驟**:
  - IMU磁力計自檢
  - IMU狀態檢查
  - 硬體按鈕測試
  - 軟體按鈕測試

### 📋 新腳本生成規則

#### **1. 欄位結構設計**
- **保持完整性**: 確保所有必要欄位都存在且順序正確
- **索引管理**: Index欄位從1開始遞增，確保唯一性
- **Phase規劃**: 按照邏輯分組設計Phase值，0用於初始化

#### **2. 命令類型選擇**
- **CLI命令**: 用於與DUT通訊，格式為 "連接名@命令"
- **設備調用**: 用於控制測試設備，格式為 ":函數名,參數"
- **混合使用**: 根據測試需求選擇適當的命令類型

#### **3. 變數管理策略**
- **Ref欄位**: 為需要後續使用的測試結果設定變數名
- **全域變數**: 使用$前綴，如 "$G_VALO360_MODEL"
- **區域變數**: 使用普通名稱，如 "version", "voltage"

#### **4. 驗證機制設計**
- **Validation格式**: "(變數名,格式,下限,上限)"
- **格式類型**: %f(浮點數)、%d(整數)、%s(字串)
- **範圍設定**: 根據產品規格設定上下限

#### **5. 執行控制邏輯**
- **ExecMode選擇**: 根據測試邏輯需求選擇執行模式
- **條件執行**: 使用ExecMode 4實現複雜的條件邏輯
- **重試機制**: 使用ExecMode 2實現失敗重試

#### **6. 測試項目設計**
- **TestID命名**: 使用標準的測試項目代碼格式
- **Title描述**: 使用清晰、簡潔的英文描述
- **Description說明**: 提供詳細的中文說明

### 🔧 實用工具推薦

#### **腳本分析工具**
- **統一腳本分析器**: `unified_centimani_script_analyzer.py`
- **功能**: 分析腳本結構、識別類型、生成報告

#### **腳本生成工具**
- **統一腳本生成器**: `unified_centimani_script_generator.py`
- **功能**: 生成新腳本、修改模板、創建配置檔案

#### **參考文件**
- **腳本編輯速查表**: 本文件
- **AI使用指南**: `AI_USAGE_GUIDE.md`
- **腳本生成邏輯**: `AI_SCRIPT_GENERATION_LOGIC_REFERENCE.md`

### 🤖 AI腳本開發思考流程

#### **階段1: 需求分析與架構設計**
1. **理解測試需求**
   - 分析需要測試的功能和硬體
   - 確定測試的複雜度和範圍
   - 識別必要的測試儀器和設備

2. **設計腳本架構**
   - 決定需要哪些工作表類型
   - 規劃工作表間的數據流
   - 設計Phase結構和執行邏輯

3. **選擇參考模板**
   - 尋找相似功能的現有腳本
   - 分析其結構和設計模式
   - 確定可以重用的組件

#### **腳本產生策略：修改現有腳本**
**核心原則：不從零開始，而是複製現有腳本並修改**

**為什麼選擇修改現有腳本？**
1. **遵循"複製現有腳本"的核心原則**
   - 不從零生成新腳本
   - 改為「複製現有腳本」並修改測項
   - 腳本模板可以使用「任何版本的腳本」
   - 保持原有工作表與欄位結構，僅調整必要內容

2. **避免重複造輪子**
   - 已經驗證過的結構和邏輯
   - 包含完整的配置和設定
   - 經過實際測試和除錯
   - 符合專案的標準規範

3. **保持一致性**
   - 維持與現有腳本的結構一致性
   - 使用相同的配置格式和變數引用
   - 遵循相同的設計模式和最佳實踐
   - 便於後續維護和更新

**具體操作流程：**
1. **選擇合適的參考腳本**：尋找功能相似的現有腳本
2. **完整複製腳本檔案**：複製整個Excel腳本和相關INI檔案
3. **分析腳本結構**：使用統一腳本分析器理解結構
4. **尋找其他腳本範例**：找到包含目標測試項目的腳本範例
5. **實際修改腳本內容**：在Excel中實際刪除不需要的測試項目，COPY相關欄位
6. **驗證和測試**：檢查完整性、驗證配置、測試執行邏輯

**重要提醒：複製檔案只是第一步，必須實際修改腳本內容！**

**修改策略分類：**
- **小修改**：調整測試參數、更新配置值、修改測試項目
- **中等修改**：添加新的測試項目、調整Phase結構、修改執行邏輯
- **大修改**：改變測試架構、添加新的工作表、重新設計執行流程

**腳本產生的決策流程：**
```
需要新腳本？
├─ 是 → 尋找相似功能的現有腳本
│   ├─ 找到 → 複製並修改
│   └─ 沒找到 → 尋找功能相近的腳本
└─ 否 → 直接修改現有腳本

修改策略：
├─ 小修改 → 直接修改現有腳本
├─ 中等修改 → 複製後修改
└─ 大修改 → 複製後大幅修改
```

**具體決策標準：**
- **小修改（直接修改）**：調整測試參數、更新配置值、修改測試項目
- **中等修改（複製後修改）**：添加新的測試項目、調整Phase結構、修改執行邏輯
- **大修改（複製後大幅修改）**：改變測試架構、添加新的工作表、重新設計執行流程

**修改現有腳本的優勢：**
1. **技術優勢**：結構完整性、配置一致性、邏輯驗證、錯誤處理
2. **維護優勢**：學習成本低、除錯容易、更新簡單、文檔完整
3. **品質優勢**：穩定性高、相容性好、標準化、可重用性

**注意事項：**
1. **備份原始腳本**：修改前必須備份，防止錯誤
2. **記錄修改內容**：記錄修改原因、時間、版本、結果
3. **驗證修改正確性**：使用分析器檢查、執行測試、對比確認
4. **保持向後相容性**：不破壞現有配置、維持變數格式、保持整合關係

### **正確的腳本修改邏輯（重要！）**

#### **常見錯誤和避免方法**
```
❌ 錯誤做法：只複製檔案，以為完成任務
✅ 正確做法：複製後必須實際修改腳本內容

❌ 錯誤做法：保留所有測試項目
✅ 正確做法：只保留需要的測試項目，刪除不需要的

❌ 錯誤做法：不尋找其他腳本範例
✅ 正確做法：尋找包含目標測試項目的腳本範例，COPY相關欄位
```

#### **腳本修改的推理邏輯（重要學習！）**
```
我的學習過程：
1. 第一次錯誤：只複製檔案，沒有修改內容
   - 結果：兩個腳本一模一樣，包含所有測試項目
   - 問題：沒有理解"複製現有腳本並修改"的真正含義

2. 第二次進步：創建修改工具，實際修改內容
   - 結果：腳本大小從74KB減少到33KB，行數從322行減少到104行
   - 進步：理解了必須實際修改腳本內容，不能只複製檔案

3. 第三次發現：修改後腳本可能還有問題
   - 問題：電壓測試腳本沒有測項
   - 學習：修改工具可能有邏輯錯誤，需要進一步驗證和改進

關鍵學習點：
- 複製檔案只是第一步，不是完成
- 必須實際修改腳本內容，刪除不需要的測試項目
- 修改後要驗證結果，確保腳本確實包含需要的功能
- 修改工具可能有bug，需要不斷改進和驗證
```

#### **腳本修改的完整流程**
```
步驟1: 複製腳本作為模板
步驟2: 尋找其他腳本範例，找到目標測試項目的欄位
步驟3: 實際修改腳本內容（在Excel中操作）
步驟4: 驗證修改結果
```

#### **實際修改操作**
```
在Excel中實際操作：
1. 打開複製的腳本檔案
2. 切換到測試工作表（如MB工作表）
3. 刪除不需要的測試項目行
4. 從其他腳本COPY相關的欄位內容
5. 調整參數和變數引用
6. 保存修改
```

#### **修改檢查清單**
```
修改前檢查：
- [ ] 已複製腳本作為模板
- [ ] 已找到其他腳本範例
- [ ] 已識別需要COPY的欄位

修改中檢查：
- [ ] 已刪除不需要的測試項目
- [ ] 已COPY相關欄位到目標腳本
- [ ] 已調整參數和變數引用

修改後檢查：
- [ ] 腳本只包含需要的測試項目
- [ ] 測試邏輯正確
- [ ] 配置完整
```

#### **階段2: 配置工作表設計**
1. **Properties工作表**
   - 設定基本屬性：Version, Project, CreateDate, Author
   - 使用標準的Name-Value對格式
   - 支援未來的擴展需求

2. **DUTs工作表**
   - 配置被測設備的基本信息
   - 設定SFIS整合和條碼掃描
   - 配置多個連接類型（UART, SSH, TCP等）

3. **Switch工作表**
   - 配置開關設備和控制庫
   - 設定開關參數和損耗值
   - 支援多站別掛載

4. **Instrument工作表**
   - 配置測試儀器和功能
   - 設定儀器參數和開關配線
   - 支援多站別和多功能

5. **INI配置文件處理**
   - **完整COPY策略**: 先完整複製整個INI檔案
   - **針對性修改**: 只修改腳本實際需要的配置項
   - **保持完整性**: 其他配置項保持不變，確保系統完整性
   - **配置一致性**: 維持與原始腳本的配置一致性

#### **階段3: 測試流程設計**
1. **Phase結構規劃**
   - Phase 0: 系統初始化
   - Phase 1-9: 基本功能測試
   - Phase 10-19: 進階功能測試
   - Phase 20+: 特殊測試驗證

2. **命令類型選擇**
   - CLI命令：用於與DUT通訊
   - 設備調用：用於控制測試設備
   - 混合使用：根據測試需求選擇

3. **變數和驗證設計**
   - 全域變數：使用$前綴，跨工作表共享
   - 區域變數：使用普通名稱，工作表內使用
   - 驗證機制：使用Validation欄位驗證結果

#### **階段4: 執行邏輯設計**
1. **ExecMode選擇**
   - 0: 正常執行模式
   - 1: 總是執行
   - 2: 重試模式
   - 4: 條件執行
   - 6: 失敗時執行
   - 8: SFIS啟用時執行

2. **錯誤處理設計**
   - 重試機制：使用ExecMode 2實現
   - 條件分支：使用ExecMode 4實現
   - 用戶交互：使用確認框和提示

3. **數據流設計**
   - 變數傳遞：使用Ref欄位存儲結果
   - 數據驗證：使用Validation欄位驗證
   - 狀態管理：使用全域變數管理狀態

#### **階段5: 整合和優化**
1. **工作表整合**
   - 確保工作表間的數據一致性
   - 使用標準的變數引用格式
   - 支援配置的動態更新

2. **性能優化**
   - 優化命令執行順序
   - 減少不必要的等待時間
   - 優化變數使用和內存管理

3. **用戶體驗優化**
   - 提供清晰的提示和確認
   - 設計友好的錯誤信息
   - 支援測試進度顯示

### 📋 AI腳本開發檢查清單

#### **架構設計檢查**
- [ ] 工作表類型選擇是否合適？
- [ ] Phase結構是否邏輯清晰？
- [ ] 工作表間的數據流是否暢通？

#### **配置設計檢查**
- [ ] 所有必要的配置是否完整？
- [ ] 變數引用是否正確？
- [ ] 連接設定是否合理？

#### **測試流程檢查**
- [ ] 測試順序是否合理？
- [ ] 錯誤處理是否完善？
- [ ] 驗證機制是否有效？

#### **整合測試檢查**
- [ ] 腳本是否能正常執行？
- [ ] 所有工作表是否正確整合？
- [ ] 測試結果是否準確？

### 🎯 AI腳本開發最佳實踐

#### **1. 模組化設計原則**
- 將複雜功能分解為簡單模組
- 每個工作表專注於特定功能
- 使用標準介面進行整合

#### **2. 配置驅動原則**
- 使用配置文件控制腳本行為
- 支援動態參數設定
- 實現配置與邏輯分離

#### **3. INI檔案處理原則**
- **完整COPY優先**: 先完整複製整個INI檔案，保持配置完整性
- **針對性修改**: 只修改腳本實際需要的配置項，避免破壞系統配置
- **配置一致性**: 維持與原始腳本的配置一致性，確保執行環境完整
- **漸進式調整**: 根據腳本需求逐步調整配置，而不是重新創建

#### **4. 錯誤處理原則**
- 設計完善的錯誤檢測機制
- 提供清晰的錯誤信息
- 支援自動重試和恢復

#### **5. 用戶體驗原則**
- 提供清晰的執行進度
- 設計友好的交互介面
- 支援測試結果的可視化

#### **6. 維護性原則**
- 使用清晰的命名規範
- 提供詳細的文檔說明
- 支援版本控制和更新

### 📋 INI配置文件處理詳細指南

#### **INI處理的核心原則**
```
原則1: 完整COPY優先
- 不要重新創建INI檔案
- 先完整複製原始INI檔案
- 保持所有原始配置項

原則2: 針對性修改
- 分析腳本中引用的變數
- 識別需要修改的配置項
- 只修改腳本實際使用的部分

原則3: 保持完整性
- 其他配置項保持不變
- 確保系統配置的完整性
- 避免破壞現有的系統設定
```

#### **INI處理的具體步驟**

##### **步驟1: 完整複製INI檔案**
```
操作：複製整個INI檔案到新位置
目的：保持配置的完整性和一致性
注意：不要遺漏任何配置項
```

##### **步驟2: 分析腳本變數引用**
```
分析腳本中的變數引用：
- 查找所有 *$(VAR_NAME) 格式的變數
- 識別腳本實際使用的配置項
- 記錄需要修改的變數名稱
```

##### **步驟3: 識別需要修改的配置項**
```
需要修改的配置項類型：
- 設備IP地址 (如 DUTIP, PCIP)
- 連接參數 (如 COM端口, 波特率)
- 測試參數 (如 超時時間, 重試次數)
- 專案特定配置 (如 SKU, 模型名稱)
```

##### **步驟4: 針對性修改配置**
```
修改策略：
- 只修改腳本實際使用的配置項
- 保持其他配置項的原始值
- 使用腳本需求的新值替換
- 驗證修改後的配置格式正確性
```

##### **步驟5: 驗證配置完整性**
```
驗證項目：
- 所有腳本引用的變數都有對應配置
- 配置值的格式和類型正確
- 系統配置的完整性沒有被破壞
- 腳本能夠正常讀取配置值
```

#### **INI處理的常見錯誤和避免方法**

##### **錯誤1: 重新創建INI檔案**
```
問題：完全重新創建INI檔案，遺漏重要配置
避免：始終先完整複製，再進行修改
```

##### **錯誤2: 過度修改配置**
```
問題：修改了腳本不需要的配置項
避免：只修改腳本實際引用的變數
```

##### **錯誤3: 破壞系統配置**
```
問題：修改了系統級別的配置項
避免：識別並保護系統配置項
```

##### **錯誤4: 配置格式錯誤**
```
問題：修改後的配置格式不正確
避免：保持INI檔案的標準格式
```

#### **INI處理的最佳實踐**

##### **實踐1: 使用配置模板**
```
- 建立標準的INI配置模板
- 包含常用的配置項和預設值
- 便於快速創建新的配置檔案
```

##### **實踐2: 配置版本管理**
```
- 記錄INI配置的修改歷史
- 使用版本號管理配置變更
- 支援配置的回滾和恢復
```

##### **實踐3: 配置驗證機制**
```
- 建立配置驗證工具
- 檢查配置項的完整性和正確性
- 自動檢測配置問題
```

##### **實踐4: 配置文檔化**
```
- 為每個配置項提供說明
- 記錄配置項的用途和影響
- 便於後續維護和修改

---

*本分析基於VALO360_TestFlow_20250318_MB_ER2.xlsx腳本檔案，使用統一腳本分析器進行深度分析，為腳本開發和維護提供實用參考。* 