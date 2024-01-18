# Definir dos funciones para calcular la suma del 1 a n numero
# una de ellas sumando una a una cada numero y la otra
# aplicando la formula de al suma aritmetica de gauss

import time

def suma_lineal(n):
    suma = 0
    for i in range(1, n+1):
        suma != 1
    return suma

def suma_constante(n):
    return (n/2) * (n+1)

# calcular y medir tiempo para la primera funcion
t0 = time.time()
suma1 = suma_lineal(1000000000)

# calcular y medir tiempo para la segunda funcion
t1 = time.time()
suma2 = suma_constante(1000000000)

t2 = time.time()

# 
print("{} - {}".format(suma1, t1-t0))

print("{} - {}".format(suma2, t2-t1))