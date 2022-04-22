# Programa para ilustrar operaciones de números racionales 

#from Libreria import *

# ************************  MÓDULOS  **************************

# ============== Módulo de Números Racionales  ====================
# Módulo Leer Nro racional
def LeerNroRacional(Texto):
    
    print(Texto)
    Numerador = int(input('Ingrese numerador:')) 
    Denominador = int(input('Ingrese denominador:')) 
    while Denominador == 0:
        
        print('ERROR. El denominador no puede ser CERO.')
        Denominador = int(input('Ingrese denominador (Diferente de CERO):'))
    return Simplificar(Numerador, Denominador) 

def EscribirNroRacional(Numerador, Denominador):
    print(Numerador,'/',Denominador)   

# Módulo Simplificar
def Simplificar(A, B):        
    mcd = MCD(A, B)
    return A / mcd, B / mcd
    
# Módulo MCD
def MCD(A, B):        
    Resto = A % B
    while Resto != 0:
        A = B
        B = Resto
        Resto = A % B
    return B        
    
# Módulo de Menú de números racionales
def Menu():
    print()
    print(' ***** OPERACIONES DE NÚMEROS RACIONALES *****')
    print('1 Sumar')
    print('2 Restar')
    print('3 Multiplicar')
    print('4 Dividir')
    print('5 FIN')    
    
# Módulo de Operación Sumar
def Sumar():
    print()
    print('***** Operación Sumar de números racionales *****')
    print('')
    N1, D1 = LeerNroRacional('Ingrese primer número racional')
    N2, D2 = LeerNroRacional('Ingrese segundo número racional')
    N = N1 * D2 + N2 * D1
    D = D1 * D2
    N, D = Simplificar(N, D)
    EscribirNroRacional(N,D)

# Programa Principal del módulo de números racionales
Opcion = 0
while Opcion != 5:
    # Mostrar Menu
    Menu()
    # Leer Opción
    Opcion = int(input('    Ingrese opción -->'))
    if Opcion == 1:
        Sumar()
    elif Opcion == 2:
        Restar()
    elif Opcion == 3:
        Multiplicar()
    elif Opcion == 4:
        Dividir()
