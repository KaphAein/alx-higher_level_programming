#!/usr/bin/python3
"""Rectangle module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class"""
    def __init__(self, width, height):
        """Rectangle instantiation"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """area method"""
        return self.__width * self.__height

    def __str__(self):
        """str method"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
