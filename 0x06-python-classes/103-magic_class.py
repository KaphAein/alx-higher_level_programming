#!/usr/bin/python3
"""Magic Class"""

import math


class MagicClass:
    """Represent Magic hehe"""
    def __init__(self, radius=0):
        """init calss magic"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """defines the area of a circle"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """defines the circumference of a circle"""
        return (2 * math.pi * self.__radius)
