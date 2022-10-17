"""
Dos números son amigos, si cada uno de ellos es igual a la suma de los divisores del otro.
Hacer una módulo que determine si dos números dados como parámetros son amigos o no. A
continuación realizar un programa que muestre todas las parejas de números amigos menores
o iguales que n, siendo n un número introducido por teclado. El programa debe usar la función
amigo previamente definida. Por ejemplo:

220 y 284 son amigos, ya que:

Suma de divisores de 284: 1 + 2 + 4 + 71 + 142 = 220

Suma de divisores de 220: 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 = 284
"""

# parejas de numeros amigos menores o iguales que n
def parejas(n):
    for a in range(1, n + 1):
        s = 0
        for i in range(1, a):
            if a % i == 0:
                s += i

        for b in range(1, n + 1):
            t = 0
            for j in range(1, b):
                if b % j == 0:
                    t += j

            if a == t and b == s:
                print(a, b)


# crear una funcion para encontrar numeros amigos

    
n = int(input("Ingresa un numero: "))
parejas(n)


