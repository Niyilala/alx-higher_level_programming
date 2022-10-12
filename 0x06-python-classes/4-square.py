#!/usr/bin/python3
"""Defines a class Square based on private instance attribute"""


class Square:
    """Represents a new square."""
    def __init__(self, size=0):
        """Initialise a new square.
        args:
            size(int): size of the new aquare.
        """
        self.size = size

    @property
    def size(self):
        """get/set the value for the square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return (self.__size * self.__size)
