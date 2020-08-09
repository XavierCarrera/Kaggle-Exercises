from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *

## 1

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    return len(zip_code) == 5 and zip_code.isdigit()

# Check your answer
q1.check()

