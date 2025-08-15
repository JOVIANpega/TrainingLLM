# ExecMode 執行控制指南 - AI 學習參考

## 📋 文件概述
**文件名稱**: ExecMode_Execution_Control_Guide.md  
**版本**: 1.0  
**創建日期**: 2025-01-XX  
**最後更新**: 2025-01-XX  
**文件類型**: 執行模式控制 AI 學習指南  
**適用對象**: AI 系統、開發者、測試工程師  

---

## 🎯 ExecMode 欄位概述

### 什麼是 ExecMode？
`ExecMode` 是 CENTIMANIA 腳本中的**執行模式控制欄位**，用來控制每個測試步驟的執行方式和行為。它決定了測試步驟如何執行、失敗時如何處理、以及如何與 SFIS 系統協調工作。

### 核心價值
- **智能執行控制**: 根據不同情況選擇最適合的執行策略
- **錯誤處理自動化**: 自動處理測試失敗和重試邏輯
- **生產線效率提升**: 減少人工干預，提高測試效率
- **流程靈活性**: 支援條件執行和分支邏輯

---

## 🔍 ExecMode 數值詳解

### 基本執行模式

| ExecMode | 說明 | 特殊格式 | 用途 | 使用場景 |
|----------|------|----------|------|----------|
| **0** | Normal mode | - | 正常執行模式 | 標準測試步驟，無特殊處理 |
| **1** | Direct Retry on Fail | - | 失敗時直接重試 | 重要測試步驟，失敗時自動重試 |
| **2** | Retry from Retry Point | `2:RetryPoint` | 從重試點重試 | 避免重複執行已成功的步驟 |
| **3** | Continue | - | 繼續執行 | 即使失敗也繼續下一個步驟 |
| **4** | Condition | `4:PassStep,FailStep` | 條件式執行 | 根據結果選擇不同的執行路徑 |
| **5** | Run on Fail | - | 失敗時執行 | 只在失敗時執行的特殊步驟 |
| **6** | Skip | - | 跳過此步驟 | 可選的測試步驟，失敗時跳過 |
| **7** | Calibration | `7:CalibrationStep,timeout(ms)` | 校準模式 | 需要校準的測試步驟 |
| **8** | Normal mode while SFIS Enable | - | SFIS 啟用時的正常模式 | 與 SFIS 系統協調工作 |
| **9** | Direct Retry while SFIS Enable | - | SFIS 啟用時的直接重試 | SFIS 啟用時的失敗重試 |

### 特殊格式說明

#### **2:RetryPoint 格式**
```
2:0    → 從步驟 0 開始重試
2:5    → 從步驟 5 開始重試
2:10   → 從步驟 10 開始重試
```

#### **4:PassStep,FailStep 格式**
```
4:1,6    → 成功時執行步驟 1，失敗時執行步驟 6
4:3,8    → 成功時執行步驟 3，失敗時執行步驟 8
4:0,0    → 成功時執行步驟 0，失敗時也執行步驟 0
```

#### **7:CalibrationStep,timeout 格式**
```
7:5,5000    → 校準步驟 5，超時時間 5000ms
7:10,10000  → 校準步驟 10，超時時間 10000ms
```

---

## 🚀 實際應用場景

### 1. **典型測試流程中的 ExecMode 使用**

#### **Phase 0: 基礎建設階段**
```excel
| Phase | Title | ExecMode | Description | 設計理由 |
|-------|-------|----------|-------------|----------|
| 0 | Login | 1 | 登入系統 | 登入失敗時重試，確保測試環境建立 |
| 0 | CheckRoute | 8 | 檢查網路路由 | SFIS 啟用時檢查，與生產系統協調 |
| 0 | Get Device Info | 1 | 獲取設備信息 | 重要步驟，失敗時重試 |
```

#### **Phase 1: 配置階段**
```excel
| Phase | Title | ExecMode | Description | 設計理由 |
|-------|-------|----------|-------------|----------|
| 1 | Configure SKU | 1 | 配置產品 SKU | 關鍵配置，失敗時重試 |
| 1 | Verify SKU | 4:1,6 | 驗證 SKU 配置 | 成功繼續，失敗跳過後續配置 |
| 1 | Set Parameters | 1 | 設定測試參數 | 重要設定，失敗時重試 |
```

