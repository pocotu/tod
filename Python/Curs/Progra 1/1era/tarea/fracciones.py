
def LeerNumeros():
    print("####### Fraccion 1 #######")
    N1 = int(input("Introduce el numerador: "))
    D1 = int(input("Introduce el denominador: "))
    while D1 == 0:
        print("El denominador no puede ser 0")
        D1 = int(input("Introduce el denominador: "))
    print("####### Fraccion 2 #######")
    N2 = int(input("Introduce el numerador: "))
    D2 = int(input("Introduce el denominador: "))
    while D2 == 0:
        print("El denominador no puede ser 0")
        D2 = int(input("Introduce el denominador: "))
    return N1, D1, N2, D2

def Suma(N1, D1, N2, D2):
    NS = (N1 * D2) + (N2 * D1)
    DS = D1 * D2
    NS, DS = Simplificar(NS, DS)
    return NS, DS

def Resta(N1, D1, N2, D2):
    NR = (N1 * D2) - (N2 * D1)
    DR = D1 * D2
    NR, DR = Simplificar(NR, DR)
    return NR, DR

def Multiplicacion(N1, D1, N2, D2):
    NM = N1 * N2
    DM = D1 * D2
    NM, DM = Simplificar(NM, DM)
    return NM, DM

def Division(N1, D1, N2, D2):
    ND = N1 * D2
    DD = D1 * N2
    ND, DD = Simplificar(ND, DD)
    return ND, DD

def Simplificar(N, D):
    MCD = MCD_Euclides(N, D)
    # se divide el numerador y el denominador entre el MCD
    N = N // MCD
    D = D // MCD
    return N, D

def MCD_Euclides(a, b):
    while a % b != 0:
        resto = a % b 
        a = b # a pasa a ser el divisor
        b = resto # b pasa a ser el resto
    return b # el MCD es el ultimo resto

def Menu():
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    opcion = int(input("Elige una opcion: "))
    while opcion < 1 or opcion > 4:
        print("Opcion incorrecta")
        opcion = int(input("Elige una opcion: "))
    if opcion == 1:
        N1, D1, N2, D2 = LeerNumeros()
        NS, DS = Suma(N1, D1, N2, D2)
        print("La suma es: ", NS, "/", DS)
    if opcion == 2:
        N1, D1, N2, D2 = LeerNumeros()
        NR, DR = Resta(N1, D1, N2, D2)
        print("La resta es: ", NR, "/", DR)
    if opcion == 3:
        N1, D1, N2, D2 = LeerNumeros()
        NM, DM = Multiplicacion(N1, D1, N2, D2)
        print("La multiplicacion es: ", NM, "/", DM)
    if opcion == 4:
        N1, D1, N2, D2 = LeerNumeros()
        ND, DD = Division(N1, D1, N2, D2)
        print("La division es: ", ND, "/", DD)

Menu()