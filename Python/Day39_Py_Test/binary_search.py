def recBinarySearch(sList, low, high, num):
    
    if high >= low:
        mid = low + (high - low) // 2
        
        if sList[mid] == num:
            return mid
        elif num < sList[mid]:
            return recBinarySearch(sList, low, mid - 1, num)
        else:
            return recBinarySearch(sList, mid + 1, high, num)
    
    else:
         return -1

if __name__ == "__main__":
    sortedList = [2, 5, 8, 12, 15, 18, 21, 25, 29, 33, 37, 41, 45, 49, 53]
    number = int(input("Enter the number to find it in list: "))
    low = 0
    high = len(sortedList) - 1
    result = recBinarySearch(sortedList, low, high, number)
    
    if result != -1:
        print(f"Number found at index: {result}")
    else:
        print("Number not found in list")