# Day 2 — Operators & Type Conversion

## Arithmetic operators

| Operator | Meaning | Example |
|---|---|---|
| `+` `-` `*` | add / subtract / multiply | `3 + 4 → 7` |
| `/` | true division — **always returns a float** | `7 / 2 → 3.5` |
| `//` | floor division — rounds down to a whole number | `7 // 2 → 3` |
| `%` | modulo — the remainder | `7 % 2 → 1` |
| `**` | exponent | `2 ** 3 → 8` |

The `/` vs `//` distinction trips up almost everyone at first: `/` always
gives you a `float`, even `10 / 2` gives `5.0`, not `5`.

## Comparison operators

`==`, `!=`, `>`, `<`, `>=`, `<=` — these always evaluate to a `bool`
(`True`/`False`). Note `==` (comparison) vs `=` (assignment) — mixing them
up is a very common typo.

## Logical operators

`and`, `or`, `not` — combine `bool` values. Unlike some languages, Python
spells these as actual words, not `&&`/`||`.

## Type conversion

This is the concept you'll lean on constantly. Since `input()` always
returns a `str`, you need to explicitly convert it to do math:

```python
age = int(input("Age? "))       # str -> int
price = float(input("Price? "))  # str -> float
label = str(42)                    # int -> str
```

**Watch out:** `int(9.9)` gives `9`, not `10` — converting float to int
*truncates* (chops off the decimal part), it does not round. Use
`round(9.9)` if you actually want rounding.

**Also watch out:** `int("hello")` crashes with a `ValueError` — you can't
convert non-numeric text to a number. Day 12 (exception handling) covers
how to guard against this safely.

## Run it

```bash
python3 main.py
```

## Exercises

Open `exercises.py` and work through the four TODOs.
