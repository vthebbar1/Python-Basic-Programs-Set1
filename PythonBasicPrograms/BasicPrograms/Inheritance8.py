# To illustrate use of super() to call parent class variables in child class (Same variable names)

a,b=4,6

class parent:
    a,b=10,12


class child(parent):
    a,b=16,18

    def display(self,a,b):
        print("Local variable values=", a,b)
        print("Global variable values=",globals()['a'], globals()['b'])
        print("Parent class variable values=",super().a, super().b)
        print("child class variable values=", self.a, self.b)


# child class object
objc= child()

objc.display(8,8)