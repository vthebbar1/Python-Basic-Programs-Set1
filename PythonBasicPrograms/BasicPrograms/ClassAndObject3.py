# To illustrate Local variables, Class Variables and Global variables

a,b=10,20 # a, b are global variables
class test:
    m,n=100,200     # m,n are class variables
    def add(self,x,y):  # x, y are local variables
        print("Sum of local variables=",x+y)
        print("Sum of class variables=", self.m+self.n)
        print("Sum of global variables=",a+b)


obj1=test()
obj1.add(40,60)