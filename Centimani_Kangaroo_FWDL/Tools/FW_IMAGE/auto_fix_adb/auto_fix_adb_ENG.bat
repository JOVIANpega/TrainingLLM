chcp 65001 > nul

@echo off
setlocal enabledelayedexpansion

echo [STEP 1] Checking ADB device connection...
adb devices > adb_check.txt
findstr /R /C:"device$" adb_check.txt > nul

if %errorlevel%==0 (
    echo ✅ ADB is connected, no fix needed.
    del adb_check.txt
    exit /b
)

echo ⚠️ No ADB device detected. Attempting to fix...

echo [STEP 2] Sending AT command to set USB mode...
python fix_usbcfg.py

if %errorlevel% NEQ 0 (
    echo ❌ Failed to send AT command. Cannot proceed with fix.
    exit /b
)

echo ✅ AT command sent successfully. Waiting 90 seconds for reboot...
timeout /t 90 /nobreak > nul

echo [STEP 3] Rechecking ADB device connection...
adb devices > adb_check.txt
findstr /R /C:"device$" adb_check.txt > nul

if %errorlevel%==0 (
    echo ✅ ADB connection restored successfully!
) else (
    echo ❌ ADB still not connected after fix. Please check the device manually.
)

del adb_check.txt
exit /b
