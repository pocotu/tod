# Implementar el metodo quicksort

# Algoritmo de ordenacion quicksort 1
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    izquierda = [x for x in arr if x < pivot]
    medio = [x for x in arr if x == pivot]
    derecha = [x for x in arr if x > pivot]
    return quicksort(izquierda) + medio + quicksort(derecha)

A = [5, 3, 8, 6, 7, 2, 0, 1]
print("Lista original: ", A)
quicksort(A)
print("Lista ordenada: ", quicksort(A))

# Algoritmo de ordenacion quicksort 2
def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    izquierda = []
    derecha = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            izquierda.append(arr[i])
        else:
            derecha.append(arr[i])
    return quicksort2(izquierda) + [pivot] + quicksort2(derecha)

lista = [5, 3, 8, 6, 7, 2, 0, 1]
print("Lista original: ", lista)
quicksort2(lista)
print("Lista ordenada: ", quicksort2(lista))

