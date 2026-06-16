# CLI "article reader" using `https://jsonplaceholder.typicode.com/posts` as fake articles. Features: list all (paginated, 10 per page, n/p for next/prev), search by keyword in title, save to `favorites.json`, view favorites, remove a favorite by id. Error handling throughout.

from pathlib import Path
import requests, json, time

def articalReader():
    try:
        session = requests.Session()
        resArticle = session.get("https://jsonplaceholder.typicode.com/posts", timeout=5)
        resArticle.raise_for_status()
        articleData = resArticle.json()
        return articleData

    except requests.RequestException:
        print("Failed Connection.")


def listAll(data):
    articles = len(data)
    page_size = 10
    page = 1

    start = (page - 1) * page_size
    end = start + page_size
    for article in data[start:end]:
        print(f"Article Id: {article['id']}\nTitle: {article['title']}\n{article['body']}\nArticle Written By: {article['userId']}\n\n")
    while True:
        goto = input("Press 'n' to go to next page or 'p' for previous page or 'X' to exit: ").strip().lower()
        if goto in ("n", "N", "next", "Next"):
            page += 1
            if page > articles // page_size:
                page = articles // page_size
                print("Already on last page")
            start = (page - 1) * page_size
            end = start + page_size
            for article in data[start:end]:
                print(f"Article Id: {article['id']}\nTitle: {article['title']}\n{article['body']}\nArticle Written By: {article['userId']}\n\n")
        elif goto in ("p", "P", "previous", "Previous"):
            page -= 1
            if page <= 0:
                page = 1
                print("Already on first page")
            start = (page - 1) * page_size
            end = start + page_size
            for article in data[start:end]:
                print(f"Article Id: {article['id']}\nTitle: {article['title']}\n{article['body']}\nArticle Written By: {article['userId']}\n\n")
        elif goto in ("x", "X", "exit", "Exit"):
            break
        else:
            print("Invalid choice")

    return
    
def searchArticle(data):
    while True:
        ifSearch = input("Do you want to search for any article: ").strip().lower()
        if ifSearch in ('true', 'yes', 'y', '1'):
            keyword = input("Enter the keyword to search related articles: ")
            print(f"Articles related to {keyword}: ")
            for article in data:
                if keyword.lower() in article["title"].lower():
                    print(f"Article Id: {article['id']}\nTitle: {article['title']}\n{article['body']}\nArticle Written By: {article['userId']}\n\n")

        elif ifSearch in ('false', 'no', 'n', '0'):
            break

        else:
            print("Invalid Choice")

    return
    
def createFavorites(data):
    try:
        with open("favorites.json", "r") as file:
            favoriteList = json.load(file)

    except FileNotFoundError:
        favoriteList = []

    except json.JSONDecodeError:
        favoriteList = []

    while True:
        doFavorite = input("Do you want to add an article in favorite?: ").strip().lower()
        if doFavorite in ('true', 'yes', 'y', '1'):
            try:
                favoriteId = int(input("Enter the article id to make it favorite: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue
            found = False
            for article in data:
                if favoriteId == article["id"]:
                    found = True
                    if article in favoriteList:
                        print("Article already Favorites")
                    else:
                        favoriteList.append(article)
                        break
            if not found:
                    print(f"Article with {favoriteId} does not exist in favorite!")

        elif doFavorite in ('false', 'no', 'n', '0'):
            break

        else:
            print("Invalid Choice")

    print("\n")

    with open("favorites.json", "w") as file:
        json.dump(favoriteList, file, indent=4)

    viewFav()
        
    return

def delFavorite():
    try:
        with open("favorites.json", "r") as file:
            favoriteList = json.load(file)

    except FileNotFoundError:
        favoriteList = []

    except json.JSONDecodeError:
        favoriteList = []

    while True:
        doFavorite = input("Do you want to delete an article from favorite?: ").strip().lower()
        
        if doFavorite in ('true', 'yes', 'y', '1'):
            try:
                favoriteId = int(input("Enter the article id to delete it from favorite: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue
            found = False
            for index, article in enumerate(favoriteList):
                if favoriteId == article["id"]:
                        favoriteList.pop(index)
                        found = True
                        break
            if not found:
                print(f"Article with {favoriteId} does not exist!")

        elif doFavorite in ('false', 'no', 'n', '0'):
            break

        else:
            print("Invalid Choice")
        
    print("\n")
    
    with open("favorites.json", "w") as file:
        json.dump(favoriteList, file, indent=4)

    viewFav()

    return

def viewFav():
    try:
        with open("favorites.json", "r") as file:
            favoriteList = json.load(file)

    except FileNotFoundError:
        favoriteList = []

    except json.JSONDecodeError:
        favoriteList = []

    if not favoriteList:
        print("There are no Favorite articles, Add them to see here.")
    else:
        for article in favoriteList:
            print(f"Article Id: {article['id']}\nTitle: {article['title']}\n{article['body']}\nArticle Written By: {article['userId']}\n\n")
    
data = articalReader()
if data is None:
    print("Could not load articles.")
    exit()
listArticles = listAll(data)
print("\n")
searched = searchArticle(data)
print("\n")
createFavorites(data)
delFavorite()