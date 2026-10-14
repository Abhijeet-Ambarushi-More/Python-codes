from abc import ABC, abstractmethod     # abc- module ....ABC - Abstract Base Class, 
            
class Base(ABC):        # if a class has abstract method and you want to use @abstractmethod decorator,then it must inherit ABC class
    @abstractmethod
    def Addition(self,No1,No2):
        pass            # as there are no curly brackets, we need to write pass to declare a empty function

class Derived(Base):
    def Addition(self,No1,No2):
        return No1+No2

dobj = Derived()
Ret = dobj.Addition(10,11)

print("Addition is : ",Ret)