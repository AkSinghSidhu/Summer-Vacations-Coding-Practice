# Write a decorator `timer` that prints how long a function took to run. Apply it to a function that sleeps for a random duration and prints `"done"`.

from datetime import datetime
import time, random

def timer(func):
    def wrapper(*args, **kwargs):
        timestampBef = datetime.now()
        result = func(*args, **kwargs)
        timestampAft = datetime.now()
        duration = timestampAft - timestampBef
        print(f"Took {duration.total_seconds():.2f} seconds")
        return result
    return wrapper

@timer
def slowfunc():
    time.sleep(random.uniform(0.5, 2))
    print("Done")


slowfunc()