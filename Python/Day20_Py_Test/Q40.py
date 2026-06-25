# Write a function using regex to clean a list of messy strings (extra whitespace, non-alphanumeric characters) using comprehensions + `re.sub`.

import re

def strCleaner(lst):
    return [re.sub(r'[^a-zA-Z0-9]+', ' ', s).strip() for s in lst]

messy_strings = [
    "  hello world  ",
    "\tpython\t",
    "\nnew\nline\n",
    "!!!hello!!!",
    "@@@test###",
    "  spaced    out  ",
    "foo-bar-baz",
    "user@example.com",
    "123-45-6789",
    "$$$money$$$",
    "  mixed_CASE123  ",
    "___underscores___",
    "***important***",
    "hello, world!",
    "  (parentheses)  ",
    "[brackets]",
    "{curly_braces}",
    "slash/and\\backslash",
    "question???",
    "multiple.....dots",
    "name: John Doe",
    "100% guaranteed!",
    "price = $19.99",
    "A\tB\tC",
    "line1\nline2\nline3",
    "   ",
    "",
    "###",
    "abc123!@#$%^&*()",
    "  \t messy \n string \r\n ",
    "ümlaut",
    "café",
    "こんにちは!!!",
    "中文@@@测试",
    "emoji 😀 🚀 👍",
    "----",
    "___---***___",
    "a   b   c",
    "   123   ",
    "\t\n\rwhitespace\r\n\t"
]

print(strCleaner(messy_strings))