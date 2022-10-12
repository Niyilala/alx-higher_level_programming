#!/usr/bin/python3
"""Defines a class Square based on private instance attribute"""


class Square:
    """Represents a new square."""
    def __init__(self, size):
        """Initialise a new square.
        args:
            size(int): size of the new aquare.
        """

        self.__size = size
