#!/usr/bin/python3
"""Module that defines an integer class with inverted comparisons."""


class MyInt(int):
    """An int that is a rebel: == and != are inverted."""

    def __eq__(self, other):
        """Return True when the values are different."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal."""
        return int.__eq__(self, other)

    __hash__ = int.__hash__
