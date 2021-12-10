# program to illustrate the use of loops - for and while

# prints values from 0 to 9
for i in range(10):   # if only one value is given, then by default start value=0 and increment rage =1
    print(i)

print("*********************")
# print even numbers from 0 to 10
for i in range(0,11,2):
    print(i)

print("*********************")
# print odd numbers from 0 to 10
for i in range(1,11,2):
    print(i)

print("*********************")

# print numbers from 10 to 0
for i in range(10,-1,-1):
    print(i)
print("*********************")

# print numbers from -1 to -10
for i in range(-1, -11, -1):
    print(i)

print("**********While Loop***********")
# print values from 0 to 10
i=0
while i<=10:
    print(i)
    i=i+1

print("2nd while loop")
# print values from 10 to -10
i=10
while i>=-10:
    print(i)
    i=i-1


