'''
Escribir un algoritmo que permita resolver un sistema de dos ecuaciones lineales:
AX + BY = C
DX + EY = F
'''

# Leer valores
print('Ingrese los valores de:')
A = float(input('A: '))
B = float(input('B: '))
C = float(input('C: '))
D = float(input('D: '))
E = float(input('E: '))
F = float(input('F: '))

# Determinando si tiene solucion
Determinante = A*E - B*D

# Determinado y mostrando el valor de X y Y
if Determinante != 0:
    X = (C*E - B*F)/Determinante
    Y = (A*F - C*D)/Determinante
    print('X =',X)
    print('Y =',Y)
else:
    print('No tiene solucion la ecuacion')

