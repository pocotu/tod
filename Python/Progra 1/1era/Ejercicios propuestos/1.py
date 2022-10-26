'''
Implementar una función que permita invertir un número entero cualquiera (Se 
tiene que tener una función que permita validar además que el número entero sea 
positivo).
'''

def invertir_numero(numero):
    if numero < 0:
        return "El numero debe ser positivo"
    numero_invertido = 0
    while numero > 0:
        # multiplica por 10 para que el numero se desplace una posicion a la izquierda
        numero_invertido = numero_invertido * 10 + numero % 10
        # divide por 10 para que el numero se desplace una posicion a la derecha
        numero = numero // 10
    return numero_invertido

def main():
    numero = int(input("Ingrese un numero entero positivo: "))
    print(invertir_numero(numero))

main()