# Using `re`, extract all phone numbers from a block of text (make up text containing 3-4 phone numbers in different formats). Use `re.findall`.

import re

text = """
For support, call 123-456-7890.
You can also reach sales at (555) 123-4567.
Our international office number is +44 20 7946 0958.
For emergencies, contact 9876543210.
+91 70825-10212
"""

numbers = r"\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}"
interNaNum = r"\+\d{1,3}[- ]\d{2}[- ]\d{4}[- ]\d{4}"
indNum = r"\+\d{2}[- ]\d{5}[- ]\d{5}"

combined = numbers + "|" + interNaNum + "|" + indNum

print(re.findall(combined, text))