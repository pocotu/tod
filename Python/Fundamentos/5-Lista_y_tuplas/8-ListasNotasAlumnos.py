'''
Se tiene una relación de N alumnos. Para cada uno de ellos se tiene 3 notas.
Escribir una aplicación que permita registrar en una lista dicha información,
luego, que muestre la relación de alumnos, con sus respectivas notas y el promedio.
'''

# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*****   ALUMNOS   *****')
    print('1 Agregar')
    print('2 Consultar')    
    print('3 Eliminar')
    print('4 Listar')
    print('5 FIN')

# -----------  Módulo Posicion  -------------
def Posicion(Codigo, Lista):
    # -- Inicializar contadores
    P = -1
    I = 0
    # -- Buscar mientras no se haya encontrado el elemento y aún existan elementos por comparar
    while (P == -1) and (I < len(Lista)):
        if (Lista[I][0] == Codigo):
            # -- Si se encontró el elemnto, el índice es la posición del elemento en la lista
            P = I
        else:
            # -- Si no se encontró el elemento, incrementar el índice
            I += 1
    # Retornar posición
    return P

# -----------  Módulo Agregar  -------------
def Agregar(Lista):    
    # -- Leer el codigo del alumno
    CodAlumno = input('Ingrese el código del alumno: ')
    if Posicion(CodAlumno,Lista) >= 0:
        print('Código ya existe en la lista')
    else:
        # Ingresar las notas
        Nota1 = int(input('Ingrese Nota1: '))
        Nota2 = int(input('Ingrese Nota2: '))
        Nota3 = int(input('Ingrese Nota3: '))
        # Agregar a la lista
        Lista.append([CodAlumno, Nota1, Nota2, Nota3])

# -----------  Consultar  -------------
def Consultar(Lista):
    # -- Leer el valor del Codigo
    Codigo = input('Ingrese el código del alumno: ')
    P = Posicion(Codigo, Lista)
    print('***', P)
    if P >= 0:
        print(Lista[P])
    else:
        print(Codigo, ' no está en la lista')

# -----------  Eliminar  -------------
def Eliminar(Lista):
    # -- Leer el codigo del alumno
    Codigo = input('Ingrese el código del alumno: ')
    P = Posicion(Codigo, Lista)
    if P >= 0:
        del Lista[P]
    else:
        print(Codigo, ' no está en la lista')

# -----------  Listar  -------------
def Listar(Lista):
    # -- Listar los alumnos
    print()
    print("LISTADO DE ALUMNOS")
    print("==================")
    print('Codigo\tNota1\tNota2\tNota3\tPromedio')
    print('------\t-----\t-----\t-----\t--------')
    for A in Lista:
        Prom = (A[1] + A[2] + A[3])/3
        print(A[0], '\t', A[1], '\t', A[2], '\t', A[3], '\t', Prom)

# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 5:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Agregar(Lista)
    elif Opcion == 2:
        Consultar(Lista)
    elif Opcion == 3:
        Eliminar(Lista)
    elif Opcion == 4:
        Listar(Lista)
    