def facto(n):
    if n < 0:
        raise ValueError("Factorial of Negative number does not exist!")
    elif n == 0:
        return 1 
    elif n <= 2:
        return n
    else:
        return n * facto(n - 1)

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    try:
        factorial = facto(num) # This function would call facto() function each time due to recursion.
        print(f"Factorial of {num} is: {factorial}")
    except ValueError as e:
        print(f"Caught an error: {e}")