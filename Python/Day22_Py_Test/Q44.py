# Use `itertools.cycle` and `itertools.islice` to print the first 10 values of a repeating pattern from a list of 3 items.

from itertools import cycle, islice

names = cycle([
    "Aarav",
    "Priya",
    "Kabir"
])

print(list(islice(names, 0, 10, 1)))