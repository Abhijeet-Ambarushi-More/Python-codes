def Area(Radius, PI):
    Ans  = PI * Radius * Radius
    return Ans

def main():
    Ret = Area(PI=3.14, Radius=10.5)        # even if you want to give one keyword then you have to give keywords for all
    print("Area of circle is : ",Ret)
    
if __name__ == "__main__":
    main()