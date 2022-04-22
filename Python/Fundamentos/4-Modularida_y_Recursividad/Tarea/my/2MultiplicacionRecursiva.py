from Libreria import *
# Programa recursivo para calcular el producto de dos numeros

# Modulo para calcular la multiplicacion de dos Nros
def Multiplicacion(x,y):
    return 0 if y == 0 else (x + Multiplicacion(x, (y-1)))

# Modulo principal
# Leer numeros
Nro1 = LeerNroEntero('Ingrese el multiplicando: ',0)
Nro2 = LeerNroEntero('Ingrese el multiplicador: ',0)

# Calcular producto
Producto = Multiplicacion(Nro1, Nro2)

# Mostrar el producto
print('El prodcuto es:',Producto)










'''
#MULTIPLICACION RECURSIVA
#  ---- Programa principal
#================AXB==========
# mudula para AXB
def Multiplicacion(N,M):
    if M==0:
        return 0
    else :
        return N + Multiplicacion(N,M-1)
#-----Programa principal 
print('==========leer numero==========')
Nro1=int(input('ingrese el numero 1 : '))
Nro2=int(input('ingrese el numero 2 : '))
#--- importar el moodulo Multiplicar 
factor=Multiplicacion(Nro1,Nro2)
#------mostrar resultado
print(factor)
'''
