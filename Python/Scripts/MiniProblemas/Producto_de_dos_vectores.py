import numpy as np

v=[]
a=int(input("Ingrese el tamaño del vector: "))
for i in range(a):
    i=int(input("Ingrese numero: "))
    v.append(i)

w=[]
b=int(input("Ingrese el tamaño del segundo vector: "))
for j in range(b):
    j=int(input("Ingrese numero: "))
    w.append(j)

print(np.dot(v,w))

