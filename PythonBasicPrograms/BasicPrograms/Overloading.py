# Overloading - calling same function with different number of parameters
# note - overloading in python is different from java or c++

# Method overloading

class A:
    def sum(self,a=None,b=None,c=None):
        s=0
        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s

a1=A()

# Overloading -> calling same method with different number of parameters
print(a1.sum())
print(a1.sum(10))
print(a1.sum(10,20))
print(a1.sum(10,20,30))
