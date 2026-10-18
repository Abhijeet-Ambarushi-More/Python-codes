class Base:
    def __init__(self):     # python doesnt really consider __init__() method a constructor, here its a magic method
        print("Inside base constructor")

class Derived(Base):        
    def __init__(self):
        super().__init__()
        print("Inside derived constructor")

dobj = Derived()