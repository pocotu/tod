'''
Implementar una función que permita determinar si un número es capicúa (Un 
número es capicúa, si es igual a su número invertido, se recomienda utilizar la 
función implementado en el ejercicio anterior).
'''

def es_capicua(numero):
    if numero < 0:
        return "El numero debe ser positivo"
    numero_invertido = 0
    numero_original = numero
    while numero > 0:
        # multiplica por 10 para que el numero se desplace una posicion a la izquierda
        numero_invertido = numero_invertido * 10 + numero % 10
        # divide por 10 para que el numero se desplace una posicion a la derecha
        numero = numero // 10
    if numero_invertido == numero_original:
        return "El numero es capicua"
    return "El numero no es capicua"

def main():
    numero = int(input("Ingrese un numero entero positivo: "))
    print(es_capicua(numero))

main()