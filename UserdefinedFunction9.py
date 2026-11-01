def Phoenix():
    print("Inside Phoenix")

    def Zara():
        print("Inside Zara")

    Zara()              # Can not call Zara without calling Phoenix

def main():
    Phoenix()           # Allowed
    
    
if __name__ == "__main__":
    main()