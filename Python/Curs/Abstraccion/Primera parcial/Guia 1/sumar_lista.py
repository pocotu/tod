'''
Cree una funcion que sume una lista de 5 números enteros.
Ejemplo: Suma ([5,8,9,4,6])
Resultado: 32
'''

lista = [5,8,9,4,6]

def sumar_lista():
    suma = 0
    for i in lista:
        suma += i
    return suma

#print(sumar_lista())

