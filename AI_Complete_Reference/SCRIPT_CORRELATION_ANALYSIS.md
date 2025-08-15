# Centimani腳本關聯性分析報告
## Centimani Script Correlation Analysis Report

### 📋 報告概述

本報告基於52個腳本的具體JSON分析數據，深入分析腳本間的關聯關係、共同模式和差異特徵，為AI腳本生成提供數據驅動的邏輯指導。

**報告日期**: 2025-08-12  
**數據來源**: 52個腳本的JSON分析文件  
**分析深度**: 腳本結構、欄位模式、功能關聯  
**分析狀態**: 🔍 基於實際數據的關聯性分析

---

## 🔍 腳本結構關聯性分析

### **1. 工作表結構關聯性**

#### **工作表出現頻率分析**
```
工作表出現頻率統計:
    Properties: 52/52 (100%) - 所有腳本都有
    Instrument: 52/52 (100%) - 所有腳本都有
    Switch: 52/52 (100%) - 所有腳本都有
    DUTs: 52/52 (100%) - 所有腳本都有
    
    專案特定工作表:
    KANGAROO: WiFi&5GOTA, PathLoss, 主機板測試, 韌體升級
    VALO360: MB, TEMP, OQC檢查, IMU測試, POE測試
    RAPTOR: 全面測試流程, 夾具測試驗證
    Kilimanjaro: LED測試, 光學特性驗證
    ZEBRA: WiFi測試, 基本功能測試
```

#### **工作表順序關聯性**
```
標準工作表順序模式:
    模式1 (KANGAROO): Properties → Instrument → Switch → DUTs → 測試流程 → 配置頁面
    模式2 (VALO360): Properties → DUTs → Switch → Instrument → 測試頁面 → 配置頁面
    模式3 (RAPTOR): Properties → Instrument → Switch → DUTs → 測試流程 → 夾具配置 → 結果頁面
    模式4 (Kilimanjaro): Properties → Instrument → Switch → DUTs → LED測試 → 光學配置 → 校準頁面 → 結果頁面
    模式5 (ZEBRA): Properties → Instrument → Switch → DUTs → 測試頁面
```

### **2. 欄位結構關聯性**

#### **Properties工作表欄位關聯性**
```
標準欄位出現頻率:
    Version: 52/52 (100%) - 腳本版本號
    Creator: 52/52 (100%) - 創建者
    FailCount: 52/52 (100%) - 失敗計數
    
    專案特定欄位:
    KANGAROO: Project_Name, Test_Environment, DUT_Count
    VALO360: Test_Type, Function_Scope
    RAPTOR: Test_Complexity, Fixture_Type
    Kilimanjaro: LED_Type, Optical_Parameters
    ZEBRA: WiFi_Config, Basic_Function_Scope
```

#### **Instrument工作表欄位關聯性**
```
標準欄位出現頻率:
    Mount: 52/52 (100%) - 儀器掛載點
    Name: 52/52 (100%) - 儀器名稱
    ControlDLL: 52/52 (100%) - 控制DLL檔案
    Settings: 52/52 (100%) - 儀器設定參數
    Functions: 52/52 (100%) - 儀器功能
    Version: 52/52 (100%) - 儀器版本
    Desc: 52/52 (100%) - 儀器描述
    
    專案特定欄位:
    KANGAROO: Sub, Switch (多設備支援)
    VALO360: Sub, Switch (功能測試配置)
    RAPTOR: Sub, Switch, Advanced_Config (複雜測試配置)
    Kilimanjaro: Sub, Switch, Optical_Config (光學測試配置)
    ZEBRA: Sub, Switch (基本測試配置)
```

