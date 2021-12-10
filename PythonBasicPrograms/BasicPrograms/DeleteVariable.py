# Program to illustrate the deletion of a variable

x=10
print(x)

del x  # variable delete

print(x)  # this line with throw error as variable is already deleted - NameError: name 'x' is not defined

