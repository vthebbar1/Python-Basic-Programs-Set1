# Declare variables inside the class and use them inside method

class test:
    a,b=10,20
    def add(self):
        print("sum=", self.a+self.b)


obj1=test()
obj1.add()