# KANGAROO專案腳本邏輯分析
## KANGAROO Project Script Logic Analysis

### 📋 文件概述

本文檔深入分析KANGAROO專案所有腳本檔案的欄位邏輯、關聯關係和AI腳本生成邏輯。透過詳細的欄位分析，理解每個腳本為什麼這樣設計，以及如何生成相同格式的腳本。

**版本**: 2.2.5  
**創建日期**: 2025-08-11  
**更新日期**: 2025-08-11  
**狀態**: 🆕 新增索引

---

## 🦘 KANGAROO專案腳本總覽

### **專案特點**
- **專案類型**: 多設備測試、複雜儀器配置、多功能整合
- **腳本數量**: 11個腳本檔案
- **主要功能**: WiFi/藍牙測試、固件升級、主機板測試、OQC檢查
- **複雜度**: 高 - 支援多設備並行測試和複雜測試流程

### **腳本列表**
1. **Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx**
2. **Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX**
3. **Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX**
4. **Test Item Code V2.04_20250310.xlsx**
5. **Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx**
6. **Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx**
7. **Pega_Kangaroo_TestFlow-Final Check_MP_20250415_CBNGSIMSLOT1.xlsx**
8. **Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx**
9. **Kangaroo_MP_AIR_TestFlow_20250326C.xlsx**
10. **Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx**

---

## 🔍 腳本1: Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx

### **腳本概述**
- **功能**: 多設備SIM卡和固件升級測試
- **工作表數量**: 5個
- **主要特點**: 支援多DUT並行測試，整合SIM卡測試和固件升級

### **工作表結構分析**

#### **工作表1: Properties (配置屬性)**
**為什麼這樣設計**:
- **集中配置管理**: 所有全局參數集中在一個工作表，便於維護和修改
- **參數標準化**: 統一的參數格式和命名規範
- **版本控制**: 便於追蹤參數變更和版本管理

**關鍵欄位邏輯**:
```
欄位名稱: Project_Name
- 為什麼這樣寫: 專案識別，用於腳本分類和管理
- 數據來源: 手動設定，根據專案需求
- 關聯關係: 與其他工作表的專案參數相關聯
- 驗證規則: 必填，不能為空

欄位名稱: Test_Environment
- 為什麼這樣寫: 測試環境配置，影響測試參數和儀器設定
- 數據來源: 根據實際測試環境選擇
- 關聯關係: 影響Instrument工作表的儀器配置
- 驗證規則: 從預定義選項中選擇

欄位名稱: DUT_Count
- 為什麼這樣寫: 多設備測試的核心參數，決定並行測試數量
- 數據來源: 根據測試需求設定
- 關聯關係: 影響DUTs工作表的設備配置和Switch工作表的路徑設定
- 驗證規則: 數值範圍1-8，必須為整數
```

#### **工作表2: Instrument (儀器配置)**
**為什麼這樣設計**:
- **儀器統一管理**: 所有儀器配置集中在一個工作表，便於儀器管理
- **配置標準化**: 統一的儀器配置格式和參數
- **多儀器支援**: 支援多種儀器類型的配置

**關鍵欄位邏輯**:
```
欄位名稱: Instrument_Type
- 為什麼這樣寫: 儀器類型識別，決定後續配置參數
- 數據來源: 從預定義儀器類型中選擇
- 關聯關係: 影響後續的連接參數和校準參數
- 驗證規則: 必須從預定義列表中選擇

欄位名稱: Connection_Parameters
- 為什麼這樣寫: 儀器連接參數，確保儀器正確連接
- 數據來源: 根據儀器類型和連接方式設定
- 關聯關係: 與Switch工作表的開關配置相關聯
- 驗證規則: 格式必須符合儀器要求

欄位名稱: Calibration_Parameters
- 為什麼這樣寫: 儀器校準參數，確保測試精度
- 數據來源: 根據儀器校準要求設定
- 關聯關係: 影響測試結果的準確性
- 驗證規則: 數值範圍必須在儀器規格內
```

#### **工作表3: Switch (開關矩陣)**
**為什麼這樣設計**:
- **路徑管理**: 管理多設備測試的路徑切換
- **開關控制**: 控制測試信號的路由和分配
- **錯誤處理**: 提供路徑錯誤檢測和恢復機制

