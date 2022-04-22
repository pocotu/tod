"""
Escribir un algoritmo para determinar el 
Nro de dígitos impares de un Nro entero de 4 digitos.
"""

# Leer un numero entero de tres digitos
Nro = int(input('Ingrese un numero entero de 4 digitos: '))

# Contar el numero de digitos impares
DigImpares = 0

DigImpares = DigImpares + (Nro%2)
Nro = Nro//10

DigImpares = DigImpares + (Nro%2)
Nro = Nro//10

DigImpares = DigImpares + (Nro%2)
Nro = Nro//10

DigImpares = DigImpares + (Nro%2)
Nro = Nro//10

DigPares = 4 - DigImpares
# Escribir el numero de digitos impares
print('Digitos impares: ',DigImpares)
print('Digitos pares: ',DigPares)