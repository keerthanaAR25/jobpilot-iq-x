@echo off
REM Quick startup verification script for JobPilot IQ X

echo.
echo ========================================
echo JobPilot IQ X - Startup Verification
echo ========================================
echo.

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Verifying dependencies...
python verify_imports.py

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✓ All dependencies verified!
    echo.
    echo You can now run the application with:
    echo   streamlit run app.py
    echo.
    echo The app will be available at: http://localhost:8501
    echo.
) else (
    echo.
    echo ✗ Some dependencies are missing
    echo Please run: pip install -r requirements.txt
    echo.
)

pause
