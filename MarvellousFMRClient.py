# Created our own fliter() , map(), reduce() functions

from MarvellousLibrary import filterX, mapX, reduceX

CheckEven = lambda No : (No % 2 == 0)
Increment = lambda No : No+1
Addition = lambda No1,No2 : No1 + No2


def main():
    Data = [13,12,8,10,11,20]

    print("Input data is : ",Data)

    FData = list(filterX(CheckEven,Data))    # dont put () after function name as it will be the call of that function
    print("Data after filter : ",FData) 

    MData = list(mapX(Increment,FData))
    print("Data after map : ",MData)

    RData = reduceX(Addition,MData)          # internally uses a Sum variable, like Sum = Sum + No
    print("Data after reduce : ",RData)


if __name__ == "__main__":
    main()