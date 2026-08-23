"""Day 13 -- OOP I: Classes & Objects.

Run me with:  python3 main.py
"""


# ---- 1. Defining a class and creating objects from it ----
# A class is a blueprint. An object (or "instance") is a specific thing
# built from that blueprint. You've been using objects this whole course
# without necessarily calling them that -- a string, a list, a dict are
# all objects of the str/list/dict classes.
class Dog:
    def __init__(self, name, breed):
        # __init__ runs automatically when you create a new Dog.
        # "self" refers to THIS specific dog being created.
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")


print("=== Creating objects ===")
dog1 = Dog("Rex", "Labrador")
dog2 = Dog("Bella", "Poodle")

print(f"dog1.name = {dog1.name}, dog1.breed = {dog1.breed}")
print(f"dog2.name = {dog2.name}, dog2.breed = {dog2.breed}")

dog1.bark()
dog2.bark()

# Each object has its own separate copy of the attributes -- changing
# dog1's name doesn't affect dog2:
dog1.name = "Max"
print(f"\nafter renaming: dog1.name = {dog1.name}, dog2.name = {dog2.name}")


# ---- 2. Methods that use and change an object's state ----
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


print("\n=== A stateful object ===")
account = BankAccount("Ada", balance=100)
account.deposit(50)
account.withdraw(30)
account.withdraw(1000)   # should fail gracefully
print(f"Final balance: {account.balance}")


# ---- 3. A "dunder" method: __str__, for nice printing ----
# By default, printing an object gives you something ugly like
# <__main__.Dog object at 0x...>. Defining __str__ controls what
# print(my_object) and str(my_object) actually show.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance_from_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5


print("\n=== __str__ and computed methods ===")
p = Point(3, 4)
print(p)   # uses __str__ automatically
print(f"distance from origin: {p.distance_from_origin()}")


# ---- 4. Class attributes vs instance attributes ----
# A class attribute is shared by ALL instances. An instance attribute
# (set via self.x = ...) belongs to just one object.
class Employee:
    company_name = "Acme Corp"   # class attribute -- same for everyone

    def __init__(self, name, salary):
        self.name = name          # instance attribute -- unique per object
        self.salary = salary


print("\n=== Class vs instance attributes ===")
e1 = Employee("Ada", 90000)
e2 = Employee("Alan", 95000)
print(f"{e1.name} works at {e1.company_name}")
print(f"{e2.name} works at {e2.company_name}")

# Changing the class attribute changes it for everyone who hasn't
# overridden it on their own instance:
Employee.company_name = "Acme International"
print(f"after rename: {e1.name} works at {e1.company_name}")


# ---- 5. A slightly bigger example, pulling several ideas together ----
class Library:
    def __init__(self):
        self.books = []   # each Library instance gets its own empty list

    def add_book(self, title):
        self.books.append(title)
        print(f"Added '{title}'")

    def list_books(self):
        if not self.books:
            print("The library is empty.")
            return
        for i, title in enumerate(self.books, start=1):
            print(f"  {i}. {title}")


print("\n=== A Library of books ===")
lib = Library()
lib.add_book("Automating the Analytical Engine")
lib.add_book("Computing Machinery and Intelligence")
lib.list_books()
