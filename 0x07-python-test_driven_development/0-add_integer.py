#!/usr/bin/python3
"""function adding two integers"""

def add_integer(a, b=98):
    """arguments to add.
    a: One of the numbers, default not defined.
    b: The other number, default 98
    """
    if type(a) not in [int, float]:
        raise TypeError("a has to be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b has to be an integer")
    return int(a) + int(b)

