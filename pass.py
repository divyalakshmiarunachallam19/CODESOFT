import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
print("Welcome to the Password Generator!")

# Input: Desired password length
length = int(input("Enter the desired length of the password: "))

# Generate and display the password
password = generate_password(length)
print(f"Your generated password is: {password}")
