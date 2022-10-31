"""
Maximo Comun Divisor utilizando el algoritmo de Euclides
"""

def MCD_Euclides(a, b):
    
    ###### metodo 1 ######
    # si b es 0, entonces a es el MCD
    if b == 0:
        return a
    # si b no es 0, entonces se calcula el MCD de b y el resto de a/b
    else:
        return MCD_Euclides(b, a % b)

    ###### metodo 2 ######
    ## mientras b no sea 0, se calcula el MCD de b y el resto de a/b
    #while b != 0:
    #    # se calcula el resto de a/b
    #    a, b = b, a % b
    #    print(a, "resto:", b)
    #return a

    ###### metodo 3 ######
    #while a % b != 0:
    #    resto = a % b
    #    a = b # a pasa a ser el divisor
    #    b = resto # b pasa a ser el resto
    #    print(resto, a, b)
    #return b # el MCD es el ultimo resto


def main():
    a = int(input("Ingresa un numero: "))
    while a < 0:
        print("El numero debe ser mayor a 0")
        a = int(input("Ingresa un numero: "))
    b = int(input("Ingresa otro numero: "))
    while b < 0:
        print("El numero debe ser mayor a 0")
        b = int(input("Ingresa otro numero: "))

    print("")
    print("El maximo comun divisor es: ", MCD_Euclides(a, b))

main()