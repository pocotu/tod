from Libreria import *
# Programa recursivo para calcular la enesima potencia de un numper

# Modulo para la n-sima potenci
def EnesimaPotencia(x,y):
    return 1 if y == 0 else x*EnesimaPotencia(x, y-1)

# Modulo principal
# Leer datos
Base = LeerNroEntero('Ingrese multiplicando: ',0)
Exponente = LeerNroEntero('Ingrese el multiplicador: ',0)

# Calcular la n-sima potencia
Potencia = EnesimaPotencia(Base, Exponente)

# Mostrar resultado
print('La n-sima potencia es: ',Potencia)