# Using the `re` module, write a function that validates if a string is a valid email format. Test it on 5 different strings (some valid, some invalid).

import re

def emailEval(mlist):
    for mail in mlist:
        if re.fullmatch(r"[\w.+-]+@[\w.-]+\.\w+", mail):
            print(f"{mail} is Valid Email.")
        else:
            print(f"{mail} is not a Valid Email.")

emailList = [
    "john.doe@gmail.com",
    "alice@@yahoo.com",
    "user_123@example.co.uk",
    "mike.smith@.com",
    "contact-us+support@company.org",
    "@gmail.com",
    "random text user@domain.com more junk"
]

emailEval(emailList)