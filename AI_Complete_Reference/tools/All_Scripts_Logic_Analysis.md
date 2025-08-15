# 全部腳本邏輯分析摘要

## 1. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Kangaroo_DWeSIMandFWUP_MultiDUT_TestFlow-20250414.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, eSIM_DW_FW_UP_OFFLINE
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GPRF, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "DLL:ESIM_DB_ACCESS.DLL":3
- 步驟數: 116 | CLI: 0 | Dev: 116 | Validation: 15
- Phase 分佈: 0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 97:1, 99:1
- ExecMode: 1:34, 6:3, 0:38, 2,1:1, 2:1:3, 2:0:5, 3:3, 8:1, 4:4,1:1, 4:4,3:1, 4:9,6:1, 7:3,3000:1, 4:12,15:1, 2,0:5, 2,2:2, 2,4:1, 2,6:2, 2,9:2, 4:19,13:1, 2:17:1, 2:2:2, 2:4:1, 5:2, 4:7,1:1, 9:3
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 2. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Kangaroo_MP_AIR_TestFlow_20250326C.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, AIR Leakage
- 儀器函數: AC, AMPL, BT, CLR, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "UART":1
- 步驟數: 49 | CLI: 6 | Dev: 43 | Validation: 4
- Phase 分佈: 0:1, 1:1, 2:1, 3:1, 97:1
- ExecMode: 0:17, 8:1, 1:15, 3:3, 4:1,21:1, 9:1, 4:3,6:1, 4:21,21:4, 4:7,10:1, 4:11,14:1, 4:15,18:1, 2:1:1, 2:3:1, 6:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求

