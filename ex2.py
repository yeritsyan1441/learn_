import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def area(self):
        ...

    @abstractmethod
    def perimeter(self):
        ...


class Triangle(Shape):

    def __init__(self, a, b=None, c=None, /, *, h=None, alpha=None):
        if a and b and alpha and not c:
            c = (a ** 2 + b ** 2 - 2 * a * b * math.sin(math.radians(alpha))) ** 0.5
        if a and b and c:
            if not (a + b > c and a + c > b and b + c > a):
                raise ValueError('Invalid sides for triangle')
        self.a = a
        self.b = b
        self.c = c
        self.h = h
        self.alpha = alpha

    def area(self):
        if self.a and self.b and self.c:
            p = self.perimetr() / 2
            s = (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
            return s
        elif self.a and self.h:
            return self.a * self.h / 2

    def perimeter(self):
        if self.a and self.b and self.c:
            return self.a + self.b + self.c


class Circle(Shape):

    def __init__(self, r):
        if isinstance(r, int | float):
            self.r = r
        else:
            raise "Invalid parameter"

    def area(self):
        return (math.pi*self.r)**2

    def perimeter(self):
        return 2*math.pi*self.r


class Rectangle(Shape):

    def __init__(self, length, width):
        if isinstance(length, int | float) and isinstance(width, int | float):
            self.width = width
            self.length = length
        else:
            raise "Invalid parameters"

    def area(self):
        return self.length * self.width

    def perimeter(self):
        # P = (L + W) × 2
        return (self.width + self.length) * 2






