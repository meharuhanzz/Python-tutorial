"""Day 15 -- Capstone: a command-line Contact Book.

Pulls together everything from the previous 14 days:
  - classes & objects, inheritance-ready design    (Day 13, 14)
  - functions, *args-free clean interfaces          (Day 9)
  - dictionaries & lists                             (Day 6, 8)
  - file I/O + JSON, so contacts persist between runs (Day 10, 11)
  - exception handling, so bad input doesn't crash it (Day 12)
  - loops, conditionals, string formatting            (Day 3, 4, 5)

Run me with:  python3 main.py
"""
import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contacts.json")


class ContactNotFoundError(Exception):
    """Raised when looking up a contact that doesn't exist."""


class Contact:
    def __init__(self, name, phone, email=""):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {"name": self.name, "phone": self.phone, "email": self.email}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"], data.get("email", ""))

    def __str__(self):
        email_part = f", {self.email}" if self.email else ""
        return f"{self.name}: {self.phone}{email_part}"


class ContactBook:
    def __init__(self):
        self.contacts = []
        self.load()

    # ---- persistence ----
    def load(self):
        if not os.path.exists(DATA_FILE):
            self.contacts = []
            return
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            raw = json.load(f)
        self.contacts = [Contact.from_dict(d) for d in raw]

    def save(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump([c.to_dict() for c in self.contacts], f, ensure_ascii=False, indent=2)

    # ---- operations ----
    def add(self, name, phone, email=""):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.contacts.append(Contact(name.strip(), phone.strip(), email.strip()))
        self.save()

    def find(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        raise ContactNotFoundError(f"No contact named '{name}'")

    def search(self, query):
        query = query.lower()
        return [c for c in self.contacts if query in c.name.lower()]

    def delete(self, name):
        contact = self.find(name)   # raises ContactNotFoundError if missing
        self.contacts.remove(contact)
        self.save()

    def all_sorted(self):
        return sorted(self.contacts, key=lambda c: c.name.lower())


MENU = """
=== Contact Book ===
1. Add contact
2. View all contacts
3. Search contacts
4. Delete a contact
5. Exit
"""


def run(book, fake_inputs=None):
    """The interactive menu loop. fake_inputs lets us demo/test this
    without needing a real terminal -- see run_demo() below."""
    fake_iter = iter(fake_inputs) if fake_inputs is not None else None

    def ask(prompt):
        if fake_iter is not None:
            value = next(fake_iter, "5")   # default to "Exit" if we run out
            print(f"{prompt}{value}")
            return value
        return input(prompt)

    while True:
        print(MENU)
        choice = ask("Choose an option (1-5): ").strip()

        if choice == "1":
            name = ask("Name: ")
            phone = ask("Phone: ")
            email = ask("Email (optional): ")
            try:
                book.add(name, phone, email)
                print(f"Added {name}.")
            except ValueError as e:
                print(f"Couldn't add contact: {e}")

        elif choice == "2":
            contacts = book.all_sorted()
            if not contacts:
                print("No contacts yet.")
            for contact in contacts:
                print(f"  {contact}")

        elif choice == "3":
            query = ask("Search for: ")
            matches = book.search(query)
            if not matches:
                print("No matches.")
            for contact in matches:
                print(f"  {contact}")

        elif choice == "4":
            name = ask("Name to delete: ")
            try:
                book.delete(name)
                print(f"Deleted {name}.")
            except ContactNotFoundError as e:
                print(f"Couldn't delete: {e}")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Please choose 1-5.")


def run_demo():
    """Runs the whole app end-to-end with scripted input, so you can see
    exactly how it behaves without typing anything -- delete contacts.json
    afterwards to reset."""
    book = ContactBook()
    scripted_actions = [
        "1", "Ada Lovelace", "555-0100", "ada@example.com",
        "1", "Alan Turing", "555-0101", "",
        "2",
        "3", "ada",
        "4", "Alan Turing",
        "2",
        "5",
    ]
    run(book, fake_inputs=scripted_actions)


if __name__ == "__main__":
    run_demo()
    # To play with it for real instead of the scripted demo, comment out
    # run_demo() above and uncomment the two lines below:
    # book = ContactBook()
    # run(book)
