# AI 參考工具使用指南

## 🎯 工具概述

這套工具集專門為其他 AI 助手設計，提供了完整的資料分析和整理功能。所有工具都基於 Centimani 資料整理專案的設計模式，具有良好的可讀性、可維護性和可擴展性。

## 🛠️ 工具架構

### 1. 核心工具
- **centimani_data_organizer.py**: 主要的資料整理工具
- **ini_parser_enhanced.py**: 增強版 INI 檔案解析器  
- **final_report_generator.py**: 最終整合報告生成器

### 2. 腳本分析工具
- **腳本範例參考系統**: 27個腳本文件的完整分析
- **專案分類指南**: 5個專案類型的腳本特點分析
- **AI學習指南**: 腳本結構和組織模式學習

### 2. 設計原則
- **模組化**: 每個工具專注於特定功能
- **類別封裝**: 使用類別管理狀態和行為
- **錯誤處理**: 完整的異常處理和日誌記錄
- **多格式輸出**: 支援 JSON、CSV、Markdown 等格式

## 💡 使用模式

### 模式 1: 資料分析流程
```python
# 1. 分析 Excel 檔案
organizer = CentimaniDataOrganizer()
organizer.run_analysis()

# 2. 解析 INI 設定
parser = EnhancedINIParser()
result = parser.parse_file("config.ini")

# 3. 生成整合報告
generator = FinalReportGenerator()
generator.run_generation()
```

### 模式 2: 自定義分析
```python
# 修改分類邏輯
def categorize_files(self):
    # 自定義檔案分類邏輯
    pass

# 修改輸出格式
def generate_output(self):
    # 自定義輸出格式
    pass
```

### 模式 3: 擴展功能
```python
# 添加新的檔案類型支援
def analyze_new_file_type(self, file_path):
    # 實現新的檔案類型分析
    pass

# 添加新的輸出格式
def export_to_new_format(self, data):
    # 實現新的輸出格式
    pass
```

## 🔧 技術特點

### 1. 程式碼結構
- 清晰的函式命名 (on_ 開頭的 callback 函式)
- 完整的 docstring 和註解
- 模組化的類別設計
- 統一的錯誤處理模式

### 2. 資料處理
- 支援大型檔案處理
- 記憶體優化的讀取方式
- 批次處理和並行處理支援
- 多種資料格式的轉換

### 3. 輸出格式
- JSON: 程式化處理
- CSV: 表格化分析
- Markdown: 人類可讀
- 自定義格式支援

## 📚 學習資源

### 1. 範例檔案
- `examples/organized_data/`: 基礎分析結果
- `examples/final_reports/`: 最終整合報告
- `examples/`: 各種輸出格式範例

### 2. 說明文件
- `documentation/README_Data_Organizer.md`: 基礎使用說明
- `documentation/README_Final_Usage.md`: 完整使用指南
- `AI_REFERENCE_INDEX.json`: 工具索引和說明

### 3. 最佳實踐
- 模組化設計原則
- 錯誤處理策略
- 效能優化技巧
- 擴展性設計

### 4. 腳本學習資源
- **SCRIPT_EXAMPLES_REFERENCE_FOR_AI.md**: 完整的腳本範例參考
- **專案分類系統**: KANGAROO、VALO360、RAPTOR、Kilimanjaro、ZEBRA
- **腳本統計分析**: 27個腳本的詳細統計和覆蓋分析
- **AI學習指南**: 腳本結構分析和最佳實踐提取

## 🚀 快速開始

### 1. 了解工具結構
```bash
# 查看工具索引
cat AI_REFERENCE_INDEX.json

# 查看主要工具
ls tools/
```

### 2. 執行範例
```bash
# 安裝依賴
pip install -r tools/requirements.txt

# 執行資料整理
python tools/centimani_data_organizer.py
```

### 3. 自定義使用
```python
# 導入工具
from tools.centimani_data_organizer import CentimaniDataOrganizer

# 自定義使用
organizer = CentimaniDataOrganizer()
# 修改參數和邏輯
```

## 🔍 常見使用場景

### 1. 檔案分析
- 批量分析 Excel 檔案
- 提取關鍵資訊和結構
- 生成檔案分類和統計

### 2. 設定解析
- 解析各種格式的設定檔案
- 提取關鍵設定項目
- 生成設定參考表

### 3. 報告生成
- 整合多個分析結果
- 生成多格式報告
- 創建速查表和範例

