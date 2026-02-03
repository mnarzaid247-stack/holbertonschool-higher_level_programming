#!/usr/bin/python3
"""creating a module"""


class Student:
    """creating a class"""
    def __init__(self, first_name, last_name, age):
        """creating a method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """creating a method"""
        if isinstance(attrs, list):
            new = {}
            for attr in attrs:
                new[attr] = self.__dict__[attr]
            return new
        return self.__dict__
