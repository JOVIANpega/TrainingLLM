# Centimani 資料整理工具 - 完整使用指南

## 🎯 工具概述

這是一套完整的 Centimani 專案資料整理工具，專門用於分析、整理和生成 Centimani DOC 資料夾中的資料速查表和範例。

## 🚀 快速開始

### 方法 1: 一鍵執行 (推薦)
```bash
# 雙擊執行批次檔案
run_organizer.bat
```

### 方法 2: 分步驟執行
```bash
# 1. 安裝套件
pip install -r requirements_organizer.txt

# 2. 執行資料整理
python centimani_data_organizer.py

# 3. 執行增強版 INI 解析
python ini_parser_enhanced.py

# 4. 生成最終整合報告
python final_report_generator.py
```

## 📁 輸出結構

```
organized_data/                    # 基礎分析結果
├── quick_reference/              # 速查表
│   ├── quick_reference.json      # 完整速查表
│   ├── excel_files_overview.csv  # Excel 檔案總覽
│   ├── ini_settings_overview.csv # INI 設定總覽
│   └── test_flow_categories.csv  # 測試流程分類
├── ini_settings_enhanced/        # 增強版 INI 分析
│   ├── enhanced_ini_analysis.json
│   └── enhanced_ini_settings.csv
├── examples.json                 # 範例資料
└── summary_report.md             # 總結報告

final_reports/                    # 最終整合報告
├── comprehensive_report.md       # 完整報告 (Markdown)
├── comprehensive_quick_reference.json # 綜合速查表
├── file_overview_report.csv      # 檔案總覽報告
├── test_flow_detailed_report.csv # 測試流程詳細報告
├── ini_settings_detailed_report.csv # INI 設定詳細報告
└── key_settings_quick_lookup.csv # 關鍵設定快速查詢表
```

## 🔍 主要功能

### 1. Excel 檔案分析
- **自動掃描**: 識別所有 Excel 檔案
- **內容分析**: 提取工作表結構和範例資料
- **關鍵字識別**: 自動識別測試項目和命令
- **分類整理**: 按平台和功能分類

