@echo off
REM Restaurant Delivery Management System - Quick Start Script
REM This script will set up and run the application

echo.
echo ========================================
echo Restaurant Delivery Management System
echo Quick Start Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [1/5] Checking Python installation... OK
echo.

REM Check if virtual environment exists
if not exist "venv" (
    echo [2/5] Creating virtual environment...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
    echo            Virtual environment created... OK
) else (
    echo [2/5] Virtual environment already exists... OK
)
echo.

REM Activate virtual environment
echo [3/5] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)
echo            Virtual environment activated... OK
echo.

REM Install dependencies
echo [4/5] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    echo Please check requirements.txt
    pause
    exit /b 1
)
echo            Dependencies installed... OK
echo.

REM Check MySQL connection
echo [5/5] Checking MySQL connection...
python -c "import MySQLdb" 2>nul
if errorlevel 1 (
    echo WARNING: MySQLdb not properly installed
    echo Please ensure MySQL Server is running
    echo and database is properly configured in app.py
)
echo            MySQL check complete
echo.

REM Start the application
echo.
echo ========================================
echo Starting Restaurant Delivery System...
echo ========================================
echo.
echo The application will be available at:
echo http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.

python app.py

pause
