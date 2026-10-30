# 6 : 1 * 2 * 3 * 4 * 5 * 6
import time

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    
    return Fact

def main():
    value = int(input("Enter number : "))

    start_time = time.perf_counter()        # Changed time() to perf_counter ...this is more relable than time()
 
    Ret = Factorial(value)

    end_time = time.perf_counter()

    print(f"Factorial of {value} is {Ret}")

    print(f"Time required is : {end_time - start_time:.5f} seconds")    # :.5f  tells to show only 5 digits after decimal

if __name__ == "__main__":
    main()