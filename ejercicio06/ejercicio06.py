import geometria
circulo1 = geometria.Circulo(1, 3)
rectangulo1 = geometria.Rectangulo(2, 10, 4)
triangulo1 = geometria.Triangulo(3, 5, 5, 5, 4.33)

figuras = [circulo1, rectangulo1, triangulo1]

for figura in figuras:
    figura.mostrar_datos()
    print("")
    