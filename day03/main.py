"""Day 3 -- Strings & String Methods.

Run me with:  python3 main.py
"""

# ---- 1. Creating strings ----
s1 = "double quotes"
s2 = 'single quotes -- both work the same'
s3 = """a triple-quoted string
can span
multiple lines"""

print("=== Creating strings ===")
print(s1, "|", s2)
print(s3)

# ---- 2. Concatenation and repetition ----
print("\n=== Concatenation ===")
first = "Py"
second = "thon"
print(first + second)     # "Python"
print(first * 3)          # "PyPyPy"

# ---- 3. Indexing and slicing ----
# Strings are sequences of characters -- you can index into them like a
# list. Indexing starts at 0. Negative indexes count from the end.
word = "Python"
print("\n=== Indexing & slicing ===")
print(f"word = '{word}'")
print(f"word[0] = '{word[0]}'")     # 'P' (first character)
print(f"word[-1] = '{word[-1]}'")   # 'n' (last character)
print(f"word[0:3] = '{word[0:3]}'")  # 'Pyt' (index 0 up to, not including, 3)
print(f"word[2:] = '{word[2:]}'")    # 'thon' (from index 2 to the end)
print(f"word[:2] = '{word[:2]}'")    # 'Py' (start to index 2)
print(f"word[::-1] = '{word[::-1]}'")  # 'nohtyP' (reversed!)

# ---- 4. Useful string methods ----
messy = "  Hello, World!  "
print("\n=== String methods ===")
print(f"repr(messy) = {messy!r}")
print(f".strip() = '{messy.strip()}'")            # remove leading/trailing whitespace
print(f".lower() = '{messy.lower()}'")
print(f".upper() = '{messy.upper()}'")
print(f".replace(...) = '{messy.replace('World', 'Python')}'")
print(f".split(',') = {messy.strip().split(',')}")  # splits into a list

clean = "python,is,fun"
print(f"'{clean}'.split(',') = {clean.split(',')}")
print(f"','.join(['a','b','c']) = {','.join(['a', 'b', 'c'])}")  # opposite of split

# Checking contents
name = "Ada Lovelace"
print(f"\n'{name}'.startswith('Ada') = {name.startswith('Ada')}")
print(f"'{name}'.endswith('ace') = {name.endswith('ace')}")
print(f"'Lovelace' in '{name}' = {'Lovelace' in name}")
print(f"len('{name}') = {len(name)}")

# ---- 5. f-strings, revisited: formatting numbers ----
pi = 3.14159265
print("\n=== f-string formatting ===")
print(f"pi to 2 decimal places: {pi:.2f}")
print(f"pi padded to width 10: '{pi:10.2f}'")
big_number = 1234567
print(f"with thousands separator: {big_number:,}")
