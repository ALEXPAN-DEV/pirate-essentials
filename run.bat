@echo off
chcp 65001 >nul
title Pirate Essentials

echo Checking Python...

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
    
    echo Refreshing environment...
    set "PATH=%PATH%;C:\Users\%USERNAME%\AppData\Local\Programs\Python\Python312\"
)

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python installation failed.
    pause
    exit /b 1
)

echo Python detected.
echo Starting Pirate Essentials...

python src\main.py

echo.
pause