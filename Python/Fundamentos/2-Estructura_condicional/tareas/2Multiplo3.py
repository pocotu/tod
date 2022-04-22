'''
Escribir un algoritmo que lea un número de tres 
dígitos y que determine si alguno de sus dígitos es múltiplo de 3.
'''

# Leer numero de 3 digitos
numero = int(input("Ingrese el numero: "))

# Descomponer en Unidad, Decena y Centena
U = numero%10
D = (numero%100)//10
C = (numero//100)%10

# Determinando y mostrando los numeros multiplos de 3
if U % 3 ==0 and D % 3 == 0 and C % 3 == 0:
    print('Los tres digitos son multiplo de 3')
elif U % 3 ==0 and D % 3 == 0:
    print(D,'y',U,'Son multiplos de 3')
elif U % 3 ==0 and C % 3 == 0:
    print(C,'y',U,'Son multiplos de 3')
elif D % 3 ==0 and C % 3 == 0:
    print(C,'y',D,'Son multiplos de 3')
else:
    print('Ninguno es multiplo de 3')

