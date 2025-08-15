# Centimani Excel 腳本 AI 參考索引

## 概述
本索引整合了 `Centimani DOC/scripe_EXCEL` 目錄中所有 Excel 檔案的深度分析結果，為 AI 系統提供完整的參考資料導航。

## 快速導航

### 📊 分析報告
- [Excel 腳本分析報告](excel_analysis_report.md) - 整體分析概覽
- [Excel 腳本 AI 參考表](EXCEL_SCRIPTS_AI_REFERENCE_TABLE.md) - 詳細專案分析
- [專案邏輯分析表](PROJECT_LOGIC_ANALYSIS_TABLE.md) - 邏輯結構深度分析

### 📁 原始分析數據
- [excel_analysis_results.json](excel_analysis_results.json) - 完整分析結果 (JSON 格式)
- [excel_analysis_summary.json](excel_analysis_summary.json) - 分析總結 (JSON 格式)

---

## 專案分類索引

### 🔴 KANGAROO 專案 (手機測試平台)
**複雜度**: High | **檔案數量**: 20 | **主要功能**: 手機硬體測試、韌體升級、網路驗證

#### 核心測試流程
- **WiFi & 藍牙校準驗證** - `Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX`
- **WiFi OTA 韌體升級** - `Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX`
- **韌體下載測試** - `Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx`
- **蜂窩網路驗證** - `Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx`
- **主機板測試** - `Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx`
- **OQC 最終檢查** - `Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx`
- **測試項目代碼** - `Test Item Code V2.04_20250310.xlsx`

#### 邏輯特點
- 階層化測試架構
- 多工作表設計
- 參數化配置
- 完整的結果追蹤

---

### 🔵 VALO360 專案 (網路設備測試平台)
**複雜度**: Medium | **檔案數量**: 20 | **主要功能**: 網路設備功能測試、性能驗證

#### 核心測試流程
- **POE 功能測試** - `VALO360_TestFlow_20250307_POE.xlsx`
- **DMIC 功能測試** - `Pega_Nokia_TestFlow_20250307_ER2_DMIC.xlsx`
- **IMU 功能測試** - `VALO360_TestFlow_20250326_IMU.xlsx`
- **ER2 功能測試** - `VALO360_TestFlow_20250218_ER2.xlsx`
- **OQC 功能檢查** - `VALO360_ER2 OQC Function Check List_20250418.xlsx`

#### 邏輯特點
- 功能模組化設計
- 網路協議專注
- 硬體介面測試
- 性能基準建立

---

### 🟡 RAPTOR 專案 (通用測試平台)
**複雜度**: Medium | **檔案數量**: 4 | **主要功能**: 通用測試流程支援

#### 核心測試流程
- **通用測試流程** - `Raptor_ALL_TestFlow_20230223_ALL.XLSX`
- **夾具測試流程** - `Raptor_ALL_TestFlow_Fixcture_20230309_ALL.XLSX`

#### 邏輯特點
- 模板化設計
- 靈活配置支援
- 標準化流程
- 通用性強

---

### 🟢 ZEBRA 專案 (WiFi 專用測試平台)
**複雜度**: Medium | **檔案數量**: 6 | **主要功能**: WiFi 功能專項測試

#### 核心測試流程
- **WiFi 測試流程** - `wifi_TestFlow.XLSX`
- **標準測試流程** - `Zebra_20190417_TestFlow.XLSX`

#### 邏輯特點
- 專項化測試
- 深度功能測試
- 標準化流程
- WiFi 專注

---

### 🟣 Kilimanjaro 專案 (LED 測試專用平台)
**複雜度**: Medium | **檔案數量**: 2 | **主要功能**: LED 功能專項測試

#### 核心測試流程
- **LED 測試流程** - `Kilimanjaro_LED_20201116_TestFlow.xlsx`

#### 邏輯特點
- 專項化測試
- 光學參數測試
- 穩定性測試
- 壽命測試

---

## 邏輯模式索引

### 🔄 測試流程通用模式
1. **線性流程**: 初始化 → 測試執行 → 結果記錄 → 分析報告
2. **條件分支**: 根據測試結果選擇不同測試路徑
3. **循環測試**: 重複執行的測試項目
4. **並行測試**: 同時執行的多個測試項目

### 🎯 測試類型模式
1. **硬體檢測**: 硬體存在性 → 功能正常性 → 性能指標
2. **功能測試**: 功能開啟 → 參數設定 → 結果驗證
3. **性能測試**: 基準測試 → 極限測試 → 穩定性測試
4. **品質控制**: 標準檢查 → 一致性驗證 → 完整性檢查

