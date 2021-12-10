# Use Display1 and Display2 modules here

from Display1 import *
from Display2 import *

display1() # This will use the function from latest module imported
display2() # This will use the function from latest module imported

# If 2 module have same function, we can solve ambiguity by using import before calling function

print("***************")

from Display1 import*

display1()  # called from Display1 module
display2()  # called from Display2 Module


print("***************")

from Display2 import*
display1()  # called from Display2 module
display2()  # called from Display2 module