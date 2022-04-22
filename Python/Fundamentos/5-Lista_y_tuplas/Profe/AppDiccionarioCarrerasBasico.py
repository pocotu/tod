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
    print('2 Listar')
    print('3 FIN')

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
while Opcion != 3:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Agregar(D)
    elif Opcion == 2:
        Listar(D)
    
