"""
Escribir un algoritmo que dado un numero entero de 3 digitos invierta el orden de sus digitos.
"""

# Leer numero
numero = int(input("Ingrese un numero: "))

# Descomponer numero
D1 = numero//100
D2 = (numero//10)%10
D3 = numero%10

# Invertir numero descompuest0
NumeroInvertido = D3*100+D2*10+D1

# Mostrar numero invertido
print("Numero invertido: ",NumeroInvertido)
