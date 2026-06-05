# You have a list of 5 sentences (make them up). Using comprehensions: get all unique words across all sentences, make a dict of word → how many sentences it appears in, get all words longer than 5 letters, make a list of `(sentence, word_count)` tuples.

sentences = [
    "The sun rises in the east.",
    "Python is a powerful programming language.",
    "I enjoy learning new coding concepts.",
    "The weather is very pleasant today.",
    "Practice is the key to improvement."
]

unique = {word for sentence in sentences for word in sentence.split()}
count = {word: sum(word in sentence for sentence in sentences) for word in unique}
print([word for word in unique if len(word) > 5])
listTuple = [(x, len(x.split())) for x in sentences]

print(unique)
print(count)
print(listTuple)