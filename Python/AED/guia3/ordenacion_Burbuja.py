# Importar la libreria para generar numeros aleatorios
import random
# Importar la libreria para utilizar el temporizador
import time
# Importar la libreria para graficar
import matplotlib.pyplot as plt

# Comparacion de la Eficiencia del metodo de Burbuja
def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(0, n-1):
        for j in range(n-1):
            if(lista[j]>lista[j+1]):
                temp1 = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp1
                # lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def ordenamiento_burbuja_optimizado1(lista):
    n = len(lista)
    intercambio = True

    while (intercambio):
        intercambio = False
        for i in range(n-1):
            if (lista[i] > lista[i+1]):
                temp1 = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp1
                #lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
    return lista

def ordenamiento_burbuja_optimizado2(lista):
    n = len(lista)
    intercambio = True
    iteracion = 0

    while (intercambio):
        intercambio = False
        for i in range(n - iteracion - 1):
            if (lista[i] > lista[i+1]):
                temp1 = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = temp1
                #lista[j], lista[j+1] = lista[j+1], lista[j]
                intercambio = True
        iteracion += 1
    #print("Numero de iteracion: ", iteracion)
    return lista

######################
# Programa principal #
######################

# Numero de elementos de lista
n = 0

# Inicializamos la lista
A = []

# Tiempos de burbujas
tiempos_burbuja = []
tiempos_burbuja_opt1 = []
tiempos_burbuja_opt2 = []
# Lista de elementos de la lista A
elementos = []



print("\ntBurbuja 1\t\tBurbuja 2\t\tBurbuja 3")
for iteracion in range(5):
    # Generamos una lista con "n" elementos aleatorios
    for i in range(n):
        A.append(random.randint(1, 100))

    # Medir tiempo Burbuja simple
    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja(B)
    t1 = time.time()
    tiempo1 = t1 - t0

    # Medir tiempo Burbuja optimnizado 1
    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja_optimizado1(B)
    t1 = time.time()
    tiempo2 = t1 - t0

    # Medir tiempo Burbuja optimizado 2
    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja_optimizado2(B)
    t1 = time.time()
    tiempo3 = t1 - t0

    # Mostrar resultados
    print(n, "\t", tiempo1,"\t", tiempo2, "\t", tiempo3)

    tiempos_burbuja.append(tiempo1)
    tiempos_burbuja_opt1.append(tiempo2)
    tiempos_burbuja_opt2.append(tiempo3)
    elementos.append(n)

    n = n + 300


'''

for iteracion in range(5):
    for i in range(n):
        A.append(random.randint(1, 100))

    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja(B)
    t1 = time.time()
    tiempo1 = t1 - t0

    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja_optimizado1(B)
    t1 = time.time()
    tiempo2 = t1 - t0

    B = A.copy()
    t0 = time.time()
    ordenamiento_burbuja_optimizado2(B)
    t1 = time.time()
    tiempo3 = t1 - t0

    tiempos_burbuja.append(tiempo1)
    tiempos_burbuja_opt1.append(tiempo2)
    tiempos_burbuja_opt2.append(tiempo3)
    elementos.append(n)

    n = n + 300
'''
# Generar gráfico
plt.plot(elementos, tiempos_burbuja, label="Burbuja 1")
plt.plot(elementos, tiempos_burbuja_opt1, label="Burbuja 2")
plt.plot(elementos, tiempos_burbuja_opt2, label="Burbuja 3")
plt.xlabel('Número de elementos')
plt.ylabel('Tiempo (segundos)')
plt.title('Comparación de eficiencia de los métodos de burbuja')
plt.legend()
plt.show()