"""
Escribir un algoritmo para determinar el mayor de 2 Nros
"""
# Determinar el mayor de dos numeros

# Leer numeros
Nro1 = float(input('Ingresa el primer numero: '))
Nro2 = float(input('Ingresa el segundo numero: '))

# Determinar el mayor
# Suponer que el mayor es el primer numero
Mayor = Nro1

# Comparar con el segundo numero y corregir si es necesario
if Mayor < Nro2:
    Mayor = Nro2

# Mostrar el mayor
print('El mayor es:',Mayor)