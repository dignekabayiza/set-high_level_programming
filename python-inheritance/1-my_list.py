#!/usr/bin/python3
"""Defines a list class with a sorted printing method."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
