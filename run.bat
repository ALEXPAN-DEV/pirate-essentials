@echo off
chcp 65001 >nul
title Pirate Essentials

echo Checking Python...

python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    
    winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
    
    echo.
    echo Python installed. Restarting installer...
    echo.

    pause
    exit
)

echo Python detected.
echo Starting Pirate Essentials...

python src\main.py

echo.
pause