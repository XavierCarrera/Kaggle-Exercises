from learntools.core import binder; binder.bind(globals())
from learntools.python.ex2 import *

## 1

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num, 2)

# Check your answer
q1.check()

## 2

# The help for round says that ndigits (the second argument) may be negative. What do you think will happen when it is? Try some examples in the following cell?
# Can you think of a case where this would be useful?

def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # ("pass" is a keyword that does literally nothing. We used it as a placeholder
    # because after we begin a code block, Python requires at least one line of code)
    return round(num, ndigits = -2)

# Check your answer
q1.check()

## 3

def to_smash(total_candies, friends=3):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    1
    """
    return total_candies % friends

# Check your answer
q3.check()