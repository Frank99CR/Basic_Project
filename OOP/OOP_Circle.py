import math

class circle:
    radius : int

    def __init__(self, radius):
        self.radius = radius

    def get_area (self, radius):
        Pi = math.pi
        area = Pi * radius ** 2
        print(f"The area of the circle is: {round(area, 2)} cm")

my_circle = circle(19)        
my_circle.get_area(19)