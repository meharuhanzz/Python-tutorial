# Day 1 — Python Basics

Today: variables, the four basic data types, and getting input/output on
the screen. This is the foundation everything else builds on.

## Variables

A variable is a name pointing at a value:

```python
name = "Ada"
age = 28
```

Python is **dynamically typed** — you never write `int age = 28` like in
some other languages. Python figures out the type from the value, and a
variable can even be reassigned to a different type later (though doing
that on purpose is usually a sign something's off in your design).

## The four basic types

| Type | Example | Meaning |
|---|---|---|
| `str` | `"hello"` | text — always in quotes |
| `int` | `42` | whole numbers |
| `float` | `3.14` | decimal numbers |
| `bool` | `True` / `False` | yes/no, capitalised, no quotes |

Check any variable's type with `type(x)`.

## print()

`print()` writes text to the screen. Two things worth knowing early:

- Multiple arguments get joined with a space by default: `print("a", "b")` → `a b`
- **f-strings** are the easiest way to mix variables into text:
  ```python
  print(f"{name} is {age} years old")
  ```
  Anything inside `{ }` is evaluated as real Python.

## input()

`input()` pauses your program, waits for the user to type something and
press Enter, and returns **whatever they typed, as a string** — always,
even if they typed `"25"`. If you want to do math with it, you must
convert it yourself:

```python
age_text = input("How old are you? ")   # "25" (a string)
age = int(age_text)                      # 25 (a number)
```

Forgetting this conversion is one of the most common first-week bugs —
if you try `age + 10` while `age` is still a string, Python will raise a
`TypeError`.

## Run it

```bash
python3 main.py
```

It'll ask you two questions via `input()` — type something and press Enter.

## Exercises

Open `exercises.py` and fill in the four TODOs. There's no single correct
answer for most of these — the point is practicing the syntax.
