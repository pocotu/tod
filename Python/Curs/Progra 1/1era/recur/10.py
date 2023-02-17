"""
implementar tanto de forma recursiva como iterativa una funcion que
invierta un numero entero positivo
"""

def invertir(n):
    if n < 10:
        return n
    else:
        return (n % 10) * 10 ** (len(str(n)) - 1) + invertir(n // 10)
    
def invertir2(n):
    res = 0
    while n > 0:
        res = res * 10 + n % 10
        n //= 10
    return res

def main():
    n = int(input("ingrese un numero entero positivo: "))
    print("el numero invertido es: ", invertir(n))
    print("el numero invertido es: ", invertir2(n))

main()