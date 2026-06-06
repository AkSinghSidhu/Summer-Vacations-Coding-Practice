# You have a file `students.txt` with lines like `"Akash,22,Delhi"` (create it, 6 lines + header). Read it, skip the header, build a list of dicts, filter people above age 20, and write results to `filtered.txt` in the same format with a header. No `csv` module — raw file I/O only.

with open("students.txt", "w") as file:
    file.write("Students Data\n")
    file.write("Akash,22,Delhi\n")
    file.write("Supan,20,Bathinda\n")
    file.write("Diljeet,21,Talwandi\n")
    file.write("Gurinder,22,Jodhpur\n")
    file.write("Parshant,19,Mansa\n")
    file.write("Harpreet,22,Maur\n")

with open("students.txt", "r") as file:
    all_lines = file.readlines()
    remove = all_lines.pop(0)
    print(all_lines)

with open("students.txt", "r") as file:
    new_list = file.readlines()
    del new_list[1:len(new_list)]
    print(new_list)

    for line in all_lines:
        name, age, city = line.strip().split(",")
        myDict = {"Name": name,"Age": int(age),"City": city}
        new_list.append(myDict)

    print(new_list)

    passed = list(filter(lambda x: x["Age"] > 20, new_list[1:]))
    print(passed)

with open("filtered.txt", "w") as file:
    file.write("Students Data\n")
    for student in passed:
        file.write(f"{student['Name']},{student['Age']},{student['City']}\n")
