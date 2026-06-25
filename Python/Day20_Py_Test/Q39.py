# Write a decorator `retry(times=3)` that retries a function if it raises an exception, up to `times` attempts, with a short delay between attempts.

import time,random

def retry(times = 3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                   last_exception = e
                   print(f"Attempt {attempt+1} failed: {e}")
                   time.sleep(1)
            raise last_exception
        return wrapper
    return decorator

@retry(times=3)
def slowfunc():
    time.sleep(random.uniform(0.5, 2))
    print("Done")
