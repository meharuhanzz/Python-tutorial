"""Day 15 -- Exercises. Fill in the TODOs, then run: python3 exercises.py

These extend the Contact Book from main.py -- import it and build on top,
rather than starting from scratch.
"""
from main import ContactBook, ContactNotFoundError  # noqa: F401


# 1. Add a method to a NEW subclass `ContactBookWithFavourites(ContactBook)`
#    that stores a list of favourite contact names, plus methods
#    `mark_favourite(name)` and `list_favourites()`. (This practices
#    inheritance from Day 14 -- extend ContactBook rather than editing it.)
# TODO


# 2. Write a function `contacts_missing_email(book)` that returns a list
#    of contact names that have no email address set.
# TODO


# 3. Add a `update_phone(name, new_phone)` method that finds a contact
#    (reuse book.find(), which already raises ContactNotFoundError if
#    missing) and updates their phone number, then saves.
# TODO


# 4. Biggest one: add an `export_csv(book, filename)` function that
#    writes all contacts to a CSV file using the csv module from Day 11,
#    with columns name, phone, email.
# TODO