### 📊 數據管理模式
1. **數據收集**: 參數讀取 → 數據驗證 → 數據存儲
2. **結果記錄**: 測試結果 → 結果統計 → 結果分析
3. **趨勢分析**: 變化檢測 → 趨勢分析 → 異常報警
4. **報告生成**: 數據整理 → 分析報告 → 建議生成

---

## AI 應用場景索引

### 🤖 腳本生成應用
- **模板化生成**: 基於現有模板生成新的測試腳本
- **參數化配置**: 自動調整測試參數以適應不同需求
- **流程優化**: 分析測試流程並提出優化建議

### 📈 資料分析應用
- **測試結果分析**: 分析測試結果並生成統計報告
- **趨勢分析**: 追蹤測試結果的變化趨勢
- **異常檢測**: 識別測試結果中的異常情況

### ✅ 品質控制應用
- **標準化檢查**: 檢查測試腳本是否符合標準
- **一致性驗證**: 驗證不同版本間的一致性
- **完整性檢查**: 檢查測試流程的完整性

### ⚡ 自動化應用
- **自動測試執行**: 基於腳本自動執行測試流程
- **結果自動記錄**: 自動記錄和整理測試結果
- **報告自動生成**: 自動生成測試報告和分析

---

## 🚨 重要：AI 開發最佳實踐

### ⚠️ 在開發新功能前，必須先檢查現有工具！

#### 1. 檢查現有工具
- **優先檢查**: `AI_Complete_Reference/tools/` 目錄
- **查找範圍**: 現有的 Python 腳本、分析工具、已生成的結果
- **避免重複**: 不要重新開發已有的功能

#### 2. 重用分析結果
- **使用已有結果**: 優先使用現有的 JSON 和 Markdown 分析結果
- **檢查完整性**: 確認現有結果是否滿足需求
- **補充缺失**: 只在現有結果不足時進行補充分析

#### 3. 擴展現有工具
- **功能擴展**: 在現有工具基礎上添加新功能
- **模組化設計**: 保持工具的模組化和可擴展性
- **向後相容**: 確保新功能不破壞現有功能

#### 4. 避免重複開發
- **建立規範**: 制定工具使用和開發規範
- **檢查清單**: 在開發前使用檢查清單確認需求
- **資源優化**: 避免重複造輪子，節省開發時間和資源

### 📋 開發前檢查清單

在開始任何新功能開發前，請按以下順序檢查：

1. **檢查現有工具目錄**
   - 查看 `AI_Complete_Reference/tools/` 目錄
   - 搜尋相關的 Python 腳本和分析工具
   - 檢查是否有現成的解決方案

2. **檢查已有分析結果**
   - 查看 JSON 格式的分析結果
   - 查看 Markdown 格式的報告
   - 確認現有結果的完整性和準確性

3. **評估現有工具功能**
   - 測試現有工具是否滿足需求
   - 檢查是否需要功能擴展
   - 評估修改現有工具的成本

4. **決定開發策略**
   - 如果現有工具完全滿足需求：直接使用
   - 如果現有工具部分滿足需求：擴展現有工具
   - 如果現有工具完全不滿足需求：開發新工具

### 🔍 現有工具資源清單

#### Excel 分析工具
- **`analyze_excel_templates.py`** - Excel 範例檔案結構分析
- **`centimani_data_organizer.py`** - 完整的資料整理和分析工具
- **`analyze_scripts_logic.py`** - 腳本邏輯深度分析工具

#### 已有分析結果
- **`excel_templates_analysis.json`** - Excel 模板分析結果 (152KB)
- **`All_Scripts_Logic_Analysis.json`** - 腳本邏輯分析結果 (107KB)
- **`All_Scripts_Logic_Analysis.md`** - 邏輯分析報告 (28KB)

#### 使用方式
```bash
# 使用現有 Excel 分析工具
cd AI_Complete_Reference/tools
python analyze_excel_templates.py

# 使用資料整理工具
python centimani_data_organizer.py

# 使用腳本邏輯分析工具
python analyze_scripts_logic.py
```

---

## 技術實現索引

### 🔧 資料讀取技術
- **Excel 讀取**: 使用 pandas 讀取多種 Excel 格式
- **多工作表處理**: 支援複雜的多工作表結構
- **格式相容性**: 支援 .xlsx, .xls, .XLSX 等格式

