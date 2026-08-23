# Day 12 — Exception Handling

You've already met several errors on earlier days: `ValueError` (Day 2,
converting bad text to a number), `TypeError` (Day 7, modifying a tuple),
`KeyError` (Day 8, missing dict key), `FileNotFoundError` (Day 11).
Today's about catching them gracefully instead of letting the whole
program crash.

## The basic pattern

```python
try:
    number = int("not a number")
except ValueError:
    print("That wasn't a valid number.")

print("execution continues here")
```

Without the `try`/`except`, that `ValueError` would stop the whole
program immediately. With it, you handle the problem and keep going.

## Catching multiple exception types

```python
try:
    ...
except ZeroDivisionError:
    ...
except TypeError:
    ...
```

Each `except` block only catches the type it names — this lets you
respond differently depending on what went wrong.

## else and finally

```python
try:
    value = int(text)
except ValueError:
    print("invalid")
else:
    print("only runs if try succeeded")
finally:
    print("always runs, error or not")
```

`finally` is commonly used for cleanup (closing a file, a network
connection) that must happen either way.

## Catching "anything"

`except Exception as e:` catches essentially all errors — useful as a
last-resort safety net, but **use it sparingly**. Catching everything
indiscriminately can hide real bugs you actually wanted to know about.
Prefer naming the specific exception you expect whenever you reasonably
can.

## Raising your own errors

```python
def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds")
    return balance - amount
```

`raise` triggers an exception on purpose — useful for enforcing rules in
your own functions ("this input doesn't make sense, stop here").

## Custom exception types

For anything beyond a small script, defining your own exception class
makes error handling more precise — callers can catch *exactly* your
error, not just any `ValueError` that might come from anywhere:

```python
class InsufficientFundsError(Exception):
    pass

raise InsufficientFundsError("Tried to withdraw 500, only have 100")
```

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
