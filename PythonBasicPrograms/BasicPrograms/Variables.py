# To illustrate variables

# dynamically types
a=100
b=20.5

fname= "Vishwa"   # string can be in double quote
lname = 'Hebbar'  # string can also be in single quote

x=True
y=False

print(a)
print(b)
print(fname)
print(lname)
print(x)
print(y)

# Assign value to multiple variables in a single statement

m,n,o,p= 10,10.5, 'Vishwa',True
print(m,n,o,p)

# if multiple variables need to be assigned the same value

q=r=s=100
print(q,r,s)

# Swapping variables

t=100
u=200
print("Before swap")
print("t=",t)
print("u=", u)
t,u=u,t # swap
print("After swap")
print("t=",t)
print("u=", u)
