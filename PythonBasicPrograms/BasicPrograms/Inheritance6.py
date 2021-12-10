# To illustrate use of super() to call parent class method in child class

class parent:
    def m1(self):
        print("Parent class method")

class child(parent):
    def m2(self):
        print("Child class method")
        super().m1()  # calls parent class method

# create child class object

objb=child()
objb.m2()