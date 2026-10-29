def Addition(No1,No2):
    Ans = No1 + No2
    return Ans

def Substraction(No1, No2):
    Ans = No1 - No2
    return Ans


print("Enter first nuber : ")
Value1 = int(input())

print("Enter second nuber : ")
Value2 = int(input())

Ret = Addition(Value1, Value2)
print("Addition is : ",Ret)

Ret = Substraction(Value1, Value2)
print("Substraction is : ",Ret)

