# To illustrate the use of local variables, Class Variables and Global Variables with SAME NAME

a,b=10,20  # Global variables
class test:
    a,b=30,40  # Class variables
    def add(self,a,b):   # Local variables
        print("Sum of local variables=", a+b)
        print("Sum of class variables=", self.a+self.b)
        print("Sum of Global variables=", globals()['a']+globals()['b'])

obj1=test()
obj1.add(4,6)
