import threading

def Display(No1, No2, No3):        # def Display (*No)..this is a variable argument
    print(f"Inside Display {No1}, {No2}, {No3}: {threading.get_ident()}")        # threadingget_ident will give TID i.e. unique thread identifier

def main():
    print(f"Inside Main : {threading.get_ident()}")

    tobj = threading.Thread(target=Display, args=(11, 21, 51,))     # correct Way to pass arguments to function called in thread

    tobj.start()                                # thread la kam suru karayala sangitala

if __name__ == "__main__":
    main()

# main thread is parent thread of tobj thread