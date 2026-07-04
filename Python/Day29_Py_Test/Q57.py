# Create two mixin classes `Flyable` and `Swimmable`, each with one method. Create a `Duck` class that inherits from both, demonstrating multiple inheritance.

class Flyable:
    def fly(self):
        print("Flying")

class Swimmable:
    def swim(self):
        print("Swimming")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()