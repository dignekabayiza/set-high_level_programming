#!/usr/bin/python3
"""Module that defines a list class with a sorted print method."""


class MyList(list):
    """A list that can print itself in ascending order."""

    def print_sorted(self):
        """Print the list in ascending order without changing it."""
        print(sorted(self))
