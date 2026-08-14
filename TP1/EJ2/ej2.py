def suma(a, b):
    return a + b

def pedir_num():
    while True:
        try: 
            return float(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero")


num1 = pedir_num()
num2 = pedir_num()

res = suma(num1, num2)

print(f"Suma: {res}")