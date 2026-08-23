# Day 15 — Capstone: Command-Line Contact Book

Congratulations on making it through 14 days — this project pulls
together everything you've learned into one working program.

## What it does

A contact book you interact with through a text menu: add contacts,
view them all, search by name, delete one, and everything is saved to
`contacts.json` so it's still there next time you run it.

## Where each earlier day shows up

| Concept | Day | Where in this project |
|---|---|---|
| Classes & objects | 13 | `Contact` and `ContactBook` classes |
| Inheritance-ready design | 14 | `ContactBook` is written to be subclassed (see `exercises.py` #1) |
| Functions & clean interfaces | 9 | `add()`, `find()`, `search()`, `delete()` methods |
| Lists & dictionaries | 6, 8 | `self.contacts` is a list; `to_dict()`/`from_dict()` convert to/from dicts |
| File I/O & JSON | 10, 11 | `load()`/`save()` persist to `contacts.json` |
| Exception handling | 12 | `ContactNotFoundError`, `ValueError` on empty names |
| Loops & conditionals | 4, 5 | the `while True:` menu loop and its `if`/`elif` chain |
| String formatting | 3 | `Contact.__str__` |

## The "fake_inputs" trick

`main.py`'s `run()` function accepts an optional `fake_inputs` list. When
provided, it feeds those values in instead of calling `input()` for real
— this is how `run_demo()` shows you the whole app working end-to-end
without you needing to type anything. It's a simple, practical way to
test an interactive program.

## Run it

```bash
python3 main.py
```

By default this runs the **scripted demo** (`run_demo()`), so you can see
it working immediately. To actually use it interactively yourself, open
`main.py`, find the `if __name__ == "__main__":` block at the bottom, and
swap which lines are commented out — instructions are right there in the
comment.

Delete `contacts.json` any time you want to reset to an empty contact
book.

## Exercises

Open `exercises.py`. These build *on top of* `ContactBook` rather than
modifying it directly — good practice for working with someone else's
code (or your own past code) without breaking what already works.

## Where to go from here

A few natural next steps if you want to keep extending this:
- Add contact editing (not just add/delete)
- Add input validation (e.g. phone number format checking)
- Turn it into a Streamlit app, like the to-do list project from earlier
  in this repository — the `ContactBook` class barely needs to change,
  only how you get input and show output would be different
- Add automated tests (a topic beyond this 15-day course, but the next
  natural one)
