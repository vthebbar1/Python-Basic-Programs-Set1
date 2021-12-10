# Use Bank1 and Bank2 modules here

from Bank1 import *
from Bank2 import *

obj1=B1()
obj2=B2()

obj1.rate_of_interest()
obj1.acct_balance()

print("**************")

obj2.rate_of_interest()
obj2.acct_balance()