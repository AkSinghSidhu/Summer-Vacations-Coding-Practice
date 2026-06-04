# You have `numbers = [1, 4, 9, 16, 25]`. Using only lambdas with built-in `map()` and `filter()` (no comprehensions, no loops): get the square root of each number, then keep only results greater than 3. Chain both into one expression.

numbers = [1, 4, 9, 16, 25]

square_root = filter(lambda x : x > 3, map(lambda x : x ** 0.5, numbers))
print(list(square_root))