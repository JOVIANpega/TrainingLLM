# Centimani 資料整理工具

## 功能說明

這個工具專門用於整理和分析 Centimani DOC 資料夾中的資料，主要功能包括：

### 🔍 資料分析
- **Excel 檔案分析**: 自動掃描並分析所有 Excel 檔案
- **INI 檔案解析**: 解析系統設定檔案
- **關鍵字提取**: 識別重要的測試項目和命令

### 📊 速查表生成
- **檔案分類**: 按平台和功能分類檔案
- **測試流程分類**: 整理 KANGAROO 和 VALO360 測試流程
- **設定參考**: 生成 INI 設定速查表

### 📁 輸出結構
```
organized_data/
├── quick_reference/          # 速查表
│   ├── quick_reference.json  # 完整速查表 (JSON)
│   ├── excel_files_overview.csv    # Excel 檔案總覽
│   ├── ini_settings_overview.csv   # INI 設定總覽
│   └── test_flow_categories.csv    # 測試流程分類
├── excel_summaries/          # Excel 分析結果
├── ini_settings/             # INI 設定分析
├── examples.json             # 範例資料
└── summary_report.md         # 總結報告
```

## 使用方法

### 方法 1: 使用批次檔案 (推薦)
1. 雙擊 `run_organizer.bat`
2. 工具會自動安裝所需套件並執行
3. 等待分析完成

### 方法 2: 手動執行
1. 安裝 Python 套件：
   ```bash
   pip install -r requirements_organizer.txt
   ```

2. 執行工具：
   ```bash
   python centimani_data_organizer.py
   ```

## 系統需求

- Python 3.7 或更新版本
- 所需套件：
  - pandas >= 1.3.0
  - openpyxl >= 3.0.0
  - configparser (內建)
  - pathlib (內建)

## 輸出說明

### 1. 速查表 (quick_reference.json)
包含完整的資料分析結果，適合程式化處理

### 2. CSV 檔案
- **excel_files_overview.csv**: Excel 檔案分類總覽
- **ini_settings_overview.csv**: INI 設定詳細清單
- **test_flow_categories.csv**: 測試流程分類表

### 3. 範例資料 (examples.json)
提供實際資料結構範例，幫助理解資料格式

### 4. 總結報告 (summary_report.md)
人類可讀的分析報告，包含統計資訊和使用建議

## 資料分類

### KANGAROO 平台
- **Mainboard**: 主機板測試流程
- **OQC**: 出貨品質檢查
- **Cellular**: 蜂窩網路驗證
- **WIFI_BT**: WiFi & Bluetooth 校準驗證
- **OTA**: 韌體升級測試
- **MultiDUT**: 多設備測試

### VALO360 平台
- **ER2**: ER2 功能檢查
- **POE**: Power over Ethernet 測試
- **IMU**: 慣性測量單元測試
- **Function**: 功能驗證測試
- **DMIC**: 數位麥克風測試

## 注意事項

1. **資料夾結構**: 確保 `Centimani DOC` 資料夾存在於工具同一目錄
2. **檔案權限**: 工具需要讀取 Excel 和 INI 檔案的權限
3. **記憶體使用**: 大型 Excel 檔案可能需要較多記憶體
4. **執行時間**: 檔案數量多時，分析可能需要幾分鐘

## 故障排除

### 常見問題
1. **找不到 Python**: 請安裝 Python 並確保在 PATH 中
2. **套件安裝失敗**: 檢查網路連線，或使用國內鏡像源
3. **檔案讀取錯誤**: 檢查檔案是否被其他程式佔用
4. **記憶體不足**: 關閉其他程式，或分批處理檔案

### 日誌檔案
工具執行時會生成 `centimani_organizer.log` 檔案，包含詳細的執行記錄和錯誤資訊。

## 版本資訊

- **版本**: 1.0.0
- **更新日期**: 2024-12-19
- **作者**: AI Assistant
- **功能**: 初始版本，包含基本的資料分析和速查表生成功能 