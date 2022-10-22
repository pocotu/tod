'''El índice de masa corporal (IMC) es un número que se calcula en función al peso y la
estatura de la persona. Para la mayoría de las personas, el IMC es un indicador confiable
de la gordura y se usa para identificar las categorías de peso que pueden llevar a
problemas de salud. La siguiente tabla resume estos indicadores.'''
# **********************   MÓDULOS   ***************************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de operaciones con listas
    print()
    print('*****   OPERACIONES CON LISTAS   *****')
    print('1 Agregar IMC')  
    print('2 Eliminar IMC')
    print('3 Número de personas en cada clase del IMC')
    print('4 Porcentaje de cada clase del IMC')
    print('5 generar una lista con los IMC de una determinada clase')
    print('6 SALIR')
def subMenu():
    # -- Mostrar el menú de operaciones con listas
    print()
    print('ingrese la clase que desea')
    print('1 normal')  
    print('2 sobrepeso')
    print('3 obesidadgrado 1')
    print('4 obesidad grado 2')
    print('5 obesidad grado 3')
# -----------  Agregar elemento a la lista  -------------
def Agregar(Lista):
    # -- Leer elemento
    Elemento = int(input('Ingresar elemento: '))
    # -- Agregar elemento a la lista
    return Lista + [Elemento]


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
def numeropersonas(lista):
    clase1=0
    clase2=0
    clase3=0
    clase4=0
    clase5=0
    for DF in lista:
        if (DF>=18.5) and (DF<=24.9):
            clase1=clase1+1
        elif (DF>=25) and (DF<=29.9):
            clase2=clase2+1
        elif (DF>=30) and (DF<=34.9):
            clase3=clase3+1
        elif (DF>=35) and (DF<=39.9):
            clase4=clase4+1
        elif (DF>=40):
            clase5=clase5+1
    return clase1,clase2,clase3,clase4,clase5
# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
Lista = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 6:
    # -- Mostrar menu
    Menu()
    Lista = [25.5,31.8,18.8,22.0,24.1,27.3,41.1,17.8,38.2,23.0,21.5,20.4,32.5]
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        Lista = Agregar(Lista)        
    elif Opcion == 2:
        Lista = Eliminar(Lista)
    elif Opcion == 3:
        normal,sobre,obe1,obe2,obe3=numeropersonas(Lista)
        print('IMC normal')
        print(normal)
        print('IMC sobrepeso')
        print(sobre)
        print('obesidad grado 1')
        print(obe1)
        print('obesidad grado 2')
        print(obe2)
        print('obesidad grado 3')
        print(obe3)
    elif Opcion == 4:
        normal,sobre,obe1,obe2,obe3=numeropersonas(Lista)
        print('IMC normal')
        print(normal*100/(normal+sobre+obe1+obe2+obe3),'%')
        print('IMC sobrepeso')
        print(sobre*100/(normal+sobre+obe1+obe2+obe3),'%')
        print('obesidad grado 1')
        print(obe1*100/(normal+sobre+obe1+obe2+obe3),'%')
        print('obesidad grado 2')
        print(obe2*100/(normal+sobre+obe1+obe2+obe3),'%')
        print('obesidad grado 3')
        print(obe3*100/(normal+sobre+obe1+obe2+obe3),'%')
    elif Opcion == 5:
        subMenu()
        clase = int(input('Ingrese opción --> '))
        normal,sobre,obe1,obe2,obe3=numeropersonas(Lista)
        if clase==1:
            print('IMC normal')
            print(normal)
        elif clase==2:
            print('IMC sobrepeso')
            print(sobre)
        elif clase==3:
            print('obesidad grado 1')
            print(obe1)
        elif clase==4:
            print('obesidad grado 2')
            print(obe2)
        elif clase==5:
            print('obesidad grado 3')
            print(obe3)
