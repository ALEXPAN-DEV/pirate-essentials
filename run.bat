@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
title Pirate Essentials

echo Checking Python...

python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...

    winget install -e --id Python.Python.3.12 --source winget --accept-source-agreements --accept-package-agreements

    python --version >nul 2>nul
    if %errorlevel% neq 0 (
        echo Python installation finished, but Python is not available in the current session yet.
        echo Restarting Pirate Essentials...
        start "" cmd /c "%~f0"
        exit /b 0
    )
)

echo Python detected.
echo Installing bootstrap dependencies...

python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install bootstrap dependencies.
    pause
    exit /b 1
)

cls
echo Starting Pirate Essentials...
python src\main.py

echo.
pause