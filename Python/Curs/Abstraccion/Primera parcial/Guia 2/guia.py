### Asignación de variables en Python ###

#definimos cuadrado de un numero
def cuadrado(x):
    return x**2
#almacenamos el nombre de la funcion en la variable cuadrado
m=cuadrado
#Procesamos
print(m(7))

##MODULOS
##MODULO PARA SUMA DE DOS NUMEROS
def suma(a, b):
    return a+b
##MODULO PARA RESTA DE DOS NUMEROS
def resta(a, b):
    return a-b
##MODULO PARA MULTIPLICACION DE DOS NUMEROS
def multiplicacion(a, b):
    return a*b
##MODULO PARA OPERAR
def operar(a, b, f):
    return f(a, b)
#####################################
##PRINCIPAL
print(operar(6, 5, suma))
print(operar(6, 5, resta))
print(operar(5, 6, multiplicacion))

######################################################
def dobleSuma(a,b,f):
    return f(f(a,b),7)
print(dobleSuma(2,3,suma))