### 4. 資料整理
- 分類和標籤化資料
- 建立資料索引
- 生成查詢工具

## 🔄 新增腳本分類解決方案

### 1. 智能分類引擎

#### 核心架構
```python
class SmartScriptClassifier:
    def __init__(self):
        self.classification_rules = {}
        self.pattern_database = {}
        self.learning_engine = None
    
    def classify_script(self, script_content, script_metadata):
        """智能分類腳本內容"""
        # 多維度分析
        content_score = self.analyze_content_patterns(script_content)
        metadata_score = self.analyze_metadata_patterns(script_metadata)
        context_score = self.analyze_context_relationships(script_content)
        
        # 綜合評分和分類
        final_classification = self.combine_scores(
            content_score, metadata_score, context_score
        )
        return final_classification
```

#### 分類維度
- **內容模式分析**: 腳本語言、語法結構、關鍵字密度
- **元資料分析**: 檔案名稱、路徑、修改時間、大小
- **上下文關係**: 與其他腳本的關聯性、依賴關係
- **功能特徵**: 測試類型、目標設備、執行環境

### 2. 學習型分類系統

#### 機器學習整合
```python
class LearningClassifier:
    def __init__(self):
        self.training_data = []
        self.model = None
        self.feature_extractor = None
    
    def train_on_existing_scripts(self, script_collection):
        """基於現有腳本集合訓練分類模型"""
        features = self.extract_features(script_collection)
        labels = self.get_manual_labels(script_collection)
        
        # 訓練分類模型
        self.model.fit(features, labels)
        
    def predict_script_category(self, new_script):
        """預測新腳本的分類"""
        features = self.extract_features([new_script])
        prediction = self.model.predict(features)
        confidence = self.model.predict_proba(features)
        return prediction, confidence
```

#### 特徵提取策略
- **文本特徵**: TF-IDF、關鍵字頻率、語法模式
- **結構特徵**: 函式數量、變數命名、註解密度
- **語義特徵**: 測試邏輯、錯誤處理、日誌記錄
- **統計特徵**: 程式碼行數、複雜度指標、重複度

### 3. 混合分類策略

#### 多層次分類架構
```python
class HybridClassifier:
    def __init__(self):
        self.rule_based_classifier = RuleBasedClassifier()
        self.ml_classifier = LearningClassifier()
        self.similarity_classifier = SimilarityClassifier()
    
    def classify_with_hybrid_approach(self, script):
        """使用混合策略進行分類"""
        # 第一層：規則基礎分類
        rule_result = self.rule_based_classifier.classify(script)
        
        if rule_result.confidence > 0.8:
            return rule_result
        
        # 第二層：相似度分類
        similarity_result = self.similarity_classifier.find_similar(script)
        
        if similarity_result.similarity > 0.7:
            return similarity_result
        
        # 第三層：機器學習分類
        ml_result = self.ml_classifier.predict(script)
        
        # 綜合決策
        return self.combine_classification_results(
            rule_result, similarity_result, ml_result
        )
```

#### 分類優先級策略
1. **高置信度規則**: 明確的關鍵字和模式匹配
2. **相似度匹配**: 與已知腳本的結構相似性
3. **機器學習預測**: 基於歷史數據的模式識別
4. **人工審核**: 低置信度情況下的專家判斷

### 4. 實現技術細節

#### 配置管理
```python
class ClassificationConfig:
    def __init__(self):
        self.rules_file = "classification_rules.json"
        self.model_file = "classification_model.pkl"
        self.thresholds = {
            "rule_confidence": 0.8,
            "similarity_threshold": 0.7,
            "ml_confidence": 0.6
        }
        self.categories = [
            "KANGAROO_Test",
            "VALO360_Test", 
            "Configuration",
            "Utility",
            "Documentation"
        ]
```

#### 效能優化
- **快取機制**: 分類結果快取，避免重複計算
- **並行處理**: 多腳本同時分類，提升處理速度
- **增量學習**: 新腳本加入後自動更新模型
- **記憶體管理**: 大型腳本集合的記憶體優化

#### 錯誤處理和日誌
```python
class ClassificationLogger:
    def __init__(self):
        self.log_file = "classification.log"
        self.error_file = "classification_errors.log"
    
    def log_classification_result(self, script_path, result, confidence):
        """記錄分類結果"""
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "script_path": script_path,
            "classification": result,
            "confidence": confidence,
            "method": "hybrid"
        }
        self.write_log(log_entry)
    
    def log_classification_error(self, script_path, error, context):
        """記錄分類錯誤"""
        error_entry = {
            "timestamp": datetime.now().isoformat(),
            "script_path": script_path,
            "error": str(error),
            "context": context
        }
        self.write_error_log(error_entry)
```

