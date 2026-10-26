class Demo:
    # Class variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        # Instance variables
        self.No1 = 11
        self.No2 = 21

    # Instance method
    def fun(self):
        print("inside instance method named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)      # Demo.variablename is better practise than self.variablename
        print(Demo.Value2)

    @classmethod
    def gun(cls):
        print("inside class method named as gun")
        # print(Demo.No1)         # class method can not access instance variables using self.variablename or even class.variablename
        # print(Demo.No2)         # so not allowed
        print(cls.Value1)      
        print(cls.Value2)

    @staticmethod
    def sun():
        print("inside static method named as sun")
        print(Demo.Value1)      # We can access class variables from static method but its good practice to avoid it.
        print(Demo.Value2)

Demo.sun()      
