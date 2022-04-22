'''
Escribir un programa modular para calcular el maximo 
comun divisor de N numeros
'''

# Modulo para determinar el MCD

# Programa principal

def MCD(numero):
    divisores = []

def Divisores(numeros):
    if len(numeros) >= 2:
        r = mcd(numeros[0], numeros[1])
        for n in numeros[2:]:
            r = mcd(r, n)
        return r
    else:
        print('Ingrese mas numeros')
 
nummeros = [12, 20, 38]
result = f(numbers)
print(result) 