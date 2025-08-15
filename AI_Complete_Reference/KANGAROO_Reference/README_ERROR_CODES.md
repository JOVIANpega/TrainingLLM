# KANGAROO ERROR CODE 速查表

## 概述
本目錄包含 KANGAROO 專案的測試項目代碼和錯誤代碼速查表，已轉換成 AI 友好的格式，便於快速查詢和分析。

## 檔案說明

### 1. error_code_comprehensive.json (完整版)
- **大小**: 13MB
- **內容**: 包含所有工作表的完整資料
- **用途**: 完整資料分析、深度查詢、資料挖掘
- **格式**: 結構化 JSON，支援巢狀查詢

### 2. error_code_simplified.json (簡化版)
- **大小**: 30KB
- **內容**: 核心錯誤代碼和測試項目資訊
- **用途**: 快速查詢、日常參考、API 整合
- **格式**: 精簡 JSON，重點突出

### 3. error_code_quick_reference.csv (快速參考)
- **大小**: 16KB
- **內容**: 錯誤代碼的快速查詢表格
- **用途**: Excel 分析、資料篩選、統計分析
- **格式**: CSV 表格，適合 pandas 處理

## 資料統計

### 工作表資訊
- **總工作表數**: 4
- **工作表名稱**:
  - 七碼定義Definition
  - Test Item All
  - Version History
  - 工作表1

### 資料量統計
- **總錯誤代碼數**: 111
- **總測試項目數**: 30,404
- **資料來源**: Test Item Code V2.04_20250310.xlsx

## 使用方式

### 1. Python 程式讀取

```python
import json
import pandas as pd

# 讀取簡化版本（推薦）
with open('error_code_simplified.json', 'r', encoding='utf-8') as f:
    error_codes = json.load(f)

# 讀取快速參考 CSV
quick_ref = pd.read_csv('error_code_quick_reference.csv', encoding='utf-8-sig')

# 讀取完整版本（需要大量記憶體）
with open('error_code_comprehensive.json', 'r', encoding='utf-8') as f:
    full_data = json.load(f)
```

### 2. 錯誤代碼查詢

```python
# 查詢特定工作表的錯誤代碼
def find_error_code(code, sheet_name=None):
    if sheet_name:
        if sheet_name in error_codes['error_codes']:
            for error in error_codes['error_codes'][sheet_name]:
                if error['code'] == code:
                    return error
    else:
        # 在所有工作表中搜尋
        for sheet, errors in error_codes['error_codes'].items():
            for error in errors:
                if error['code'] == code:
                    return error
    return None

# 使用範例
error_info = find_error_code(1001, "Test Item All")
```

### 3. 測試項目分類

```python
# 按類別統計測試項目
def analyze_test_items():
    categories = {}
    for sheet_name, items in error_codes['test_item_categories'].items():
        categories[sheet_name] = len(items)
    return categories

# 使用範例
item_stats = analyze_test_items()
print(f"各工作表測試項目數量: {item_stats}")
```

## 資料結構

### 錯誤代碼結構
```json
{
  "code": 錯誤代碼數字,
  "row_data": {
    "欄位名稱": "欄位值",
    ...
  },
  "sheet": "工作表名稱"
}
```

### 測試項目結構
```json
{
  "item": "測試項目名稱",
  "row_data": {
    "欄位名稱": "欄位值",
    ...
  },
  "sheet": "工作表名稱"
}
```

## 常見查詢場景

### 1. 錯誤代碼診斷
- 根據錯誤代碼查詢詳細資訊
- 分析錯誤代碼的分佈和頻率
- 建立錯誤代碼與測試項目的關聯

### 2. 測試項目管理
- 統計各類測試項目的數量
- 分析測試項目的複雜度
- 建立測試項目的分類體系

### 3. 品質分析
- 分析錯誤代碼的趨勢
- 識別高風險測試項目
- 優化測試流程和策略

## 注意事項

1. **檔案大小**: 完整版檔案較大，建議根據需求選擇合適的版本
2. **編碼格式**: 所有檔案使用 UTF-8 編碼
3. **資料更新**: 當原始 Excel 檔案更新時，需要重新執行解析腳本
4. **記憶體使用**: 讀取完整版時需要足夠的記憶體空間

## 更新記錄

- **V2.04**: 2025年3月10日版本
- **解析時間**: 2024年12月
- **資料格式**: AI 友好結構化格式
- **支援工具**: Python、pandas、JSON、CSV

## 相關檔案

- **原始檔案**: `Centimani DOC/scripe_EXCEL/KANGAROO/Test Item Code V2.04_20250310.xlsx`
- **解析腳本**: `error_code_parser.py`
- **整合目錄**: `AI_Complete_Reference/`

---
*本速查表專為 AI 軟體和開發者設計，持續更新中* 