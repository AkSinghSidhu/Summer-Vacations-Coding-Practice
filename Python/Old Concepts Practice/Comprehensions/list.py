# From [1,2,3,4,5,6,7,8,9,10] get all numbers divisible by 3.

num_List = [1,2,3,4,5,6,7,8,9,10]
result = [x for x in num_List if x % 3 ==0]
print(result)

# From ["apple","banana","cherry","date","elderberry"] get words longer than 5 letters.

fruit_list = ["apple","banana","cherry","date","elderberry"]
longWords = [fruit for fruit in fruit_list if len(fruit) > 5]
print(longWords)

# From [1,2,3,4,5] get the square of each number.

toSquareList = [1,2,3,4,5]
squaredList = [num **2 for num in toSquareList]
print(squaredList)

# From ["hello","world","python","code"] get each word in uppercase.

wordList = ["hello","world","python","code"]
upperCaseList = [word.upper() for word in wordList]
print(upperCaseList)

# From [-3,-2,-1,0,1,2,3] get only positive numbers.

integerList = [-3,-2,-1,0,1,2,3]
positiveNumList = [num for num in integerList if num >= 0]
print(positiveNumList)

# From [1,2,3,4,5,6,7,8,9,10] get even numbers doubled.

intList = [1,2,3,4,5,6,7,8,9,10]
evenDoubledList = [num * 2 for num in intList if num % 2 == 0]
print(evenDoubledList)

# From ["  hello  ","  world  ","  python  "] get each word stripped of whitespace.

uncleanWordList = ["  hello  ","  world  ","  python  "]
cleanedList = [word.strip() for word in uncleanWordList]
print(cleanedList)

# From [1,2,3,4,5] get strings like "item_1", "item_2", etc.

numList = [1,2,3,4,5]
itemString = [(f"item_{num}") for num in numList]
print(itemString)

# From ["cat","dog","elephant","ox","ant"] get words that start with a vowel.

species = ["cat","dog","elephant","ox","ant"]
vowelWordList = [word for word in species if word.startswith(("a", "e", "i", "o", "u"))]
print(vowelWordList)

# From range(1,21) get numbers that are neither divisible by 2 nor by 3.

notDiv = [num for num in range(1,21) if num % 2 != 0 and num % 3 != 0]
print(notDiv)