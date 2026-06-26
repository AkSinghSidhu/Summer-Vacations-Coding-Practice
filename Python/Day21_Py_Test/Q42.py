# Use `collections.defaultdict` to group a list of words by their first letter, without manually checking `if key in dict`.

from collections import defaultdict

words = [
    "apple",
    "ant",
    "banana",
    "ball",
    "cat",
    "car",
    "dog",
    "door",
    "elephant",
    "eagle",
    "fish",
    "frog"
]

defDict = defaultdict(list)

for word in words:
    key = word[0]
    defDict[key].append(word)

print(dict(defDict))