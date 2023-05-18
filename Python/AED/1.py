import time

def codigo_1(numero):
    a = 0
    for j in range(1, numero+1):
        a += a + j

    for k in range(numero, 0, -1):
        a -= 1
        a *= 2
    return a

def codigo_2():
    b = 0
    b -= 1
    b *= 2
    return b

def codigo_3(numero):
    c = 0

    for j in range(1, numero+1):
        for k in range(1, numero * 1):
            c += c + (k*j)
    return c

#########################

# Factorial recursivo
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
# Factorial iterativo
def factorial2(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

# suma de los primeros n numeros
# Suma recursiva
def suma1(n):
    if n == 0:
        return 0
    else:
        return n + suma1(n-1)
    
# Suma iterativa
def suma2(n):
    resultado = 0
    for i in range(1, n+1):
        resultado += i
    return resultado

#########################

# Calcular y medir tiempo para la primera función
t0 = time.time()

primero = codigo_1(6)

# Calcular y medir tiempo para la segunda función
t1 = time.time()

segundo = codigo_2()

# Calcular y medir tiempo para la tercera función
t2 = time.time()

tercero = codigo_3(6)

t3 = time.time()

#######################

# Calcular y medir tiempo para factorial recursivo
t4 = time.time()

fac_1 = factorial(6)

# Calcular y medir tiempo para factorial iterativo
t5 = time.time()

fac_2 = factorial2(6)

#######################

# Calcular y medir tiempo para suma recursiva
t6 = time.time()

fac_3 = suma1(6)

# Calcular y medir tiempo para suma iterativa
t7 = time.time()

fac_4 = suma2(6)

t8 = time.time()


# Mostrar resultados
#print("{}   -   {}".format(suma1, t1-t0))
#print("{}   -   {}".format(suma2, t2-t1))
print("")
print("Primer codigo:       {}".format(t1-t0))
print("Segundo codigo:      {}".format(t2-t1))
print("Tercer codigo:       {}".format(t3-t2))
print("")
print("Factorial recursivo: {}".format(t5-t4))
print("Factorial iterativo: {}".format(t6-t5))
print("")
print("Suma recursiva:      {}".format(t7-t6))
print("Suma iterativa:      {}".format(t8-t7))
print("")






