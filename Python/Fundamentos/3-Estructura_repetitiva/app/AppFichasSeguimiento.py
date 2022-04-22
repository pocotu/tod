'''
Se tiene las fichas de seguimiento de los N estudiantes de la EPIIS,
para cada uno se tiene las M asignaturas cursadas con sus respectivas notas.
Escribir un algoritmo que determine:
- El número de asignaturas aprobadas por cada estudiante.
- El promedio de notas correspondiente a las asignaturas aprobadas por
  cada estudiante
'''
# -- Leer el número de estudiantes
NroAlumnos = int(input('Ingrese el número de estudiantes: '))
# -- Procesar la ficha de seguimiento de cada estudiante
for K in range(1, NroAlumnos+1):
    print()
    print('Procesando la información del estudiante ',K)
    # -- Inicializar contador y acumulador
    NroAsignaturasAprobadas = 0
    SumaNotasAprobadas = 0
    # -- Leer el número de asignaturas del K-ésimo estudiante
    NroAsignaturas = int(input('Ingrese el número de asignaturas: '))
    # -- Procesar las asignaturas del K-ésimo estudiante
    for I in range(1, NroAsignaturas+1):
        # -- Leer la nota de la I-ésima asignatura
        Nota = int(input('Ingrese nota de la asignatura '+str(I)+' : '))
        # -- Procesar la nota
        if Nota >= 14:
            NroAsignaturasAprobadas += 1
            SumaNotasAprobadas += Nota
    # -- Calcular el promedio de las notas aprobadas
    Promedio = SumaNotasAprobadas / NroAsignaturasAprobadas
    # -- Mostrar resultados
    print('Número de asignaturas aprobadas: ', NroAsignaturasAprobadas)
    print('Promedio: ', Promedio)
            
