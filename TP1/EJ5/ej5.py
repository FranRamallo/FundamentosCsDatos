def es_par(num):
    if num % 2 == 0: 
        return True
    else:
        return False

numero = float(input("Escriba un numero: "))
par = es_par(numero)

if par:
    print("El numero es par")
else: 
    print("El numero es impar")