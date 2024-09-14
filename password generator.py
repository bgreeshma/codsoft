import random
import string

def generate_password(length=12):
    # Define character sets for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one lowercase, one uppercase, one digit, and one special character
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Join the list into a string
    return ''.join(password)
# Generate a password with the default length of 12
password = generate_password()
print("Generated Password:", password)