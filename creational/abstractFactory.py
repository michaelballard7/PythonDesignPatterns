
""" 

- THe abstract pattern is a pattern of factory of factories

- The goal of an abstract factory is to create families of related objects without depending on their specific classes

- Abstract Factory is used when you need to create a family of objects that do some work together.

- The benefit of using Abstract Factory is that it isolates the creation of objects from
the client that needs them, giving the client only the possibility of accessing them
through an interface, which makes the manipulation easier

 """


class Dog():

    def speak(self):    
        return "Woof"

    def __str__(self):
        return "Dog"


class DogFactory:
    """ Concrete Factory """

    def get_pet(self):
        """Returns a Dog object"""

    def get_food(self):
        """ Returns a Dog Food object """ 


class PetStore: 
    """ PetStore houses my abstract factory """

    def __init__(self, pet_factory= None):
        """ pet_factory is my abstract factory """

    def showPet(self):
        """ Utility method to display the details  of the objects  returned by the DogFactory"""