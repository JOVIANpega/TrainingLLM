# Centimani 資料整合報告

## 生成時間
2025-08-11 11:13:42

## 資料概覽

### 檔案統計
- **總檔案數**: 22
- **主要平台**: KANGAROO, VALO360, Centimani
- **檔案類型**: Excel 測試流程、INI 設定、測試項目代碼

### 平台分類

#### KANGAROO 平台
- 主機板測試流程
- OQC 出貨品質檢查
- 蜂窩網路驗證
- WiFi & Bluetooth 校準驗證
- OTA 韌體升級測試
- 多設備測試

#### VALO360 平台
- ER2 功能檢查
- POE 測試流程
- IMU 測試流程
- 功能驗證測試
- DMIC 測試流程

#### Centimani 工具
- INI 設定檔案
- 儀器參數設定
- 腳本使用指南

## 快速查詢指南

### 1. 找到特定測試流程
- 使用 `file_overview_report.csv` 按類別篩選
- 使用 `test_flow_detailed_report.csv` 按平台和功能篩選

### 2. 配置系統設定
- 使用 `ini_settings_detailed_report.csv` 查看所有設定
- 使用 `key_settings_quick_lookup.csv` 快速找到重要設定

### 3. 檔案組織結構
- 按平台分類：KANGAROO、VALO360
- 按功能分類：Mainboard、OQC、Cellular、WiFi_BT、OTA、ER2、POE、IMU

## 使用範例

### 測試流程選擇
1. 確認設備平台 (KANGAROO 或 VALO360)
2. 選擇測試類型 (主機板、OQC、蜂窩網路等)
3. 根據日期選擇最新版本

### 設定配置
1. 修改網路設定 (IP 位址、埠號)
2. 配置設備參數 (型號、版本)
3. 啟用/停用功能開關

## 最佳實踐

### 檔案管理
- 使用統一的命名規範
- 定期更新測試項目代碼
- 保持版本一致性

### 配置管理
- 備份原始設定檔案
- 使用註解說明設定用途
- 區分測試和生產環境

### 測試流程
- 根據設備型號選擇對應流程
- 確認環境設定正確性
- 記錄重要參數和結果

## 輸出檔案說明

- **comprehensive_quick_reference.json**: 完整的速查表 (JSON 格式)
- **file_overview_report.csv**: 檔案總覽報告
- **test_flow_detailed_report.csv**: 測試流程詳細報告
- **ini_settings_detailed_report.csv**: INI 設定詳細報告
- **key_settings_quick_lookup.csv**: 關鍵設定快速查詢表

## 聯絡資訊

如有問題或建議，請參考原始資料或聯絡系統管理員。
