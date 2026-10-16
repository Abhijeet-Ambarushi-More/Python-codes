def Addition(No1, No2):     # NO1 and No2 can accept int,float etc any datatype
    Ans = No1 + No2
    return Ans

def main():
    print("Enter first number : ")
    Value1 = int(input())

    print("Enter second number : ")
    Value2 = int(input())           # Run hotana value la kalnar ki tyacha datatype kay ahe

    Ret = Addition(Value1, Value2)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()