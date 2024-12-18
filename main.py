import string
import random
import json
import os
from cryptography.fernet import Fernet
from nltk.corpus import words


def load_or_generate_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
    return key
def encrypt_password(password: str, key: bytes) -> str:
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password.decode()

def decrypt_password(encrypted_password: str, key: bytes) -> str:

def checkLength(password: str) -> int:
    if len(password) < 8:
        return 3    # Password is too short
    elif len(password) > 30:
        return 2    # Password is too long
    return 1    # Valid length

def generateRecommendations(password):
    word_list = words.words()  # load word list
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_chars = upper + digits

    has_upper = any(char.isupper() for char in password)
    has_special = any(char in special for char in password)
    has_digit = any(char.isdigit() for char in password)

    status = checkLength(password)
    if status == 3:  # Too short
        print("[ERROR] Password too short: \n")
        print("\tShort passwords are inherently less secure. Each additional character in a password exponentially increases the number of possible combinations,\n thereby enhancing its security. Short passwords, often less than eight characters, are simply too easy to crack.\n")
    elif status == 2:
        print("[WARNING] Password too long: \n")
        print("\tOverly long passwords may be impractical to use and manage. Consider reducing the length for usability without compromising security.\n")
    
    if not has_upper:
        print("[WARNING] Password lacks uppercase letters:\n")
        print("\tPasswords with uppercase letters are harder to guess. Mix upper and lowercase letters for better security.\n")
    if not has_special:
        print("[WARNING] Password lacks special characters: \n")
        print("\tSpecial characters add complexity and make passwords more secure against brute-force attacks.\n")
    if not has_digit:
        print("[WARNING] Password lacks digits:")
        print("\tPasswords with digits add numerical complexity and are harder to guess.\n")

    if(status == 2):  # Truncate overly long passwords
        password = password[:25]
        print("[INFO] Your password has been truncated to 25 characters for practical recommendations. \n")
        print(f"[MESSAGE] This is your password shortened: {password}")

    new_length = max(len(password), 12, random.randint(12, 20))  # Ensure at least 12+ characters
    recommendations = []

    for _ in range(3):
        # Start with original password
        new_password = list(password)
        word = random.choice(word_list)
        new_password.append(word)

        if not has_upper:
            new_password.append(random.choice(upper))
        if not has_special:
            special_count = random.randint(3, 6)
            new_password += random.choices(special, k=special_count)
        if not has_digit:
            new_password.append(random.choice(digits))

        while(len(new_password) < new_length):
            new_password.append(random.choice(all_chars))

        random.shuffle(new_password)
        recommendations.append(''.join(new_password))
    
    return recommendations

def evaluatePassword(password: str):
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation    

    has_upper = any(char.isupper() for char in password)
    has_special = any(char in special for char in password)
    has_digit = any(char.isdigit() for char in password)
    status = checkLength(password)

    # Check if the password meets all requirements
    if status == 1 and has_upper and has_special and has_digit:
        print("[SUCCESS] Your password meets all the requirements!")
        print("\t- It is of valid length.")
        print("\t- It contains uppercase letters, digits, and special characters.")
        print("\nWould you like to generate some additional strong passwords? (y/n)")
        choice = input().strip().lower()
        if choice == 'y':
            recommendations = generateRecommendations(password)
            print("\nHere are some recommended strong passwords: ")
            for idx, rec in enumerate(recommendations, start=1):
                print(f"{idx}. {rec}")
        else:
            print("Great! Your password is strong enough. You can move on!")
    else:
        print("[FAILURE] Your password does not meet all requirements. Here's why:")
        recommendations = generateRecommendations(password)  # Always generate recommendations even on failure
        print("\nHere are some recommended strong passwords: ")
        for idx, rec in enumerate(recommendations, start=1):
            print(f"{idx}. {rec}")

class passwordManager:
    def __init__(self, key):
    
    def load_passwords(self):

    def save_passwords(self):

    def add_password(self):

    def get_password(self, service: str):

    def delete_password(self, service: str):

    def list_passwords(self):

    def evaluate_password(self):




def main():
    key = load_or_generate_key()
    pm = passwordManager(key)

    while True:
        print("\nPassword Manager: ")
        print("1. Add a new password.")
        print("2. Retrieve a password")
        print("3. Delete a password")
        print("4. List all passwords")
        print("5. Generate password recommendations")
        print("6. Evaluate Password")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == 1:
            service = input("Enter the service name (e.g., Facebook): ").strip()
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()
            pm.add_password(service, username, password)
        elif choice == 2:
            service = input("Enter the service name (e.g., Facebook): ").strip()
            print(pm.get_password(service))
        elif choice == 3:
            service = input("Enter the service name(e.g., Facebook) over the password you want to delete: ").strip()
            pm.delete_password(service)
        elif choice == 4:
            print(pm.list_passwords())
        elif choice == 5:
            password = input("Enter your password to generate recommendations: ").strip()
            recommendations = generateRecommendations(password)
            print("\nHere are some recommended strong passwords: ")
            for idx, rec in enumerate(recommendations, start = 1):
                print(f"{idx}, {rec}")
        elif choice == 6:
            password = input("Enter your password to be evaluated: ").strip()
            pm.evaluate_password(password)
        elif choice == 7:
            print("Exiting Password Manager.")
            break
        else:
            print("Invalid Choice. Please try again.")


if __name__ == "__main__":
    main()