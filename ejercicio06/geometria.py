import math

class Figura:
    def __init__(self, id):
        self.id = id
    def area(self):
        pass
    def perimetro(self):
        pass
    def mostrar_datos(self):
        print("ID:", self.id)
        print("Área:", self.area())
        print("Perímetro:", self.perimetro())

class Rectangulo(Figura):
    def __init__(self, id, ancho, alto):
        super().__init__(id)
        self.ancho = ancho
        self.alto = alto
    def area(self):
        return self.ancho * self.alto
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(Figura):
    def __init__(self, id, lado1, lado2, lado3, altura):
        super().__init__(id)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.altura = altura
    def area(self):
        return (self.lado1 * self.altura) / 2
    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

class Circulo(Figura):
    def __init__(self, id, radio):
        super().__init__(id)
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def perimetro(self):
        return 2 * math.pi * self.radio