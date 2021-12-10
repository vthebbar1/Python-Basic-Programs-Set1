# Using equality operators == and != to compare dictionaries

phone1={'raj':9999988888,'ram':8888899999}
phone2={'ram':8888899999,'raj':9999988888}

print(phone1==phone2)  # True ,  It compares key value pairs but order of elements does not matter

print(phone1!=phone2) # False

# iterating dictionary using for loop
for i in phone1:
    print(i,":",phone1[i])