## 3. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Kangaroo_PR_CellularVerification-20240923_PC3_TestFlow.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, Cellular Verification, 5G_PathLoss, ANT0_TX, ANT3_TX, ANT0_RX, ANT1_RX, ANT2_RX, ANT3_RX
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GPRF, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":1, "UART":1
- 步驟數: 613 | CLI: 2 | Dev: 605 | Validation: 118
- Phase 分佈: 0:2, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:1, 10:1, 11:1, 97:1, 99:1
- ExecMode: 1:62, 6:11, 0:449, 2:9:3, 3:3, 8:5, 4:1,8:1, 4:2,5:1, 4:8,8:3, 4:2,1:1, 4:3,7:1, 4:21,21:3, 4:8,12:1, 4:13,17:1, 4:2,3:2, 4:6,8:2, 4:9,9:2, 4:12,14:1, 4:15,15:1, 2:1:6, 4:16,20:1, 4:24,24:1, 4:4,7:2, 7:1,3000:2, 4:13,16:2, 7:10,3000:2, 4:17,17:2, 4:22,25:2, 7:19,3000:2, 4:26,26:2, 4:31,34:2, 7:28,3000:2, 4:35,35:2, 4:40,43:2, 7:37,3000:2, 4:44,44:2, 4:49,52:2, 7:46,3000:2, 4:53,53:2, 4:58,61:2, 7:55,3000:2, 4:62,62:2, 4:67,70:2, 7:64,3000:2, 4:71,71:2, 4:76,79:2, 7:73,3000:2, 4:80,80:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 4. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow-Final Check_MP_20250415_CBNGSIMSLOT1.xlsx
- 工作表: Properties, Instrument, Switch, DUTs, Final Check, Final Check_TPE
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, txPWR, ypbCB
- DUT 連線: "UART":12, "APP":4
- 步驟數: 814 | CLI: 4 | Dev: 810 | Validation: 108
- Phase 分佈: 0:2, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 19:2, 20:2, 21:2, 22:2, 23:2, 24:2, 97:4, -1:2
- ExecMode: 4:4,1:2, 1:240, 6:65, 3:63, 0:65, 8:42, 4:1,3:5, 4:1,4:7, 4:1,20:3, 4:2,5:4, 4:20,20:16, 4:6,9:4, 4:10,13:4, 4:14,17:4, 2,0:2, 2:0:9, 4:11,4:2, 4:7,8:2, 2:5:9, 4:10,11:2, 4:12,14:2, 9:52, 4:16,16:2, 4:16,15:2, 4:2,1:4, 4:5,3:2, 4:3,3:4, 2:1:28, 4:3,1:2, 4:14,1:2, 4:25,25:2, 4:3,8:2, 4:31,31:8, 4:9,14:2, 4:15,20:2, 4:21,26:2, 2:13:7, 2:25:2, 2:31:7, 2:47:6, 4:2,2:2, 2:4:7, 4:6,1:8, 4:4,4:8, 2:2:20, 4:1,11:4, 2:3:10, 2:7:8, 2:9:4, 4:10,10:4, 2:6:4, 2:8:12, 4:1,13:2, 4:6,8:2, 4:11,12:2, 4:1,15:2, 2:11:2, 4:2,4:10, 4:1,2:2, 4:1,21:1, 4:2,21:2, 2:14:2, 2:18:2, 4:10,2:2, 4:10,7:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 5. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow-OQC_MP_20250415_CBNGSIMSLOT1.xlsx
- 工作表: Properties, Instrument, Switch, DUTs, OQC, OQC_TPE
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, txPWR, ypbCB
- DUT 連線: "UART":4, "APP":2, "DLL:FANPROJECT.DLL":2
- 步驟數: 742 | CLI: 6 | Dev: 736 | Validation: 80
- Phase 分佈: 0:2, 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 19:2, 20:2, 21:2, 22:2, 23:2, 24:2, 25:2, 99:2, 97:2
- ExecMode: 4:4,1:2, 1:274, 6:42, 3:50, 0:64, 8:38, 4:13,15:2, 4:16,18:4, 4:1,20:2, 4:2,5:10, 4:20,20:8, 4:6,9:2, 4:10,13:2, 4:14,17:2, 4:6,3:2, 2:4:16, 4:3,1:2, 4:14,1:2, 4:25,25:2, 9:24, 4:2,1:2, 4:3,8:2, 4:31,31:8, 4:9,14:2, 4:15,20:2, 4:21,26:2, 4:1,4:4, 4:1,2:2, 4:1,15:2, 4:10,10:2, 2:5:10, 2:2:10, 4:1,14:4, 2:3:10, 2:6:8, 2:8:8, 2:9:10, 2:12:6, 4:1,22:4, 4:8,8:6, 2:10:2, 2:13:4, 2:17:2, 2:18:6, 4:21,22:2, 2:0:14, 2:1:8, 4:7,9:6, 4:12,13:4, 4:12,1:2, 4:1,11:2, 2:16:2, 2:20:2, 2:24:2, 4:1,3:2, 4:14,14:8, 4:4,6:2, 4:10,12:2, 4:3,3:4, 4:4,4:8, 4:2,4:4
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 6. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow-WIFI&BT_CAL&VERIF_MP_20250421.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, WIFI&BT CAL&VERIF, PathLoss
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, GPRF, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MEAN, MSCurr, MSVolt, NFT, OUTONOFF, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RMS, RRout, SETDVBC, SMASK, SetCurr, SetON, SetVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, txPWR, ypbCB
- DUT 連線: "UART":4, "APP":4
- 步驟數: 259 | CLI: 10 | Dev: 249 | Validation: 58
- Phase 分佈: 0:2, 1:2, 2:1, 3:1, 4:1, 5:1, 6:1, -1:3, 97:1
- ExecMode: 1:79, 0:99, 2:5:1, 2:7:3, 3:7, 8:19, 2:2:5, 4:1,12:1, 4:2,5:1, 4:12,12:2, 4:6,9:1, 4:11,1:1, 4:21,21:4, 9:10, 4:2,1:1, 4:3,7:1, 4:8,12:1, 4:13,17:1, 2:0:3, 4:31,5:1, 4:28,30:1, 4:30,29:1, 4:60,60:1, 4:32,60:1, 2:54:1, 2:53:1, 4:28,5:1, 4:55,55:1, 4:29,55:1, 6:7, 2:4:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 7. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow-WIFIOTA_MP_20250419_ForFWUpgrade.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, WIFI&5GOTA, PathLoss
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, GPRF, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MEAN, MSCurr, MSVolt, NFT, OUTONOFF, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RF_Switch, RMS, RRout, SETDVBC, SMASK, SetCurr, SetON, SetVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, gInfo, gName, getActive, getSwitch, initDev, setSwitch, svCB, txPWR, ypbCB
- DUT 連線: "UART":6, "APP":6
- 步驟數: 620 | CLI: 2 | Dev: 618 | Validation: 59
- Phase 分佈: 0:2, 1:2, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1, 24:1, 25:1, 26:1, 27:1, 28:1, 29:1, 30:1, 31:1, 32:1, 33:1, 34:1, 35:1, 36:1, 37:1, 38:1, 39:1, 40:1, 41:1, 42:1, 43:1, 44:1, 45:1, 46:1, 47:1, 48:1, 97:2, 99:1
- ExecMode: 4:4,1:2, 1:263, 6:53, 3:39, 0:47, 8:16, 2,0:1, 2:0:11, 4:7,4:1, 2:5:1, 4:10,8:1, 4:6,1:1, 2:1:3, 4:4,5:1, 2:3:7, 4:3,1:1, 4:1,20:1, 4:2,5:9, 4:20,20:4, 4:6,9:1, 4:10,13:1, 4:14,17:1, 4:14,1:1, 4:26,26:1, 9:16, 4:5,1:1, 4:4,2:1, 4:2,1:2, 4:3,8:1, 4:31,31:4, 4:9,14:1, 4:15,20:1, 4:21,26:1, 4:3,4:1, 4:2,3:1, 2:4:61, 2:2:1, 2:18:1, 4:21,23:1, 4:34,34:4, 4:24,26:1, 4:27,29:1, 4:30,32:1, 4:1,4:1, 4:3,13:12, 4:5,5:12, 4:2,12:12, 4:6,6:12, 4:1,3:2, 4:3,2:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 8. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow_Mainboard_MP_250407.xlsx
- 工作表: Properties, Instrument, Switch, DUTs, MB FUNCTION
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, FC_Fixture, FREQ, FSCAN, Freq, GPRF, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MEAN, MSCurr, MSVolt, NFT, OUTONOFF, PK2PK, POWERSWITCH, PREDEV, QRCODE, RESDEV, RFPWR, RMS, RRout, SETDVBC, SMASK, SetCurr, SetON, SetVolt, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, txPWR, ypbCB
- DUT 連線: "UART":4, "SSH":2
- 步驟數: 250 | CLI: 86 | Dev: 159 | Validation: 20
- Phase 分佈: 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, -1:2, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 97:1
- ExecMode: 0:39, 8:5, 1:67, 4:1,11:1, 4:3,5:1, 4:10,10:1, 9:14, 4:1,12:1, 4:2,5:2, 4:12,12:2, 4:6,9:1, 3:8, 2:1:16, 4:5,5:1, 2:4:7, 4:3,2:1, 2:2:8, 6:17, 4:23,23:2, 4:18,21:1, 2:17:1, 2:15:4, 4:5,4:1, 4:6,10:1, 2:0:13, 4:24,24:3, 4:11,15:1, 4:16,20:1, 4:1,5:1, 4:1,9:1, 4:11,11:2, 2:9:2, 4:3,1:1, 4:7,1:1, 4:17,17:1, 2:7:3, 2:11:1, 2:13:1, 4:2,2:2, 4:3,3:3, 2:3:1, 4:15,7:1, 2:10:1, 4:13,14:1, 4:25,25:1, 2:18:1, 4:21,22:1, 2:5:1, 4:1,3:1, 4:1,4:1, 4:6,2:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 9. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Pega_Kangaroo_TestFlow_MP_FWdownload_20250410-RecordUSBInfo.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, FWDL
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- 步驟數: 105 | CLI: 0 | Dev: 105 | Validation: 0
- Phase 分佈: 0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 97:2, 99:1
- ExecMode: 1:15, 8:1, 4:1,4:1, 9:2, 4:3,4:1, 0:34, 2,0:2, 4:1,13:1, 4:3,6:1, 4:13,13:2, 4:7,10:1, 3:4, 4:5,1:3, 4:5,5:1, 2,2:5, 4:6,8:1, 4:16,16:3, 4:9,11:1, 4:12,14:1, 2:0:1, 6:10, 2:2:4, 4:7,3:2, 2:3:5, 4:6,2:1, 4:1,5:1, 2:1:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求

