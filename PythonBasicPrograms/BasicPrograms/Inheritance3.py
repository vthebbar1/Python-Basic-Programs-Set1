# Multi level inheritance (A->B->C)

class A:
    def funa(self):
        print("Function A")
class B(A):
    def funb(self):
        print("Function B")
class C(B):
    def func(self):
        print("Function C")

# object creation

obja=A()
objb=B()
objc=C()


objc.funa() # calling parent class method using child class object
objc.funb() # calling parent class method using child class object
objc.func()