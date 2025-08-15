# KANGAROO 腳本分析報告

**分析日期**: 2025-08-11T11:02:24.316386
**分析檔案數量**: 10

## 測試項目總結

- **總項目數**: 5346
- **工作表數量**: 2

### 各工作表項目數量
- Test Item All: 5247 項
- Version History: 99 項

## 測試流程總結

- **總檔案數**: 9
- **總工作表數**: 56
- **測試流程工作表數**: 15

### 檔案詳細資訊

#### Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx
- 工作表數量: 5
- 測試流程工作表: DUTs
- 總行數: 198

#### Kangaroo_MP_AIR_TestFlow_20250326C.xlsx
- 工作表數量: 5
- 測試流程工作表: DUTs
- 總行數: 125

#### Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx
- 工作表數量: 5
- 測試流程工作表: DUTs
- 總行數: 1115

#### Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx
- 工作表數量: 5
- 測試流程工作表: DUTs
- 總行數: 202

#### Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX
- 工作表數量: 6
- 測試流程工作表: DUTs
- 總行數: 1134

#### Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX
- 工作表數量: 6
- 測試流程工作表: DUTs
- 總行數: 1345

#### Pega_Kangaroo_TestFlow-Final Check_MP_20250415_CBNGSIMSLOT1.xlsx
- 工作表數量: 6
- 測試流程工作表: DUTs
- 總行數: 2463

#### Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx
- 工作表數量: 6
- 測試流程工作表: DUTs
- 總行數: 2386

#### Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx
- 工作表數量: 12
- 測試流程工作表: DUTs, ANT0_TX, ANT3_TX, ANT0_RX, ANT1_RX, ANT2_RX, ANT3_RX
- 總行數: 5566

## 腳本結構總結

- **唯一結構數量**: 3

### 常見結構模式

#### 結構 9 次出現
**標題欄位**:
- Name
- Value

**出現位置**:
- Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx/Properties
- Kangaroo_MP_AIR_TestFlow_20250326C.xlsx/Properties
- Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx/Properties
- Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx/Properties
- Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX/Properties
- ... 還有 4 個

#### 結構 9 次出現
**標題欄位**:
- Load
- DUT Name
- Station
- Parameter
- SFIS_DeviceID
- ScanBarcode( {Name,Lengh,Pattern} )
- Connection1 (Type,Name,ConnectString)
- Connection2 (Type,Name,ConnectString)
- Connection3 (Type,Name,ConnectString)
- Connection4(Type,Name,ConnectString)
- Connection5(Type,Name,ConnectString)
- Connection6(Type,Name,ConnectString)
- Connection7(Type,Name,ConnectString)
- Connection8(Type,Name,ConnectString)
- Connection9(Type,Name,ConnectString)
- Connection10(Type,Name,ConnectString)

**出現位置**:
- Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx/DUTs
- Kangaroo_MP_AIR_TestFlow_20250326C.xlsx/DUTs
- Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx/DUTs
- Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx/DUTs
- Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX/DUTs
- ... 還有 4 個

#### 結構 6 次出現
**標題欄位**:
- 02
- :Utility.StrSpilt,"*(MSG)","\,","-1"
- 0
- Index;$TestItem;Unit;$MeasureValue;$LowerLimit;$UpperLimit;TestResult
- 0
- PC#-#Spilt_TestItem@#$
- KAWI011

**出現位置**:
- Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx/ANT0_TX
- Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx/ANT3_TX
- Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx/ANT0_RX
- Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx/ANT1_RX
- Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx/ANT2_RX
- ... 還有 1 個
