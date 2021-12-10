# program to read input from user

x=input("Key in value of x:")    # reads input as string
y= input("Key in value of y:")  # reads input as string

print(x+y) # Concatinates strings

# Need to perform type casting as given below to add 2 numbers

a=int(input("Key in value of a:"))  # reads input as string and converts to int
b=int(input("Key in value of b:"))  # reads input as string and converts to int
print(a+b)    # 2 number a, b will be added


# Another way to type cast
m=input("Enter value of m:")
n=input("Enter value of n:")

print(int(m)+int(n))