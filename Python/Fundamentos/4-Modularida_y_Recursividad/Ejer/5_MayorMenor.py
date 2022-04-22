# Programa para determinar el mayor de cuatro números

# Módulo para determinar el mayor de dos números
def MayorDos(A, B):
    return A if A > B else B

# Programa principal 
# -- Leer los números
Nro1 = float(input('Ingrese el primer número: '))
Nro2 = float(input('Ingrese el segundo número: '))
Nro3 = float(input('Ingrese el tercer número: '))
Nro4 = float(input('Ingrese el cuarto número: '))
# -- Determinar el mayor
Mayor1 = MayorDos(Nro1, Nro2)
Mayor2 = MayorDos(Nro3, Nro4)
Mayor = MayorDos(Mayor1, Mayor2)
# -- Mostrar el mayor
print('El mayor es: '+str(Mayor))