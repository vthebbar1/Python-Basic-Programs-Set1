# program to illustrate type casting / type conversion

a=int(input("Key in integer:"))
b=float(input("Key in integer:"))  # integer can be stored in float variable
print(a+b)  # Numbers a and b will be added, output successful

# Example 2

c=int(input("Key in integer:"))
d=int(input("Input float/decimal:")) # int can not hold float value -ValueError: invalid literal for int() with base 10
print(c+d)

# example 3

e=input("Enter Number :")
f=input("Enter Decimal Number :")
print(int(e)+float(f))  # success - can add int and float , output will be float
