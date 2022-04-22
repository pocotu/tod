'''
Dados dos puntos, escribir un algoritmo 
que determine la pendiente entre estos puntos.
'''
# Leer puntos
print('Ingrese los valores de:')
X1 = int(input('X1 = '))
X2 = int(input('X2 = '))
Y1 = int(input('Y1 = '))
Y2 = int(input('Y2 = '))

# Determinando si tiene solucion
Denominador = X2 - X1

# Calculando y mostrando pendiente
if Denominador != 0:
    Pendiente = (Y2 - Y1)/Denominador
    print('Pendiente =',Pendiente)
else:
    print('Indeterminado')