## 10. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\KANGAROO\Test Item Code V2.04_20250310.xlsx
- 工作表: 七碼定義Definition, Test Item All, Version History, 工作表1
- 儀器函數: -
- 步驟數: 0 | CLI: 0 | Dev: 0 | Validation: 0
- Phase 分佈: -
- ExecMode: -
- 為什麼這樣寫: 依欄位使用狀態，腳本兼具功能檢查與儀器量測，符合綜合測試流程

## 11. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\Kilimanjaro\Kilimanjaro_LED_20201116_TestFlow.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, LED_golden_Test, LED_golden_Up, LED_golden_Fix, LED_24, LED_M
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "UART":13, "DLL:LV_LIBRARY.DLL":4
- 步驟數: 563 | CLI: 339 | Dev: 224 | Validation: 72
- Phase 分佈: 0:5, 1:5, 2:5, 3:5, 4:5, 97:5
- ExecMode: 6:151, 1:285, 0:42, 8:5, 3:22, 2:7:1, 2:15:4, 2:23:1, 2:30:1, 2:38:1, 2:46:1, 2:53:1, 2:61:1, 2:69:1, 2:76:1, 2:84:1, 2:92:1, 2:99:1, 2:107:1, 2:115:1, 2:3:4, 2:4:4, 2:5:3, 2:10:3, 2:22:3, 2:28:3, 2:35:3, 2:40:3, 2:45:3, 2:52:3, 2:59:3, 4:1,1:1, 4:2,3:1, 4:7,3:1, 4:7,4:1, 4:7,7:1
- 為什麼這樣寫: 以 CLI 功能檢查為主：Send 多為 Connection@Command，偏向功能/診斷；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 12. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\RAPTOR\Raptor_ALL_TestFlow_20230223_ALL.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, Download, Board Test, Wifi Test
- 儀器函數: CLR, MCurr, MVolt, OnOff, SCurr, SON, SVolt, TCP_Transfer, switch
- DUT 連線: "APP":9, "DLL:FANPROJECT.DLL":3, "TCP":4, "DLL:FUNCTION0311.DLL":2, "UART":2, "DLL:LITEPOINT_DLL.DLL":1, "UDP":1
- 步驟數: 572 | CLI: 113 | Dev: 459 | Validation: 286
- Phase 分佈: 1:3, 2:3, 3:3, 4:3, 5:3, 97:3, -1:1, -2:1, 0:2, 6:2, 7:2, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1
- ExecMode: 0:332, 1:118, 9:70, 8:10, 3:7, 4:1,2:1, 4:4,2:1, 2:0:18, 4:6,1:1, 4:10,10:1, 4:1,7:1, 4:8,6:1, 4:9,9:1, 4:6,2:2, 4:1,8:1, 4:6,3:1, 4:1,12:1, 2:1:1, 2:4:1, 4:2,3:1, 4:160,1:1, 4:1,88:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 13. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\RAPTOR\Raptor_ALL_TestFlow_Fixcture_20230309_ALL.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, Download, Board Test, Wifi Test
- 儀器函數: CLR, Freq, LED_Test, MCurr, MVolt, OnOff, RMS, SCurr, SON, SVolt, TCP_Transfer, Voltage, switch
- DUT 連線: "APP":9, "DLL:FANPROJECT.DLL":3, "TCP":4, "DLL:FUNCTION0311.DLL":2, "UART":2, "DLL:LITEPOINT_DLL.DLL":1, "UDP":1
- 步驟數: 618 | CLI: 113 | Dev: 505 | Validation: 310
- Phase 分佈: 1:3, 2:3, 3:3, 4:3, 5:3, 97:3, -1:1, -2:1, 0:2, 6:2, 7:2, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1
- ExecMode: 0:337, 1:148, 9:70, 8:10, 3:8, 2:0:26, 4:1,2:1, 4:4,2:1, 4:6,1:1, 4:10,10:1, 4:1,7:1, 4:8,6:1, 4:9,9:1, 4:13,12:1, 4:15,16:1, 4:6,2:2, 4:1,8:1, 4:6,3:1, 4:1,12:1, 2:1:1, 2:4:1, 4:2,3:1, 4:160,1:1, 4:1,88:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 14. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\Pega_Nokia_TestFlow_20250307_ER2_DMIC.xlsx
- 工作表: Properties, Switch, Instrument, DUTs, DMIC, TEMP
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":2, "UART":4
- 步驟數: 70 | CLI: 29 | Dev: 41 | Validation: 0
- Phase 分佈: 0:1, 1:2, 2:2, 3:2, 4:2, 5:2, 6:1, 7:1, 97:1
- ExecMode: 0:28, 8:2, 1:26, 4:3,1:1, 2:0:11, 3:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；以 CLI 功能檢查為主：Send 多為 Connection@Command，偏向功能/診斷

