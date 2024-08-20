# Chrome Password Extractor

This Python script extracts saved passwords from Google Chrome on a Windows machine. It retrieves encrypted passwords stored in Chrome's local database, decrypts them using the system's encryption key, and prints the origin URL, username, and password in the console.

## Features

- Extracts saved passwords from Google Chrome.
- Decrypts the passwords using the system's encryption key.
- Prints the origin URL, username, and password.

## Prerequisites

- **Python 3.x** installed on your system.
- Required Python libraries:
  - `pycryptodome`
  - `pypiwin32`

## Installation

1. Clone the repository or download the script.
2. Install the required libraries:
    ```bash
    pip install pycryptodome pypiwin32
    ```

## Usage

1. Save the script as `testchrome.py`.
2. Open Command Prompt or Terminal.
3. Navigate to the directory where the script is located.
4. Run the script using Python:
    ```bash
    testchrome.py
    ```
5. The script will display the saved passwords in the console.

## Legal Disclaimer

This script is intended for educational purposes only. Unauthorized access to personal data, including passwords, is illegal and unethical. Use this tool only on systems where you have explicit permission to do so.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
