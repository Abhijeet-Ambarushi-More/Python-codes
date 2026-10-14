class Demo:
    def __init__(self):             # self is like this pointer or this referance from other languages
        print("Inside Constructor")

    def __del__(self):
        print("Inside Destructor")

obj1 = Demo()
obj2 = Demo()

print("end of application")

# constructor name should always be __init__()...not like other languages where it should be same like class name