**關鍵欄位邏輯**:
```
欄位名稱: Switch_Matrix_Configuration
- 為什麼這樣寫: 開關矩陣配置，定義測試路徑
- 數據來源: 根據DUT數量和測試需求設定
- 關聯關係: 與DUTs工作表的設備配置相關聯
- 驗證規則: 路徑配置必須有效且不衝突

欄位名稱: Path_Status
- 為什麼這樣寫: 路徑狀態監控，確保路徑正常工作
- 數據來源: 系統自動檢測和更新
- 關聯關係: 影響測試執行的成功與否
- 驗證規則: 狀態必須為"Active"才能執行測試

欄位名稱: Error_Handling
- 為什麼這樣寫: 錯誤處理機制，提供路徑故障恢復
- 數據來源: 預定義的錯誤處理策略
- 關聯關係: 與測試流程的穩定性相關
- 驗證規則: 必須有有效的錯誤處理策略
```

#### **工作表4: DUTs (設備配置)**
**為什麼這樣設計**:
- **多設備支援**: 支援多個DUT的同時配置
- **設備管理**: 統一管理所有測試設備的參數
- **並行測試**: 支援多設備的並行測試

**關鍵欄位邏輯**:
```
欄位名稱: DUT_ID
- 為什麼這樣寫: 設備唯一識別，用於設備管理和測試追蹤
- 數據來源: 系統自動分配或手動設定
- 關聯關係: 與測試結果的設備對應
- 驗證規則: 必須唯一，不能重複

欄位名稱: Device_Type
- 為什麼這樣寫: 設備類型識別，決定測試參數和流程
- 數據來源: 從預定義設備類型中選擇
- 關聯關係: 影響測試項目的選擇和參數設定
- 驗證規則: 必須從支援的設備類型中選擇

欄位名稱: Test_Parameters
- 為什麼這樣寫: 設備特定的測試參數，確保測試準確性
- 數據來源: 根據設備類型和測試要求設定
- 關聯關係: 與測試流程的參數配置相關
- 驗證規則: 參數必須在設備規格範圍內
```

#### **工作表5: FWDL (固件下載)**
**為什麼這樣設計**:
- **專用功能**: 專門針對固件下載流程設計
- **流程控制**: 完整的固件下載流程控制
- **進度監控**: 實時監控下載進度和狀態

**關鍵欄位邏輯**:
```
欄位名稱: Download_Process
- 為什麼這樣寫: 下載流程控制，定義下載步驟和順序
- 數據來源: 預定義的下載流程模板
- 關聯關係: 與固件版本和設備類型相關
- 驗證規則: 流程步驟必須完整且順序正確

欄位名稱: Progress_Monitoring
- 為什麼這樣寫: 進度監控，實時追蹤下載狀態
- 數據來源: 系統自動更新
- 關聯關係: 與下載成功率和錯誤處理相關
- 驗證規則: 進度值必須在0-100%範圍內

欄位名稱: Error_Handling
- 為什麼這樣寫: 錯誤處理，提供下載失敗的恢復機制
- 數據來源: 預定義的錯誤處理策略
- 關聯關係: 與下載流程的穩定性相關
- 驗證規則: 必須有有效的錯誤處理策略
```

### **關聯關係分析**

#### **工作表間關聯**
```
Properties → Instrument: 測試環境參數影響儀器配置
Properties → Switch: DUT數量影響開關矩陣配置
Properties → DUTs: 全局參數影響設備配置
Instrument → Switch: 儀器配置影響開關路徑設定
Switch → DUTs: 開關路徑影響設備連接方式
DUTs → FWDL: 設備配置影響固件下載參數
```

#### **外部檔案關聯**
```
關聯檔案: Test Item Code V2.04_20250310.xlsx
關聯原因: 測試項目代碼和參數定義
關聯方式: 引用測試項目代碼和參數
影響範圍: 測試流程和參數設定

關聯檔案: Centimani INI file setting(20210506).xlsx
關聯原因: 系統配置參數和儀器設定
關聯方式: 引用系統配置參數
影響範圍: 儀器配置和系統參數
```

---

## 🔍 腳本2: Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX

### **腳本概述**
- **功能**: WiFi和藍牙校準與驗證測試
- **工作表數量**: 6個
- **主要特點**: 整合WiFi和藍牙測試，包含校準和驗證流程

### **工作表結構分析**

