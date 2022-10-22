from Libreria import *

# leer 3 numeros
Nro1 = LeerNroReal('Ingresa numero 1: ',0)
Nro2 = LeerNroReal('Ingresa numero 2: ',0)
Nro3 = LeerNroReal('Ingresa numero 3: ',0)

# Ordenar los numeros
Nro1,Nro2 = OrdenarDos(Nro1,Nro2)
Nro2,Nro3 = OrdenarDos(Nro2,Nro3)
Nro1,Nro2 = OrdenarDos(Nro1,Nro2)

# Mostrar los numeros ordenados
print(Nro1,Nro2,Nro3)