'''
Implementar una función recursiva que calcule el promedio de los elementos de una lista.
'''

def promedio(lista):
    # si la lista esta vacia
    if len(lista) == 0:
        return 0
    # si la lista tiene un elemento
    else:
        # retornar el elemento de la lista en la posicion 0 mas el promedio de la lista sin el elemento de la posicion 0
        return lista[0] + promedio(lista[1:]) 

def main():
    tamano = int(input("Tamano: "))
    lista = []
    for i in range(tamano):
        lista.append(int(input("Numero {}: ".format(i+1))))
    print(promedio(lista)/tamano)

main()
