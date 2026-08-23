"""Day 12 -- Exception Handling.

Run me with:  python3 main.py
"""

# ---- 1. The basic try/except ----
# You've already seen the ERRORS these catch on earlier days
# (ValueError, TypeError, KeyError, FileNotFoundError). Today is about
# handling them gracefully instead of letting the program crash.
print("=== Basic try/except ===")
try:
    number = int("not a number")
except ValueError:
    print("That wasn't a valid number.")

print("The program kept running after the error!")

# ---- 2. Catching a specific exception and using its details ----
print("\n=== Using the exception object ===")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Math error: {e}")

# ---- 3. Catching multiple exception types ----
print("\n=== Multiple except blocks ===")


def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Can't divide by zero!")
        return None
    except TypeError:
        print("Both arguments need to be numbers!")
        return None


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "two"))

# ---- 4. else and finally ----
# else: runs only if the try block did NOT raise an exception
# finally: runs no matter what -- error or not, this always executes
print("\n=== try / except / else / finally ===")


def read_number(text):
    try:
        value = int(text)
    except ValueError:
        print(f"'{text}' is not a number")
    else:
        print(f"Successfully parsed: {value}")
    finally:
        print("Done attempting to parse.\n")


read_number("42")
read_number("oops")

# ---- 5. Catching ANY exception (use sparingly!) ----
# A bare `except:` or `except Exception:` catches everything -- handy for
# a top-level safety net, but overusing it can hide real bugs. Prefer
# catching the specific exception you expect whenever you can.
print("=== Catching any exception ===")
risky_operations = [lambda: 1 / 0, lambda: int("x"), lambda: [1, 2][5]]

for operation in risky_operations:
    try:
        operation()
    except Exception as e:
        print(f"Something went wrong: {type(e).__name__}: {e}")

# ---- 6. Raising your own exceptions ----
print("\n=== Raising exceptions ===")


def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount


try:
    withdraw(100, 500)
except ValueError as e:
    print(f"Withdrawal failed: {e}")

# ---- 7. Defining your own exception type ----
# For bigger projects, custom exception classes make error handling more
# precise -- callers can catch exactly your error type, not just any
# ValueError from anywhere in the program.
print("\n=== Custom exception types ===")


class InsufficientFundsError(Exception):
    pass


def withdraw_v2(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Tried to withdraw {amount}, only have {balance}")
    return balance - amount


try:
    withdraw_v2(100, 500)
except InsufficientFundsError as e:
    print(f"Custom error caught: {e}")

# ---- 8. A realistic example: safely getting numeric input ----
print("\n=== Realistic example: safe input loop ===")


def get_positive_number(prompt, fake_inputs=None):
    """fake_inputs lets us demo this without needing real user typing."""
    fake_iter = iter(fake_inputs) if fake_inputs else None
    while True:
        text = next(fake_iter) if fake_iter else input(prompt)
        try:
            value = float(text)
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print(f"'{text}' isn't a valid number, try again.")


# Demo with pretend user input: "-5" (rejected), "abc" (rejected), "3.5" (accepted)
answer = get_positive_number("Enter a positive number: ", fake_inputs=["-5", "abc", "3.5"])
print(f"Got: {answer}")
