'''
hacer triangulo de pascal de n < 20 filas
'''

def pascal(n):
    if n == 0:
        return 1
    else:
        return pascal(n-1) + n*pascal(n-1)

def triangulo(n):
    for i in range(n):
        for j in range(i+1):
            print(pascal(j), end=" ")
        print()

triangulo(int(input('Ingrese un numero: ')))

