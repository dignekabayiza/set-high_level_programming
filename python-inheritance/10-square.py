#!/usr/bin/python3
"""Module that defines a square class based on Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a private size."""

    def __init__(self, size):
        """Initialize a square after validating its size.

        Args:
            size (int): the side length, must be a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