### 5. 預期效果

#### 使用者體驗提升
- **自動分類**: 新腳本加入後自動獲得合適分類
- **智能建議**: 根據腳本內容提供分類建議
- **快速搜尋**: 基於分類的快速腳本定位
- **一致性維護**: 確保分類標準的一致性

#### 腳本品質改善
- **標準化**: 統一的腳本結構和命名規範
- **可維護性**: 清晰的分類有助於維護和更新
- **重用性**: 相似腳本的快速識別和重用
- **文檔化**: 自動生成分類相關的文檔

### 6. 使用場景

#### 開發階段
- **新腳本開發**: 開發完成後自動分類
- **腳本重構**: 重構後重新分類
- **版本控制**: 不同版本的腳本分類管理

#### 維護階段
- **腳本更新**: 更新後的分類調整
- **問題診斷**: 基於分類的問題定位
- **效能優化**: 分類相關的效能分析

#### 團隊協作
- **知識共享**: 團隊成員快速找到相關腳本
- **標準制定**: 基於分類的開發標準
- **培訓支援**: 新成員的腳本學習

### 7. 注意事項

#### 實現過程
- **漸進式部署**: 先在小範圍測試，再逐步推廣
- **回饋機制**: 建立分類準確性的回饋機制
- **定期評估**: 定期評估分類系統的效能
- **持續改進**: 根據使用情況持續優化

#### 技術考量
- **資料品質**: 確保訓練資料的品質和多樣性
- **效能平衡**: 分類準確性與處理速度的平衡
- **擴展性**: 支援新腳本類型和分類標準
- **相容性**: 與現有腳本管理系統的相容性

#### 維護管理
- **規則更新**: 定期更新分類規則和模型
- **品質監控**: 監控分類結果的品質
- **備份恢復**: 分類配置和模型的備份策略
- **版本控制**: 分類系統的版本管理

## 🔄 Centimani腳本格式學習與改進

### 1. 格式分析經驗

#### 範例檔案結構分析
通過分析Centimani DOC資料夾中的Excel範例檔案，發現了標準的腳本格式：

**KANGAROO腳本結構**:
- **Properties工作表**: 19 x 2 - 腳本基本資訊
- **Switch工作表**: 6 x 7 - 開關配置
- **Instrument工作表**: 45 x 9 - 儀器配置  
- **DUTs工作表**: 4 x 16 - 被測設備配置
- **測試流程工作表**: 124 x 256 - 具體測試項目

**VALO360腳本結構**:
- **OQC工作表**: 21 x 7 - 品質檢查配置
- **VLC工作表**: 46 x 9 - 視覺檢查配置
- **WebUI工作表**: 130 x 12 - 網頁介面配置
- **WiFi工作表**: 140 x 4 - WiFi測試配置
- **5G工作表**: 109 x 18 - 5G測試配置

#### 關鍵發現
1. **標準化工作表**: 所有腳本都有固定的工作表結構
2. **配置導向**: 腳本主要包含配置資訊而非執行邏輯
3. **測試項目**: 測試流程以表格形式定義，包含步驟、參數、預期結果
4. **儀器管理**: 統一的儀器配置和開關管理方式

### 2. 腳本創建邏輯

#### 核心架構設計
```python
class CentimaniTestScript:
    """Centimani格式測試腳本生成器"""
    
    def __init__(self):
        self.script_data = {
            "properties": {},      # 腳本屬性
            "switches": [],        # 開關配置
            "instruments": [],     # 儀器配置
            "duts": [],           # 被測設備
            "test_items": []      # 測試項目
        }
```

#### 工作表創建邏輯
1. **Properties工作表**: 腳本基本資訊和版本管理
2. **Switch工作表**: 測試開關和路由配置
3. **Instrument工作表**: 測試儀器配置和功能
4. **DUTs工作表**: 被測設備配置
5. **Test_Items工作表**: 具體測試流程和參數

### 3. 功能實現經驗

#### 版本號碼管理
- **版本格式**: 主版本.次版本.修補版本-建置編號
- **自動生成**: 基於時間戳的版本號碼生成
- **變更追蹤**: 完整的版本變更歷史記錄

