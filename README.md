# Python Tutorial

Beginner-friendly Python tutorials for first-time learners.

## Streamlit To-Do List

A minimal to-do list web app with a full mentoring guide (how Streamlit
works, code walkthrough, exercises). See
[`streamlit-todolist/`](streamlit-todolist/).

## Expense Tracker

A minimal expense tracker web app — log expenses, filter by category,
delete them, see totals and a spending-by-category chart — with the same
kind of full mentoring guide. See
[`streamlit-expensetracker/`](streamlit-expensetracker/).

## Digital Clock

A live digital clock (client-side JS via `st.iframe`), a timezone lookup
using the standard-library `zoneinfo` module, and a session-state-driven
stopwatch. See [`streamlit-digitalclock/`](streamlit-digitalclock/).

## PDF Generator

Build a simple document from title + content blocks (paragraphs,
headings, bullet lists) and download it as a real PDF, built entirely in
memory with `reportlab`. See [`streamlit-pdfgenerator/`](streamlit-pdfgenerator/).

## Plagiarism Checker

Compares two texts for overlap using the standard-library `difflib`
module — two similarity scores, and a highlighted diff of the matching
passages. A teaching tool, not a research-grade detector (the guide
explains why). See [`streamlit-plagiarismchecker/`](streamlit-plagiarismchecker/).

## Python in 15 Days

A full beginner Python course — browse day-by-day right here as folders,
or check out the matching `dayNN` branch if you'd rather have just that
day's files at the repo root.

```bash
git clone https://github.com/meharuhanzz/Python-tutorial.git
cd Python-tutorial/day01
python3 main.py
```

| Day | Folder | Topic |
|---|---|---|
| 1 | [`day01/`](day01/) | Python basics: variables, data types, `print`/`input` |
| 2 | [`day02/`](day02/) | Operators & type conversion |
| 3 | [`day03/`](day03/) | Strings & string methods |
| 4 | [`day04/`](day04/) | Conditionals: `if` / `elif` / `else` |
| 5 | [`day05/`](day05/) | Loops: `for`, `while`, `break`/`continue` |
| 6 | [`day06/`](day06/) | Lists |
| 7 | [`day07/`](day07/) | Tuples & sets |
| 8 | [`day08/`](day08/) | Dictionaries |
| 9 | [`day09/`](day09/) | Functions |
| 10 | [`day10/`](day10/) | Modules & the standard library |
| 11 | [`day11/`](day11/) | File I/O |
| 12 | [`day12/`](day12/) | Exception handling |
| 13 | [`day13/`](day13/) | OOP I: classes & objects |
| 14 | [`day14/`](day14/) | OOP II: inheritance & polymorphism |
| 15 | [`day15/`](day15/) | Capstone: a command-line contact book |

Every `dayNN/` folder has the same shape:

- **`README.md`** — what you're learning today, explained, with examples
- **`main.py`** — runnable code demonstrating today's concepts
- **`exercises.py`** — practice problems (with TODOs) — try these yourself

Run any day's code with `python3 main.py` from inside that folder.

## Author

Meharuniza
