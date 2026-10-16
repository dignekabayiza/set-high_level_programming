#!/usr/bin/python3
"""0-add_integer module.

Adds two integers.
Floats are cast to integers.
"""


def add_integer(a, b=98):
    """Return the sum of a and b as integers.
    a and b must be integers or floats, else TypeError is raised.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
