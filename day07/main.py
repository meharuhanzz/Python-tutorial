"""Day 7 -- Tuples & Sets.

Run me with:  python3 main.py
"""

# ==========================================================
# PART 1: Tuples -- like lists, but immutable (can't change after creation)
# ==========================================================

print("=== Creating tuples ===")
point = (3, 4)
print(point, type(point))

# A single-item tuple needs a trailing comma -- (5) is just the number 5
# in parentheses, not a tuple!
not_a_tuple = (5)
really_a_tuple = (5,)
print(f"type((5)) = {type(not_a_tuple)}")
print(f"type((5,)) = {type(really_a_tuple)}")

# Indexing and slicing work exactly like lists
print(f"\npoint[0] = {point[0]}, point[1] = {point[1]}")

# But you CANNOT modify a tuple -- this is the whole point of them:
print("\n=== Immutability ===")
try:
    point[0] = 99
except TypeError as e:
    print(f"point[0] = 99 failed as expected: {e}")

# ---- Why use a tuple instead of a list? ----
# 1. It signals "this shouldn't change" to anyone reading your code.
# 2. Tuples can be used as dictionary keys (Day 8) -- lists can't, because
#    dict keys must be immutable.
# 3. A very common pattern: returning multiple values from a function
#    (Day 9) actually returns a tuple under the hood.

# ---- Tuple unpacking ----
print("\n=== Tuple unpacking ===")
x, y = point
print(f"x = {x}, y = {y}")

name, age, city = ("Ada", 28, "London")
print(f"{name} is {age} and lives in {city}")


# ==========================================================
# PART 2: Sets -- unordered collections of UNIQUE items
# ==========================================================

print("\n=== Creating sets ===")
fruits = {"apple", "banana", "cherry", "apple"}  # duplicate "apple" is dropped
print(fruits)  # order is not guaranteed!

# Turning a list into a set is the classic way to remove duplicates:
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(numbers)
print(f"\nlist: {numbers}")
print(f"set (duplicates removed): {unique_numbers}")

# ---- Adding, removing, checking membership ----
print("\n=== Modifying sets ===")
fruits.add("date")
print(f"after add: {fruits}")
fruits.discard("banana")   # doesn't error if the item isn't there
print(f"after discard: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")  # membership checks are very fast on sets

# ---- Set operations (this is where sets really shine) ----
print("\n=== Set operations ===")
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"a = {a}")
print(f"b = {b}")
print(f"union (a | b): {a | b}")              # everything in either
print(f"intersection (a & b): {a & b}")        # only what's in both
print(f"difference (a - b): {a - b}")          # in a but not b
print(f"symmetric difference (a ^ b): {a ^ b}")  # in one or the other, not both

# ---- Sets are unordered -- you can't index into them ----
try:
    fruits[0]
except TypeError as e:
    print(f"\nfruits[0] failed as expected: {e}")
