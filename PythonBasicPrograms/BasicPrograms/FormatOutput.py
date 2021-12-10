# Program to illustrate different ways of formatting/displaying output

name="Raj Kumar"
age=22
salary= 150000.55
# method 1 - only print values

print(name, age, salary)

# method 2 - print values with description

print("Name is:",name)
print("Age:", age)
print("Salary:",salary)

# method 3 - print using % - type of variable need to be taken to consideration

print("name:%s  Age:%d  Salary:%f" %(name, age, salary))

# method 4 - print using {}

print("Name {} Age {}, Salary {}".format(name, age, salary))

# method 5 - print using {index number}

print("Name: {0}  Age: {1} Salary: {2}".format(name,age, salary))  # index starts with 0