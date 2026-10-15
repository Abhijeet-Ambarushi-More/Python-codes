def Area(Radius, PI = 3.14):        
    Ans  = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(10.5)                    # If we dont give parameter for the PI, it will cdr its default value
    print("Area of circle is : ",Ret)

    Ret = Area(10.5, 7.12)              # If we  give parameter for the PI, it will cdr the given value
    print("Area of circle is : ",Ret)
    
if __name__ == "__main__":
    main()