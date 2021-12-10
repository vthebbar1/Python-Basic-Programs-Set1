# To illustrate the use of *args
# *args is to represent variable number of argument

def sum(*args):
    Total=0
    for i in args:
        Total+=i
    print(Total)


sum(10) #  1 argument
sum(10,10) # 2 arguments
sum(10,10,10) # 3 arguments
sum(10,10,10,10) # 4 arguments