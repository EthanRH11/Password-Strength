import string
import random
from nltk.corpus import words
#Create a function to evaluate the password, length, capital letters, and atleast 2 special characters

#Create a function that returns recommendations to make the password stronger

#Shows password being used again John The Ripper? Be able to show the user
#that there password is either easy to be cracked or hard to crack



#Check the length of the password
def checkLength(password: str) -> int:
    if len(password) < 8:
        return 3    #Password is too short
    elif len(password) > 30:
        return 2    #Password is too long
    return 1    #Valid length
def generateRecommendations(password):
    #TODO:
    #Rework entirely, explain why their password is weak, return relateed passwords that are strong
    #Take the password, review it, find what it is missing, generate random combos of characters to add 
    #into the password. Generate 3 different ones, return them in a vector of strings or maybe a stack,
    
    #Character Sets
    word_list = words.words() #load word list
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    all_chars = upper + digits

    #Analysis Flags
    has_upper = any(char.isupper() for char in password)
    has_special = any(char in special for char in password)

    status = checkLength(password)
    if status == 3: #Too short
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
    
    if(status == 2): #Truncate overly long passwords
        password = password[:25]
        print("[INFO] Your password has been truncated to 25 characters for practical recommendations. \n")
        print(f"[MESSAGE] This is your password shortened: {password}")


    new_length = max(len(password), 12, random.randint(12,20)) #Ensure atleast 12+ characters
    recommendations = []

    for _ in range(3):
        #start with original password
        new_password = list(password)
        word = random.choice(word_list)
        new_password.append(word)

        if not has_upper:
            new_password.append(random.choice(upper))

        special_count = random.randint(3,6)
        new_password += random.choices(special, k=special_count)

        while(len(new_password) < new_length):
            new_password.append(random.choice(all_chars))

        random.shuffle(new_password)
        recommendations.append(''.join(new_password))
    
    return recommendations


if __name__ == "__main__":
    user_password = input("Enter your password: ")
    recommendations = generateRecommendations(user_password)

    print("\nHere are some recommended stronger passwords: ")
    for idx, rec in enumerate(recommendations, start=1):
        print(f"{idx}. {rec}")

