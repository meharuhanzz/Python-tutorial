"""Day 10 -- Modules & the Standard Library.

Run me with:  python3 main.py
"""

# ---- 1. Importing a whole module ----
import math

print("=== import math ===")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"math.floor(4.7) = {math.floor(4.7)}")
print(f"math.ceil(4.2) = {math.ceil(4.2)}")

# ---- 2. Importing specific names ----
from random import randint, choice

print("\n=== from random import ... ===")
print(f"randint(1, 6) = {randint(1, 6)}")   # a random dice roll
colours = ["red", "green", "blue", "yellow"]
print(f"choice(colours) = {choice(colours)}")

# ---- 3. Importing with an alias ----
import datetime as dt

print("\n=== import datetime as dt ===")
today = dt.date.today()
print(f"today = {today}")
print(f"today.year = {today.year}, today.month = {today.month}, today.day = {today.day}")

now = dt.datetime.now()
print(f"now = {now}")

# ---- 4. Importing your OWN module ----
# mymath.py sits right next to this file. "Importing" it just means
# Python runs mymath.py once and gives you access to whatever it defined.
import mymath

print("\n=== import mymath (our own file) ===")
print(mymath.GREETING)
print(f"mymath.square(5) = {mymath.square(5)}")
print(f"mymath.is_palindrome('racecar') = {mymath.is_palindrome('racecar')}")
print(f"mymath.is_palindrome('python') = {mymath.is_palindrome('python')}")

# You could also do: from mymath import square, is_palindrome
# and then call square(5) directly, without the "mymath." prefix.

# ---- 5. A few other stdlib modules worth knowing exist ----
print("\n=== A few more useful stdlib modules ===")

import os
print(f"os.getcwd() = {os.getcwd()}")   # current working directory

import json
data = {"name": "Ada", "age": 28}
as_json = json.dumps(data)               # Python dict -> JSON string
print(f"json.dumps(data) = {as_json}")
back_to_dict = json.loads(as_json)       # JSON string -> Python dict
print(f"json.loads(...) = {back_to_dict}")

import string
print(f"string.ascii_lowercase = {string.ascii_lowercase}")

# ---- 6. Why this matters ----
# Python's standard library is huge and covers most everyday problems --
# random numbers, dates, file paths, JSON, regular expressions, and much
# more. Before writing something from scratch, it's always worth checking
# "is there already a stdlib module for this?"
