# Day 6 — Lists

Lists are Python's general-purpose, ordered, **mutable** collection — the
data structure you'll reach for constantly.

```python
fruits = ["apple", "banana", "cherry"]
```

## Indexing and slicing

Same rules as strings from Day 3 — `fruits[0]` for the first item,
`fruits[-1]` for the last, `fruits[1:3]` for a slice.

## Mutability

Unlike strings, lists **can** be changed in place:

```python
fruits[0] = "avocado"   # works fine -- lists are mutable
```

## Adding and removing

| Method | What it does |
|---|---|
| `.append(x)` | add `x` to the end |
| `.insert(i, x)` | insert `x` at index `i` |
| `.remove(x)` | remove the first item *equal to* `x` |
| `.pop()` | remove and return the last item |
| `.pop(i)` | remove and return the item at index `i` |

## sorted() vs .sort()

- `sorted(my_list)` returns a **new** sorted list, leaving the original
  untouched.
- `my_list.sort()` sorts the list **in place** and returns `None` — a
  classic gotcha is writing `my_list = my_list.sort()`, which sets
  `my_list` to `None`.

## List comprehensions

A compact way to build a new list from an existing one:

```python
squares = [n ** 2 for n in range(1, 6)]
evens = [n for n in range(20) if n % 2 == 0]
```

Read the first as "n-squared, for each n in range(1, 6)". This is
shorthand for the loop-and-append pattern you already know from Day 5:

```python
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
```

Both do exactly the same thing — the comprehension is just more compact
once you're comfortable with the pattern. Don't force it if a plain loop
is clearer for what you're doing.

## Handy built-ins

`len(x)`, `sum(x)`, `min(x)`, `max(x)`, `x in list` (membership check) all
work directly on lists.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
