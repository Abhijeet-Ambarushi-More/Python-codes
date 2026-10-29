def CheckEven(No):
    if(No % 2) == 0:
        print("Its an even number")
    else:
        print("Its an odd number")

def main():
    Value = int (input("Enter number : "))

    CheckEven(Value)

if __name__ == "__main__":
    main()