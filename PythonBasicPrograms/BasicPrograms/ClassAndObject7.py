# To illustrate the class, object and constructor

class A:
    def __init__(self):  #  constructor
        print("Class A consructor")


# create object (constructor will be called automatically)

obja=A()  # constructor will be called


# constructor with arguments
print("*************************")
class B:
    def __init__(self,a,b):
        print("Class B constructor",a,b)

objb=B(10,20)

print("******************************88")
# convert local variables to class variable

class C:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        print("Class C constructor")



objc=C(5,5)
print(objc.x)  # class variable
print(objc.y) # class variable


print("*********************")
# call current class method in another method
class D:
    def fun1(self):
        print("Fun1")

    def fun2(self):
        print("Fun2")
        self.fun1()

# create object
objd=D()
objd.fun2()  # This will internally calls fun1 as well

print("****************************")
# Use of functions :  __str__ and __del__

class E:
    def disp(self):
        print("Display")

obje=E()
print(obje.__str__())  # Returns memory location of obje -__main__.E object at 0x0000021B96AEFD60

del obje

print("****************")
# Override __str__

class F:
    def __str__(self):
         return "This is __str__"
    def __del__(self):
        print("Object destroyed")

objf=F()
print(objf) # __str__ will be called automatically whenever we print reference variable
del objf    # __del__ will be called

