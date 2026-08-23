"""A small module of our own, imported by main.py to demonstrate that
"importing a module" just means "running another .py file and getting
access to whatever it defined"."""


def square(n):
    return n ** 2


def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]


GREETING = "Hello from mymath.py!"
