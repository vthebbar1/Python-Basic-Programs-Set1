# To illustrate use of set {}

# set is unordered, un-indexed, duplicates not allowed

set1 ={"Raj","Raj", "Raj"}
print(set1)  # only one time Raj will be printed

employee_set = {"Raju","Ramu","Bhimu", "Somu", "motu","devi","raji"}
print(employee_set)

# Add single element to set
employee_set.add("Gowri")
print(employee_set)

# Adding multiple elements to set using list
employee_set.update([1,2,3,"bobby"])
print(employee_set)

# Removes element if present , else does nothing,
# we can use this if we are not sure whether element is present in set or not
employee_set.discard("motu")
print(employee_set)

# Removes element if present, else gives error
employee_set.remove("raji")
print(employee_set)

# using loop
print("********Looping through a set*******")
for x in employee_set:
    print(x)

employee_set.pop()  # Removes an arbitrary element from set
print(employee_set)

employee_set.clear() # Removes all elements from set
print(employee_set)

del employee_set
print(employee_set)