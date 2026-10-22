import threading

def Display():
    print(f"Inside Display : {threading.get_ident()}")        # threadingget_ident will give TID i.e. unique thread identifier

def main():
    print(f"Inside Main : {threading.get_ident()}")

    tobj = threading.Thread(target=Display)     # tobj navachi navin thread tayar keli ani display function parameter mhnun dila

    tobj.start()                                # thread la kam suru karayala sangitala

if __name__ == "__main__":
    main()

# main thread is parent thread of tobj thread