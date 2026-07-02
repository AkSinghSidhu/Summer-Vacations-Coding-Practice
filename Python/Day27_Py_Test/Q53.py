# Build a "word frequency analyzer" CLI tool: reads any text file, uses regex to clean the text, `Counter` to count frequencies, and a decorator to time the whole operation. Save results to a CSV file.

from collections import Counter
import time, re, csv

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time took to do the operations: {end - start}s")
        return result
    return wrapper

@timer
def wordFreqAnalyzer():
    with open("sample.txt", "r") as file:
        content = file.read()

    cleaned_content = [word.lower() for word in re.split(r'[^a-zA-Z0-9]+', content) if word]

    count = dict(Counter(cleaned_content))
    newList = []
    for key, value in count.items():
        new_dict = {
            "word": key,
            "count": value
        }
        newList.append(new_dict)

    with open("output.csv", "w", newline = "") as file:
        fieldnames = ["word", "count"]
        writer = csv.DictWriter(file, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(newList)


wordFreqAnalyzer()