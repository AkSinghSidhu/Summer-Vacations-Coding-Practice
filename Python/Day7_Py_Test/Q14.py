# Build a lap timer using `datetime`. Functions: `start()`, `lap()` — prints time since last lap, `stop()` — prints total time and all laps. Simulate 5 tasks with `time.sleep` and random durations between 0.5–2s. Run them through the timer. Save the timing report to a file.
import random, time, os
from datetime import datetime, timedelta

def start():
    global start_time
    start_time = datetime.now()
    return start_time

def lap():
    global last_lap_time, start_time, laps
    if last_lap_time == 0:
        lapDuration = datetime.now() - start_time
        last_lap_time = datetime.now()
    else:
        lapDuration = datetime.now() - last_lap_time
        last_lap_time = datetime.now()
    
    laps.append(lapDuration)
    return lapDuration

def stop():
    total_time = datetime.now() - start_time
    for lap in laps:
        print(f"{lap.total_seconds():.2f}s")

    return total_time
    

os.makedirs("Python/Day7_Py_Test/timer", exist_ok = True)

start_time = 0
last_lap_time = 0
laps = []

start()

for x in range(5):
    time.sleep(random.uniform(0.5, 2))
    print(lap())

print(stop())

with open("Python/Day7_Py_Test/timer/lapTimes.txt", "w")as file:
    for lap in laps:
        file.write(f"{lap.total_seconds():.2f}s\n")