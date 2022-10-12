#!/usr/bin/python3
"""Defines a class Square based on private instance attribute"""


class Square:
    """Represents a new square."""
    def __init__(self, size=0):
        """Initialise a new square.
        args:
            size(int): size of the new aquare.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
