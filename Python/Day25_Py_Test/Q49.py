# Write a recursive function to calculate the sum of digits of a number, and another recursive function to reverse a string.

def sumDigit(num, sum):
    initialNums = num // 10
    lastNum = num % 10
    sum += lastNum

    if initialNums > 0:
        sum = sumDigit(initialNums, sum)
    
    return sum

def reverseString(inputString, revString):
    
    if inputString:
        lastLetter = inputString[-1]
        inputString = inputString[:-1]
        revString = reverseString(inputString, revString)
        revString = lastLetter + revString
        
    return revString


number = int(input("Enter the number to find sum of its digits: "))
total = 0
print(f"Sum of digits of {number}: {sumDigit(number, total)}")

inputStr = input("Enter the string you want to reverse: ")
reversedStr = ""
print(f"Reversed String: {reverseString(inputStr, reversedStr)}")