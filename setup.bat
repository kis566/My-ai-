@echo off
setlocal

echo ============================================
echo  Jarvis Wake Word Setup (openWakeWord)
echo ============================================

py -3.12 --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python 3.12 nahi mila. 
    echo Pehle Python 3.12 install karein: https://www.python.org/downloads/release/python-3129/
    echo Install karte waqt "Add python.exe to PATH" tick karein.
    pause
    exit /b 1
)

echo [1/3] Virtual environment bana rahe hain...
if not exist "%~dp0venv" (
    py -3.12 -m venv "%~dp0venv"
)

echo [2/3] Pip update kar rahe hain...
call "%~dp0venv\Scripts\activate.bat"
python -m pip install --upgrade pip

echo [3/3] Packages install kar rahe hain (isme 2-3 minute lagenge)...
pip install openwakeword pyaudio numpy

echo.
echo Setup complete! Ab run_jarvis.bat chalao.
pause