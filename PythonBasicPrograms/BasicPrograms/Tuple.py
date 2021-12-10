# To illustrate the tuple creation

t1=() #empty tuple
print(t1)

t2=(1,2,3,4)
print(t2)



print("**************************")
# Tuple functions
print("Length of t2=",len(t2))
print("Sum of t2=",sum(t2))
print("min of t2=",min(t2))
print("max of t2=", max(t2))


print("**********************************")
# slicing tuple
print(t2[0:2])  # prints elements at index 0,1
print(t2[:4])  # index 0 to 3
print(t2[1:])  # index 1 to last

print("**********************************")
# 'in' and 'not in' operators
print(1 in t2) # True
print(1 not in t2)  # False


print("**********************************")
# Access tuple elements using for loop
t3=(10,20,40,90,100)
for i in t3:
    print(i, end=" ")  # to print all elements in same line use end=" "