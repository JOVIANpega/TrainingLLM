# AI Complete Reference - 統一參考指南

## 🎯 專案概述

這是TrainingLLM專案的AI完整參考資料庫，整合了所有Centimani腳本分析、生成、最佳實踐和工具。

## 📁 目錄結構

```
AI_Complete_Reference/
├── 00_MAIN_INDEX/                    # 主要索引和導航
│   ├── README.md                     # 本檔案 - 主導航
│   ├── AI_REFERENCE_INDEX.json      # AI索引資料
│   └── QUICK_START_GUIDE.md         # 快速開始指南
│
├── 01_CORE_REFERENCE/               # 核心參考資料
│   ├── Centimani_Script_Editing_Complete_Quick_Reference.md
│   ├── Script_Structure_Reference.md
│   └── Test_Item_Codes_Reference.md
│
├── 02_SCRIPT_ANALYSIS/              # 腳本分析結果
│   ├── VALO360_Analysis/
│   ├── KANGAROO_Analysis/
│   ├── RAPTOR_Analysis/
│   └── Kilimanjaro_Analysis/
│
├── 03_SCRIPT_GENERATION/            # 腳本生成相關
│   ├── Generation_Logic_Reference.md
│   ├── Design_Patterns.md
│   └── Decision_Tree.md
│
├── 04_TOOLS_AND_UTILITIES/          # 工具和實用程式
│   ├── unified_centimani_script_analyzer.py
│   ├── unified_centimani_script_generator.py
│   └── modify_script_content.py
│
├── 05_EXAMPLES_AND_TEMPLATES/       # 範例和模板
│   ├── Script_Templates/
│   ├── INI_Templates/
│   └── Test_Examples/
│
├── 06_BEST_PRACTICES/               # 最佳實踐
│   ├── Development_Best_Practices.md
│   ├── Error_Handling_Guide.md
│   └── Optimization_Strategies.md
│
└── 07_DOCUMENTATION/                # 文檔和說明
    ├── User_Guides/
    ├── API_Reference/
    └── Troubleshooting/
```

## 🚀 快速導航

### **核心參考資料**
- **[Centimani腳本編輯完整快速參考](01_CORE_REFERENCE/Centimani_Script_Editing_Complete_Quick_Reference.md)** - 最重要的參考資料
- **[腳本結構參考](01_CORE_REFERENCE/Script_Structure_Reference.md)** - 腳本結構詳細說明
- **[測試項目代碼參考](01_CORE_REFERENCE/Test_Item_Codes_Reference.md)** - 測試代碼快速查詢

### **腳本分析結果**
- **[VALO360專案分析](02_SCRIPT_ANALYSIS/VALO360_Analysis/)** - VALO360腳本分析報告
- **[KANGAROO專案分析](02_SCRIPT_ANALYSIS/KANGAROO_Analysis/)** - KANGAROO腳本分析報告
- **[RAPTOR專案分析](02_SCRIPT_ANALYSIS/RAPTOR_Analysis/)** - RAPTOR腳本分析報告
- **[Kilimanjaro專案分析](02_SCRIPT_ANALYSIS/Kilimanjaro_Analysis/)** - Kilimanjaro腳本分析報告

### **腳本生成工具**
- **[腳本分析器](04_TOOLS_AND_UTILITIES/unified_centimani_script_analyzer.py)** - 統一的腳本分析工具
- **[腳本生成器](04_TOOLS_AND_UTILITIES/unified_centimani_script_generator.py)** - 統一的腳本生成工具
- **[腳本修改工具](04_TOOLS_AND_UTILITIES/modify_script_content.py)** - 腳本內容修改工具

### **最佳實踐和指南**
- **[開發最佳實踐](06_BEST_PRACTICES/Development_Best_Practices.md)** - 腳本開發最佳實踐
- **[錯誤處理指南](06_BEST_PRACTICES/Error_Handling_Guide.md)** - 常見錯誤和解決方法
- **[優化策略](06_BEST_PRACTICES/Optimization_Strategies.md)** - 腳本優化策略

