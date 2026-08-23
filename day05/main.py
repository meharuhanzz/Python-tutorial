"""Day 5 -- Loops: for, while, break/continue.

Run me with:  python3 main.py
"""

# ---- 1. for loops over a range ----
# range(5) produces 0, 1, 2, 3, 4 -- 5 numbers, starting at 0, NOT
# including 5. This trips up almost everyone at first.
print("=== range(5) ===")
for i in range(5):
    print(i)

print("\n=== range(2, 6) -- start, stop ===")
for i in range(2, 6):
    print(i)

print("\n=== range(0, 10, 2) -- start, stop, step ===")
for i in range(0, 10, 2):
    print(i)

# ---- 2. for loops over a sequence directly ----
# You very often loop over the actual items, not indexes.
print("\n=== for over a list ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# When you need BOTH the index and the item, use enumerate():
print("\n=== enumerate() ===")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# ---- 3. for loops over a string ----
print("\n=== for over a string ===")
for letter in "abc":
    print(letter)

# ---- 4. while loops ----
# Runs as long as the condition stays True. You are responsible for making
# sure something inside the loop eventually makes the condition False --
# otherwise it's an infinite loop.
print("\n=== while loop ===")
count = 0
while count < 5:
    print(f"count is {count}")
    count += 1   # without this line, the loop would never end!

# ---- 5. break -- exit a loop early ----
print("\n=== break ===")
for number in range(100):
    if number == 5:
        break   # stop the loop entirely, right here
    print(number)

# ---- 6. continue -- skip to the next iteration ----
print("\n=== continue ===")
for number in range(10):
    if number % 2 != 0:
        continue   # skip the rest of this iteration for odd numbers
    print(f"{number} is even")

# ---- 7. A classic: FizzBuzz, using everything from today and Day 4 ----
print("\n=== FizzBuzz (1-15) ===")
for n in range(1, 16):
    if n % 15 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)

# ---- 8. Nested loops ----
print("\n=== Nested loops: multiplication table ===")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row} x {col} = {row * col}", end="   ")
    print()  # newline after each row
