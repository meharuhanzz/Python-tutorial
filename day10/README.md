# Day 10 — Modules & the Standard Library

A **module** is just a `.py` file. When you `import` one, Python runs it
once and gives you access to whatever names (functions, variables,
classes) it defined at the top level.

## Three ways to import

```python
import math
math.sqrt(16)              # access things with the module name prefix

from random import randint
randint(1, 6)               # imported directly, no prefix needed

import datetime as dt
dt.date.today()             # aliased to a shorter name
```

All three are common — which one you reach for depends on how much of the
module you're using and whether the name clashes with something else in
your file.

## Importing your own files

This is the same mechanism as importing `math` or `random` — `mymath.py`
sits right next to `main.py` in this folder, and:

```python
import mymath
mymath.square(5)
```

just runs `mymath.py` and gives you access to the `square` function (and
anything else) it defined. This is how real Python projects are
organized: split code across multiple files, and `import` between them,
rather than putting everything in one giant script.

## The standard library

Python ships with a huge collection of modules covering common problems,
so you don't need external packages for a lot of everyday tasks:

| Module | For |
|---|---|
| `math` | mathematical functions and constants |
| `random` | random numbers, choices, shuffling |
| `datetime` | dates and times |
| `os` | interacting with the operating system (paths, environment) |
| `json` | converting between Python objects and JSON text |
| `string` | useful string constants (`ascii_lowercase`, etc.) |

Before reaching for an external package or writing something from
scratch, it's always worth checking whether the standard library already
has it — the official docs at
[docs.python.org/3/library](https://docs.python.org/3/library/) are
searchable and a good habit to build.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs. Exercise 4 has you
add a function to `mymath.py` — practice editing a module, not just using
one.
