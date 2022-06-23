def CalcularPromedios(N):
    # -- Verificar si hay alumnos
    if (N == 0):
        # retornamos 0, 0 porque no hay alumnos
        return 0, 0
    else:
        # -- Calcular los promedios de los N-1 primeros alumnos
        A, D = CalcularPromedios(N-1)
        # -- Leer notas, calcular el promedio del N-ésimo alumno y mostrar resultado
        print('Ingresar notas del alumno ',N)
        Nota1 = int(input('Nota 1: '))
        Nota2 = int(input('Nota 2: '))
        Nota3 = int(input('Nota 3: '))
        Promedio = (Nota1 + Nota2 + Nota3)/3
        print('Promedio: ',Promedio)
        # -- Acumular aprobados y desaprobados
        if Promedio >= 14:
            A += 1
        else:
            D += 1
        return A, D

print(CalcularPromedios(-5))