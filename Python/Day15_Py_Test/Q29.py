# Build a `Rectangle` class. Properties: `area`, `perimeter`. Methods: `scale(factor)` returns a new scaled Rectangle, `is_square()`, `can_fit(other)` checks if another Rectangle fits inside. Then a `Square` subclass that takes only one side argument. `Square(5).area` should work correctly.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.height + self.width)
    
    def scale(self, factor):
        return Rectangle(factor * self.width, factor * self.height)
    
    def is_square(self):
        return self.width == self.height
        
    def can_fit(self,other):
        if other.width <= self.width and other.height <= self.height:
            return True
        else:
            return False

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

rect1 = Rectangle(10, 5)
rect2 = Rectangle(12, 4)
sqr = Square(5)

print(f"Area of Rectange (with {rect1.width} unit width and {rect1.height} unit height): {rect1.area}")
print(f"Perimeter of Rectange (with {rect1.width} unit width and {rect1.height} unit height): {rect1.perimeter}")
print(f"Height of Rectangle (with {rect1.height} unit height) scaled by 6x: {rect1.scale(6).height}")
print(f"Width of Rectangle (with {rect1.width} unit width) scaled by 6x: {rect1.scale(6).width}")
print(f"Is this Rectangle actually Sqaure: {rect1.is_square()}")
print(f"Can Rectangle 1 (with {rect1.width} unit width and {rect1.height} unit height) fit Rectangle 2 (with {rect2.width} unit width and {rect2.height} unit height)?: {rect1.can_fit(rect2)}")
print(f"Area of Square (with {sqr.side} unit side): {sqr.area}")