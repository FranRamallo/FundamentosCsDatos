import math

def pedir_radio():
    while True:
        try: 
            return int(input("Radio: "))
        except ValueError:
            print("El radio debe ser un numero")

r = pedir_radio()
area = math.pi * (r ** 2)

print(f"El area del circulo es: {area}")