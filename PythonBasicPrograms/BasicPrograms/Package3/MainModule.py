# To illustrate the use of packages in python (Here we use modules from Package1, Package11 and Package2)
# Importing modules from different packages

# Method 1
import sys
sys.path.append("C:/Users/user/PycharmProjects/pythonBasics/PythonBasicPrograms/BasicPrograms/Package1")
import Module1
Module1.show1()

sys.path.append("C:/Users/user/PycharmProjects/pythonBasics/PythonBasicPrograms/BasicPrograms/Package1/Package11")
import Module11
Module11.show11()

sys.path.append("C:/Users/user/PycharmProjects/pythonBasics/PythonBasicPrograms/BasicPrograms/Package2")
import Module2
Module2.show2()

print("****************")

# method 2
from Module1 import *
from Module11 import*
from Module2 import *

show1()
show11()
show2()

print("************")
# Using class in module 2
obj=cal()
obj.add(10,10)