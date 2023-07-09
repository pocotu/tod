# crea la funcion qick_sort

# tipo1
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista.pop()
        menores = []
        mayores = []
        for i in lista:
            if i < pivote:
                menores.append(i)
            else:
                mayores.append(i)
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# tipo2
def quick_sort2(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista.pop()
        menores = [i for i in lista if i < pivote]
        mayores = [i for i in lista if i >= pivote]
        return quick_sort2(menores) + [pivote] + quick_sort2(mayores)

# tipo3
def quick_sort3(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista.pop()
        menores = [i for i in lista if i < pivote]
        mayores = [i for i in lista if i >= pivote]
        return quick_sort3(menores) + [pivote] + quick_sort3(mayores)

# ejemplos para correr
lista = [1, 5, 3, 2, 4]
print(quick_sort(lista))
print(quick_sort2(lista))
print(quick_sort3(lista))


