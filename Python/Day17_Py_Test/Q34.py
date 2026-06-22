# Write a decorator `log_call` that prints the function name and its arguments every time it's called. Apply it to 2 different functions with different argument types.

from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logNameArg = (f"Called {func.__name__} with arguments: {args}")
        print(logNameArg)
        print(f"{result}")
        return result
    return wrapper

@log_call
def add_num(a, b):
    return a + b

@log_call
def greet(name):
    return (f"Hi {name}")

add_num(7, 3)
greet("Akash")