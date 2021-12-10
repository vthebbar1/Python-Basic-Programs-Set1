# To illustrate use of super() to call parent class constructor

class parent:
    def __init__(self):
        print("Parent class Constructor")


class child(parent):
    def __init__(self):
        print("Child class constructor")
        super().__init__()

        parent.__init__(self) # another way of calling parent class constructor

# child class object
objc= child()  # it will child class constructor , which in turn will call parent class constructor