# From ["a","b","c","d"] create {"a":1, "b":2, "c":3, "d":4} where value is position+1.

letterslist = ["a","b","c","d"]
positionList = {letter: letterslist.index(letter) + 1 for letter in letterslist}
print(positionList)

# From {"name":"Akash","age":22,"city":"Delhi"} create a new dict with all keys in uppercase.

info = {"name":"Akash","age":22,"city":"Delhi"}
upperKeys = {k.upper(): v for k, v in info.items()}
print(upperKeys)

# From [("apple",3),("banana",5),("cherry",2)] create a dict of fruit→count.

fruitCountList = [("apple",3),("banana",5),("cherry",2)]
fruitCountDict = {fruit: count for fruit, count in fruitCountList}
print(fruitCountDict)

# From range(1,6) create {1:"odd", 2:"even", 3:"odd",...}.

oddEven = {num:("even" if num % 2 == 0 else "odd") for num in range(1,6)}
print(oddEven)

# From {"a":1,"b":2,"c":3,"d":4,"e":5} keep only key-value pairs where value is greater than 2.

numDict = {"a":1,"b":2,"c":3,"d":4,"e":5}
greaterThan = {key: val for key, val in numDict.items() if val > 2}
print(greaterThan)