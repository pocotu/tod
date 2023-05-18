import time
import matplotlib.pyplot as plt

# Factorial recursivo
def fac_recursivo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fac_recursivo(n - 1) + fac_recursivo(n - 2)

# Factorial iterativo
def fac_iterativo(n):
    f_ant = 0
    f_sig = 1
    for i in range(1, n):
        aux = f_ant
        f_ant = f_sig
        f_sig = f_sig + aux
    return f_sig

ln = []
for i in range(10, 50):
    ln.append(i)

# interativo_times es una lista que almacena los tiempos de ejecución del factorial iterativo
lista_iterativa = []
lista_recursiva = []

print("#### Factorial iterativo ####")
for i in ln:
    tiempo_inicial = time.time()
    fac_iterativo(i)
    tiempo_final = time.time() - tiempo_inicial
    print("El tiempo transcurrido es {:.3f} ms".format(tiempo_final * 1000))
    lista_iterativa.append(tiempo_final)

print("#### Factorial recursivo ####")
for j in ln:
    tiempo_inicial = time.time()
    fac_recursivo(j)
    tiempo_final = time.time() - tiempo_inicial
    print("El tiempo transcurrido es {:.3f} ms".format(tiempo_final * 1000))
    lista_recursiva.append(tiempo_final)

# Plotting the graph
plt.plot(ln, lista_iterativa, label='Factorial Iterativo')
plt.plot(ln, lista_recursiva, label='Factorial Recursivo')
plt.xlabel('n')
plt.ylabel('Tiempo (ms)')
plt.title('Comparación de tiempo de ejecución')
plt.legend()
plt.show()