'''
Implementar una función que dado un dígito d [1..9] muestre por pantalla el 
siguiente renglón: 1 2 3 .. d .. 3 2 1. Por ejemplo, si d = 6 la función deberá imprimir 
1 2 3 4 5 6 5 4 3 2 1. Luego implemente un módulo principal utilizando dicha función, 
para que solicite un dígito d al usuario, y muestre por pantalla una figura como la 
siguiente:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
...
1 2 3 .....d..... 3 2 1
'''

def imprimir_renglon(d):
    # Imprimimos los numeros de 1 a d
    for i in range(1, d + 1):
        print(i, end=" ")
    # Imprimimos los numeros de d - 1 a 1
    for i in range(d - 1, 0, -1):
        print(i, end=" ")
    print()

def main():
    d = int(input("Ingrese un numero: "))
    while d < 1 or d > 9:
        print("El numero debe estar entre 1 y 9")
        d = int(input("Ingrese un numero: "))
    for i in range(1, d + 1):
        imprimir_renglon(i)

main()
