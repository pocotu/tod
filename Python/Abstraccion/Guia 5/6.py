'''
Escriba un programa NumPy para calcular la suma de todas las columnas de una
matriz 2D NumPy
'''
import numpy as np

matriz = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
print(matriz)
print(np.sum(matriz, axis=0))

#matriz[:, 1] = np.random.randint(1, int(filas), int(filas))
#print(matriz)
#matriz[:, 2] = np.random.randint(1, int(filas)*2, int(filas))
#print(matriz)
#matriz[:, 3] = np.random.randint(1, int(filas)*3, int(filas))
#print(matriz)
#matriz[:, 4] = np.random.randint(1, int(filas)*4, int(filas))