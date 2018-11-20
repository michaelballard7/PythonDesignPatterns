"""
    The observer pattern is a behavioral pattern 

    This pattern is used to control the operation of some object

    This pattern allows me to define a one to many relationship between a set of objects

    This allows a state change in one object to notify all its dependent objects

    This is also known as the dependents pattern or the publish - suscribe pattern 


    Remember in python abstract classes may indeed have implementation
 """
from collections import namedtuple
from itertools import starmap
import abc

# create the abstract observer class 
class AbsObserver(object):

    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def update(self, value):
        pass

# create the abstract subject class
class AbsSubject(object): 
    __metaclass__ = abc.ABCMeta
    _observers = set()

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derived from AbsObserver')
        self._observers |= {observer}

    def detach(self, observer):
        self._observers -= {observer}

    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

# concrete subject class implementation
class KPIs(AbsSubject):
    _open_tickets = -1
    _closed_tickets = -1 
    _new_tickets = -1 

    @property
    def open_tickets(self):
        return self._open_tickets

    @property
    def closed_tickets(self):
        return self._closed_tickets

    @property
    def new_tickets(self):
        return self._new_tickets

    def set_KPIs(self, open_tickets, closed_tickets,new_tickets):
        self._open_tickets = open_tickets
        self._closed_tickets = closed_tickets
        self._new_tickets = new_tickets
        self.notify()

# concrete observer class implementation
class CurrentKPIs(AbsObserver):
    open_tickets = -1 
    closed_tickets = -1
    new_tickets = -1 

    def __init__(self, kpis):
        self._kpis = kpis
        kpis.attach(self)

    def update(self):
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets 
        self.display()

    def display(self):
        print('Current open tickets: {}'.format(self.open_tickets))
        print('New tickets in the last hour!: {}'.format(self.new_tickets))
        print('Tickets closed in the last hour: {}'.format(self.closed_tickets))
        print('*****\n')


    def theGreatestEver(self, hardworker="Michael"):
        print("The greatest ever is {}".format(hardworker))

data = (('new', 10),('open', 20), ('closed', 30))
nt = namedtuple('KPI', 'name value')
KPI_Data = starmap(nt, data)


# below are the main programs: 
""" Program 1 implementation """
for kpi in KPI_Data:
    if kpi.name == 'open':
        print('Current open tickets: %s ' %kpi.value)

    elif kpi.name == 'new':
        print("New tickets in last hour: %s" %kpi.value)

    elif kpi.name == "closed":
        print("Tickets closed in last hr: %s" %kpi.value) 


""" Program 2 refactored using observer pattern """
kpis = KPIs()
currentKPIs = CurrentKPIs(kpis)
# forecastKPIs = ForecastKPIS(kpis)
kpis.set_KPIs(26, 10, 3)
kpis.set_KPIs(30, 12, 3)
kpis.set_KPIs(40, 14, 5)
print('\n***Detaching currentKPIs observer ***\n\n')
kpis.detach(currentKPIs)
kpis.set_KPIs(150,100,103)
currentKPIs.theGreatestEver()