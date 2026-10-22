import time
import threading

# 2+4+6+8 = 20
def SumEven(No):
    print("TID of SumEven thread is ",threading.get_ident())

# 1+3+5+7+9 = 25
def SumOdd(No):
    print("TID of SumOdd thread is ",threading.get_ident())

def main():
    print("TID of main thread is ",threading.get_ident())

    start_time = time.perf_counter()

    t1 = threading.Thread(target=SumEven,args=(10000000,))
    t2 = threading.Thread(target=SumOdd,args=(10000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    # join() does not "merge" two threads together. It also doesn't "stop" a thread.
    # It only pauses the calling thread (here, the main thread) until the target thread has finished.
    
    end_time = time.perf_counter()
    print(f"Time required is : {end_time - start_time:.4f}")

if __name__ == "__main__":
    main()
