# Day 7 — Tuples & Sets

Two more collection types, each solving a specific problem lists don't.

## Tuples — immutable, ordered

Written with parentheses: `(3, 4)`. Indexing and slicing work exactly like
lists — the difference is you **cannot change a tuple after creating it**:

```python
point = (3, 4)
point[0] = 99   # TypeError: 'tuple' object does not support item assignment
```

**Gotcha:** a single-item tuple needs a trailing comma — `(5)` is just the
number `5`, but `(5,)` is a tuple containing `5`.

Why use a tuple instead of a list?
- It signals to readers "this data shouldn't change."
- Tuples can be dictionary keys (Day 8) — lists can't, since dict keys
  must be immutable.
- Functions that return multiple values (Day 9) return a tuple under the
  hood.

### Unpacking

```python
name, age, city = ("Ada", 28, "London")
```

This works for any tuple (or list) of the matching length — it's used
constantly, not just for literal tuples.

## Sets — unordered, unique

Written with curly braces: `{1, 2, 3}`. A set automatically drops
duplicates and has **no guaranteed order** — you can't index into one.

The most common use: removing duplicates from a list.

```python
unique = set([1, 2, 2, 3, 3, 3])   # {1, 2, 3}
```

### Set operations

Where sets really shine — fast, readable comparisons between groups:

| Operator | Meaning |
|---|---|
| `a \| b` | union — everything in either set |
| `a & b` | intersection — only what's in both |
| `a - b` | difference — in `a` but not `b` |
| `a ^ b` | symmetric difference — in one or the other, not both |

Checking membership (`x in my_set`) is also significantly faster on a
large set than on a large list — worth knowing as your data grows.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
