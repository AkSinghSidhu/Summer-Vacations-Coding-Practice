# Convert a list of dictionaries into a CSV file using `csv.DictWriter`, then read it back using `csv.DictReader` and print each row as a dict.

import csv

students = [
    {"name": "Aarav Sharma", "age": 16, "score": 92},
    {"name": "Priya Singh", "age": 15, "score": 85},
    {"name": "Rohan Verma", "age": 17, "score": 88},
    {"name": "Neha Gupta", "age": 16, "score": 79},
    {"name": "Karan Patel", "age": 15, "score": 67},
    {"name": "Simran Kaur", "age": 17, "score": 95},
    {"name": "Arjun Mehta", "age": 16, "score": 83},
    {"name": "Ananya Roy", "age": 15, "score": 90},
    {"name": "Vikram Das", "age": 17, "score": 76},
    {"name": "Ishita Jain", "age": 16, "score": 98}
]

with open("CSV_files/Q52File.csv", "w", newline="") as file:
    fieldnames = ["name", "age", "score"]

    writer = csv.DictWriter(file, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerows(students)

with open("CSV_files/Q52File.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)