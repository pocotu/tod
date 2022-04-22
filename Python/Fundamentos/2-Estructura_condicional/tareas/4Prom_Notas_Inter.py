'''
En un examen de suficiencia un postulante es evaluado por cinco jurados, 
cada jurado emite una nota de 0 a 100. 
Para determinar la nota final del postulante, 
se anula la nota más baja y la nota más alta, promediándose sólo las notas intermedias. 
Escribir un algoritmo que permita calcular la nota final del postulante.
'''

# Leer notas
Nota1 = int(input('Nota de jurado 1: '))
Nota2 = int(input('Nota de jurado 2: '))
Nota3 = int(input('Nota de jurado 3: '))
Nota4 = int(input('Nota de jurado 4: '))
Nota5 = int(input('Nota de jurado 5: '))

# Determinar las notas mas bajas
# Nota menor
NotaMenor = Nota1

if NotaMenor > Nota2:
    NotaMenor = Nota2
if NotaMenor > Nota3:
    NotaMenor = Nota3
if NotaMenor > Nota4:
    NotaMenor = Nota4
if NotaMenor > Nota5:
    NotaMenor = Nota5

# Nota mayor
NotaMayor = Nota1

if NotaMayor < Nota2:
    NotaMayor = Nota2
if NotaMayor < Nota3:
    NotaMayor = Nota3
if NotaMayor < Nota4:
    NotaMayor = Nota4
if NotaMayor < Nota5:
    NotaMayor = Nota5

# Determinando el promedio
SumaNotas = (Nota1 + Nota2 + Nota3 + Nota4 + Nota5)
Promedio = (SumaNotas - NotaMayor - NotaMenor)/3

# Mostrando promedio
print(f'El promedio es: {Promedio}')