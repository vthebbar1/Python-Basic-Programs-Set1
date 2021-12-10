# To illustrate the tuple ()

tup1 =(10,"Raj",20.0,True)
print(tup1)

# Accessing elements in tuple
print(tup1[1])

# Assignment of value to tuple - NOT allowed -Immutable
# tup1[4] = "Ram"

print(tup1[-1])  # refers to last element

# slicing or accessing range of elements
print(tup1[1:3]) # elements at index 1,2 will be printed, element at index 3 is excluded

# Find length
print(len(tup1))

# Nested tuple - Tuple inside tuple and list inside tuple
tup2 =( 10,20,30,("Raj","Bhim","Ram"),[100,200,300])
print(tup2)
print(tup2[3]) # ('Raj', 'Bhim', 'Ram')
print(tup2[4]) # [100, 200, 300]

print(tup2[3][2]) # Ram
print(tup2[4][1]) # 200

# Modifying list inside the tuple - is allowed
tup2[4][2] ="New Value"
print(tup2)

print("**********")
# Looping the tuple
for x in tup2:
    print(x)