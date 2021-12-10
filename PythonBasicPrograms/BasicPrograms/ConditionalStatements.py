# Program to illustrate the use of conditional statements

# example 1
x=20
if x>10:
    print("True")
else:
    print("False")


    # example 2
if True:              # if part will be executed, else will not be executed
    print("True condition")
else:
    print("False Confition")

# example 3

if False:          # else part will be executed, if part will not be executed
    print("True Condition")
else:
    print("False condition")

# example 4

if 1:           # 1 means True , if part will be executed, else will not be executed
    print("True condition")
else:
    print("False condition")

# example 5

if 0:       # 0  means False , else part will be executed, if part will not be executed
    print("True Condition")
else:
    print("False condition")


# program to find even or odd number

num=int(input("Input a number:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number")


# Write multiple statements under if else block
# example 1
if True:
    print("stmt1")
    print("stmt2")
    print("stmt3")
    print("stmt4")
else:
    print("stmt5")
    print("stmt6")
    print("stmt7")
    print("stmt8")
print("Outside of if else block")

# example 2
if False:
    print("stmt1")
    print("stmt2")
    print("stmt3")
    print("stmt4")
else:
    print("stmt5")
    print("stmt6")
    print("stmt7")
    print("stmt8")
print("Outside of if else block")

# Single line if else

print("Raj") if True else print("Kumar")  # prints Raj
print("Raj") if False else print("Kumar") # prints kumar

z=10
print("Grater") if z>1 else print("Less")
print("Greater") if z>11 else print("Less")



# print multiple statements in a single line using { }

{ print("Hey"),print("Kumar")} if True else { print("Welcome"), print("Raj")}
{ print("Hey"),print("Kumar")} if False else { print("Welcome"), print("Raj")}