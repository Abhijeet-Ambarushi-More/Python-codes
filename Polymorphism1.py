class base:
    def fun(self):
        print("Inside base fun")

class derived(base):
    def fun(self):
        print("Inside derived fun")

dobj = derived()

dobj.fun()