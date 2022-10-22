'''
Escribir un algoritmo que muestre las tablas aricmeticas
de sumar, Restar, Multiplicar y Dividir. El algoritmo debe
utilizar un modulo menu y modulos para cada tabla.
'''

# Módulo que muestra una línea de asteriscos
def Asteriscos(N):
    print('*' * N) #Multiplica por la cantidad de letras

# Módulo que muestra un texto dentro de un recuadro de asteriscos
def TextoAsteriscos(Texto):
    Asteriscos(len(Texto)+4)
    print('* '+Texto+' *')
    Asteriscos(len(Texto)+4)
    print()

# Menu de tablas Aritmeticas
def Menu():
    TextoAsteriscos('TABLAS ARITMÉTICAS')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')
    
# Tabla Aritmetica de Sumar
def Sumar():
    TextoAsteriscos('TABLA ARITMÉTICA DE SUMAR')
    N = int(input('Ingrese un número:'))
    for K in range(1,13):
        print(str(K)+'+'+str(N)+'='+str(K+N))

# Tabla Aritmetica de Restar
def Restar():
    TextoAsteriscos('TABLA ARITMÉTICA DE RESTAR')
    N = int(input('Ingrese un número:'))
    for K in range(1,13):
        print(str(K+N)+'-'+str(N)+'='+str(K))


# Programa principal de Tablas Aritméticas
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        Sumar()
    elif Opcion == 2:
        Restar()
