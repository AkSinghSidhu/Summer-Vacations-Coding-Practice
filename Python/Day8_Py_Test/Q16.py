# Compare two folders. Print: files only in folder A, files only in folder B, files in both. For files in both, flag if sizes differ. Folder paths are hardcoded variables. `pathlib` only.

from pathlib import Path

folder = Path("Python/Day8_Py_Test/FolderComparing")
folder.mkdir(exist_ok=True)

folderA = Path("Python/Day8_Py_Test/FolderComparing/A")
folderA.mkdir(exist_ok=True)

folderB = Path("Python/Day8_Py_Test/FolderComparing/B")
folderB.mkdir(exist_ok=True)

A = set()
B = set()

for item in folderA.iterdir():
    A.add(item.name)
    print(item.name)

for item in folderB.iterdir():
    B.add(item.name)
    print(item.name)

print(A - B)
print(B - A)
filesInBoth = A & B
print(filesInBoth)

for items in filesInBoth:
    if (folderA/items).stat().st_size != (folderB/items).stat().st_size:
        print(f"{items}: SIZE DIFFERS")
    else:
        print(f"{items}: sizes match")