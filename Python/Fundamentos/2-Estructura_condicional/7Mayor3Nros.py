'''
Escribir un algoritmo para determinar el mayor de 3
numeros
'''

# Determinar el mayor de tres numeros
# Leer numeros
Nro1 = float(input('Ingresa el primer numero: '))
Nro2 = float(input('Ingresa el segundo numero: '))
Nro3 = float(input('Ingresa el tercer numero: '))

# Determinar el mayor
if Nro1 >= Nro2:
    if Nro1 >= Nro3:
        Mayor = Nro1
    else:
        Mayor = Nro3
else:
    if Nro2 >= Nro3:
        Mayor = Nro2
    else:
        Mayor = Nro3

# Mostrar el mayor
print('El mayor es',Mayor)