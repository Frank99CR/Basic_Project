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
    
    def calculate_perimeter(self, diametro):
        Pi = math.pi
        print(f"El diametro del circulo es: {round(Pi * diametro, 2)}cm")

    def calculate_area(self, diametro):
        radius = diametro / 2
        Pi = math.pi
        print(f"El area del cirdulo es: {round(Pi * radius ** 2, 2)}cm")

class Square(Shape):
    Longitud_lado : int

    def __init__(self, Longitud_lado):
        self.Longitud_lado = Longitud_lado

    def calculate_perimeter(self, Longitud_lado):
        perimeter = Longitud_lado * 4
        print(f"El perimetro del cuadrado es: {perimeter} cm")

    def calculate_area(self, Longitud_lado):
        area = Longitud_lado * Longitud_lado
        print(f"El area dle circulo es: {area} cm2")

class Rectangle(Shape):
    Longitud : int
    Ancho : int

    def __init__(self, Longitud, Ancho):
        self.Longitud = Longitud
        self.Ancho = Ancho
        
    def calculate_perimeter(self, Longitud, Ancho):
        Perimeter = Longitud + Ancho
        print(f"El perimetro del rectangulo es: {Perimeter * 2}cm ")

    def calculate_area(self, Longitud, Ancho):
        area_of_rectangle = Longitud * Ancho
        print(f"El area del rectangulo es: {area_of_rectangle}cm")
        pass


circulo = Circle(10)
#circulo.calculate_perimeter(10)
#circulo.calculate_area(10)

cuadrado = Square(8)
#cuadrado.calculate_perimeter(8)
#cuadrado.calculate_area(8)

rectangulo = Rectangle(10, 5)
#rectangulo.calculate_perimeter(10, 5)
rectangulo.calculate_area(10, 5)
