from abc import ABC, abstractmethod
import math


class Figura(ABC):
    @abstractmethod
    def calcular_area(self):
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
  
        return math.pi * self.radio ** 2


class Rectangulo(Figura):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):

        return self.largo * self.ancho


def mostrar_area(figura: Figura):
    print(f"El área de la figura es: {figura.calcular_area():.2f}")


circulo = Circulo(5)
rectangulo = Rectangulo(4, 6)

mostrar_area(circulo) 
mostrar_area(rectangulo)  
