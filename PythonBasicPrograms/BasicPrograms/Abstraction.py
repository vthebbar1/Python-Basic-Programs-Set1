# To illustrate abstraction
# ABC is a predefined abstract class

from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def fun1(self):
        None


class B(A):
    def fun1(self):
        print("Fun1 implementation")



# obj=A() -> Not valid, can not create object of abstract class

obj1=B()
obj1.fun1()