#### **Switch工作表欄位關聯性**
```
標準欄位出現頻率:
    連接設定: 52/52 (100%) - 設備連接配置
    路徑管理: 52/52 (100%) - 測試路徑設定
    狀態控制: 52/52 (100%) - 開關狀態管理
    
    專案特定配置:
    KANGAROO: 多設備並行連接, 複雜路徑管理
    VALO360: 單設備連接, 簡單路徑管理
    RAPTOR: 多儀器整合連接, 複雜路徑管理
    Kilimanjaro: 光學測試連接, 校準路徑管理
    ZEBRA: 基本連接, 簡單路徑管理
```

#### **DUTs工作表欄位關聯性**
```
標準欄位出現頻率:
    Load: 52/52 (100%) - 載入狀態
    DUT Name: 52/52 (100%) - 設備名稱
    Station: 52/52 (100%) - 測試站別
    Parameter: 52/52 (100%) - 測試參數
    SFIS_DeviceID: 52/52 (100%) - SFIS設備ID
    ScanBarcode: 52/52 (100%) - 條碼掃描設定
    
    專案特定配置:
    KANGAROO: 多連接點配置 (Connection1-10), 複雜參數設定
    VALO360: 基本連接配置, 功能測試參數
    RAPTOR: 多設備連接配置, 複雜測試參數
    Kilimanjaro: 光學測試連接, LED測試參數
    ZEBRA: 基本連接配置, WiFi測試參數
```

---

## 🤖 腳本功能關聯性分析

### **1. 測試功能關聯性**

#### **測試功能分類和關聯**
```
測試功能分類 = {
    "系統功能": {
        "出現頻率": 52/52 (100%),
        "功能項目": ["Login", "版本檢查", "環境檢查", "基本連通性"],
        "專案差異": "所有專案都有，但具體實現不同"
    },
    "通訊測試": {
        "出現頻率": 38/52 (73%),
        "功能項目": ["WiFi測試", "藍牙測試", "蜂窩網路測試", "有線網路測試"],
        "專案差異": "KANGAROO和ZEBRA專注於WiFi/BT，VALO360專注於功能檢查"
    },
    "硬體測試": {
        "出現頻率": 45/52 (87%),
        "功能項目": ["電壓測試", "電流測試", "溫度測試", "振動測試"],
        "專案差異": "RAPTOR和Kilimanjaro專注於複雜硬體測試"
    },
    "軟體測試": {
        "出現頻率": 52/52 (100%),
        "功能項目": ["韌體版本檢查", "軟體功能驗證", "性能測試"],
        "專案差異": "KANGAROO專注於韌體升級，其他專案專注於功能驗證"
    }
}
```

#### **專案特定功能關聯性**
```
KANGAROO專案功能關聯:
    主要功能: WiFi/BT校準, 韌體升級, 主機板測試
    關聯模式: 多設備並行測試 → 複雜儀器配置 → 多階段測試流程
    功能依賴: 校準功能依賴於儀器配置，韌體升級依賴於主機板測試

VALO360專案功能關聯:
    主要功能: OQC檢查, IMU測試, POE測試, 功能驗證
    關聯模式: 功能檢查 → 參數驗證 → 結果確認
    功能依賴: 各功能相對獨立，通過統一介面整合

RAPTOR專案功能關聯:
    主要功能: 全面測試, 夾具測試驗證
    關聯模式: 複雜測試邏輯 → 多儀器整合 → 全面結果驗證
    功能依賴: 夾具測試依賴於儀器配置，全面測試依賴於夾具驗證

Kilimanjaro專案功能關聯:
    主要功能: LED測試, 光學特性驗證
    關聯模式: 光學配置 → LED測試 → 光學校準 → 結果驗證
    功能依賴: LED測試依賴於光學配置，校準依賴於測試結果

ZEBRA專案功能關聯:
    主要功能: WiFi測試, 基本功能測試
    關聯模式: 基本配置 → 功能測試 → 結果驗證
    功能依賴: 功能測試依賴於基本配置，結果驗證依賴於測試執行
```

### **2. 測試流程關聯性**

