#!/usr/bin/python3
"""Module that defines a rectangle class based on BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a private width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle after validating its sides.

        Args:
            width (int): the width, must be a positive integer.
            height (int): the height, must be a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
