# Write a recursive function to calculate factorial. Then write a recursive function to calculate the nth Fibonacci number. Compare their structure in a comment.

def facto(n):
    if n < 0:
        raise ValueError("Factorial of Negative number does not exist!")
    elif n == 0:
        return 1 
    elif n <= 2:
        return n
    else:
        return n * facto(n - 1)
    
def fib(n):
    if n < 0:
        raise ValueError("Negative Number!")
    elif n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

num = int(input("Enter a number: "))
try:
    factorial = facto(num) # This function would call facto() function each time due to recursion.
    print(f"Factorial of {num} is: {factorial}")
except ValueError as e:
    print(f"Caught an error: {e}")

try:
    fibonacci = fib(num)
    print(F"Fibonacci number of {num} position number is: {fibonacci}") # This function would call fib() function 2 times in each run due to recursion.
except ValueError as e:
    print(f"Caught an error: {e}")

# Thus the calls made by fib() would be much more than the facto() function