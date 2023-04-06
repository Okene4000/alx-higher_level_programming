#!/usr/bin/python3
"""function that adds two numbers"""

def add_integer(a, b=98):
    """ The function adds two integer or float numbers or both integers and floats
        a: first number, b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
