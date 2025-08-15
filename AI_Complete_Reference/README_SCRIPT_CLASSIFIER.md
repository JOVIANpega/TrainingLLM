# 腳本智能分類工具使用說明

## 🎯 工具概述

腳本智能分類工具是一個強大的腳本管理和分類系統，能夠自動識別、分類和管理各種類型的腳本檔案。該工具結合了規則基礎分類、相似度匹配和機器學習技術，提供準確且智能的腳本分類解決方案。

## 🏗️ 系統架構

### 核心組件
1. **智能分類引擎** - 多維度腳本分析
2. **學習型分類系統** - 機器學習輔助分類
3. **混合分類策略** - 多層次分類決策
4. **自動化分類管理** - 智能分類和學習

### 技術特點
- **多維度分析**: 內容、元資料、結構、語義等多角度分析
- **智能學習**: 基於歷史數據的持續學習和改進
- **高效處理**: 支援批量處理和並行執行
- **靈活配置**: 可自定義分類規則和閾值

## 🚀 快速開始

### 1. 基本使用

```python
from tools.script_classifier import ScriptClassificationManager

# 創建分類管理器
manager = ScriptClassificationManager()

# 分類單個腳本
result = manager.classify_single_script("path/to/script.py")
print(f"分類結果: {result}")

# 分類整個目錄
results = manager.classify_directory("path/to/scripts/")

# 生成分類報告
manager.generate_classification_report(results, "report.json")
```

### 2. 配置自定義

```python
# 自定義配置文件
config = {
    "thresholds": {
        "rule_confidence": 0.8,
        "similarity_threshold": 0.7,
        "ml_confidence": 0.6
    },
    "categories": [
        "KANGAROO_Test",
        "VALO360_Test",
        "Configuration",
        "Utility",
        "Documentation"
    ]
}

# 使用自定義配置
manager = ScriptClassificationManager("custom_config.json")
```

## 📊 分類方法

### 1. 規則基礎分類

#### 關鍵字匹配
- **測試腳本**: `test`, `check`, `verify`, `validate`
- **配置檔案**: `config`, `setting`, `parameter`, `ini`
- **工具腳本**: `utility`, `tool`, `helper`, `function`
- **錯誤處理**: `error`, `exception`, `fail`, `warning`
- **日誌記錄**: `log`, `logging`, `debug`, `info`

#### 檔案模式匹配
- **KANGAROO測試**: `.*kangaroo.*\.(py|exe|bat)$`
- **VALO360測試**: `.*valo360.*\.(py|exe|bat)$`
- **配置文件**: `.*\.ini$`, `.*config.*`, `.*setting.*`
- **工具腳本**: `.*\.py$`, `.*tool.*`, `.*utility.*`
- **文檔檔案**: `.*\.md$`, `.*\.txt$`, `.*readme.*`

### 2. 相似度分類

#### 特徵提取
- **結構特徵**: 函式數量、類別數量、導入數量
- **複雜度特徵**: 嵌套層級、條件語句、循環語句
- **語言特徵**: Python、批次檔、Shell腳本等
- **統計特徵**: 檔案大小、行數、註解密度

#### 相似度計算
```python
# 數值特徵相似度
similarity = 1 - abs(val1 - val2) / max(val1, val2)

# 布林特徵相似度
similarity = 1.0 if val1 == val2 else 0.0

# 字典特徵相似度
similarity = average(key_similarities)
```

### 3. 機器學習分類

#### 特徵工程
- **數值特徵**: 標準化的數值指標
- **分類特徵**: One-hot編碼的類別特徵
- **文本特徵**: TF-IDF關鍵字密度
- **結構特徵**: 程式碼複雜度指標

#### 模型訓練
```python
# 添加訓練資料
manager.add_script_to_database("script.py", "KANGAROO_Test")

# 訓練模型
classifier = manager.classifier.learning_classifier
classifier.train_model()
classifier.save_model()
```

## 🔧 進階功能

### 1. 批量處理

```python
# 分類多個目錄
directories = ["scripts/", "tools/", "tests/"]
all_results = []

for directory in directories:
    results = manager.classify_directory(directory)
    all_results.extend(results)

# 生成綜合報告
manager.generate_classification_report(all_results, "comprehensive_report.json")
```

### 2. 自定義分類規則

```python
# 創建自定義規則
custom_rules = {
    "Custom_Category": [
        {"type": "keyword", "value": "custom_keyword", "weight": 0.9},
        {"type": "file_pattern", "value": r".*custom.*", "weight": 0.8}
    ]
}

# 應用自定義規則
classifier = manager.classifier.rule_classifier
classifier.rules.update(custom_rules)
```

### 3. 分類結果驗證

