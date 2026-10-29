import os

print("PID of current process is : ",os.getpid())
print("PID of parent process is : ",os.getppid())   

# Here parent process is command prompt
# There is parent-child relationship of cmd and python programs
# tasklist for windows, ps for linux