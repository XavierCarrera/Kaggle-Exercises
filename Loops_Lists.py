from learntools.core import binder; binder.bind(globals())
from learntools.python.ex5 import *

## 1

def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    
    for num in nums:
        if num % 7 == 0:
            return True
        
    return False

# Check your answer
q1.check()

## 2

def elementwise_greater_than(L, thresh):
    """Return a list with the same length as L, where the value at index i is 
    True if L[i] is greater than thresh, and False otherwise.
    
    >>> elementwise_greater_than([1, 2, 3, 4], 2)
    [False, False, True, True]
    """
    x = []
    for i in L:
        x.append(i > thresh)
    return x

# Check your answer
q2.check()

## 3

def menu_is_boring(meals):
    """Given a list of meals served over some period of time, return True if the
    same meal has ever been served two days in a row, and False otherwise.
    """
    for i in range(len(meals)-1):
        if meals[i] == meals[i+1]:
            return True
    return False

# Check your answer
q3.check()

