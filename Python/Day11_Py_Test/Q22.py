# Random password generator. Params: `length`, `use_upper=True`, `use_digits=True`, `use_symbols=True`. Generate 5 passwords. Rate each as weak (one character type), medium (two types), strong (three+ types). Save all passwords and ratings to a file with the generation timestamp.

from datetime import datetime
from pathlib import Path
import random, string

def passGen():
    global passInfo
    pool = string.ascii_lowercase

    passLen = int(input("Enter the Length of password to generate: "))
    passInfo += (f'Password Length: {passLen}\n\n')

    while True:
        print("Use Uppercase letters in Password?")
        use_upper = input().strip().lower()
        if use_upper in ('true', 'yes', 'y', '1'):
            use_upper = True
            pool += string.ascii_uppercase
            break
        elif use_upper in ('false', 'no', 'n', '0'):
            use_upper = False
            break
        else:
            print("Invalid Choice")

    passInfo += (f'Use Uppercase letters in Password?: {use_upper}\n')

    while True:
        print("Use Digits in Password?")
        use_digits = input().strip().lower()
        if use_digits in ('true', 'yes', 'y', '1'):
            use_digits = True
            pool += string.digits
            break
        elif use_digits in ('false', 'no', 'n', '0'):
            use_digits = False
            break
        else:
            print("Invalid Choice")

    passInfo += (f'Use Digits in Password?: {use_digits}\n')

    while True:
        print("Use Symbols in Password?")
        use_symbols = input().strip().lower()
        if use_symbols in ('true', 'yes', 'y', '1'):
            use_symbols = True
            pool += string.punctuation
            break
        elif use_symbols in ('false', 'no', 'n', '0'):
            use_symbols = False
            break
        else:
            print("Invalid Choice")

    passInfo += (f'Use Symbols in Password?: {use_symbols}\n\n')

    for x in range(5):
        password = "".join(
            random.choices(pool, k = passLen)
        )
        passDict = {
            "Password" : password,
            "Timestamp" : datetime.now().strftime("%d-%m-%Y %H:%M")
        }
        passList.append(passDict)

    return passList
        
def ratePass(plist):
    for passwords in plist:
        pwd = passwords["Password"]
        ratingSum = 1
        
        if any(char.isupper() for char in pwd):
            ratingSum += 1

        if any(char.isdigit() for char in pwd):
            ratingSum += 1

        if any(char in string.punctuation for char in pwd):
            ratingSum += 1

        
        if ratingSum == 1:
            strength = "Low"
        elif ratingSum == 2:
            strength = "Medium"
        elif ratingSum >= 3:
            strength = "Strong"
        
        passwords["Strength"] = strength

passList = []
passInfo = ""

listOfPass = passGen()
ratePass(listOfPass)

passInfo += ('\nPasswords Generated:\n')
for paswords in passList:
    prevStr = (f'Password: {paswords["Password"]} | Timestamp: {paswords["Timestamp"]} | Strength: {paswords["Strength"]}\n')
    passInfo += prevStr


passFile = Path("PasswordFile.txt")
passFile.write_text(passInfo)