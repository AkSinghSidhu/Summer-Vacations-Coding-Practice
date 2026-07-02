# Build a generator-based data pipeline: a generator that reads lines from a file lazily, another generator that filters lines matching a regex pattern, and a final consumer that writes the matches to an output file. Chain all three together.

import re

def reader(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

def filtering(source):
    for line in source:
        match = re.search(r'^\[(ERROR|WARNING)\].*$', line)
        if match:
            yield match.group()

def consumer(source):
    with open("output.txt", "w") as file:
        for line in source:
            file.write(line + "\n")


consumer(filtering(reader("inputQ54.txt")))