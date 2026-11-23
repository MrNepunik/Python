print("Welcome to the Password Strength Checker")
print("Use a made-up password for testing, not your real password.")

password = input("\nEnter a password: ")

common_passwords = [
    "password", "password1", "password1!", "123456",
    "12345678", "123456789", "qwerty", "qwerty123",
    "admin", "admin123", "letmein", "12345",
    "1234567", "1234567890", "1234", "111111",
    "123123", "987654321", "abc123", "monkey",
    "dragon", "11111111", "baseball", "iloveyou",
    "trustno1", "123456789a", "welcome", "login",
    "princess", "qwertyuiop", "solo", "passw0rd",
    "starwars"
]

has_upper = False
has_lower = False
has_number = False
has_symbol = False

for character in password:
    if character.isupper():
        has_upper = True
    elif character.islower():
        has_lower = True
    elif character.isdigit():
        has_number = True
    elif not character.isspace():
        has_symbol = True

lower_password = password.lower()
has_pattern = False

for pattern in ["1234", "abcd", "qwerty", "asdf"]:
    if pattern in lower_password:
        has_pattern = True

has_repetition = False

for i in range(len(password) - 2):
    if password[i] == password[i + 1] == password[i + 2]:
        has_repetition = True

suggestions = []

if len(password) < 15:
    suggestions.append("Try using at least 15 characters.")

if lower_password in common_passwords:
    suggestions.append("Avoid common passwords.")

if has_pattern:
    suggestions.append("Avoid patterns like 1234 or qwerty.")

if has_repetition:
    suggestions.append("Avoid repeating the same character many times.")

if not password.strip():
    strength = "Weak"
    suggestions.append("Enter a password that is not empty or only spaces.")
elif lower_password in common_passwords:
    strength = "Weak"
elif len(password) < 8:
    strength = "Weak"
elif has_pattern or has_repetition:
    strength = "Weak"
elif len(password) < 15:
    strength = "Moderate"
else:
    strength = "Strong"

print("\n--- Password Check ---")
print("Length:", len(password))
print("Uppercase letters:", "Yes" if has_upper else "No")
print("Lowercase letters:", "Yes" if has_lower else "No")
print("Numbers:", "Yes" if has_number else "No")
print("Symbols:", "Yes" if has_symbol else "No")
print("Estimated strength:", strength)

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print("-", suggestion)

print("\nThis is a basic practice checker, not a security guarantee.")