class Base:
    def __init__(self):     # python doesnt really consider __init__() method a constructor, here its a magic/Dunder method
        print("Inside Base constructor")

    def fun(self):
        print("Inside Base fun")

class Derived(Base):        
    def __init__(self):
        super().__init__()          # observe this is not super.__init__ 
        print("Inside Derived constructor")

dobj = Derived()

dobj.fun()