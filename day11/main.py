"""Day 11 -- File I/O.

Run me with:  python3 main.py

Creates a couple of small files in the same folder so you can see the
results for yourself afterwards (notes.txt, data.csv).
"""
import csv
import os

# ---- 1. Writing a file ----
# The "with" statement is the standard, recommended way to work with
# files -- it automatically closes the file for you, even if an error
# happens partway through. Always prefer it over manually calling
# open()/close().
print("=== Writing a file ===")
with open("notes.txt", "w") as f:      # "w" = write mode (overwrites!)
    f.write("Day 11: File I/O\n")
    f.write("This line was written by main.py\n")
print("Wrote notes.txt")

# ---- 2. Reading a whole file at once ----
print("\n=== Reading a whole file ===")
with open("notes.txt", "r") as f:      # "r" = read mode (the default)
    contents = f.read()
print(contents)

# ---- 3. Reading a file line by line ----
# This is usually the better approach for larger files -- it doesn't load
# the whole thing into memory at once.
print("=== Reading line by line ===")
with open("notes.txt", "r") as f:
    for line in f:
        print(f"  line: {line.strip()}")   # .strip() removes the trailing \n

# ---- 4. Appending to a file (not overwriting) ----
print("\n=== Appending ===")
with open("notes.txt", "a") as f:      # "a" = append mode
    f.write("This line was appended later\n")

with open("notes.txt", "r") as f:
    print(f.read())

# ---- 5. What happens if the file doesn't exist? ----
print("=== Reading a file that doesn't exist ===")
try:
    with open("does_not_exist.txt", "r") as f:
        f.read()
except FileNotFoundError as e:
    print(f"failed as expected: {e}")

# ---- 6. Working with CSV files ----
# CSV (comma-separated values) is one of the most common data formats
# you'll run into. Python's csv module handles the fiddly bits (quoting,
# commas inside values, etc.) for you.
print("\n=== Writing CSV ===")
students = [
    {"name": "Ada", "score": 92},
    {"name": "Alan", "score": 88},
    {"name": "Grace", "score": 95},
]

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    writer.writerows(students)
print("Wrote data.csv")

print("\n=== Reading CSV ===")
with open("data.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # every value from csv.DictReader comes back as a STRING --
        # convert row["score"] with int() if you need to do math with it
        print(f"  {row['name']} scored {row['score']}")

# ---- 7. Cleaning up the files we created (so re-running is repeatable) ----
os.remove("notes.txt")
os.remove("data.csv")
print("\nCleaned up notes.txt and data.csv")
