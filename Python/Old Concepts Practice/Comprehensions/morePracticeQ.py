orders = [
    {"item": "laptop", "qty": 2, "price": 45000},
    {"item": "mouse", "qty": 5, "price": 800},
    {"item": "keyboard", "qty": 3, "price": 2500},
    {"item": "monitor", "qty": 1, "price": 18000},
]

#   Get total value of each order (qty × price) as a dict {"laptop": 90000, ...}
total_price = {item["item"]: item["price"] * item["qty"] for item in orders}
print(total_price)


#   Find the order with highest total value
highest_priced = max(total_price, key = lambda price: total_price[price])
print(highest_priced)

#   Get items where total value exceeds 10000
expensive_items = {k for k, v in total_price.items() if v > 10000}
print(expensive_items)

#---------------------------------------------------------------

company = {
    "name": "TechCorp",
    "departments": {
        "engineering": {"head": "Akash", "size": 12},
        "design": {"head": "Priya", "size": 5},
        "marketing": {"head": "Ravi", "size": 8}
    }
}

# Print the head of engineering
print(company["departments"]["engineering"]["head"])

# Print all department names where size > 6
print([name for name in company["departments"] if company["departments"][name]["size"] > 6])

# Build a dict of {dept_name: head} for all departments
head_dept = {dept_name: dept_info["head"] for dept_name, dept_info in company["departments"].items()}
print(head_dept)

#---------------------------------------------------------------

logs = ["ERROR", "INFO", "ERROR", "WARNING", "INFO", "ERROR", "INFO", "INFO", "WARNING"]

# Count each log level (no Counter)
count = {level: logs.count(level) for level in set(logs)}
print(count)

# Find the most common log level
most_common = max(count, key = lambda k: count[k])
print(most_common)

# Get all unique log levels as a set (one line)
unique_log = {log for log in logs}
print(unique_log)


#---------------------------------------------------------------

#  1. Given "the quick brown fox jumps over the lazy dog" — build a dict of {word: length} for every word. Then find the longest word using max() with a key.
sen_arr = "the quick brown fox jumps over the lazy dog".split()
word_len_dict = {word: len(word) for word in sen_arr}
print(word_len_dict)
longest_word = max(word_len_dict, key = lambda length: word_len_dict[length])
print(longest_word)


#  2. Given a list of temperatures in Celsius [0, 20, 37, 100, -10, 25] — convert all to Fahrenheit in one comprehension. Also filter only temperatures above 50°F in the same step.
temp_celsius = [0, 20, 37, 100, -10, 25]
temp_fehrn = [(c * (9/5) + 32) for c in temp_celsius]
temps_filtered = [c for c in temp_fehrn if c > 50]
print(temp_fehrn)
print(temps_filtered)

## or if both in 1 go then:
temp_fehrn_filtered = [(c * (9/5) + 32) for c in temp_celsius if (c * (9/5) + 32) > 50]
print(temp_fehrn_filtered)

#  3. Given {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30} — get months with exactly 31 days as a list. Then build a new dict with month names capitalized.
months_dict = {"january": 31, "february": 28, "march": 31, "april": 30, "may": 31, "june": 30}
months_31day = [k for k, v in months_dict.items() if v == 31]
print(months_31day)
capital_months = {k.capitalize(): v for k, v in months_dict.items()}
print(capital_months)

#  4. Given a list of strings ["hello123", "world", "python3", "code", "test99"] — separate into two lists: ones containing digits and ones that don't. Use any() with a generator inside a comprehension.
word_list = ["hello123", "world", "python3", "code", "test99"]
with_digits = [word for word in word_list if any(char.isdigit() for char in word)]
print(with_digits)
without_digits = [word for word in word_list if not any(char.isdigit() for char in word)]
print(without_digits)

#  5. Given [1, 2, 3, 4, 5] — build a dict where each number maps to a list of its multiples up to 5x. Like {1: [1,2,3,4,5], 2: [2,4,6,8,10], ...}.
num_list = [1, 2, 3, 4, 5]
table_dict = {num: list(map(lambda number: number * num, num_list)) for num in num_list}
print(table_dict)

#  6. Given a paragraph of text (make one up, at least 30 words) — find all words that appear more than once. Return them as a set.
para = "Artificial intelligence is transforming the way people work, learn, and create. From helping designers generate ideas to assisting programmers in solving complex problems, modern technology continues to open new possibilities and improve everyday experiences."

