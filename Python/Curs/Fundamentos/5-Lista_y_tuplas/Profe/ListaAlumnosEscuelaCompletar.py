# ********************   LISTA DE LISTAS    *************************

# ************   MÓDULOS ESPECÍFICOS DE LA APLICACIÓN  ***************

# -----------  Menu  -------------
def Menu():
    # -- Mostrar el menú de opciones
    print()
    print('*****   ALUMNOS ESCUELA   *****')
    print('1 Agregar Escuelas')
    print('2 Agregar Alumnos')
    print('3 Consultar Alumnos')    
    print('4 Consultar Escuelas')
    print('5 Eliminar Alumnos')    
    print('6 Eliminar Escuelas')
    print('7 Listar Alumnos por Escuela')
    print('8 Número de Alumnos de cada Escuela')
    print('9 Relación de Alumnos ingresantes')
    print('10 Listar Alumnos')
    print('11 Listar Escuelas')
    print('12 Relación de Alumnos ingresantes por Escuela y Año')
    print('13 FIN')

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

# -----------  Módulo Agregar Alumno  -------------
def AgregarAlumnos(ListaE, ListaA):    
    # -- Leer el codigo del Alumno
    CodAlumno = input('Ingrese el código del Alumno: ')
    if Posicion(CodAlumno,ListaA) >= 0:
        print('Código ya existe en la lista de Alumnos')
    else:
        # Ingresar la Información
        AP = input('Ingrese Apellido Paterno: ')
        AM = input('Ingrese Apellido Materno: ')
        Nombres = input('Ingrese Nombres: ')
        # -- Ingresar Escuela validando
        CodEscuela = input('Ingrese código Escuela: ')
        P = Posicion(CodEscuela, ListaE)
        while P < 0:
            print('Escuela ingresada no existe')
            CodEscuela = input('Ingrese código de Escuela válido: ')
            P = Posicion(CodEscuela, ListaE)            
        # Agregar a la lista de Alumnos
        ListaA.append([CodAlumno, AP, AM, Nombres, CodEscuela])
# -----------  Módulo Agregar Escuela  -------------
def AgregarEscuelas(ListaE):    
    # -- Leer el codigo de la Escuela
    CodEscuela = input('Ingrese el código de la Escuela: ')
    if Posicion(CodEscuela,ListaE) >= 0:
        print('Código ya existe en la lista de Escuelas')
    else:
        # Ingresar la Información
        Nombre = input('Ingrese Nombre de Escuela: ')
        
        # Agregar a la lista de Escuelas
        ListaE.append([CodEscuela, Nombre])

# -----------  Consultar Alumnos -------------
def ConsultarAlumnos(ListaA):
    # -- Leer el código del Alumno
    CodAlumno = input('Ingrese el código del Alumno: ')
    P = Posicion(CodAlumno, ListaA)
    if P >= 0:
        print(ListaA[P])
    else:
        print(CodAlumno, ' no está en la lista')

# -----------  Consultar Escuelas -------------
def ConsultarEscuelas(ListaE):
    # -- Leer el código de la Escuela
    CodEscuela = input('Ingresa el código de la Escuela: ')
    P = Posicion(CodEscuela, ListaE)
    if P >= 0:
        print(ListaE[P])
    else:
        print(CodEscuela, ' no está en la lista')

# -----------  Eliminar Alumno  -------------
def EliminarAlumnos(ListaA):
    # -- Leer el codigo del Alumno
    CodAlumno = input('Ingrese el código del Alumno: ')
    P = Posicion(CodAlumno, ListaA)
    if P >= 0:
        del ListaA[P]
    else:
        print(CodAlumno, ' no está en la lista')

# -----------  Eliminar Escuela  -------------
def EliminarEscuelas(ListaE):
    # -- Leer el codigo de la Escuela
    CodEscuela = input('Ingrese el código de la Escuela: ')
    P = Posicion(CodEscuela, ListaE)
    if P >= 0:
        del ListaE[P]
    else:
        print(CodEscuela, ' no está en la lista')

