'''
graficar una funcion ingresada por el usuario
'''
import matplotlib.pyplot as plt
import numpy as np

def funcion(x):
    return x**2+2*x+3

def graficar(funcion, x_min, x_max, n):
    x = np.linspace(x_min, x_max, n)
    y = funcion(x)
    plt.plot(x, y)
    plt.show()

print("Ingrese el valor de x_min: ")
x_min = int(input())
print("Ingrese el valor de x_max: ")
x_max = int(input())
print("Ingrese el valor de n: ")
n = int(input())
graficar(funcion, x_min, x_max, n)









