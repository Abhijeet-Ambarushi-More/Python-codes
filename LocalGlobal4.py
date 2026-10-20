
no = 11     # Global variable

def Display():
    global no # As we have declared no global here, i will refer the global variable no
    no = 21  
    print("From Display",no)

print("Before : ",no)
Display()
print("After : ",no)