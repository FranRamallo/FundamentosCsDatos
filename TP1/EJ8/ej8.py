def palindromo(cadena):
    esPalindromo = True
    contador = len(cadena)-1
    while esPalindromo and contador>=0:
        if cadena[contador] != cadena[len(cadena)-1-contador]:
            esPalindromo = False
        contador -= 1
    return esPalindromo

pal = input("Ingrese una cadena: ")
esPal = palindromo(pal)
if esPal: 
    print("Es palindromo")
else: 
    print("No es palindromo")
