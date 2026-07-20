# In one line each:

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
# Find the most common log level
# Get all unique log levels as a set (one line)