import string

#Create a function to evaluate the password, length, capital letters, and atleast 2 special characters

#Create a function that returns recommendations to make the password stronger

#Shows password being used again John The Ripper? Be able to show the user
#that there password is either easy to be cracked or hard to crack



#Check the length of the password
def checkLength(password):
    if len(password) < 8:
        return "Error: Password length is too short (must be at least 8 characters)."
    elif len(password) > 30:
        return "Error: Password length is too long (must be less than 30 characters)."
    return "Valid length."

#Check that there is a special character in the password
def checkSpecialChar(password):
    specialChars = string.punctuation
    count = sum(1 for char in password if char in specialChars)
    if count < 2:
        return f"Error: Password needs at least 2 special characters."
    return "Contains enough special characters."
#Check for capital letters
def checkCapitals(password):
    count = sum(1 for char in password if char.isupper())
    if count == 0:
        return "Error: Password needs atleast 1 uppercase character."
    return "Contains capital letters."
#Function to evaluate password strength
def evaluate_strength(password):
    feedback = []
    feedback.append(checkLength(password))
    feedback.append(checkSpecialChar(password))
    feedback.append(checkCapitals(password))

    if all("Error" not in f for f in feedback):
        return "Strong password!", feedback
    return "Weak password!", feedback
#Function to generate recommendations
def generateRecommendations(password):
    _, feedback = evaluate_strength(password)
    recommendations = [f for f in feedback if "Error" in f]
    return "Recommendations to improve password strength: \n" + "\n".join(recommendations)

def passwordChecker(password):
    print("Evaluating password...")
    strength, feedback = evaluate_strength(password)
    recommendations = generateRecommendations(password)
    
    print("\nResults:")
    print("Strength:", strength)
    print("Feedback:")
    for line in feedback:
        print(" -", line)
    print("\n", recommendations)



password = input("Enter a password to evaluate: ")
passwordChecker(password)