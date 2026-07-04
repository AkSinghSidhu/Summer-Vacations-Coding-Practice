# Create a small diamond inheritance scenario (two classes inheriting from the same base, one class inheriting from both of those). Print `ClassName.__mro__` to see the order Python resolves it in.

class Animal:
    def animal(self):
        print("Is animal")

class Live_birth(Animal):
    def live_birth(self):
        print("Gives live birth")

class Fly(Animal):
    def fly(self):
        print("Can Fly")

class Bat(Live_birth, Fly):
    pass

print(Bat.__mro__)