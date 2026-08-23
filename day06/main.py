"""Day 6 -- Lists.

Run me with:  python3 main.py
"""

# ---- 1. Creating and indexing lists ----
fruits = ["apple", "banana", "cherry"]
print("=== Creating & indexing ===")
print(fruits)
print(f"fruits[0] = {fruits[0]}")
print(f"fruits[-1] = {fruits[-1]}")   # last item
print(f"len(fruits) = {len(fruits)}")

# Lists can hold mixed types, and even other lists
mixed = ["text", 42, 3.14, True, [1, 2]]
print(f"mixed = {mixed}")

# ---- 2. Lists are mutable -- you can change them in place ----
print("\n=== Mutability ===")
fruits[0] = "avocado"   # replace an item
print(fruits)

# ---- 3. Adding and removing items ----
print("\n=== Adding & removing ===")
fruits.append("date")           # add to the end
print(f"after append: {fruits}")

fruits.insert(1, "blueberry")   # insert at a specific index
print(f"after insert: {fruits}")

fruits.remove("banana")         # remove the first matching value
print(f"after remove('banana'): {fruits}")

popped = fruits.pop()           # remove & return the LAST item
print(f"popped: {popped}, remaining: {fruits}")

popped_first = fruits.pop(0)    # remove & return item at index 0
print(f"popped index 0: {popped_first}, remaining: {fruits}")

# ---- 4. Slicing (same rules as string slicing from Day 3) ----
print("\n=== Slicing ===")
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"numbers[2:5] = {numbers[2:5]}")
print(f"numbers[:3] = {numbers[:3]}")
print(f"numbers[-3:] = {numbers[-3:]}")
print(f"numbers[::2] = {numbers[::2]}")   # every 2nd item

# ---- 5. Checking membership, sorting, reversing ----
print("\n=== Membership, sort, reverse ===")
print(f"5 in numbers: {5 in numbers}")
print(f"99 in numbers: {99 in numbers}")

unsorted = [5, 2, 8, 1, 9]
print(f"sorted(unsorted) = {sorted(unsorted)}")               # new list, doesn't change original
print(f"sorted(unsorted, reverse=True) = {sorted(unsorted, reverse=True)}")
print(f"unsorted is still: {unsorted}")

unsorted.sort()  # this one DOES change the list in place (no return value)
print(f"after .sort(): {unsorted}")

# ---- 6. Looping over a list (recap from Day 5) ----
print("\n=== Looping ===")
for fruit in fruits:
    print(f"- {fruit}")

# ---- 7. List comprehensions -- a compact way to build a new list ----
# This is one of Python's signature features. The pattern is:
#   [expression for item in iterable if condition]
print("\n=== List comprehensions ===")
squares = [n ** 2 for n in range(1, 6)]
print(f"squares = {squares}")

evens = [n for n in range(20) if n % 2 == 0]
print(f"evens = {evens}")

# The traditional way, for comparison -- comprehensions are shorthand
# for this exact pattern:
squares_the_long_way = []
for n in range(1, 6):
    squares_the_long_way.append(n ** 2)
print(f"squares_the_long_way = {squares_the_long_way}")

# ---- 8. Useful built-ins that work on lists ----
print("\n=== sum, min, max ===")
scores = [88, 92, 79, 95, 60]
print(f"sum = {sum(scores)}, min = {min(scores)}, max = {max(scores)}, avg = {sum(scores) / len(scores):.1f}")
