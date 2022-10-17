def LeerFracciones():
    print("Introduzca la fraccion 1")
    n1 = int(input("Numerador: "))
    d1 = int(input("Denominador: "))
    print("Introduzca la fraccion 2")
    n2 = int(input("Numerador: "))
    d2 = int(input("Denominador: "))
    return n1, d1, n2, d2

def Suma(n1, d1, n2, d2):
    ns = (n1 * d2) + (n2 * d1)
    ds = d1 * d2
    return ns, ds

def Resta(n1, d1, n2, d2):
    nr = (n1 * d2) - (n2 * d1)
    dr = d1 * d2
    return nr, dr

def Multiplicacion(n1, d1, n2, d2):
    nm = n1 * n2
    dm = d1 * d2
    return nm, dm

def Division(n1, d1, n2, d2):
    nd = n1 * d2
    dd = d1 * n2
    return nd, dd

def Simplificar(n, d):
    mcd = MCD(n, d)
    n = n // mcd
    d = d // mcd
    return n, d

def MCD(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

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
        n1, d1, n2, d2 = LeerFracciones()
        ns, ds = Suma(n1, d1, n2, d2)
        ns, ds = Simplificar(ns, ds)
        print("La suma es: ", ns, "/", ds)
    elif opcion == 2:
        n1, d1, n2, d2 = LeerFracciones()
        nr, dr = Resta(n1, d1, n2, d2)
        nr, dr = Simplificar(nr, dr)
        print("La resta es: ", nr, "/", dr)
    elif opcion == 3:
        n1, d1, n2, d2 = LeerFracciones()
        nm, dm = Multiplicacion(n1, d1, n2, d2)
        nm, dm = Simplificar(nm, dm)
        print("La multiplicacion es: ", nm, "/", dm)
    elif opcion == 4:
        n1, d1, n2, d2 = LeerFracciones()
        nd, dd = Division(n1, d1, n2, d2)
        nd, dd = Simplificar(nd, dd)
        print("La division es: ", nd, "/", dd)

Menu()