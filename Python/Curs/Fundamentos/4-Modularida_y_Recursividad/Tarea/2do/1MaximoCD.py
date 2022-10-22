'''
Escribir un programa modular para calcular el maximo 
comun divisor de N numeros
'''

from Libreria import *

TextoAsteriscos('Ingrese el numero cero "0" para detener el ingreso de numeros')

print()
# Modulo para determinar el MCD

# Modulo para sacar MCD de dos numeros
def MCD(Dividendo, Divisor):
    # Utilizando el algoritmo de Euclides.
    Resto = Dividendo % Divisor if Divisor != 0 else Dividendo
    return Divisor if Resto == 0 else MCD(Divisor, Resto)

# Modulo para sacar MCD mas de dos numeros
def DivisoresNNros(numeros):
    if len(Numeros) >= 2:
        Resto = MCD(Numeros[0], Numeros[1]) #Llamando a modulo MCD 
        for n in Numeros[2:]:
            Resto = MCD(Resto, n)#Probando valores hasta optener 0 como resto
        return Resto
 
# Agregando numeros
Numeros = []
Temporal = int(input('Ingrese numero: '))
while Temporal != 0:
    Numeros.append(Temporal)
    Temporal = int(input('Ingrese numero: '))

# Programa principal
Resultado = DivisoresNNros(Numeros)

# Mostrando resultado
print('El Maximo comundo divisor es:',Resultado)