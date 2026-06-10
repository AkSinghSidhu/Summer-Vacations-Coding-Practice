import os
from datetime import datetime, timedelta
from pathlib import Path

folder = Path("Python/Day9_Py_Test/ModifiedFiles")
folder.mkdir(exist_ok=True)

files = [
    ("notes.txt", 0),
    ("script.py", 0),
    ("app.js", 1),
    ("readme.md", 1),
    ("data.csv", 2),
    ("config.txt", 2),
    ("test.py", 3),
    ("index.html", 3),
    ("styles.css", 4),
    ("report.txt", 5),
]

for filename, days_ago in files:
    f = folder / filename
    f.write_text("dummy")
    mod_time = (datetime.now() - timedelta(days=days_ago)).timestamp()
    os.utime(f, (mod_time, mod_time))