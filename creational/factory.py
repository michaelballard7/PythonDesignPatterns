
""" 

An implementation of the factory pattern

A factory is an object that specializes in creating other objects

The factory pattern allows me to create an object without exposing the creation logic to the client

Usually this class has methods that accept some parameters and returns some type of object depending on the parameters passed.

The Factory class can reuse existing objects, while direct instantiation always creates a new object

"""

class Dog:

    def __init__(self, name):
        self._name = name 


    def speak(self):
        return "Woof"

class Cat:

    def __init__(self, name):
        self._name = name 

    def speak(self):
        return "Meow"

# this is my factory function:
def get_pet(pet="dog"):

    pets= dict(dog = Dog("Hope"), cat=Cat("Lina"))

    return pets[pet]

d = get_pet("dog")

c = get_pet("cat")

print(c.speak())

print(d.speak())