'''
Desarrolle una funcion que tenga dos parámetros de entrada. El primer parámetro de 
entrada es una funcion y el segundo es una lista. La funcion principal retorna una lista
como resultado de aplicar el proceso de la funcion (parámetro uno) a cada uno de los 
elementos de la lista (parámetro dos).
Ejemplo: 
Parámetros: 
- funcion (n)
- [1,2,3,4,5]
funcionPrincipal (suma, [1,2,3,4])
Resultado: []
'''
from sumar_lista import *
lista = [1,2,3,4,5]

def sumar_lista():
    suma = 0
    for i in lista:
        suma += i
    return suma

def funcion_principal(suma, lista):
    resultado = []
    for i in lista:
        resultado.append(i)
    return resultado

print(funcion_principal(sumar_lista, lista))




