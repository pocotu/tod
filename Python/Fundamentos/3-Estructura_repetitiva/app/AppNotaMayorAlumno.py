'''Modificar el ejercicio anterior, considerando que en el colegio
hay N estudiantes, los que están codificados con números correlativos
de 1 a N; y que además de saber la nota mayor se desea saber qué
número de estudiante obtuvo esa nota.'''


# Leer el número de estudiantes de la promoción
N = int(input('Ingrese el número de estudiantes: '))
while ( N <= 0):
    N = int(input('Error. Ingrese el número de alumnos (N > 0): '))
# Leer las notas y determinar la nota mayor
K = 0
# Suponer que la nota mayor es cero
NotaMayor = 0
NroAlumnoNotaMayor = 0;
while K < N:
    # Incrementar el contador
    K += 1
    # Leer la nota del k-ésimo estudiante
    Nota = float(input('Ingrese la nota final del estudiante '+str(K)+': '))
    # --- Validar Nota
    while not (0<= Nota <= 20):
        Nota = int(input('Error. Ingrese una nota entre 0 y 20: '))
    # Si la actual nota mayor es menor que la nota leida, entoces corregir
    if NotaMayor < Nota:
        NotaMayor = Nota
        NroAlumnoNotaMayor = K
        
# Mostrar la nota mayor
print('la nota mayor es', NotaMayor, ' y corresponde al alumno ', NroAlumnoNotaMayor)
    
