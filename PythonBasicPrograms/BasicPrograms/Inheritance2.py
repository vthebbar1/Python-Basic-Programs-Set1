# To illustrate singe inheritance (1 parent class and 1 child class)

class Parent:
    a,b=1,2
    def display(self):
        print("a=", self.a,"b=", self.b)

class Child(Parent):
    c,d=3,4
    def display2(self):
        print("c=", self.c,"d=", self.d)


# create objects

p=Parent()
c=Child()

p.display()
c.display() # calling parent class method using child class object
c.display2()