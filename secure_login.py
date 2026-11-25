import hashlib
import secrets
import hmac

username = "admin"
password = "StrongPassword@123"

salt = secrets.token_bytes(16)

stored_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    200000
)

print("Account Created Successfully!")

login_user = input("Enter Username: ")
login_pass = input("Enter Password: ")

login_hash = hashlib.pbkdf2_hmac(
    "sha256",
    login_pass.encode(),
    salt,
    200000
)

if login_user == username and hmac.compare_digest(
    login_hash, stored_hash
):
    print("Login Successful!")
else:
    print("Login Failed!")
