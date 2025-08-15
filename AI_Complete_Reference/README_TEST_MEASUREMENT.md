# 測試量測腳本使用說明

## 🎯 腳本概述

測試量測腳本是一個功能完整的測試工具，提供版本號碼管理、電壓量測、藍牙量測和報告生成功能。該腳本專為測試環境設計，能夠自動化測試流程並生成標準化的測試報告。

## 🚀 主要功能

### 1. 版本號碼管理
- **自動版本控制**: 自動生成和管理版本資訊
- **版本類型支援**: 主版本、次版本、修補版本、建置編號
- **變更歷史記錄**: 完整的版本變更歷史追蹤
- **版本描述管理**: 每個版本的詳細描述和說明

### 2. 電壓量測
- **多通道支援**: 支援多個電壓通道同時量測
- **高精度採樣**: 可配置的採樣率和精度
- **統計分析**: 自動計算平均值、最大值、最小值、標準差
- **噪聲模擬**: 模擬真實環境中的電壓噪聲

### 3. 藍牙量測
- **設備掃描**: 自動掃描周圍的藍牙設備
- **連接測試**: 測試藍牙設備的連接穩定性
- **協議支援**: 支援多種藍牙協議（HFP、A2DP、AVRCP、GATT）
- **信號強度**: 記錄RSSI信號強度指標

### 4. 報告生成
- **多格式支援**: 支援CSV和Excel格式輸出
- **詳細數據**: 包含所有測試數據和統計資訊
- **格式化樣式**: 美觀的Excel報表樣式
- **自動分類**: 按測試類型自動分類數據

## 📋 系統需求

### Python版本
- Python 3.7 或更高版本

### 依賴套件
```
pandas>=1.3.0
openpyxl>=3.0.0
```

### 安裝依賴
```bash
pip install pandas openpyxl
```

## 🔧 使用方法

### 1. 基本使用

```python
from test_measurement_script import TestMeasurementScript

# 創建測試腳本實例
script = TestMeasurementScript()

# 執行完整測試套件
test_summary = script.run_full_test_suite()

# 查看測試結果
print(f"測試完成，生成報告: {test_summary['report_files']}")
```

### 2. 電壓測試

```python
# 測試指定通道
voltage_results = script.run_voltage_tests(
    channels=[1, 2, 3],  # 測試通道
    duration=2.0          # 測試持續時間（秒）
)

# 查看測試結果
for result in voltage_results:
    if result["status"] == "success":
        stats = result["statistics"]
        print(f"通道 {result['channel']}: 平均電壓 = {stats['average_voltage']}V")
```

### 3. 藍牙測試

```python
# 執行藍牙掃描
bluetooth_results = script.run_bluetooth_tests(
    scan_duration=15.0,      # 掃描時間（秒）
    test_connections=True     # 是否測試連接
)

# 查看掃描結果
for result in bluetooth_results:
    if "devices" in result:
        print(f"發現 {len(result['devices'])} 個藍牙設備")
```

### 4. 版本管理

```python
# 查看當前版本
current_version = script.version_manager.get_version_string()
print(f"當前版本: {current_version}")

# 增加版本號碼
new_version = script.version_manager.increment_version(
    version_type="minor",           # 版本類型：major/minor/patch
    description="新增藍牙測試功能"    # 版本描述
)
print(f"新版本: {new_version}")
```

### 5. 報告生成

```python
# 生成多格式報告
report_files = script.generate_reports(
    voltage_results,      # 電壓測試結果
    bluetooth_results,    # 藍牙測試結果
    output_formats=["csv", "xlsx"]  # 輸出格式
)

# 查看生成的報告
for format_type, file_path in report_files.items():
    print(f"{format_type.upper()} 報告: {file_path}")
```

## 📊 輸出格式

### CSV格式
- 包含所有測試數據的表格格式
- 支援中文編碼（UTF-8-BOM）
- 適合數據分析和處理

### Excel格式
- 多工作表結構
- 美觀的格式樣式
- 包含版本資訊、測試數據、摘要等

#### Excel工作表結構
1. **版本資訊**: 腳本版本和變更歷史
2. **電壓量測**: 電壓測試結果和統計數據
3. **藍牙量測**: 藍牙測試結果和設備資訊
4. **測試摘要**: 測試概況和統計摘要

## ⚙️ 配置選項

