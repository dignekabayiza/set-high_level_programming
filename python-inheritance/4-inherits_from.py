#!/usr/bin/python3
"""Module that defines a function to check for a strict subclass."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    An instance of a_class itself does not count. Otherwise return False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
