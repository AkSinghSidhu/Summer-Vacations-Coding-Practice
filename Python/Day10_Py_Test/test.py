# CLI contact book (no OOP). Loads from `contacts.json` at start. Supports: add, delete, search by name or city, list all, update field, save. Each contact: name, phone (must be 10 digits), email (must contain @). Error handling everywhere. Auto-saves on exit.

from pathlib import Path
import os, json

def contactBook():
    global myContacts

    while True:
        print("1. Add\n2. Delete\n3. Search\n4. List\n5. Update\n6. Exit")
        choice = input("Choose: ")
        if choice == "1":
            addContacts()
        elif choice == "2":
            delContact()
        elif choice == "3":
            searchContact()
        elif choice == "4":
            listAll()
        elif choice == "5":
            updateField()
        elif choice == "6":
            break
        else:
            print("Invalid input")
    
    return myContacts

def addContacts():
    contact = {}
    name = input("Enter the Contacts name: ")
    contact["name"] = name
    
    phoneCheck = checkPhone()
    contact["phone"] = phoneCheck
    
    emailCheck = checkEmail()
    contact["email"] = emailCheck

    city = input("Enter the City name of Contact: ")
    contact["city"] = city

    myContacts.append(contact)

def checkPhone():
    phone = input("Enter a valid phone number: ")
    if len(phone) == 10 and phone.isdigit():
        return phone
    else:
        print("Entered Phone number is invalid")
        return checkPhone()
    
def checkEmail():
    email = input("Enter a valid Email address: ")
    if "@" in email:
        return email
    else:
        print("Entered Email address is invalid!")
        return checkEmail()

def delContact():
    if not myContacts:
        print("No contacts yet")
        return
    print("To delete ")
    contact = checkPhone()
    delIdx = next((idx for idx,item in enumerate(myContacts) if item["phone"] == contact), None)
    if delIdx is None:
        print("Contact not found")
        return
    myContacts.pop(delIdx)
    

def searchContact():
    contact = checkPhone()

    search = next((phone for phone in myContacts if phone["phone"] == contact), None)
    if search:
        print(f"{contact} found in Contact Book\nContact Details:\n{search}")
    else:
        print(f"{contact} Not found in Contact Book")

def listAll():
    print(f"All Contacts: {myContacts}")

def updateField():
    if not myContacts:
        print("No contacts yet")
        return
    contact = checkPhone()
    idxUpdate = next((idx for idx,item in enumerate(myContacts) if item["phone"] == contact), None)
    if idxUpdate is None:
        print("Contact not found")
        return

    while True:
        print("1. Update Name\n2. DUpdate Phone Number\n3. Update Email Address\n4. Update City\n5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            newName = input("Enter new name for the contact: ")
            myContacts[idxUpdate]["name"] = newName
        elif choice == "2":
            contact = checkPhone()
            myContacts[idxUpdate]["phone"] = contact
        elif choice == "3":
            newEmail = checkEmail()
            myContacts[idxUpdate]["email"] = newEmail
        elif choice == "4":
            newCity = input("Enter new City for the contact: ")
            myContacts[idxUpdate]["city"] = newCity
        elif choice == "5":
            break
        else:
            print("Invalid input")

contactsFolder = Path("ContactsFolder")
contactsFolder.mkdir(parents=True, exist_ok=True)

myContacts = []
try:
    with open("ContactsFolder/contacts.json", "r") as file:
        myContacts = json.load(file)
except FileNotFoundError:
    myContacts = []
except json.JSONDecodeError:
    myContacts = []

try:
    contactBook()
finally:
    try:
        with open("ContactsFolder/contacts.json", "w") as file:
            json.dump(myContacts, file)
    except Exception as e:
        print(f"Failed to save: {e}")