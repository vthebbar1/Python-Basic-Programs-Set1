# Multiple Inheritance (A,B ->C)

class A:
    def funa(self):
        print("Function A")
class B:
    def funb(self):
        print("Function B")
class C(A,B):
    def func(self):
        print("Function C")

# create objects

obja=A()
objb=B()
objc=C()

objc.funa() # calling parent class method using child class object
objc.funb() # calling parent class method using child class object
objc.func() # Calling Child class method using child class object