```python
# 驗證分類結果
def validate_classification(result):
    if result["confidence"] < 0.5:
        print(f"低置信度分類: {result['script_path']}")
        print(f"建議人工審核")
    
    if result["method"] == "error":
        print(f"分類錯誤: {result['error']}")

# 應用驗證
for result in results:
    validate_classification(result)
```

## 📈 效能優化

### 1. 快取機制
- **內容快取**: 避免重複讀取檔案內容
- **元資料快取**: 快取檔案統計資訊
- **相似度快取**: 快取計算結果

### 2. 並行處理
```python
# 多執行緒處理
num_threads = min(4, len(script_paths))
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=classify_worker)
    thread.start()
    threads.append(thread)
```

### 3. 記憶體管理
- **批次處理**: 分批處理大型腳本集合
- **資源釋放**: 及時釋放不需要的資源
- **記憶體監控**: 監控記憶體使用情況

## 📝 輸出格式

### 1. JSON格式
```json
{
  "timestamp": "2024-12-19T10:30:00",
  "total_scripts": 150,
  "classification_summary": {
    "KANGAROO_Test": 45,
    "VALO360_Test": 38,
    "Configuration": 25,
    "Utility": 22,
    "Documentation": 20
  },
  "detailed_results": [...],
  "statistics": {
    "average_confidence": 0.85,
    "min_confidence": 0.45,
    "max_confidence": 0.98
  }
}
```

### 2. CSV格式
```csv
script_path,category,confidence,method,timestamp
script1.py,KANGAROO_Test,0.92,rule_based,2024-12-19T10:30:00
script2.py,VALO360_Test,0.87,similarity_based,2024-12-19T10:30:01
```

### 3. 日誌格式
```log
2024-12-19 10:30:00 - INFO - 腳本分類完成: script.py -> KANGAROO_Test (置信度: 0.92)
2024-12-19 10:30:01 - INFO - 批量分類完成，共處理 150 個腳本
```

## 🚨 錯誤處理

### 1. 常見錯誤
- **檔案不存在**: 檢查檔案路徑是否正確
- **權限不足**: 確保有讀取檔案的權限
- **編碼錯誤**: 處理不同編碼格式的檔案
- **記憶體不足**: 分批處理大型檔案集合

### 2. 錯誤恢復
```python
try:
    result = manager.classify_single_script(script_path)
except FileNotFoundError:
    print(f"檔案不存在: {script_path}")
except PermissionError:
    print(f"權限不足: {script_path}")
except Exception as e:
    print(f"未知錯誤: {e}")
    # 記錄錯誤到日誌
    manager.classifier.logger.log_classification_error(script_path, e, "main")
```

## 🔍 監控和維護

### 1. 日誌監控
- **分類日誌**: `classification.log`
- **錯誤日誌**: `classification_errors.log`
- **系統日誌**: 標準Python日誌

### 2. 效能監控
```python
import time

start_time = time.time()
results = manager.classify_directory("scripts/")
end_time = time.time()

processing_time = end_time - start_time
scripts_per_second = len(results) / processing_time

print(f"處理速度: {scripts_per_second:.2f} 腳本/秒")
```

### 3. 品質評估
- **分類準確率**: 定期評估分類結果的準確性
- **置信度分析**: 分析分類置信度的分佈
- **錯誤模式**: 識別常見的分類錯誤模式

## 📚 最佳實踐

### 1. 分類策略
- **漸進式部署**: 先在小範圍測試，再逐步推廣
- **規則優先**: 優先使用明確的規則進行分類
- **學習改進**: 持續收集反饋，改進分類模型
- **人工審核**: 低置信度結果需要人工審核

### 2. 效能優化
- **批次處理**: 批量處理腳本，減少I/O開銷
- **快取策略**: 合理使用快取，避免重複計算
- **並行處理**: 利用多執行緒提升處理速度
- **記憶體管理**: 及時釋放不需要的資源

### 3. 維護管理
- **定期更新**: 定期更新分類規則和模型
- **備份策略**: 備份重要的配置和模型檔案
- **版本控制**: 使用版本控制管理配置變更
- **文檔維護**: 及時更新使用說明和配置文檔

## 🤝 支援和聯絡

### 1. 技術支援
- 檢查日誌檔案獲取詳細錯誤資訊
- 參考配置檔案了解系統設定
- 查看範例程式碼學習使用方法

### 2. 問題回報
- 記錄錯誤發生的具體情況
- 提供相關的配置和環境資訊
- 附上錯誤日誌和堆疊追蹤

### 3. 功能建議
- 描述期望的功能和改進
- 提供具體的使用場景
- 說明對工作流程的影響

---

**注意**: 本工具專為腳本管理和分類設計，請根據實際需求進行調整和擴展。
**版本**: 1.0.0
**更新日期**: 2024-12-19
**作者**: AI Assistant 