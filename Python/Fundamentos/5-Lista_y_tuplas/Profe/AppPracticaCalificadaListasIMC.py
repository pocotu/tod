# **********************   MÓDULOS   ***************************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de operaciones con listas
    print()
    print('*****   OPERACIONES CON LISTAS   *****')
    print('1 Agregar IMC')
    print('2 Eliminar IMC')    
    print('3 Nro. Personas en Cada Clase')
    print('4 Porcentaje de cada clase del IMC')
    print('5 Generar una SubLista con los IMC de un Clase')
    print('6 Listado en General')
    print('7 Salir')
    
# -----------  Agregar Indice de Masa corporal a la lista  -------------
def Agregar(ListaIMC):
    # -- Leer Indice de Masa Corporal
    IMC = float(input('Ingresar IMC de cada Persona: '))
    # -- Agregar IMC a la lista
    return ListaIMC + [IMC]

# -----------  Eliminar IMC de la lista  -------------
def Eliminar(ListaIMC):
    if (len(ListaIMC)>0):
        # -- Ingresar la Posicion del IMC a Eliminar
        Pos = int(input('Ingresa Posicion: '))
        return ListaIMC[:Pos]+ ListaIMC[Pos+1:len(ListaIMC)]
    else:
        return ListaIMC

# -----------  Número de personas de una clase de IMC  -------------
def NroPersonasClase(ListaIMC, Vmin, Vmax):
    # -- Incicializar contador
    NroPersonas = 0
    # -- Contar los IMC de esta clase
    for IMC in ListaIMC:
        if (Vmin <= IMC < Vmax):
            NroPersonas+=1
    # -- Devolver resultado
    return NroPersonas

# -----------  Reporte de Nro. de personas de cada clase de IMC  -------------
def NroPersonasClases(ListaIMC):
    # -- Incicializar contadores
    NroIMCNormal = NroPersonasClase(ListaIMC, 18.5, 25)
    NroIMCSobrepeso = NroPersonasClase(ListaIMC, 25, 30)
    NroIMCObesidad1 = NroPersonasClase(ListaIMC, 30, 35)
    NroIMCObesidad2 = NroPersonasClase(ListaIMC, 35, 40)
    NroIMCObesidad3 = NroPersonasClase(ListaIMC, 40, 200)
    # -- Mostrar número de personas por clase
    print()
    print('Número de personas con IMC')
    print('==========================')
    print('Normal= ', NroIMCNormal)
    print('Sobrepeso = ', NroIMCSobrepeso)
    print('Obesidad 1 = ', NroIMCObesidad1)
    print('Obesidad 2 = ', NroIMCObesidad2)
    print('Obesidad 3 = ', NroIMCObesidad3)
# -----------  Reporte de porcentaje de cada clase de IMC  -------------
def PorcentajesClases(ListaIMC):
    # -- Determinar el número total de personas
    N = len(ListaIMC)
    # -- Determinar porcentajes
    PorcentajeIMCNormal = NroPersonasClase(ListaIMC, 18.5, 25)/N*100
    PorcentajeIMCSobrepeso = NroPersonasClase(ListaIMC, 25, 30)/N*100
    PorcentajeIMCObesidad1 = NroPersonasClase(ListaIMC, 30, 35)/N*100
    PorcentajeIMCObesidad2 = NroPersonasClase(ListaIMC, 35, 40)/N*100
    PorcentajeIMCObesidad3 = NroPersonasClase(ListaIMC, 40, 200)/N*100
    # -- Mostrar Porcentaje de personas por clase
    print()
    print('Porcentaje de personas con IMC')
    print('===============================')
    print('Normal = ', PorcentajeIMCNormal)
    print('Sobrepeso = ', PorcentajeIMCSobrepeso)
    print('Obesidad 1 = ', PorcentajeIMCObesidad1)
    print('Obesidad 2 = ', PorcentajeIMCObesidad2)
    print('Obesidad 3 = ', PorcentajeIMCObesidad3)
# -----------  Sub lista de IMC de una determinada clase  -------------
def SubListaClase(ListaIMC, Vmin, Vmax):
    # -- Inicializar sub lista
    SL = []
    # -- Contar los IMC de esta clase
    for IMC in ListaIMC:
        if (Vmin <= IMC < Vmax):
            SL += [IMC]
    # -- Devolver resultado
    return SL

# -----------  Generar Sub lista de IMC de una determinada clase  -------------
def GenerarSubListaIMC(ListaIMC):
    # -- Leer la clase cuya sub lista se desea generar
    Clase = input('Ingrese clase: ')
    # -- Recuperar  sub lista
    if Clase == 'Normal':
        SL = SubListaClase(ListaIMC, 18.5, 25)
    elif Clase == 'Sobrepeso':
        SL = SubListaClase(ListaIMC, 25, 30)
    elif Clase == 'Obesidad1':
        SL = SubListaClase(ListaIMC, 30, 35)
    elif Clase == 'Obesidad2':
        SL = SubListaClase(ListaIMC, 35, 40)
    elif Clase == 'Obesidad3':
        SL = SubListaClase(ListaIMC, 40, 200)

    # -- Mostrar sub lista
    print()
    print('Listado por Clases')
    print('==================')
    EscribirLista(SL)

# -----------   Listado en Genral  -------------
def EscribirLista(Lista):
    print()
    # -- Mostrar los elementos de la lista
    print('LISTADO GENERAL')
    print('===============')
    for IMC in Lista:
        # -- Escribir el K-ésimo elemento de la lista
        print(IMC)

# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
ListaIMC = []
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
        NroPersonasClases(ListaIMC)
    elif Opcion == 4:
        PorcentajesClases(ListaIMC)
    elif Opcion == 5:
        GenerarSubListaIMC(ListaIMC)
    elif Opcion == 6:
        EscribirLista(ListaIMC)