### 2. INI 檔案解析
- **標準格式**: 支援標準 INI 格式
- **增強解析**: 處理非標準註解格式 (//)
- **設定分類**: 按類型分類 (網路、設備、功能開關等)
- **重複處理**: 自動處理重複的設定項目

### 3. 速查表生成
- **多格式輸出**: JSON、CSV、Markdown
- **分類統計**: 檔案數量、大小、類型統計
- **快速查詢**: 按平台、功能、設定類型篩選
- **範例資料**: 提供實際使用範例

## 📊 資料分類

### KANGAROO 平台
| 分類 | 說明 | 檔案範例 |
|------|------|----------|
| Mainboard | 主機板測試流程 | Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx |
| OQC | 出貨品質檢查 | Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx |
| Cellular | 蜂窩網路驗證 | Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx |
| WIFI_BT | WiFi & Bluetooth 校準驗證 | Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX |
| OTA | 韌體升級測試 | Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX |
| MultiDUT | 多設備測試 | Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx |

### VALO360 平台
| 分類 | 說明 | 檔案範例 |
|------|------|----------|
| ER2 | ER2 功能檢查 | VALO360_ER2 OQC Function Check List_202504122_for Factory.xlsx |
| POE | Power over Ethernet 測試 | VALO360_TestFlow_20250307_POE.xlsx |
| IMU | 慣性測量單元測試 | VALO360_TestFlow_20250326_IMU.xlsx |
| Function | 功能驗證測試 | VALO360_TestFlow_20250407_Function.xlsx |
| DMIC | 數位麥克風測試 | Pega_Nokia_TestFlow_20250307_ER2_DMIC.xlsx |

### INI 設定類型
| 類型 | 說明 | 範例 |
|------|------|------|
| Network | 網路相關設定 | IP 位址、埠號 |
| Communication | 通訊設定 | COM 埠、波特率 |
| File_Path | 檔案路徑設定 | 測試流程檔案路徑 |
| Timing | 時間相關設定 | 延遲、超時 |
| Feature_Flag | 功能開關 | 啟用/停用功能 |
| Device_Info | 設備資訊 | 型號、版本、SKU |

## 💡 使用範例

### 1. 找到特定測試流程
```bash
# 要找 KANGAROO 主機板測試流程
# 查看 file_overview_report.csv 中 Category=KANGAROO 的檔案
# 或查看 test_flow_detailed_report.csv 中 Platform=KANGAROO, Category=Mainboard

# 要找 VALO360 ER2 測試流程
# 查看 Platform=VALO360, Category=ER2 的檔案
```

### 2. 配置系統設定
```bash
# 修改網路設定
# 查看 key_settings_quick_lookup.csv 中 Type=Network 的設定
# 主要設定：PCIP_1, DUTIP_1, DUT_UR1, PCUART_fixture

# 修改設備設定
# 查看 Type=Device_Info 的設定
# 主要設定：VALO360_ALL_MODEL, FW_VERSION, Product_SKU
```

### 3. 快速查詢
```bash
# 使用 comprehensive_quick_reference.json 進行程式化查詢
# 使用各種 CSV 檔案進行 Excel 篩選和排序
# 使用 comprehensive_report.md 了解整體結構
```

## 🛠️ 進階功能

### 1. 自定義分析
```python
# 修改 centimani_data_organizer.py 中的分類邏輯
# 調整關鍵字識別規則
# 自定義輸出格式

# 修改 ini_parser_enhanced.py 中的設定類型分類
# 添加新的設定類型
# 自定義設定描述
```

### 2. 批次處理
```bash
# 創建自定義的批次檔案
# 設定定時執行
# 整合到 CI/CD 流程
```

### 3. 資料匯出
```python
# 支援多種輸出格式
# 可自定義 CSV 欄位
# 支援 JSON 格式的程式化處理
```

## 📋 最佳實踐

### 1. 檔案管理
- 使用統一的命名規範
- 定期更新測試項目代碼
- 保持版本一致性
- 備份重要檔案

### 2. 設定管理
- 備份原始 INI 檔案
- 使用註解說明設定用途
- 區分測試和生產環境
- 記錄設定變更

### 3. 測試流程
- 根據設備型號選擇對應流程
- 確認環境設定正確性
- 記錄重要參數和結果
- 定期驗證測試流程

## 🔧 故障排除

### 常見問題

#### 1. Python 套件安裝失敗
```bash
# 使用國內鏡像源
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements_organizer.txt
```

#### 2. 檔案讀取錯誤
- 檢查檔案是否被其他程式佔用
- 確認檔案權限
- 檢查檔案路徑是否正確

#### 3. 記憶體不足
- 關閉其他程式
- 分批處理大型檔案
- 增加系統記憶體

#### 4. 編碼問題
- 確認檔案編碼格式
- 使用 UTF-8 編碼
- 檢查特殊字元

### 日誌檔案
- `centimani_organizer.log`: 主要執行日誌
- 檢查錯誤訊息和警告
- 追蹤執行過程

## 📈 效能優化

### 1. 大型檔案處理
- 使用 `read_only=True` 模式
- 分批讀取資料
- 優化記憶體使用

### 2. 批次處理
- 並行處理多個檔案
- 使用多執行緒
- 優化 I/O 操作

### 3. 輸出優化
- 選擇合適的輸出格式
- 壓縮大型檔案
- 使用增量更新

## 🔄 版本更新

### 當前版本: 1.0.0
- 基礎資料分析功能
- Excel 和 INI 檔案解析
- 多格式輸出支援
- 完整的速查表生成

### 未來計劃
- 支援更多檔案格式
- 圖形化使用者介面
- 即時資料更新
- 雲端同步功能

## 📞 支援與聯絡

### 技術支援
- 檢查日誌檔案
- 參考使用說明
- 查看範例程式碼

### 功能建議
- 記錄使用需求
- 提供改進建議
- 回報問題和錯誤

## 📚 參考資料

- [Python 官方文件](https://docs.python.org/)
- [pandas 使用指南](https://pandas.pydata.org/docs/)
- [openpyxl 文件](https://openpyxl.readthedocs.io/)
- [INI 檔案格式說明](https://en.wikipedia.org/wiki/INI_file)

---

**注意**: 本工具僅供內部使用，請勿外傳或商業使用。
**版本**: 1.0.0
**更新日期**: 2024-12-19
**作者**: AI Assistant 