'''
Escribir un algoritmo para ordenar 2 Nros en Ascendente
'''

# Leer numeros
Nro1 = float(input('Ingresa el primer numero: '))
Nro2 = float(input('Ingresa el segundo numero: '))

# Determina el mayor
if Nro1 >= Nro2:
    # Intercambiar los numeros
    Temp = Nro1
    Nro1 = Nro2
    Nro2 = Temp

# Mostrar el mayor
print('Mostrar los nros, ordenados:',Nro1,',',Nro2)
