
Set WshShell = CreateObject("WScript.Shell")

WshShell.CurrentDirectory = "C:\Users\adim\Desktop\Mark-LIII-main"

WshShell.Run """C:\Users\adim\Desktop\Mark-LIII-main\.venv\Scripts\pythonw.exe"" ""C:\Users\adim\Desktop\Mark-LIII-main\jarvis_wake.py""", 0, False
