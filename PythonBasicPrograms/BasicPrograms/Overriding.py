# Method overriding - Same function in parent and child class (with same number and type of parameters)

class Parent:
    def display(self):
        print("Display in Parent")

class Child(Parent):
    def display(self):
        print("Display in Child")


p=Parent()
c=Child()
p.display() # Calls Parent display function
c.display() # Calls Child display function
