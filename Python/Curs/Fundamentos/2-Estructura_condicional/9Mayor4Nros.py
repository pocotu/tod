'''
Determinar el mayor de 4 numeros
'''

# Leer datos
print("Ingrese los numeros:")
N1 = int(input('Numero 1: '))
N2 = int(input('Numero 2: '))
N3 = int(input('Numero 3: '))
N4 = int(input('Numero 4: '))

# Intercambiando numeros
if N1 > N2:
    if N1 > N3:
        if N1 > N4:
            Mayor = N1
        else:
            Mayor = N4
    else:
        if N3 > N4:
            Mayor = N3
        else:
            Mayor = N4
else:
    if N2 > N3:
        if N2 > N4:
            Mayor = N2
        else:
            Mayor = N4
    else:
        if N3 > N4:
            Mayor = N3
        else:
            Mayor = N4

print(f'El mayor es {Mayor}')
