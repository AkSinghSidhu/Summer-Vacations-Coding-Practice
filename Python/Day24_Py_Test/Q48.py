# Write a recursive function that flattens an arbitrarily nested list (e.g. `[1, [2, [3, 4], 5], 6]`) into a single flat list.

def flatten(lst,newlist):
    for item in lst:
        if isinstance(item, int):
            newlist.append(item)
        elif isinstance(item, list):
            flatten(item, newlist)
        else:
            print("Error")
    return newlist

nestedList = [1, [2, [3, 4], 5], 6]
new = []
print(flatten(nestedList, new))