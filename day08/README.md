# Day 8 — Dictionaries

A dictionary (`dict`) stores **key → value** pairs. If a list is "a bunch
of things in order," a dict is "a bunch of things you look up by name."

```python
person = {"name": "Ada", "age": 28, "city": "London"}
person["name"]   # "Ada"
```

Keys must be immutable — strings, numbers, and tuples work; lists don't
(this connects back to why Day 7 covered tuple immutability).

## Accessing safely: [] vs .get()

```python
person["email"]           # raises KeyError if "email" isn't there
person.get("email")        # returns None instead
person.get("email", "?")   # returns "?" instead
```

Prefer `.get()` whenever a missing key is a normal possibility, not a bug.

## Adding, updating, removing

```python
person["email"] = "ada@example.com"   # adds if new, updates if it exists
del person["city"]                    # remove a key
person.pop("email")                    # remove and return its value
```

## Looping over a dict

```python
for key in scores:              # just the keys
for value in scores.values():   # just the values
for key, value in scores.items():  # both -- this is what you'll use most
```

## Dict comprehensions

Same idea as list comprehensions:

```python
squares = {n: n ** 2 for n in range(1, 6)}
```

## The counting pattern

One of the most useful dict idioms — worth memorizing:

```python
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
```

`counts.get(word, 0)` returns the current count (or `0` if we haven't
seen this word yet), then we add 1 and store it back.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
