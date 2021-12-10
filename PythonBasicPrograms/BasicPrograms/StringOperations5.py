# Use of 'in' and 'not in' operators in string

str1="RajKuamr"
str2="Raj"

a= str2 in str1  # Returns True, because str2 is found in str1
print(a)

b=str2 not in str1 # Returns False
print(b)

c= "abc" in str1 # Reurns False
print(c)

d= "abc" not in str1 # retruns True
print(d)