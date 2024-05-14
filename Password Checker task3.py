import re

def password_strength(password):
    length = len(password)
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_number = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    strength = 0
    
    # Criteria for password strength
    if length >= 8:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_number:
        strength += 1
    if has_special:
        strength += 1
    
    return strength

def main():
    password = input("Enter your password: ")
    strength = password_strength(password)
    
    if strength == 5:
        print("Password is very strong.")
    elif strength >= 3:
        print("Password is strong.")
    elif strength >= 2:
        print("Password is medium strength.")
    elif strength >= 1:
        print("Password is weak.")
    else:
        print("Password does not meet minimum criteria.")

if __name__ == "__main__":
    main()