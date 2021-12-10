# To illustrate encapsulation (Wrapping of variables and methods together)

class A:
    __i=10
    a=20
    def __fun1(self):
        print("Function 1-Private")
        print("Private variable=",self.__i)
    def fun2(self):
        print("Public function")
        print("Public variable=", self.a)
        self.__fun1()


# create object of class
obj=A()
# obj.__fun1() -> can not call proviate method outside class

obj.fun2() # This function in turn will call private function

print(A.a) # can call public variables

# print(A.__i) -> private variable __i can not use outside function