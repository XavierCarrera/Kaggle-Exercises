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
