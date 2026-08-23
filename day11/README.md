# Day 11 — File I/O

## The `with` statement

Always open files using `with` — it guarantees the file gets closed
properly, even if an error happens while you're working with it:

```python
with open("notes.txt", "w") as f:
    f.write("hello\n")
# file is automatically closed here, even if something went wrong above
```

Avoid the manual `f = open(...)` / `f.close()` pattern — it's easy to
forget the `close()` call, especially if an exception happens in between.

## File modes

| Mode | Meaning |
|---|---|
| `"r"` | read (default) — errors if the file doesn't exist |
| `"w"` | write — **creates the file, or overwrites it if it already exists** |
| `"a"` | append — adds to the end without erasing what's there |

The `"w"` mode overwriting silently is a common source of "wait, where
did my data go" bugs — reach for `"a"` when you mean to add, not replace.

## Reading

```python
contents = f.read()          # the whole file as one string

for line in f:                 # loop over it line by line (memory-efficient)
    print(line.strip())         # .strip() removes the trailing newline
```

## CSV files

CSV (comma-separated values) is everywhere in real data work. Python's
built-in `csv` module handles quoting and edge cases for you — don't
parse CSV by hand with `.split(",")`, it breaks the moment a value
contains a comma.

```python
import csv

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows([{"name": "Ada", "score": 92}])

with open("data.csv", "r", newline="") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["score"])
```

**Note:** everything `csv.DictReader` gives you back is a `str` — if you
need to do math on a column, convert it (`int(row["score"])`) yourself,
same as with `input()` back on Day 1.

## Errors are normal here

Files not existing, or being in the wrong format, is one of the most
common real-world error sources — `main.py` shows what a
`FileNotFoundError` looks like. Day 12 covers handling these gracefully
with `try`/`except` rather than letting your program crash.

## Run it

```bash
python3 main.py
```

It creates and then deletes a couple of small files so you can re-run it
freely.

## Exercises

Open `exercises.py` and work through the four TODOs.
