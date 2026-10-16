def main():
    Ans = 0     # Ans baher kadla karan try madhe thevla asta tr tyacha scope fakt try madhe asla asta

    try:
        print("Enter first number : ")
        No1 = int(input())

        print("Enter first number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successful") # this line will be skipped if there is exception

    except Exception as eobj:               # Genereric Exception block(should always be at the bottom of all except blocks)
        print("Exception occured",eobj)


    print("Result is : ",Ans)


if __name__ == "__main__":
    main()

# in ExceptionDemo5 -
# we switch generic exception block to top , so specific exception blocks wont run, java will show syntax error for this
# this is the beauty of python
# we can remove other specific exceptions if we want

# if divide a number by zero we get
# ZeroDivisionError: division by zero
# ZeroDivisionError is the name of exception
# division by zero is the cause of exception

# if we enter character
# ValueError: invalid literal for int() with base 10: 'h'

# generic exception block handles all exceptions
# jar exception konta yenar te mahit nahit nahi tr generic lihayacha ani tyat je exceptin disel te varti lihayacha