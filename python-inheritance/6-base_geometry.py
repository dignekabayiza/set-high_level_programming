#!/usr/bin/python3
"""Defines a geometry base class with an unimplemented area method."""


class BaseGeometry:
    """A base class for geometry shapes."""

    def area(self):
        """Raise an Exception: area is not implemented."""
        raise Exception("area() is not implemented")
