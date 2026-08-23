# Day 13 — OOP I: Classes & Objects

Everything you've used so far — strings, lists, dicts — is an **object**.
Today you start building your own object types.

## Class = blueprint, object = the actual thing

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

dog1 = Dog("Rex", "Labrador")   # dog1 is an "instance" of Dog
dog1.bark()
```

- `class Dog:` defines the blueprint.
- `__init__` is a special method that runs automatically whenever you
  create a new object — this is where you set up its starting state.
- `self` refers to *this particular object* — inside any method, `self.x`
  means "this object's `x`," as opposed to some other Dog's `x`.
- `dog1 = Dog(...)` creates an actual object (an "instance") from the
  blueprint. You can make as many independent Dogs as you like.

## Instance attributes are separate per object

```python
dog1.name = "Max"
```

changes only `dog1`'s name — `dog2` is completely unaffected. Each object
has its own independent copy of its attributes.

## Methods can read and change an object's own state

A method is just a function defined inside a class, that automatically
gets `self` (the object it was called on) as its first argument:

```python
def deposit(self, amount):
    self.balance += amount
```

## \_\_str\_\_ — controlling how an object prints

By default, `print(my_object)` shows something unhelpful like
`<__main__.Dog object at 0x7f...>`. Defining `__str__` lets you control
that:

```python
def __str__(self):
    return f"Point({self.x}, {self.y})"
```

Methods with double underscores on both sides (like `__init__` and
`__str__`) are called "dunder" (double-underscore) methods — Python calls
these automatically in specific situations, rather than you calling them
directly.

## Class attributes vs instance attributes

An attribute defined directly on the class (not inside `__init__`) is
shared by every instance, unless a specific instance overrides it:

```python
class Employee:
    company_name = "Acme Corp"   # shared by every Employee

    def __init__(self, name):
        self.name = name          # unique to each Employee
```

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
