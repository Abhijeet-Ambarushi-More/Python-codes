def Phoenix():
    print("Inside Phoenix")

    def Zara():
        print("Inside Zara")

def main():
    Phoenix()           # Allowed
    zara()              # Error
    Phoenix.Zara()      # Error
    
if __name__ == "__main__":
    main()