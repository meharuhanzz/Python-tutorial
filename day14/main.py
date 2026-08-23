"""Day 14 -- OOP II: Inheritance & Polymorphism.

Run me with:  python3 main.py
"""


# ---- 1. Basic inheritance ----
# A subclass ("child") inherits everything from its parent class, and can
# add or override behaviour. This lets you avoid duplicating code between
# closely related classes.
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def describe(self):
        print(f"{self.name} is an animal.")


class Dog(Animal):          # Dog inherits from Animal
    def speak(self):         # overriding the parent's speak()
        print(f"{self.name} says Woof!")


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")


print("=== Basic inheritance ===")
generic = Animal("Some Creature")
dog = Dog("Rex")
cat = Cat("Whiskers")

generic.speak()   # uses Animal's own speak()
dog.speak()        # uses Dog's overridden speak()
cat.speak()        # uses Cat's overridden speak()

# describe() was never overridden -- Dog and Cat both use Animal's version
dog.describe()
cat.describe()

# ---- 2. Polymorphism -- treating different types the same way ----
# This is the payoff of inheritance: you can loop over a mix of Dog and
# Cat objects and call .speak() on each, without caring which specific
# type each one is. Each object knows how to handle the call correctly.
print("\n=== Polymorphism ===")
animals = [Dog("Rex"), Cat("Whiskers"), Dog("Max"), Animal("Generic")]
for animal in animals:
    animal.speak()   # the CORRECT speak() runs for each one automatically


# ---- 3. super() -- calling the parent's version of a method ----
# Sometimes you want to EXTEND the parent's behaviour, not fully replace
# it. super() lets a subclass call its parent's method from inside its
# own override.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def describe(self):
        print(f"{self.name} earns {self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)   # let Employee set up name & salary
        self.team_size = team_size        # then add Manager's own extra bit

    def describe(self):
        super().describe()                # run Employee's describe() first...
        print(f"...and manages a team of {self.team_size}")   # ...then add more


print("\n=== super() ===")
mgr = Manager("Ada", 120000, team_size=5)
mgr.describe()


# ---- 4. A slightly bigger, realistic hierarchy ----
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        print(f"{type(self).__name__} with area {self.area():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


print("\n=== Shape hierarchy ===")
shapes = [Circle(5), Rectangle(4, 6), Circle(2)]
for shape in shapes:
    shape.describe()   # polymorphism again -- each shape computes its own area

total_area = sum(shape.area() for shape in shapes)
print(f"Total area: {total_area:.2f}")

# ---- 5. What happens if you try to instantiate the "abstract" base? ----
print("\n=== Deliberately-unimplemented base ===")
generic_shape = Shape()
try:
    generic_shape.area()
except NotImplementedError as e:
    print(f"failed as expected: {e}")
