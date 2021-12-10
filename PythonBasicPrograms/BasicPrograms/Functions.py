# To illustrate the use of functions

# creating functions
def sum(a,b):
    print("Sum=",a+b)
sum(10,10)

print("******************")
# Function with return value

def sum1(c,d):
    return c+d

s1= sum1(10,10)
print("Sum=",s1)

print("******************")
# Skip the body of the function

def sum3(e,f):
    pass
print(sum3(10,10))  # it will return 'None' as there is no function body , Default retrun value for a function is None

print("********************")
# Local and Global variables

global_var=10

def sum4(g,h): # g, h are local variables
    print("Sum=",global_var+g+h)  # global variable can be used inside the fucntion

sum4(10,10)
# print(g,h) # Can not access local variables outside the function
print("Global variable=",global_var)


print("********************")
# Declaring glbal variable inside the function using 'global'

def sum5(i,j):
    global m  # global variable
    m=100
    print("Sum=",m+i+j)
sum5(10,10)
print("Global variable=", m)


print("*************************")

# Positional arguments

def disp1(name, age):
    print("name=",name,"age=",age)

disp1('raj',10)

print("*************************")

# Keyword arguments
def disp2(name, age, gender):
    print("Name=", name, "Age=", age, "Gender=",gender)

disp2(gender='Male',name='Kumar',age='10')  # order of arguments does not matter here

print("*************************")
# combination of position and keyword arguments
def disp3(name1, age1, gender1):
    print("Name=", name1, "Age=", age1, "Gender=", gender1)

disp3("Raju",gender1='Male', age1='22')     # we need to pass position arguments first , then keyword arguments

print("*************************")
# function with multiple return values

def func(a,b,c):
    return a,b,c

r=func(10,20,30)
print("Retrun values printed as tuble",r)  # multiple retrun values printed as tuple