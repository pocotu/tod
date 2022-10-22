'''Se tiene N estudiantes en la asignatura de F de P, para cada estudiante
se tiene tres notas.
Escribir un programa que calcule el promedio de cada estudiante'''

# Leer el número de estudiantes
NroAlumnos = int(input('Ingresa el número de estudiantes: '))

# Calcular el promedio de cada estudiante
K = 0
while K < NroAlumnos:
    # Incrementar contador
    K += 1  
    # Leer notas del K-ésimo alumno
    print('\nIngresa las notas del estudiante ', K)
    Nota1 = float(input('Nota 1: '))
    Nota2 = float(input('Nota 2: '))
    Nota3 = float(input('Nota 3: '))
    # Calcular el promedio
    Promedio = (Nota1 + Nota2 + Nota3) / 3
    # Mostrar el promedio
    print('El promedio del estudiante ',K,' es ', Promedio)
    
