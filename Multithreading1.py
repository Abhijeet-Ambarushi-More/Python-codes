import threading

def Display():
    print(f"Inside Display : {threading.get_ident()}")        # threading.get_ident will give TID i.e. unique thread identifier

def main():
    print(f"Inside Main : {threading.get_ident()}")
    Display()

if __name__ == "__main__":
    main()