# Use `functools.reduce` to find the product of all numbers in a list, and separately to flatten a list of lists into one list.

from functools import reduce

# part 1
numbers = [2, 3, 4, 5, 6]
product = reduce(lambda x, y : x * y, numbers)
print(product)


# part 2
nested_list = [
    [1, 2, 3],
    [4, 5],
    [6, 7, 8],
    [9]
]

flattenedList = reduce(lambda x, y : x + y, nested_list)
print(flattenedList)