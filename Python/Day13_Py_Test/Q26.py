# Write `robust_get(url, retries=3)` with exponential backoff between retries. Use it to fetch `https://jsonplaceholder.typicode.com/todos`. Filter incomplete todos. Save each user's incomplete todos to a separate file: `todos/user_{id}.json`. Create the folder if needed.

from pathlib import Path
import requests, json, time

pending = Path("todos")
pending.mkdir(exist_ok=True)

def robust_get(url, retries = 3):
    session = requests.Session()

    for attempts in range(retries):
        try:
            requestTodos = session.get(url, timeout=5)
            requestTodos.raise_for_status()
            todoData = requestTodos.json()
            return writeTodos(todoData)

        except requests.RequestException:
            wait = 2 ** (attempts + 1)
            print(wait)
            time.sleep(wait)
    raise Exception("All retries failed")
    
def writeTodos(todoData):
    for uid in range(1, 11):
        userTodos = [t for t in todoData if t["userId"] == uid and not t["completed"]]
        with open(f"todos/user_{uid}.json", "w") as file:
            json.dump(userTodos, file, indent=4)

    return

robust_get("https://jsonplaceholder.typicode.com/todos")