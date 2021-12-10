# Python collection - Dictionary

# Creation

employee_dict = {"name": "Raj", "age":24, "Salary":100000.10, "email":"email@gmail.com", "Phone": 9876540981}

# print full dictionary
print(employee_dict)

# Access elements of dictionary
print(employee_dict["name"])
print(employee_dict.get("age"))

print("*************Loop1 output**************")
# Accessing in loop
for x in employee_dict:
    print(x)  # prints key
    print(employee_dict[x]) # prints value


print("*************Loop2 output**************")

for x,y in employee_dict.items():
    print("Key=",x," " ,"Value=", y)


# change/modify existing element

employee_dict["age"] = 25
print(employee_dict)

# Add new key, value
employee_dict["address"] = "1234, Maytwoer"
print(employee_dict)

# removing the key/value
employee_dict.pop("address")
print(employee_dict)

# Removes last element
employee_dict.popitem()
print(employee_dict)

# using del to remove key/value
del employee_dict["email"]
print(employee_dict)

# To clear all elements of dictionary

employee_dict.clear()
print(employee_dict)

# Delete the dictionary (memory location will be released)

del employee_dict

# print(employee_dict) -> This will throw error as entire dictionary is deleted from memory location
