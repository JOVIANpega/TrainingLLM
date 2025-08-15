# 功能測試代碼詳細分類索引

## 🎯 分類索引概述

本文件提供按功能分類的詳細測試代碼索引，涵蓋所有測試類別和子類別，支援深度查詢和分析。

## 📊 主要測試類別分類

### 1. **射頻測試類 (RF Testing)**

#### 1.1 空間頻率回應測試 (SFR - Spatial Frequency Response)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IPIO00K | SFR_H2 | ARFA05 | Rev. 1.18 | 空間頻率回應H2不良 |
| IPIO00L | SFR_V2 | ARFA06 | Rev. 1.18 | 空間頻率回應V2不良 |
| IPIO00M | SFR_H3 | ARFA07 | Rev. 1.18 | 空間頻率回應H3不良 |
| IPIO00N | SFR_V3 | ARFA08 | Rev. 1.18 | 空間頻率回應V3不良 |

#### 1.2 RF功率測試 (RF Power Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IORF121 | RF Downstream Power | ARFA10 | Rev. 1.3 | RF downstream功率測試不良 |
| IORF124 | RF Upstream Power | ARFA09 | Rev. 1.3 | RF upstream功率測試不良 |
| IORF122 | RF Remote | ARFA49 | Rev. 1.3 | RF遙控器不良 |
| IORF123 | RF Remote Test | ARFA56 | Rev. 1.3 | RF遙控器測試錯誤 |

#### 1.3 頻率測試 (Frequency Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOUS128 | US ACI Test | ARFA19 | Rev. 1.3 | US ACI測試失敗 |
| IOUS129 | US Frequency Test | ARFA22 | Rev. 1.3 | US frequency測試失敗 |
| IOUS130 | US Harmonic Test | ARFA21 | Rev. 1.3 | US harmonic測試失敗 |
| IOUS131 | US LOCK Frequency | ARFA03 | Rev. 1.3 | US LOCK Frequency測試不良 |

### 2. **顯示器測試類 (Display Testing)**

#### 2.1 LCD品質測試 (LCD Quality Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| NBLD004 | LCD異常線條 | N0FL02 | Rev. 1.17 | LCD有異常線條 |
| NBLD005 | LCD異常亮點 | N0FL03 | Rev. 1.17 | LCD亮點過大或過多 |
| NBLD006 | LCD顯示異常 | N0FL04 | Rev. 1.17 | LCD顯示功能異常 |
| NBLD007 | LCD色彩測試 | N0FL05 | Rev. 1.17 | LCD色彩準確性異常 |

#### 2.2 LED測試 (LED Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOET159 | Power Button LED | N0FL83 | Rev. 1.5 | Power button LED不良 |
| IOET173 | LED Green Check | N0FL20 | Rev. 1.11 | 檢測LED燈亮綠色錯誤 |
| IOET174 | LED Red Check | N0FL21 | Rev. 1.11 | 檢測LED燈亮紅色錯誤 |

#### 2.3 VFD顯示測試 (VFD Display Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOET163 | VFD Display | N0FY22 | Rev. 1.7 | VFD display不良 |
| IOET164 | VFD On/Off | N0FY07 | Rev. 1.7 | VFD on/off不良 |

### 3. **通訊測試類 (Communication Testing)**

#### 3.1 網路通訊測試 (Network Communication)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOPI113 | Ping Test Fail | BSFM11 | Rev. 1.3 | Ping測試失敗 |
| IOPI114 | Network Connect | BSFM12 | Rev. 1.3 | 網路連線失敗 |
| IOET177 | Ethernet Loopback | BPJ693 | Rev. 1.23 | Ethernet Loopback不良 |

#### 3.2 USB通訊測試 (USB Communication)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOET153 | Read USB Test | BSFI02 | Rev. 1.5 | Read USB測試不良 |
| IOET154 | Front USB Test | BSFI02 | Rev. 1.5 | Front USB測試不良 |
| IOET155 | USB High Power | BSFI02 | Rev. 1.5 | USB High Power測試不良 |
| IOET162 | USB 3.0 Detect | BSFI31 | Rev. 1.7 | USB 3.0偵測失敗 |

#### 3.3 序列埠通訊測試 (Serial Communication)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOET179 | UART Interface | E00IO000001 | Rev. 1.31 | Meter UART介面不良 |
| IOET17A | GPIO1 | E00IO000002 | Rev. 1.31 | GPIO1不良 |
| IOET17B | GPIO2 | E00IO000003 | Rev. 1.31 | GPIO2不良 |

### 4. **功能測試類 (Functional Testing)**

#### 4.1 基本設定測試 (Basic Configuration)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| B7PL025 | Set Model Name | BSFM25 | Rev. 1.0 | 設定型號名稱 |
| B7PL026 | Get Device Info | BSFM26 | Rev. 1.0 | 獲取設備資訊 |
| B7PL027 | Set Device Config | BSFM27 | Rev. 1.0 | 設定設備配置 |

#### 4.2 SFIS功能測試 (SFIS Functional Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| OTFX064 | SFIS Get 60ISN | BSFM64 | Rev. 1.0 | 獲取60ISN資訊 |
| OTFX079 | Get Change 60ISN | BSFM79 | Rev. 1.0 | 獲取變更的60ISN |
| OTFX080 | Device Status | BSFM80 | Rev. 1.0 | 設備狀態檢查 |

#### 4.3 按鍵功能測試 (Button Functional Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IORB116 | Reset Button | BSFI07 | Rev. 1.3 | Reset Button不良 |
| IOFP117 | Front Panel Button | BSFO58 | Rev. 1.3 | BIST模式下前視面板按鍵測試不良 |
| IOFP118 | Reset Button Test | BSFO51 | Rev. 1.3 | BIST模式下Reset按鍵測試不良 |
| IOBU119 | Buttons Test | BSFO40 | Rev. 1.3 | 按鍵不良 |

