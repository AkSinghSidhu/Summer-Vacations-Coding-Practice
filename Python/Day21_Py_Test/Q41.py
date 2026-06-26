# Use `collections.Counter` to count word frequency in any paragraph of text. Print the 3 most common words using `.most_common()`.

from collections import Counter
import re

para = """
During the weekend, a group of students visited a science museum to learn about space, robotics, and renewable energy. The museum guide explained how robots are used in modern industries and how renewable energy can help reduce pollution. After the tour, the students discussed their favorite exhibits while enjoying lunch together. Everyone agreed that the museum was both educational and enjoyable, and many students said they would like to visit the museum again with their families. The experience inspired the students to learn more about science and technology.
"""

cleanedPara = re.findall(r'[a-zA-Z0-9]+', para)
count = Counter(cleanedPara)
print(count.most_common(3))