words_list = [item.strip(",.") for item in para.split()]
unique_words = set(words_list)
recurring_words = {word for word in unique_words if words_list.count(word) > 1}
print(recurring_words)

# 7. Given {"fruits": ["apple", "banana", "mango"], "veggies": ["carrot", "spinach"], "grains": ["rice", "wheat", "oats"]} — flatten all items into one list. Then count total items per category as a separate dict.
groceries_dict = {"fruits": ["apple", "banana", "mango"], "veggies": ["carrot", "spinach"], "grains": ["rice", "wheat", "oats"]}
items_list = [item for category in groceries_dict.values() for item in category]
print(items_list)
count_item = {item_type: len(items) for item_type, items in groceries_dict.items()}
print(count_item)

# 8. Given a list of dicts [{"name": "Akash", "skills": ["Python", "Flask"]}, {"name": "Priya", "skills": ["React", "Python", "CSS"]}] — find all unique skills across everyone. Then find who has the most skills.
student_skills = [{"name": "Akash", "skills": ["Python", "Flask"]}, {"name": "Priya", "skills": ["React", "Python", "CSS"]}]
unique_skills = {skill for student in student_skills for skill in student["skills"]}
print(unique_skills)

# 9. Given [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5] — without using Counter or set(), find duplicate numbers (appear more than once) using only a dict.
number_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
count_dict = {}
for num in number_list:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

recurring_num = {num: counter for num, counter in count_dict.items() if counter > 1}
print(recurring_num)

# 10. Given a string "aabbccddee" — count each character's frequency and return only characters that appear exactly twice.
abcde_string = "aabbccddee"
unique_letter = set(abcde_string)
double_letters = {letter for letter in unique_letter if abcde_string.count(letter) == 2}
print(double_letters)

    # or more optimised version:

frequency_dict = {}
for letter in abcde_string:
    if letter in frequency_dict:
        frequency_dict[letter] += 1
    else:
        frequency_dict[letter] = 1
double_dict = {letter for letter in frequency_dict if frequency_dict[letter] == 2}
print(double_dict)

# 11. Given [{"product": "laptop", "sold": 5}, {"product": "mouse", "sold": 20}, {"product": "keyboard", "sold": 8}] — calculate total units sold, find best seller, and sort by sold descending. Three separate operations.
from functools import reduce
products = [{"product": "laptop", "sold": 5}, {"product": "mouse", "sold": 20}, {"product": "keyboard", "sold": 8}]
sorted_by_sale = sorted(products, key = lambda unit: unit["sold"], reverse = True)
print(sorted_by_sale)
best_seller = sorted_by_sale[0]["product"]
print(best_seller)
total_sale = reduce(lambda acc, curr: acc + curr["sold"], sorted_by_sale, 0)
print(total_sale)

# 12. Given two lists ["a", "b", "c", "d"] and [1, 2, 3, 4] — zip them into a dict. Then swap keys and values. Both in one line each.
letter_list = ["a", "b", "c", "d"]
digit_list = [1, 2, 3, 4]
zipped_dict = dict(zip(letter_list, digit_list))
print(zipped_dict)
reversed_zipped_dict = dict(zip(digit_list, letter_list))
print(reversed_zipped_dict)

# 13. Given {"name": "Akash", "age": 22, "city": "Delhi", "score": 88, "active": True} — split into two dicts: one with string values only, one with non-string values only.
main_dict = {"name": "Akash", "age": 22, "city": "Delhi", "score": 88, "active": True}
string_val_dict = {key: val for key, val in main_dict.items() if isinstance(val, str)}
non_string_dict = {key: val for key, val in main_dict.items() if not isinstance(val, str)}
print(string_val_dict)
print(non_string_dict)

# 14. Given [[1,2,3],[4,5,6],[7,8,9]] — get the diagonal elements [1,5,9] using enumerate() in a comprehension.
nums_list = [[1,2,3],[4,5,6],[7,8,9]]
diagonal_nums = [row[idx] for idx, row in enumerate(nums_list)]
print(diagonal_nums)

# 15. Given a list of words ["python", "java", "javascript", "ruby", "go", "rust", "swift"] — group by first letter into a dict {"p": ["python"], "j": ["java", "javascript"], ...} using defaultdict or the manual pattern.
from collections import defaultdict
lang_list = ["python", "java", "javascript", "ruby", "go", "rust", "swift"]
letter_dict = defaultdict(list)
for lang in lang_list:
    first_letter = lang[0]
    letter_dict[first_letter].append(lang)

