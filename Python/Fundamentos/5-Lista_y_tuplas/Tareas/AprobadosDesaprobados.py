from functools import *
from Libreria import *

# *******   Módulos   *****

# -- Módulo para leer las notas
def LeerNotas(N):
    Notas = []
    # -- Poner título
    print()
    print('Ingresar las notas')
    for K in range(0, N):
        Nota = LeerNroReal('Ingresar la nota '+str(K+1)+': ', 0, 20)
        Notas.append(Nota)
    return Notas

# -- Módulo para procesar aprobados
def ProcesarAprobados(Notas):
    print()
    print('PROCESO DE NOTAS APROBADAS')
    NotasA = [Nota for Nota in Notas if Nota >= 13.5]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))
# -- Módulo para procesar desaprobados
def ProcesarDesaprobados(Notas):
    print()
    print('PROCESO DE NOTAS DESAPROBADAS')
    NotasA = [Nota for Nota in Notas if (Nota < 13.5) and (Nota >= 10)]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))
    print('nota mas alta',reduce(lambda x, y : x if x>y else y, Notas))
    print('nota mas baja',reduce(lambda x, y : x if x<y else y, Notas))
# -- Módulo para procesar desaprobados
def ProcesarReprobados(Notas):
    print()
    print('PROCESO DE NOTAS REPROBADAS')
    NotasA = [Nota for Nota in Notas if Nota < 10]
    print('Las notas son: ', NotasA)
    print('El número de notas es: ', len(NotasA))
    if (len(NotasA) > 0):
        Suma = reduce(lambda x, y : x + y, NotasA)
        print('Promedio: ', Suma/len(NotasA))
    
# *******  Programa principal   *****

# -- Poner titulo
print()
print('PROCESAR NOTAS')
# -- Leer el número de alumnos
N = LeerNroEntero('Número de Alumnos: ', 1, 100)
# -- Leer las notas
Notas = LeerNotas(N)
# -- Procesar aprobados
ProcesarAprobados(Notas)
# -- Procesar DESaprobados
ProcesarDesaprobados(Notas)
# -- Procesar reprobados
ProcesarReprobados(Notas)
