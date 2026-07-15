# From [["a","b"],["c","d"],["e","f"]] flatten into one list.

complexList = [["a","b"],["c","d"],["e","f"]]
flattendList = [word for wordsList in complexList for word in wordsList]
print(flattendList)

# From range(1,6) create a multiplication table as list of lists — [[1,2,3,4,5],[2,4,6,8,10],...].

multiplication_table = [[row * column for column in range(1, 6)] for row in range(1, 6)]
print(multiplication_table)

# From ["the quick brown fox","jumps over the lazy dog"] get all unique words longer than 3 letters.

sentenceList = ["the quick brown fox","jumps over the lazy dog"]
unique = {word for words in sentenceList for word in words.split() if len(word) > 3}
print(unique)

# From [1,2,3,4,5] create all possible pairs (a,b) where a != b.

numList = [1,2,3,4,5]
combination_pairs = [[(a,b) for b in numList if a != b] for a in numList]
print(combination_pairs)