### 🔄 資料處理技術
- **格式標準化**: 統一不同來源的資料格式
- **數據驗證**: 建立完整的數據驗證機制
- **異常處理**: 處理缺失值和異常值

### 🧠 邏輯分析技術
- **流程建模**: 建立測試流程的邏輯模型
- **關係分析**: 分析測試項目間的邏輯關係
- **模式識別**: 識別常見的測試邏輯模式

### 📤 結果輸出技術
- **多格式輸出**: 支援 JSON, CSV, Markdown 等格式
- **結構化報告**: 生成結構化的分析報告
- **查詢介面**: 提供資料查詢和分析介面

---

## 使用指南

### 📖 初學者指南
1. 從 [Excel 腳本分析報告](excel_analysis_report.md) 開始了解整體概況
2. 查看 [Excel 腳本 AI 參考表](EXCEL_SCRIPTS_AI_REFERENCE_TABLE.md) 了解專案詳情
3. 深入學習 [專案邏輯分析表](PROJECT_LOGIC_ANALYSIS_TABLE.md) 理解邏輯結構

### 🔍 進階使用者指南
1. 直接查詢 [excel_analysis_results.json](excel_analysis_results.json) 獲取原始數據
2. 使用 [excel_analysis_summary.json](excel_analysis_summary.json) 進行快速統計
3. 結合多個參考表進行深度分析和應用開發

### 🤖 AI 開發者指南
1. **首先檢查現有工具**: 使用邏輯模式索引設計 AI 算法
2. **參考 AI 應用場景索引**: 確定開發方向
3. **結合技術實現索引**: 選擇合適的技術方案
4. **遵循最佳實踐**: 在開發前檢查現有工具，避免重複開發

---

## 更新與維護

### 📅 更新頻率
- **分析報告**: 每次 Excel 檔案更新後
- **邏輯分析**: 發現新的邏輯模式時
- **AI 應用**: 根據實際應用需求
- **最佳實踐**: 根據開發經驗持續更新

### 🔄 維護內容
- 新增 Excel 檔案的分析結果
- 更新專案邏輯結構分析
- 補充 AI 應用場景和技術實現
- 優化參考索引的組織結構
- 更新開發最佳實踐建議

### 📝 貢獻方式
- 報告分析結果中的錯誤或遺漏
- 提供新的 AI 應用場景建議
- 分享實際應用中的經驗和改進
- 報告重複開發的情況和改進建議

---

## 聯絡與支援

### 📧 問題回報
如發現分析結果中的問題或有改進建議，請：
1. 檢查是否為已知問題
2. 提供詳細的問題描述
3. 附上相關的 Excel 檔案範例

### 💡 功能建議
歡迎提出新的功能需求：
1. 描述期望的功能特性
2. 說明使用場景和價值
3. 提供實現思路或參考

### 🚀 合作機會
如有合作開發或技術交流需求，請：
1. 說明合作目標和範圍
2. 描述技術能力和資源
3. 提出合作方式和時間安排

---

## 版本資訊

- **當前版本**: v1.1.0
- **更新日期**: 2025-08-11
- **分析範圍**: 5 個專案，52 個 Excel 檔案
- **主要內容**: 專案分析、邏輯結構、AI 應用建議、最佳實踐

---

*本索引專為 AI 系統設計，持續更新中*

## 📚 相關文檔

### 核心參考文檔
- [README.md](../../README.md) - 專案總覽
- [README_AI_Reference_Complete.md](../../README_AI_Reference_Complete.md) - AI 完整參考文件
- [README_AI_Reference_Complete.md](../../README_AI_Reference_Complete.md) - 版本檢查器說明

### AI 參考資料
- [AI_REFERENCE_INDEX.json](../../AI_REFERENCE_INDEX.json) - AI 參考資料索引
- [AI_USAGE_GUIDE.md](../../AI_USAGE_GUIDE.md) - AI 使用指南
- [HOW_TO_USE.md](../../HOW_TO_USE.md) - 使用說明

### 腳本生成相關
- [README_AI_Reference_Complete.md](../../README_AI_Reference_Complete.md) - AI 完整參考文件
- [SCRIPT_EXAMPLES_REFERENCE_FOR_AI.md](../../SCRIPT_EXAMPLES_REFERENCE_FOR_AI.md) - 腳本範例參考
- [templates/](../../templates/) - 腳本模板目錄

### 工具和範例
- [tools/](../../tools/) - 分析工具目錄
- [examples/](../../examples/) - 使用範例目錄
- [best_practices/](../../best_practices/) - 最佳實踐指南 