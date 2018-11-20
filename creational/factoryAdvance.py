from abc import ABCMeta, abstractmethod
import time 

class Platform(metaclass=ABCMeta):
    """ This is a base class with abstract methods

        Every supported platform will inherit from this base class
    
     """
    @abstractmethod
    def stop_systems(self):
        raise NotImplementedError('Please implement the method! <stop systems> ')

    @abstractmethod
    def start_systems(self):
        raise NotImplementedError('Please implement this method <start systems> ')

    @abstractmethod
    def systems_health_check(self):
        raise NotImplementedError('Please implement this method <system health check>')

class DatabaseConnectionScan(Platform):
    __node = ['MobileNodeA', 'MobileNodeB','MobileNodeC']
    def stop_systems(self):
        for system in self.__node:
            print("Stopping mobile system {}").format(system)
            time.sleep(0.7)
    
class WebServer(Platform):
    __node = ['WebNodeA', 'WebNodeB','WebNodeC']
    def stop_systems(self):
        for system in self.__node:
            print("Stopping systems {}").format(system)
            time.sleep(0.6)


class EquitiesScan(Platform):
    __node = ['MobileNodeA', 'MobileNodeB','MobileNodeC']
    def stop_systems(self):
        for system in self.__node:
            print("Stopping mobile system {}").format(system)
            time.sleep(0.7)


class PatchingFactory(object):
    def stop_all(self,platform_object):
        return eval(platform_object)().stop_systems()


PF = PatchingFactory()

platform_to_stop = input("Which platform would you like to stop?")

PF.stop_all(platform_to_stop)