#### **工作表1: Properties (配置屬性)**
**為什麼這樣設計**:
- **無線測試專用**: 專門針對WiFi和藍牙測試的配置參數
- **校準參數整合**: 將WiFi和藍牙的校準參數整合在一起
- **驗證標準統一**: 統一的驗證標準和參數

**關鍵欄位邏輯**:
```
欄位名稱: WiFi_Calibration_Parameters
- 為什麼這樣寫: WiFi校準參數，確保WiFi測試精度
- 數據來源: 根據WiFi標準和測試要求設定
- 關聯關係: 影響WiFi測試的準確性
- 驗證規則: 參數必須符合WiFi標準規範

欄位名稱: Bluetooth_Calibration_Parameters
- 為什麼這樣寫: 藍牙校準參數，確保藍牙測試精度
- 數據來源: 根據藍牙標準和測試要求設定
- 關聯關係: 影響藍牙測試的準確性
- 驗證規則: 參數必須符合藍牙標準規範

欄位名稱: Verification_Standards
- 為什麼這樣寫: 驗證標準，定義測試通過的標準
- 數據來源: 根據產品規格和測試要求設定
- 關聯關係: 影響測試結果的判定
- 驗證規則: 標準必須明確且可測量
```

#### **工作表2: Instrument (儀器配置)**
**為什麼這樣設計**:
- **無線測試儀器**: 專門針對WiFi和藍牙測試的儀器配置
- **信號分析儀**: 用於信號品質分析和測量
- **校準設備**: 專門的校準設備配置

**關鍵欄位邏輯**:
```
欄位名稱: WiFi_Test_Instrument
- 為什麼這樣寫: WiFi測試儀器配置，確保WiFi測試能力
- 數據來源: 根據WiFi測試需求選擇儀器
- 關聯關係: 與WiFi測試流程相關
- 驗證規則: 儀器必須支援WiFi測試功能

欄位名稱: Bluetooth_Test_Instrument
- 為什麼這樣寫: 藍牙測試儀器配置，確保藍牙測試能力
- 數據來源: 根據藍牙測試需求選擇儀器
- 關聯關係: 與藍牙測試流程相關
- 驗證規則: 儀器必須支援藍牙測試功能

欄位名稱: Signal_Analyzer
- 為什麼這樣寫: 信號分析儀配置，用於信號品質分析
- 數據來源: 根據信號分析需求選擇儀器
- 關聯關係: 與信號品質測試相關
- 驗證規則: 儀器必須支援信號分析功能
```

#### **工作表3: Switch (開關矩陣)**
**為什麼這樣設計**:
- **無線路徑管理**: 管理WiFi和藍牙信號的路徑切換
- **校準路徑**: 專門的校準路徑配置
- **信號路徑**: 信號測試路徑配置

**關鍵欄位邏輯**:
```
欄位名稱: WiFi_Signal_Path
- 為什麼這樣寫: WiFi信號路徑配置，確保WiFi信號正確路由
- 數據來源: 根據WiFi測試需求設定路徑
- 關聯關係: 與WiFi測試流程相關
- 驗證規則: 路徑必須有效且不干擾

欄位名稱: Bluetooth_Signal_Path
- 為什麼這樣寫: 藍牙信號路徑配置，確保藍牙信號正確路由
- 數據來源: 根據藍牙測試需求設定路徑
- 關聯關係: 與藍牙測試流程相關
- 驗證規則: 路徑必須有效且不干擾

欄位名稱: Calibration_Path
- 為什麼這樣寫: 校準路徑配置，用於儀器校準
- 數據來源: 根據校準需求設定路徑
- 關聯關係: 與校準流程相關
- 驗證規則: 路徑必須專用且穩定
```

#### **工作表4: DUTs (設備配置)**
**為什麼這樣設計**:
- **無線模組配置**: 專門針對WiFi和藍牙模組的配置
- **天線配置**: 天線參數和配置設定
- **功率設定**: 發射功率和接收靈敏度設定

**關鍵欄位邏輯**:
```
欄位名稱: WiFi_Module_Configuration
- 為什麼這樣寫: WiFi模組配置，確保WiFi功能正常
- 數據來源: 根據WiFi模組規格設定
- 關聯關係: 與WiFi測試結果相關
- 驗證規則: 配置必須符合WiFi模組規格

欄位名稱: Bluetooth_Module_Configuration
- 為什麼這樣寫: 藍牙模組配置，確保藍牙功能正常
- 數據來源: 根據藍牙模組規格設定
- 關聯關係: 與藍牙測試結果相關
- 驗證規則: 配置必須符合藍牙模組規格

欄位名稱: Antenna_Configuration
- 為什麼這樣寫: 天線配置，影響信號發射和接收
- 數據來源: 根據天線規格和測試需求設定
- 關聯關係: 與信號強度和品質相關
- 驗證規則: 配置必須符合天線規格
```

