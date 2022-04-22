'''
Escribir un algoritmo que indique si un Nro es Par o Impar
'''

# Leer Nro
Nro = int(input('Ingrese Nro: '))

# Calcular el residuo
residuo = Nro % 2

# Determinar el Nro es par o impar
if residuo == 0:
    #mensaje = 'Par'
    print('el numero es par')
else:
    #mensaje = 'Impar'
    print('el numero es impar')

# Mostrar resultado
#print('Mensaje=',mensaje)
