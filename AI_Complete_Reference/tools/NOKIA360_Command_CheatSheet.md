# NOKIA360 指令與腳本速查表

## 來源指令表

- D:\((Python TOOL\TrainingLLM\Centimani DOC\CMD＿TABLE\Kangaroo_Diag_Command_List_v1.4.xlsx
- D:\((Python TOOL\TrainingLLM\Centimani DOC\CMD＿TABLE\MU310 _COMMAND LIST_0.1.xlsx
- D:\((Python TOOL\TrainingLLM\Centimani DOC\CMD＿TABLE\MU310_Command_Verification_SR.xlsx
- D:\((Python TOOL\TrainingLLM\Centimani DOC\CMD＿TABLE\VAL360_Diag_Command_List_Requirement_20250627.xlsx

## 指令欄位映射建議

- command: 指令/命令/CMD/CLI/DIAG
- description: 用途/說明
- reply: 回覆/Response
- example: 範例


## 代表性指令樣本 (最多200)

1. `fw_printenv -n mfg (只要不是1下次開機就會是一般模式)` - MFG mode read/write
2. `uci -P /var/state get pega.fw.cur_ver` - SW ver
3. `fw_printenv -n hwver` - HW ver
4. `atcli at+cgmr` - Modem FW version
5. `fw_printenv -n pega_model` - Model Name read/write
6. `fw_printenv -n sn` - Unit SN read/write
7. `fw_printenv -n mb_sn` - MB SN read/write
8. `fw_printenv -n uuid` - UUID read/write
9. `/etc/diag.sh resetBtnStatusGet

Output:( 1: pressed, 0 released)
#INFO#1:pressed#END
#INFO#0:released#END` - Get reset button status
10. `atcli at+cpin? (expect:  +CPIN: READY)` - Get sim detect
11. `atcli at+ccid` - Get sim iccid (need insert SIM)
12. `atcli at+cimi` - Get sim imsi (need insert SIM)
13. `atcli at+gsn` - Modem imei read/write
14. `fw_printenv -n eth0_addr` - MAC address
15. `fw_printenv -n fanless` - w/ or w/o FAN
16. `/bin/fan.sh` - Status
17. `/bin/fan.sh | grep duty_cycle` - Duty
18. `/bin/fan.sh | grep rpm` - Speed (RPM)
19. `fw_printenv -n wifi0_addr` - MAC address
20. `fw_printenv -n wifi0_ssid` - SSID (default)
21. `fw_printenv -n wifi0_password` - key (default)
22. `iwconfig wlan0 | grep ESSID | cut -d : -f 2 | tr -d '"'` - SSID (MFG testing)
23. `iwlist wlan0 channel | grep Current` - Channel (MFG testing)
24. `5g  on off status:
atcli at+cfun?` - 5G on/off 

25. `atcli 'AT+QTHERMAL="thermal_level"'` - 5G module Thermal
26. `atcli 'AT+QCFG="usbcfg"'` - Set USB port functions (AT/ADB enabled)
27. `fw_printenv -n fr2_only` - FR2 only
28. `fw_printenv -n fr2_band` - FR2 band list
29. `fw_printenv -n wifi_disable` - Wi-Fi disable
30. `atcli 'AT+QCFG="ims"'` - Disable IMS (CBNG only)
31. `uci -P /var/state show pega.board.model` - 
32. `uci -P /var/state show pega.fw.cur_ver` - 
33. `uci -c /var/etc show cellstatus.sim.status` - 
34. `atcli 'AT+GMM' | awk '{if(NR==2){print "module_sku=\047" $1 "\047"}}'` - 
35. `ethtool eth0 | grep Speed | awk '{print "ethernet_linkSpeed=\047" $2 "\047"}'` - 
36. `ping x.x.x.x` - 
37. `ping -6 xxxx::xxxx:xxxx` - 
38. `echo 255 > /sys/class/leds/signal\:blue/brightness
echo 0 > /sys/class/leds/signal\:blue/brightness
echo 255 > /sys/class/leds/signal\:green/brightness
echo 0 > /sys/class/leds/signal\:green/brightness
echo 255 > /sys/class/leds/signal\:red/brightness
echo 0 > /sys/class/leds/signal\:red/brightness
echo 255 > /sys/class/leds/status\:red/brightness
echo 0 > /sys/class/leds/status\:red/brightness
echo 255 > /sys/class/leds/status\:blue/brightness
echo 0 > /sys/class/leds/status\:blue/brightness
echo 255 > /sys/class/leds/status\:green/brightness
echo 0 > /sys/class/leds/status\:green/brightness` - 
39. `systemctl stop pu_resetBtn_monitor.service
touch /tmp/MFG
/usr/sbin/pu_resetBtn_monitor &

cat /tmp/reset_button
按下Reset button 10 秒後放開` - 
40. `rm -f /tmp/MFG
systemctl restart pu_resetBtn_monitor.service
按下Reset button 10 秒後放開` - 
41. `[發送] uci -P /var/state get pega.led.booting_state
uci -P /var/state get pega.led.booting_state
Booting
root@Kangaroo:~# 
root@Kangaroo:~#` - 
42. `[發送] atcli at+cgmm
atcli at+cgmm
at+cgmm
RG520N-EB

OK
root@Kangaroo:~# 
root@Kangaroo:~#` - 
43. `[發送] uci -P /var/state get pega.fw.cur_ver
uci -P /var/state get pega.fw.cur_ver
V0.0.0.0_1
root@Kangaroo:~# 
root@Kangaroo:~#` - 
44. `[發送] manufacture.sh
manufacture.sh
manufacture.sh  : set mfg mode
root@Kangaroo:~# 
root@Kangaroo:~#` - 
45. `[發送] fw_setenv pega_model MU310
fw_setenv pega_model MU310
Cannot read environment, using default
root@Kangaroo:~# 
root@Kangaroo:~#` - 
46. `[發送] fw_printenv -n pega_model
fw_printenv -n pega_model
MU310
root@Kangaroo:~# 
root@Kangaroo:~#` - 
47. `[發送] fw_setenv wifi0_ssid WIFI_SSIDName
fw_setenv wifi0_ssid WIFI_SSIDName
root@Kangaroo:~# 
root@Kangaroo:~#` - 
48. `[發送] fw_printenv -n wifi0_ssid
fw_printenv -n wifi0_ssid
WIFI_SSIDName
root@Kangaroo:~# 
root@Kangaroo:~#` - 
49. `[發送] fw_setenv wifi0_password 12345678
fw_setenv wifi0_password 12345678
root@Kangaroo:~# 
root@Kangaroo:~#` - 
50. `[發送] fw_printenv -n wifi0_password
fw_printenv -n wifi0_password
12345678
root@Kangaroo:~# 
root@Kangaroo:~#` - 

## 腳本欄位填寫範例（三測項）

- 版本號碼: TestID=查表, Send=UART1@ver, Reply=@Version:, Ref=version

- 電壓: TestID=查表, Instrument=DMM.MeasureV, Send=:DMM.MeasureV,"CH1","DC", Validation=(voltage,%f,4.75,5.25)

- BT: TestID=查表, Send=UART1@bt status, Reply=@BT:ON


## TestID 查詢

- 依 `System.ini > TestItemCodeFile` 或專案根目錄的 `Test Item Code V*.xlsx` 查表
