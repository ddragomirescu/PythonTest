import random
import string

def generate_random_password(length=12):
    # Define character sets to include in the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]

    # Fill the rest of the password length with random characters from all sets
    # password += random.choices(all_characters, k=length-4)
    
    # Fill the rest of the password length with random characters from letters and digits, only 1 special character
    remaining_length = length - 4
    password += random.choices(lowercase_letters + uppercase_letters + digits, k=remaining_length)

    # Shuffle the password list to make it more random
    random.shuffle(password)

    # Convert list to string
    return ''.join(password)

# Generate a random password of desired length
password_length = 12  # You can change the length if needed
random_password = generate_random_password(password_length)
print(f"Generated random password: {random_password}")
