# VALO360 SKU 配置模式 - AI 學習指南

## 📋 文件概述
**文件名稱**: VALO360_SKU_Configuration_Pattern.md  
**版本**: 1.0  
**創建日期**: 2025-01-XX  
**最後更新**: 2025-01-XX  
**文件類型**: SKU 配置模式 AI 學習指南  
**適用對象**: AI 系統、開發者、測試工程師  

---

## 🎯 模式概述

### 什麼是 SKU 配置模式？
SKU 配置模式是一種**智能產品識別和自動配置**的測試流程設計模式，能夠根據生產系統（SFIS）的產品信息，自動識別產品型號並配置相應的參數。

### 核心價值
- **自動化程度高**: 減少人工配置錯誤
- **適應性強**: 支援多種產品變體
- **品質保證**: 確保每個產品都有正確配置
- **生產效率**: 提高生產線測試效率

---

## 🔍 模式分析

### 1. **基本流程結構**
```
SFIS 系統 → 型號識別 → 模型設定 → SKU 配置 → 驗證確認
    ↓           ↓         ↓         ↓         ↓
  獲取信息   確定版本   設定名稱   寫入設備   驗證結果
```

### 2. **具體實現邏輯**

#### **階段 1: 基礎建設**
```
Login → CheckRoute → GET sfisSKU
```
**目的**: 建立測試環境，獲取設備資訊，準備模型配置

#### **階段 2: 智能模型配置**
```
Check Valo360 model → 條件分支 → 三種模型設定
```
**核心邏輯**:
1. 從 SFIS 讀取 SKU 值
2. 設定到全域變數 `$G_VALO360_MODEL`
3. 根據 SKU 值執行對應的模型配置路徑
4. 每種配置都有完整的設定→驗證→等待流程

#### **階段 3: 具體配置執行**
```
0,SET iplus Modelname_Valo360_5G
:SetVal,"$G_VALO360_MODEL","*(sfisSKU)"
:SetModelName, "N3C2401C"
UART@diag -s sku N3C2401C\r\n
:Delay, "2000"
UART@diag -g sku\r\n
```

### 3. **變數系統設計**

#### **變數類型**
- **SFIS 變數**: `*(sfisSKU)` - 從生產系統讀取
- **全域變數**: `$G_VALO360_MODEL` - 腳本執行時的中央配置
- **配置變數**: `*$(VALO360_5G)` - 預定義的模型配置

#### **變數使用模式**
```
:SetVal,"$G_VALO360_MODEL","*(sfisSKU)"  → 從 SFIS 設定全域變數
:GetVal,"$G_VALO360_MODEL"              → 讀取設定值
:GetVal,"$G_VALO360_MODEL"              → 驗證是否為 *$(VALO360_ALL_MODEL)
```

---

## 🚀 通用化設計

### 1. **通用化原則**

#### **產品抽象化**
```
原始設計: VALO360_5G → N3C2401C
通用設計: PRODUCT_TYPE_1 → SKU_CODE_1
```

#### **配置參數化**
```
原始設計: UART@diag -s sku N3C2401C
通用設計: UART@diag -s sku *(PRODUCT_SKU)
```

### 2. **通用化模板**

#### **模板結構**
```excel
| Phase | Title | Send | Reply | Ref | Validation | Description |
|-------|-------|------|-------|-----|------------|-------------|
| 0 | Check Product Model | :SfGetVersion,"*(ISN)","ISN_ITEMINFO","3","","" | | $sfisSKU | | Get product info from SFIS |
| 0 | SET Product Model | :SetVal,"$G_PRODUCT_MODEL","*(sfisSKU)" | | | | Set product model variable |
| 0 | Configure Product Type 1 | :GetVal,"$G_PRODUCT_MODEL" | *(PRODUCT_TYPE_1) | | | Check if product type 1 |
| 0 | Set SKU for Type 1 | UART@diag -s sku *(SKU_CODE_1) | | | | Set SKU for product type 1 |
| 0 | Verify SKU | UART@diag -g sku | | $DUT_SKU | (DUT_SKU,%s,*(SKU_CODE_1),) | Verify SKU setting |
```

#### **通用變數定義**
```ini
# Global.ini
PRODUCT_TYPE_1=@PRODUCT_TYPE_1_NAME||@SKU_CODE_1
PRODUCT_TYPE_2=@PRODUCT_TYPE_2_NAME||@SKU_CODE_2
PRODUCT_TYPE_3=@PRODUCT_TYPE_3_NAME||@SKU_CODE_3
PRODUCT_ALL_MODEL=@PRODUCT_TYPE_1||@PRODUCT_TYPE_2||@PRODUCT_TYPE_3
```

### 3. **適用於不同產品的邏輯**

#### **產品 A (例如: VALO360)**
```
VALO360_5G → N3C2401C
VALO360_WIFI → N3C2401W
VALO360_NObattery → N3C2401NB
```

#### **產品 B (例如: KANGAROO)**
```
KANGAROO_4G → K4G001
KANGAROO_5G → K5G001
KANGAROO_WIFI → KWF001
```

#### **產品 C (例如: RAPTOR)**
```
RAPTOR_PRO → RPR001
RAPTOR_LITE → RLT001
RAPTOR_ENTERPRISE → REN001
```

