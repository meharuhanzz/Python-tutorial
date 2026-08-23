# Day 4 — Conditionals

## The basic shape

```python
if condition:
    # runs if condition is True
elif other_condition:
    # runs if condition was False but other_condition is True
else:
    # runs if nothing above matched
```

Two things that are easy to trip on if you're coming from another
language:

- **No parentheses needed** around the condition (`if x > 5:`, not `if (x > 5):`).
- **Indentation defines the block.** Python doesn't use `{ }` — the
  indented lines (4 spaces is the convention) *are* the if-block. Get the
  indentation wrong and either you'll get an error, or worse, code that
  runs but does the wrong thing.

`elif` conditions are checked top to bottom, and only the **first** one
that's `True` runs — the rest are skipped, even if they'd also be `True`.

## Combining conditions

```python
if has_ticket and is_over_18:   # both must be True
if username == "admin" or password == "letmein":  # either can be True
if not is_banned:                # negation
```

## Truthiness

You'll often see values used directly in an `if` without a `==`
comparison:

```python
if name:       # True if name is a non-empty string
if items:      # True if the list has anything in it
if count:      # True if count is not 0
```

Empty strings, empty lists, and `0` are all treated as "falsy"; anything
non-empty/non-zero is "truthy". This is idiomatic Python, not a shortcut
to be avoided.

## The ternary expression

A compact one-line if/else that produces a *value* rather than running a
block:

```python
label = "even" if n % 2 == 0 else "odd"
```

Read it as: "`label` is `"even"`, if `n % 2 == 0`, else `"odd"`."

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