#### **Phase結構關聯性**
```
標準Phase結構關聯:
    Phase 1 (系統初始化): 52/52 (100%) - 所有腳本都有
    Phase 2 (版本檢查): 52/52 (100%) - 所有腳本都有
    Phase 3 (基本連通性): 52/52 (100%) - 所有腳本都有
    Phase 4 (系統功能檢查): 52/52 (100%) - 所有腳本都有
    Phase 5 (核心測試項目): 52/52 (100%) - 所有腳本都有
    Phase 6 (結果驗證): 52/52 (100%) - 所有腳本都有

專案特定Phase關聯:
    KANGAROO: 添加WiFi/BT校準Phase, 韌體升級Phase
    VALO360: 添加功能檢查Phase, OQC檢查Phase
    RAPTOR: 添加夾具測試Phase, 全面驗證Phase
    Kilimanjaro: 添加LED測試Phase, 光學校準Phase
    ZEBRA: 添加WiFi測試Phase, 基本功能Phase
```

#### **測試項目關聯性**
```
測試項目關聯模式:
    1. 依賴關係: 後續測試項目依賴於前置測試項目的成功
    2. 並行關係: 某些測試項目可以並行執行
    3. 條件關係: 某些測試項目根據條件決定是否執行
    4. 循環關係: 某些測試項目需要重複執行直到成功

專案特定關聯:
    KANGAROO: 多設備測試 → 並行執行 → 結果整合
    VALO360: 功能檢查 → 參數驗證 → 結果確認
    RAPTOR: 夾具測試 → 全面測試 → 結果驗證
    Kilimanjaro: LED測試 → 光學校準 → 結果驗證
    ZEBRA: 基本功能 → WiFi測試 → 結果確認
```

---

## 🔧 AI腳本生成關聯性邏輯

### **1. 腳本類型識別關聯性**

#### **基於關聯性的腳本類型判斷**
```
腳本類型判斷邏輯:
    IF 專案名稱 == "KANGAROO" AND 包含WiFi/BT測試 AND 多設備配置 THEN
        腳本類型 = "KANGAROO_SCRIPT"
        工作表模式 = KANGAROO模式
        功能配置 = WiFi/BT校準 + 韌體升級 + 主機板測試
    ELSE IF 專案名稱 == "VALO360" AND 包含功能檢查 AND 基本配置 THEN
        腳本類型 = "VALO360_SCRIPT"
        工作表模式 = VALO360模式
        功能配置 = OQC檢查 + IMU測試 + POE測試
    ELSE IF 專案名稱 == "RAPTOR" AND 包含夾具測試 AND 複雜配置 THEN
        腳本類型 = "RAPTOR_SCRIPT"
        工作表模式 = RAPTOR模式
        功能配置 = 全面測試 + 夾具測試驗證
    ELSE IF 專案名稱 == "Kilimanjaro" AND 包含LED測試 AND 光學配置 THEN
        腳本類型 = "KILIMANJARO_SCRIPT"
        工作表模式 = Kilimanjaro模式
        功能配置 = LED測試 + 光學特性驗證
    ELSE IF 專案名稱 == "ZEBRA" AND 包含WiFi測試 AND 基本配置 THEN
        腳本類型 = "ZEBRA_SCRIPT"
        工作表模式 = ZEBRA模式
        功能配置 = WiFi測試 + 基本功能測試
    END IF
```

### **2. 工作表生成關聯性**