---

## 🤖 AI 學習重點

### 1. **模式識別能力**
- **識別 SKU 配置模式**: 能夠識別腳本中的 SKU 配置邏輯
- **理解變數系統**: 掌握 SFIS、全域、配置三層變數的關係
- **分析條件分支**: 理解根據產品類型選擇不同配置路徑的邏輯

### 2. **模式應用能力**
- **腳本生成**: 基於模板生成新的產品 SKU 配置腳本
- **邏輯修改**: 修改現有腳本以支援新的產品類型
- **錯誤診斷**: 識別和修復 SKU 配置腳本中的問題

### 3. **模式優化能力**
- **流程優化**: 改進 SKU 配置流程的效率
- **驗證增強**: 增強 SKU 驗證的準確性
- **錯誤處理**: 改進錯誤處理和恢復機制

---

## 📝 實現步驟

### 1. **分析新產品需求**
```
1. 識別產品類型數量
2. 確定每種類型的 SKU 代碼
3. 分析配置參數
4. 設計驗證邏輯
```

### 2. **設計變數結構**
```
1. 定義 SFIS 變數名稱
2. 設計全域變數結構
3. 建立配置變數映射
4. 設定預設值
```

### 3. **編寫腳本邏輯**
```
1. 基礎建設階段
2. 產品識別階段
3. 條件分支階段
4. 配置執行階段
5. 驗證確認階段
```

### 4. **測試和驗證**
```
1. 單元測試每個階段
2. 整合測試完整流程
3. 錯誤情況測試
4. 性能測試
```

---

## 🔧 實際應用範例

### 1. **VALO360 腳本範例**
```excel
| Phase | Title | Send | Reply | Ref | Validation | Description |
|-------|-------|------|-------|-----|------------|-------------|
| 0 | Check Valo360 model | :SfGetVersion,"*(ISN)","ISN_ITEMINFO","3","","" | | $sfisSKU | | Get VALO360 model from SFIS |
| 0 | SET iplus Modelname_Valo360_5G | :SetVal,"$G_VALO360_MODEL","*(sfisSKU)" | | | | Set VALO360 5G model |
| 0 | Configure 5G SKU | UART@diag -s sku N3C2401C\r\n | | | | Set 5G SKU |
| 0 | Verify 5G SKU | UART@diag -g sku | | $DUT_SKU | (DUT_SKU,%s,N3C2401C,) | Verify 5G SKU |
```

### 2. **通用產品腳本範例**
```excel
| Phase | Title | Send | Reply | Ref | Validation | Description |
|-------|-------|------|-------|-----|------------|-------------|
| 0 | Check Product Model | :SfGetVersion,"*(ISN)","ISN_ITEMINFO","3","","" | | $sfisSKU | | Get product model from SFIS |
| 0 | SET Product Model | :SetVal,"$G_PRODUCT_MODEL","*(sfisSKU)" | | | | Set product model variable |
| 0 | Configure Type 1 | :GetVal,"$G_PRODUCT_MODEL" | *(PRODUCT_TYPE_1) | | | Check if product type 1 |
| 0 | Set SKU Type 1 | UART@diag -s sku *(SKU_CODE_1) | | | | Set SKU for type 1 |
| 0 | Verify SKU Type 1 | UART@diag -g sku | | $DUT_SKU | (DUT_SKU,%s,*(SKU_CODE_1),) | Verify SKU for type 1 |
```

---

## 🎯 總結

### 1. **模式特點**
- **智能識別**: 自動識別產品類型
- **動態配置**: 根據識別結果動態配置參數
- **完整驗證**: 配置後進行完整性驗證
- **錯誤處理**: 完善的錯誤處理和恢復機制

### 2. **適用範圍**
- **多變體產品**: 支援同一產品的多種變體
- **不同產品線**: 可應用於不同的產品系列
- **生產環境**: 適用於各種生產測試環境

### 3. **AI 學習價值**
- **模式理解**: 深入理解 SKU 配置的設計邏輯
- **邏輯應用**: 能夠將邏輯應用於新的產品
- **腳本生成**: 基於模式生成新的測試腳本
- **問題解決**: 能夠診斷和修復相關問題

---

## 🔗 相關資源

### 1. **核心文檔**
- [VALO360_Script_Analysis_Guide.md](VALO360_Script_Analysis_Guide.md) - VALO360 腳本分析指南
- [Centimani_Script_Editing_Complete_Quick_Reference.md](tools/Centimani_Script_Editing_Complete_Quick_Reference.md) - 腳本編輯完整指南

### 2. **實際腳本**
- [VALO360_TestFlow_20250318_MB_ER2.xlsx](../Centimani DOC/scripe_EXCEL/VALO360/VALO360_TestFlow_20250318_MB_ER2.xlsx) - 實際的 SKU 配置腳本

### 3. **分析工具**
- [analyze_valo360_script.py](../Centimani DOC/scripe_EXCEL/VALO360/analyze_valo360_script.py) - 腳本分析工具

---

*本文件為 AI 系統提供 SKU 配置模式的完整學習指南，幫助 AI 理解、應用和優化這種重要的測試流程設計模式。* 