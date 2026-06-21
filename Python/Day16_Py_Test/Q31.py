# Write a generator function `countdown(n)` that yields numbers from `n` down to 1, then yields `"Liftoff!"`. Loop over it and print each value.

def countdown(n):
    for i in range(n, 0, -1):
        yield i
    yield "Liftoff!"

number = int(input("Enter the Countdown limit: "))
for num in countdown(number):
    print(num)