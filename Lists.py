from learntools.core import binder; binder.bind(globals())
from learntools.python.ex4 import *

## 1

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) < 2:
        return None
    return L[1]

# Check your answer
q1.check()

## 2

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

# Check your answer
q2.check()

## 3

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """

    x = racers[0]
    racers[0] = racers[-1]
    racers[-1] = x
    
# Check your answer
q3.check()

## 4

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

# Put your predictions in the list below. Lengths should contain 4 numbers, the
# first being the length of a, the second being the length of b and so on.
lengths = [len(a), len(b), len(c), len(d)]

# Check your answer
q4.check()

## 5

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    
    n = arrivals.index(name)
    print(n)
    return n >= len(arrivals) / 2 and n != len(arrivals) - 1
    
    

# Check your answer
q5.check()
