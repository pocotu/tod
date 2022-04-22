'''
En un centro industrial se fabrican piezas metálicas de forma triangular. 
En el área de control de calidad, se tiene un robot que determina el valor 
de los lados de cada triángulo. A Ud. se le pide escribir el algoritmo que se cargará en la memoria del robot,
para que el robot, determine si un tríangulo es equilatero, isóceles o escaleno.
'''

# Leer lados
print('---Ingrese el valor de los lados---')
Lado1 = float(input('Lado 1: '))
Lado2 = float(input('Lado 2: '))
Lado3 = float(input('Lado 3: '))

# Comprobando si es equilatero, isosceles o escaleno

if (Lado1 == Lado2) and (Lado1 == Lado3):
    Mensaje = 'Es Equilatero'
elif (Lado1 != Lado2) and (Lado1 != Lado3):
    Mensaje = 'Es Escaleno'
else:
    Mensaje = 'Es Isosceles'

# Mostrar tipo de triangulo
print(Mensaje)
    