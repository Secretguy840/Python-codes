import itertools
import string

def brute_force_attempt(password_length=4):
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    for guess in itertools.product(chars, repeat=password_length):
        attempts += 1
        guess = ''.join(guess)
        if guess == "test":  # Replace with your OWN test password
            return f"Password found: {guess} (in {attempts} attempts)"
    return "Password not found."

print(brute_force_attempt(4))  # Only for educational purposes!
