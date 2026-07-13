import re

def emailEval(mail):
    if re.fullmatch(r"[\w.+-]+@[\w.-]+\.\w+", mail):
        return True
    else:
        return False


if __name__ == "__main__":
    emailList = [
        "john.doe@gmail.com",
        "alice@@yahoo.com",
        "user_123@example.co.uk",
        "mike.smith@.com",
        "contact-us+support@company.org",
        "@gmail.com",
        "random text user@domain.com more junk"
    ]

    for email in emailList:
        if emailEval(email):
            print(f"{email} is Valid Email.")
        else:
            print(f"{email} is not a Valid Email.")