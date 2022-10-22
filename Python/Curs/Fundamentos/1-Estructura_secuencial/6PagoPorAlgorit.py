'''
Al mejor estudiante de fundamentos de programación se le incentiva de la siguiente forma:
Por el 1er algoritmo se la paga 1 centavo
Por el 2do algoritmo se la paga 2 centavo
Por el 3er algoritmo se la paga 4 centavo
Por el 4to algoritmo se la paga 8 centavo
Y asi sucesivamente. Escribir un algoritmo que calcule cuanto se le paga al estudiante
'''

# Leer cantidad de ejercicios resueltos
Resueltos = int(input('Ingrese la cantidad de ejercicios resueltos: '))

# Calcular pago
pago = 2**(Resueltos-1)

# Mostrar Pago
print('El pago es: ',pago,'Centavos')