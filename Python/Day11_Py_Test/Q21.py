# Generate 15 random events, each with a random datetime in the next 30 days and a random name from a list you define. Sort chronologically. Print: events today, this week, days until each future event. Find the average gap between consecutive events. Flag events less than 3 hours apart as conflicts.

import random
from datetime import datetime, timedelta

eventNames = [
    "Team Meeting",
    "Doctor Appointment",
    "Project Deadline",
    "Birthday Party",
    "Movie Night",
    "Gym Session",
    "Client Call",
    "Lunch with Friends",
    "Shopping Trip",
    "Study Session",
    "Job Interview",
    "Conference",
    "Workshop",
    "Game Tournament",
    "Family Dinner",
    "Road Trip",
    "Music Concert",
    "Coding Challenge",
    "Book Club",
    "Coffee Meetup"
]

today = datetime.now()
month = today + timedelta(days = 30)
week = today + timedelta(days = 7)

eventSchedule = []

for x in range(15):
    event = {}
    event[random.choice(eventNames)] = (today + timedelta(days = random.randint(0, 30)))
    eventSchedule.append(event)


sortedList = sorted(eventSchedule, key=lambda x: list(x.values())[0])


print("Events today: ")
noEventToday = True
for event in sortedList:
    key = list(event.keys())[0]
    if event[key].date() == today.date():
        print(f'{key}: {event[key].strftime("%d-%m-%Y %H:%M")}')
        noEventToday = False

if noEventToday == True:
    print("No Events Today")
print("\n")

print("Events this week: ")
noEventWeek = True
for event in sortedList:
    key = list(event.keys())[0]
    if today <= event[key] <= week:
        print(f'{key}: {event[key].strftime("%d-%m-%Y %H:%M")}')
        noEventWeek = False

if noEventWeek == True:
    print("No Events this Week")
print("\n")

for event in sortedList:
    key = list(event.keys())[0]
    print(f"Days Remaining till {key} : {(event[key] - today).days} days")

print("\n")

prevDictKey = None
totalGap = timedelta(0)
gaps = []
for index, event in enumerate(sortedList):
    key = list(event.keys())[0]
    
    current = event[key]

    if prevDictKey is not None:
        gap = current - prevDictKey
        totalGap += gap
        gaps.append(gap)
        print(f"The Gap between Task {index + 1} and {index} is: {gap}")
        if gap < timedelta(hours=3):
            print(f"Conflicts between Task {index + 1} and {index}")

    prevDictKey = current

if len(gaps) > 0:
    averageGap = totalGap / len(gaps)
else:
    averageGap = timedelta(0)

print("\n")

print(f"Average Gap between Events: {averageGap}")