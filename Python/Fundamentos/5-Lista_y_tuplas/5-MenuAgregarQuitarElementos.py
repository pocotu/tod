# **********************   MÓDULOS   ***************************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de operaciones con listas
    print()
    print('*****   OPERACIONES CON LISTAS   *****')
    print('1 Agregar')
    print('2 Insertar')    
    print('3 Eliminar')
    print('4 Listar')
    print('5 FIN')

# -----------  Agregar elemento a la lista  -------------
def Agregar(Lista):
    # -- Leer elemento
    Elemento = input('Ingresar elemento: ')
    # -- Agregar elemento a la lista
    return Lista + [Elemento]

# -----------  Insertar elemento a la lista  -------------
def Insertar(Lista):
    if (len(Lista)>0):
        # -- Leer elemento y Posicion
        Elemento = input('Ingresar elemento a Insertar: ')
        Pos = int(input('Ingresa Posicion: '))
        Lista = Lista[:Pos] + [Elemento] + Lista[Pos:]
        return Lista
    else:
        print('No hay elementos en la Lista...')

# -----------  Insertar elemento a la lista  -------------
def Eliminar(Lista):
    if (len(Lista)>0):
        # -- Leer elemento y Posicion
        Pos = int(input('Ingresa Posicion: '))
        return Lista[0:Pos]+ Lista[Pos+1:len(Lista)]
    else:
        return Lista

# -----------  Escribir Lista  -------------
def EscribirLista(Lista):
    print()
    # -- Escribir los elementos de la lista
    for Elemento in Lista:
        # -- Escribir el K-ésimo elemento de la lista
        print(Elemento)



    
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
        Lista = Agregar(Lista)        
    elif Opcion == 2:
        Lista = Insertar(Lista)
    elif Opcion == 3:
        Lista = Eliminar(Lista)
    elif Opcion == 4:
        EscribirLista(Lista)
