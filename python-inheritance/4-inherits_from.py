#!/usr/bin/python3
"""Defines a function that checks for strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but not of a_class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
