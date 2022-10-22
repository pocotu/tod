'''
Se tiene N Alumnos en el curso de F de programacion,
para cada estudiante se tiene 3 notas. Escribir un algoritmo que
calcule el promedio de cada estudiante
'''

# Leer el numero de estudiantes
NroAlumnos = int(input('Ingresa el numero de estudiantes'))

# Calcular el promedio de cada estudiante
k=0
while k < NroAlumnos:
    # Incrementar contador
    k = k + 1
    # Leer notas de k-esimo alumno
    print('\nIngresa las notas del estudiante',k)
    Nota1 = float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    Nota3 = float(input('Nota 3: '))
    # Calcular promedio
    Promedio = (Nota1 + Nota2 + Nota3)/3
    #Mostrar el promedio
    print('El promedio del estudiante',k,'es',Promedio)