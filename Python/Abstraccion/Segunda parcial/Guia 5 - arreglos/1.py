'''
Escriba un programa NumPy para crear un vector nulo de tamaño 10 y actualice
el sexto valor a 11
'''
import numpy as np
x = np.zeros(10)
print(x)
print("Modificar el sexto valor a 11")
x[6] = 11
print(x)