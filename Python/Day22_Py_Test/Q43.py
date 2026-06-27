# Use `itertools.combinations` to generate all possible pairs from a list of 5 names. Print them.

from itertools import combinations

names = [
    "Aarav",
    "Priya",
    "Kabir",
    "Ananya",
    "Rohan"
]

for i in range(1,6):
    print(f"Combination with {i} number of names in each combination: ")
    for combo in combinations(names, i):
        print(combo)