#### **工作表5: WIFI&BT CAL&VERIF (測試流程)**
**為什麼這樣設計**:
- **整合測試流程**: 將WiFi和藍牙測試整合在一起
- **校準優先**: 先進行校準，再進行驗證
- **流程優化**: 優化測試順序，提高測試效率

**關鍵欄位邏輯**:
```
欄位名稱: WiFi_Calibration_Process
- 為什麼這樣寫: WiFi校準流程，確保WiFi測試精度
- 數據來源: 預定義的WiFi校準流程
- 關聯關係: 與WiFi校準參數相關
- 驗證規則: 流程必須完整且順序正確

欄位名稱: Bluetooth_Calibration_Process
- 為什麼這樣寫: 藍牙校準流程，確保藍牙測試精度
- 數據來源: 預定義的藍牙校準流程
- 關聯關係: 與藍牙校準參數相關
- 驗證規則: 流程必須完整且順序正確

欄位名稱: Function_Verification
- 為什麼這樣寫: 功能驗證，確保WiFi和藍牙功能正常
- 數據來源: 預定義的功能驗證流程
- 關聯關係: 與校準結果相關
- 驗證規則: 驗證項目必須完整且有效
```

#### **工作表6: PathLoss (路徑損耗)**
**為什麼這樣設計**:
- **損耗補償**: 補償信號傳輸過程中的路徑損耗
- **信號強度**: 監控和調整信號強度
- **環境因素**: 考慮環境因素對信號的影響

**關鍵欄位邏輯**:
```
欄位名稱: Loss_Compensation
- 為什麼這樣寫: 損耗補償，確保測試結果準確
- 數據來源: 根據實際測試環境測量
- 關聯關係: 與信號強度測試相關
- 驗證規則: 補償值必須在合理範圍內

欄位名稱: Signal_Strength
- 為什麼這樣寫: 信號強度，監控信號品質
- 數據來源: 儀器測量結果
- 關聯關係: 與測試結果的準確性相關
- 驗證規則: 強度值必須在標準範圍內

欄位名稱: Distance_Compensation
- 為什麼這樣寫: 距離補償，考慮距離對信號的影響
- 數據來源: 根據測試距離計算
- 關聯關係: 與路徑損耗相關
- 驗證規則: 補償值必須與距離成正比
```

### **關聯關係分析**

#### **工作表間關聯**
```
Properties → Instrument: 校準參數影響儀器配置
Properties → Switch: 測試需求影響路徑配置
Instrument → Switch: 儀器配置影響路徑設定
Switch → DUTs: 路徑配置影響設備連接
DUTs → WIFI&BT CAL&VERIF: 設備配置影響測試流程
WIFI&BT CAL&VERIF → PathLoss: 測試流程影響損耗補償
```

#### **外部檔案關聯**
```
關聯檔案: Centimani instrument parameter -Ver1.71(20230411).xlsx
關聯原因: 儀器參數和校準參數定義
關聯方式: 引用儀器參數和校準標準
影響範圍: 儀器配置和校準流程

關聯檔案: Test Item Code V2.04_20250310.xlsx
關聯原因: WiFi和藍牙測試項目定義
關聯方式: 引用測試項目和參數
影響範圍: 測試流程和驗證標準
```

---

## 🤖 AI腳本生成邏輯

### **模板化生成策略**

#### **1. 標準工作表模板**
```
Properties工作表模板:
- 專案參數區塊: Project_Name, Test_Environment, DUT_Count
- 測試參數區塊: Test_Type, Test_Standard, Test_Duration
- 配置參數區塊: System_Config, Network_Config, Security_Config

Instrument工作表模板:
- 儀器識別區塊: Instrument_Type, Model_Number, Serial_Number
- 連接參數區塊: Connection_Type, IP_Address, Port_Number
- 校準參數區塊: Calibration_Date, Calibration_Parameters, Status

Switch工作表模板:
- 開關配置區塊: Switch_Matrix, Path_Configuration, Status_Control
- 路徑管理區塊: Path_Definition, Routing_Logic, Error_Handling
- 監控區塊: Path_Monitoring, Performance_Metrics, Alert_System

DUTs工作表模板:
- 設備識別區塊: DUT_ID, Device_Type, Model_Number
- 配置參數區塊: Test_Parameters, Calibration_Data, Status_Info
- 連接信息區塊: Connection_Type, Port_Number, IP_Address
```

