# Return last value in list and tuple

print("Last value of List")
a=[1,2,3,4] # List
print(a[-1])

print("Last value of Tuple")
b=(1,2,3,4) # Tuple
print(b[-1])


# Access based on index
print("Accessing based on index")
print(a[3])


# Slicing
print("Slicing")
c=[10,20,30,40,50,60]
print(c[:4]) # 0 to 4
print(c[4:]) # index 4 to till end
print(c[0::2])  # start from index 0 till end, with step=2 i.e 0, 3, 5..

# convert list of integers to comma separated string
print("Convert integers to string")
print("Before")
print(c)
numbers=','.join(str(i) for i in c)
print("After")
print(numbers)

print("*************")
# Use of extend() and append()

p=[1,2,3,4]
q=['a','b']
r=[1,2,3,4]

print("Append result")
p.append(q)
print(p)

print("Extend Result")
r.extend(q)
print(r)


print("*****To reverse a list*******")

l1=[10,20,40,80]
print("Before reverse", l1)

r1 = list(reversed(l1))
print("After reverse", r1)


print("**********Dictionary********************")

dr={'raj':10,'bhim':20,'ram':30,'soni':40}

print("Access element based on key",dr['soni'])

print("Add element to dictionary")

dr['sam']=50
print(dr)

print("Modify dictionary element based on key -sam")
dr['sam']=100
print(dr)

print("Delete dictionary element based on key-sam")
del dr['sam']
print(dr)

print("Merge dictionaries using update()")
dr2={'priti':101,'gowri':102}
dr.update(dr2)
print(dr)

print("***walk through list in sorted order without sorting the actual list****")
l2=[100,90,10,20,101]
print("Original list", l2)
print("Sorted list")
print(sorted(l2))


print("***Using one line of code print all names starting with ‘a’ in below list.***")
names=['akash','raju','rani','arjun','akshu']
anames= [name for name in names if name[0]=='a']
print(anames)

print("***Write a code to find how many different characters are present in string****")

str1="This is a sample string"

print("List the unique characters in string")
print(set(str1))

print("Count of number of unique characters")
print(len(set(str1)))

print("**Generate Random Number between 0 to 1")
import random
print(random.random())

print(" Randomize list items in python ")

ls1 = [10,20,30,40,50]
print("Before randomize", ls1)
from random import shuffle # shuffle is a function in random module (predefined in python)
shuffle((ls1))
print("After randomize", ls1)

print("sorting  for numerical data set ")

ls2=["1","4","2","5"]
print("Before sort values in string", ls2)
ls2 =[int(i)  for i in ls2]    # converting list values to integer
print("After type conversion to integer", ls2)
ls2.sort()
print("After sorting",ls2)


print("**  current date and time ***")
import time
localtime1=time.asctime()
print(localtime1)

# can also use as below
localtime=time.asctime(time.localtime(time.time()))
print(localtime)

