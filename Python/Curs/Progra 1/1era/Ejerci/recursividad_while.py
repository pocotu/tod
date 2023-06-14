'''
crear una funcion recursiva con bucle while
'''
def factorial(n):
    while n > 1:
        return n * factorial(n - 1)
    return 1

# recursidad con bucle for
def factorial2(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def main():
    n = int(input("Ingrese un numero: "))
    print("El factorial de {} es {} en el bucle while".format(n, factorial(n)))
    print("El factorial de {} es {} en el bucle for".format(n, factorial2(n)))

main()