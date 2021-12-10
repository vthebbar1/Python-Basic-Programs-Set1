# To illustrate the use of kwargs
# passing **kwargs while calling function
def display(a,b,c):
    print(a,b,c)

d={'a':10, 'b':20, 'c':30}

display(**d)


# Using **kwargs in function definition

def display1(**kwargs):
    for i,j in kwargs.items():
        print(i,j)

display1(name='raj', age=20, phone=99999999)