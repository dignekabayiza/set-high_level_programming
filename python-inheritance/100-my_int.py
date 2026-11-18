#!/usr/bin/python3
"""Defines a rebel integer class."""


class MyInt(int):
    """An int with the == and != operators inverted."""

    def __eq__(self, other):
        """Return True when the values are different."""
        return int.__ne__(self, other)

    def __ne__(self, other):
        """Return True when the values are equal."""
        return int.__eq__(self, other)
