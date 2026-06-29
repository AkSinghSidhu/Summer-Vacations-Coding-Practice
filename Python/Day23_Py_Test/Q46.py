# Use `functools.lru_cache` to memoize a slow recursive function (like Fibonacci). Add a comment on why repeated calls become faster.

from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
val1 = fib(999)
print(val1)
val2 = fib(1000)
print(val2)

# "val2" would be calculated significantly faster as fib(999) is already stored in cache and isnt being calculated again and is simply reusing the "val1"