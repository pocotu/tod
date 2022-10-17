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
    # recorre todos los numeros desde 1 hasta n
    for a in range(1, n + 1):
        x = 0
        # recorre todos los numeros desde 1 hasta a
        for i in range(1, a):
            # si a es divisible por i, entonces i es divisor de a
            if a % i == 0:
                x += i
        # recorre todos los numeros desde 1 hasta n
        for b in range(1, n + 1):
            y = 0
            # recorre todos los numeros desde 1 hasta b
            for j in range(1, b):
                # si b es divisible por j, entonces j es divisor de b
                if b % j == 0:
                    y += j
            # si a es igual a la suma de los divisores de b y b es igual a la suma de los divisores de a
            if a == y and b == x:
                print(a, b)


def main():
    n = int(input("Introduce un numero: "))
    parejas(n)

main()