#### **2. 專用工作表模板**
```
FWDL工作表模板:
- 下載流程區塊: Download_Process, Progress_Monitoring, Error_Handling
- 版本管理區塊: Firmware_Version, Update_History, Rollback_Plan
- 安全控制區塊: Security_Check, Authentication, Encryption

WIFI&BT CAL&VERIF工作表模板:
- 校準流程區塊: Calibration_Process, Parameter_Setting, Result_Validation
- 功能驗證區塊: Function_Test, Performance_Test, Quality_Check
- 結果記錄區塊: Test_Results, Pass_Fail_Criteria, Improvement_Suggestions

PathLoss工作表模板:
- 損耗補償區塊: Loss_Compensation, Signal_Strength, Distance_Compensation
- 環境因素區塊: Environmental_Factors, Temperature_Effect, Humidity_Effect
- 優化建議區塊: Optimization_Suggestions, Best_Practices, Performance_Tips
```

### **參數化配置邏輯**

#### **1. 動態參數生成**
```
專案類型參數:
- KANGAROO: 多設備測試、複雜儀器配置、多功能整合
- VALO360: 高精度測試、環境控制、品質控制流程
- RAPTOR: 全面測試覆蓋、測試流程整合、多階段測試

測試功能參數:
- WiFi測試: 頻率範圍、功率設定、調製方式
- 藍牙測試: 協議版本、功率等級、連接模式
- 固件升級: 升級方式、版本管理、回滾策略
- 主機板測試: 功能模組、接口測試、性能指標
```

#### **2. 智能參數優化**
```
參數範圍優化:
- 根據設備規格自動調整參數範圍
- 根據測試環境自動優化配置參數
- 根據歷史數據自動調整最佳參數

參數關聯優化:
- 自動檢測參數間的依賴關係
- 自動調整相關參數的一致性
- 自動優化參數組合的最佳性
```

### **品質保證機制**

#### **1. 格式一致性檢查**
```
工作表結構檢查:
- 確保工作表數量符合模板要求
- 確保工作表順序符合邏輯流程
- 確保工作表內容符合標準格式

欄位格式檢查:
- 確保欄位名稱符合命名規範
- 確保數據類型符合欄位定義
- 確保數據格式符合驗證規則
```

#### **2. 邏輯驗證檢查**
```
參數邏輯檢查:
- 檢查參數值是否在有效範圍內
- 檢查參數間的依賴關係是否正確
- 檢查參數組合是否合理有效

流程邏輯檢查:
- 檢查測試流程是否完整
- 檢查流程步驟是否順序正確
- 檢查流程分支是否邏輯合理
```

---

## 📊 分析總結

### **已完成分析**
- ✅ 腳本1: Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx
- ✅ 腳本2: Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX
- [ ] 腳本3: Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX
- [ ] 腳本4: Test Item Code V2.04_20250310.xlsx
- [ ] 腳本5: Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx
- [ ] 腳本6: Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx
- [ ] 腳本7: Pega_Kangaroo_TestFlow-Final Check_MP_20250415_CBNGSIMSLOT1.xlsx
- [ ] 腳本8: Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx
- [ ] 腳本9: Kangaroo_MP_AIR_TestFlow_20250326C.xlsx
- [ ] 腳本10: Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx

### **分析進度**
- **總腳本數量**: 11個
- **已完成分析**: 2個
- **分析進度**: 18.2%
- **預計完成時間**: 待定

---

## 🔗 相關文檔

- [AI腳本邏輯分析主索引](AI_SCRIPT_LOGIC_ANALYSIS_MAIN_INDEX.md)
- [腳本設計模式深度分析](SCRIPT_DESIGN_PATTERNS_REFERENCE.md)
- [腳本結構深度分析](SCRIPT_STRUCTURE_DEEP_ANALYSIS.md)

---

*本文檔將持續更新，完成所有KANGAROO專案腳本的邏輯分析。* 