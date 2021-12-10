# To know the version of python

import sys
print(sys.version)


# for-else

a=[1,2,3,4]
for i in a:
    print("Inside for")
else:
    print("Inside else")

print("*************")
# while-else
j=0
while j<4:
    print("Inside while")
    j+=1
else:
    print("Inside else")

print("******ind number of references pointing to a particular object********")

x="Raj"
y=x
print(sys.getrefcount(x))
del x


print("****** use fo range() ********")
k=range(1,10)
print(type(k))
print(k)
for i in k:
    print(i)