#### 量測功能配置
- **電壓量測**: 多通道、精度、採樣率配置
- **藍牙量測**: 掃描、連接、協議測試配置
- **儀器整合**: 統一的儀器管理和配置

#### 測試項目定義
- **步驟編號**: 有序的測試步驟定義
- **參數配置**: 詳細的測試參數設定
- **預期結果**: 明確的測試結果期望
- **超時設定**: 測試執行時間限制

### 4. 格式驗證與改進

#### 驗證機制
```python
def verify_excel_file(file_path):
    """驗證Excel檔案結構"""
    expected_sheets = ["Properties", "Switch", "Instrument", "DUTs", "Test_Items"]
    # 檢查工作表存在性
    # 驗證欄位結構
    # 檢查數據完整性
```

#### 改進方向
1. **欄位映射**: 需要更精確的欄位對應關係
2. **數據格式**: 某些欄位的數據格式需要調整
3. **樣式統一**: 與範例檔案的視覺樣式保持一致
4. **功能擴展**: 支援更多測試類型和配置選項

### 5. 學習收穫

#### 格式理解
- **配置優先**: Centimani腳本以配置為主，執行邏輯為輔
- **結構化**: 嚴格的表格結構和欄位定義
- **專業性**: 針對測試環境的專業腳本格式

#### 技術實現
- **Excel操作**: 使用openpyxl進行專業Excel檔案操作
- **樣式管理**: 統一的字體、顏色、對齊樣式
- **數據組織**: 結構化的數據組織和管理

#### 改進空間
- **執行邏輯**: 當前腳本缺少實際的執行邏輯
- **錯誤處理**: 需要更完善的錯誤處理機制
- **用戶介面**: 可以考慮添加圖形化配置介面

### 6. 下一步改進計劃

#### 短期目標
1. **完善欄位映射**: 修正測試項目工作表的欄位對應
2. **統一樣式**: 與範例檔案保持一致的視覺樣式
3. **添加驗證**: 更完善的格式驗證機制

#### 中期目標
1. **執行引擎**: 開發腳本執行引擎
2. **配置介面**: 圖形化配置工具
3. **測試報告**: 自動化測試報告生成

#### 長期目標
1. **腳本庫**: 建立標準腳本庫
2. **版本管理**: 完整的腳本版本管理系統
3. **協作平台**: 團隊腳本協作平台

### 7. 經驗總結

#### 成功要素
1. **深入分析**: 仔細分析範例檔案的結構和格式
2. **模組化設計**: 將腳本生成分解為多個獨立模組
3. **驗證機制**: 建立完整的格式驗證機制
4. **迭代改進**: 基於驗證結果持續改進

#### 注意事項
1. **格式一致性**: 嚴格遵循Centimani標準格式
2. **數據完整性**: 確保所有必要欄位都有適當的數據
3. **樣式統一**: 保持與範例檔案的視覺一致性
4. **功能驗證**: 確保生成的腳本能夠正常使用

#### 最佳實踐
1. **先分析後實現**: 深入理解需求再開始編程
2. **模組化開發**: 將複雜功能分解為可管理的模組
3. **持續驗證**: 每個階段都進行充分的驗證
4. **文檔記錄**: 詳細記錄開發過程和經驗教訓

## 📝 開發建議

### 1. 擴展工具
- 保持模組化設計
- 添加新的檔案類型支援
- 實現新的輸出格式
- 優化效能和記憶體使用

### 2. 自定義分類
- 修改關鍵字識別規則
- 調整檔案分類邏輯
- 自定義設定類型
- 添加新的分析維度

### 3. 整合其他工具
- 與其他 AI 工具整合
- 支援更多檔案格式
- 添加圖形化介面
- 實現雲端功能

## 🤝 貢獻指南

### 1. 改進建議
- 記錄使用體驗
- 提出功能需求
- 回報問題和錯誤
- 提供改進建議

### 2. 程式碼貢獻
- 遵循現有的程式碼風格
- 添加完整的註解和文檔
- 包含測試和範例
- 更新相關文檔

## 📞 支援與聯絡

### 1. 技術支援
- 檢查日誌檔案
- 參考使用說明
- 查看範例程式碼
- 分析錯誤訊息

### 2. 功能建議
- 記錄使用需求
- 提供改進建議
- 回報問題和錯誤
- 分享使用經驗

---

**注意**: 本工具集專為 AI 助手設計，請根據實際需求進行調整和擴展。
**版本**: 1.0.0
**更新日期**: 2024-12-19
**作者**: AI Assistant 