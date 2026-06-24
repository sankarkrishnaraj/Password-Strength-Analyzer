import re
import random
import string
import hashlib

# Common Password List
common_passwords = ["123456", "password", "admin", "qwerty", "abc123"]

password = input("Enter Password: ")

# Common Password Check
if password in common_passwords:
    print("⚠ Common Password! Choose another password.")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Uppercase Check
if re.search("[A-Z]", password):
    score += 1

# Lowercase Check
if re.search("[a-z]", password):
    score += 1

# Number Check
if re.search("[0-9]", password):
    score += 1

# Special Character Check
if re.search("[!@#$%^&*]", password):
    score += 1

# Password Strength Result
if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")

# Strong Password Suggestion
if score < 5:
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    suggested_password = ''.join(
        random.choice(characters) for i in range(12)
    )
    print("Suggested Strong Password:", suggested_password)

# SHA-256 Hashing
hashed_password = hashlib.sha256(password.encode()).hexdigest()

print("\nPassword Hash:")
print(hashed_password)