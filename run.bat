@echo off
chcp 65001 >nul
title Pirate Essentials

echo Checking Python...

python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...

    winget install -e --id Python.Python.3.12 --source winget --accept-source-agreements --accept-package-agreements

    echo.
    echo Python installed. Please run Pirate Essentials again.
    echo.
    pause
    exit /b 0
)

echo Python detected.
echo Installing bootstrap dependencies...

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Failed to install bootstrap dependencies.
    pause
    exit /b 1
)

echo Starting Pirate Essentials...
python src\main.py

echo.
pause