## 15. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_ER2 OQC Function Check List_202504122_for Factory.xlsx
- 工作表: OQC, VLC, WebUI, PrivateKey, WiFi, 5G (Cellular)
- 儀器函數: -
- 步驟數: 0 | CLI: 0 | Dev: 0 | Validation: 0
- Phase 分佈: -
- ExecMode: -
- 為什麼這樣寫: 依欄位使用狀態，腳本兼具功能檢查與儀器量測，符合綜合測試流程

## 16. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_ER2 OQC Function Check List_20250418.xlsx
- 工作表: OQC, VLC, WebUI, PrivateKey, WiFi, 5G (Cellular)
- 儀器函數: -
- 步驟數: 0 | CLI: 0 | Dev: 0 | Validation: 0
- Phase 分佈: -
- ExecMode: -
- 為什麼這樣寫: 依欄位使用狀態，腳本兼具功能檢查與儀器量測，符合綜合測試流程

## 17. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250218_ER2.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, IO Board
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":1, "UART":2, "SSH":1
- 步驟數: 23 | CLI: 11 | Dev: 12 | Validation: 0
- Phase 分佈: 0:1, 1:1, -1:1, 2:1, 3:1, 97:1
- ExecMode: 1:16, 8:1, 2:0:3, 0:2, 3:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；以 CLI 功能檢查為主：Send 多為 Connection@Command，偏向功能/診斷

