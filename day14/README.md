# Day 14 — OOP II: Inheritance & Polymorphism

## Inheritance

A class can inherit from another class, getting all of its attributes
and methods for free, and can override anything it needs to behave
differently:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

class Dog(Animal):        # Dog inherits from Animal
    def speak(self):        # overrides Animal's speak()
        print(f"{self.name} says Woof!")
```

`Dog` automatically has `__init__` from `Animal` (it didn't need to be
rewritten) but provides its own `speak()`. Any method *not* overridden
(like a hypothetical `describe()`) is simply inherited unchanged.

## Polymorphism

This is the actual payoff of inheritance: you can treat a `Dog` and a
`Cat` the same way in your code, and each one automatically does the
*right* thing:

```python
animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    animal.speak()   # correct version runs automatically for each type
```

You don't need `if isinstance(animal, Dog): ...` checks scattered through
your code — each object already knows how to handle `.speak()` itself.
This is one of the main reasons OOP is useful for larger programs.

## super()

Sometimes you want to *extend* the parent's behaviour rather than fully
replace it — `super()` lets you call the parent class's version of a
method from inside your override:

```python
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # let Employee do its normal setup
        self.team_size = team_size        # then add Manager's extra bit
```

This avoids duplicating `Employee`'s `__init__` logic inside `Manager`.

## A common pattern: a shared "interface" via NotImplementedError

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")
```

This says "every kind of Shape must know how to compute its own area,
but the base Shape class itself doesn't know how" — it forces each
subclass (`Circle`, `Rectangle`, ...) to provide its own `area()`, while
still letting you write code that treats all shapes uniformly (like
`shape.describe()` in `main.py`, which works for any shape regardless of
which specific subclass it is).

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
