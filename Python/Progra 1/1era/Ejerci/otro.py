'''
escribir una funcion recursiva para calcular (n, k) sabiendo que:
(n, k) = (n-1,k) + (n-1,k-1)
(n, n) = 1e (n, 1)= n
'''

def combinaciones(n, k):
    if n == k or k == 1:
        return n
    else:
        # se calcula la combinacion de n y k con la formula (n, k) = (n-1,k) + (n-1,k-1)
        return combinaciones(n-1, k) + combinaciones(n-1, k-1)

def main():
    n = int(input("n: "))
    while n < 1:
        n = int(input("n: "))
    k = int(input("k: "))
    while k < 1 or k > n:
        k = int(input("k: "))
    print(combinaciones(n, k))

main()


def combinacion(n, k):
    if k == 1:
        return n
    elif k == n:
        return 1
    else:
        # se calcula la combinacion de n y k con la formula (n, k) = (n-1,k) + (n-1,k-1)
        return combinacion(n-1, k) + combinacion(n-1, k-1)

def main():
    n = int(input("n1: "))
    while n < 1:
        n = int(input("n1: "))
    k = int(input("k1: "))
    while k < 1 or k > n:
        k = int(input("k1: "))
    print(combinacion(n, k))

main()
