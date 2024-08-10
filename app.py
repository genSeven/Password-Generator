import random
import string

def generate_password(length):
    if length < 4:  # Ensure password is at least 4 characters long to include all character types
        return "Password length should be at least 4."

    # Define the character sets to be used in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one character from each character set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random choices from all character sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure the first few characters aren't always predictable
    random.shuffle(password)

    # Convert the list of characters into a string and return it
    return ''.join(password)

def main():
    print("Password Generator")

    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("Enter the desired password length (minimum 4): "))
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
