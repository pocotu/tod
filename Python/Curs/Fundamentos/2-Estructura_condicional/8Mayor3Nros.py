'''
Determinar le mayor de tres numeros
'''

# Leer numeros
print('Ingrese los numeros:')
N1 = int(input('Numero 1'))
N2 = int(input('Numero 2'))
N3 = int(input('Numero 3'))
N4 = int(input('Numero 4'))

# Determinar el mayor del primer y segundo numero
if N1 >= N2:
    Mayor = N1
else:
    Mayor = N2

# Determinar el mayor del mayor anterior y el tercer numero
if Mayor <= N3:
    Mayor = N3

# Mostrar el mayor
print('El mayor es',Mayor)