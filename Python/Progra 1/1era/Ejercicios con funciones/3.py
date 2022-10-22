'''
Escribir una función que reciba dos números enteros positivos a y b como parámetro y determine 
si ellos son amigos o no, devolviendo True caso sean amigos y False caso contrario.
Dos números son amigos si cada número es igual a la suma de los divisores propios del otro (los 
divisores propios de un número m son los divisores estrictamente menores que m). Por ejemplo, 
los divisores propios de 220 son 1,2,4,5,10,11,20,22, 44, 55 y 110, cuya suma es 284; y los 
divisores propios de 284 son 1,2,4,71 y 142, cuya suma es 220. Luego, 220 y 284 son números 
amigos.
La siguiente función debe ser implementada:
def amigos (a,b):
'''

def amigos(a, b):
    suma_divisores_a = []
    suma_divisores_b = []
    for i in range(1, a):
        # si el resto de a/i es 0, entonces i es divisor de a
        if a % i == 0:
            # acumula la suma de los divisores de a
            suma_divisores_a.append(i)
    # lista con los divisores de a hasta a-1
    suma_a = suma_divisores_a[0:-1]

    for m in suma_a:
        print(m, end=" + ")
    # imprime el ultimo elemento de la lista y agrega la suma de los divisores de a
    print(suma_divisores_a[-1], end = f" = {sum(suma_divisores_a)}")
    # imprime un salto de linea para separar los resultados
    print()
    for i in range(1, b):
        # si el resto de b/i es 0, entonces i es divisor de b
        if b % i == 0:
            # acumula la suma de los divisores de b
            suma_divisores_b.append(i)
    # lista con los divisores de b hasta b-1
    suma_b = suma_divisores_b[0:-1]

    for n in suma_b:
        print(n, end=" + ")
    # imprime el ultimo elemento de la lista y agrega la suma de los divisores de b
    print(suma_divisores_b[-1], end = f" = {sum(suma_divisores_b)}")
    print()

    ## si la suma de los divisores de a es igual a "b" y 
    ## la suma de los divisores de b es igual a "a", entonces son amigos
    if suma_divisores_a == b and suma_divisores_b == a:
        return True
    else:
        return False

    ## si la suma de los divisores de a es igual a "b" y 
    ## la suma de los divisores de b es igual a "a", entonces son amigos
    #return suma_divisores_a == b and suma_divisores_b == a

def main():
    a = int(input("Ingrese el primer numero: "))
    while a < 0:
        print("Ingrese un numero mayor a 0")
        a = int(input("Ingrese el primer numero: "))
    b = int(input("Ingrese el segundo numero: "))
    while b < 0:
        print("Ingrese un numero mayor a 0")
        b = int(input("Ingrese el segundo numero: "))
    print()
    print(amigos(a, b))

main()