@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
title Pirate Essentials

call :find_python
if defined PYTHON_EXE goto python_found

echo Checking Python...
echo Python not found. Installing Python...

winget install -e --id Python.Python.3.12 --source winget --accept-source-agreements --accept-package-agreements

call :find_python
if not defined PYTHON_EXE (
    echo.
    echo Python installation finished, but python.exe was not found automatically.
    echo Please close this window and run Pirate Essentials again.
    echo.
    pause
    exit /b 1
)

:python_found
echo Python detected:
echo %PYTHON_EXE%
echo Installing bootstrap dependencies...

"%PYTHON_EXE%" -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to upgrade pip.
    pause
    exit /b 1
)

"%PYTHON_EXE%" -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Failed to install bootstrap dependencies.
    pause
    exit /b 1
)

cls
echo Starting Pirate Essentials...
"%PYTHON_EXE%" src\main.py

echo.
pause
exit /b 0


:find_python
set "PYTHON_EXE="

for %%P in (
    python.exe
    py.exe
    "%LocalAppData%\Programs\Python\Python312\python.exe"
    "%LocalAppData%\Programs\Python\Python313\python.exe"
    "%LocalAppData%\Programs\Python\Python314\python.exe"
    "%LocalAppData%\Python\pythoncore-3.12-64\python.exe"
    "%LocalAppData%\Python\pythoncore-3.13-64\python.exe"
    "%LocalAppData%\Python\pythoncore-3.14-64\python.exe"
) do (
    call :test_python "%%~P"
    if defined PYTHON_EXE goto :eof
)

for /f "delims=" %%I in ('where python 2^>nul') do (
    call :test_python "%%~I"
    if defined PYTHON_EXE goto :eof
)

for /f "delims=" %%I in ('where py 2^>nul') do (
    call :test_python "%%~I"
    if defined PYTHON_EXE goto :eof
)

goto :eof


:test_python
%~1 --version >nul 2>nul
if %errorlevel% equ 0 (
    set "PYTHON_EXE=%~1"
)
goto :eof