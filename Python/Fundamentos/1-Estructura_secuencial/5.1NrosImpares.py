"""
Escribir un algoritmo para determinar el 
Nro de dígitos impares de un Nro entero de 4 digitos.
"""

# Leer numero entero de 4 digitos
Nro = int(input('Ingrese un numero de 4 digitos: '))

# Descomponer el Nro en D1, D2, D3 y D4
D1 = Nro//1000
D2 = (Nro%1000)//100
D3 = (Nro%100)//10
D4 = Nro%10

# Calcular el Nro de digitos impares
NroDigitosImpares = D1%2 + D2%2 + D3%2 + D4%2

# Mostrar el Nro de digitos impares
print('Digitos impares: ',NroDigitosImpares)