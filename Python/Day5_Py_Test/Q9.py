# Write a journal script. It: appends a new entry (hardcode title and text for now) to `journal.txt` with a separator between entries, then reads the whole file back and prints only entries containing a word you specify, then shows total entry count.

with open("journal.txt", "w") as file:
    file.write("The Sky\n")
    file.write("The sky is bright and beautiful.\n")
    file.write("---\n")

with open("journal.txt", "a") as file:
    file.write("The Grass\n")
    file.write("The Grass is green and vibrant.\n")
    file.write("---\n")

with open("journal.txt", "a") as file:
    file.write("The Weather\n")
    file.write("It is a windy day.\n")
    file.write("---\n")


with open("journal.txt", "r") as file:
    all_lines = file.readlines()
    print(all_lines)
    print([line for line in all_lines if "The" in line])
    sumOfSep = sum("---" in line for line in all_lines)
    print(f"Total Enteries: {sumOfSep}")