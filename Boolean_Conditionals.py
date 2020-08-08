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

# 2

def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    
    if total_candies > 1:
        print("Splitting", total_candies, "candies")
        return total_candies % 3
    else:
        print("There's only one candy")

to_smash(91)
to_smash(1)

