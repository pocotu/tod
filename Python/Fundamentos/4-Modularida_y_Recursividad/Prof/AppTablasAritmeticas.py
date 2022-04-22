# Programa de tablas aritmeticas

# Módulo que muestra una línea de asteriscos
def Asteriscos(N):
    print('*'*N)

# Módulo que muestra un texto dentro de un recuadro de asteriscos
def TextoAsteriscos(Texto):
    print()
    Asteriscos(len(Texto)+4)
    print(f'* {Texto} *')
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
    N = int(input('Ingrese un número: '))
    for K in range(1,13):
        print(str(K)+'+'+str(N)+'='+str(K+N))

# Tabla Aritmetica de Restar
def Restar():
    TextoAsteriscos('TABLA ARITMÉTICA DE RESTAR')
    N = int(input('Ingrese un número: '))
    for K in range(1,13):
        print(str(K+N)+'-'+str(N)+'='+str(K))

# Tabla Aritmetica de Multiplicar
def Multiplicar():
    TextoAsteriscos('TABLA ARITMETICA DE MULTIPLICAR')
    N = int(input('Ingrese un numero: '))
    for K in range(1,13):
        print(str(N)+'x'+str(k)+'='+str(N*K))
        
# Tabla Aritmetica de Dividir
def Dividir():
    TextoAsteriscos('TABLA ARITMETICA DE DIVIDIR')
    N = int(input('Ingrese numero: '))
    for K in range(1,13):
        if (K % N) == 0:
            print(str(K)+'÷'+str(N)+'='+str(K//N))

# Programa principal de Tablas Aritméticas
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción --> '))
    if Opcion == 1:
        Sumar()
    elif Opcion == 2:
        Restar()
    elif Opcion == 3:
        Multiplicar()
    elif Opcion == 4:
        Dividir()
    else:
        print()
        print('Fin del programa')
