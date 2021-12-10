# operations on list and list methods

list1=list([10,20,40,80])
list2=list([1,2,3,4])

# Concatenate list1 and list2 (use of +)
list3= list1+list2
print(list3)

print("**********************")

# Repeate the list elements (use of *)
list4= list2 * 4  # repeates list2 4 times
print(list4)

print("**********************")
# Use of 'in' and 'not in'
print( 10 in list1) # returns True
print(10 not in list1) #returns False

print("**********************")
# use of functions len, min, max, sum

print(len(list1)) # retruns number of elements in list
print(min(list1)) # retruns minimum value element in list
print(max(list1)) # retruns maximum value element in list
print(sum(list1)) # returns sum of all value in list

print("**********************")
# list slicing to get sub list

list5= list1[0:2] # returns 2 element from list1 (element at index 0 and index 1) i.e 10, 20
print(list5)

list6=list1[:3]  # return element from index 0 to 2
print(list6)

list7=list1[1:] # retrun element from index 1 to last index
print(list7)