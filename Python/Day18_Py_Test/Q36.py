# Write a context manager using the `@contextmanager` decorator from `contextlib` that prints "starting" on entry and "cleaning up" on exit, wrapping any block of code.

from contextlib import contextmanager

@contextmanager
def context_Manager():
    print("Starting")
    yield
    print("Cleaning Up")

with context_Manager():
    print("doing work")