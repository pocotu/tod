'''
Implementar una función que, dada una lista, 
retorne otra lista con los elementos de la lista 
original, sin repeticiones.
'''

def eliminar_repetidos(lista):
    lista_sin_repetidos = []
    for elemento in lista:
        # si el elemento no esta en la lista sin repetidos, lo agrega
        if elemento not in lista_sin_repetidos:
            lista_sin_repetidos.append(elemento)
    return lista_sin_repetidos

def main():
    lista = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print(eliminar_repetidos(lista))

main()