
def sumaTotal(n, termino):
    total , k = 0, 1
    while k <= n:
        total, k = total + termino(k), k + 1
    return total

def cubo(x):
    return x*x*x

def sumaCubos(n):
    return sumaTotal(n, cubo)

resultado = sumaCubos(4)
print(resultado)

