class Arithmatic:
    def Addition(No1, No2):
        Ans = No1 + No2
        return Ans

    def Substraction(No1, No2):
        Ans = No1 - No2
        return Ans
    
Aobj = Arithmatic()

print("Enter first nuber : ")
Value1 = int(input())

print("Enter second nuber : ")
Value2 = int(input())

Ret = Aobj.Addition(Value1, Value2)         # Issue / Error
print("Addition is : ",Ret) 

Ret = Aobj.Substraction(Value1, Value2)     # Issue / Error
print("Substraction is : ",Ret)

# we are giving 3 parameters as(aobj, Value1, Value2) but Aobj.Addition() takes only two