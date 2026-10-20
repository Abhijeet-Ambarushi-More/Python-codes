
no = 11     # Global variable

def Display():
    no = 21     # as we have not declared global no...interpreter will create another local varable no..and print it as its nearest
    print("From Display",no)

print("Before : ",no)
Display()
print("After : ",no)