#  Use `https://jsonplaceholder.typicode.com`. Fetch all 100 posts and all 10 users. Match posts to users. For each user: name, email, post count, and their 2 longest post titles. Save as clean JSON. Use a `requests.Session` and set a timeout on every call.

import requests , json
from pathlib import Path

session = requests.Session()
responsePost = session.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
postData = responsePost.json()

responseUser = session.get("https://jsonplaceholder.typicode.com/users", timeout=5)
userData = responseUser.json()

newList = []

for user in userData:
    uid = user["id"]
    userPosts = [post for post in postData if post["userId"] == uid]
    sortedPosts = sorted(userPosts, key = lambda post: len(post["title"]), reverse = True)
    twoTitles = sortedPosts[:2]
    count = len(userPosts)

    titles = []
    for post in twoTitles:
        titles.append(post["title"])

    newData = {
        "name": user["name"],
        "email": user["email"],
        "post_count": count,
        "longest_titles": titles
    }

    newList.append(newData)
    

with open("newJson.json", "w") as file:
    json.dump(newList, file, indent=4)