## 18. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250218_POE_LoopOK.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, Power
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":1, "UART":2, "SSH":1
- 步驟數: 46 | CLI: 14 | Dev: 32 | Validation: 5
- Phase 分佈: 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 97:1
- ExecMode: 0:18, 8:1, 1:13, 2:0:12, 3:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求

## 19. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250307_POE.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, Power
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":1, "UART":2, "SSH":1
- 步驟數: 73 | CLI: 16 | Dev: 57 | Validation: 7
- Phase 分佈: 0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 97:1
- ExecMode: 0:21, 8:2, 1:25, 2:0:13, 9:1, 4:1,3:3, 6:1, 4:1,7:1, 4:1,4:1, 4:1,6:1, 4:6,4:1, 4:6,5:1, 3:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求

## 20. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250318_MB_ER2.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, MB, TEMP
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":2, "UART":4, "SSH":2
- 步驟數: 172 | CLI: 64 | Dev: 108 | Validation: 8
- Phase 分佈: 0:1, 1:2, 2:2, 3:2, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1, -1:1, 21:1, 97:2
- ExecMode: 1:82, 8:4, 0:47, 2:0:16, 9:2, 4:1,6:4, 6:2, 3:7, 4:1,5:1, 4:3,5:1, 4:1,4:2, 2:1:3, 4:4,2:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 21. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250326_Final.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, Final, TEMP
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":2, "UART":4, "SSH":2
- 步驟數: 75 | CLI: 25 | Dev: 50 | Validation: 3
- Phase 分佈: 0:1, 1:2, 2:2, 3:2, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 97:1
- ExecMode: 1:25, 0:18, 9:11, 6:2, 2:0:3, 8:11, 4:1,3:3, 4:3,1:1, 3:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 22. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250326_IMU.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, IMU, TEMP
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":2, "UART":4, "SSH":2
- 步驟數: 52 | CLI: 13 | Dev: 39 | Validation: 0
- Phase 分佈: 0:2, 1:2, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1
- ExecMode: 1:30, 2:0:6, 8:5, 4:1,3:3, 6:2, 0:6
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求

