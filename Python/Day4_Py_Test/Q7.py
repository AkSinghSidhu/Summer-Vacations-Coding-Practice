# Given a list of numbers 1–20, using only comprehensions (one per task): get all odd numbers, get squares of even numbers, make a dict mapping each number to `"odd"` or `"even"`, make a set of all numbers divisible by 3 or 5.

myList = list(range(1,21))

print(list(filter(lambda x: x % 2 != 0, myList)))
#or
print([x for x in myList if x % 2 != 0])
print([x ** 2 for x in myList if x % 2 == 0])
print({x: "even" if x % 2 == 0 else "odd" for x in myList})
print({x for x in myList if x % 3 == 0 or x % 5 == 0})