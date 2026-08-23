# Day 3 — Strings & String Methods

## Making strings

`"double"` and `'single'` quotes are identical in Python — pick whichever
avoids escaping (e.g. use `'He said "hi"'` rather than `"He said \"hi\""`).
Triple quotes (`"""..."""`) let a string span multiple lines.

## Indexing and slicing

A string is a sequence of characters, and you can pull pieces out of it
with `[ ]`:

```python
word = "Python"
word[0]     # 'P'   -- first character (indexing starts at 0!)
word[-1]    # 'n'   -- last character
word[0:3]   # 'Pyt' -- from index 0 up to (not including) index 3
word[2:]    # 'thon' -- from index 2 to the end
word[::-1]  # 'nohtyP' -- the whole string, reversed
```

The slice syntax is `[start:stop:step]` — any of the three can be omitted.

## Strings are immutable

You can't change a character in place (`word[0] = "J"` raises an error) —
string methods always **return a new string** rather than modifying the
original:

```python
s = "hello"
s.upper()      # returns "HELLO" -- but s itself is still "hello"!
s = s.upper()   # you have to reassign to actually keep the change
```

## Common methods

| Method | What it does |
|---|---|
| `.strip()` | remove leading/trailing whitespace |
| `.lower()` / `.upper()` | change case |
| `.replace(old, new)` | swap all occurrences of `old` for `new` |
| `.split(sep)` | break into a list of pieces around `sep` |
| `sep.join(list)` | opposite of split — join a list back into a string |
| `.startswith(x)` / `.endswith(x)` | check the start/end |
| `x in s` | check whether `x` appears anywhere in `s` |
| `len(s)` | how many characters |

## f-string number formatting

You already know `f"{value}"`. You can also control *how* it's shown:

```python
f"{pi:.2f}"       # 2 decimal places -> "3.14"
f"{big_number:,}"  # thousands separator -> "1,234,567"
```

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