# -----------  Listar Alumnos  -------------
def ListarAlumnos(ListaA):
    # -- Listar Alumnos en General
    print()
    print("LISTADO DE ALUMNOS EN GENERAL")
    print("=======================================")
    print('Codigo'.ljust(6),'Apellido Pat.'.ljust(15),'Apellido Mat.'.ljust(15),'Nombres'.ljust(15),'CodEscuela')
    print('----------------------------------------------------------------------------')
    for L in ListaA:        
        print(L[0].ljust(6),L[1].ljust(15),L[2].ljust(15), L[3].ljust(20),L[4])

# -----------  Listar Escuelas  -------------
def ListarEscuelas(ListaE):
    # -- Listar Escuelas en General
    print()
    print("LISTADO DE ESCUELAS EN GENERAL")
    print("=======================================")
    print('Codigo\tNombres')
    print('------\t--------------------------')
    for L in ListaE:        
        print(L[0], '\t', L[1])
# -----------  Listar Alumnos de una Escuela  -------------
def ListarAlumnosDeUnaEscuela(CodEscuela, LA):
    # -- Mostrar los alumnos que pertenecen a la escuela de CodEscuela
    print()
    print('RELACION DE ALUMNOS DE LA ESCUELA ', CodEscuela)
    for A in LA:
        if CodEscuela == A[4]:
            print(A)
# -----------  Listar Alumnos Por Escuela  -------------
def ListarAlumnosEscuela(LE, LA):
    # -- Leer codigo de escuela
    CodEscuela = input('Ingrese código de Escuela: ')
    # -- Verificar si existe escuela
    PE = Posicion(CodEscuela, LE)
    if PE >= 0: # -- Existe escuela
        ListarAlumnosDeUnaEscuela(CodEscuela, LA)
    else: # -- No existe escuela
        print('No existe código de Escuela')
# -----------  Listar Nro de Alumnos de Escuela  -------------
def NumeroAlumnosDeEscuela(CodEscuela, LA):
    # -- Determinar número de alumnos que pertenecen a la escuela de CodEscuela
    N = 0
    for A in LA:
        if CodEscuela == A[4]:
            N += 1
    # -- Devolver resultado    
    return N
# -----------  Listar Nro de Alumnos de cada Escuela  -------------        
def NumeroAlumnosCadaEscuela(LE, LA):
    # -- Determinar número de alumnos de cada Escuela
    for E in LE:
        # -- Contar número de alumnos de la Escuela E
        NroAlumnos = NumeroAlumnosDeEscuela(E[0], LA)        
        # -- Mostrar Escuela con número de alumnos
        print(E[0].ljust(5), E[1].ljust(25), str(NroAlumnos).rjust(5))        
# -----------  Listar Alumnos Ingresante de un año -------------
def AlumnosIngresantes(LA):
    # -- Ingresar el año de ingreso
    Anio = input('Ingrese año de ingreso: ')
    # -- Mostrar relación de alumnos ingresantes de dicho año
    for A in LA:
        # -- Verificar si el código del alumno empieza con los dos primeros
        #    dígitos del año
        if A[0].startswith(Anio[2:]):
            print(A)
  
       
# *****************   PROGRAMA PRINCIPAL   *******************

# -- Declarar la lista
ListaA = []
ListaE = []
# -- Mostrar y procesar Menu
Opcion = 0
while Opcion !=13:
    # -- Mostrar menu
    Menu()
    # -- Leer opción
    Opcion = int(input('Ingrese opción --> '))
    # -- Procesar de acuerdo a opción
    if Opcion == 1:
        AgregarEscuelas(ListaE)
    elif Opcion == 2:
        AgregarAlumnos(ListaE,ListaA)
    elif Opcion == 3:
        ConsultarAlumnos(ListaA)
    elif Opcion == 4:
        ConsultarEscuelas(ListaE)
    elif Opcion == 5:
        EliminarAlumnos(ListaA)
    elif Opcion == 6:
        EliminarEscuelas(ListaE)        
    elif Opcion == 7:
        ListarAlumnosEscuela(ListaE, ListaA)
    elif Opcion == 8:
        NumeroAlumnosCadaEscuela(ListaE, ListaA)
    elif Opcion == 9:
        AlumnosIngresantes(ListaA)        
    elif Opcion == 10:
        ListarAlumnos(ListaA)
    elif Opcion == 11:
        ListarEscuelas(ListaE)
    elif Opcion == 12:
        AlumnosIngresantesEscuela(ListaA)
