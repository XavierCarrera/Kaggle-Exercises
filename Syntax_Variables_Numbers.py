from learntools.core import binder; binder.bind(globals())
from learntools.python.ex1 import *

pi = 3.14159 # approximate
diameter = 3

## 1 

# Create a variable called 'radius' equal to half the diameter
____

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
____

radius = diameter / 2

area = pi * (radius **2)

# Check your answer
q1.check()

## 2

########### Setup code - don't touch this part ######################
# If you're curious, these are examples of lists. We'll talk about 
# them in depth a few lessons from now. For now, just know that they're
# yet another type of Python object, like int or float.
a = [1, 2, 3]
b = [3, 2, 1]
q2.store_original_ids()
######################################################################

# Your code goes here. Swap the values to which a and b refer.
# If you get stuck, you can always uncomment one or both of the lines in
# the next cell for a hint, or to peek at the solution.

c = a
d = b
a = d
b = c

######################################################################

# Check your answer
q2.check()

## 3

## Add parentheses to the following expression so that it evaluates to 1.

(5 - 3) // 2

## Add parentheses to the following expression so that it evaluates to 0

8 - (3 * 2) - (1 + 1)

## 4. 

# Alice, Bob and Carol have agreed to pool their Halloween candy and split it evenly among themselves. For the sake of their friendship, any candies left over will be smashed. For example, if they collectively bring home 91 candies, they'll take 30 each and smash 1.
# Write an arithmetic expression below to calculate how many candies they must smash for a given haul.

# Variables representing the number of candies collected by alice, bob, and carol
alice_candies = 121
bob_candies = 77
carol_candies = 109

# Your code goes here! Replace the right-hand side of this assignment with an expression
# involving alice_candies, bob_candies, and carol_candies
total_candies = alice_candies + bob_candies + carol_candies

to_smash = (total_candies % 3)

