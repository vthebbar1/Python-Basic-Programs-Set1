# To illustrate constructor in abstraction

from abc import ABC,abstractmethod
class A(ABC):
    def __init__(self,sum):
        self.sum=sum

    @abstractmethod
    def display1(self):
        pass

    @abstractmethod
    def display2(self):
        pass

class B(A):
    def display1(self):
        print("Implement display",self.sum)

    def display2(self):
        print("Implement display2",self.sum)

obj=B(10)
obj.display1()
obj.display2()
