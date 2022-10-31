'''
Escribir un programa que lea un numero natural de 5 cifras, no todos iguales.
Implementa la funcion Mayor(N), que calcula el mayor numero que se puede formar
con las cifras de N, y la funcion Menor(N) que calcula el menor numero que se puede
formar con las cifras de numero
'''


# Implementa la funcion Mayor(N), que calcula el mayor numero que se puede formar con las cifras de N
def mayor(N):
    N = str(N)
    # sorted devuelve una lista ordenada y reverse=True la ordena de mayor a menor
    N = sorted(N, reverse=True)
    N = ''.join(N)
    return int(N)

def menor(N):
    N = str(N)
    # sorted devuelve una lista ordenada
    N = sorted(N)
    # ''.join une los elementos de la lista en un string
    N = ''.join(N)
    return int(N)

def leerN():
    while True:
        N = int(input("Ingrese un numero natural de 5 cifras: "))
        if N > 9999 and N < 100000:
            break
    return N

def main():
    N = leerN()
    print("El mayor numero que se puede formar con las cifras de %d es %d" % (N, mayor(N)))
    print("El menor numero que se puede formar con las cifras de %d es %d" % (N, menor(N)))

main()