def Display(*Data):
    print(Data)
    print(type(Data))

def main():
   Display(10,45.89,False,"Python")     #this can accept any number of elements

if __name__ == "__main__":
    main()