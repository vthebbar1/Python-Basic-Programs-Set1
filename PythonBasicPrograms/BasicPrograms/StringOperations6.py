# Use of  comparison operators with the string >, <, >=, <=, ==, !=
# Python compares string lexicographically i.e using ASCII value of the characters.

str1="Raj"
str2="Raj"
str3="Kumar"

print(str1>str3) # True
print(str1==str2) # True
print(str1 > str2) # False
print(str1 >= str2) # True
print(str1 <= str2) # True
print(str1!=str2) # False
print(str1<str2) # False