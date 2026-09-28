#!/usr/bin/python3
"""Module that defines LockedClass."""


class LockedClass:
    """Only allows the instance attribute first_name."""
    __slots__ = ["first_name"]
