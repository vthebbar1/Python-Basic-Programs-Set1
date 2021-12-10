# To illustrate instance method and static method

class test:
    def add(self,a,b):  # Instance method
        print("Sum=",a+b)

    @staticmethod
    def display():              # static method
        print("Static method display")


# we can call static method without creating object of class
test.display()


# Calling instance without creating object of class
test.add(0,10,20)

obj1=test()
obj1.add(10,50) # call instance method using object
