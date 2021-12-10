# program to find the memory location of string & illustrate strings are immutable

# 2 strings have same value, hence they will point to same memory location
str1="Raj"
str2="Raj"
print(id(str1))
print(id(str2))


str3="Kumar"
print(id(str3))

str3=str3+"Add"  # str3 is changed here, hence memory location will also change, hence strings are called immutable
print(id(str3)) # memory location printed will be different from line 11