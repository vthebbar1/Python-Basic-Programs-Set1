# Creating multiple objects for a one class, Find the memory location of those objects, use  of 'is' and 'is not' operators

class test:
    def display(self):
        print("Disply function")


obj1=test()
obj2=test()
obj3=obj1

print("obj1 memory location=",id(obj1))
print("Obj2 memory location=",id(obj2))
print("Obj3 memory location=obj1 memory location=",id(obj3))


print(obj1 is obj2)  # False
print(obj1 is obj3) # True

print(obj1 is not obj2)  # True
print(obj1 is not obj3) # False
