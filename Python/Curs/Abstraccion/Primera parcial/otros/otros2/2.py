'''
graficar una funcion
'''

def graficar(funcion, xmin, xmax, ymin, ymax, n):
    import matplotlib.pyplot as plt
    import numpy as np
    x = np.linspace(xmin, xmax, n)
    y = funcion(x)
    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.show()

def funcion(x):
    return x**2

print("Ingrese el valor de xmin: ")