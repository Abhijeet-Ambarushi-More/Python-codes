import sys

if(len(sys.argv) == 3):
    No1 = int(sys.argv[1])
    No2 = int(sys.argv[2])

    Ans = No1 + No2

    print("Addition is : ",Ans)

else:                                       # This is a validator not a filter
    print("Invalid number of arguments")