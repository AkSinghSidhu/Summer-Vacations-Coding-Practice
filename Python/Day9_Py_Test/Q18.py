# Recursively find all files in a folder modified in the last 7 days. Group them by weekday name (Mon, Tue...). Build a dict `{day: [filenames]}`. Save as a formatted report in a `logs/` folder. Use `pathlib` + `datetime`.

from pathlib import Path
from datetime import datetime, timedelta

folder = Path("Python/Day9_Py_Test/ModifiedFiles")
folder.mkdir(exist_ok = True)

dayFile = {}
compare = datetime.now() - timedelta(days=7)

for files in folder.rglob("*"):
    timestamp = files.stat().st_mtime
    date = datetime.fromtimestamp(timestamp)

    if date >= compare:
        day = date.strftime("%A")

        if day not in dayFile:
            dayFile[day] = []
        dayFile[day].append(files.name)

logFolder = Path("Python/Day9_Py_Test/logs")
logFolder.mkdir(exist_ok = True)

logs = ""
for day, logFiles in dayFile.items():
    prevLogs = f"{day}:\n" + "\n".join(f"  - {f}" for f in logFiles) + "\n\n"
    logs = logs + prevLogs


files = Path("Python/Day9_Py_Test/logs/logs.txt")
files.write_text(logs)
