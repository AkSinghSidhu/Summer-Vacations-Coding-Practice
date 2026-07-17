# Given {"name": "Akash", "age": 22, "city": "Delhi"} — print the city. Then try accessing a key "phone" that doesn't exist using .get() with a default of "Not provided".

info = {"name": "Akash", "age": 22, "city": "Delhi"}
print(info["city"])
print(info.get("phone", "Not Provided"))

# Given {"scores": [88, 92, 75, 60, 95]} — print the highest score from the list inside the dict.

scoresDict = {"scores": [88, 92, 75, 60, 95]}
print(max(scoresDict["scores"]))

# Given {"user": {"name": "Akash", "address": {"city": "Delhi", "pin": 110001}}} — access and print the pin code.

userInfo = {"user": {"name": "Akash", "address": {"city": "Delhi", "pin": 110001}}}
pinCode = userInfo["user"]["address"]["pin"]
print(pinCode)

# Given {"name": "Akash", "age": 22} — add a "city" key, update "age" to 23, delete "name". Print the final dict.

myInfo = {"name": "Akash", "age": 22}
myInfo.update({"city": "Sirsa"})
print(myInfo)

# Given two dicts {"a": 1, "b": 2} and {"b": 3, "c": 4} — merge them so the second dict's values win on conflicts. Do it two ways: using update() and using {**d1, **d2}.

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print({**dict1, **dict2})
dict1.update(dict2)
print(dict1)

# Given {"math": 88, "physics": 72, "chemistry": 91, "english": 65} — print only subjects where score is above 75.

subjectScores = {"math": 88, "physics": 72, "chemistry": 91, "english": 65}
for key, val in subjectScores.items():
    if val > 75:
        print({key: val})

filteredScores = {k: v for k, v in subjectScores.items() if v > 75}
print(filteredScores)

# Same dict — print each subject and score formatted as "Math: 88" (capitalize the key).

print({k.capitalize(): v for k, v in subjectScores.items()})

# Given {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5} — build a new dict with keys and values swapped.

tobeswapped = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
swappedDict = {v: k for k, v in tobeswapped.items()}
print(swappedDict)

# Given a list of 5 student dicts {"name", "age", "score"} — find the student with highest score using max() with a key.

students = [
    {"name": "Alice", "age": 20, "score": 91},
    {"name": "Bob", "age": 19, "score": 84},
    {"name": "Charlie", "age": 21, "score": 76},
    {"name": "Diana", "age": 20, "score": 95},
    {"name": "Ethan", "age": 22, "score": 88},
]

print(max(students, key = lambda students: students["score"]))

# Same list — filter only students above age 20.

filteredAge = [student for student in students if student["age"] > 20]
print(filteredAge)

# Same list — get just the names as a list.

namesList = [student["name"] for student in students]
print(namesList)

# Same list — find one specific student by name using next(). Handle the case where name doesn't exist.

search = next((student for student in students if student["name"] == "Charlie"), "No Match Found!")
print(search)

# Same list — find the index of a specific student by name using enumerate() and next().

searchIdx = next((index for index, student in enumerate(students) if student["name"] == "Charlie"), "No Match Found!")
print(searchIdx)

# Same list — sort by score descending.

sortedScores = [sorted(students, key = lambda students: students["score"], reverse = True)]
print(sortedScores)

# Same list — group into {"passed": [...], "failed": [...]} where pass is score >= 50.

passFailDict = {}

# Given ["apple", "banana", "apple", "cherry", "banana", "apple"] — count occurrences of each fruit using a dict (no Counter).
# Given a list of student dicts — count how many students are in each city.
# Given ["cat", "dog", "cat", "bird", "dog", "dog"] — find the most frequent animal without using Counter.
# Given [{"name": "Akash", "subjects": ["Math", "Physics"]}, {"name": "Priya", "subjects": ["English", "Chemistry", "Math"]}] — get all unique subjects across all students.
# Same data — find which student has the most subjects.