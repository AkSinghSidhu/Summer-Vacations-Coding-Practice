from functools import reduce


def flatten_list(nested_list):
    return reduce(lambda x, y: x + y, nested_list, [])

if __name__ == "__main__":
    nested_list = [
        [1, 2, 3],
        [4, 5],
        [6, 7, 8],
        [9]
    ]

    flattenedList = flatten_list(nested_list)
    print(flattenedList)