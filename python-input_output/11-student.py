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
                if attr in self.__dict__:
                    new[attr] = self.__dict__[attr]
            return new
        return self.__dict__

    def reload_from_json(self, json):
        """creating a method"""
        for key, value in json.items():
            setattr(self, key, value)
