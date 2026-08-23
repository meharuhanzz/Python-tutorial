"""Day 4 -- Conditionals: if / elif / else.

Run me with:  python3 main.py
"""

# ---- 1. The basic if statement ----
# Notice: no parentheses needed around the condition, and the indented
# block (4 spaces, by convention) is what runs if the condition is True.
# Indentation is not just style in Python -- it's how blocks are defined.
temperature = 28

print("=== Basic if ===")
if temperature > 25:
    print("It's warm outside.")

# ---- 2. if / else ----
print("\n=== if / else ===")
age = 15
if age >= 18:
    print("You can vote.")
else:
    print("You can't vote yet.")

# ---- 3. if / elif / else -- checking several conditions in order ----
# Python checks each condition top to bottom and runs the FIRST one that's
# True, then skips the rest. elif = "else if".
print("\n=== if / elif / else ===")
score = 82

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score {score} -> Grade {grade}")

# ---- 4. Combining conditions with and / or ----
print("\n=== Combined conditions ===")
has_ticket = True
is_over_18 = True

if has_ticket and is_over_18:
    print("Welcome to the concert!")

username = "admin"
password = "wrong"
if username == "admin" or password == "letmein":
    print("Access might be granted (one condition matched)")

# ---- 5. Nested conditionals ----
print("\n=== Nested if ===")
weather = "rainy"
have_umbrella = False

if weather == "rainy":
    if have_umbrella:
        print("Good, you're prepared.")
    else:
        print("You'll get wet -- grab an umbrella!")
else:
    print("No umbrella needed today.")

# ---- 6. The "truthiness" of non-bool values ----
# Python lets you use non-bool values directly in an if -- this is common
# and idiomatic, not a hack.
print("\n=== Truthiness ===")
name = ""            # empty string -> treated as False
items = [1, 2, 3]     # non-empty list -> treated as True
count = 0             # zero -> treated as False

if name:
    print("name is set")
else:
    print("name is empty -- this branch runs")

if items:
    print("items has stuff in it -- this branch runs")

if count:
    print("count is non-zero")
else:
    print("count is zero -- this branch runs")

# ---- 7. The ternary (one-line if/else) expression ----
print("\n=== Ternary expression ===")
n = 7
label = "even" if n % 2 == 0 else "odd"
print(f"{n} is {label}")
