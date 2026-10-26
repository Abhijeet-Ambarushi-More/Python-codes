class Demo:
    # Class variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        # Instance variables
        self.No1 = 11
        self.No2 = 21

obj1 = Demo()
obj2 = Demo()

obj1.No1 = 0

print(obj1.No1) # 0 
print(obj2.No1) # 11

Demo.Value1 = 0

# this might behave abnormally...in python, not proper way to access, accessing class variable with object.classvariable , it will create new variable
# print(obj1.Value1) # 0 
# print(obj2.Value1) # 11

print(Demo.Value1)

# good practice
# call instance variable with self.variablename
# call class variable with class.variablename