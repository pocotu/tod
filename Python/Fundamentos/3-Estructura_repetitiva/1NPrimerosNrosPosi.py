'''
Escribir un algoritmo que escriba los N primeros
enteros positivos
'''

# Leer Nro de enteros
N = int(input('Ingresa N: '))

# Mostrar los N primeros numeros
# Algoritmo 1
Nro = 0 
print()
print('Primeros N numeros')
print('==================')
while Nro < N:
    # Mostrar numero
    Nro = Nro + 1
    print('Numero =',Nro)

# Algoritmo 2
"""
Nro = 1
print()
print('Primeros N numeros')
print('==================')
while Nro <= N:
    # Mostrar numero  
    print('Numero =',Nro)
    Nro = Nro + 1
"""