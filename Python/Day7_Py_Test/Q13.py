# Write a weekly schedule generator. Use `random` to assign topics from a list to daily time slots, use `datetime` to label each day starting from today, use `os` to create a `schedules/` folder if it doesn't exist, and save the schedule as a `.txt` file named with today's date. Also print it to the console.
import random, os
from datetime import datetime, timedelta

toDoList = ["JavaScript", "Python", "DSA", "Flask", "Node.js"]
timeSlots = ["Morning", "Afternoon", "Evening"]
days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

os.makedirs("Python/Day7_Py_Test/schedules", exist_ok = True)
today = datetime.today()
print("Week's Schedule:")

schedule = ""
for x in range(7):
    date = today + timedelta(days = x)
    day = days[x]
    prevSchedule = (f"{day} {date.strftime('%Y-%m-%d')}\n\t{timeSlots[0]}: {random.choice(toDoList)}\n\t{timeSlots[1]}: {random.choice(toDoList)}\n\t{timeSlots[2]}: {random.choice(toDoList)}\n\n")
    schedule =  schedule + prevSchedule
    
with open(f"Python/Day7_Py_Test/schedules/{today.strftime('%Y-%m-%d')}.txt", "w") as file:
        file.write(f"{schedule}")
    
with open(f"Python/Day7_Py_Test/schedules/{today.strftime('%Y-%m-%d')}.txt", "r") as file:
    read = file.readlines()
    print(''.join(read))