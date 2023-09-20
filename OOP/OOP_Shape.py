from abc import ABC, abstractmethod
import math

class Shape (ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass
    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    diametro : int

    def __init__(self, diametro):
        self.diametro = diametro
    
    def calculate_perimeter(self):
        Pi = math.pi
        print(f"El diametro del circulo es: {round(Pi * self.diametro, 2)}cm")

    def calculate_area(self):
        radius = self.diametro / 2
        Pi = math.pi
        print(f"El area del cirdulo es: {round(Pi * radius ** 2, 2)}cm")

class Square(Shape):
    longitud_lado : int

    def __init__(self, longitud_lado):
        self.longitud_lado = longitud_lado

    def calculate_perimeter(self):
        perimeter = self.longitud_lado * 4
        print(f"El perimetro del cuadrado es: {perimeter} cm")

    def calculate_area(self):
        area = self.longitud_lado * self.longitud_lado
        print(f"El area dle circulo es: {area} cm2")

class Rectangle(Shape):
    longitud : int
    ancho : int

    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho
        
    def calculate_perimeter(self):
        Perimeter = self.longitud + self.ancho
        print(f"El perimetro del rectangulo es: {Perimeter * 2}cm ")

    def calculate_area(self):
        area_of_rectangle = self.longitud * self.ancho
        print(f"El area del rectangulo es: {area_of_rectangle} cm")
        pass


circulo = Circle(10)
circulo.calculate_perimeter()
circulo.calculate_area()

cuadrado = Square(8)
cuadrado.calculate_perimeter()
cuadrado.calculate_area()

rectangulo = Rectangle(10, 5)
rectangulo.calculate_perimeter()
rectangulo.calculate_area()
