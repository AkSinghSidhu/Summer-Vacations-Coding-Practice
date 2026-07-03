# Build a small polymorphism demo — a list of different shape objects (Circle, Rectangle, Square), loop through calling `.area()` on each without knowing the specific type ahead of time.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError("Arguments must be numbers")
        if radius <= 0:
            raise ValueError("Arguments must be positive")
        
        self.radius = radius
        
    def area(self):
        return pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
            raise TypeError("Arguments must be numbers")
        if width <= 0 or height <= 0:
            raise ValueError("Arguments must be positive")
        
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height        
    
class Square(Shape):
    def __init__(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError("Arguments must be numbers")
        if side <= 0:
            raise ValueError("Arguments must be positive")
        
        self.side = side

    def area(self):
        return self.side * self.side
    
shapes = [Circle(4), Rectangle(3,7), Square(2), Circle(6), Rectangle(7,8)]

for shape in shapes:
    print(shape.area())