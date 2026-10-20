
no = 11     # Global variable

def Display():
    a = 21      # Local variable
    print(" From Dislay : ",no)
    print(" From Dislay value of a : ",a)

def Demo():
    print(" From Demo : ",no)
    print("Value of a : ",a)        # Error

Display()
Demo()