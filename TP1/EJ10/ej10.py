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

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

cuadrado1 = Cuadrado(5)
cuadrado1.area()
cuadrado1.perimetro()

