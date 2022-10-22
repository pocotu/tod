"""
Escribir un algoritmo para calcular el promedio
de 3 notas y luego determinar si el alumno esta 
aprobado o desaprobado
"""
# Crear algoritmo que calcule y determine si
# esta aprobado o desaprobado

# Leer notas
Nota1 = int(input("Ingrese la nota 1: "))
Nota2 = int(input("Ingrese la nota 2: "))
Nota3 = int(input("Ingrese la nota 3: "))

# calcular el promedio
Promedio = (Nota1 + Nota2 + Nota3)/3

# Determinar si esta aprobado o desaprobado
if Promedio >= 13.5:
    Mensaje = "Aprobado"
else:
    Mensaje = "Desaprobado"

# Escribir Aprobado o Desaprobado
print('Promedio =',Promedio,Mensaje)