
@echo off
title JARVIS - CodeShalaByKMFL
cd /d "C:\Users\adim\Desktop\Mark-LIII-main"

call "C:\Users\adim\Desktop\Mark-LIII-main\.venv\Scripts\activate.bat"
if errorlevel 1 (
    echo Virtual environment activate nahi hua.
    pause
    exit /b 1
)

python main.py
pause
