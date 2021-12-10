# Hierarchical inheritance (A -> B, C)

class A:
    def funa(self):
        print("Function A")

class B(A):
    def funb(self):
        print("Function B")
class C(A):
    def func(self):
        print("Function C")


# Create objects & call methods

obja=A()
objb=B()
objc=C()

obja.funa()

objb.funa()
objb.funb()

objc.funa()
objc.func()