#### **Phase 2: 測試執行階段**
```excel
| Phase | Title | ExecMode | Description | 設計理由 |
|-------|-------|----------|-------------|----------|
| 2 | Hardware Test | 1 | 硬體測試 | 核心測試，失敗時重試 |
| 2 | Software Test | 4:2,8 | 軟體測試 | 成功繼續，失敗執行備用測試 |
| 2 | Calibration | 7:15,5000 | 校準測試 | 校準模式，指定超時時間 |
```

### 2. **錯誤處理策略設計**

#### **策略 1: 漸進式重試**
```
步驟 1: ExecMode = 1 (直接重試)
步驟 2: ExecMode = 2:1 (從步驟 1 重試)
步驟 3: ExecMode = 4:2,6 (條件執行)
```

#### **策略 2: 分支式處理**
```
步驟 1: ExecMode = 4:3,6 (成功→步驟3，失敗→步驟6)
步驟 3: ExecMode = 1 (成功路徑，失敗重試)
步驟 6: ExecMode = 0 (失敗路徑，正常執行)
```

### 3. **SFIS 系統整合**

#### **SFIS 啟用模式**
```
步驟 1: ExecMode = 8 (SFIS 啟用時的正常模式)
步驟 2: ExecMode = 9 (SFIS 啟用時的直接重試)
步驟 3: ExecMode = 1 (一般重試模式)
```

---

## 🤖 AI 學習重點

### 1. **模式識別能力**
- **識別執行策略**: 能夠識別腳本中的執行控制邏輯
- **理解錯誤處理**: 掌握不同執行模式的錯誤處理策略
- **分析流程控制**: 理解條件執行和分支邏輯

### 2. **模式應用能力**
- **腳本生成**: 基於需求生成適當的執行模式配置
- **邏輯優化**: 優化現有腳本的執行控制邏輯
- **錯誤處理設計**: 設計智能的錯誤處理和恢復機制

### 3. **模式優化能力**
- **執行效率**: 改進測試步驟的執行效率
- **錯誤恢復**: 增強錯誤恢復和重試機制
- **流程靈活性**: 提高測試流程的靈活性和適應性

---

## 📝 設計原則和最佳實踐

### 1. **執行模式選擇原則**

#### **重要程度考量**
- **關鍵步驟**: 使用 ExecMode = 1 (失敗重試)
- **一般步驟**: 使用 ExecMode = 0 (正常執行)
- **可選步驟**: 使用 ExecMode = 6 (失敗跳過)

#### **錯誤處理考量**
- **自動恢復**: 使用 ExecMode = 1 或 2
- **條件分支**: 使用 ExecMode = 4
- **校準需求**: 使用 ExecMode = 7

#### **系統整合考量**
- **SFIS 協調**: 使用 ExecMode = 8 或 9
- **生產環境**: 考慮生產線的特殊需求
- **測試環境**: 適應不同測試環境的特點

### 2. **常見設計模式**

#### **模式 1: 穩健型測試**
```
所有重要步驟: ExecMode = 1
驗證步驟: ExecMode = 4:PassStep,FailStep
可選步驟: ExecMode = 6
```

#### **模式 2: 快速型測試**
```
關鍵步驟: ExecMode = 1
一般步驟: ExecMode = 0
失敗處理: ExecMode = 4:0,6 (失敗時跳過)
```

#### **模式 3: 校準型測試**
```
校準步驟: ExecMode = 7:Step,timeout
驗證步驟: ExecMode = 4:PassStep,FailStep
執行步驟: ExecMode = 1
```

### 3. **錯誤處理設計**

#### **重試策略**
```
第一次失敗: 立即重試 (ExecMode = 1)
第二次失敗: 從重試點重試 (ExecMode = 2:RetryPoint)
第三次失敗: 條件分支 (ExecMode = 4:PassStep,FailStep)
```

