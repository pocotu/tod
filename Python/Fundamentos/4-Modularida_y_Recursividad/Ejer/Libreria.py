# Librerias de modulos que pueden ser utilizados en cualquier programa

# Modulo de lectura de numeros

# Modulo para leer un numero entero
def LeerNroEntero(Texto, Minimo, Maximo = 100000000000):
    Nro = int(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = int(input(Texto))
    return Nro

# Modulo para leer un numero real
def LeerNroReal(Texto, Minimo, Maximo = 100000000000):
    Nro = float(input(Texto))
    while (Nro < Minimo) or (Nro > Maximo):
        print('Error. Número fuera de rango...')
        Nro = float(input(Texto))
    return Nro

# Modulo para determinar el menor de dos numeros
def MayorDos(A, B):
    return A if A > B else B

# Modulo intercambiar numeros
def Intercambiar(A, B):
    temp = A
    A = B
    B = temp
    return (A, B)

# Modulo para ordenar dos numeros
def OrdenarDos(A,B):
    if A > B:
        A, B = Intercambiar(A, B)
    return(A,B)