## 🔍 查找指南

### **按功能查找**
- **腳本分析** → `02_SCRIPT_ANALYSIS/`
- **腳本生成** → `03_SCRIPT_GENERATION/`
- **工具程式** → `04_TOOLS_AND_UTILITIES/`
- **範例模板** → `05_EXAMPLES_AND_TEMPLATES/`
- **最佳實踐** → `06_BEST_PRACTICES/`

### **按專案查找**
- **VALO360** → `02_SCRIPT_ANALYSIS/VALO360_Analysis/`
- **KANGAROO** → `02_SCRIPT_ANALYSIS/KANGAROO_Analysis/`
- **RAPTOR** → `02_SCRIPT_ANALYSIS/RAPTOR_Analysis/`
- **Kilimanjaro** → `02_SCRIPT_ANALYSIS/Kilimanjaro_Analysis/`

### **按類型查找**
- **參考資料** → `01_CORE_REFERENCE/`
- **分析報告** → `02_SCRIPT_ANALYSIS/`
- **生成邏輯** → `03_SCRIPT_GENERATION/`
- **工具程式** → `04_TOOLS_AND_UTILITIES/`

## 📚 重要檔案說明

### **核心參考檔案**
1. **Centimani_Script_Editing_Complete_Quick_Reference.md** - 最重要的參考資料，包含腳本編輯的完整指南
2. **AI_REFERENCE_INDEX.json** - AI索引資料，包含所有參考資料的結構化資訊
3. **Script_Structure_Reference.md** - 腳本結構的詳細參考

### **分析報告檔案**
1. **AI_SCRIPT_LOGIC_ANALYSIS_MAIN_INDEX.md** - 腳本邏輯分析的主索引
2. **各專案分析報告** - 按專案分類的詳細分析報告

### **生成邏輯檔案**
1. **AI_SCRIPT_GENERATION_LOGIC_REFERENCE.md** - 腳本生成邏輯的完整參考
2. **SCRIPT_DESIGN_PATTERNS_REFERENCE.md** - 腳本設計模式的參考

## 🛠️ 工具使用指南

### **腳本分析器**
```bash
python unified_centimani_script_analyzer.py -s "腳本路徑" -f both
```

### **腳本生成器**
```bash
python unified_centimani_script_generator.py --help
```

### **腳本修改工具**
```bash
python modify_script_content.py
```

## 📖 學習路徑

### **初學者路徑**
1. 閱讀 [快速開始指南](00_MAIN_INDEX/QUICK_START_GUIDE.md)
2. 學習 [腳本結構參考](01_CORE_REFERENCE/Script_Structure_Reference.md)
3. 查看 [範例和模板](05_EXAMPLES_AND_TEMPLATES/)

### **進階用戶路徑**
1. 深入 [腳本分析結果](02_SCRIPT_ANALYSIS/)
2. 學習 [腳本生成邏輯](03_SCRIPT_GENERATION/)
3. 參考 [最佳實踐](06_BEST_PRACTICES/)

### **開發者路徑**
1. 使用 [工具和實用程式](04_TOOLS_AND_UTILITIES/)
2. 參考 [API文檔](07_DOCUMENTATION/API_Reference/)
3. 學習 [錯誤處理](06_BEST_PRACTICES/Error_Handling_Guide.md)

## 🔄 版本更新

- **當前版本**: v2.5
- **最後更新**: 2025-08-12
- **更新內容**: 目錄結構整合、內容重組、導航優化

## 📞 支援和反饋

如有問題或建議，請參考：
- [故障排除指南](07_DOCUMENTATION/Troubleshooting/)
- [用戶指南](07_DOCUMENTATION/User_Guides/)
- [錯誤分析記錄](06_BEST_PRACTICES/Error_Handling_Guide.md)

---

*本README是AI_Complete_Reference的主要導航檔案，整合了所有重要內容和工具。* 