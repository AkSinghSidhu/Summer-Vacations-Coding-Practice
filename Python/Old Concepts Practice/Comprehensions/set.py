# From ["apple","banana","avocado","blueberry","apricot","cherry"] get unique first letters.

fruitsList = ["apple","banana","avocado","blueberry","apricot","cherry"]
letterSet = {letter[0] for letter in fruitsList}
print(letterSet)

# From [1,1,2,2,3,3,4,4,5,5] get unique values that are odd.

numList = [1,1,2,2,3,3,4,4,5,5]
numSet = {num for num in numList if num % 2 != 0}
print(numSet)

# From ["hello world","foo bar","hello python"] get all unique words across all strings.

stringList = ["hello world","foo bar","hello python"]
wordList = {word for words in stringList for word in words.split()}
print(wordList)