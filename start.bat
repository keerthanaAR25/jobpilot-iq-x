@echo off
REM Quick Start Script for JobPilot IQ X (Windows)

echo.
echo 🚀 JobPilot IQ X - Quick Start
echo ==============================
echo.

REM Check Python version
echo Checking Python version...
python --version
echo.

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

echo Installing dependencies...
pip install -q -r requirements.txt

echo Initializing database...
python -c "from src.utils.database import Database; Database(); print('Database initialized')"

echo.
echo Setup complete!
echo.
echo 🚀 Starting JobPilot IQ X...
echo ============================
echo.
echo Access the app at: http://localhost:8501
echo.

streamlit run app.py
