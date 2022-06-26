'''
graficar una derivada de una funcion
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
    return x**2+x*3+3

print("Ingrese el valor de xmin: ")
xmin = int(input())
print("Ingrese el valor de xmax: ")
xmax = int(input())
print("Ingrese el valor de ymin: ")
ymin = int(input())
print("Ingrese el valor de ymax: ")
ymax = int(input())
print("Ingrese el valor de n: ")
n = int(input())
graficar(funcion, xmin, xmax, ymin, ymax, n)


