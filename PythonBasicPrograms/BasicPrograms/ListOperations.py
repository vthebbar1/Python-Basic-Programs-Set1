list1=[10,40,80,10,20,10]

print(list1.count(10)) # print number of occurences of 10 in list1

list1.append(108)  # append 108 to list1
print(list1)

print(list1.index(80)) # return index of 80

list2=[1,2,3,4]

list1.extend(list2) # appends list2 to list1
print(list1)

list1.insert(0, 101) # inserts 101 at index o
print(list1)

list1.sort() # sort in ascending order
print(list1)

list1.reverse() # reverse the list1
print(list1)

list1.pop(1)  # removes element at index 1
print(list1)

# List comprehension
list3= [x for x in range(10)]  # creates list with numbers from 0 to 9
print(list3)

list4=[x for x in range(10) if x%2==0]   # creates list of EVEN numbers from 0 to 9
print(list4)