estudiantes = {"Tomi": 9.0, "Dani" : 8, "Ale" : 8}

suma_notas = sum(estudiantes.values())
cant_estudiantes = len(estudiantes)
promedio = suma_notas / cant_estudiantes

print(f"El promedio de las notas es: {promedio}")