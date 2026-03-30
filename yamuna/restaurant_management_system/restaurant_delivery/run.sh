#!/bin/bash

# Restaurant Delivery Management System - Quick Start Script for Linux/Mac
# This script will set up and run the application

echo ""
echo "========================================"
echo "Restaurant Delivery Management System"
echo "Quick Start Setup"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python 3.7+ from https://www.python.org/downloads/"
    exit 1
fi

python3 --version
echo "[1/5] Checking Python installation... OK"
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "[2/5] Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "            Virtual environment created... OK"
else
    echo "[2/5] Virtual environment already exists... OK"
fi
echo ""

# Activate virtual environment
echo "[3/5] Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi
echo "            Virtual environment activated... OK"
echo ""

# Install dependencies
echo "[4/5] Installing Python dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    echo "Please check requirements.txt"
    exit 1
fi
echo "            Dependencies installed... OK"
echo ""

# Check MySQL connection
echo "[5/5] Checking MySQL connection..."
python3 -c "import MySQLdb" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "WARNING: MySQLdb not properly installed"
    echo "Please ensure MySQL Server is running"
    echo "and database is properly configured in app.py"
fi
echo "            MySQL check complete"
echo ""

# Start the application
echo ""
echo "========================================"
echo "Starting Restaurant Delivery System..."
echo "========================================"
echo ""
echo "The application will be available at:"
echo "http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py
