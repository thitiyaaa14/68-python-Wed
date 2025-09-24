class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.hieght = height

    def area(self):
        return self.width * self.hieght

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 

    def area(self):
        import math
        return math.pi * (self.redius ** 2)

shapes = [Rectangle(10, 20), Circle(5)]

for shape in shapes:
    print(f"Area : {shape.area()}")
