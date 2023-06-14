'''
Escriba un programa NumPy para encontrar la unión de dos matrices. Union
devolverá la matriz única y ordenada de valores que se encuentran en cualquiera
de las dos matrices de entrada
'''

import numpy as np
array1 = np.array([0, 10, 20, 40, 60, 80])
print("Array1: ",array1)
array2 = [10, 30, 40, 50, 70]
print("Array2: ",array2)
print("Matriz única de valores que se encuentran en cualquiera de las dos matrices de entrada:")
print(np.union1d(array1, array2))
