'''
Escribir una aplicación para gestionar Carreras profesionales
'''

# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*****   CARRERAS PROFESIONALES   *****')
    print('1 Agregar')
    print('2 Buscar')    
    print('3 Modificar')
    print('4 Eliminar')
    print('5 Listar')
    print('6 FIN')

# -----------  Agregar  -------------
def Agregar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la Carrera Profesional: ')
    if Clave in D:
        print(Clave,' ya existe en la Base de datos')
    else:
        # -- Leer el valor
        Valor = input('Ingrese el nombre de la Carrera Profesional: ')
        # -- Agregar al diccionario
        D[Clave] = Valor

# -----------  Buscar  -------------
def Buscar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la Carrera Profesional: ')
    if Clave in D:
        print(Clave,' : ', D[Clave])
    else:
        print(Clave, 'No existe en la base de datos')

# -----------  Modificar  -------------
def Modificar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la Carrera Profesional: ')
    if Clave in D:
        # -- Mostrar el actual valor
        print(Clave,' tiene actualmente el valor de ',D[Clave])
        # -- Leer el valor
        Valor = input('Ingrese el nombre de la Carrera Profesional con el que desea cambiar: ')
        # -- Modificar el diccionario
        D[Clave] = Valor
    else:
        print(Clave, 'No existe en la base de datos')

# -----------  Eliminar  -------------
def Eliminar(D):
    # -- Leer el valor clave
    Clave = input('Ingrese el código de la Carrera Profesional: ')
    if Clave in D:
        del D[Clave]
    else:
        print(Clave, 'No existe en la base de datos')

# -----------  Listar  -------------
def Listar(D):
    # -- Listar los elementos del diccionario
    print()
    print('LOS ELEMENTOS DEL DICCIONARIO SON:')
    print('==================================')
    for K, V in D.items():
        print(K,'\t', V)

# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar el diccionario
D = {}
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 6:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Agregar(D)
    elif Opcion == 2:
        Buscar(D)
    elif Opcion == 3:
        Modificar(D)
    elif Opcion == 4:
        Eliminar(D)
    elif Opcion == 5:
        Listar(D)

