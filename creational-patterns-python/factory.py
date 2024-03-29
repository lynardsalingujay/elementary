""" Problem
    1. Uncertainties in types of objects
    2. decisions to be made at runtime regarding of what classes to use
"""

class Dog:
    """A simple dog class"""
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Awww"

class Cat:
    """A simple cat class"""
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"

def get_pet(pet="dog"):
    """The factory method"""
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

d = get_pet("dog")
c = get_pet("cat")

print(d.speak())
print(c.speak())
