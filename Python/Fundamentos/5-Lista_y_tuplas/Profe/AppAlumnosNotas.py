'''
Escribir una aplicación para gestionar Alumnos
'''

# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

# -----------  Menu  -------------
def Menu():
    print(' *******  ALUMNOS  ******* ')
    print(' 1 -> Agregar alumno y notas')
    print(' 2 -> Mostrar alumnos y notas')
    print(' 3 -> Mostrar alumnos y promedios ')
    print(' 4 -> Fin ')
    print('')
# -----------  Agregar Alumno  -------------
def AgregarAlumno(DA):
    # -- Leer el código del Alumno
    Codigo = input('Ingrese el código: ')
    # -- Leer las notas del alumno
    Notas = []
    for K in range(1, 5):
        Nota = float(input('Ingrese nota '+str(K)+': '))
        Notas += [Nota]
    # -- Agregar al diccionario
    DA[Codigo] = Notas
        
# -------  Mostrar Alumnos y Notas  ---------
def MostrarAlumnosNotas(DA):
    # -- Mostrar alumnos y sus respectivas notas
    print('*** LISTADO DE ALUMNOS Y NOTAS ***')
    for Codigo, Notas in DA.items():
        print(Codigo, Notas)
    print('')

# -------  Mostrar Alumnos y promedios  ---------
def MostrarAlumnosPromedios(DA):
    # -- Mostrar alumnos y sus respectivas notas
    print('*** LISTADO DE ALUMNOS Y NOTAS ***')
    print('Código   ','Promedio')
    print('====================')
    for Codigo, Notas in DA.items():
        Suma = 0
       
        for Nota in Notas:
            Suma += Nota
        print(Codigo,'   ',Suma/len(Notas))
    print('')
        
# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar diccionario
DA = {}
# -- Mostrar y procesar Menú
Opcion = 0
while Opcion < 4:
    # -- Mostrar Menú
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción: '))
    # -- Procesar cada opcion del menu    
    if (Opcion == 1):
        AgregarAlumno(DA)
    elif (Opcion == 2):
        MostrarAlumnosNotas(DA)
    elif (Opcion == 3):
        MostrarAlumnosPromedios(DA)
    
