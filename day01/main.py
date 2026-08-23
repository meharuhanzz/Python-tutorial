"""Day 1 -- Python Basics: variables, data types, print/input.

Run me with:  python3 main.py
"""

# ---- 1. Variables ----
# A variable is just a name that points to a value. Python figures out the
# type for you -- you never have to declare it up front.
name = "Ada"
age = 28
height_m = 1.68
is_programmer = True

print("=== Variables ===")
print(name, age, height_m, is_programmer)

# ---- 2. Checking a variable's type ----
print("\n=== Types ===")
print(type(name))          # <class 'str'>
print(type(age))           # <class 'int'>
print(type(height_m))      # <class 'float'>
print(type(is_programmer))  # <class 'bool'>

# ---- 3. The four basic data types you'll use constantly ----
# str   -- text, always in quotes: "hello" or 'hello'
# int   -- whole numbers: 5, -3, 1000
# float -- decimal numbers: 3.14, -0.5
# bool  -- True or False (capitalised, no quotes)

# ---- 4. print() -- getting output onto the screen ----
print("\n=== print() ===")
print("Hello, world!")
print("Multiple", "values", "get", "joined", "with spaces", "by default")
print("You can change the separator:", "a", "b", "c", sep=" -> ")
print("No newline at the end", end=" | still on this line\n")

# f-strings: the modern, easiest way to build a string with variables in it
print(f"\n{name} is {age} years old and {height_m}m tall.")

# ---- 5. input() -- getting text from the user ----
# input() ALWAYS returns a string, even if the user types a number.
print("\n=== input() ===")
your_name = input("What's your name? ")
print(f"Nice to meet you, {your_name}!")

# To use a number the user typed, you must convert it explicitly:
age_text = input("How old are you? ")
your_age = int(age_text)  # convert the string "25" to the number 25
print(f"In 10 years you'll be {your_age + 10}.")

# ---- 6. Multiple assignment ----
x, y, z = 1, 2, 3
print(f"\nx={x}, y={y}, z={z}")

# ---- 7. Constants (by convention, not enforcement) ----
# Python has no true constants -- by convention, ALL_CAPS names are treated
# as "please don't change this" by other programmers.
PI = 3.14159
