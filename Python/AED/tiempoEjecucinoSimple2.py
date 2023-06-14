import time
#import matplotlib.pyplot as plt

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

ln = [10, 20, 30, 40, 50,
      100, 200, 300, 400, 500,
      1000, 2000, 3000, 5000,
      10000, 20000, 50000, 100000]

print("#### Factorial iterativo ####")
for i in ln:
    tiempo_inicial = time.time()
    print(fac_iterativo(i))
    tiempo_final = time.time() - tiempo_inicial
    print("El tiempo transcurrido es {:.3f} ms".format(tiempo_final * 1000))

print("#### Factorial recursivo ####")
for j in ln:
    tiempo_incial = time.time()
    print(fac_recursivo(j))
    tiempo_final = time.time() - tiempo_inicial
    print("El tiempo transcurrido es {:.3f} ms".format(tiempo_final * 1000))
'''
# Código a medir para el factorial recursivo
tiempo_incial = time.time()
resultado1 = fac_recursivo(20)
tiempo_final = time.time() - tiempo_incial
print("El resultado del factorial recursivo es: {}".format(resultado1))
print("El tiempo de ejecución para el factorial recursivo es: {:.3f} ms".format(tiempo_final * 1000))

# Código a medir para el factorial iterativo
tiempo_incial = time.time()
resultado2 = fac_iterativo(20)
tiempo_final = time.time() - tiempo_incial
print("El resultado del factorial iterativo es: {}".format(resultado2))
print("El tiempo de ejecución para el factorial iterativo es: {:.3f} ms".format(tiempo_final * 1000))
'''

# Gráfica comparativa de los tiempos de ejecución de los dos algoritmos
#plt.plot([1, 2], [tiempo_final, tiempo_final], 'ro-', label='Factorial iterativo')



