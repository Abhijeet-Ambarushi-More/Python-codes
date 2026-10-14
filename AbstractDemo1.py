from abc import ABC, abstractmethod     # abc- module ....ABC - Abstract Base Class, 
            
class Base(ABC):        # if a class has abstract method and you want to use @abstractmethod decorator,then it must inherit ABC class
    @abstractmethod
    def Addition(self,No1,No2):
        pass            # as there are no curly brackets, we need to write pass to declare a empty function

class Derived(Base):
    pass

dobj = Derived()        # Error