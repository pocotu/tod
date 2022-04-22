from Libreria import *

# Programa recursivo para calcular el numero de digitos
# Modulo numero de digitos
def NroDigitos(x):
    return 1 if x < 10 else 1 +NroDigitos(x//10)

# Modulo Principal
# Leer numeros
Nro = LeerNroEntero('Ingrese un numero: ',0)

# Determinar el numero de digitos
N = NroDigitos(Nro)

# Mostrar resultados
print('El numero de digitos es:',N)
