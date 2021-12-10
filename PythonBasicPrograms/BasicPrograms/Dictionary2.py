# To illustrate the use of dictionary methods
phone={'raj':9876432090,'ram':9834500888,'bhim':8976089760,'shah':7689076890}

print(phone)

# Return and remove last item from dictionary
print(phone.popitem())
print(phone)
# Get keys as a tuple
print(phone.keys())

# Get the values as a tuple
print(phone.values())


# Return and remove item based on key
print(phone.pop('raj'))
print(phone)


# clear all items in dictionary
phone.clear()
print(phone)