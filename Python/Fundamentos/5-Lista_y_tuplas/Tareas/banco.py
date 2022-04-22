# *******   BANCO    **********


# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('** CUENTAS Y MOVIMIENTOS **')
    print('1 Agregar Cuenta Corriente')
    print('2 Agregar Movimientos')
    print('3 Listar Cuentas Corrientes')
    print('4 Listar Movimientos')
    print('5 Listar Movimientos de una cuenta')
    print('6 Saldo de una cuenta')
    print('7 FIN')


#  Módulo Posicion
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


#  Módulo Agregar Cliente CTA CTE
def AgregarCTE(ListaJ):
    # -- Leer el codigo de la cuenta
    CTACTE = input('Ingrese número de cuenta: ')
    if Posicion(CTACTE, ListaJ) >= 0:
        print('Ya existe número de cuenta')
    else:
        # Ingresar la Información
        RazonSocial = input('Ingrese razón social: ')
        Direccion = input('Ingrese Dirección: ')
        Celular = input('Ingrese número de celular: ')
        # Agregar a la lista de Cuentas
        ListaJ.append([CTACTE, RazonSocial, Direccion, Celular])


#   Módulo Agregar Movimientos
def AgregarMovimientos(ListaJ, ListaM):
    # -- Leer el codigo del documento
    Doc = input('Ingrese número de documento del movimiento: ')
    if Posicion(Doc, ListaM) >= 0:
        print('Ya existe número de documento')
    else:
        # Ingresar la Información
        Fecha = input('Ingrese fecha: ')
        Tipo = input('Ingrese tipo de operacion: ')
        Monto = float(input('Ingrese monto: '))
        # -- Ingresar CUENTA validando
        CTACTE = input('Ingrese número de cuenta: ')
        P = Posicion(CTACTE, ListaJ)
        while P < 0:
            print('Número de cuenta ingresada no existe')
            CTACTE = input('Ingrese número de cuenta existente: ')
            P = Posicion(CTACTE, ListaJ)
        # Agregar a la lista de Movimientos
        ListaM.append([Doc, Fecha, Tipo, Monto, CTACTE])


#  Listar Cuentas
def ListarCTE(ListaJ):
    # -- Listar Cuentas en General
    print()
    print("LISTADO DE CUENTAS CORRIENTES EN GENERAL")
    print("===========================================")
    print('Codigo'.ljust(6), 'Razón Social'.ljust(15), 'Dirección'.ljust(15), 'Celular'.ljust(10))
    print('----------------------------------------------------------------------------')
    for L in ListaJ:
        print(L[0].ljust(6), L[1].ljust(15), L[2].ljust(15), L[3].ljust(10))


#  Listar Movimientos
def ListarMovimientos(ListaM):
    # -- Listar Moviinetos en General
    print()
    print("LISTADO DE MOVIMIENTOS EN GENERAL")
    print("===========================================")
    print('Doc'.ljust(6), 'Fecha'.ljust(10), 'Tipo'.ljust(3), 'Monto'.ljust(7), 'CodCuenta'.ljust(5))
    print('----------------------------------------------------------------------------')
    for L in ListaM:
        print(L[0].ljust(6), L[1].ljust(10), L[2].ljust(3), str(L[3]).ljust(7), L[4].ljust(5))


#  Listar Movimientos de una cuenta
def MovimientosCuenta(CTACTE, ListaM):
    # -- Mostrar los movimientos que pertenecen a la cuenta corriente
    print()
    print('RELACION DE MOVIMIENTOS DE LA CUENTA', CTACTE)
    for A in ListaM:
        if CTACTE == A[4]:
            print(A)


#  Listar Movimientos Por Cuenta
def ListarMovimientosCuenta(LC, LM):
    # -- Leer codigo de CUENTA
    CTACTE = input('Ingrese número de cuenta: ')
    # -- Verificar si existe cuenta
    PE = Posicion(CTACTE, LC)
    if PE >= 0:  # -- Existe cuenta
        MovimientosCuenta(CTACTE, LM)
    else:  # -- No existe cuenta
        print('No existe código de cuenta corriente')


#   Saldo de una cuenta corriente
def SaldoCuentaCte(LM):
    S = 0
    R = 0
    # -- Leer codigo de cuenta
    CTACTE = input('Ingrese número de cuenta: ')
    # -- Determinar saldo
    for E in LM:
        if CTACTE == E[4] and 'D' == E[2]:
            S += E[3]
        if CTACTE == E[4] and 'R' == E[2]:
            R += E[3]
    print('SALDO DE LA CUENTA', CTACTE)
    print('====> ', S - R)

# ******   PROGRAMA PRINCIPAL   ********
# -- Declarar la lista
ListaJ = []
ListaM = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion != 7:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        AgregarCTE(ListaJ)
    elif Opcion == 2:
        AgregarMovimientos(ListaJ, ListaM)
    elif Opcion == 3:
        ListarCTE(ListaJ)
    elif Opcion == 4:
        ListarMovimientos(ListaM)
    elif Opcion == 5:
        ListarMovimientosCuenta(ListaJ, ListaM)
    elif Opcion == 6:
        SaldoCuentaCte(ListaM)