### 5. **感測器測試類 (Sensor Testing)**

#### 5.1 IMU感測器測試 (IMU Sensor Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOGS145 | G-Sensor Test | BSFT45 | Rev. 1.3 | 重力感測器測試不良 |
| IOGS146 | IMU Test | BSFT46 | Rev. 1.3 | IMU測試不良 |
| IOGS147 | GPS Test | BSFT47 | Rev. 1.3 | GPS測試不良 |

#### 5.2 GPS定位測試 (GPS Positioning Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOGP142 | GPS Fix Location | BSFT22 | Rev. 1.3 | GPS無法定位 |
| IOGP143 | GPS CN Value | BSFT21 | Rev. 1.3 | GPS CN值超出範圍 |
| IOGP144 | GPS ColdStart | BSFT20 | Rev. 1.3 | GPS ColdStart測試不良 |

### 6. **環境測試類 (Environmental Testing)**

#### 6.1 溫度測試 (Temperature Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOTP127 | Temperature Test | BSFM38 | Rev. 1.3 | 溫度測試失敗 |
| IOTP128 | Humidity Test | BSFM39 | Rev. 1.3 | 濕度測試失敗 |

#### 6.2 風扇測試 (Fan Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOFN135 | Power Off Fan Speed | BSFO28 | Rev. 1.3 | 測試風扇斷電后轉速錯誤 |
| IOFN136 | Fan Test | BSFV32 | Rev. 1.3 | 風扇測試不良 |
| IOFN137 | 100% Fan Speed | BSFO29 | Rev. 1.3 | 測試風扇100%轉速錯誤 |

### 7. **電氣測試類 (Electrical Testing)**

#### 7.1 電壓測試 (Voltage Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOVL001 | Voltage Test | BSFV01 | Rev. 1.3 | 電壓測試失敗 |
| IOVL002 | Current Test | BSFI02 | Rev. 1.3 | 電流測試失敗 |
| IOVL003 | Power Test | BSFI03 | Rev. 1.3 | 功率測試失敗 |

#### 7.2 阻抗測試 (Impedance Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOIM001 | Impedance Test | BSFI01 | Rev. 1.3 | 阻抗測試失敗 |
| IOIM002 | Resistance Test | BSFI02 | Rev. 1.3 | 電阻測試失敗 |

### 8. **音頻測試類 (Audio Testing)**

#### 8.1 音頻輸出測試 (Audio Output Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOSP126 | Speaker Test | BSFI42 | Rev. 1.3 | Speaker測試不良 |
| IOSP127 | Audio Quality | BSFI43 | Rev. 1.3 | 音頻品質測試 |

#### 8.2 音頻輸入測試 (Audio Input Testing)
| 代碼 | 測試項目 | 測試類別 | 版本 | 描述 |
|------|----------|----------|------|------|
| IOMI125 | Microphone Test | BSFI39 | Rev. 1.3 | 麥克風測試失敗 |
| IOMI126 | Audio Input | BSFI40 | Rev. 1.3 | 音頻輸入測試 |

## 🔍 進階搜尋索引

### 按版本分類搜尋
- **Rev. 1.18** → 最新射頻測試項目
- **Rev. 1.17** → 顯示器測試項目
- **Rev. 1.3** → 基礎功能測試項目
- **Rev. 1.0** → 核心功能測試項目

### 按測試類別代碼搜尋
- **ARFA** → 射頻測試類別
- **N0FL** → 顯示器測試類別
- **BSFM** → 功能測試類別
- **BSFI** → 輸入輸出測試類別
- **BSFO** → 輸出測試類別

### 按錯誤嚴重程度搜尋
- **嚴重錯誤** → 影響基本功能的錯誤（如 B7PL 系列）
- **一般錯誤** → 影響特定功能的錯誤（如 IPIO 系列）
- **警告錯誤** → 不影響功能但需注意的錯誤（如 IOET 系列）

## 📊 統計分析

### 測試類別分佈
- **射頻測試**：約 800 個代碼
- **顯示器測試**：約 600 個代碼
- **通訊測試**：約 700 個代碼
- **功能測試**：約 1000 個代碼
- **感測器測試**：約 400 個代碼
- **環境測試**：約 300 個代碼
- **電氣測試**：約 500 個代碼
- **音頻測試**：約 300 個代碼

### 版本分佈統計
- **Rev. 1.18**：最新功能，約 200 個代碼
- **Rev. 1.17**：近期更新，約 300 個代碼
- **Rev. 1.3**：穩定版本，約 2000 個代碼
- **Rev. 1.0**：基礎版本，約 2500 個代碼

## 🚀 使用指南

### 1. 按功能查詢
```
需要射頻測試 → 查看「射頻測試類」→ 找到 IPIO 系列
需要顯示器測試 → 查看「顯示器測試類」→ 找到 NBLD 系列
需要通訊測試 → 查看「通訊測試類」→ 找到 IOPI 系列
```

### 2. 按代碼查詢
```
知道代碼開頭 → 按代碼開頭搜尋 → 找到對應類別
知道完整代碼 → 直接搜尋 → 找到詳細資訊
```

### 3. 按版本查詢
```
需要最新功能 → 查看 Rev. 1.18 → 找到最新測試項目
需要穩定功能 → 查看 Rev. 1.3 → 找到成熟測試項目
```

## 📝 更新記錄

- **v1.0** (2025-01-XX)：建立功能測試代碼詳細分類索引
- **覆蓋範圍**：8個主要測試類別，5000+ 個測試代碼
- **更新狀態**：持續完善中

---

_本文件為功能測試代碼的詳細分類索引，支援深度查詢和分析所有測試類別_ 