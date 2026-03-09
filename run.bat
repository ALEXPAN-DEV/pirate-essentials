@echo off
chcp 65001 >nul
title Pirate Essentials

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...
    winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
)

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Failed to install Python.
    pause
    exit /b 1
)

python src\main.py

echo.
pause