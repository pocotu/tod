import random
import time
import matplotlib.pyplot as plt

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        less = [x for x in lista[1:] if x <= pivot]
        greater = [x for x in lista[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
def ordenamiento_burbuja_optimizado2(lista):
    n = len(lista)
    intercambio = True
    iteracion = 0

    while (intercambio):
        intercambio = False
        for i in range(n - iteracion - 1):
            if (lista[i] > lista[i+1]):
                temp1 = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp1
                #lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        iteracion += 1
    #print("Numero de iteracion: ", iteracion)
    return lista

def ordenamiento_insercion(A):
    n = len(A)

    for i in range(n):
        posicion = i
        aux = A[i]
        while (posicion > 0) and (A[posicion-1] > aux):
            A[posicion] = A[posicion-1]
            posicion = posicion - 1
        A[posicion] = aux
    return A