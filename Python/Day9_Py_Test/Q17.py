# Script that recursively finds all `.txt` files in a folder. Renames each by prefixing today's date: `2026-06-07_filename.txt`. Moves them into `archive/texts/` (create if missing). Skips files that already have a date prefix. Logs every action. `pathlib` only.

from pathlib import Path
from datetime import datetime

folder = Path("Python/Day9_Py_Test/TextFiles")
folder.mkdir(exist_ok = True)

for x in range(6):
    files = Path(f"Python/Day9_Py_Test/TextFiles/{x}.txt")
    files.write_text("")

timestamp = files.stat().st_mtime
date = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

for files in folder.rglob("*.txt"):
    print(files.name)

for files in folder.rglob("*.txt"):
    print(f"Current File Name: {files.name}")
    if files.name.startswith(date):
        print("No need to Rename")
    else:
        renamedFiles = files.rename(f"Python/Day9_Py_Test/TextFiles/{date}_{files.name}")
        print(f"Renamed File Name: {renamedFiles}")

archiveText = Path(f"Python/Day9_Py_Test/archive/texts")
archiveText.mkdir(parents = True, exist_ok = True)

for files in folder.rglob("*.txt"):
    movedFiles = files.rename(f"Python/Day9_Py_Test/archive/texts/{files.name}")
    print(f"Moved Files using Rename: {movedFiles}")
     