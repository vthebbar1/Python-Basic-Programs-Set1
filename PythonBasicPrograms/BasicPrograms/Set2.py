# set illustration and mathematical operations

# converting lis to set
list1 =[1,2,3,3,"Raj"]
print("Original list:",list1)

print("List to set")
s = set(list1)
print(s)

print("Set to List")
# converting set to list
l = list(s)
print(l)

print("************Mathematical operations**************")

set1 ={1,2,3,"Raj","Ram"}
set2 = {3,4,5,"Ram","Bhim"}

print("Set1=", set1)
print("set2=", set2)

# union
print("Union")
print(set1.union(set2))
print(set1 | set2)

print("Intersection")
# intersection
print(set1.intersection(set2))
print(set1 & set2)

# Difference
print("Difference set1-set2")
print(set1.difference(set2))
print(set1 - set2)

# Difference
print("Difference set2-set1")
print(set2.difference(set1))
print(set2 - set1)

# Symmetric difference -> elements which are not common in both sets
print("Symmetric difference")
print(set1.symmetric_difference(set2))
print(set1 ^ set2)