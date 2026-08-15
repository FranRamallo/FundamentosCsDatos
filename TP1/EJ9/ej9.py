class Rectangulo:

    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        area = self.ancho * self.alto
        print(f"El area es: {area}")

    def perimetro(self):
        per = 2*self.ancho + 2*self.alto
        print(f"El perimetro es {per}")

rectangulo1 = Rectangulo(5,6)
rectangulo1.area()
rectangulo1.perimetro()

