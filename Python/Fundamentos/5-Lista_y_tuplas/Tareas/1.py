'''
El índice de masa corporal (IMC) es un número que se calcula en función al peso y la 
estatura de la persona. Para la mayoría de las personas, el IMC es un indicador confiable
de la gordura y se usa para identificar las categorías de peso que pueden llevar 
a problemas de salud. La siguiente tabla resume estos indicadores.

Clasificacion       IMC(Kg/m2)      Riesgo
-----------------------------------------------
Normal              18.5 - 24.9     Promedio
Sobrepeso           25 - 29.9       Aumentado
Obesidad grado 1    30 - 34.9       Moderado
Obesidad grado 2    35 - 39.9       Severo
Obesidad grado 3    Mas de 40       Muy severo

La universidad, en su politica de prevencion, determino el IMC del personal de labora en
la institucion, habiendo registrado dichos valores en una lista, similiar a la siguiente:

ListaIMC = [25.5, 31.8, 18.8, 22.0, 24.1, 27.3, 41.1, 17.8, 38.2, 23.0, 21.5, 20.4, 32.5]

Escribir una aplicación que efectúe lo siguiente:
Implementar un menú con las siguientes alternativas:
1 Agregar IMC
2 Eliminar IMC
3 Número de personas en cada clase del IMC
4 Porcentaje de cada clase del IMC
5 Generar una sub lista con los IMC de una determinada clase.
6 Salir
'''

# **********************   MÓDULOS   ***************************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*****   Ingrese una opcion   *****')
    print('1 Agregar IMC')
    print('2 Eliminar IMC')    
    print('3 Numero de personas en cada clase de IMC')
    print('4 Porcentaje de cada clase del IMC')
    print('5 Generar una sub lista con los IMC de una determinada clase')
    print('6 listar')
    print('7 Salir')

# -----------  Agregar elemento a la lista  -------------
def Agregar(ListaIMC):
    # -- Leer elemento
    Elemento = input('Ingresar IMC: ')
    # -- Agregar elemento a la lista
    return ListaIMC + [Elemento]

# -----------  Eliminar elemento a la lista  -------------
def Eliminar(ListaIMC):
    if (len(ListaIMC)>0):
        # -- Leer elemento y Posicion
        Pos = int(input('Ingresa Posicion: '))
        return ListaIMC[0:Pos]+ ListaIMC[Pos+1:len(ListaIMC)]
    else:
        return ListaIMC

# -----------  Numero de personas en cada clase de IMC -------------
def NroPersonasClase():
    print('Mormal: ', len(ListaNormal))
    print('Sobrepeso: ', len(ListaSobrepeso))
    print('Obesidad grado 1: ', len(ListaObeGrado1))
    print('Obesidad grado 2: ', len(ListaObeGrado2))
    print('Obesidad grado 3: ', len(ListaObeGrado3))
        
# -----------  Porcentaje de cada clase del IMC  -------------
def PorcentajeClase():
    print('Normal: ', (len(ListaNormal)/len(ListaIMC))*100, '%')
    print('Sobrepeso: ', (len(ListaSobrepeso)/len(ListaIMC))*100, '%')
    print('Obesidad grado 1: ', (len(ListaObeGrado1)/len(ListaIMC))*100, '%')
    print('Obesidad grado 2: ', (len(ListaObeGrado2)/len(ListaIMC))*100, '%')
    print('Obesidad grado 3: ', (len(ListaObeGrado3)/len(ListaIMC))*100, '%')

'''
# -----------  Generar una sub lista con los IMC de una determinada clase  -------------
def SubListaIMCClase(ListaIMC):
'''

# -----------  Escribir Lista  -------------
def EscribirLista(ListaIMC):
    print()
    # -- Escribir los elementos de la lista
    for Elemento in ListaIMC:
        # -- Escribir el K-ésimo elemento de la lista
        print(Elemento)

    
# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
ListaIMC = [25.5, 31.8, 18.8, 22.0, 24.1, 27.3, 41.1, 17.8, 38.2, 23.0, 21.5, 20.4, 32.5]

ListaNormal = []
for i in ListaIMC:
    if i >= 18.5 and i <= 24.9:
        ListaNormal.append(i)
#print(ListaModerada)

ListaSobrepeso = []
for i in ListaIMC:
    if i >= 25 and i <= 29.9:
        ListaSobrepeso.append(i)
#print(ListaSobrepeso)

ListaObeGrado1 = []
for i in ListaIMC:
    if i >= 30 and i <= 34.9:
        ListaObeGrado1.append(i)
#print(ListaObeGrado1)

ListaObeGrado2 = []
for i in ListaIMC:
    if i >= 35 and i <= 39.9:
        ListaObeGrado2.append(i)
#print(ListaObeGrado2)

ListaObeGrado3 = []
for i in ListaIMC:
    if i >= 40:
        ListaObeGrado3.append(i)
#print(ListaObeGrado3)

# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 7:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        ListaIMC = Agregar(ListaIMC)        
    elif Opcion == 2:
        ListaIMC = Eliminar(ListaIMC)
    elif Opcion == 3:
        NroPersonasClase()
    elif Opcion == 4:
        PorcentajeClase()
    elif Opcion == 5:
        ListaIMC = SubListaIMCClase(ListaIMC)
    elif Opcion == 6:
        ListaIMC = EscribirLista(ListaIMC)

# Programa principal 

# Declarar lista
ListaIMC = [] 


