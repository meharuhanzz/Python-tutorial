"""Day 9 -- Functions.

Run me with:  python3 main.py
"""


# ---- 1. Defining and calling a function ----
def greet():
    print("Hello!")


print("=== Basic function ===")
greet()      # calling it -- note the parentheses
greet()      # can call it as many times as you want


# ---- 2. Parameters -- passing data in ----
def greet_person(name):
    print(f"Hello, {name}!")


print("\n=== Parameters ===")
greet_person("Ada")
greet_person("Alan")


# ---- 3. Return values -- getting data out ----
# print() just displays something; return actually gives a value back to
# whoever called the function, so you can use it in further code.
def add(a, b):
    return a + b


print("\n=== Return values ===")
result = add(3, 4)
print(f"add(3, 4) = {result}")
print(f"add(3, 4) * 2 = {add(3, 4) * 2}")   # using the return value directly


# ---- 4. Default parameter values ----
def greet_with_title(name, title="Ms."):
    print(f"Hello, {title} {name}!")


print("\n=== Default parameters ===")
greet_with_title("Lovelace")               # uses the default title
greet_with_title("Turing", title="Dr.")    # overrides it


# ---- 5. Multiple return values (returns a tuple, from Day 7) ----
def min_and_max(numbers):
    return min(numbers), max(numbers)


print("\n=== Multiple return values ===")
smallest, largest = min_and_max([4, 8, 15, 16, 23, 42])
print(f"smallest = {smallest}, largest = {largest}")


# ---- 6. *args -- accepting any number of positional arguments ----
def total(*numbers):
    # inside the function, `numbers` is just a tuple
    return sum(numbers)


print("\n=== *args ===")
print(f"total(1, 2, 3) = {total(1, 2, 3)}")
print(f"total(1, 2, 3, 4, 5) = {total(1, 2, 3, 4, 5)}")


# ---- 7. **kwargs -- accepting any number of named arguments ----
def print_profile(**details):
    # inside the function, `details` is just a dict
    for key, value in details.items():
        print(f"  {key}: {value}")


print("\n=== **kwargs ===")
print_profile(name="Ada", age=28, city="London")


# ---- 8. Variable scope: local vs global ----
counter = 0   # this is a "global" variable, defined outside any function


def increment_broken():
    counter = counter + 1   # this actually FAILS -- see below


def increment_fixed():
    global counter           # explicitly say "use the global one"
    counter = counter + 1


print("\n=== Scope ===")
try:
    increment_broken()
except UnboundLocalError as e:
    print(f"increment_broken() failed as expected: {e}")

increment_fixed()
print(f"counter after increment_fixed(): {counter}")

# The `global` keyword is needed rarely in well-designed code -- usually
# it's cleaner to pass values in and return the new value out, rather
# than reaching into a global variable. It's shown here so you recognise
# the error message if you hit it by accident.


# ---- 9. A small, realistic example pulling this together ----
def is_prime(n):
    """Return True if n is a prime number, False otherwise."""
    if n < 2:
        return False
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False
    return True


print("\n=== Primes under 30 ===")
primes = [n for n in range(30) if is_prime(n)]
print(primes)
