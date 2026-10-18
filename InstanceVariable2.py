class Marvellous:
    # Class variables
    No1 = 11
    No2 = 12
    
    def __init__(self):
        #Instance variables
        self.Value1 = 21
        self.Value2 = 51

print(Marvellous.No1)       # can access this before creating object as its already there
print(Marvellous.No1)

# Object / Instance creation
mobj1 = Marvellous()
mobj2 = Marvellous()
mobj3 = Marvellous()
mobj4 = Marvellous()

print(mobj1.Value1)
print(mobj2.Value1)


#  prev languages       Python

# static variable ->    class variable
# instance variable ->  instance variable

# In python, we must always write __innit__ method i.e. constructor to create any variable in object (compulsory)
# constructor is not mandatory in previous languages