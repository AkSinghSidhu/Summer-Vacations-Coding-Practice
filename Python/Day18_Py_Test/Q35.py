# Write a custom context manager class `Timer` using `__enter__` and `__exit__` that times a block of code and prints the duration when the block exits.

from datetime import datetime
import time, random

class Timer:
    def __enter__(self):
        self.timestampBef = datetime.now()
        return self

    def __exit__(self, exc_type, exc, tb):
        timestampAft = datetime.now()
        timediff = timestampAft - self.timestampBef
        print(f"Took {timediff.total_seconds():.2f} seconds")

with Timer():
    time.sleep(random.uniform(0.5, 2))
    print("Done")