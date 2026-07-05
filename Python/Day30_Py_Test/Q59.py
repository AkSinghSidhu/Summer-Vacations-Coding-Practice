# Build a CLI "habit tracker": an OOP `Habit` class, data persisted to JSON, supports marking a habit done for today, calculating the current streak (consecutive days), and generating a text report. Combines OOP, JSON, datetime, and file I/O.

from pathlib import Path
from datetime import datetime, timedelta
import json

class Habit:
    def __init__(self, name):
        self.name = name
        self.record = []

    def loadFile(self):
        habitfolder = Path("Habits_Folder")
        habitfolder.mkdir(parents=True, exist_ok=True)
        try:
            with open("Habits_Folder/Habits.json", "r") as file:
                self.habitfile = json.load(file)
        except FileNotFoundError:
            self.habitfile = {}
        except json.JSONDecodeError:
            self.habitfile = {}

    def addHabit(self):
        self.loadFile()
        if self.name in self.habitfile:
            self.record = self.habitfile[self.name]
            if str(datetime.now().date()) in self.record:
                print("Already marked done today")
                return
            else:
                self.mark_done()
        else:
            self.habitfile.update({self.name: self.record})
            self.mark_done()

    def mark_done(self):
        while True:
            done = input("Done today's task? (y/n): ").strip().lower()
            if done in ("true", "yes", "y", "1"):
                self.record.append(str(datetime.now().date()))
                self.habitfile[self.name] = self.record
                self.save()
                break

            elif done in ("false", "no", "n", "0"):
                break

            else:
                print("Invalid input. Please enter yes or no.")

    def save(self):
        try:
            with open("Habits_Folder/Habits.json", "w") as file:
                json.dump(self.habitfile, file, indent=4)
        except OSError:
            print("Save Failed")

    def writeReport(self):
        full_report = ""
        for habit in self.habitfile:
            full_report += f"{habit}\nDates on which task done:\n"
            dates = self.habitfile[habit]
            for date in dates:
                full_report += f"\t{date}\n"
            count = 1 if dates else 0
            for i in range(len(dates) - 1, 0, -1):
                date1 = datetime.strptime(dates[i], "%Y-%m-%d").date()
                date2 = datetime.strptime(dates[i - 1], "%Y-%m-%d").date()
                if date1 - date2 == timedelta(days=1):
                    count += 1
                else:
                    break
            full_report += f"\nCurrent streak: {count}\n"
            full_report += f"Total Completions: {len(dates)}\n\n"
        try:
            with open("Habits_Folder/report.txt", "w") as file:
                file.write(full_report)
        except OSError:
            print("Save Failed")

while True:
    habit_name = input("Enter habit name: ").strip()
    if habit_name:
        break
    print("Habit name cannot be empty.")

h = Habit(habit_name)
h.addHabit()
h.writeReport()