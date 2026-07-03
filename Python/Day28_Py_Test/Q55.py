# Using the `abc` module, create an abstract base class `Shape` with an abstract method `area()`. Create `Circle` and `Rectangle` subclasses that implement it. Show what happens if you try to instantiate `Shape` directly.

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self, *args):
        if len(args) == 0:
            raise ValueError("At least one number is required.")

        for num in args:
            if not isinstance(num, (int, float)):
                raise TypeError("All arguments must be integers or floats.")

        for num in args:
            if num < 0:
                raise ValueError("Negative numbers are not allowed.")
        
        return args

class Circle(Shape):
    def area(self, *args):
        validated_arg = super().area(*args)
        num = validated_arg[0]
        return pi * (num ** 2)
    
class Rectangle(Shape):
    def area(self, *args):
        if len(args) < 2:
            raise ValueError("Rectangle needs 2 arguments")
        validated_args = super().area(*args)
        num1 = validated_args[0]
        num2 = validated_args[1]
        
        return num1 * num2
    
try:
    shape = Shape()
except TypeError as e:
    print(f"Cannot instantiate Shape directly: {e}")

circle = Circle()
rectangle = Rectangle()

print(f"Area of Circle with 5 unit radius is: {circle.area(5)}")
print(f"Area of Rectangle with 5 unit length and 7 unit breadth is: {rectangle.area(5,7)}")