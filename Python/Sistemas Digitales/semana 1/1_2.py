"""
Dado el siguiente pseudocódigo, escribe los valores que tendrán 
las variables a, b, c y d una vez ejecutado el algoritmo. 
Escribe los valores separados por un espacio en blanco. 
Ejemplo: si el resultado al acabar la ejecución es a=1, b=2, c=23, d=4,
"""

a = 5
b = 2
c = 4
d = 6

if (a>0) and (c > d):
    a = d + c
else:
    a = d * c

c = d + a

if b == c:
    c = c + b
else:
    c = c - a

d = a + b + c

print(a,b,c,d)

# 5 7 14 26
