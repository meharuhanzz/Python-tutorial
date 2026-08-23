"""Day 8 -- Dictionaries.

Run me with:  python3 main.py
"""

# ---- 1. Creating and accessing dictionaries ----
# A dict stores key -> value pairs. Keys must be immutable (str, int,
# float, tuple all work; list does not).
person = {
    "name": "Ada",
    "age": 28,
    "city": "London",
}

print("=== Creating & accessing ===")
print(person)
print(f"person['name'] = {person['name']}")

# Accessing a missing key with [] raises an error:
try:
    person["email"]
except KeyError as e:
    print(f"person['email'] failed as expected: {e}")

# .get() is the safer way -- returns None (or a default) instead of crashing
print(f"person.get('email') = {person.get('email')}")
print(f"person.get('email', 'not set') = {person.get('email', 'not set')}")

# ---- 2. Adding and updating ----
print("\n=== Adding & updating ===")
person["email"] = "ada@example.com"   # adds a new key
person["age"] = 29                    # updates an existing key
print(person)

# ---- 3. Removing ----
print("\n=== Removing ===")
del person["city"]
print(person)

removed_value = person.pop("email")
print(f"popped: {removed_value}, remaining: {person}")

# ---- 4. Checking for a key ----
print("\n=== Membership ===")
print(f"'name' in person: {'name' in person}")
print(f"'city' in person: {'city' in person}")

# ---- 5. Looping over a dictionary ----
print("\n=== Looping ===")
scores = {"Ada": 92, "Alan": 88, "Grace": 95}

print("keys:")
for key in scores:          # looping over a dict directly gives you the keys
    print(f"  {key}")

print("values:")
for value in scores.values():
    print(f"  {value}")

print("key-value pairs:")
for key, value in scores.items():   # .items() is what you'll use most often
    print(f"  {key}: {value}")

# ---- 6. A dictionary of lists (a very common pattern) ----
print("\n=== Nested structures ===")
classroom = {
    "Ada": ["Math", "Physics"],
    "Alan": ["Computer Science", "Math"],
}
for student, subjects in classroom.items():
    print(f"{student} takes: {', '.join(subjects)}")

# ---- 7. Dict comprehensions (same idea as list comprehensions, Day 6) ----
print("\n=== Dict comprehensions ===")
squares = {n: n ** 2 for n in range(1, 6)}
print(squares)

# ---- 8. A realistic mini-example: counting word frequency ----
print("\n=== Word frequency counter ===")
text = "the cat sat on the mat the cat ran"
words = text.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1   # classic dict-counting pattern

for word, count in counts.items():
    print(f"{word}: {count}")