## 23. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\VALO360_TestFlow_20250407_Function.xlsx
- 工作表: Properties, DUTs, Switch, Instrument, Funtion, TEMP
- 儀器函數: AC, AMPL, BT, CLR, CW, DC, DEFDEV, ElectronicLoad, FC_Fixture, FREQ, FSCAN, Freq, GetVoltageCurrent, HXTaudio1, IOswitch, LED_Test, LVdut_Device, MCurr, MEAN, MVolt, NFT, OnOff, PK2PK, POWERSWITCH, PREDEV, PowerSource, QRCODE, RESDEV, RFPWR, RMS, RRout, SCurr, SETDVBC, SMASK, SON, SVolt, SetVoltageCurrent, TCP_Transfer, VOIP, VOLAGE, Voltage, WIFI, WIFI 2.4G, WIFI 5G, cvbsCB, svCB, ypbCB
- DUT 連線: "APP":2, "UART":4, "SSH":2
- 步驟數: 202 | CLI: 99 | Dev: 103 | Validation: 22
- Phase 分佈: 0:2, 1:2, 2:2, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 14:1, 15:1, 16:1, 17:1, 18:1, 19:1, 20:1, 21:1, 22:1, 23:1, -1:1, 24:1, 97:1
- ExecMode: 1:92, 9:12, 3:8, 2:0:6, 0:37, 8:20, 6:5, 4:1,3:5, 4:1,10:1, 4:1,6:1, 4:3,1:1, 4:1,5:3, 4:5,3:1, 4:5,4:1, 4:1,4:2, 4:3,4:1, 2:1:3, 4:1,11:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；以 CLI 功能檢查為主：Send 多為 Connection@Command，偏向功能/診斷；使用 Validation 進行上下限/型別檢核，對齊規格要求；使用 Prompt/EndPrompt 控制互動時序，加速長回覆命令

## 24. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\VALO360\~$VALO360_TestFlow_20250326_IMU.xlsx
- 工作表: 
- 儀器函數: -
- 步驟數: 0 | CLI: 0 | Dev: 0 | Validation: 0
- Phase 分佈: -
- ExecMode: -
- 為什麼這樣寫: 

## 25. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\ZEBRA\wifi_TestFlow.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, WifiCalibration
- 儀器函數: CLR, MCurr, MVolt, OnOff, SCurr, SON, SVolt, TCP_Transfer, switch
- DUT 連線: "APP":4, "DLL:FANPROJECT.DLL":1
- 步驟數: 106 | CLI: 13 | Dev: 93 | Validation: 17
- Phase 分佈: 0:1, 1:1, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1, 9:1, 10:1, 11:1, 12:1, 13:1, 97:1
- ExecMode: 0:71, 1:13, 2:1:1, 9:3, 8:1, 6:1, 2:0:5, 2:2:8, 4:25:22:1, 2:3:2
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求

## 26. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\ZEBRA\Zebra_20190417_TestFlow.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, L10A_FA5, ET5X_FA5
- 儀器函數: CLR, MCurr, MVolt, OnOff, SCurr, SON, SVolt, switch
- DUT 連線: "DLL:DUTQDART.DLL":2, "APP":2
- 步驟數: 251 | CLI: 0 | Dev: 251 | Validation: 25
- Phase 分佈: 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 97:2, 19:1, 20:1, 21:1, 22:1, 23:1, 24:1, 25:1, 26:1, 27:1
- ExecMode: 0:91, 1:114, 2:0:35, 8:6, 2:7:2, 4:2,11:1, 4:20,20:1, 4:6,4:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求

## 27. D:\((Python TOOL\TrainingLLM\Centimani DOC\scripe_EXCEL\ZEBRA\Zebra_20190725_TestFlow0801.XLSX
- 工作表: Properties, Instrument, Switch, DUTs, L10A_FA5, ET5X_FA5
- 儀器函數: CLR, MCurr, MVolt, OnOff, SCurr, SON, SVolt, switch
- DUT 連線: "DLL:DUTQDART.DLL":2, "APP":2
- 步驟數: 264 | CLI: 0 | Dev: 264 | Validation: 25
- Phase 分佈: 1:2, 2:2, 3:2, 4:2, 5:2, 6:2, 7:2, 8:2, 9:2, 10:2, 11:2, 12:2, 13:2, 14:2, 15:2, 16:2, 17:2, 18:2, 97:5, 19:1, 20:1, 21:1, 22:1, 23:1, 24:1, 25:1, 26:1
- ExecMode: 0:100, 1:117, 2:0:36, 8:6, 2:7:2, 3:1, 4:2,11:1, 4:20,20:1
- 為什麼這樣寫: 以儀器量測為主：Send 有較多 :Dev.Function 呼叫，符合硬體量測/校準需求；使用 Validation 進行上下限/型別檢核，對齊規格要求
