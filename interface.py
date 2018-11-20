""" Interfaces are create through abstract base classes in python """

import abc 


class MyABC(metaclass=abc.ABCMeta):
    """ Abstract base class definition """

    @abc.abstractmethod
    def do_something(self, value):
        """ Required Method """


    @abc.abstractproperty
    def some_property(self):
        """ Required Property """


    # implementation of my concrete class

    class MyClass(MyABC):
        """ Implementation of MyABC """

        def __init__(self, value=None):
            self._myprop = value 
        
        def do_something(self, value):
                self._myprop *= 2 + value
    
        @property
        def some_property(self):
                return self._myprop