from learntools.core import binder; binder.bind(globals())
from learntools.python.ex3 import *

# 1 

# Your code goes here. Define a function called 'sign'

def sign(n):
    
    if n == 0:
        return 0
    elif n < 0:
        return - 1
    else:
        return 1
    

# Check your answer

q1.check()