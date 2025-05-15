import re

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak (Too short)"
    
    # Check for uppercase, lowercase, digits, and special chars
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score == 4:
        return "Very Strong"
    elif score == 3:
        return "Strong"
    elif score == 2:
        return "Moderate"
    else:
        return "Weak (Needs more complexity)"
    
# Test the function
password = input("Enter a password: ")
print("Password strength:", check_password_strength(password))
