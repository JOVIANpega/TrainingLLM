@echo off
chcp 65001 >nul
cd /d %~dp0

echo ===============================================
echo    MU310 Firmware Flashing Tool v1.0
echo ===============================================

:: === Step 1: Check ADB connection state ===
echo === Step 1: Check ADB connection state ===
echo Executing adb devices...

for /f "skip=1 tokens=*" %%A in ('adb devices 2^>nul') do (
    if not "%%A"=="" (
        echo Found device: %%A
        set "DEVICE_FOUND=1"
        goto :device_check_done
    )
)

:device_check_done
if not defined DEVICE_FOUND (
    echo.
    echo [ERROR] ADB device not found!
    echo Please check:
    echo 1. USB cable is normal
    echo 2. Device USB debugging mode is enabled
    echo 3. ADB driver is properly installed
    echo.
    pause
    exit /b 1
)

echo [SUCCESS] ADB device connection normal
echo.

:: === Step 2: Check if DM PORT exists ===
echo === Step 2: Check if DM PORT exists ===
set "DM_PORT="

for /f "tokens=*" %%A in ('powershell -Command "Get-WmiObject Win32_PnPEntity | Where-Object { $_.Name -like '*DM PORT*' -and $_.Name -like '*COM*' } | Select-Object -ExpandProperty Name" 2^>nul') do (
    for /f "tokens=2 delims=()" %%B in ("%%A") do (
        set "DM_PORT=%%B"
        echo Found DM PORT: %%A
    )
)

if not defined DM_PORT (
    echo.
    echo [ERROR] DM PORT not found!
    echo Please check:
    echo 1. Device driver is properly installed
    echo 2. Device is properly connected
    echo 3. COM port is occupied by other programs
    echo.
    pause
    exit /b 1
)

echo [SUCCESS] Found DM PORT = %DM_PORT%
echo.

:: === Step 3: Check if firmware file exists ===
echo === Step 3: Check firmware file ===
if not exist "MU310-Q611GT_V1.1.0.0_1_modem.bin" (
    echo [ERROR] Firmware file not found: MU310-Q611GT_V1.1.0.0_1_modem.bin
    echo Please confirm firmware file is in current directory
    pause
    exit /b 1
)

echo [SUCCESS] Firmware file exists
echo.

:: === Step 4: Start firmware flashing process ===
echo === Step 4: Start firmware flashing process ===
echo.

echo [4.1] Uploading firmware to device...
adb push "MU310-Q611GT_V1.1.0.0_1_modem.bin" /usrdata/cache/ufs/update.zip
if %errorlevel% neq 0 (
    echo [ERROR] Firmware upload failed!
    pause
    exit /b 1
)
echo [SUCCESS] Firmware upload completed

echo.
echo [4.2] Executing sync operation...
adb shell sync
adb shell sync
echo [SUCCESS] Sync operation completed

echo.
echo [4.3] Stopping related system services...
adb shell systemctl stop pega-5GNR-init
adb shell systemctl stop pega-framework-init
adb shell systemctl stop pega-atcmder-init
echo [SUCCESS] System services stopped

echo.
echo [4.4] Preparing to send firmware update command...
adb shell fuser /dev/smd7
echo [SUCCESS] /dev/smd7 status check completed

echo.
echo [4.5] Sending firmware update command...
adb shell "printf 'at\r\n' > /dev/smd7"
timeout /t 2 /nobreak >nul
adb shell "printf 'AT+QFOTADL=\"/usrdata/cache/ufs/update.zip\"\r\n' > /dev/smd7"

echo.
echo ===============================================
echo [SUCCESS] Firmware flashing command sent!
echo.
echo Notes:
echo 1. Please wait for device to complete firmware update
echo 2. Do not disconnect during update process
echo 3. Device may restart automatically
echo 4. The entire process may take several minutes
echo ===============================================
echo.
echo MU310 burn in PASS and please wait 4 mins for update.

REM "Use PowerShell to read Windows device list, then filter out DM PORT related COM ports"
