def CheckEven(No):
    if(No % 2) == 0:
        return True
        
    else:
        return False

def main():
    Value = int (input("Enter number : "))

    Ret = CheckEven(Value)

    if(Ret == True):
        print("Its an even number")
    else:
        print("Its an odd number")

if __name__ == "__main__":
    main()