print(dict(letter_dict))

#---------------------------------------------------------------
from functools import reduce
# 1. Given this dict of student grades:
students = {
    "Akash": [88, 92, 75, 60, 95],
    "Priya": [70, 85, 90, 78, 82],
    "Ravi": [55, 60, 45, 70, 65],
    "Neha": [95, 98, 92, 88, 97]
}
# Calculate average score for each student as a new dict
avg_score = {name: reduce(lambda x, y: x + y, marks) / len(marks) for name, marks in students.items()}
print(avg_score)

# Find the student with highest average
highest_avg = max(avg_score, key = lambda name: avg_score[name])
print(highest_avg)

# Get students who are passing (average >= 70) as a list of names
passing_students = [name for name in avg_score if avg_score[name] >= 70]
print(passing_students)

# 2. Given:
inventory = [
    {"item": "apple", "category": "fruit", "qty": 50},
    {"item": "carrot", "category": "vegetable", "qty": 30},
    {"item": "banana", "category": "fruit", "qty": 20},
    {"item": "spinach", "category": "vegetable", "qty": 15},
    {"item": "mango", "category": "fruit", "qty": 40},
]
# Find total quantity per category
total_qty = {}
for item in inventory:
    item_cat = item["category"]
    if item_cat in total_qty:
        total_qty[item_cat] += item["qty"]
    else:
        total_qty[item_cat] = item["qty"]

print(total_qty)

# Group items by category into {"fruit": [...], "vegetable": [...]}
item_category = defaultdict(list)
for item in inventory:
    item_cat = item["category"]
    item_category[item_cat].append(item["item"])

print(dict(item_category))

# Find the item with lowest quantity in each category
lowest = {}
for item in inventory:
    item_cat = item["category"]
    if item_cat not in lowest:
        lowest[item_cat] = item
    elif item["qty"] < lowest[item_cat]["qty"]:
        lowest[item_cat] = item

print(lowest)

#3. Given a string "Programming is fun and programming makes you think. Fun problems make better programmers." — do all of this:
sentence = "Programming is fun and programming makes you think. Fun problems make better programmers."

# Count frequency of each word (case-insensitive, strip punctuation)
words = [word.strip(",.").lower() for word in sentence.split()]
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print(frequency)

# Find words that appear exactly once
unique_word = {word for word, count in frequency.items() if count == 1}
print(unique_word)

# Find the top 3 most frequent words
top_three = dict(sorted(frequency.items(), key = lambda word: word[1], reverse = True)[:3])
print(top_three)

# Build a dict of {word: "common"} if it appears more than once, {word: "rare"} if exactly once
common_word = {word: ("common" if count > 1 else "rare") for word, count in frequency.items()}
print(common_word)

# 4. Given:
employees = [
    {"name": "Akash", "dept": "Engineering", "salary": 85000},
    {"name": "Priya", "dept": "Design", "salary": 72000},
    {"name": "Ravi", "dept": "Engineering", "salary": 91000},
    {"name": "Neha", "dept": "Marketing", "salary": 68000},
    {"name": "Arjun", "dept": "Design", "salary": 78000},
    {"name": "Simran", "dept": "Engineering", "salary": 95000},
    {"name": "Karan", "dept": "Marketing", "salary": 71000},
]

# Find average salary per department
dept_salary = defaultdict(int)
dept_count = defaultdict(int)

for employee in employees:
    dept = employee["dept"]
    dept_salary[dept] += employee["salary"]
    dept_count[dept] += 1

avg_salary = {
    dept: dept_salary[dept] / dept_count[dept]
    for dept in dept_salary
}

print(avg_salary)

# Find the highest paid employee in each department
# Find the highest paid employee in each department
top_earner = {}

for employee in employees:
    dept = employee["dept"]

    if dept not in top_earner or employee["salary"] >= top_earner[dept]["salary"]:
        top_earner[dept] = {
            "name": employee["name"],
            "salary": employee["salary"]
        }

print(top_earner)

# Find departments where average salary exceeds 75000
rich_dept = [dept for dept, salary in avg_salary.items() if salary > 75000]
print(rich_dept)

# Sort employees by salary descending and print names only