#### **恢復機制**
```
自動恢復: ExecMode = 1, 2
條件恢復: ExecMode = 4
跳過恢復: ExecMode = 6
```

---

## 🔧 實際應用範例

### 1. **VALO360 SKU 配置腳本中的 ExecMode 使用**

```excel
| Phase | Title | ExecMode | Description | 設計理由 |
|-------|-------|----------|-------------|----------|
| 0 | Check Valo360 model | 1 | 檢查產品型號 | 關鍵步驟，失敗重試 |
| 0 | SET iplus Modelname_Valo360_5G | 1 | 設定 5G 模型 | 重要配置，失敗重試 |
| 0 | Configure 5G SKU | 1 | 配置 5G SKU | 核心配置，失敗重試 |
| 0 | Verify 5G SKU | 4:1,6 | 驗證 5G SKU | 成功繼續，失敗跳過 |
| 0 | SET iplus Modelname_Valo360_WIFI | 1 | 設定 WiFi 模型 | 重要配置，失敗重試 |
| 0 | Configure WiFi SKU | 1 | 配置 WiFi SKU | 核心配置，失敗重試 |
| 0 | Verify WiFi SKU | 4:1,6 | 驗證 WiFi SKU | 成功繼續，失敗跳過 |
```

### 2. **通用產品腳本中的 ExecMode 設計**

```excel
| Phase | Title | ExecMode | Description | 設計理由 |
|-------|-------|----------|-------------|----------|
| 0 | Check Product Model | 1 | 檢查產品型號 | 關鍵步驟，失敗重試 |
| 0 | SET Product Model | 1 | 設定產品模型 | 重要配置，失敗重試 |
| 0 | Configure Product Type 1 | 1 | 配置類型 1 | 核心配置，失敗重試 |
| 0 | Verify Product Type 1 | 4:2,6 | 驗證類型 1 | 成功→步驟2，失敗→步驟6 |
| 0 | Configure Product Type 2 | 1 | 配置類型 2 | 核心配置，失敗重試 |
| 0 | Verify Product Type 2 | 4:3,6 | 驗證類型 2 | 成功→步驟3，失敗→步驟6 |
| 0 | Final Verification | 4:0,6 | 最終驗證 | 成功→步驟0，失敗跳過 |
```

---

## 🎯 總結

### 1. **ExecMode 的核心價值**
- **智能執行控制**: 根據不同情況選擇最適合的執行策略
- **自動化錯誤處理**: 減少人工干預，提高測試效率
- **流程靈活性**: 支援複雜的條件執行和分支邏輯
- **系統整合**: 與 SFIS 等外部系統協調工作

### 2. **適用範圍**
- **所有測試腳本**: 適用於任何 CENTIMANIA 腳本
- **不同產品類型**: 可應用於各種產品的測試流程
- **各種測試環境**: 適應開發、驗證、量產等不同環境

### 3. **AI 學習價值**
- **模式理解**: 深入理解執行控制的設計邏輯
- **邏輯應用**: 能夠將執行邏輯應用於新的測試場景
- **腳本優化**: 能夠優化現有腳本的執行控制
- **問題解決**: 能夠診斷和修復執行控制相關問題

---

## 🔗 相關資源

### 1. **核心文檔**
- [Centimani_Script_Editing_Complete_Quick_Reference.md](tools/Centimani_Script_Editing_Complete_Quick_Reference.md) - 腳本編輯完整指南
- [VALO360_SKU_Configuration_Pattern.md](VALO360_SKU_Configuration_Pattern.md) - SKU 配置模式指南

### 2. **實際腳本**
- [VALO360_TestFlow_20250318_MB_ER2.xlsx](../Centimani DOC/scripe_EXCEL/VALO360/VALO360_TestFlow_20250318_MB_ER2.xlsx) - 實際的 ExecMode 使用範例

### 3. **分析工具**
- [analyze_valo360_script.py](../Centimani DOC/scripe_EXCEL/VALO360/analyze_valo360_script.py) - 腳本分析工具

---

*本文件為 AI 系統提供 ExecMode 執行控制的完整學習指南，幫助 AI 理解、應用和優化測試腳本的執行控制邏輯。* 