'''
Escriba un programa NumPy para encontrar la diferencia de conjunto de dos
matrices. La diferencia establecida devolverá los valores únicos ordenados en
matriz1 que no están en matriz2.
'''

import numpy as np

array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Unicos valores que están en el arreglo uno y no en el arreglo dos:")
print(np.setdiff1d(array1, array2))
