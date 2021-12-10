# program to illustrate the use of break and continue statements

print("*************Break at 6 **********")
for i in range(0,11,1):
    if i==6:
        break  # when i=6 control comes out of the loop
    print(i)

print("*************Break at 3 **********")
a=0
while a<=10:
    if a==3:
        break
    else:
        print(a)
        a=a+1


print("*************Skip printing 2 **********")
x=0
for x in range(0,10,1):
    if x==2:
        continue
    print(x)

print("**********Skip printing 5 *************")
z=0
while z<=10:
    if z==5:
        z=z+1
        continue
    else:
        print(z)
        z=z+1