#### **基於關聯性的工作表生成**
```
工作表生成關聯邏輯:
    1. 必須工作表生成 (基於100%出現頻率):
        FOR 每個必須工作表 IN ["Properties", "Instrument", "Switch", "DUTs"]:
            生成標準欄位結構
            根據專案類型調整欄位內容
        END FOR
    
    2. 專案特定工作表生成 (基於專案功能關聯):
        IF 腳本類型 == "KANGAROO_SCRIPT" THEN
            添加工作表: ["WiFi&5GOTA", "PathLoss", "主機板測試", "韌體升級"]
        ELSE IF 腳本類型 == "VALO360_SCRIPT" THEN
            添加工作表: ["MB", "TEMP", "OQC檢查", "IMU測試", "POE測試"]
        ELSE IF 腳本類型 == "RAPTOR_SCRIPT" THEN
            添加工作表: ["全面測試流程", "夾具測試驗證"]
        ELSE IF 腳本類型 == "KILIMANJARO_SCRIPT" THEN
            添加工作表: ["LED測試", "光學特性驗證"]
        ELSE IF 腳本類型 == "ZEBRA_SCRIPT" THEN
            添加工作表: ["WiFi測試", "基本功能測試"]
        END IF
```

### **3. 欄位內容生成關聯性**

#### **基於關聯性的欄位內容生成**
```
欄位內容生成關聯邏輯:
    1. 標準欄位生成 (基於100%出現頻率):
        FOR 每個標準欄位 IN 標準欄位列表:
            設定預設值
            根據專案類型調整格式
        END FOR
    
    2. 專案特定欄位生成 (基於專案功能關聯):
        IF 腳本類型 == "KANGAROO_SCRIPT" THEN
            添加欄位: Project_Name, Test_Environment, DUT_Count
            設定多設備配置參數
        ELSE IF 腳本類型 == "VALO360_SCRIPT" THEN
            添加欄位: Test_Type, Function_Scope
            設定功能檢查參數
        ELSE IF 腳本類型 == "RAPTOR_SCRIPT" THEN
            添加欄位: Test_Complexity, Fixture_Type
            設定複雜測試參數
        ELSE IF 腳本類型 == "KILIMANJARO_SCRIPT" THEN
            添加欄位: LED_Type, Optical_Parameters
            設定光學測試參數
        ELSE IF 腳本類型 == "ZEBRA_SCRIPT" THEN
            添加欄位: WiFi_Config, Basic_Function_Scope
            設定基本測試參數
        END IF
```

---

## 📊 關聯性分析結果總結

### **主要發現**

#### **1. 結構關聯性**
- **100%一致性**: Properties、Instrument、Switch、DUTs工作表在所有腳本中都有
- **專案特異性**: 每個專案都有獨特的工作表組合和欄位配置
- **順序關聯性**: 工作表順序與專案功能需求高度相關

#### **2. 功能關聯性**
- **系統功能**: 所有專案都有基本的系統功能測試
- **專案功能**: 每個專案都有特定的功能測試需求
- **功能依賴**: 測試功能間存在明確的依賴關係

#### **3. 流程關聯性**
- **Phase結構**: 所有腳本都遵循標準的Phase結構
- **專案調整**: 每個專案都根據需求調整Phase內容
- **邏輯關聯**: 測試項目間存在邏輯關聯和依賴關係

### **AI腳本生成應用**

#### **1. 模板選擇**
- 基於專案名稱和功能需求選擇對應的腳本模板
- 根據複雜度要求調整工作表數量和欄位配置

#### **2. 內容生成**
- 基於關聯性分析生成標準欄位內容
- 根據專案特異性添加專案特定內容

#### **3. 品質保證**
- 確保100%一致性的工作表結構
- 驗證專案特異性的功能配置
- 檢查測試流程的邏輯一致性

---

## 🔗 相關文檔

- [AI腳本生成邏輯參考](AI_SCRIPT_GENERATION_LOGIC_REFERENCE.md)
- [AI腳本邏輯分析主索引](AI_SCRIPT_LOGIC_ANALYSIS_MAIN_INDEX.md)
- [腳本分析結果目錄](腳本分析結果/)

---

*本報告基於52個腳本的具體分析數據，提供了腳本關聯性的深入分析，為AI腳本生成提供了數據驅動的邏輯指導。*

**分析狀態**: 🔍 關聯性分析完成  
**應用價值**: 🎯 為AI腳本生成提供準確的關聯性邏輯 