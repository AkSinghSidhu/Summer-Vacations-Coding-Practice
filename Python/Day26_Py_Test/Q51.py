# Write a script that reads a CSV file of students (`name,age,score`) using the `csv` module, filters students with grade above 80, and writes them to a new CSV file.

import csv

newList = []
with open("CSV_files/read.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["score"]) > 80:
            newList.append(row)

with open ("CSV_files/write.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "score"]

    writer = csv.DictWriter(file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(newList)
