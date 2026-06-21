# Write a generator function `even_numbers(limit)` that yields even numbers up to `limit`. Then write a generator expression that does the same thing in one line. Add a comment explaining why generators don't hold the whole sequence in memory at once.

def even_numbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
            yield i


lim = int(input("Enter the ceiling number between which you want to print even numbers: "))
even = (x for x in range(lim + 1) if x % 2 == 0)

print("Even numbers using generator function: ")
for num in even_numbers(lim):
    print(num)

print("Even numbers using generator expression: ")
for num in even:
    print(num)


# Why generators don't hold the whole sequence in memory at once: Because they literally pause the execution between each value as they use yield which stops after "returning" a value and continues again when either looped over or next is used. So generators basically provide the result on demand.