# ********************   LISTA DE LIBROS    *************************

# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*****   LIBROS   *****')
    print('1 Agregar')
    print('2 Consultar')    
    print('3 Eliminar')
    print('4 Listar por especialidad')
    print('5 Listar por año')
    print('6 Listar (General)')
    print('7 FIN')

# -----------  Módulo Posicion  -------------
def Posicion(Codigo, Lista):
    # -- Inicializar contadores
    P = -1
    I = 0
    # -- Buscar mientras no se haya encontrado el elemento y aún existan elementos por comparar
    while (P == -1) and (I < len(Lista)):
        if (Lista[I][0]== Codigo):
            # -- Si se encontró el elemnto, el índice es la posición del elemento en la lista
            P = I
        else:
            # -- Si no se encontró el elemento, incrementar el índice
            I += 1
    # Retornar posición
    return P
# -----------  Agregar  -------------
def Agregar(Lista):    
    # -- Leer el codigo del Libro
    CodLibro = input('Ingrese el código del Libro: ')
    if Posicion(CodLibro,Lista) >= 0:
        print('Código ya existe en la lista')
    else:
        # Ingresar la informacion del libro
        Titulo = input('Ingrese Título: ')
        Autor = input('Ingrese Autor: ')
        Anio = int(input('Ingrese año: '))
        Especialidad = input('Ingrese Especilidad: ')
        # Agregar a la lista
        Lista.append([CodLibro, Titulo, Autor, Anio, Especialidad])

# -----------  Consultar  -------------
def Consultar(Lista):
    # -- Leer el código del libro
    Codigo = input('Ingrese el código del Libro: ')
    P = Posicion(Codigo, Lista)
    if P >= 0:
        print(Lista[P])
    else:
        print(Codigo, ' no está en la lista')

# -----------  Eliminar  -------------
def Eliminar(Lista):
    # -- Leer el codigo del Libro
    Codigo = input('Ingrese el código del Libro: ')
    P = Posicion(Codigo, Lista)
    if P >= 0:
        del Lista[P]
    else:
        print(Codigo, ' no está en la lista')

# -----------  Listar por especialidad  -------------

# -----------  Listar por año  -------------

# -----------  Listar  -------------
def Listar(Lista):
    # -- Listar los Libros
    print()
    print("LISTADO DE LIBROS EN GENERAL")
    print("=======================================")
    print('Codigo'.ljust(6),'Titulo'.ljust(15),'Autor'.ljust(20),'Año'.ljust(5),'Especialidad')
    print('------\t---------------\t-------------\t------\t---------------')
    for L in Lista:        
        print(L[0].ljust(5),L[1].ljust(15),L[2].ljust(20),str(L[3]).rjust(5),L[4].ljust(15))

# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 7:
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
        ListarEspecialidad(Lista)
    elif Opcion == 5:
        ListarAnio(Lista)
    elif Opcion == 6:
        Listar(Lista)

