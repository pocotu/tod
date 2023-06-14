# ************* MÓDULOS ***************
def CalcularPromedios(N):
    # -- Verificar si hay alumnos
    if (N > 0):
        # -- Calcular los promedios de los N-1 primeros alumnos
        CalcularPromedios(N-1)#2
        # -- Leer notas, calcular el promedio del N-ésimo alumno y mostrar resultado
        print('Ingresar notas del alumno ',N)
        Nota1 = int(input('Nota 1: '))
        Nota2 = int(input('Nota 2: '))
        Nota3 = int(input('Nota 3: '))
        Promedio = (Nota1 + Nota2 + Nota3)/3
        print('Promedio: ',Promedio)
print(CalcularPromedios(5))
