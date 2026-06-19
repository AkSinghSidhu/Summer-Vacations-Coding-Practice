# File sync simulator. Two folders (create with dummy files). Script: compares contents, lists new/deleted/changed files (by size), "syncs" by copying missing files, saves a timestamped report. Use `pathlib`, `shutil`, `datetime`, error handling.

from pathlib import Path
from datetime import datetime
import json,  shutil

def compareFolder():
    folder1 = Path("Folder1")
    folder1.mkdir(exist_ok=True)

    folder2 = Path("Folder2")
    folder2.mkdir(exist_ok=True)

    filesFold1 = {file.name for file in folder1.glob("*")}
    filesFold2 = {file.name for file in folder2.glob("*")}

    diff = filesFold1 - filesFold2
    deleted = filesFold2 - filesFold1
    common = filesFold1 & filesFold2
    changed = [f for f in common if (folder1/f).stat().st_size != (folder2/f).stat().st_size]

    logs = ("Files present in Folder 1:\n")
    for files in filesFold1:
        logs += (f"\t{files}\n")

    logs += ("\nFiles present in Folder 2:\n")
    for files in filesFold2:
        logs += (f"\t{files}\n")
    
    logs += ("\nNew Files in folder 1 and yet to be synced:\n")
    for files in diff:
        logs += (f"\t{files} : {(folder1 / files).stat().st_size} Kb\n")
    
    logs += ("\nDeleted files in folder 1:\n")
    if deleted:
        for files in deleted:
            logs += (f"\t{files} : {(folder2 / files).stat().st_size} Kb\n")
    else:
        logs += ("\tNone\n")

    logs += ("\nCommon files in folders:\n")
    if common:
        for files in common:
            logs += (f"\t{files} : {(folder1 / files).stat().st_size} Kb\n")
    else:
        logs += ("\tNone\n")

    logs += ("\nChanged files in folder 1:\n")
    if changed:
        for files in changed:
            logs += (f"\t{files} : {(folder1 / files).stat().st_size} Kb\n")
    else:
        logs += ("\tNone\n")

    if diff:
        for filename in diff:
            shutil.copy(folder1 / filename, folder2 / filename)
        print("Synced Successfully")
        logs += ("Synced Successfully")
    else:
        logs += ("\nAlready Synced")
        print("\nAlready Synced")
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    with open(f"sync_report_{timestamp}.txt", "w") as file:
        file.write(logs)

compareFolder()