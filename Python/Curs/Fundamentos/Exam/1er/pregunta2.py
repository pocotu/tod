'''
El docente de la asignatura de Fundamentos de Programación, luego de haber tomado el primer examen, 
ofrecio bonificar a la nota del examen con un puntaje obtenido bajo los sgtes criterios:
 - Si no hay ninguna nota mayor a 18 se bonificará con 1 punto.
 - Si el número de aprobados es menor que el número de desarpobados, se bonificará con 1 punto mas.
 - Si el promedio de la clase es menor a 9, se bonificará con 2 ptos mas.
 Escribir un algoritmo que determine el número de puntos de bonificación para cada alumno.
'''

# Leer el número de estudiantes
NroAlumnos = int(input('Ingrese el número de estudiantes: '))

# Procesando la nota de cada alumno
for K in range(1, NroAlumnos+1):
    # Inicializar contador y acumulador
    NroAlumnosAprobados = 0
    SumaNotas = 0
    # Leer la nota de la I-ésimo alumno
    Nota = int(input('Ingrese nota del alumno '+str(K)+' : '))
    # Procesar la nota
    NroAlumnosAprobados += 1
    SumaNotas += Nota

    Promedio = SumaNotas / NroAlumnos
    
    # Mostrar resultados
    print('Número de alumnos aprobados: ', NroAlumnosAprobados)
    print('Promedio: ', Promedio)
    
