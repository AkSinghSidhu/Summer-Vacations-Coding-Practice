# You have 3 JSON files each containing a list of user objects (some users repeat across files with different fields). Merge them so each user appears once with all fields combined. If a field conflicts, keep the last-seen value. Save merged result. Handle missing files gracefully.

from pathlib import Path
import os, json, random


files = ["Users/users_a.json", "Users/users_b.json", "Users/users_c.json"]
all_users = []


for filename in files:
    try:
        with open(filename, "r") as file:
            all_users.extend(json.load(file))

    except FileNotFoundError:
        print(f"{filename} not found, skipping")

    except json.JSONDecodeError:
        print(f"{filename} invalid JSON, skipping")


dictUsers = {}
for user in all_users:
    uid = user["id"]
    if uid in dictUsers:
        dictUsers[uid].update(user)
    else:
        dictUsers[uid] = user

try:
    with open("Users/mergedUsers.json", "w") as file:
        json.dump(dictUsers, file, indent=4)

except OSError:
    print("File write Fail!")