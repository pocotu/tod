"""
Se tiene 4 notas. Escribir un algoritmo para calcular el promedio
de las tres notas mas altas y determinar si el alumno es aprobado,
desaprobado o reprobado
"""

# Calcular el promedio de 3 notas mas altas
# Leer notas
print('Ingresa cada nota:')
Nota1 = float(input('Nota 1: '))
Nota2 = float(input('Nota 2: '))
Nota3 = float(input('Nota 3: '))
Nota4 = float(input('Nota 4: '))

# Determinar la nota mas baja
NotaMenor = Nota1
if NotaMenor > Nota2:
    NotaMenor = Nota2
if NotaMenor > Nota3:
    NotaMenor = Nota3
if NotaMenor > Nota4:
    NotaMenor = Nota4

# Calcular promedio
Promedio = (Nota1 + Nota2 + Nota3 + Nota4 - NotaMenor)/3

# Determinar si es un promedio aprobado, desaprobado o reprobado
if Promedio >= 13.5:
    Mensaje = 'APROBADO'
else:
    if Promedio >= 8.5:
        Mensaje = 'DESAPROBADO'
    else:
        Mensaje = 'REPROBADO'

# Escribir el promedio y el mensaje
print('Promedio =',Promedio,Mensaje)