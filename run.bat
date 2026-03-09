@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
title Pirate Essentials

if /I "%~1"=="--after-python-install" goto after_python_install

echo Checking Python...

python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python not found. Installing Python...

    winget install -e --id Python.Python.3.12 --source winget --accept-source-agreements --accept-package-agreements

    echo.
    echo Python installation finished. Restarting Pirate Essentials...
    start "" cmd /c ""%~f0" --after-python-install"
    exit /b 0
)

goto bootstrap

:after_python_install
echo Re-checking Python after installation...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is still not available in the current PATH.
    echo Please close this window and run Pirate Essentials again manually.
    pause
    exit /b 1
)

:bootstrap
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