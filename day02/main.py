"""Day 2 -- Operators & Type Conversion.

Run me with:  python3 main.py
"""

# ---- 1. Arithmetic operators ----
a, b = 17, 5

print("=== Arithmetic ===")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")    # true division -> always a float
print(f"{a} // {b} = {a // b}")  # floor division -> rounds down to an int
print(f"{a} % {b} = {a % b}")    # modulo -> the remainder
print(f"{a} ** {b} = {a ** b}")  # exponent -> a to the power of b

# ---- 2. Comparison operators (always return a bool) ----
print("\n=== Comparison ===")
print(f"{a} == {b}: {a == b}")   # equal to
print(f"{a} != {b}: {a != b}")   # not equal to
print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} >= 17: {a >= 17}")
print(f"{a} <= 16: {a <= 16}")

# ---- 3. Logical operators ----
print("\n=== Logical ===")
is_sunny = True
is_warm = False
print(f"is_sunny and is_warm: {is_sunny and is_warm}")
print(f"is_sunny or is_warm: {is_sunny or is_warm}")
print(f"not is_sunny: {not is_sunny}")

# ---- 4. Assignment shortcuts ----
print("\n=== Assignment shortcuts ===")
counter = 0
counter += 1   # same as: counter = counter + 1
counter += 1
counter *= 10
print(f"counter ended up at: {counter}")

# ---- 5. Type conversion ("casting") ----
# This is the big one -- you'll use this constantly, especially after
# input(), which always gives you back a string.
print("\n=== Type conversion ===")
num_text = "42"
num = int(num_text)          # str -> int
print(f"int('42') = {num}, type: {type(num)}")

price_text = "19.99"
price = float(price_text)    # str -> float
print(f"float('19.99') = {price}, type: {type(price)}")

count = 7
count_text = str(count)      # int -> str (useful for building messages)
print(f"str(7) = '{count_text}', type: {type(count_text)}")

# Converting a float to int TRUNCATES (cuts off), it doesn't round:
print(f"int(9.9) = {int(9.9)}")   # 9, not 10!

# Converting a non-numeric string raises an error -- try/except (Day 12)
# is how you'd handle that safely. For now, just know it can fail:
try:
    int("not a number")
except ValueError as e:
    print(f"\nint('not a number') failed as expected: {e}")
