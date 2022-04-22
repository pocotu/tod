# Programa de tablas aritmeticas

from Libreria import *

# ************************  MÓDULOS  **************************
# Menu de tablas Aritmeticas
def Menu():
    print()
    print(' ***** TABLAS ARITMÉTICAS *****')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')
    
# Tabla Aritmetica
def TablaAritmetica(Titulo, Operacion):
    print()
    print('***** TABLA ARITMÉTICA DE '+Titulo+' *****')
    N = LeerNroEntero('Ingrese un número entre 1 y 12:',1,12)
    for K in range(1,13):
        print(Operacion(K, N))


# *******************  PROGRAMA PRINCIPAL  **************************
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        TablaAritmetica('SUMAR', lambda K, N: str(K)+'+'+str(N)+'='+str(K+N))
    elif Opcion == 2:
        TablaAritmetica('RESTAR', lambda K, N: str(K+N)+'-'+str(N)+'='+str(K))
    elif Opcion == 3:
        TablaAritmetica('MULTIPLICAR', lambda K, N: str(K)+'x'+str(N)+'='+str(K*N))
    elif Opcion == 4:
        TablaAritmetica('DIVIDIR', lambda K, N: str(K*N)+'/'+str(N)+'='+str(K))

