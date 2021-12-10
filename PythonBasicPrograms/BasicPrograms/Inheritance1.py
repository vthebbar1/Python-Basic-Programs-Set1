# To illustrate inheritance

class A:
    def display(self):
        print("Class A display method")

class B(A):
    def display1(self):
        print("Class B display function")


obja=A() # Parent class object
objb=B() # child class object

obja.display()
objb.display()  # call parent class function using child class object
objb.display1()