# Programa de tablas aritmeticas

# Módulo que muestra una línea de asteriscos
from Libreria import *

# Menu de tablas Aritmeticas
def Menu():
    TextoAsteriscos('TABLAS ARITMÉTICAS')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')
    
# Tabla Aritmetica de Sumar
def Sumar(K,N):
    return(str(K)+'+'+str(N)+'='+str(K+N))

# Tabla Aritmetica de Restar
def Restar(K,N):
    return(str(K+N)+'-'+str(N)+'='+str(K))

# Tabla Aritmetica de Multiplicar
def Multiplicar(K,N):
    return(str(K)+'*'+str(N)+'='+str(K*N))
        
# Tabla Aritmetica de Dividir
def Dividir(K,N):
    return(str(K*N)+'/'+str(N)+'='+str(K))

# -- Modulo Procesar
def Procesar(Titulo,Operacion):
    TextoAsteriscos('TABLA ARITMETICA DE '+Titulo)
    # --- Ingresa Nro
    N = LeerNroEntero('Ingresa un Nro. entre 1 y 12: ',1,12)
    # -- Procesar Tabla
    for K in range(1,13):
        print(Operacion(K,N))
    
# Programa principal de Tablas Aritméticas
Opcion = 0;
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        Procesar('SUMAR',Sumar)
    elif Opcion == 2:
        Procesar('RESTAR',Restar)
    elif Opcion == 3:
        Procesar('MULTIPLICAR',Multiplicar)
    elif Opcion == 4:
        Procesar('DIVIDIR',Dividir)
