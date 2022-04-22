# Programa para intercambiar y ordenar dos numeros

# Modulo intercambiar numeros
def Intercambiar(A, B):
    temp = A
    A = B
    B = temp
    return (A, B)

# Modulo para ordenar dos numeros
def OrdenarDos(A,B):
    if A > B:
        A, B = Intercambiar(A, B)
    return(A,B)

# Leer numeros
A = int(input('Ingrese el primer numero: ')) 
B = int(input('Ingrese el segundo numero: '))

# Mostrar numeros intercambiados
print('Numeros intercambiados: ',Intercambiar(A, B))
print('Numeros ordenados: ',OrdenarDos(A, B))