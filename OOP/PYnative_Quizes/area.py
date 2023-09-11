import math 

class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

    def calculate_perimeter(self):
        return math.pi * 2 * self.radius

class Triangle(Shape):
    def __init__(self, base, height, side1, side2, side3):
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self):
        return (0.5 * self.base * self.height)

    def calculate_perimeter(self):
        return self.base + self.side1 + self.side2 + self.side3

class Rectangle(Shape):
    def __init__(self, height, width):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return (self.width * 2) + (self.height * 2)

#CIRCLE
rad = float(input("Enter Radius of the circle: "))

circle = Circle(rad)
per = circle.calculate_perimeter()
ar = circle.calculate_area()

print("The area of circle is: ", ar)
print("The perimeter of circle is: ", per)

#TRIANGLE
b = float(input("Enter triangle base: "))
h = float(input("Enter triangle height: "))
s1 = float(input("Enter side1 of triangle: "))
s2 = float(input("Enter side2 of triangle: "))
s3 = float(input("Enter side3 of triangle: "))

triangle= Triangle(b,h, s1, s2, s3)
peri = triangle.calculate_perimeter()
are = triangle.calculate_area()

print("Area of triangle: ", are)
print("Perimeter of triangle: ", peri)

#RECTANGLE
h = float(input("Enter Height: "))
w = float(input("Enter Width: "))

rect = Rectangle(h, w)

perim = rect.calculate_perimeter()
arre = rect.calculate_area()

print("The area of rectangle is: ", arre)
print("The perimeter of rectangle is: ", perim)
