# Write a chain: read two numbers from a file → divide them → write result to another file. Each step is a separate function with its own specific exception if it fails. A `main()` function runs the whole chain, handles every failure with a unique message, and always logs "operation complete" in a finally block whether it succeeded or not.

class WriteFail:
    pass


def readFile(numberFile):
    try:
        with open(numberFile, "r") as file:
            line = int(file.readline())
            line1 = int(file.readline())
            return line,line1

    finally:
        print("Operation Complete: File Reading function was called and did ran")
    
def divideFunc(numbers):
    num1, num2= numbers
    try:
        if num2 == 0:
            raise ZeroDivisionError("Number Cannot be divided by 0")
        else:
            divNum = num1 / num2
            return divNum

    finally:
        print("Operation Complete: Divide function was called and did ran")
    

def writeFile(wriNum):
    try:
        with open("chainProblemOutput.txt", "w") as file:
            file.write(f"{wriNum}\n")

    finally:
        print("Operation Complete: File Writing function was called and did ran")

def main(file):
    try:
        reading = readFile(file)
        dividing = divideFunc(reading)
        writing = writeFile(dividing)
        
    except FileNotFoundError as e:
        print(f"Read failed: {e}")
        
    except ZeroDivisionError as e:
        print(f"Division failed: {e}")

    except WriteFail as e:
        print(f"Write failed: {e}")

    finally:
        print("Operation Complete: Main function was called and did ran")


try:
    int1 = int(input("Enter the First Number: "))
except ValueError:
    raise TypeError("Input must be a number")

try:
    int2 = int(input("Enter the Second Number: "))
except ValueError:
    raise TypeError("Input must be a number")


try:
    with open("chainProblem.txt", "w") as file:
        file.write(f"{int1}\n")
        file.write(f"{int2}")
    
except WriteFail:
    print("Numbers Failed to write in file")

finally:
    print("Operation Complete: File writing was done")

main("chainProblem.txt")