### 電壓量測配置
```python
# 修改電壓量測參數
script.voltage_measurement.measurement_config.update({
    "voltage_range": (0.0, 12.0),    # 電壓範圍
    "accuracy": 0.001,               # 精度
    "sampling_rate": 2000,           # 採樣率
    "measurement_time": 2.0          # 量測時間
})
```

### 藍牙量測配置
```python
# 修改藍牙量測參數
script.bluetooth_measurement.measurement_config.update({
    "scan_duration": 20.0,           # 掃描時間
    "rssi_threshold": -70,           # RSSI閾值
    "connection_timeout": 60.0,      # 連接超時
    "supported_profiles": ["HFP", "A2DP"]  # 支援協議
})
```

### 報告配置
```python
# 修改報告輸出目錄
script.report_generator.output_dir = "custom_reports"

# 修改報告檔案名格式
script.report_generator.timestamp = "custom_format"
```

## 🔍 測試和驗證

### 1. 簡單測試
```bash
# 執行簡單功能測試
python test_simple.py
```

### 2. 完整測試
```bash
# 執行完整測試套件
python test_measurement_script.py
```

### 3. 自定義測試
```python
# 創建自定義測試
script = TestMeasurementScript()

# 測試特定功能
voltage_results = script.run_voltage_tests(channels=[1], duration=1.0)
bluetooth_results = script.run_bluetooth_tests(scan_duration=5.0)

# 生成報告
reports = script.generate_reports(voltage_results, bluetooth_results)
```

## 📝 日誌和除錯

### 日誌檔案
- **測試日誌**: `test_measurement.log`
- **日誌級別**: INFO、WARNING、ERROR
- **編碼格式**: UTF-8

### 除錯模式
```python
import logging

# 設置更詳細的日誌級別
logging.getLogger().setLevel(logging.DEBUG)

# 查看詳細執行資訊
script = TestMeasurementScript()
```

## 🚨 常見問題

### 1. 依賴套件問題
**問題**: 導入pandas或openpyxl失敗
**解決**: 安裝依賴套件
```bash
pip install pandas openpyxl
```

### 2. 權限問題
**問題**: 無法創建報告目錄或檔案
**解決**: 檢查目錄權限，確保有寫入權限

### 3. 編碼問題
**問題**: 中文顯示亂碼
**解決**: 確保使用UTF-8編碼，Excel報告會自動處理編碼

### 4. 記憶體問題
**問題**: 大量數據處理時記憶體不足
**解決**: 分批處理數據，或減少採樣數量

## 🔧 擴展和自定義

### 1. 添加新的量測類型
```python
class CustomMeasurement:
    def __init__(self):
        self.config = {}
    
    def measure(self):
        # 實現自定義量測邏輯
        pass

# 集成到主腳本
script.custom_measurement = CustomMeasurement()
```

### 2. 自定義報告格式
```python
class CustomReportGenerator:
    def generate_custom_report(self, data):
        # 實現自定義報告格式
        pass

# 替換預設報告生成器
script.report_generator = CustomReportGenerator()
```

### 3. 添加新的輸出格式
```python
def generate_json_report(self, data):
    # 實現JSON格式輸出
    import json
    with open("report.json", "w") as f:
        json.dump(data, f, indent=2)
```

## 📚 最佳實踐

### 1. 測試流程
- 先執行簡單測試驗證基本功能
- 根據實際需求調整配置參數
- 定期執行完整測試套件
- 保存重要的測試結果和報告

### 2. 版本管理
- 每次重要更新後增加版本號碼
- 記錄詳細的版本描述和變更內容
- 定期備份版本資訊檔案

### 3. 數據管理
- 定期清理舊的測試數據
- 備份重要的測試報告
- 使用有意義的檔案命名規則

### 4. 效能優化
- 根據需要調整採樣參數
- 避免不必要的數據重複計算
- 合理設置測試時間和頻率

## 🤝 支援和聯絡

### 技術支援
- 檢查日誌檔案獲取詳細錯誤資訊
- 參考程式碼註解了解實現細節
- 使用簡單測試腳本驗證功能

### 問題回報
- 記錄錯誤發生的具體情況
- 提供相關的配置和環境資訊
- 附上錯誤日誌和堆疊追蹤

### 功能建議
- 描述期望的功能和改進
- 提供具體的使用場景
- 說明對工作流程的影響

---

**注意**: 本腳本專為測試環境設計，請根據實際需求進行調整和擴展。
**版本**: 1.0.0
**更新日期**: 2024-12-19
**作者**: AI Assistant 