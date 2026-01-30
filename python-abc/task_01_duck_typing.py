#!/usr/bin/env python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """creating a class"""

    @abstractmethod
    def area(self):
        """creating a area"""
        pass

    @abstractmethod
    def perimeter(self):
        """creating a gitter"""
        pass


class Circle(Shape):
    """creating a class"""

    def __init__(self, radius):
        """creating a method"""
        self.radius = radius

    def area(self):
        """creating a area"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """creating a gitter"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """creating a class"""

    def __init__(self, width, height):
        """creating a mithod"""
        self.width = width
        self.height = height

    def area(self):
        """creating a area"""
        return self.width * self.height

    def perimeter(self):
        """creating a gitter"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """creating a mithod"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
