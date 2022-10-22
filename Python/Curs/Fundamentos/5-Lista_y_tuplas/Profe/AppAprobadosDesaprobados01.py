from Libreria import *

# *******  Programa principal   *****

# -- Poner titulo
print()
print('PROCESAR NOTAS')
# -- Leer el número de alumnos
N = LeerNroEntero('Número de Alumnos: ', 1, 100)
# -- Leer las notas
Notas = []
for K in range(0, N):
    Notas.append(LeerNroReal('Ingresar la nota '+str(K+1)+':', 0, 20))
# -- Contar número de alumnos aprobados
print('Aprobados:', len([x for x in Notas if x > 13.5 ]))
# -- Contar número de alumnos desaprobados
print('Desaprobados:', len([x for x in Notas if x < 13.5 ]))
