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
print(month)
print(random.choice(eventNames))

eventSchedule = []

for x in range(15):
    event = {}
    event[random.choice(eventNames)] = (today + timedelta(days = random.randint(1, 30)))
    eventSchedule.append(event)


sortedList = sorted(eventSchedule, key=lambda x: list(x.values())[0])

for event in sortedList:
    key = list(event.keys())[0]
    event[key] = event[key].strftime("%d-%m-%Y %H:%M")

for event in sortedList:
    if today == 

print(eventSchedule)
print(len(eventSchedule))
print(sortedList)