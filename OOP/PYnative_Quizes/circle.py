import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return self.radius * 2
    def circumference(self):
        return math.pi * self.radius * 2

a = float(input("Enter Radius: "))

x= Circle(a)

ar = x.area()
per = x.perimeter()
circ = x.circumference()

print("The perimeter is: ", per)
print("The area is: ", ar)
print("THe circumference is: ", circ)
