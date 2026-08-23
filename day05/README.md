# Day 5 — Loops

## for loops and range()

`range(stop)` produces numbers starting at 0, up to but **not including**
`stop`:

```python
for i in range(5):    # 0, 1, 2, 3, 4 -- five numbers
    print(i)
```

`range(start, stop)` and `range(start, stop, step)` give you more control:

```python
range(2, 6)      # 2, 3, 4, 5
range(0, 10, 2)  # 0, 2, 4, 6, 8
```

## Looping over items directly

Most of the time you don't need indexes at all — loop over the actual
values:

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

If you need the index *and* the value, use `enumerate()` rather than
manually tracking a counter:

```python
for index, fruit in enumerate(fruits):
    print(index, fruit)
```

## while loops

Runs as long as its condition is `True`. **You** are responsible for
making the condition eventually become `False` — forgetting to update the
thing being checked is the classic way to write an infinite loop:

```python
count = 0
while count < 5:
    print(count)
    count += 1   # miss this line and the loop never ends
```

## break and continue

- **`break`** exits the loop immediately, entirely.
- **`continue`** skips the rest of *this* iteration and moves to the next one.

```python
for n in range(100):
    if n == 5:
        break       # stop looping entirely once n hits 5

for n in range(10):
    if n % 2 != 0:
        continue     # skip odd numbers, keep going for the rest
    print(n)
```

## Nested loops

A loop inside another loop — the inner loop runs completely for every
single iteration of the outer one. Common for grids, tables, and anything
2D.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
