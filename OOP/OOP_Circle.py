import math

class Circle:
    radius : int

    def __init__(self, radius):
        self.radius = radius

    def get_area (self, radius):
        pi = math.pi
        area = pi * radius ** 2
        print(f"The area of the circle is: {round(area, 2)} cm")

my_circle = Circle(19)        
my_circle.get_area(19)