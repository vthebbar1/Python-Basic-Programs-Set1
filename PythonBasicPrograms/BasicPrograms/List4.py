# To illustrate list

# Creation

list1 = [] # empty list
print(list1)

list2 = [10,20,"Raj","Ram"]
print(list2)

# Accessing list elements
print(list2[2])
print(list2[-1]) # Last element index is -1

# Add element to list
list2.append("True")
print(list2)

# insert element at specified index
list2.insert(0,"Ravi")
print(list2)

#Remove element at index 1
list2.pop(1)
print(list2)

# Removes last element
list2.pop()
print(list2)

# Removes given value
list2.remove("Raj")
print(list2)

# Reverse
list2.reverse()
print(list2)

print(list2.count("Ravi")) # Counts number of occurrences of a given value

# clears all elements in list
list2.clear()
print(list2)


list3 = [10,20,40,90,101,100,11]
print("List3=",list3)

#sort
list3.sort()
print("List3 sorted=", list3)

# delete at element
del list3[0]
print(list3)

# Find length
print(len(list3))

# delete entire list
del list3

print(list3)