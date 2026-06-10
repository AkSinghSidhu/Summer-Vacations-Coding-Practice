# Script that scans a folder you pick. Prints all files with size in KB. Groups and counts files by extension. Finds the 3 largest files. Creates a `report/` subfolder if missing and writes a summary `.txt` file into it. `pathlib` only — no `os` module.

from pathlib import Path
import shutil

folder = Path("Python/Day8_Py_Test/ScannableFolder")
folder.mkdir(exist_ok=True)

rootFolder = Path("/home/aksingh001/Development/Summer Vacations/Coding-Practice")
rootFolder.mkdir(exist_ok=True)

for file in rootFolder.iterdir():
    if file.suffix == ".txt":
        shutil.copy(file, folder)

report = folder / "summary.md"
report.write_text("Monthly Report")
report1 = folder / "random.md"
report1.write_text("This file contains Random Text")

my_dict = {}
for file in folder.iterdir():
    my_dict[file.name] = file.stat().st_size
    print(f"File Size of {file.name}: {file.stat().st_size} Kb")
    

counts = {}
for file in folder.iterdir():
    ext = file.suffix
    if ext in counts:
        counts[ext] += 1
    else:
        counts[ext] = 1

print(counts)
sorted_files = sorted(my_dict.items(), key=lambda items: items[1])
largest = sorted_files[-3:]
largest.reverse()
print(largest)
summaryFolder = Path("Python/Day8_Py_Test/Summary")
summaryFolder.mkdir(exist_ok=True)

summary = summaryFolder / "summary.txt"

summaryStr = "Summary\n"
summaryStr += "\nFiles with their sizes:\n"
for key, values in my_dict.items():
    prevSummary = (f"\tFile Size of {key}: {values} Kb\n")
    summaryStr = summaryStr + prevSummary
    
summaryStr += "\nExtension Count:\n"
for ext, count in counts.items():
    summaryStr += f"\t{ext}: {count} files\n"

summaryStr += "\n3 Largest Files:\n"
for name, size in largest:
    summaryStr += f"\t{name}: {size} Kb\n"

summary.write_text(f"{summaryStr}")

