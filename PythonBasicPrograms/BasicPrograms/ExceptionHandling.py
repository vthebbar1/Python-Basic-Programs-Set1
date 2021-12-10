# To illustrate exception handling

print("Program started")
a= float(input("Key in Numerator:"))
b=float(input("Key in Denominator:"))

try:
    result= (a/b)
    print("Result=",result)
except ZeroDivisionError as ex:
    print("Exception handling - Divide by Zero:-", ex)
else:
    print("Else Block- execute if no except block is executed")

finally:
    print("Finally block")

print("Program completed")

