# Metodo de ordenacion por insercion
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

# Programa principal

A = [5, 3, 8, 6, 7, 2, 0, 1]
print("Lista original: ", A)
print("Lista ordenada: ", ordenamiento_insercion(A))