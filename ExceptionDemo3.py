def main():
    Ans = 0     # Ans baher kadla karan try madhe thevla asta tr tyacha scope fakt try madhe asla asta

    try:
        print("Enter first number : ")
        No1 = int(input())

        print("Enter first number : ")
        No2 = int(input())

        Ans = No1 / No2

        print("Division is successful") # this line will be skipped if there is exception

    except ZeroDivisionError as zobj:
        print("Exception occured due to second operand is zero : ",zobj)    # pvm ne he kagadavar lihla, kagad mhnje zobj

    except ValueError as vobj:
        print("Exception occured due to Invalid datatype : ",vobj)      # printing vobj will print "invalid literal for int() with base 10: 'h'"

    print("Result is : ",Ans)


if __name__ == "__main__":
    main()

# if divide a number by zero we get
# ZeroDivisionError: division by zero
# ZeroDivisionError is the name of exception
# division by zero is the cause of exception

# if we enter character
# ValueError: invalid literal for int() with base 10: 'h'