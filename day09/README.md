# Day 9 — Functions

Functions let you package up a piece of logic, give it a name, and reuse
it — instead of copy-pasting the same code everywhere.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Ada")   # calling it
```

## return vs print

These get confused constantly when you're starting out:

- `print()` **displays** something on screen. It doesn't give the calling
  code anything to work with.
- `return` **hands a value back** to whoever called the function, so you
  can store it, use it in a calculation, pass it to another function, etc.

```python
def add(a, b):
    return a + b

result = add(3, 4)       # result is now 7
print(add(3, 4) * 2)      # 14 -- you can use the return value directly
```

A function with no `return` statement implicitly returns `None`.

## Default parameters

```python
def greet_with_title(name, title="Ms."):
    ...

greet_with_title("Lovelace")             # uses "Ms."
greet_with_title("Turing", title="Dr.")   # overrides it
```

## Multiple return values

Python lets you return several values at once — this is really returning
a single tuple (Day 7) that gets unpacked automatically:

```python
def min_and_max(numbers):
    return min(numbers), max(numbers)

smallest, largest = min_and_max([4, 8, 15, 16, 23, 42])
```

## \*args and \*\*kwargs

For when you don't know in advance how many arguments will be passed:

```python
def total(*numbers):     # numbers becomes a tuple inside the function
    return sum(numbers)

total(1, 2, 3)             # 6
total(1, 2, 3, 4, 5)        # 15
```

```python
def print_profile(**details):   # details becomes a dict inside the function
    for key, value in details.items():
        print(key, value)

print_profile(name="Ada", age=28)
```

## Scope: local vs global

Variables created *inside* a function only exist inside that function
(that's "local scope"). A variable defined outside every function is
"global." If you try to modify a global variable from inside a function
without saying `global counter` first, Python raises an
`UnboundLocalError` — see `main.py` for exactly what that looks like.

In practice, you'll rarely need the `global` keyword in well-organized
code — usually it's cleaner to pass the value in as a parameter and
`return` the updated value, rather than reaching into a global.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
