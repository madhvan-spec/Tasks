import math

class Shape:
    pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

   


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    
c1 = Circle(4)
r1 = Rectangle(4,5)
print(f"Area of Circle with radius {c1.radius}cm is {c1.area()}cm^2\n")
print(f"Perimeter of Circle with radius {c1.radius}cm is {c1.perimeter()}cm\n")

print(f"Area of Rectange with width {r1.width}cm and height {r1.height}cm is {r1.area()}cm^2\n")
print(f"Perimeter of Rectangle with width {r1.width}cm and {r1.height}cm is {r1.perimeter()}cm\n")